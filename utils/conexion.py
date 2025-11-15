
from utils.db import get_connection  # tu función central de conexión

def verificar_conexion_bd() -> bool:
    conexion = None
    cursor = None
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        cursor.execute("SELECT 1")
        cursor.fetchone()
        return True
    except get_connection().Error as err:
        print(f"Error de conexión a la BD: {err}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conexion and conexion.is_connected():
            conexion.close()