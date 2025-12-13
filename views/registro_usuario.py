import re
from ui_compiled.registro_user_ui import Ui_registro_user
from PySide6.QtWidgets import QDialog, QMessageBox
from models.user_model import UsuarioModel
from utils.dialogs import crear_msgbox
from utils.sombras import crear_sombra_flotante


class RegistroUsuario(QDialog, Ui_registro_user):
    def __init__(self, usuario_actual, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual

        self.setupUi(self)   # esto mete todos los widgets en self

        # Ventana Registro usuario
        self.setWindowTitle("Nuevo registro de usuario")

        # Botones
        self.btnRegistrar_user.clicked.connect(self.guardar_en_bd)
        self.btnCancelar_reg_user.clicked.connect(self.reject)

        ## Sombras de elementos ##
        crear_sombra_flotante(self.btnRegistrar_user)
        crear_sombra_flotante(self.btnCancelar_reg_user)
        crear_sombra_flotante(self.lneNombreCompleto_reg_user, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lnePass_reg_user, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lneRepPass_reg_user, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lneUsername_reg_user, blur_radius=8, y_offset=1)
        
    def guardar_en_bd(self):

        
        # --- Datos usuario ---
        nombre = self.lneNombreCompleto_reg_user.text().strip()

        # Validar que solo tenga letras y espacios
        if not re.match(r'^[A-Za-zÁÉÍÓÚÑáéíóúñ\s]+$', nombre):
            msg = crear_msgbox(
                    self,
                    "Error",
                    "El nombre solo puede contener letras y espacios.",
                    QMessageBox.Warning,
                )
            msg.exec()
            return
        
        nombre = " ".join(p.capitalize() for p in nombre.split())

        usuario_data = {
            "nombre_completo": nombre,
            "username": self.lneUsername_reg_user.text().strip(),
            "password": self.lnePass_reg_user.text().strip(),
            "rol": self.cbxRol_reg_user.currentText().strip(),
        }

        if not usuario_data["username"] or not usuario_data["password"] or not usuario_data["rol"]:
            msg = crear_msgbox(
                    self,
                    "Campos incompletos",
                    "Por favor, completa los campos obligatorios.",
                    QMessageBox.Warning,
                )
            msg.exec()
            return
        
        if self.lnePass_reg_user.text().strip() == self.lneRepPass_reg_user.text().strip():
            try:
                UsuarioModel.guardar(usuario_data, self.usuario_actual)
                msg = crear_msgbox(
                    self,
                    "Éxito",
                    "Usuario creado correctamente.",
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
        else:
            msg = crear_msgbox(
                    self,
                    "La contraseña no coincide",
                    "Por favor revise la repeticion de contraseña.",
                    QMessageBox.Warning,
                )
            msg.exec()
            return