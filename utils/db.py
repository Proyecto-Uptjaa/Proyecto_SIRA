import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
from typing import Optional

# Cargar variables del archivo .env
load_dotenv()

# Cache de credenciales (se leen una sola vez al importar el módulo)
_DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS"),
    "database": os.getenv("DB_NAME"),
}


def get_connection() -> Optional[mysql.connector.MySQLConnection]:
    """Retorna una conexión a MySQL o None si falla."""
    try:
        if not all(_DB_CONFIG.values()):
            print("Error: Variables de entorno incompletas en .env")
            return None
        
        connection = mysql.connector.connect(
            host=_DB_CONFIG["host"],
            user=_DB_CONFIG["user"],
            password=_DB_CONFIG["password"],
            database=_DB_CONFIG["database"],
            connection_timeout=10,
            autocommit=False
        )
        
        return connection
        
    except Error as e:
        print(f"Error conectando a MySQL: {e}")
        return None
    except Exception as e:
        print(f"Error inesperado en conexión: {e}")
        return None


def verificar_conexion() -> bool:
    """Verifica si la conexión a BD está disponible."""
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
    """Busca un usuario por username."""
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
    """Inserta un nuevo usuario en la BD."""
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