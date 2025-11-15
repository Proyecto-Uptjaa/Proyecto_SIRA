import os
import subprocess

UI_DIR = "resources/ui"
OUT_DIR = "ui_compiled"

def compile_ui():
    for filename in os.listdir(UI_DIR):
        if filename.endswith(".ui"):
            in_path = os.path.join(UI_DIR, filename)
            out_name = os.path.splitext(filename)[0] + "_ui.py"
            out_path = os.path.join(OUT_DIR, out_name)
            print(f"Compilando {in_path} -> {out_path}")
            subprocess.run(["pyside6-uic", in_path, "-o", out_path])

            # corregir import automáticamente
            with open(out_path, "r+", encoding="utf-8") as f:
                content = f.read().replace("import resources_ui_rc", "from resources import resources_ui")
                f.seek(0)
                f.write(content)
                f.truncate()

def compile_qrc():
    qrc_path = os.path.join("resources", "icons", "resources_ui.qrc")
    if os.path.exists(qrc_path):
        out_path = os.path.join("resources", "resources_ui.py")
        print(f"Compilando {qrc_path} -> {out_path}")
        subprocess.run(["pyside6-rcc", qrc_path, "-o", out_path])

if __name__ == "__main__":
    compile_ui()
    compile_qrc()