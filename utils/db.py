import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
from typing import Optional

# Cargar variables del archivo .env al inicio
load_dotenv()


def get_connection() -> Optional[mysql.connector.MySQLConnection]:
    """
    Establece y retorna una conexión a la base de datos MySQL.
    
    Returns:
        Conexión MySQL o None si falla
        
    Raises:
        No lanza excepciones, retorna None en caso de error
    """
    try:
        # Validar variables de entorno
        host = os.getenv("DB_HOST")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASS")
        database = os.getenv("DB_NAME")
        
        if not all([host, user, password, database]):
            print("Error: Variables de entorno incompletas en .env")
            return None
        
        # Establecer conexión con timeout
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            connection_timeout=10,  # Timeout de 10 segundos
            autocommit=False  # Transacciones manuales para mejor control
        )
        
        return connection
        
    except Error as e:
        print(f"Error conectando a MySQL: {e}")
        return None
    except Exception as e:
        print(f"Error inesperado en conexión: {e}")
        return None


def verificar_conexion() -> bool:
    """
    Verifica que la conexión a la base de datos esté disponible.
    Útil para checks de salud al iniciar la aplicación.
    
    Returns:
        True si la conexión es exitosa, False en caso contrario
    """
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
        
    except Error as e:
        print(f"Error verificando conexión: {e}")
        return False
    except Exception as e:
        print(f"Error inesperado verificando conexión: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conexion and conexion.is_connected():
            conexion.close()


def get_user_by_username(username: str) -> Optional[dict]:
    """
    Busca un usuario por nombre de usuario.
    
    Args:
        username: Nombre de usuario a buscar
        
    Returns:
        Dict con datos del usuario o None si no existe
    """
    if not username or not isinstance(username, str):
        return None
    
    conexion = None
    cursor = None
    try:
        conexion = get_connection()
        if not conexion:
            return None
            
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("""
            SELECT id, username, password_hash, estado, rol
            FROM usuarios
            WHERE username = %s
        """, (username.strip(),))
        
        return cursor.fetchone()
        
    except Error as e:
        print(f"Error buscando usuario: {e}")
        return None
    except Exception as e:
        print(f"Error inesperado buscando usuario: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conexion and conexion.is_connected():
            conexion.close()


def insert_user(username: str, password_hash: str, rol: str = "Empleado") -> bool:
    """
    Inserta un nuevo usuario en la base de datos.
    
    
    Args:
        username: Nombre de usuario
        password_hash: Hash de la contraseña
        rol: Rol del usuario (default: "Empleado")
        
    Returns:
        True si se insertó correctamente, False en caso contrario
    """
    if not username or not password_hash:
        return False
    
    conexion = None
    cursor = None
    try:
        conexion = get_connection()
        if not conexion:
            return False
            
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO usuarios (username, password_hash, rol)
            VALUES (%s, %s, %s)
        """, (username.strip(), password_hash, rol))
        
        conexion.commit()
        return True
        
    except Error as e:
        if conexion:
            conexion.rollback()
        print(f"Error insertando usuario: {e}")
        return False
    except Exception as e:
        if conexion:
            conexion.rollback()
        print(f"Error inesperado insertando usuario: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conexion and conexion.is_connected():
            conexion.close()