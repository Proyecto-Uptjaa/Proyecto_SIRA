from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Signal, Qt

from models.user_model import UsuarioModel
from ui_compiled.actualizar_user_ui import Ui_actualizar_user
from utils.dialogs import crear_msgbox
from utils.sombras import crear_sombra_flotante


class ActualizarUsuario(QDialog, Ui_actualizar_user):
    """Formulario de actualización de usuarios."""
    
    datos_actualizados = Signal()

    def __init__(self, id_usuario, usuario_actual, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.id = id_usuario
        self.id_usuario = id_usuario

        self.setupUi(self)
        self.setWindowTitle("Actualizar datos usuario")

        # Deshabilitar placeholder del combo
        model = self.cbxRol_actu_user.model()
        item0 = model.item(0)
        if item0:
            item0.setEnabled(False)
            item0.setForeground(Qt.GlobalColor.gray)

        # Cargar datos
        self.cargar_datos()

        # Conectar botones
        self.btnActualizar_user.clicked.connect(self.guardar_datos)
        self.btnCancelar_actu_user.clicked.connect(self.reject)

        self. aplicar_sombras()

    def aplicar_sombras(self):
        # Sombras
        crear_sombra_flotante(self.btnActualizar_user)
        crear_sombra_flotante(self.btnCancelar_actu_user)
        crear_sombra_flotante(self.lneNombreCompleto_actu_user, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lnePass_actu_user, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lneRepPass_actu_user, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lneUsername_actu_user, blur_radius=8, y_offset=1)

    def cargar_datos(self):
        """Carga los datos del usuario en el formulario."""
        datos = UsuarioModel.obtener_por_id(self.id)

        if not datos:
            crear_msgbox(
                self,
                "Error",
                f"No se encontró el usuario con ID {self.id}",
                QMessageBox.Critical
            ).exec()
            self.reject()
            return

        # Mostrar datos
        self.lneNombreCompleto_actu_user.setText(str(datos["nombre_completo"]))
        self.lneUsername_actu_user.setText(str(datos["username"]))
        
        # Campos de solo lectura
        self.lneNombreCompleto_actu_user.setReadOnly(True)
        self.lneUsername_actu_user.setReadOnly(True)
        
        # Seleccionar rol actual
        index = self.cbxRol_actu_user.findText(str(datos["rol"]))
        if index >= 0:
            self.cbxRol_actu_user.setCurrentIndex(index)

    def guardar_datos(self):
        """Valida y guarda los cambios."""
        
        # --- VALIDAR ROL ---
        rol = self.cbxRol_actu_user.currentText().strip()
        
        if not rol or rol == "Seleccionar un rol":
            crear_msgbox(
                self,
                "Campo requerido",
                "Debe seleccionar un rol válido.",
                QMessageBox.Warning,
            ).exec()
            return

        # --- DATOS BASE ---
        usuario_data = {
            "rol": rol,
        }

        # --- VALIDAR CONTRASEÑA (SI SE PROPORCIONA) ---
        pass_user = self.lnePass_actu_user.text().strip()
        pass_rep = self.lneRepPass_actu_user.text().strip()

        if pass_user or pass_rep:
            if not pass_user:
                crear_msgbox(
                    self,
                    "Campo incompleto",
                    "Ingrese la nueva contraseña.",
                    QMessageBox.Warning,
                ).exec()
                return
            
            if len(pass_user) < 6:
                crear_msgbox(
                    self,
                    "Contraseña débil",
                    "La nueva contraseña debe tener al menos 6 caracteres.",
                    QMessageBox.Warning,
                ).exec()
                return
            
            if pass_user != pass_rep:
                crear_msgbox(
                    self,
                    "Contraseñas no coinciden",
                    "La contraseña y su repetición deben ser idénticas.",
                    QMessageBox.Warning,
                ).exec()
                return
            
            usuario_data["password"] = pass_user

        # --- GUARDAR EN BD ---
        try:
            ok, mensaje = UsuarioModel.actualizar(
                self.id, 
                usuario_data, 
                self.usuario_actual
            )
            
            if ok:
                crear_msgbox(
                    self,
                    "Éxito",
                    mensaje,
                    QMessageBox.Information,
                ).exec()
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
                "Error inesperado",
                f"No se pudo guardar cambios: {err}",
                QMessageBox.Critical,
            ).exec()
