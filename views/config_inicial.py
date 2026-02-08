import re
from ui_compiled.config_inicial_ui import Ui_config_inicial
from utils.sombras import crear_sombra_flotante
from PySide6.QtWidgets import QDialog, QMessageBox, QLineEdit
from models.user_model import UsuarioModel
from models.institucion_model import InstitucionModel
from utils.dialogs import crear_msgbox
from datetime import datetime

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
        
        # Configurar página de año escolar
        self.anio_confirmado = False
        self.lneAnio_escolar.setMaxLength(9)  # Para formato "2025-2026"
        self.btnConfirmar_anio.clicked.connect(self.on_confirmar_anio)
        self.lneAnio_Inicio.textChanged.connect(self.on_anio_inicio_changed)
        
        # Conectar checkbox de licencia para habilitar/deshabilitar botón Finalizar
        self.chkLicencia.stateChanged.connect(self.actualizar_botones)
        
        # Sombras
        crear_sombra_flotante(self.btnSiguiente)
        crear_sombra_flotante(self.btnAtras)
        crear_sombra_flotante(self.lneNombreCompleto_admin, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lneUsername_admin, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lnePass_admin, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lneRepPass_admin, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lneRol_admin, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lneNombreInstitucion, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lneDirectorName, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lneDirectorCI, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lneCodigoDEA, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lneAnio_Inicio, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lneAnio_escolar, blur_radius=8, y_offset=1)
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
        elif indice_actual == 3:  # Página de año escolar
            if not self.validar_datos_anio():
                return
        elif indice_actual == 4:  # Página de licencia
            if not self.chkLicencia.isChecked():
                crear_msgbox(
                    self,
                    "Licencia requerida",
                    "Debe aceptar los términos de la licencia para continuar.",
                    QMessageBox.Warning,
                ).exec()
                return
        elif indice_actual == 5:  # Página final - ejecutar guardado
            self.guardar_configuracion_inicial()
            return
        
        # Avanzar a la siguiente página
        if indice_actual < total_paginas - 1:
            self.stackedWidget.setCurrentIndex(indice_actual + 1)
            self.actualizar_botones()
    
    def pagina_anterior(self):
        indice_actual = self.stackedWidget.currentIndex()
        
        if indice_actual > 0:
            self.stackedWidget.setCurrentIndex(indice_actual - 1)
            self.actualizar_botones()
    
    def actualizar_botones(self):
        """Actualiza el estado de los botones según la página actual."""
        indice_actual = self.stackedWidget.currentIndex()
        total_paginas = self.stackedWidget.count()
        
        # Deshabilitar/ocultar botón Atrás en la primera página
        self.btnAtras.setEnabled(indice_actual > 0)
        self.btnAtras.setVisible(indice_actual > 0)
        
        # Página 5 (final) - botón Finalizar
        if indice_actual == 5:
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
    
    def on_confirmar_anio(self):
        """Valida el año de inicio y muestra el año escolar formateado."""
        texto = self.lneAnio_Inicio.text().strip()
        
        if not texto.isdigit() or len(texto) != 4:
            crear_msgbox(
                self,
                "Año inválido",
                "Ingrese un año válido de 4 dígitos (Ej: 2026).",
                QMessageBox.Warning,
            ).exec()
            self.lneAnio_escolar.clear()
            self.anio_confirmado = False
            return
        
        anio_inicio = int(texto)
        
        if anio_inicio < 2000 or anio_inicio > 2100:
            crear_msgbox(
                self,
                "Año fuera de rango",
                "El año debe estar entre 2000 y 2100.",
                QMessageBox.Warning,
            ).exec()
            self.lneAnio_escolar.clear()
            self.anio_confirmado = False
            return
        
        anio_fin = anio_inicio + 1
        self.lneAnio_escolar.setText(f"{anio_inicio}-{anio_fin}")
        self.anio_confirmado = True
    
    def on_anio_inicio_changed(self):
        """Resetea la confirmación si el usuario cambia el año de inicio."""
        self.lneAnio_escolar.clear()
        self.anio_confirmado = False
    
    def validar_datos_anio(self) -> bool:
        """Valida que el año escolar haya sido confirmado."""
        if not self.anio_confirmado or not self.lneAnio_escolar.text().strip():
            crear_msgbox(
                self,
                "Año escolar requerido",
                "Debe ingresar el año de inicio y presionar el botón de confirmar.",
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
        
        if not self.validar_datos_anio():
            self.stackedWidget.setCurrentIndex(3)  # Volver a página de año escolar
            return
        
        # Recopilar datos de usuario
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
        
        # Recopilar datos de institución
        director_nombre = self.lneDirectorName.text().strip()
        director_nombre = " ".join(p.capitalize() for p in director_nombre.split())
        
        institucion_data = {
            "nombre": self.lneNombreInstitucion.text().strip(),
            "codigo_dea": self.lneCodigoDEA.text().strip(),
            "director": director_nombre,
            "director_ci": self.lneDirectorCI.text().strip(),
            "direccion": "Por definir"
        }
        
        # Recopilar datos de año escolar
        anio_inicio = int(self.lneAnio_Inicio.text().strip())
        anio_fin = anio_inicio + 1
        nombre_anio = f"{anio_inicio}-{anio_fin}"

        # Guardar en bd
        from utils.db import get_connection
        import bcrypt
        
        conexion = None
        cursor = None
        try:
            # Obtener conexión única para toda la transacción
            conexion = get_connection()
            if not conexion:
                crear_msgbox(
                    self,
                    "Error de conexión",
                    "No se pudo conectar a la base de datos.",
                    QMessageBox.Critical,
                ).exec()
                return
            
            cursor = conexion.cursor(dictionary=True)
            conexion.start_transaction()
            
            # 1. Crear o actualizar datos de institución
            
            cursor.execute("SELECT id FROM institucion WHERE id = 1")
            if not cursor.fetchone():
                # Crear registro inicial de institución
                cursor.execute("""
                    INSERT INTO institucion (id, nombre, codigo_dea, director, director_ci, direccion)
                    VALUES (1, %s, %s, %s, %s, %s)
                """, (
                    institucion_data["nombre"],
                    institucion_data["codigo_dea"],
                    institucion_data["director"],
                    institucion_data["director_ci"],
                    institucion_data["direccion"]
                ))
            else:
                # Actualizar registro existente
                cursor.execute("""
                    UPDATE institucion
                    SET nombre=%s, codigo_dea=%s, director=%s, director_ci=%s, direccion=%s
                    WHERE id=1
                """, (
                    institucion_data["nombre"],
                    institucion_data["codigo_dea"],
                    institucion_data["director"],
                    institucion_data["director_ci"],
                    institucion_data["direccion"]
                ))
            
            # 2. Crear usuario administrador
            
            # Verificar que no exista el username
            cursor.execute("SELECT id FROM usuarios WHERE username = %s", (username,))
            if cursor.fetchone():
                conexion.rollback()
                crear_msgbox(
                    self,
                    "Usuario duplicado",
                    f"El usuario '{username}' ya existe en el sistema.",
                    QMessageBox.Warning,
                ).exec()
                return
            
            # Hashear contraseña
            password_hash = bcrypt.hashpw(
                usuario_data["password"].encode("utf-8"),
                bcrypt.gensalt()
            ).decode("utf-8")
            
            # Insertar usuario
            cursor.execute("""
                INSERT INTO usuarios (nombre_completo, username, password_hash, rol, estado)
                VALUES (%s, %s, %s, %s, 1)
            """, (
                usuario_data["nombre_completo"],
                usuario_data["username"],
                password_hash,
                usuario_data["rol"]
            ))
            
            usuario_id = cursor.lastrowid
            
            # 3. Crear año escolar
            
            # Verificar que no exista ya ese año
            cursor.execute(
                "SELECT id FROM años_escolares WHERE año_inicio = %s",
                (anio_inicio,)
            )
            if cursor.fetchone():
                conexion.rollback()
                crear_msgbox(
                    self,
                    "Año existente",
                    f"El año escolar {nombre_anio} ya existe en el sistema.",
                    QMessageBox.Warning,
                ).exec()
                return
            
            fecha_inicio = datetime.now().strftime('%Y-%m-%d')
            cursor.execute("""
                INSERT INTO años_escolares
                (año_inicio, año_fin, nombre, fecha_inicio, estado, es_actual, creado_por, creado_en)
                VALUES (%s, %s, %s, %s, 'activo', 1, %s, NOW())
            """, (anio_inicio, anio_fin, nombre_anio, fecha_inicio, usuario_id))
            
            anio_id = cursor.lastrowid
            
            # 4. Registrar auditoría (usando el ID del admin recién creado)
            
            cursor.execute("""
                INSERT INTO auditoria (usuario_id, accion, entidad, entidad_id, referencia, descripcion, fecha)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                usuario_id,
                "INSERT",
                "usuarios",
                usuario_id,
                username,
                f"Configuración inicial: creó usuario administrador {nombre}",
                datetime.now()
            ))
            
            cursor.execute("""
                INSERT INTO auditoria (usuario_id, accion, entidad, entidad_id, referencia, descripcion, fecha)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                usuario_id,
                "INSERT",
                "institucion",
                1,
                institucion_data["nombre"],
                f"Configuración inicial: estableció datos de institución",
                datetime.now()
            ))
            
            cursor.execute("""
                INSERT INTO auditoria (usuario_id, accion, entidad, entidad_id, referencia, descripcion, fecha)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                usuario_id,
                "APERTURA_AÑO",
                "años_escolares",
                anio_id,
                nombre_anio,
                f"Configuración inicial: aperturó año escolar {nombre_anio}",
                datetime.now()
            ))
            
            # Commit de toda la transacción
            
            conexion.commit()
            
            # Éxito - cerrar diálogo
            self.accept()
                
        except Exception as err:
            if conexion:
                conexion.rollback()
            crear_msgbox(
                self,
                "Error en configuración inicial",
                f"No se pudo completar la configuración:\n{err}\n\nNingún cambio fue guardado.",
                QMessageBox.Critical,
            ).exec()
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
    
    def cambiar_pagina_main(self, indice):
        """Cambia directamente a una página específica."""
        self.stackedWidget.setCurrentIndex(indice)
        self.actualizar_botones()
