from utils.db import get_connection
import bcrypt
from models.auditoria_model import AuditoriaModel

class UsuarioModel:

    @staticmethod
    def guardar(usuario_data: dict, usuario_actual: dict):
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor()

            # 1. Hashear la contraseña antes de guardar
            password_hash = bcrypt.hashpw(
                usuario_data["password"].encode("utf-8"),
                bcrypt.gensalt()
            ).decode("utf-8")

            # 2. Insertar usuario
            sql_usuario = """
                INSERT INTO usuarios (nombre_completo, username, password_hash, rol)
                VALUES (%s, %s, %s, %s)
            """
            valores_usuario = (
                usuario_data["nombre_completo"],
                usuario_data["username"],
                password_hash,
                usuario_data["rol"],
            )
            cursor.execute(sql_usuario, valores_usuario)
            usuario_id = cursor.lastrowid

            # 3. Registrar en auditoría
            AuditoriaModel.registrar(
                usuario_id=usuario_actual["id"],   # el que está logueado
                accion="INSERT",
                entidad="usuarios",
                entidad_id=usuario_id,
                referencia=usuario_data["username"],
                descripcion=f"Se creó usuario {usuario_data['nombre_completo']} con rol {usuario_data['rol']}"
            )

            conexion.commit()
            return True, "Usuario registrado correctamente."

        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
   
    @staticmethod
    def actualizar(usuario_id: int, data: dict, usuario_actual: dict):
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor(dictionary=True)

            # 1. Obtener datos actuales
            cursor.execute("SELECT * FROM usuarios WHERE id=%s", (usuario_id,))
            usuario_db = cursor.fetchone()
            if not usuario_db:
                return False, "Usuario no encontrado."

            # 2. Preparar cambios
            cambios = []

            # Contraseña
            password_hash = None
            if "password" in data and data["password"]:
                password_hash = bcrypt.hashpw(
                    data["password"].encode("utf-8"),
                    bcrypt.gensalt()
                ).decode("utf-8")
                cambios.append("contraseña: [cambiada]")

            # Rol
            if "rol" in data and str(usuario_db.get("rol")) != str(data["rol"]):
                cambios.append(f"rol: '{usuario_db.get('rol')}' → '{data['rol']}'")

            # 3. Construir SQL dinámico
            if password_hash:
                sql = """
                    UPDATE usuarios
                    SET password_hash=%s,
                        rol=%s
                    WHERE id=%s
                """
                valores = (password_hash, data["rol"], usuario_id)
            else:
                sql = """
                    UPDATE usuarios
                    SET rol=%s
                    WHERE id=%s
                """
                valores = (data["rol"], usuario_id)

            cursor.execute(sql, valores)
            conexion.commit()

            # 4. Registrar en auditoría si hubo cambios
            if cambios:
                descripcion = "; ".join(cambios)
                AuditoriaModel.registrar(
                    usuario_id=usuario_actual["id"],
                    accion="UPDATE",
                    entidad="usuarios",
                    entidad_id=usuario_id,
                    referencia=usuario_db["username"],
                    descripcion=f"Cambios: {descripcion}"
                )

            return True, "Usuario actualizado correctamente."

        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()


    @staticmethod
    def eliminar(usuario_id: int, usuario_actual: dict):
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor(dictionary=True)

            # 1. Obtener datos del usuario antes de borrar
            cursor.execute("SELECT * FROM usuarios WHERE id = %s", (usuario_id,))
            usuario_db = cursor.fetchone()
            if not usuario_db:
                return False, "Usuario no encontrado."

            # 2. Registrar en auditoría (antes de eliminar)
            AuditoriaModel.registrar(
                usuario_id=usuario_actual["id"],   # el que está logueado
                accion="DELETE",
                entidad="usuarios",
                entidad_id=usuario_id,
                referencia=usuario_db["username"],
                descripcion=f"Se eliminó usuario {usuario_db['nombre_completo']} con rol {usuario_db['rol']}"
            )

            # 3. Eliminar
            cursor.execute("DELETE FROM usuarios WHERE id = %s", (usuario_id,))
            conexion.commit()

            return True, "Eliminación realizada correctamente."

        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def listar():
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT id, username, rol, CASE WHEN estado = 1 THEN 'Activo' ELSE 'Inactivo' END AS estado, nombre_completo, creado_en, actualizado_en
                FROM usuarios
            """)
            return cursor.fetchall()
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()
    
    @staticmethod
    def obtener_por_id(usuario_id: int):
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("""
                SELECT username, rol, nombre_completo
                FROM usuarios
                WHERE id = %s
            """, (usuario_id,))
            return cursor.fetchone()
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()
    
    @staticmethod
    def cambiar_estado(usuario_id: int, nuevo_estado: str, usuario_actual: dict):
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor(dictionary=True)

            # 1. Obtener datos actuales
            cursor.execute("SELECT username, estado FROM usuarios WHERE id=%s", (usuario_id,))
            usuario_db = cursor.fetchone()
            if not usuario_db:
                return False, "Usuario no encontrado."

            estado_actual = usuario_db["estado"]

            # 2. Actualizar estado
            cursor.execute(
                "UPDATE usuarios SET estado=%s WHERE id=%s",
                (nuevo_estado, usuario_id)
            )
            conexion.commit()

            # 3. Registrar en auditoría
            AuditoriaModel.registrar(
                usuario_id=usuario_actual["id"],
                accion="UPDATE",
                entidad="usuarios",
                entidad_id=usuario_id,
                referencia=usuario_db["username"],
                descripcion=f"Se cambió estado: '{estado_actual}' → '{nuevo_estado}'"
            )

            return True, f"Estado actualizado a {nuevo_estado}."

        except Exception as e:
            return False, str(e)

        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()