from utils.db import get_connection
import bcrypt
from models.auditoria_model import AuditoriaModel
from typing import Optional, Dict, List, Tuple


class UsuarioModel:
    """Modelo de usuarios del sistema."""

    @staticmethod
    def guardar(usuario_data: dict, usuario_actual: dict) -> Tuple[bool, str]:
        """Registra un nuevo usuario con contraseña hasheada."""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos"
            
            cursor = conexion.cursor()

            # Validar username duplicado
            cursor.execute("SELECT id FROM usuarios WHERE username = %s", (usuario_data["username"],))
            if cursor.fetchone():
                return False, f"El usuario '{usuario_data['username']}' ya existe"

            # Hashear contraseña
            password_hash = bcrypt.hashpw(
                usuario_data["password"].encode("utf-8"),
                bcrypt.gensalt()
            ).decode("utf-8")

            # Insertar usuario
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
            conexion.commit()
            
            usuario_id = cursor.lastrowid

            # Auditoría
            AuditoriaModel.registrar(
                usuario_id=usuario_actual["id"],
                accion="INSERT",
                entidad="usuarios",
                entidad_id=usuario_id,
                referencia=usuario_data["username"],
                descripcion=f"Creó usuario {usuario_data['nombre_completo']} con rol {usuario_data['rol']}"
            )

            return True, "Usuario registrado correctamente"

        except Exception as e:
            if conexion:
                conexion.rollback()
            return False, f"Error al guardar usuario: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
   
    @staticmethod
    def actualizar(usuario_id: int, data: dict, usuario_actual: dict) -> Tuple[bool, str]:
        """Actualiza datos de un usuario existente."""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos"
            
            cursor = conexion.cursor(dictionary=True)

            # Obtener datos actuales
            cursor.execute("SELECT * FROM usuarios WHERE id=%s", (usuario_id,))
            usuario_db = cursor.fetchone()
            
            if not usuario_db:
                return False, "Usuario no encontrado"

            # Preparar cambios
            cambios = []

            # Validar que no se quite el único admin
            if "rol" in data:
                nuevo_rol = data["rol"].strip()
                rol_actual = usuario_db.get("rol", "")
                
                if rol_actual == "admin" and nuevo_rol != "admin":
                    # Contar administradores activos
                    cursor.execute("""
                        SELECT COUNT(*) as total 
                        FROM usuarios 
                        WHERE rol = 'admin' AND estado = 1 AND id != %s
                    """, (usuario_id,))
                    resultado = cursor.fetchone()
                    
                    if resultado["total"] == 0:
                        return False, "No se puede cambiar el rol: debe existir al menos un administrador activo"
                
                if rol_actual != nuevo_rol:
                    cambios.append(f"rol: '{rol_actual}' → '{nuevo_rol}'")

            # Contraseña
            password_hash = None
            if "password" in data and data["password"]:
                password_hash = bcrypt.hashpw(
                    data["password"].encode("utf-8"),
                    bcrypt.gensalt()
                ).decode("utf-8")
                cambios.append("contraseña: [cambiada]")

            # Construir SQL dinámico
            if password_hash:
                sql = """
                    UPDATE usuarios
                    SET password_hash=%s, rol=%s
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

            # Auditoría solo si hubo cambios
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

            return True, "Usuario actualizado correctamente"

        except Exception as e:
            if conexion:
                conexion.rollback()
            return False, f"Error al actualizar usuario: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def eliminar(usuario_id: int, usuario_actual: dict) -> Tuple[bool, str]:
        """Elimina un usuario del sistema."""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos"
            
            cursor = conexion.cursor(dictionary=True)

            # Validar que no se elimine a sí mismo
            if usuario_id == usuario_actual["id"]:
                return False, "No puede eliminarse a sí mismo"

            # Obtener datos antes de eliminar
            cursor.execute("SELECT * FROM usuarios WHERE id = %s", (usuario_id,))
            usuario_db = cursor.fetchone()
            
            if not usuario_db:
                return False, "Usuario no encontrado"

            # Validar que no sea el último administrador activo
            if usuario_db["rol"] == "admin" and usuario_db["estado"] == 1:
                cursor.execute("""
                    SELECT COUNT(*) as total 
                    FROM usuarios 
                    WHERE rol = 'admin' AND estado = 1 AND id != %s
                """, (usuario_id,))
                resultado = cursor.fetchone()
                
                if resultado["total"] == 0:
                    return False, "No se puede eliminar el único administrador activo del sistema"

            # Auditoría antes de eliminar
            AuditoriaModel.registrar(
                usuario_id=usuario_actual["id"],
                accion="DELETE",
                entidad="usuarios",
                entidad_id=usuario_id,
                referencia=usuario_db["username"],
                descripcion=f"Eliminó usuario {usuario_db['nombre_completo']} con rol {usuario_db['rol']}"
            )

            # Eliminar
            cursor.execute("DELETE FROM usuarios WHERE id = %s", (usuario_id,))
            conexion.commit()

            return True, "Usuario eliminado correctamente"

        except Exception as e:
            if conexion:
                conexion.rollback()
            return False, f"Error al eliminar usuario: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def listar() -> List[tuple]:
        """Lista todos los usuarios del sistema."""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return []
            
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT id, username, rol, 
                       CASE WHEN estado = 1 THEN 'Activo' ELSE 'Inactivo' END AS estado, 
                       nombre_completo, creado_en, actualizado_en
                FROM usuarios
            """)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error en listar: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
    
    @staticmethod
    def obtener_por_id(usuario_id: int) -> Optional[Dict]:
        """Obtiene datos de un usuario por su ID."""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return None
            
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("""
                SELECT username, rol, nombre_completo, estado
                FROM usuarios
                WHERE id = %s
            """, (usuario_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error en obtener_por_id: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
    
    @staticmethod
    def cambiar_estado(usuario_id: int, nuevo_estado: int, usuario_actual: dict) -> Tuple[bool, str]:
        """Cambia el estado de un usuario (activo/inactivo)."""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos"
            
            cursor = conexion.cursor(dictionary=True)

            # Validar que no se desactive a sí mismo
            if usuario_id == usuario_actual["id"] and nuevo_estado == 0:
                return False, "No puede desactivarse a sí mismo"

            # Obtener datos actuales
            cursor.execute("SELECT username, estado, rol FROM usuarios WHERE id=%s", (usuario_id,))
            usuario_db = cursor.fetchone()
            
            if not usuario_db:
                return False, "Usuario no encontrado"

            estado_actual = usuario_db["estado"]

            # Validar que no sea el último admin activo
            if usuario_db["rol"] == "admin" and estado_actual == 1 and nuevo_estado == 0:
                cursor.execute("""
                    SELECT COUNT(*) as total 
                    FROM usuarios 
                    WHERE rol = 'admin' AND estado = 1 AND id != %s
                """, (usuario_id,))
                resultado = cursor.fetchone()
                
                if resultado["total"] == 0:
                    return False, "No se puede desactivar el único administrador activo del sistema"

            # Actualizar estado
            cursor.execute(
                "UPDATE usuarios SET estado=%s WHERE id=%s",
                (nuevo_estado, usuario_id)
            )
            conexion.commit()

            # Auditoría
            estado_texto = "Activo" if nuevo_estado == 1 else "Inactivo"
            AuditoriaModel.registrar(
                usuario_id=usuario_actual["id"],
                accion="UPDATE",
                entidad="usuarios",
                entidad_id=usuario_id,
                referencia=usuario_db["username"],
                descripcion=f"Cambió estado a: {estado_texto}"
            )

            return True, f"Estado actualizado a {estado_texto}"

        except Exception as e:
            if conexion:
                conexion.rollback()
            return False, f"Error al cambiar estado: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()