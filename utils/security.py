import bcrypt
import re
from typing import Tuple


def hash_password(password: str) -> str:
    """
    Genera un hash seguro de una contraseña usando bcrypt.
    
    Args:
        password: Contraseña en texto plano
        
    Returns:
        Hash de la contraseña en formato string
        
    Raises:
        ValueError: Si la contraseña está vacía
        Exception: Si falla el proceso de hashing
    """
    if not password or not isinstance(password, str):
        raise ValueError("La contraseña no puede estar vacía")
    
    if len(password.strip()) == 0:
        raise ValueError("La contraseña no puede estar vacía")
    
    try:
        salt = bcrypt.gensalt(rounds=12)  # 12 rondas = buen balance seguridad/performance
        hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed.decode("utf-8")
    except Exception as e:
        raise Exception(f"Error al generar hash: {e}")


def check_password(password: str, hashed: str) -> bool:
    """
    Verifica si una contraseña coincide con su hash.
    
    Args:
        password: Contraseña en texto plano a verificar
        hashed: Hash almacenado en la base de datos
        
    Returns:
        True si la contraseña es correcta, False en caso contrario
    """
    if not password or not hashed:
        return False
    
    if not isinstance(password, str) or not isinstance(hashed, str):
        return False
    
    try:
        return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))
    except Exception as e:
        print(f"Error verificando contraseña: {e}")
        return False