import os
import sys

def resource_path(relative_path):
    # Obtiene la ruta absoluta del recurso
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# Carpeta base del proyecto
BASE_DIR = os.path.dirname(__file__)

# Carpeta de recursos
ICON_DIR = os.path.join(BASE_DIR, "resources", "icons")