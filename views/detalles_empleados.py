import re
import os
from datetime import date

from models.registro_base import RegistroBase

from utils.widgets import Switch
from utils.exportar import generar_constancia_trabajo
from utils.edad import calcular_edad
from utils.forms import set_campos_editables
from utils.dialogs import crear_msgbox
from utils.sombras import crear_sombra_flotante
from utils.archivos import abrir_archivo

from models.emple_model import EmpleadoModel
from models.institucion_model import InstitucionModel
from ui_compiled.ficha_emple_ui import Ui_ficha_emple
from PySide6.QtWidgets import QDialog, QMessageBox, QMenu, QToolButton
from PySide6.QtCore import QDate, Signal


class DetallesEmpleado(QDialog, Ui_ficha_emple):
    """Ventana de detalles de un empleado."""
    
    datos_actualizados = Signal()

    def __init__(self, id_empleado, usuario_actual, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.usuario_actual = usuario_actual
        self.setWindowTitle("Ficha de empleado")
        self.id = id_empleado
        self.id_empleado = id_empleado
        self.stackFicha_emple.setCurrentIndex(0)
        
        # Variable para evitar bucles en señales del switch
        self.actualizando_switch = False
        
        # Cargar datos primero
        self.cargar_datos()
        
        # Inicializar switch después de cargar datos
        self.switchActivo = Switch()
        self.switchActivo.setFixedSize(50, 25)
        self.contenedorSwitch_emple.layout().addWidget(self.switchActivo)
        
        # Conectar botones de navegación
        self.btnDatosPersonales_ficha_emple.clicked.connect(
            lambda: self.cambiar_pagina_ficha_empleado(0)
        )
        self.btnDatosLaborales_ficha_emple.clicked.connect(
            lambda: self.cambiar_pagina_ficha_empleado(1)
        )
        self.btnModificar_ficha_emple.clicked.connect(self.toggle_edicion)
        self.btnEliminar_ficha_emple.clicked.connect(self.eliminar_empleado)
        
        # Conectar señal de fecha para cálculo de edad
        self.lneFechaNac_ficha_emple.dateChanged.connect(self.actualizar_edad_empleado)
        
        # Configurar menú de exportación
        self.btnExportar_ficha_emple.setPopupMode(QToolButton.InstantPopup)
        menu_exportar = QMenu(self.btnExportar_ficha_emple)
        menu_exportar.addAction("Constancia de trabajo", self.exportar_constancia)
        self.btnExportar_ficha_emple.setMenu(menu_exportar)
        
        # Bloquear campos y configurar estado inicial
        self.set_campos_editables(False)
        self.lneCedula_ficha_emple.setReadOnly(True)
        
        # Establecer estado inicial del switch sin disparar eventos
        self.actualizando_switch = True
        self.switchActivo.setChecked(bool(self.empleado_actual.get("Estado", 1)))
        self.actualizando_switch = False
        
        # Conectar señal del switch después de establecer el estado
        self.switchActivo.stateChanged.connect(self.cambiar_estado_empleado)

        # Aplicar efectos visuales
        crear_sombra_flotante(self.btnExportar_ficha_emple)
        crear_sombra_flotante(self.btnModificar_ficha_emple)
        crear_sombra_flotante(self.btnEliminar_ficha_emple)
        crear_sombra_flotante(self.btnDatosLaborales_ficha_emple)
        crear_sombra_flotante(self.btnDatosPersonales_ficha_emple)
        crear_sombra_flotante(self.lneCedula_ficha_emple, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lblTitulo_ficha_emple, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lblLogo_ficha_emple, blur_radius=8, y_offset=1)

    def cambiar_estado_empleado(self, state):
        """Maneja el cambio de estado del empleado."""
        if self.actualizando_switch:
            return
        
        self.actualizando_switch = True

        # Convertir estado del switch a valor de BD
        nuevo_estado = 1 if state == 2 else 0
        estado_actual = int(self.empleado_actual.get("Estado", 1))
        
        if nuevo_estado == estado_actual:
            self.actualizando_switch = False
            return

        texto = "activar" if nuevo_estado else "desactivar"

        msg = crear_msgbox(
            self,
            "Confirmar acción",
            f"¿Seguro que deseas {texto} a este empleado?",
            QMessageBox.Question,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if msg.exec() == QMessageBox.StandardButton.Yes:
            try:
                base = RegistroBase()
                ok, mensaje = base.cambiar_estado(
                    "empleados", 
                    self.id, 
                    nuevo_estado, 
                    self.usuario_actual
                )

                if ok:
                    self.empleado_actual["Estado"] = nuevo_estado
                    self.lblEstado_ficha_emple.setText("Activo" if nuevo_estado else "Inactivo")
                    
                    # Emitir señal para actualizar tablas padre
                    self.datos_actualizados.emit()
                    
                    crear_msgbox(
                        self,
                        "Éxito",
                        f"Empleado {texto}do correctamente.",
                        QMessageBox.Information,
                    ).exec()
                else:
                    crear_msgbox(
                        self,
                        "Error",
                        f"No se pudo {texto} al empleado: {mensaje}",
                        QMessageBox.Critical,
                    ).exec()
                    self.revertir_switch()

            except Exception as e:
                crear_msgbox(
                    self,
                    "Error",
                    f"Error inesperado: {str(e)}",
                    QMessageBox.Critical,
                ).exec()
                self.revertir_switch()
        else:
            self.revertir_switch()
            
        self.actualizando_switch = False
    
    def revertir_switch(self):
        """Revierte el switch al estado anterior."""
        self.actualizando_switch = True
        estado = self.empleado_actual.get("Estado", 1) == 1
        self.switchActivo.setChecked(estado)
        self.lblEstado_ficha_emple.setText("Activo" if estado else "Inactivo")
        self.actualizando_switch = False

    def exportar_constancia(self):
        """Genera constancia de trabajo en PDF."""
        try:
            # Preparar datos para la constancia
            empleado = {
                "Cédula": self.lneCedula_ficha_emple.text(),
                "Nombres": self.lneNombres_ficha_emple.text(),
                "Apellidos": self.lneApellidos_ficha_emple.text(),
                "Fecha Ingreso": self.lneFechaIngreso_ficha_emple.date().toString("dd/MM/yyyy"),
                "Cargo": self.lneCargo_ficha_emple.text()
            }
            
            # Obtener datos de la institución
            institucion = InstitucionModel.obtener_por_id(1)
            
            # Generar PDF
            archivo = generar_constancia_trabajo(empleado, institucion)
            
            # Abrir archivo con aplicación predeterminada
            abrir_archivo(archivo)
            
            crear_msgbox(
                self,
                "Éxito",
                f"Constancia generada correctamente:\n{archivo}",
                QMessageBox.Information,
            ).exec()
            
        except Exception as e:
            crear_msgbox(
                self,
                "Error",
                f"Error al exportar constancia: {e}",
                QMessageBox.Critical,
            ).exec()

    def actualizar_edad_empleado(self):
        """Calcula y muestra la edad del empleado."""
        fecha_nac = self.lneFechaNac_ficha_emple.date().toPython()
        
        # Validar que no sea futura
        if fecha_nac > date.today():
            self.lneEdad_ficha_emple.setText("0")
            return
        
        edad = calcular_edad(fecha_nac)
        self.lneEdad_ficha_emple.setText(str(edad))

    def cambiar_pagina_ficha_empleado(self, indice):
        """Cambia entre páginas del formulario."""
        self.stackFicha_emple.setCurrentIndex(indice)

    def set_campos_editables(self, estado: bool):
        """Habilita/deshabilita la edición de campos."""
        campos = [
            self.lneNombres_ficha_emple, self.lneApellidos_ficha_emple, 
            self.lneFechaNac_ficha_emple, self.cbxGenero_ficha_emple, 
            self.lneDir_ficha_emple, self.lneNum_ficha_emple, 
            self.lneCorreo_ficha_emple, self.lneRIF_ficha_emple, 
            self.lneCentroV_ficha_emple, self.cbxTitulo_ficha_emple, 
            self.lneCargo_ficha_emple, self.lneFechaIngreso_ficha_emple,
            self.lneCarnet_ficha_emple, self.lneRAC_ficha_emple
        ]
        campos_solo_lectura = [self.lneEdad_ficha_emple]
        set_campos_editables(campos, estado, campos_solo_lectura)

    def cargar_datos(self):
        """Carga los datos del empleado desde la BD."""
        datos = EmpleadoModel.obtener_por_id(self.id)

        if not datos:
            crear_msgbox(
                self,
                "Error",
                f"No se encontró el empleado con ID {self.id}",
                QMessageBox.Critical
            ).exec()
            self.reject()
            return

        # Guardar estado actual en memoria
        self.empleado_actual = {
            "ID": self.id,
            "Cédula": str(datos["cedula"]),
            "Estado": datos["estado"]
        }
        
        # Mostrar estado en el label
        estado_texto = "Activo" if self.empleado_actual["Estado"] else "Inactivo"
        self.lblEstado_ficha_emple.setText(estado_texto)

        # --- DATOS PERSONALES ---
        self.lneCedula_ficha_emple.setText(str(datos["cedula"]))
        self.lneNombres_ficha_emple.setText(str(datos["nombres"]))
        self.lneApellidos_ficha_emple.setText(str(datos["apellidos"]))
        
        # Fecha de nacimiento
        fecha_emple = datos["fecha_nac"]
        qdate_emple = QDate(fecha_emple.year, fecha_emple.month, fecha_emple.day)
        self.lneFechaNac_ficha_emple.setDate(qdate_emple)
        self.lneEdad_ficha_emple.setText(str(calcular_edad(fecha_emple)))
        
        # Género
        index_genero = self.cbxGenero_ficha_emple.findText(str(datos["genero"]))
        if index_genero >= 0:
            self.cbxGenero_ficha_emple.setCurrentIndex(index_genero)
        
        # Otros datos personales
        self.lneDir_ficha_emple.setText(str(datos["direccion"]))
        self.lneNum_ficha_emple.setText(str(datos["num_contact"]))
        self.lneCorreo_ficha_emple.setText(str(datos["correo"]))
        self.lneRIF_ficha_emple.setText(str(datos["rif"]))
        self.lneCentroV_ficha_emple.setText(str(datos["centro_votacion"]))
        
        # --- DATOS LABORALES ---
        # Título
        index_titulo = self.cbxTitulo_ficha_emple.findText(str(datos["titulo"]))
        if index_titulo >= 0:
            self.cbxTitulo_ficha_emple.setCurrentIndex(index_titulo)
        
        self.lneCargo_ficha_emple.setText(str(datos["cargo"]))
        
        # Fecha de ingreso
        fecha_ing = datos["fecha_ingreso"]
        qdate_ing = QDate(fecha_ing.year, fecha_ing.month, fecha_ing.day)
        self.lneFechaIngreso_ficha_emple.setDate(qdate_ing)
        
        self.lneCarnet_ficha_emple.setText(str(datos["num_carnet"]))
        self.lneRAC_ficha_emple.setText(str(datos["codigo_rac"]))
    
    def _validar_texto_solo_letras(self, texto, nombre_campo):
        """Valida que el texto contenga solo letras."""
        if not texto:
            return False, ""
        
        if not re.match(r'^[A-Za-zÁÉÍÓÚÑáéíóúñ\s]+$', texto):
            crear_msgbox(
                self,
                "Formato inválido",
                f"El campo '{nombre_campo}' solo puede contener letras y espacios.",
                QMessageBox.Warning,
            ).exec()
            return False, ""
        
        texto_norm = " ".join(p.capitalize() for p in texto.split())
        return True, texto_norm
    
    def _validar_email(self, email):
        """Valida formato de email."""
        if not email:
            return True
        
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
        """Valida formato de teléfono."""
        if not telefono:
            return True
        
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
        """Guarda los cambios en la BD."""
        try:
            # --- VALIDACIONES ---
            
            # Validar nombres y apellidos
            nombres = self.lneNombres_ficha_emple.text().strip()
            apellidos = self.lneApellidos_ficha_emple.text().strip()
            
            valido_nombres, nombres_norm = self._validar_texto_solo_letras(
                nombres, "Nombres"
            )
            valido_apellidos, apellidos_norm = self._validar_texto_solo_letras(
                apellidos, "Apellidos"
            )
            
            if not valido_nombres or not valido_apellidos:
                return
            
            # Validar fecha de nacimiento
            fecha_nac = self.lneFechaNac_ficha_emple.date().toPython()
            if fecha_nac > date.today():
                crear_msgbox(
                    self,
                    "Fecha inválida",
                    "La fecha de nacimiento no puede ser futura.",
                    QMessageBox.Warning,
                ).exec()
                return
            
            # Validar teléfono
            telefono = self.lneNum_ficha_emple.text().strip()
            if not self._validar_telefono(telefono):
                return
            
            # Validar email
            email = self.lneCorreo_ficha_emple.text().strip()
            if not self._validar_email(email):
                return
            
            # Validar fecha de ingreso
            fecha_ingreso = self.lneFechaIngreso_ficha_emple.date().toPython()
            if fecha_ingreso > date.today():
                crear_msgbox(
                    self,
                    "Fecha inválida",
                    "La fecha de ingreso no puede ser futura.",
                    QMessageBox.Warning,
                ).exec()
                return

            # --- RECOLECTAR DATOS ---
            empleado_data = {
                "nombres": nombres_norm,
                "apellidos": apellidos_norm,
                "fecha_nac": fecha_nac,
                "genero": self.cbxGenero_ficha_emple.currentText().strip(),
                "rif": self.lneRIF_ficha_emple.text().strip(),
                "centro_votacion": self.lneCentroV_ficha_emple.text().strip(),
                "direccion": self.lneDir_ficha_emple.text().strip(),
                "num_contact": telefono,
                "correo": email,
                "titulo": self.cbxTitulo_ficha_emple.currentText().strip(),
                "cargo": self.lneCargo_ficha_emple.text().strip(),
                "fecha_ingreso": fecha_ingreso,
                "num_carnet": self.lneCarnet_ficha_emple.text().strip(),
                "codigo_rac": self.lneRAC_ficha_emple.text().strip(),
            }
            
            # --- ACTUALIZAR EN BD ---
            ok, mensaje = EmpleadoModel.actualizar(
                self.id, 
                empleado_data, 
                self.usuario_actual
            )

            if ok:
                crear_msgbox(
                    self,
                    "Éxito",
                    mensaje,
                    QMessageBox.Information,
                ).exec()
                
                # Emitir señal para actualizar tablas padre
                self.datos_actualizados.emit()
            else:
                crear_msgbox(
                    self,
                    "Error",
                    mensaje,
                    QMessageBox.Warning,
                ).exec()

        except Exception as err:
            crear_msgbox(
                self,
                "Error",
                f"No se pudo guardar cambios: {err}",
                QMessageBox.Critical,
            ).exec()
    
    def toggle_edicion(self):
        """Alterna entre modo edición y guardado"""
        if self.btnModificar_ficha_emple.text() == "Modificar":
            self.set_campos_editables(True)
            self.btnModificar_ficha_emple.setText("Guardar")
        else:
            self.guardar_datos()
            self.set_campos_editables(False)
            self.btnModificar_ficha_emple.setText("Modificar")

    def eliminar_empleado(self):
        """Elimina el empleado tras confirmación"""
        msg = crear_msgbox(
            self,
            "Confirmar eliminación",
            "¿Está seguro de eliminar este empleado?\n\n"
            "Esta acción no se puede deshacer.",
            QMessageBox.Question,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if msg.exec() != QMessageBox.StandardButton.Yes:
            return

        try:
            ok, mensaje = EmpleadoModel.eliminar(self.id_empleado, self.usuario_actual)

            if ok:
                crear_msgbox(
                    self,
                    "Éxito",
                    mensaje,
                    QMessageBox.Information,
                ).exec()
                
                # Emitir señal y cerrar ventana
                self.datos_actualizados.emit()
                self.accept()
            else:
                crear_msgbox(
                    self,
                    "Error",
                    mensaje,
                    QMessageBox.Warning,
                ).exec()

        except Exception as err:
            crear_msgbox(
                self,
                "Error",
                f"Error en la BD: {err}",
                QMessageBox.Critical,
            ).exec()