import re

from utils.forms import limpiar_widgets
from utils.edad import calcular_edad
from utils.dialogs import crear_msgbox

from ui_compiled.registro_emple_ui import Ui_registro_emple
from PySide6.QtWidgets import QDialog, QMessageBox

from models.emple_model import EmpleadoModel


class RegistroEmpleado(QDialog, Ui_registro_emple):
    def __init__(self, usuario_actual, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual

        self.setupUi(self)   # esto mete todos los widgets en self

        # Ventana Registro empleado
        self.setWindowTitle("Nuevo registro de empleado v0.5")
        self.stackRegistro_emple.setCurrentIndex(0)

        # Botones
        self.btnGuardar_reg_emple.clicked.connect(self.guardar_en_bd)
        self.btnDatosPersonales_reg_emple.clicked.connect(
            lambda: self.cambiar_pagina_registro_empleado(0)
        )
        self.btnDatosLaborales_reg_emple.clicked.connect(
            lambda: self.cambiar_pagina_registro_empleado(1)
        )
        self.btnLimpiar_reg_emple.clicked.connect(self.limpiar_formulario)

        # Conectar cálculo automático de edad
        self.lneFechaNac_reg_emple.dateChanged.connect(self.actualizar_edad_empleado)

    def limpiar_formulario(self):
        limpiar_widgets(self)

    # --- Funciones de cálculo de edad ---
    def actualizar_edad_empleado(self):
        qdate = self.lneFechaNac_reg_emple.date()
        fecha_nac = qdate.toPython()
        edad = calcular_edad(fecha_nac)
        self.lneEdad_reg_emple.setText(str(edad))

    def cambiar_pagina_registro_empleado(self, indice):
        self.stackRegistro_emple.setCurrentIndex(indice)

    def guardar_en_bd(self):
        # --- Datos empleado ---
        nombres = self.lneNombres_reg_emple.text().strip()
        apellidos = self.lneApellidos_reg_emple.text().strip()
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

        empleado_data = {
            "cedula": self.lneCedula_reg_emple.text().strip(),
            "apellidos": apellidos,
            "nombres": nombres,
            "fecha_nac": self.lneFechaNac_reg_emple.date().toPython(),
            "genero": self.lneGenero_reg_emple.text().strip(),
            "direccion": self.lneDir_reg_emple.text().strip(),
            "num_contact": self.lneNum_reg_emple.text().strip(),
            "correo": self.lneCorreo_reg_emple.text().strip(),
            "titulo": self.cbxTitulo_reg_emple.currentText().strip(),
            "cargo": self.lneCargo_reg_emple.text().strip(),
            "fecha_ingreso": self.lneFechaIngreso_reg_emple.text().strip(),
            "num_carnet": self.lneCarnet_reg_emple.text().strip(),
            "rif": self.lneRIF_reg_emple.text.strip(),
            "centro_votacion": self.lneCentroV_reg_emple.text.strip(),
            "codigo_rac": self.lneRAC_reg_emple.text().strip(),
        }

        if not empleado_data["nombres"] or not empleado_data["apellidos"] or not empleado_data["cedula"]:
            msg = crear_msgbox(
                    self,
                    "Campos incompletos",
                    "Por favor completa los campos obligatorios.",
                    QMessageBox.Warning,
                )
            msg.exec()
            return

        try:
            EmpleadoModel.guardar(empleado_data, self.usuario_actual)
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
