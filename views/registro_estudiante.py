import re
from datetime import date

from utils.dialogs import crear_msgbox
from utils.forms import limpiar_widgets
from utils.edad import calcular_edad
from utils.animated_stack import AnimatedStack
from ui_compiled.registro_estu_ui import Ui_registro_estu
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import QDate, Qt

from models.repre_model import RepresentanteModel
from models.estu_model import EstudianteModel


class NuevoRegistro(QDialog, Ui_registro_estu):
    def __init__(self, usuario_actual, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual

        self.setupUi(self)   # esto mete todos los widgets en self

        # Ventana Registro Estudiante
        self.setWindowTitle("Nuevo registro de estudiante v0.5")
        self.stackRegistro_estudiante.setCurrentIndex(0)
        # Botones
        self.btnGenCedula_reg_estu.clicked.connect(self.generar_cedula_estudiantil)
        self.btnGuardar_reg_estu.clicked.connect(self.guardar_en_bd)
        self.btnConsult_ci_repre.clicked.connect(self.buscar_representante)
        self.btnStudentDatos_registro.clicked.connect(lambda: self.cambiar_pagina_registro_estudiante(0))
        self.btnRepre_registro.clicked.connect(lambda: self.cambiar_pagina_registro_estudiante(1))
        self.btnLimpiar_reg_estu.clicked.connect(self.limpiar_formulario)

        # Conectar cálculo automático de edad
        self.lneFechaNac_reg_estu.dateChanged.connect(self.actualizar_edad_estudiante)
        self.lneFechaNac_reg_estu_repre.dateChanged.connect(self.actualizar_edad_representante)

        # Variable para almacenar la cédula generada
        self.cedula_estudiantil_generada = None

        self.cbxTipoEdu_reg_estu.currentIndexChanged.connect(self.actualizar_grado)
        self.cbxGrado_reg_estu.setEnabled(False)

        # Deshabilitar el primer ítem (el vacío) en grado y sección
        self.cbxSeccion_reg_estu.model().item(0).setEnabled(False)
    
    def limpiar_formulario(self):
        limpiar_widgets(self)
        self.cedula_estudiantil_generada = None
    
    def actualizar_grado(self):
        
        t_educacion = self.cbxTipoEdu_reg_estu.currentText()
        # Limpiar y agregar placeholder
        self.cbxGrado_reg_estu.clear()
        self.cbxGrado_reg_estu.addItem("Seleccione grado")
        # Opcional: deshabilitar el placeholder para que no se pueda seleccionar desde el menú
        model = self.cbxGrado_reg_estu.model()
        item0 = model.item(0)
        if item0 is not None:
            item0.setEnabled(False)
            item0.setForeground(Qt.GlobalColor.gray)

        # Cargar criterios si hay población válida
        if t_educacion in EstudianteModel.tipos_de_educacion:
            self.cbxGrado_reg_estu.addItems(EstudianteModel.tipos_de_educacion[t_educacion])
            self.cbxGrado_reg_estu.setEnabled(True)
            # Mantener el placeholder como selección inicial
            self.cbxGrado_reg_estu.setCurrentIndex(0)
        else:
            self.cbxGrado_reg_estu.setEnabled(False)

    # --- Funciones de cálculo de edad ---
    def actualizar_edad_estudiante(self):
        qdate = self.lneFechaNac_reg_estu.date()
        fecha_nac = qdate.toPython()
        edad = calcular_edad(fecha_nac)
        self.lneEdad_reg_estu.setText(str(edad))

    def actualizar_edad_representante(self):
        qdate = self.lneFechaNac_reg_estu_repre.date()
        fecha_nac = qdate.toPython()
        edad = calcular_edad(fecha_nac)
        self.lneEdad_reg_estu_repre.setText(str(edad))


    def buscar_representante(self):
        cedula_repre = self.lneCedula_reg_estu_repre.text().strip()
        if not cedula_repre:
            msg = crear_msgbox(
                    self,
                    "Campo vacío",
                    "Ingrese una cédula para buscar.",
                    QMessageBox.Warning,
                )
            msg.exec()
            return

        try:
            repre = RepresentanteModel.buscar_por_cedula(cedula_repre)
            if repre:
                # Rellenar los campos del formulario
                self.lneApellido_reg_estu_repre.setText(repre["apellidos_repre"])
                self.lneNombre_reg_estu_repre.setText(repre["nombres_repre"])

                fecha_repre = repre["fecha_nac_repre"]
                if isinstance(fecha_repre, date):
                    self.lneFechaNac_reg_estu_repre.setDate(QDate.fromPyDate(fecha_repre))
                else:
                    y, m, d = map(int, str(fecha_repre).split("-"))
                    self.lneFechaNac_reg_estu_repre.setDate(QDate(y, m, d))
                index_genero_repre = self.cbxGenero_reg_estu_repre.findText(repre["genero_repre"])
                if index_genero_repre >= 0:
                    self.cbxGenero_reg_estu_repre.setCurrentIndex(index_genero_repre)
            
                self.lneDir_reg_estu_repre.setText(repre["direccion_repre"])
                self.lneNum_reg_estu_repre.setText(repre["num_contact_repre"])
                self.lneCorreo_reg_estu_repre.setText(repre["correo_repre"])
                self.lneObser_reg_estu_repre.setText(repre["observacion"])

                msg = crear_msgbox(
                    self,
                    "Encontrado",
                    "Datos del representante cargados.",
                    QMessageBox.Information,
                )
                msg.exec()
            else:
                msg = crear_msgbox(
                    self,
                    "No encontrado",
                    "No existe representante con esa cédula.",
                    QMessageBox.Information,
                )
                msg.exec()

        except Exception as err:
            msg = crear_msgbox(
                    self,
                    "Error",
                    f"No se pudo buscar: {err}",
                    QMessageBox.Critical,
                )
            msg.exec()
    
    def cambiar_pagina_registro_estudiante(self, indice):
        self.stackRegistro_estudiante.setCurrentIndex(indice)
    
    def generar_cedula_estudiantil(self):
        qdate = self.lneFechaNac_reg_estu.date()
        fecha_nac = qdate.toPython()
        cedula_madre = self.lneCI_madre_reg_estu.text().strip()

        if not fecha_nac or not cedula_madre:
            msg = crear_msgbox(
                    self,
                    "Campos incompletos",
                    "Debe ingresar fecha de nacimiento de estudiante y cédula de la madre",
                    QMessageBox.Warning,
                )
            msg.exec()
            return

        try:
            cedula = EstudianteModel.generar_cedula_estudiantil(fecha_nac, cedula_madre)

            if cedula:
                self.cedula_estudiantil_generada = cedula
                self.lneCedula_reg_estu.setText(cedula)
            else:
                msg = crear_msgbox(
                    self,
                    "Error",
                    "No se pudo generar la cédula estudiantil.",
                    QMessageBox.Warning,
                )
                msg.exec()

        except Exception as err:
            msg = crear_msgbox(
                    self,
                    "Error",
                    f"No se pudo generar: {err}",
                    QMessageBox.Critical,
                )
            msg.exec()
    
    def guardar_en_bd(self):
        if not self.cedula_estudiantil_generada:
            msg = crear_msgbox(
                    self,
                    "Falta generar",
                    "Debe generar la cédula estudiantil antes de guardar.",
                    QMessageBox.Warning,
                )
            msg.exec()
            return

        # --- Datos estudiante ---
        nombres = self.lneNombre_reg_estu.text().strip()
        apellidos = self.lneApellido_reg_estu.text().strip()
        campos = [nombres, apellidos]
        # Validar que solo tenga letras y espacios
        if not all(re.match(r'^[A-Za-zÁÉÍÓÚÑáéíóúñ\s]+$', campo) for campo in campos):
            msg = crear_msgbox(
                    self,
                    "Error",
                    "Los campos de texto solo pueden contener letras y espacios.",
                    QMessageBox.Warning,
                )
            msg.exec()
            return
        nombres = " ".join(p.capitalize() for p in nombres.split())
        apellidos = " ".join(p.capitalize() for p in apellidos.split())
        
        estudiante_data = {
            "cedula": self.cedula_estudiantil_generada,
            "apellidos": apellidos,
            "nombres": nombres,
            "fecha_nac_est": self.lneFechaNac_reg_estu.date().toPython(),
            "city": self.lneCity_reg_estu.text().strip(),
            "genero": self.cbxGenero_reg_estu.currentText().strip(),
            "direccion": self.lneDir_reg_estu.text().strip(),
            "fecha_ingreso": self.lneFechaIng_reg_estu.date().toPython(),
            "tipo_educacion": self.cbxTipoEdu_reg_estu.currentText().strip(),
            "grado": self.cbxGrado_reg_estu.currentText().strip(),
            "seccion": self.cbxSeccion_reg_estu.currentText().strip(),
            "docente": self.lneDocente_reg_estu.text().strip(),
            "tallaC": self.lneTallaC_reg_estu.text().strip(),
            "tallaP": self.lneTallaP_reg_estu.text().strip(),
            "tallaZ": self.lneTallaZ_reg_estu.text().strip(),
            "madre": self.lneMadre_reg_estu.text().strip(),
            "madre_ci": self.lneCI_madre_reg_estu.text().strip(),
            "ocupacion_madre": self.lneOcup_madre_reg_estu.text().strip(),
            "padre": self.lnePadre_reg_estu.text().strip(),
            "padre_ci": self.lneCI_padre_reg_estu.text().strip(),
            "ocupacion_padre": self.lneOcup_padre_reg_estu.text().strip(),
        }

        # --- Datos representante ---
        nombres_repre = self.lneNombre_reg_estu_repre.text().strip()
        apellidos_repre = self.lneApellido_reg_estu_repre.text().strip()
        campos_repre = [nombres_repre, apellidos_repre]
        # Validar que solo tenga letras y espacios
        if not all(re.match(r'^[A-Za-zÁÉÍÓÚÑáéíóúñ\s]+$', campo) for campo in campos_repre):
            msg = crear_msgbox(
                    self,
                    "Error",
                    "Los campos de texto solo pueden contener letras y espacios.",
                    QMessageBox.Warning,
                )
            msg.exec()
            return
        nombres_repre = " ".join(p.capitalize() for p in nombres_repre.split())
        apellidos_repre = " ".join(p.capitalize() for p in apellidos_repre.split())

        representante_data = {
            "cedula_repre": self.lneCedula_reg_estu_repre.text().strip(),
            "apellidos_repre": nombres_repre,
            "nombres_repre": apellidos_repre,
            "fecha_nac_repre": self.lneFechaNac_reg_estu_repre.date().toPython(),
            "genero_repre": self.cbxGenero_reg_estu_repre.currentText().strip(),
            "direccion_repre": self.lneDir_reg_estu_repre.text().strip(),
            "num_contact_repre": self.lneNum_reg_estu_repre.text().strip(),
            "correo_repre": self.lneCorreo_reg_estu_repre.text().strip(),
            "observacion": self.lneObser_reg_estu_repre.text().strip(),
        }

        if not estudiante_data["nombres"] or not estudiante_data["apellidos"] or not estudiante_data["madre"]:
            msg = crear_msgbox(
                    self,
                    "Campos incompletos",
                    "Por favor completa los campos obligatorios.",
                    QMessageBox.Warning,
                )
            msg.exec()
            return

        try:
            EstudianteModel.guardar(estudiante_data, representante_data, self.usuario_actual)
            msg = crear_msgbox(
                    self,
                    "Éxito",
                    "Registro guardado correctamente.",
                    QMessageBox.Information,
                )
            msg.exec()
            self.close()
        except Exception as err:
            msg = crear_msgbox(
                    self,
                    "Error",
                    f"No se pudo guardar: {err}",
                    QMessageBox.Critical,
                )
            msg.exec()
