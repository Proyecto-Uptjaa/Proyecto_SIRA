from utils.db import get_connection

def verificar_conexion_bd() -> bool:
    """Verifica si la conexión a la BD está disponible."""
    conexion = None
    cursor = None
    try:
        conexion = get_connection()
        if not conexion:
            return False
        cursor = conexion.cursor()
        cursor.execute("SELECT 1")
        cursor.fetchone()
        return True
    except Exception as err:
        print(f"Error de conexión a la BD: {err}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conexion and conexion.is_connected():
            conexion.close()