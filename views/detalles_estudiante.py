from models.registro_base import RegistroBase
from ui_compiled.ficha_estu_ui import Ui_ficha_estu
from PySide6.QtWidgets import QDialog, QMessageBox, QMenu, QToolButton
from PySide6.QtCore import Qt, QDate, Signal
from models.repre_model import RepresentanteModel
from models.estu_model import EstudianteModel
from utils.widgets import Switch
from utils.exportar import generar_constancia_estudios
import os
from utils.edad import calcular_edad
from utils.forms import set_campos_editables
from utils.dialogs import crear_msgbox


class DetallesEstudiante(QDialog, Ui_ficha_estu):
    datos_actualizados = Signal()

    def __init__(self, id_estudiante, usuario_actual, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.setupUi(self)   # esto mete todos los widgets en self

        self.setWindowTitle("Ficha de estudiante v0.5")
        self.id = id_estudiante
        self.id_estudiante = id_estudiante
        self.stackFicha_estu.setCurrentIndex(0)
        
        # Variable para evitar bucles en las señales
        self.actualizando_switch = False
        
        # Cargar datos primero
        self.cargar_datos()
        
        # Inicializar el switch después de cargar datos
        self.switchActivo = Switch()
        self.switchActivo.setFixedSize(50, 25)
        self.contenedorSwitch.layout().addWidget(self.switchActivo)
        
        # Conectar señales de botones
        self.btnStudentDatos_ficha.clicked.connect(lambda: self.cambiar_pagina_ficha_estudiante(0))
        self.btnRepre_ficha.clicked.connect(lambda: self.cambiar_pagina_ficha_estudiante(1))
        self.btnModificar_ficha_estu.clicked.connect(self.toggle_edicion)
        self.btnEliminar_ficha_estu.clicked.connect(self.eliminar_estudiante)
        
        # Conectar señales de fechas para cálculo de edad
        self.lneFechaNac_ficha_estu.dateChanged.connect(self.actualizar_edad_estudiante)
        self.lneFechaNac_repre_ficha_estu.dateChanged.connect(self.actualizar_edad_representante)
        
        # Configurar botón de exportar
        self.btnExportar_ficha_estu.setPopupMode(QToolButton.InstantPopup)
        menu_exportar = QMenu(self.btnExportar_ficha_estu)
        menu_exportar.addAction("Constancia de estudios", self.exportar_constancia)
        #menu_exportar.addAction("Exportar a Excel", self.exportar_excel)
        #menu_exportar.addAction("Exportar a CSV", self.exportar_csv)
        self.btnExportar_ficha_estu.setMenu(menu_exportar)
        
        # Bloquear campos y configurar estado inicial
        self.set_campos_editables(False)
        self.lneCedula_repre_ficha_estu.setReadOnly(True)
        self.lneCedula_ficha_estu.setReadOnly(True)
        
        # Establecer el estado inicial del switch sin disparar eventos
        self.actualizando_switch = True
        self.switchActivo.setChecked(bool(self.estudiante_actual.get("Estado", 1)))
        self.actualizando_switch = False
        
        # Conectar la señal del switch después de establecer el estado inicial
        self.switchActivo.stateChanged.connect(self.cambiar_estado_estudiante)

        self.cbxTipoEdu_ficha_estu.currentIndexChanged.connect(self.actualizar_grado)
    
    def actualizar_grado(self):
        t_educacion = self.cbxTipoEdu_ficha_estu.currentText()
        # Limpiar y agregar placeholder
        self.cbxGrado_ficha_estu.clear()
        self.cbxGrado_ficha_estu.addItem("Seleccione grado")
        # Opcional: deshabilitar el placeholder para que no se pueda seleccionar desde el menú
        model = self.cbxGrado_ficha_estu.model()
        item0 = model.item(0)
        if item0 is not None:
            item0.setEnabled(False)
            item0.setForeground(Qt.GlobalColor.gray)

        # Cargar criterios si hay población válida
        if t_educacion in EstudianteModel.tipos_de_educacion:
            self.cbxGrado_ficha_estu.addItems(EstudianteModel.tipos_de_educacion[t_educacion])
            self.cbxGrado_ficha_estu.setEnabled(True)
            # Mantener el placeholder como selección inicial
            self.cbxGrado_ficha_estu.setCurrentIndex(0)
        else:
            self.cbxGrado_ficha_estu.setEnabled(False)

    def cambiar_estado_estudiante(self, state):
        if self.actualizando_switch:
            return

        nuevo_estado = 1 if state == Qt.Checked else 0
        estado_actual = int(self.estudiante_actual.get("Estado", 1))  # ahora la clave es 'estado'
        if nuevo_estado == estado_actual:
            return

        texto = "activar" if nuevo_estado else "desactivar"

        msg = crear_msgbox(
                    self,
                    "Confirmar acción",
                    f"¿Seguro que deseas {texto} a este estudiante?",
                    QMessageBox.Question,
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                    QMessageBox.StandardButton.No
                )

        if msg.exec() == QMessageBox.StandardButton.Yes:
            try:
                base = RegistroBase()
                ok, mensaje = base.cambiar_estado("estudiantes", self.id, nuevo_estado, self.usuario_actual)

                if ok:
                    # Mantén el estado como número en estudiante_actual
                    self.estudiante_actual["Estado"] = nuevo_estado
                    self.lblEstado_ficha_estu.setText("Activo" if nuevo_estado else "Inactivo")
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
                dlg = crear_msgbox(
                        self,
                        "Error",
                        f"Error inesperado: {str(e)}",
                        QMessageBox.Critical,
                    )
                dlg.exec()
                self.revertir_switch()
        else:
            self.revertir_switch()
    
    def revertir_switch(self):
        """Método auxiliar para revertir el estado del switch de manera segura"""
        self.actualizando_switch = True
        estado = bool(self.estudiante_actual["Estado"])
        self.switchActivo.setChecked(bool(self.estudiante_actual["Estado"]))
        self.lblEstado_ficha_estu.setText("Activo" if estado else "Inactivo")
        self.actualizando_switch = False

    def exportar_constancia(self):
        try:
            estudiante = {
                "Cédula": self.lneCedula_ficha_estu.text(),
                "Nombres": self.lneNombre_ficha_estu.text(),
                "Apellidos": self.lneApellido_ficha_estu.text(),
                "Grado": self.cbxGrado_ficha_estu.currentText(),
                "Sección": self.cbxSeccion_ficha_estu.currentText()
            }
            archivo = generar_constancia_estudios(estudiante)
            os.startfile(archivo)  # Windows
        except Exception as e:
            msg = crear_msgbox(
                self,
                "Error",
                f"Error al exportar constancia: {e}",
                QMessageBox.Critical,
            )
            msg.exec()

    def actualizar_edad_estudiante(self):
        fecha_nac = self.lneFechaNac_ficha_estu.date().toPython()
        edad = calcular_edad(fecha_nac)
        self.lneEdad_ficha_estu.setText(str(edad))

    def actualizar_edad_representante(self):
        fecha_nac = self.lneFechaNac_repre_ficha_estu.date().toPython()
        edad = calcular_edad(fecha_nac)
        self.lneEdad_repre_ficha_estu.setText(str(edad))
    def cambiar_pagina_ficha_estudiante(self, indice):
        self.stackFicha_estu.setCurrentIndex(indice)

    def set_campos_editables(self, estado: bool):
        campos = [
            self.lneNombre_ficha_estu, self.lneApellido_ficha_estu, self.lneFechaNac_ficha_estu,
            self.lneCity_ficha_estu, self.cbxGenero_ficha_estu, self.lneDir_ficha_estu,
            self.cbxTipoEdu_ficha_estu, self.cbxGrado_ficha_estu,
            self.cbxSeccion_ficha_estu, self.lneDocente_ficha_estu, self.lneTallaC_ficha_estu,
            self.lneTallaP_ficha_estu, self.lneTallaZ_ficha_estu,
            self.lneMadre_ficha_estu, self.lneOcup_madre_ficha_estu, self.lnePadre_ficha_estu,
            self.lneCedula_padre_ficha_estu, self.lneOcup_padre_ficha_estu, self.lneApellidos_repre_ficha_estu,
            self.lneNombres_repre_ficha_estu, self.lneFechaNac_repre_ficha_estu,
            self.cbxGenero_repre_ficha_estu, self.lneDir_repre_ficha_estu,
            self.lneNum_repre_ficha_estu, self.lneCorreo_repre_ficha_estu, self.lneObser_ficha_estu_repre,
        ]
        campos_solo_lectura = [self.lneEdad_ficha_estu, self.lneEdad_repre_ficha_estu, self.lneCedula_madre_ficha_estu,
                               self.lneFechaIng_ficha_estu]
        set_campos_editables(campos, estado, campos_solo_lectura)

    def cargar_datos(self):
        datos = EstudianteModel.obtener_por_id(self.id)

        # Guardar estado actual
        self.estudiante_actual = {
            "ID": self.id,
            "Cédula": str(datos["cedula"]) if datos else "",
            "Estado": datos["estado"] if datos else 1
        }
        
        # Mostrar estado en el label
        estado_texto = "Activo" if self.estudiante_actual["Estado"] else "Inactivo"
        self.lblEstado_ficha_estu.setText(estado_texto)
        
        if datos:
            self.lneCedula_ficha_estu.setText(str(datos["cedula"]))
            self.lneNombre_ficha_estu.setText(str(datos["nombres"]))
            self.lneApellido_ficha_estu.setText(str(datos["apellidos"]))

            fecha_est = datos["fecha_nac_est"]
            qdate_est = QDate(fecha_est.year, fecha_est.month, fecha_est.day)
            self.lneFechaNac_ficha_estu.setDate(qdate_est)
            self.lneEdad_ficha_estu.setText(str(calcular_edad(fecha_est)))
            self.lneCity_ficha_estu.setText(str(datos["city"]))
            index_genero = self.cbxGenero_ficha_estu.findText(str(datos["genero"]))
            if index_genero >= 0:
                self.cbxGenero_ficha_estu.setCurrentIndex(index_genero)
            self.lneDir_ficha_estu.setText(str(datos["direccion"]))
            fecha_ing = datos["fecha_ingreso"]
            qdate_ing = QDate(fecha_ing.year, fecha_ing.month, fecha_ing.day)
            self.lneFechaIng_ficha_estu.setDate(qdate_ing)
            index_edu = self.cbxTipoEdu_ficha_estu.findText(str(datos["tipo_educacion"]))
            if index_edu >= 0:
                self.cbxTipoEdu_ficha_estu.setCurrentIndex(index_edu)
            index_grado = self.cbxGrado_ficha_estu.findText(str(datos["grado"]))
            if index_grado >= 0:
                self.cbxGrado_ficha_estu.setCurrentIndex(index_grado)
            index_seccion = self.cbxSeccion_ficha_estu.findText(str(datos["seccion"]))
            if index_seccion >= 0:
                self.cbxSeccion_ficha_estu.setCurrentIndex(index_seccion)
            self.lneDocente_ficha_estu.setText(str(datos["docente"]))
            self.lneTallaC_ficha_estu.setText(str(datos["tallaC"]))
            self.lneTallaP_ficha_estu.setText(str(datos["tallaP"]))
            self.lneTallaZ_ficha_estu.setText(str(datos["tallaZ"]))
            self.lnePadre_ficha_estu.setText(str(datos["padre"]))
            self.lneCedula_padre_ficha_estu.setText(str(datos["padre_ci"]))
            self.lneOcup_padre_ficha_estu.setText(str(datos["ocupacion_padre"]))
            self.lneMadre_ficha_estu.setText(str(datos["madre"]))
            self.lneCedula_madre_ficha_estu.setText(str(datos["madre_ci"]))
            self.lneOcup_madre_ficha_estu.setText(str(datos["ocupacion_madre"]))

            representante_id = datos["representante_id"]
            if representante_id:
                datos_repre = RepresentanteModel.obtener_representante(representante_id)
                if datos_repre:
                    self.lneCedula_repre_ficha_estu.setText(str(datos_repre["cedula_repre"]))
                    self.lneNombres_repre_ficha_estu.setText(str(datos_repre["nombres_repre"]))
                    self.lneApellidos_repre_ficha_estu.setText(str(datos_repre["apellidos_repre"]))

                    fecha_repre = datos_repre["fecha_nac_repre"]
                    qdate_repre = QDate(fecha_repre.year, fecha_repre.month, fecha_repre.day)
                    self.lneFechaNac_repre_ficha_estu.setDate(qdate_repre)
                    self.lneEdad_repre_ficha_estu.setText(str(calcular_edad(fecha_repre)))

                    index_genero_repre = self.cbxGenero_repre_ficha_estu.findText(str(datos_repre["genero_repre"]))
                    if index_genero_repre >= 0:
                        self.cbxGenero_repre_ficha_estu.setCurrentIndex(index_genero_repre)
                    self.lneDir_repre_ficha_estu.setText(str(datos_repre["direccion_repre"]))
                    self.lneNum_repre_ficha_estu.setText(str(datos_repre["num_contact_repre"]))
                    self.lneCorreo_repre_ficha_estu.setText(str(datos_repre["correo_repre"]))
                    self.lneObser_ficha_estu_repre.setText(str(datos_repre["observacion"]))

    def guardar_datos(self):
        try:

            # --- Datos estudiante ---
            estudiante_data = {
                "nombres": self.lneNombre_ficha_estu.text(),
                "apellidos": self.lneApellido_ficha_estu.text(),
                "fecha_nac_est": self.lneFechaNac_ficha_estu.date().toPython(),
                "city": self.lneCity_ficha_estu.text(),
                "genero": self.cbxGenero_ficha_estu.currentText().strip(),
                "direccion": self.lneDir_ficha_estu.text(),
                "fecha_ingreso": self.lneFechaIng_ficha_estu.date().toPython(),
                "tipo_educacion": self.cbxTipoEdu_ficha_estu.currentText().strip(),
                "grado": self.cbxGrado_ficha_estu.currentText().strip(),
                "seccion": self.cbxSeccion_ficha_estu.currentText().strip(),
                "docente": self.lneDocente_ficha_estu.text(),
                "tallaC": self.lneTallaC_ficha_estu.text(),
                "tallaP": self.lneTallaP_ficha_estu.text(),
                "tallaZ": self.lneTallaZ_ficha_estu.text(),
                "padre": self.lnePadre_ficha_estu.text(),
                "padre_ci": self.lneCedula_padre_ficha_estu.text(),
                "ocupacion_padre": self.lneOcup_padre_ficha_estu.text(),
                "madre": self.lneMadre_ficha_estu.text(),
                "madre_ci": self.lneCedula_madre_ficha_estu.text(),
                "ocupacion_madre": self.lneOcup_madre_ficha_estu.text(),
            }
            EstudianteModel.actualizar(self.id, estudiante_data, self.usuario_actual)

            # --- Representante ---
            representante_id = RepresentanteModel.obtener_representante_id(self.id)
            if representante_id:
                representante_data = {
                    "nombres_repre": self.lneNombres_repre_ficha_estu.text(),
                    "apellidos_repre": self.lneApellidos_repre_ficha_estu.text(),
                    "fecha_nac_repre": self.lneFechaNac_repre_ficha_estu.date().toPython(),
                    "genero_repre": self.cbxGenero_repre_ficha_estu.currentText().strip(),
                    "direccion_repre": self.lneDir_repre_ficha_estu.text(),
                    "num_contact_repre": self.lneNum_repre_ficha_estu.text(),
                    "correo_repre": self.lneCorreo_repre_ficha_estu.text(),
                    "observacion": self.lneObser_ficha_estu_repre.text(),
                }
                RepresentanteModel.actualizar_representante(representante_id, representante_data)

            msg = crear_msgbox(
                self,
                "Éxito",
                "Datos actualizados correctamente.",
                QMessageBox.Information,
            )
            msg.exec()

        except Exception as err:
            msg = crear_msgbox(
                self,
                "Error",
                f"No se pudo guardar cambios: {err}",
                QMessageBox.Critical,
            )
            msg.exec()
    
    def toggle_edicion(self):
        """Alterna entre modo edición y guardado"""
        if self.btnModificar_ficha_estu.text() == "Modificar":
            self.set_campos_editables(True)
            self.btnModificar_ficha_estu.setText("Guardar")
        else:
            self.guardar_datos()
            self.set_campos_editables(False)
            self.btnModificar_ficha_estu.setText("Modificar")

    def eliminar_estudiante(self):
        msg = crear_msgbox(
            self,
            "Confirmar eliminación",
            "¿Está seguro de eliminar este estudiante?",
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