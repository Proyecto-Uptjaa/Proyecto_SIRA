from PySide6.QtWidgets import QDialog, QMessageBox

from utils.db import get_user_by_username
from utils.security import check_password
from utils.dialogs import crear_msgbox

from ui_compiled.login_ui import Ui_login


class LoginDialog(QDialog, Ui_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)   # esto mete todos los widgets en self
        self.setWindowTitle("Inicio de sesión - SIRA")

        self.btnLogin.clicked.connect(self.on_login_clicked)

    def on_login_clicked(self):
        username = self.inputUser.text().strip()
        password = self.inputPassword.text()

        # Buscar usuario en la BD
        user = get_user_by_username(username)
        if not user:
            msg = crear_msgbox(
                    self,
                    "Error",
                    "Usuario no encontrado.",
                    QMessageBox.Warning,
                )
            msg.exec()
            return

        if user["estado"] == 0:
            msg = crear_msgbox(
                    self,
                    "Error",
                    "Cuenta deshabilitada. Contacte con el administrador.",
                    QMessageBox.Warning,
                )
            msg.exec()
            return

        if check_password(password, user["password_hash"]):
            # Guardar info del usuario logueado con rol incluido
            self.usuario = {
                "id": user["id"],
                "username": user["username"],
                "rol": user["rol"],
                "estado": user["estado"]
            }
            self.accept()
        else:
            msg = crear_msgbox(
                    self,
                    "Error",
                    "Contraseña incorrecta",
                    QMessageBox.Warning,
                )
            msg.exec()
