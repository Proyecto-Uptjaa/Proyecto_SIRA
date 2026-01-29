import re
from ui_compiled.config_inicial_ui import Ui_config_inicial
from utils.sombras import crear_sombra_flotante
from PySide6.QtWidgets import QDialog, QMessageBox, QLineEdit
from models.user_model import UsuarioModel
from models.institucion_model import InstitucionModel
from utils.dialogs import crear_msgbox

class Config_inicial(QDialog, Ui_config_inicial):
    """Ventana de configuración inicial"""
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowTitle("Configuración Inicial")
        self.stackedWidget.setCurrentIndex(0)

        # Conectar botones
        self.btnSiguiente.clicked.connect(self.pagina_siguiente)
        self.btnAtras.clicked.connect(self.pagina_anterior)
        
        # Actualizar estado de botones al iniciar
        self.actualizar_botones()
        
        # Configurar campos de contraseña
        self.lnePass_admin.setEchoMode(QLineEdit.Password)
        self.lneRepPass_admin.setEchoMode(QLineEdit.Password)
        
        # Conectar checkbox de licencia para habilitar/deshabilitar botón Finalizar
        self.chkLicencia.stateChanged.connect(self.actualizar_botones)
        
        # Sombras
        crear_sombra_flotante(self.btnSiguiente)
        crear_sombra_flotante(self.btnAtras)
        crear_sombra_flotante(self.lblLogo_SIRA, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lblLogo_UPTJAA_acercade, blur_radius=8, y_offset=1)

    def pagina_siguiente(self):
        """Avanza a la siguiente página o finaliza el proceso."""
        indice_actual = self.stackedWidget.currentIndex()
        total_paginas = self.stackedWidget.count()
                
        # Validar página actual antes de avanzar
        if indice_actual == 1:  # Página de usuario
            if not self.validar_datos_usuario():
                return
        elif indice_actual == 2:  # Página de institución
            if not self.validar_datos_institucion():
                return
        elif indice_actual == 3:  # Página de licencia
            if not self.chkLicencia.isChecked():
                crear_msgbox(
                    self,
                    "Licencia requerida",
                    "Debe aceptar los términos de la licencia para continuar.",
                    QMessageBox.Warning,
                ).exec()
                return
        elif indice_actual == 4:  # Página final - ejecutar guardado
            self.guardar_configuracion_inicial()
            return
        
        # Avanzar a la siguiente página
        if indice_actual < total_paginas - 1:
            self.stackedWidget.setCurrentIndexInstant(indice_actual + 1)
            self.actualizar_botones()
    
    def pagina_anterior(self):
        indice_actual = self.stackedWidget.currentIndex()
        
        if indice_actual > 0:
            self.stackedWidget.setCurrentIndexInstant(indice_actual - 1)
            self.actualizar_botones()
    
    def actualizar_botones(self):
        """Actualiza el estado de los botones según la página actual."""
        indice_actual = self.stackedWidget.currentIndex()
        total_paginas = self.stackedWidget.count()
        
        # Deshabilitar/ocultar botón Atrás en la primera página
        self.btnAtras.setEnabled(indice_actual > 0)
        
        # Página 4 - botón Finalizar
        if indice_actual == 4:
            self.btnSiguiente.setText("Finalizar")
            self.btnSiguiente.setEnabled(True)
            self.btnSiguiente.setVisible(True)
        else:
            self.btnSiguiente.setText("Siguiente")
            self.btnSiguiente.setEnabled(True)
            self.btnSiguiente.setVisible(True)
    
    def validar_datos_usuario(self) -> bool:
        """Valida los datos del usuario administrador."""
        # VALIDACIÓN DE NOMBRE COMPLETO
        nombre = self.lneNombreCompleto_admin.text().strip()
        
        if not nombre:
            crear_msgbox(
                self,
                "Campo requerido",
                "El nombre completo del administrador es obligatorio.",
                QMessageBox.Warning,
            ).exec()
            return False
        
        # Solo letras y espacios
        if not re.match(r'^[A-Za-zÁÉÍÓÚÑáéíóúñ\s]+$', nombre):
            crear_msgbox(
                self,
                "Formato inválido",
                "El nombre solo puede contener letras y espacios.",
                QMessageBox.Warning,
            ).exec()
            return False

        # VALIDACIÓN DE USERNAME
        username = self.lneUsername_admin.text().strip()
        
        if not username:
            crear_msgbox(
                self,
                "Campo requerido",
                "El nombre de usuario es obligatorio.",
                QMessageBox.Warning,
            ).exec()
            return False
        
        # Sin espacios, alfanumérico, guiones bajos permitidos
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            crear_msgbox(
                self,
                "Formato inválido",
                "El username solo puede contener letras, números y guiones bajos.",
                QMessageBox.Warning,
            ).exec()
            return False
        
        if len(username) < 3:
            crear_msgbox(
                self,
                "Username muy corto",
                "El nombre de usuario debe tener al menos 3 caracteres.",
                QMessageBox.Warning,
            ).exec()
            return False

        # VALIDACIÓN DE CONTRASEÑA
        password = self.lnePass_admin.text().strip()
        rep_password = self.lneRepPass_admin.text().strip()
        
        if not password:
            crear_msgbox(
                self,
                "Campo requerido",
                "La contraseña es obligatoria.",
                QMessageBox.Warning,
            ).exec()
            return False
        
        if len(password) < 6:
            crear_msgbox(
                self,
                "Contraseña débil",
                "La contraseña debe tener al menos 6 caracteres.",
                QMessageBox.Warning,
            ).exec()
            return False
        
        if password != rep_password:
            crear_msgbox(
                self,
                "Contraseñas no coinciden",
                "La contraseña y su repetición deben ser idénticas.",
                QMessageBox.Warning,
            ).exec()
            return False
        
        return True
    
    def validar_datos_institucion(self) -> bool:
        """Valida los datos de la institución."""
        # VALIDACIÓN CÓDIGO DEA
        codigo_dea = self.lneCodigoDEA.text().strip()
        
        if not codigo_dea:
            crear_msgbox(
                self,
                "Campo requerido",
                "El código DEA es obligatorio.",
                QMessageBox.Warning,
            ).exec()
            return False
        
        if len(codigo_dea) < 3:
            crear_msgbox(
                self,
                "Código muy corto",
                "El código DEA debe tener al menos 3 caracteres.",
                QMessageBox.Warning,
            ).exec()
            return False

        # VALIDACIÓN DIRECTOR
        director = self.lneDirectorName.text().strip()
        
        if not director:
            crear_msgbox(
                self,
                "Campo requerido",
                "El nombre del director es obligatorio.",
                QMessageBox.Warning,
            ).exec()
            return False
        
        # Solo letras y espacios
        if not re.match(r'^[A-Za-zÁÉÍÓÚÑáéíóúñ\s]+$', director):
            crear_msgbox(
                self,
                "Formato inválido",
                "El nombre del director solo puede contener letras y espacios.",
                QMessageBox.Warning,
            ).exec()
            return False

        # VALIDACIÓN CÉDULA DIRECTOR
        director_ci = self.lneDirectorCI.text().strip()
        
        if not director_ci:
            crear_msgbox(
                self,
                "Campo requerido",
                "La cédula del director es obligatoria.",
                QMessageBox.Warning,
            ).exec()
            return False
        
        # Solo números
        if not director_ci.replace(".", "").replace("-", "").isdigit():
            crear_msgbox(
                self,
                "Formato inválido",
                "La cédula del director debe ser numérica.",
                QMessageBox.Warning,
            ).exec()
            return False
        
        return True
    
    def guardar_configuracion_inicial(self):
        """Guarda el usuario y los datos de la institución."""
        
        # Validar datos una última vez
        if not self.validar_datos_usuario():
            self.stackedWidget.setCurrentIndex(1)  # Volver a página de usuario
            return
        
        if not self.validar_datos_institucion():
            self.stackedWidget.setCurrentIndex(2)  # Volver a página de institución
            return
        
        # VALIDAR DATOS DE USUARIO
        nombre = self.lneNombreCompleto_admin.text().strip()
        nombre = " ".join(p.capitalize() for p in nombre.split())

        username = self.lneUsername_admin.text().strip()
        password = self.lnePass_admin.text().strip()
        
        usuario_data = {
            "nombre_completo": nombre,
            "username": username,
            "password": password,
            "rol": "Administrador",
        }
        
        # VALIDAR DATOS DE INSTITUCIÓN
        director_nombre = self.lneDirectorName.text().strip()
        director_nombre = " ".join(p.capitalize() for p in director_nombre.split())
        
        institucion_data = {
            "nombre": self.lneNombreInstitucion.text().strip(),
            "codigo_dea": self.lneCodigoDEA.text().strip(),
            "director": director_nombre,
            "director_ci": self.lneDirectorCI.text().strip(),
            "direccion": "Por definir"
        }

        # GUARDAR EN BD
        try:
            # Usuario ficticio para auditoría (ID 0 = sistema)
            usuario_sistema = {"id": 0, "username": "sistema"}
            
            # 1. Guardar usuario
            ok_user, mensaje_user = UsuarioModel.guardar(usuario_data, usuario_sistema)
            
            if not ok_user:
                crear_msgbox(
                    self,
                    "Error al guardar usuario",
                    mensaje_user,
                    QMessageBox.Warning,
                ).exec()
                return
            
            # 2. Inicializar registro de institución si no existe
            InstitucionModel.inicializar_si_no_existe()
            
            # 3. Actualizar datos de institución
            ok_inst, mensaje_inst = InstitucionModel.actualizar(1, institucion_data, usuario_sistema)
            
            if not ok_inst:
                crear_msgbox(
                    self,
                    "Advertencia",
                    f"Usuario creado correctamente, pero hubo un error al guardar datos institucionales:\n{mensaje_inst}",
                    QMessageBox.Warning,
                ).exec()
                # Aún así aceptar el diálogo
                self.accept()
                return
            
            # 4. Éxito completo - cerrar diálogo
            self.accept()  # Cerrar con éxito
                
        except Exception as err:
            crear_msgbox(
                self,
                "Error inesperado",
                f"No se pudo completar la configuración: {err}",
                QMessageBox.Critical,
            ).exec()
    
    def cambiar_pagina_main(self, indice):
        """Cambia directamente a una página específica."""
        self.stackedWidget.setCurrentIndexInstant(indice)
        self.actualizar_botones()
