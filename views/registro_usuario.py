import re
from ui_compiled.registro_user_ui import Ui_registro_user
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Qt
from models.user_model import UsuarioModel
from utils.dialogs import crear_msgbox
from utils.sombras import crear_sombra_flotante


class RegistroUsuario(QDialog, Ui_registro_user):
    """Formulario de registro de usuarios."""
    
    def __init__(self, usuario_actual, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual

        self.setupUi(self)
        self.setWindowTitle("Nuevo registro de usuario")

        # Conectar botones
        self.btnRegistrar_user.clicked.connect(self.guardar_en_bd)
        self.btnCancelar_reg_user.clicked.connect(self.reject)

        # Deshabilitar placeholder del combo
        model = self.cbxRol_reg_user.model()
        item0 = model.item(0)
        if item0:
            item0.setEnabled(False)
            item0.setForeground(Qt.GlobalColor.gray)

        # Sombras
        crear_sombra_flotante(self.btnRegistrar_user)
        crear_sombra_flotante(self.btnCancelar_reg_user)
        crear_sombra_flotante(self.lneNombreCompleto_reg_user, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lnePass_reg_user, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lneRepPass_reg_user, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lneUsername_reg_user, blur_radius=8, y_offset=1)
        
    def guardar_en_bd(self):
        """Valida y guarda el nuevo usuario."""
        
        # --- VALIDACIÓN DE NOMBRE COMPLETO ---
        nombre = self.lneNombreCompleto_reg_user.text().strip()
        
        if not nombre:
            crear_msgbox(
                self,
                "Campo requerido",
                "El nombre completo es obligatorio.",
                QMessageBox.Warning,
            ).exec()
            return
        
        # Solo letras y espacios
        if not re.match(r'^[A-Za-zÁÉÍÓÚÑáéíóúñ\s]+$', nombre):
            crear_msgbox(
                self,
                "Formato inválido",
                "El nombre solo puede contener letras y espacios.",
                QMessageBox.Warning,
            ).exec()
            return
        
        # Capitalizar correctamente
        nombre = " ".join(p.capitalize() for p in nombre.split())

        # --- VALIDACIÓN DE USERNAME ---
        username = self.lneUsername_reg_user.text().strip()
        
        if not username:
            crear_msgbox(
                self,
                "Campo requerido",
                "El nombre de usuario es obligatorio.",
                QMessageBox.Warning,
            ).exec()
            return
        
        # Sin espacios, alfanumérico, guiones bajos permitidos
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            crear_msgbox(
                self,
                "Formato inválido",
                "El username solo puede contener letras, números y guiones bajos (sin espacios).",
                QMessageBox.Warning,
            ).exec()
            return
        
        if len(username) < 3:
            crear_msgbox(
                self,
                "Username muy corto",
                "El nombre de usuario debe tener al menos 3 caracteres.",
                QMessageBox.Warning,
            ).exec()
            return

        # --- VALIDACIÓN DE ROL ---
        rol = self.cbxRol_reg_user.currentText().strip()
        
        if not rol or rol == "Seleccionar un rol":
            crear_msgbox(
                self,
                "Campo requerido",
                "Debe seleccionar un rol válido.",
                QMessageBox.Warning,
            ).exec()
            return

        # --- VALIDACIÓN DE CONTRASEÑA ---
        password = self.lnePass_reg_user.text().strip()
        rep_password = self.lneRepPass_reg_user.text().strip()
        
        if not password:
            crear_msgbox(
                self,
                "Campo requerido",
                "La contraseña es obligatoria.",
                QMessageBox.Warning,
            ).exec()
            return
        
        if len(password) < 6:
            crear_msgbox(
                self,
                "Contraseña débil",
                "La contraseña debe tener al menos 6 caracteres.",
                QMessageBox.Warning,
            ).exec()
            return
        
        if password != rep_password:
            crear_msgbox(
                self,
                "Contraseñas no coinciden",
                "La contraseña y su repetición deben ser idénticas.",
                QMessageBox.Warning,
            ).exec()
            return

        # --- PREPARAR DATOS ---
        usuario_data = {
            "nombre_completo": nombre,
            "username": username,
            "password": password,
            "rol": rol,
        }

        # --- GUARDAR EN BD ---
        try:
            ok, mensaje = UsuarioModel.guardar(usuario_data, self.usuario_actual)
            
            if ok:
                crear_msgbox(
                    self,
                    "Éxito",
                    mensaje,
                    QMessageBox.Information,
                ).exec()
                self.accept()  # Cerrar con éxito
            else:
                crear_msgbox(
                    self,
                    "Error al guardar",
                    mensaje,
                    QMessageBox.Warning,
                ).exec()
                
        except Exception as err:
            crear_msgbox(
                self,
                "Error inesperado",
                f"No se pudo guardar el usuario: {err}",
                QMessageBox.Critical,
            ).exec()