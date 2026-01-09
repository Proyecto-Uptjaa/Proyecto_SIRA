import re
from models.registro_base import RegistroBase
from ui_compiled.ficha_estu_ui import Ui_ficha_estu
from PySide6.QtWidgets import QDialog, QMessageBox, QMenu, QToolButton, QInputDialog, QTableWidgetItem
from PySide6.QtCore import QDate, Signal
from PySide6.QtGui import QStandardItemModel, QStandardItem
from models.repre_model import RepresentanteModel
from models.estu_model import EstudianteModel
from models.institucion_model import InstitucionModel
from utils.widgets import Switch
from utils.exportar import (
    generar_constancia_estudios, generar_buena_conducta,
    generar_constancia_inscripcion, generar_constancia_prosecucion_inicial,
    generar_constancia_retiro
)
from utils.sombras import crear_sombra_flotante
from utils.forms import ajustar_columnas_tabla
from utils.forms import set_campos_editables
from utils.dialogs import crear_msgbox
from utils.archivos import abrir_archivo
from datetime import datetime, date
import os
from utils.edad import calcular_edad


class DetallesEstudiante(QDialog, Ui_ficha_estu):
    """
    Ventana de detalles completos de un estudiante.
    
    Funcionalidades:
    - Visualización y edición de datos personales
    - Gestión de representante
    - Cambio de estado (activo/inactivo)
    - Historial académico completo
    - Devolución de grado (repitencia)
    - Exportación de constancias
    - Eliminación de registro
    
    Soporta dos modos:
    - Estudiante regular: edición completa, asignación a secciones
    - Egresado: solo lectura, muestra datos históricos
    """
    
    # Señal emitida cuando se modifican datos (para refrescar tablas padre)
    datos_actualizados = Signal()

    def __init__(self, id_estudiante, usuario_actual, año_escolar, es_egresado=False, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.año_escolar = año_escolar
        self.es_egresado = es_egresado
        self.setupUi(self)

        self.setWindowTitle("Ficha de estudiante")
        self.id = id_estudiante
        self.id_estudiante = id_estudiante
        self.stackFicha_estu.setCurrentIndex(0)
        
        # Inicializar lista de delegates para tooltips
        self.tooltip_delegates = []
        
        # Variable para evitar bucles en las señales del switch
        self.actualizando_switch = False
        
        # Inicializar diccionarios vacíos para evitar errores
        self.grados_por_nivel = {}
        self.secciones_por_grado = {}
        
        # Cargar secciones desde la BD (solo si NO es egresado)
        if not self.es_egresado:
            self.cargar_secciones_en_combos()
            # Conectar señales de combos en cascada (nivel → grado → sección)
            self.cbxTipoEdu_ficha_estu.currentIndexChanged.connect(self.actualizar_grado)
            self.cbxGrado_ficha_estu.currentTextChanged.connect(self.actualizar_seccion)
        
        # Cargar datos del estudiante y su historial
        self.cargar_datos()
        self.cargar_historial()
        
        # Inicializar el switch de estado después de cargar datos
        self.switchActivo = Switch()
        self.switchActivo.setFixedSize(50, 25)
        self.contenedorSwitch.layout().addWidget(self.switchActivo)

        # Establecer el estado inicial del switch sin disparar eventos
        self.actualizando_switch = True
        # Estado=1 (activo) -> Checked(True) verde
        # Estado=0 (inactivo) -> Checked(False) gris
        self.switchActivo.setChecked(bool(self.estudiante_actual.get("Estado", 1)))
        self.actualizando_switch = False

        # Configurar visibilidad según tipo (egresado vs regular)
        self.configurar_visibilidad_campos()
        
        # Conectar señales de botones de navegación
        self.btnStudentDatos_ficha.clicked.connect(lambda: self.cambiar_pagina_ficha_estudiante(0))
        self.btnRepre_ficha.clicked.connect(lambda: self.cambiar_pagina_ficha_estudiante(1))
        self.btnHistorial_estu.clicked.connect(lambda: self.cambiar_pagina_ficha_estudiante(2))
        
        # Conectar señales de botones de acción
        self.btnModificar_ficha_estu.clicked.connect(self.toggle_edicion)
        self.btnDevolver_grado.clicked.connect(self.devolver_estudiante)
        self.btnEliminar_ficha_estu.clicked.connect(self.eliminar_estudiante)

        self.configurar_menu_exportacion()
        
        # Conectar señales de fechas para cálculo automático de edad
        self.lneFechaNac_ficha_estu.dateChanged.connect(self.actualizar_edad_estudiante)
        self.lneFechaNac_repre_ficha_estu.dateChanged.connect(self.actualizar_edad_representante)
              
        # Bloquear campos y configurar estado inicial (modo lectura)
        self.set_campos_editables(False)
        self.lneCedula_repre_ficha_estu.setReadOnly(True)
        self.lneCedula_ficha_estu.setReadOnly(True)
        
        # Conectar la señal del switch después de establecer el estado inicial
        self.switchActivo.stateChanged.connect(self.cambiar_estado_estudiante)

        # Aplicar efectos visuales (sombras flotantes)
        self.aplicar_sombras()
    
    def configurar_menu_exportacion(self):
        """Configura el menú desplegable de exportación"""
        self.btnExportar_ficha_estu.setPopupMode(QToolButton.InstantPopup)
        menu_exportar_estu = QMenu(self.btnExportar_ficha_estu)
        
        # Agregar opciones de exportación
        menu_exportar_estu.addAction("Constancia de estudios", self.exportar_constancia_estudios)
        menu_exportar_estu.addAction("Constancia de buena conducta", self.exportar_buena_conducta)
        menu_exportar_estu.addAction("Constancia de inscripción", self.exportar_constancia_inscripcion)
        menu_exportar_estu.addAction("Constancia prosecución Educación Inicial", 
                                     self.exportar_constancia_prosecucion_inicial)
        menu_exportar_estu.addAction("Constancia de retiro", self.exportar_constancia_retiro)
        
        self.btnExportar_ficha_estu.setMenu(menu_exportar_estu)
    
    def obtener_estudiante_actual_dict(self):
        """Convierte los datos del formulario en dict compatible con exportar.py"""
        return {
            "ID": str(self.id_estudiante),
            "Cédula": self.lneCedula_ficha_estu.text().strip(),
            "Nombres": self.lneNombre_ficha_estu.text().strip(),
            "Apellidos": self.lneApellido_ficha_estu.text().strip(),
            "Fecha Nac.": self.lneFechaNac_ficha_estu.date().toPython(),
            "Edad": self.lneEdad_ficha_estu.text().strip(),
            "Ciudad": self.lneCity_ficha_estu.text().strip(),
            "Género": self.cbxGenero_ficha_estu.currentText().strip(),
            "Dirección": self.lneDir_ficha_estu.text().strip(),
            "Fecha Ingreso": self.lneFechaIng_ficha_estu.date().toPython(),
            "Tipo Educ.": self.cbxTipoEdu_ficha_estu.currentText().strip() if not self.es_egresado else "",
            "Grado": self.cbxGrado_ficha_estu.currentText().strip() if not self.es_egresado else "",
            "Sección": self.cbxSeccion_ficha_estu.currentText().strip() if not self.es_egresado else "",
            "Docente": self.lneDocente_ficha_estu.text().strip(),
        }

    def exportar_constancia_estudios(self):
        """Genera constancia de estudios"""
        try:
            estudiante = self.obtener_estudiante_actual_dict()
            institucion = InstitucionModel.obtener_por_id(1)
            archivo = generar_constancia_estudios(estudiante, institucion)
            crear_msgbox(self, "Éxito", f"Constancia generada:\n{archivo}", QMessageBox.Information).exec()
            abrir_archivo(archivo)
        except Exception as e:
            crear_msgbox(self, "Error", f"No se pudo generar:\n{e}", QMessageBox.Critical).exec()

    def exportar_constancia_inscripcion(self):
        """Genera constancia de inscripción"""
        try:
            estudiante = self.obtener_estudiante_actual_dict()
            institucion = InstitucionModel.obtener_por_id(1)
            archivo = generar_constancia_inscripcion(estudiante, institucion)
            crear_msgbox(self, "Éxito", f"Constancia generada:\n{archivo}", QMessageBox.Information).exec()
            abrir_archivo(archivo)
        except Exception as e:
            crear_msgbox(self, "Error", f"No se pudo generar:\n{e}", QMessageBox.Critical).exec()

    def exportar_buena_conducta(self):
        """Genera constancia de buena conducta"""
        try:
            estudiante = self.obtener_estudiante_actual_dict()
            institucion = InstitucionModel.obtener_por_id(1)
            archivo = generar_buena_conducta(estudiante, institucion, self.año_escolar)
            crear_msgbox(self, "Éxito", f"Constancia generada:\n{archivo}", QMessageBox.Information).exec()
            abrir_archivo(archivo)
        except Exception as e:
            crear_msgbox(self, "Error", f"No se pudo generar:\n{e}", QMessageBox.Critical).exec()

    def exportar_constancia_prosecucion_inicial(self):
        """Genera constancia de prosecución"""
        grado_actual = self.cbxGrado_ficha_estu.currentText().strip()
        if grado_actual != "1ero":
            crear_msgbox(self, "Estudiante no válido", 
                f"Solo para 1er grado. Está en: {grado_actual}", QMessageBox.Warning).exec()
            return
        
        try:
            historial = EstudianteModel.obtener_historial_estudiante(self.id_estudiante)
            if not historial:
                crear_msgbox(self, "Sin historial", "No hay historial.", QMessageBox.Warning).exec()
                return
            
            año_anterior = self.año_escolar['anio_inicio'] - 1
            curso_inicial = any(
                '3' in r['grado'].lower() and 
                r['nivel'].lower() in ['inicial', 'preescolar'] and 
                r['año_inicio'] == año_anterior 
                for r in historial
            )
            
            if not curso_inicial:
                crear_msgbox(self, "No elegible", 
                    f"No cursó 3er nivel inicial en {año_anterior}-{año_anterior+1}", 
                    QMessageBox.Warning).exec()
                return
            
            estudiante = self.obtener_estudiante_actual_dict()
            institucion = InstitucionModel.obtener_por_id(1)
            archivo = generar_constancia_prosecucion_inicial(estudiante, institucion, self.año_escolar)
            crear_msgbox(self, "Éxito", f"Constancia generada:\n{archivo}", QMessageBox.Information).exec()
            abrir_archivo(archivo)
        except Exception as e:
            crear_msgbox(self, "Error", f"No se pudo generar:\n{e}", QMessageBox.Critical).exec()
    
    def exportar_constancia_retiro(self):
        """Genera constancia de retiro"""
        # Verificar si el estudiante está inactivo
        if self.estudiante_actual.get("Estado", 1) == 1:
            crear_msgbox(
                self,
                "Estudiante activo",
                "La constancia de retiro solo se puede generar para estudiantes retirados (inactivos).\\n\\n"
                "Use el switch para marcar al estudiante como retirado primero.",
                QMessageBox.Warning
            ).exec()
            return
        
        try:
            # Obtener motivo de retiro desde la BD
            datos = EstudianteModel.obtener_por_id(self.id_estudiante)
            motivo_retiro = datos.get("motivo_retiro") if datos else None
            
            estudiante_dict = self.obtener_estudiante_actual_dict()
            institucion = InstitucionModel.obtener_por_id(1)
            
            archivo = generar_constancia_retiro(
                estudiante_dict,
                institucion,
                self.año_escolar,
                motivo_retiro
            )
            
            crear_msgbox(
                self,
                "Éxito",
                f"Constancia de retiro generada:\\n{archivo}",
                QMessageBox.Information
            ).exec()
            
            abrir_archivo(archivo)
            
        except Exception as e:
            crear_msgbox(
                self,
                "Error",
                f"No se pudo generar la constancia: {e}",
                QMessageBox.Critical
            ).exec()
    
    def aplicar_sombras(self):
        """Aplica efectos de sombra a los elementos de la interfaz"""
        crear_sombra_flotante(self.btnModificar_ficha_estu)
        crear_sombra_flotante(self.btnExportar_ficha_estu)
        crear_sombra_flotante(self.btnEliminar_ficha_estu)
        crear_sombra_flotante(self.btnRepre_ficha)
        crear_sombra_flotante(self.btnStudentDatos_ficha)
        crear_sombra_flotante(self.lneCedula_ficha_estu, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.frameTabla_student, blur_radius=5, y_offset=1)

    def cargar_secciones_en_combos(self):
        """
        Carga las secciones activas del año escolar actual en los combos.
        Organiza las secciones jerárquicamente: nivel → grado → letra
        """
        año = self.año_escolar['anio_inicio']
        secciones = EstudianteModel.obtener_secciones_activas(año)
        
        # Limpiar combos existentes
        self.cbxTipoEdu_ficha_estu.clear()
        self.cbxGrado_ficha_estu.clear()
        self.cbxSeccion_ficha_estu.clear()
        
        # Estructuras para organizar datos jerárquicamente
        niveles = set()
        self.grados_por_nivel = {}
        self.secciones_por_grado = {}
        
        # Procesar cada sección y organizarla
        for sec in secciones:
            nivel = sec["nivel"]
            grado = sec["grado"]
            letra = sec["letra"]
            
            # Agregar nivel único
            if nivel not in niveles:
                niveles.add(nivel)
                self.cbxTipoEdu_ficha_estu.addItem(nivel)
            
            # Agrupar grados por nivel
            if nivel not in self.grados_por_nivel:
                self.grados_por_nivel[nivel] = set()
            self.grados_por_nivel[nivel].add(grado)
            
            # Agrupar secciones por combinación nivel_grado
            clave = f"{nivel}_{grado}"
            if clave not in self.secciones_por_grado:
                self.secciones_por_grado[clave] = []
            self.secciones_por_grado[clave].append({
                "letra": letra,
                "id": sec["id"]
            })
    
    def actualizar_grado(self):
        """
        Actualiza el combo de grados según el nivel seleccionado.
        Llamado automáticamente al cambiar el nivel educativo.
        """
        t_educacion = self.cbxTipoEdu_ficha_estu.currentText()
        
        # Limpiar combo de grado
        self.cbxGrado_ficha_estu.clear()
        
        if not t_educacion:
            self.cbxGrado_ficha_estu.setEnabled(False)
            self.cbxSeccion_ficha_estu.clear()
            self.cbxSeccion_ficha_estu.setEnabled(False)
            return
        
        # Cargar grados disponibles para este nivel
        grados = sorted(self.grados_por_nivel.get(t_educacion, set()))
        if grados:
            for g in grados:
                self.cbxGrado_ficha_estu.addItem(g)
            self.cbxGrado_ficha_estu.setEnabled(True)
            
            # Actualizar secciones si hay un grado seleccionado por defecto
            grado_actual = self.cbxGrado_ficha_estu.currentText()
            if grado_actual:
                self.actualizar_seccion(grado_actual)
        else:
            self.cbxGrado_ficha_estu.setEnabled(False)
            self.cbxSeccion_ficha_estu.clear()
            self.cbxSeccion_ficha_estu.setEnabled(False)
    
    def actualizar_seccion(self, grado):
        """
        Actualiza el combo de secciones según nivel y grado seleccionados.
        
        Args:
            grado: Grado seleccionado (ej: "1ero", "2do")
        """
        nivel = self.cbxTipoEdu_ficha_estu.currentText()
        if not nivel or not grado:
            self.cbxSeccion_ficha_estu.clear()
            self.cbxSeccion_ficha_estu.setEnabled(False)
            return
        
        # Buscar secciones para esta combinación nivel-grado
        clave = f"{nivel}_{grado}"
        self.cbxSeccion_ficha_estu.clear()
        opciones = self.secciones_por_grado.get(clave, [])
        
        if opciones:
            for opt in opciones:
                # Guardar ID de sección como userData
                self.cbxSeccion_ficha_estu.addItem(opt["letra"], opt["id"])
            self.cbxSeccion_ficha_estu.setEnabled(True)
        else:
            self.cbxSeccion_ficha_estu.setEnabled(False)
    
    def cambiar_estado_estudiante(self, state):
        """
        Maneja el cambio de estado del estudiante (activo/inactivo).
        Requiere confirmación del usuario y registra en auditoría.
        
        Args:
            state: Estado del switch (2=checked/activo, 0=unchecked/inactivo)
        """
        # Evitar bucles infinitos durante actualizaciones programáticas
        if self.actualizando_switch:
            return
        
        self.actualizando_switch = True

        # Convertir estado del switch a valor de BD
        # Checked=2 (verde) → Estado 1 (activo)
        # Unchecked=0 (gris) → Estado 0 (inactivo)
        nuevo_estado = 1 if state == 2 else 0
        estado_actual = int(self.estudiante_actual.get("Estado", 1))
        
        # No hacer nada si el estado no cambió
        if nuevo_estado == estado_actual:
            self.actualizando_switch = False
            return

        # Texto para mensajes
        texto = "activar" if nuevo_estado else "desactivar"

        # Solicitar confirmación
        msg = crear_msgbox(
            self,
            "Confirmar acción",
            f"¿Seguro que deseas {texto} a este estudiante?",
            QMessageBox.Question,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if msg.exec() == QMessageBox.StandardButton.Yes:
            motivo_retiro = None
            
            # Si se está inactivando (retirando), pedir motivo
            if nuevo_estado == 0:
                motivo_retiro, ok_motivo = QInputDialog.getText(
                    self,
                    "Motivo de retiro",
                    "Ingrese el motivo del retiro del estudiante:\n(Opcional, presione Cancelar para usar motivo predeterminado)",
                    text="es retirado de la institución a solicitud de su representante siendo Promovido al siguiente grado"
                )
                
                # Si canceló, usar el motivo predeterminado
                if not ok_motivo or not motivo_retiro.strip():
                    motivo_retiro = "es retirado de la institución a solicitud de su representante siendo Promovido al siguiente grado"
                else:
                    motivo_retiro = motivo_retiro.strip()
            
            try:
                # Ejecutar cambio en BD
                base = RegistroBase()
                ok, mensaje = base.cambiar_estado(
                    "estudiantes", 
                    self.id, 
                    nuevo_estado, 
                    self.usuario_actual
                )

                if ok:
                    # Si fue retiro, guardar motivo y fecha
                    if nuevo_estado == 0 and motivo_retiro:
                        from utils.db import get_connection
                        from datetime import date
                        
                        conn = get_connection()
                        if conn:
                            try:
                                cursor = conn.cursor()
                                cursor.execute(
                                    "UPDATE estudiantes SET motivo_retiro = %s, fecha_retiro = %s WHERE id = %s",
                                    (motivo_retiro, date.today(), self.id)
                                )
                                conn.commit()
                                cursor.close()
                            except Exception as e:
                                print(f"Error guardando motivo de retiro: {e}")
                            finally:
                                if conn.is_connected():
                                    conn.close()
                    
                    # Actualizar estado local
                    self.estudiante_actual["Estado"] = nuevo_estado
                    self.lblEstado_ficha_estu.setText("Activo" if nuevo_estado else "Inactivo")
                    
                    # Emitir señal para actualizar tablas padre
                    self.datos_actualizados.emit()
                    
                    dlg = crear_msgbox(
                        self,
                        "Éxito",
                        f"Estudiante {texto}do correctamente.",
                        QMessageBox.Information,
                    )
                    dlg.exec()
                else:
                    dlg = crear_msgbox(
                        self,
                        "Error",
                        f"No se pudo {texto} al estudiante: {mensaje}",
                        QMessageBox.Critical,
                    )
                    dlg.exec()
                    self.revertir_switch()

            except Exception as e:
                print(f"Excepción al cambiar estado: {str(e)}")
                dlg = crear_msgbox(
                    self,
                    "Error",
                    f"Error inesperado: {str(e)}",
                    QMessageBox.Critical,
                )
                dlg.exec()
                self.revertir_switch()
        else:
            # Usuario canceló: revertir switch
            self.revertir_switch()
        
        self.actualizando_switch = False
    
    def revertir_switch(self):
        """Revierte el switch a su estado anterior sin disparar eventos"""
        self.actualizando_switch = True
        estado = self.estudiante_actual.get("Estado", 1) == 1
        self.switchActivo.setChecked(estado)
        self.lblEstado_ficha_estu.setText("Activo" if estado else "Inactivo")
        self.actualizando_switch = False

    def actualizar_edad_estudiante(self):
        """Calcula y muestra la edad del estudiante al cambiar su fecha de nacimiento"""
        fecha_nac = self.lneFechaNac_ficha_estu.date().toPython()
        
        # Validar que no sea fecha futura
        if fecha_nac > date.today():
            self.lneEdad_ficha_estu.setText("0")
            return
        
        edad = calcular_edad(fecha_nac)
        self.lneEdad_ficha_estu.setText(str(edad))

    def actualizar_edad_representante(self):
        """Calcula y muestra la edad del representante al cambiar su fecha de nacimiento"""
        fecha_nac = self.lneFechaNac_repre_ficha_estu.date().toPython()
        
        # Validar que no sea fecha futura
        if fecha_nac > date.today():
            self.lneEdad_repre_ficha_estu.setText("0")
            return
        
        edad = calcular_edad(fecha_nac)
        self.lneEdad_repre_ficha_estu.setText(str(edad))
    
    def cambiar_pagina_ficha_estudiante(self, indice):
        """
        Cambia entre las páginas del stack.
        
        Args:
            indice: 0=Datos estudiante, 1=Representante, 2=Historial
        """
        self.stackFicha_estu.setCurrentIndex(indice)

    def set_campos_editables(self, estado: bool):
        """
        Habilita/deshabilita la edición de campos del formulario.
        
        Args:
            estado: True para habilitar edición, False para bloquear
        """
        # Campos editables del estudiante
        campos = [
            self.lneNombre_ficha_estu, self.lneApellido_ficha_estu, self.lneFechaNac_ficha_estu,
            self.lneCity_ficha_estu, self.cbxGenero_ficha_estu, self.lneDir_ficha_estu,
            self.cbxTipoEdu_ficha_estu, self.cbxGrado_ficha_estu,
            self.cbxSeccion_ficha_estu, self.lneTallaC_ficha_estu,
            self.lneTallaP_ficha_estu, self.lneTallaZ_ficha_estu,
            self.lneMadre_ficha_estu, self.lneOcup_madre_ficha_estu, self.lnePadre_ficha_estu,
            self.lneCedula_padre_ficha_estu, self.lneOcup_padre_ficha_estu, 
            self.lneApellidos_repre_ficha_estu, self.lneNombres_repre_ficha_estu, 
            self.lneFechaNac_repre_ficha_estu, self.cbxGenero_repre_ficha_estu, 
            self.lneDir_repre_ficha_estu, self.lneNum_repre_ficha_estu, 
            self.lneCorreo_repre_ficha_estu, self.lneObser_ficha_estu_repre,
        ]
        
        # Campos de solo lectura (calculados o inmutables)
        campos_solo_lectura = [
            self.lneEdad_ficha_estu, 
            self.lneEdad_repre_ficha_estu, 
            self.lneCedula_madre_ficha_estu,
            self.lneFechaIng_ficha_estu,
            self.lneDocente_ficha_estu
        ]
        
        set_campos_editables(campos, estado, campos_solo_lectura)

    def cargar_datos(self):
        """
        Carga todos los datos del estudiante desde la BD y los muestra en el formulario.
        Incluye datos personales, académicos y del representante.
        """
        datos = EstudianteModel.obtener_por_id(self.id)

        if not datos:
            msg = crear_msgbox(
                self,
                "Error",
                f"No se encontró el estudiante con ID {self.id}",
                QMessageBox.Critical
            )
            msg.exec()
            self.reject()
            return

        # Guardar estado actual del estudiante en memoria
        self.estudiante_actual = {
            "ID": self.id,
            "Cédula": str(datos["cedula"]) if datos else "",
            "Estado": int(datos.get("estado", 1)) if datos else 1
        }
        
        # Mostrar estado en el label
        estado_texto = "Activo" if self.estudiante_actual["Estado"] else "Inactivo"
        self.lblEstado_ficha_estu.setText(estado_texto)
        
        # --- DATOS PERSONALES DEL ESTUDIANTE ---
        self.lneCedula_ficha_estu.setText(str(datos["cedula"]))
        self.lneNombre_ficha_estu.setText(str(datos["nombres"]))
        self.lneApellido_ficha_estu.setText(str(datos["apellidos"]))

        # Fecha de nacimiento y edad
        fecha_est = datos["fecha_nac_est"]
        qdate_est = QDate(fecha_est.year, fecha_est.month, fecha_est.day)
        self.lneFechaNac_ficha_estu.setDate(qdate_est)
        self.lneEdad_ficha_estu.setText(str(calcular_edad(fecha_est)))
        
        # Otros datos personales
        self.lneCity_ficha_estu.setText(str(datos["city"]))
        index_genero = self.cbxGenero_ficha_estu.findText(str(datos["genero"]))
        if index_genero >= 0:
            self.cbxGenero_ficha_estu.setCurrentIndex(index_genero)
        self.lneDir_ficha_estu.setText(str(datos["direccion"]))
        
        # Fecha de ingreso
        fecha_ing = datos["fecha_ingreso"]
        qdate_ing = QDate(fecha_ing.year, fecha_ing.month, fecha_ing.day)
        self.lneFechaIng_ficha_estu.setDate(qdate_ing)
        
        # --- DATOS ACADÉMICOS ---
        # Cargar según si es egresado o estudiante regular
        if self.es_egresado:
            # Datos de egresado (históricos)
            estatus = datos.get("estatus_academico", "Egresado")
            self.lneEstatus_egresado.setText(estatus)
            
            # Último grado cursado (incluye letra de sección)
            ultimo_grado = datos.get("ultimo_grado", "N/A")
            self.lneUltimoGrado.setText(ultimo_grado if ultimo_grado else "N/A")

            # Año escolar de egreso
            año_egreso = datos.get("año_egreso", "N/A")
            self.lneAnioEgreso.setText(año_egreso)
        else:
            # Estudiante regular: cargar sección actual
            tipo_edu = datos.get("tipo_educacion", "")
            if tipo_edu and tipo_edu != "Sin asignar":
                index_edu = self.cbxTipoEdu_ficha_estu.findText(tipo_edu)
                if index_edu >= 0:
                    self.cbxTipoEdu_ficha_estu.setCurrentIndex(index_edu)
                    self.actualizar_grado()
                    
                    grado = datos.get("grado", "")
                    if grado and grado != "Sin asignar":
                        index_grado = self.cbxGrado_ficha_estu.findText(grado)
                        if index_grado >= 0:
                            self.cbxGrado_ficha_estu.setCurrentIndex(index_grado)
                            self.actualizar_seccion(grado)
                            
                            seccion = datos.get("seccion", "")
                            if seccion and seccion != "Sin asignar":
                                index_seccion = self.cbxSeccion_ficha_estu.findText(seccion)
                                if index_seccion >= 0:
                                    self.cbxSeccion_ficha_estu.setCurrentIndex(index_seccion)
        
        docente_seccion = datos.get("docente_seccion", "Sin docente asignado")
        self.lneDocente_ficha_estu.setText(str(docente_seccion))
        
        # Tallas
        self.lneTallaC_ficha_estu.setText(str(datos["tallaC"]))
        self.lneTallaP_ficha_estu.setText(str(datos["tallaP"]))
        self.lneTallaZ_ficha_estu.setText(str(datos["tallaZ"]))
        
        # --- DATOS DE PADRES ---
        self.lnePadre_ficha_estu.setText(str(datos["padre"]))
        self.lneCedula_padre_ficha_estu.setText(str(datos["padre_ci"]))
        self.lneOcup_padre_ficha_estu.setText(str(datos["ocupacion_padre"]))
        self.lneMadre_ficha_estu.setText(str(datos["madre"]))
        self.lneCedula_madre_ficha_estu.setText(str(datos["madre_ci"]))
        self.lneOcup_madre_ficha_estu.setText(str(datos["ocupacion_madre"]))

        # --- DATOS DEL REPRESENTANTE ---
        representante_id = datos["representante_id"]
        if representante_id:
            datos_repre = RepresentanteModel.obtener_representante(representante_id)
            if datos_repre:
                self.lneCedula_repre_ficha_estu.setText(str(datos_repre["cedula_repre"]))
                self.lneNombres_repre_ficha_estu.setText(str(datos_repre["nombres_repre"]))
                self.lneApellidos_repre_ficha_estu.setText(str(datos_repre["apellidos_repre"]))

                # Fecha de nacimiento del representante
                fecha_repre = datos_repre["fecha_nac_repre"]
                qdate_repre = QDate(fecha_repre.year, fecha_repre.month, fecha_repre.day)
                self.lneFechaNac_repre_ficha_estu.setDate(qdate_repre)
                self.lneEdad_repre_ficha_estu.setText(str(calcular_edad(fecha_repre)))

                # Género del representante
                index_genero_repre = self.cbxGenero_repre_ficha_estu.findText(
                    str(datos_repre["genero_repre"])
                )
                if index_genero_repre >= 0:
                    self.cbxGenero_repre_ficha_estu.setCurrentIndex(index_genero_repre)
                
                # Resto de datos del representante
                self.lneDir_repre_ficha_estu.setText(str(datos_repre["direccion_repre"]))
                self.lneNum_repre_ficha_estu.setText(str(datos_repre["num_contact_repre"]))
                self.lneCorreo_repre_ficha_estu.setText(str(datos_repre["correo_repre"]))
                self.lneObser_ficha_estu_repre.setText(str(datos_repre["observacion"]))

    def _validar_texto_solo_letras(self, texto, nombre_campo):
        """
        Valida que un texto contenga solo letras y espacios.
        
        Args:
            texto: Texto a validar
            nombre_campo: Nombre del campo para mensajes de error
            
        Returns:
            tuple: (es_valido: bool, texto_normalizado: str)
        """
        if not texto:
            return False, ""
        
        # Validar patrón: solo letras (incluyendo acentos) y espacios
        if not re.match(r'^[A-Za-zÁÉÍÓÚÑáéíóúñ\s]+$', texto):
            crear_msgbox(
                self,
                "Formato inválido",
                f"El campo '{nombre_campo}' solo puede contener letras y espacios.",
                QMessageBox.Warning,
            ).exec()
            return False, ""
        
        # Normalizar: capitalizar cada palabra
        texto_normalizado = " ".join(p.capitalize() for p in texto.split())
        return True, texto_normalizado
    
    def _validar_email(self, email):
        """
        Valida formato de email.
        
        Args:
            email: Email a validar
            
        Returns:
            bool: True si es válido o está vacío, False si es inválido
        """
        if not email:
            return True  # Email opcional
        
        # Patrón básico de validación de email
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron, email):
            crear_msgbox(
                self,
                "Email inválido",
                "El formato del correo electrónico no es válido.",
                QMessageBox.Warning,
            ).exec()
            return False
        
        return True
    
    def _validar_telefono(self, telefono):
        """
        Valida formato de teléfono (solo números y guiones).
        
        Args:
            telefono: Número de teléfono a validar
            
        Returns:
            bool: True si es válido o está vacío, False si es inválido
        """
        if not telefono:
            return True  # Teléfono opcional
        
        # Solo números y guiones permitidos
        if not re.match(r'^[\d\-]+$', telefono):
            crear_msgbox(
                self,
                "Teléfono inválido",
                "El teléfono solo puede contener números y guiones.",
                QMessageBox.Warning,
            ).exec()
            return False
        
        return True

    def guardar_datos(self):
        """
        Guarda los cambios realizados en el formulario.
        Actualiza tanto al estudiante como a su representante.
        Incluye validaciones exhaustivas antes de guardar.
        """
        try:
            # --- VALIDACIONES DE DATOS DEL ESTUDIANTE ---
            
            # Validar nombres y apellidos
            nombres = self.lneNombre_ficha_estu.text().strip()
            apellidos = self.lneApellido_ficha_estu.text().strip()
            
            valido_nombres, nombres_norm = self._validar_texto_solo_letras(
                nombres, "Nombres del estudiante"
            )
            valido_apellidos, apellidos_norm = self._validar_texto_solo_letras(
                apellidos, "Apellidos del estudiante"
            )
            
            if not valido_nombres or not valido_apellidos:
                return
            
            # Validar nombre de la madre (obligatorio)
            madre = self.lneMadre_ficha_estu.text().strip()
            valido_madre, madre_norm = self._validar_texto_solo_letras(
                madre, "Nombre de la madre"
            )
            if not valido_madre:
                return
            
            # Validar nombre del padre (opcional)
            padre = self.lnePadre_ficha_estu.text().strip()
            if padre:
                valido_padre, padre_norm = self._validar_texto_solo_letras(
                    padre, "Nombre del padre"
                )
                if not valido_padre:
                    return
            else:
                padre_norm = ""
            
            # Validar fecha de nacimiento
            fecha_nac = self.lneFechaNac_ficha_estu.date().toPython()
            if fecha_nac > date.today():
                crear_msgbox(
                    self,
                    "Fecha inválida",
                    "La fecha de nacimiento del estudiante no puede ser futura.",
                    QMessageBox.Warning,
                ).exec()
                return
            
            # --- RECOLECTAR DATOS DEL ESTUDIANTE ---
            estudiante_data = {
                "nombres": nombres_norm,
                "apellidos": apellidos_norm,
                "fecha_nac_est": fecha_nac,
                "city": self.lneCity_ficha_estu.text().strip(),
                "genero": self.cbxGenero_ficha_estu.currentText().strip(),
                "direccion": self.lneDir_ficha_estu.text().strip(),
                "fecha_ingreso": self.lneFechaIng_ficha_estu.date().toPython(),
                "tipo_educacion": self.cbxTipoEdu_ficha_estu.currentText().strip(),
                "grado": self.cbxGrado_ficha_estu.currentText().strip(),
                "seccion": self.cbxSeccion_ficha_estu.currentText().strip(),
                "docente": self.lneDocente_ficha_estu.text().strip(),
                "tallaC": self.lneTallaC_ficha_estu.text().strip(),
                "tallaP": self.lneTallaP_ficha_estu.text().strip(),
                "tallaZ": self.lneTallaZ_ficha_estu.text().strip(),
                "padre": padre_norm,
                "padre_ci": self.lneCedula_padre_ficha_estu.text().strip(),
                "ocupacion_padre": self.lneOcup_padre_ficha_estu.text().strip(),
                "madre": madre_norm,
                "madre_ci": self.lneCedula_madre_ficha_estu.text().strip(),
                "ocupacion_madre": self.lneOcup_madre_ficha_estu.text().strip(),
            }
            
            # Obtener ID de sección si cambió
            seccion_id = self.cbxSeccion_ficha_estu.currentData()
            
            # --- VALIDACIONES DEL REPRESENTANTE ---
            
            # Validar nombres del representante
            nombres_repre = self.lneNombres_repre_ficha_estu.text().strip()
            apellidos_repre = self.lneApellidos_repre_ficha_estu.text().strip()
            
            valido_nombres_repre, nombres_repre_norm = self._validar_texto_solo_letras(
                nombres_repre, "Nombres del representante"
            )
            valido_apellidos_repre, apellidos_repre_norm = self._validar_texto_solo_letras(
                apellidos_repre, "Apellidos del representante"
            )
            
            if not valido_nombres_repre or not valido_apellidos_repre:
                return
            
            # Validar teléfono
            telefono = self.lneNum_repre_ficha_estu.text().strip()
            if not self._validar_telefono(telefono):
                return
            
            # Validar email
            email = self.lneCorreo_repre_ficha_estu.text().strip()
            if not self._validar_email(email):
                return
            
            # Validar fecha de nacimiento del representante
            fecha_nac_repre = self.lneFechaNac_repre_ficha_estu.date().toPython()
            if fecha_nac_repre > date.today():
                crear_msgbox(
                    self,
                    "Fecha inválida",
                    "La fecha de nacimiento del representante no puede ser futura.",
                    QMessageBox.Warning,
                ).exec()
                return
            
            # --- ACTUALIZAR ESTUDIANTE ---
            ok_estudiante, msg_estudiante = EstudianteModel.actualizar(
                self.id, 
                estudiante_data, 
                self.usuario_actual,
                seccion_id
            )
            
            if not ok_estudiante:
                crear_msgbox(
                    self,
                    "Error",
                    f"No se pudo actualizar el estudiante:\n{msg_estudiante}",
                    QMessageBox.Critical,
                ).exec()
                return

            # --- ACTUALIZAR REPRESENTANTE ---
            representante_id = RepresentanteModel.obtener_representante_id(self.id)
            if representante_id:
                representante_data = {
                    "nombres_repre": nombres_repre_norm,
                    "apellidos_repre": apellidos_repre_norm,
                    "fecha_nac_repre": fecha_nac_repre,
                    "genero_repre": self.cbxGenero_repre_ficha_estu.currentText().strip(),
                    "direccion_repre": self.lneDir_repre_ficha_estu.text().strip(),
                    "num_contact_repre": telefono,
                    "correo_repre": email,
                    "observacion": self.lneObser_ficha_estu_repre.text().strip(),
                }
                
                ok_repre, msg_repre = RepresentanteModel.actualizar_representante(
                    representante_id, 
                    representante_data
                )
                
                if not ok_repre:
                    # Advertir pero no fallar (estudiante ya se guardó)
                    crear_msgbox(
                        self,
                        "Advertencia",
                        f"Estudiante actualizado, pero hubo un problema con el representante:\n{msg_repre}",
                        QMessageBox.Warning,
                    ).exec()

            # Éxito total
            crear_msgbox(
                self,
                "Éxito",
                "Datos actualizados correctamente.",
                QMessageBox.Information,
            ).exec()
            
            # Emitir señal para actualizar tablas padre
            self.datos_actualizados.emit()

        except Exception as err:
            msg = crear_msgbox(
                self,
                "Error",
                f"No se pudo guardar cambios: {err}",
                QMessageBox.Critical,
            )
            msg.exec()
    
    def toggle_edicion(self):
        """
        Alterna entre modo edición y guardado.
        En modo edición: habilita campos y cambia botón a "Guardar"
        En modo guardado: guarda cambios, deshabilita campos y cambia botón a "Modificar"
        """
        if self.btnModificar_ficha_estu.text() == "Modificar":
            # Entrar en modo edición
            self.set_campos_editables(True)
            self.btnModificar_ficha_estu.setText("Guardar")
        else:
            # Guardar cambios y salir de modo edición
            self.guardar_datos()
            self.set_campos_editables(False)
            self.btnModificar_ficha_estu.setText("Modificar")

    def eliminar_estudiante(self):
        """
        Elimina el registro completo del estudiante.
        Requiere confirmación doble y registra en auditoría.
        """
        msg = crear_msgbox(
            self,
            "Confirmar eliminación",
            "¿Está seguro de eliminar este estudiante?\n\n"
            "Esta acción eliminará:\n"
            "- El registro del estudiante\n"
            "- Sus asignaciones a secciones\n"
            "- Su historial académico\n\n"
            "Esta acción NO se puede deshacer.",
            QMessageBox.Question,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if msg.exec() != QMessageBox.Yes:
            return

        try:
            ok, mensaje = EstudianteModel.eliminar(self.id_estudiante, self.usuario_actual)

            if ok:
                msg = crear_msgbox(
                    self,
                    "Éxito",
                    mensaje,
                    QMessageBox.Information,
                )
                msg.exec()
                
                # Emitir señal y cerrar ventana
                self.datos_actualizados.emit()
                self.accept()
            else:
                msg = crear_msgbox(
                    self,
                    "Error",
                    mensaje,
                    QMessageBox.Warning,
                )
                msg.exec()

        except Exception as err:
            msg = crear_msgbox(
                self,
                "Error",
                f"Error en la BD: {err}",
                QMessageBox.Critical,
            )
            msg.exec()

    def configurar_visibilidad_campos(self):
        """
        Configura qué campos mostrar según si es egresado o estudiante regular.
        
        Egresado:
        - Muestra: estatus académico, último grado, año de egreso
        - Oculta: controles de edición, asignación de sección
        
        Regular:
        - Muestra: controles completos de edición
        - Oculta: campos históricos de egresado
        """
        if self.es_egresado:
            # --- MODO EGRESADO (SOLO LECTURA) ---
            
            # Ocultar campos de estudiante regular
            self.lblTipoEdu.setVisible(False)
            self.frTipoEdu_reg_estu.setVisible(False)
            self.cbxTipoEdu_ficha_estu.setVisible(False)
            self.lblGrado.setVisible(False)
            self.frGrado_reg_estu.setVisible(False)
            self.cbxGrado_ficha_estu.setVisible(False)
            self.lblSeccion.setVisible(False)
            self.frseccion.setVisible(False)
            self.cbxSeccion_ficha_estu.setVisible(False)
            
            # Mostrar campos de egresado
            self.lblEstatus.setVisible(True)
            self.lneEstatus_egresado.setVisible(True)
            self.lblUltimoGrado.setVisible(True)
            self.lneUltimoGrado.setVisible(True)
            self.lblAnioEgreso.setVisible(True)
            self.lneAnioEgreso.setVisible(True)
            
            # Hacer campos de solo lectura
            self.lneEstatus_egresado.setReadOnly(True)
            self.lneUltimoGrado.setReadOnly(True)
            self.lneAnioEgreso.setReadOnly(True)
            
            # Ocultar controles de edición y estado
            self.btnModificar_ficha_estu.setVisible(False)
            self.btnEliminar_ficha_estu.setVisible(False)
            self.btnDevolver_grado.setVisible(False)
            self.switchActivo.setVisible(False)
            self.lblEstado_ficha_estu.setVisible(False)
        else:
            # --- MODO REGULAR (EDITABLE) ---
            
            # Ocultar campos de egresado
            self.lblEstatus.setVisible(False)
            self.lneEstatus_egresado.setVisible(False)
            self.lblUltimoGrado.setVisible(False)
            self.lneUltimoGrado.setVisible(False)
            self.lblAnioEgreso.setVisible(False)
            self.lneAnioEgreso.setVisible(False)
            
            # Mostrar campos normales
            self.lblTipoEdu.setVisible(True)
            self.frTipoEdu_reg_estu.setVisible(True)
            self.cbxTipoEdu_ficha_estu.setVisible(True)
            self.lblGrado.setVisible(True)
            self.frGrado_reg_estu.setVisible(True)
            self.cbxGrado_ficha_estu.setVisible(True)
            self.lblSeccion.setVisible(True)
            self.frseccion.setVisible(True)
            self.cbxSeccion_ficha_estu.setVisible(True)
            
            # Mostrar controles normales
            self.btnModificar_ficha_estu.setVisible(True)
            self.btnEliminar_ficha_estu.setVisible(True)
            self.btnDevolver_grado.setVisible(True)
            self.switchActivo.setVisible(True) 
            self.lblEstado_ficha_estu.setVisible(True)

    def devolver_estudiante(self):
        """
        Permite devolver al estudiante a un grado/sección anterior por repitencia.
        
        Restricciones:
        - Solo secciones del año actual
        - Solo grados iguales o inferiores al actual
        - Requiere confirmación explícita
        - Registra en historial y auditoría
        """
        # Validar que el estudiante esté activo
        if self.estudiante_actual.get("Estado") == 0:
            crear_msgbox(
                self,
                "Estudiante inactivo",
                "No se puede devolver un estudiante inactivo.\n"
                "Reactive al estudiante primero.",
                QMessageBox.Warning
            ).exec()
            return
        
        # 1. Obtener secciones disponibles del año actual
        año_actual = self.año_escolar['anio_inicio']
        secciones = EstudianteModel.obtener_secciones_activas(año_actual)
        
        if not secciones:
            msg = crear_msgbox(
                self,
                "Sin secciones",
                "No hay secciones disponibles para devolver al estudiante.",
                QMessageBox.Warning
            )
            msg.exec()
            return
        
        # 2. Filtrar solo grados válidos (mismo nivel o inferior)
        # TODO: Implementar lógica de jerarquía de grados si es necesario
        
        # 3. Crear lista de opciones (formato: "Grado Letra - Nivel")
        opciones = []
        mapa_secciones = {}
        for sec in secciones:
            texto = f"{sec['grado']} {sec['letra']} - {sec['nivel']}"
            opciones.append(texto)
            mapa_secciones[texto] = sec['id']
        
        # 4. Mostrar diálogo de selección
        seleccion, ok = QInputDialog.getItem(
            self,
            "Devolver estudiante",
            "Seleccione la sección a la que desea devolver al estudiante\n"
            "(por repitencia o cambio de grado):",
            opciones,
            0,
            False
        )
        
        if not ok or not seleccion:
            return
        
        # 5. Confirmación explícita
        msg_confirm = crear_msgbox(
            self,
            "Confirmar devolución",
            f"¿Está seguro de devolver al estudiante a {seleccion}?\n\n"
            "Esto registrará en el historial que el estudiante repitió grado "
            "o fue reasignado a un nivel inferior.",
            QMessageBox.Question,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if msg_confirm.exec() != QMessageBox.StandardButton.Yes:
            return
        
        # 6. Ejecutar devolución
        try:
            seccion_id = mapa_secciones[seleccion]
            ok, mensaje = EstudianteModel.devolver_estudiante(
                self.id_estudiante,
                seccion_id,
                año_actual,
                self.usuario_actual
            )
            
            if ok:
                msg = crear_msgbox(
                    self,
                    "Éxito",
                    mensaje,
                    QMessageBox.Information
                )
                msg.exec()
                
                # Recargar datos completos
                self.cargar_datos()
                self.cargar_historial()
                
                # Emitir señal para actualizar tablas padre
                self.datos_actualizados.emit()
            else:
                msg = crear_msgbox(
                    self,
                    "Error",
                    mensaje,
                    QMessageBox.Critical
                )
                msg.exec()

        except Exception as e:
            msg = crear_msgbox(
                self,
                "Error",
                f"Error inesperado: {e}",
                QMessageBox.Critical
            )
            msg.exec()

    def cargar_historial(self):
        """
        Carga y muestra el historial académico completo del estudiante.
        Muestra todos los años escolares cursados con sus respectivas secciones.
        """
        try:
            # Obtener historial desde el modelo
            historial = EstudianteModel.obtener_historial_estudiante(self.id_estudiante)
            
            if not historial:
                # Si no hay historial, mostrar tabla vacía
                model = QStandardItemModel(0, 4)
                model.setHorizontalHeaderLabels(["Año Escolar", "Nivel", "Grado", "Sección"])
                self.tableW_historial.setModel(model)
                return
            
            # Configurar modelo con datos
            columnas = ["Año Escolar", "Nivel", "Grado", "Sección"]
            model = QStandardItemModel(len(historial), len(columnas))
            model.setHorizontalHeaderLabels(columnas)
            
            # Llenar tabla con datos del historial
            for fila, registro in enumerate(historial):
                # Año escolar (formato: "2023-2024")
                año_escolar = f"{registro['año_inicio']}-{registro['año_inicio']+1}"
                item_año = QStandardItem(año_escolar)
                item_año.setEditable(False)
                model.setItem(fila, 0, item_año)
                
                # Nivel educativo
                item_nivel = QStandardItem(str(registro['nivel']))
                item_nivel.setEditable(False)
                model.setItem(fila, 1, item_nivel)
                
                # Grado
                item_grado = QStandardItem(str(registro['grado']))
                item_grado.setEditable(False)
                model.setItem(fila, 2, item_grado)
                
                # Sección (letra)
                item_seccion = QStandardItem(str(registro['letra']))
                item_seccion.setEditable(False)
                model.setItem(fila, 3, item_seccion)
            
            # Asignar modelo a la tabla
            self.tableW_historial.setModel(model)
            self.tableW_historial.setSortingEnabled(True)
            self.tableW_historial.setAlternatingRowColors(True)
            
            # Ajustar anchos de columnas con tooltips si las columnas son muy estrechas
            anchos_historial = {
                0: 120,  # Año Escolar
                1: 150,  # Nivel
                2: 80,   # Grado
                3: 80    # Sección
            }
            ajustar_columnas_tabla(self, self.tableW_historial, anchos_historial)
            
        except Exception as e:
            print(f"Error al cargar historial: {e}")
            msg = crear_msgbox(
                self,
                "Error",
                f"No se pudo cargar el historial académico:\n{e}",
                QMessageBox.Warning
            )
            msg.exec()