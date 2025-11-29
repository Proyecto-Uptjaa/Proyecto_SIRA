# compilar_ui.py
import os
import subprocess
import sys

# Ruta absoluta basada en la ubicación del propio script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
UI_DIR = os.path.join(SCRIPT_DIR, "resources", "ui")
OUT_DIR = os.path.join(SCRIPT_DIR, "ui_compiled")
QRC_PATH = os.path.join(SCRIPT_DIR, "resources", "icons", "resources_ui.qrc")
RESOURCE_PY = os.path.join(SCRIPT_DIR, "resources", "resources_ui.py")

os.makedirs(OUT_DIR, exist_ok=True)

def compilar_ui():
    if not os.path.isdir(UI_DIR):
        print(f"Error: No se encontró la carpeta {UI_DIR}")
        sys.exit(1)
    
    for archivo in os.listdir(UI_DIR):
        if archivo.endswith(".ui"):
            entrada = os.path.join(UI_DIR, archivo)
            salida = os.path.join(OUT_DIR, os.path.splitext(archivo)[0] + "_ui.py")
            print(f"Compilando {archivo} → {os.path.basename(salida)}")
            subprocess.run(["pyside6-uic", entrada, "-o", salida], check=True)
            
            # Corrige el import del recurso
            with open(salida, "r", encoding="utf-8") as f:
                contenido = f.read()
            contenido = contenido.replace(
                "import resources_ui_rc",
                "from resources import resources_ui"
            )
            with open(salida, "w", encoding="utf-8") as f:
                f.write(contenido)

def compilar_qrc():
    if os.path.exists(QRC_PATH):
        print("Compilando resources_ui.qrc → resources_ui.py")
        subprocess.run(["pyside6-rcc", QRC_PATH, "-o", RESOURCE_PY], check=True)
    else:
        print("Advertencia: No se encontró resources_ui.qrc")

if __name__ == "__main__":
    compilar_ui()
    compilar_qrc()
    print("¡Compilación terminada!")