from utils.db import get_connection

class AuditoriaModel:
    @staticmethod
    def listar(limit=50):
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("""
                SELECT a.id,
                       u.username AS usuario,
                       a.accion,
                       a.entidad,
                       a.entidad_id,
                       a.referencia,
                       a.descripcion,
                       a.fecha
                FROM auditoria a
                JOIN usuarios u ON a.usuario_id = u.id
                ORDER BY a.fecha DESC
                LIMIT %s
            """, (limit,))
            return cursor.fetchall()
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
    
    @staticmethod
    def registrar(usuario_id, accion, entidad, entidad_id, referencia, descripcion=""):
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO auditoria (usuario_id, accion, entidad, entidad_id, referencia, descripcion)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (usuario_id, accion, entidad, entidad_id, referencia, descripcion))
            conexion.commit()
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()