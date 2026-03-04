import os
import sys
import subprocess


def _obtener_env_limpio() -> dict:
    """Obtiene una copia del entorno limpia de variables inyectadas por PyInstaller.

    Cuando la app se ejecuta como binario compilado con PyInstaller, este modifica
    variables como LD_LIBRARY_PATH, GDK_BACKEND, QT_PLUGIN_PATH, etc., lo que
    impide que programas externos (como xdg-open y los visores de PDF) funcionen
    correctamente al heredar ese entorno contaminado.
    """
    env = os.environ.copy()

    # Si estamos corriendo desde un bundle de PyInstaller
    if getattr(sys, 'frozen', False):
        # LD_LIBRARY_PATH: restaurar el valor original o eliminar
        ld_path_orig = env.get('LD_LIBRARY_PATH_ORIG')
        if ld_path_orig is not None:
            env['LD_LIBRARY_PATH'] = ld_path_orig
        else:
            env.pop('LD_LIBRARY_PATH', None)

        # Eliminar variables que PyInstaller puede inyectar y afectan a apps externas
        for var in ['GDK_BACKEND', 'QT_PLUGIN_PATH', 'QT_QPA_PLATFORM_PLUGIN_PATH',
                     'GI_TYPELIB_PATH', 'GST_PLUGIN_PATH', 'GST_PLUGIN_SYSTEM_PATH']:
            env.pop(var, None)

    return env


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
            # Linux y otros Unix - usar entorno limpio para evitar
            # conflictos con las librerías de PyInstaller
            env = _obtener_env_limpio()
            subprocess.Popen(["xdg-open", ruta], env=env,
                             start_new_session=True)

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
            # Linux y otros Unix - usar entorno limpio para evitar
            # conflictos con las librerías de PyInstaller
            env = _obtener_env_limpio()
            subprocess.Popen(["xdg-open", ruta], env=env,
                             start_new_session=True)

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
