import os
import sys
import subprocess
from pathlib import Path


def abrir_archivo(ruta: str) -> bool:
    """Abre un archivo con la aplicación predeterminada del sistema."""
    try:
        if not os.path.exists(ruta):
            print(f"Error: El archivo no existe: {ruta}")
            return False
        
        # Convertir a ruta absoluta
        ruta = os.path.abspath(ruta)
        
        if sys.platform == "win32":
            # Windows
            os.startfile(ruta)
        elif sys.platform == "darwin":
            # MacOS
            subprocess.Popen(["open", ruta])
        else:
            # Linux y otros Unix
            subprocess.Popen(["xdg-open", ruta])
        
        return True
        
    except Exception as e:
        print(f"Error al abrir archivo {ruta}: {e}")
        return False


def abrir_carpeta(ruta: str) -> bool:
    """Abre una carpeta en el explorador de archivos del sistema."""
    try:
        if not os.path.exists(ruta):
            print(f"Error: La carpeta no existe: {ruta}")
            return False
        
        # Convertir a ruta absoluta
        ruta = os.path.abspath(ruta)
        
        if sys.platform == "win32":
            # Windows - usar explorer
            os.startfile(ruta)
        elif sys.platform == "darwin":
            # MacOS
            subprocess.Popen(["open", ruta])
        else:
            # Linux y otros Unix
            subprocess.Popen(["xdg-open", ruta])
        
        return True
        
    except Exception as e:
        print(f"Error al abrir carpeta {ruta}: {e}")
        return False


def normalizar_ruta(ruta: str) -> str:
    """Normaliza una ruta para el sistema operativo actual."""
    return os.path.normpath(os.path.abspath(ruta))


def crear_carpeta_si_no_existe(ruta: str) -> bool:
    """Crea una carpeta si no existe."""
    try:
        os.makedirs(ruta, exist_ok=True)
        return True
    except Exception as e:
        print(f"Error al crear carpeta {ruta}: {e}")
        return False
