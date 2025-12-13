from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Signal

from models.user_model import UsuarioModel
from ui_compiled.actualizar_user_ui import Ui_actualizar_user
from utils.dialogs import crear_msgbox
from utils.sombras import crear_sombra_flotante


class ActualizarUsuario(QDialog, Ui_actualizar_user):
    datos_actualizados = Signal()

    def __init__(self, id_usuario, usuario_actual, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.id = id_usuario
        self.id_usuario = id_usuario

        self.setupUi(self)

        self.setWindowTitle("Actualizar datos usuario")

        # Cargar datos
        self.cargar_datos()
        self.cbxRol_actu_user.model().item(0).setEnabled(False)

        # Conectar señales de botones
        self.btnActualizar_user.clicked.connect(self.guardar_datos)
        self.btnCancelar_actu_user.clicked.connect(self.reject)

        ## Sombras de elementos ##
        crear_sombra_flotante(self.btnActualizar_user)
        crear_sombra_flotante(self.btnCancelar_actu_user)
        crear_sombra_flotante(self.lneNombreCompleto_actu_user, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lnePass_actu_user, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lneRepPass_actu_user, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lneUsername_actu_user, blur_radius=8, y_offset=1)

    def cargar_datos(self):
        datos = UsuarioModel.obtener_por_id(self.id)

        if datos:
            self.lneNombreCompleto_actu_user.setText(str(datos["nombre_completo"]))
            self.lneUsername_actu_user.setText(str(datos["username"]))
            index = self.cbxRol_actu_user.findText(str(datos["rol"]))
            if index >= 0:
                self.cbxRol_actu_user.setCurrentIndex(index)

    def guardar_datos(self):
        pass_user = self.lnePass_actu_user.text().strip()
        pass_rep = self.lneRepPass_actu_user.text().strip()

        try:
            # --- Validar rol ---
            rol = self.cbxRol_actu_user.currentText().strip()
            if rol == "Seleccionar un rol":
                msg = crear_msgbox(
                    self,
                    "Rol inválido",
                    "Debe seleccionar un rol válido antes de continuar.",
                    QMessageBox.Warning,
                )
                msg.exec()
                return

            # --- Datos usuario ---
            usuario_data = {
                "rol": rol,
            }

            # --- Validar contraseñas ---
            if pass_user or pass_rep:  # si alguno de los campos tiene algo
                if pass_user == pass_rep:
                    usuario_data["password"] = pass_user
                else:
                    msg = crear_msgbox(
                        self,
                        "La contraseña no coincide",
                        "Por favor revise la repetición de contraseña.",
                        QMessageBox.Warning,
                    )
                    msg.exec()
                    return

            UsuarioModel.actualizar(self.id, usuario_data, self.usuario_actual)
            msg = crear_msgbox(
                self,
                "Éxito",
                "Datos actualizados correctamente.",
                QMessageBox.Information,
            )
            msg.exec()
            self.datos_actualizados.emit()
            self.accept()

        except Exception as err:
            msg = crear_msgbox(
                self,
                "Error",
                f"No se pudo guardar cambios: {err}",
                QMessageBox.Critical,
            )
            msg.exec()
