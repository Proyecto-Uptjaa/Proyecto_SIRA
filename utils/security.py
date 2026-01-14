import bcrypt
import re
from typing import Tuple


def hash_password(password: str) -> str:
    """Genera un hash bcrypt de la contraseña."""
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
    """Verifica si la contraseña coincide con el hash."""
    if not password or not hashed:
        return False
    
    if not isinstance(password, str) or not isinstance(hashed, str):
        return False
    
    try:
        return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))
    except Exception as e:
        print(f"Error verificando contraseña: {e}")
        return False