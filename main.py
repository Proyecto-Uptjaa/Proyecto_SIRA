from utils.db import get_connection
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
from PySide6.QtGui import QIcon
import sys
from resources import resources_ui
from paths import resource_path
from views.main_window import MainWindow
from views.login import LoginDialog
from views.config_inicial import Config_inicial
from utils.forms import GlobalTooltipEventFilter
from utils.fonts import FontManager
from utils.dialogs import crear_msgbox


def main():
    """Punto de entrada de la aplicación."""
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(resource_path("resources/icons/SIRA.ico")))
    
    # Cargar y aplicar fuente Inter globalmente
    FontManager.cargar_fuentes()
    FontManager.aplicar_fuente_global(app, tamaño=10)
    
    # Instalar event filter global para tooltips personalizados
    tooltip_filter = GlobalTooltipEventFilter(app)
    app.installEventFilter(tooltip_filter)
    
    # Verificar conexión a BD antes de iniciar
    conexion = get_connection()
    if not conexion:
        crear_msgbox(
            None,
            "Error de Conexión",
            "No se pudo conectar a la base de datos.\nVerifique la configuración en el archivo .env",
            QMessageBox.Critical
        ).exec()
        return 1
    
    # Verificar si existen usuarios en la BD
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM usuarios")
        count = cursor.fetchone()[0]
        cursor.close()
        conexion.close()
        
        # Si no hay usuarios, mostrar configuración inicial
        if count == 0:
            config = Config_inicial()
            resultado_config = config.exec()
            
            if resultado_config != QDialog.Accepted:
                # Usuario canceló la configuración inicial
                crear_msgbox(
                    None,
                    "Configuración Requerida",
                    "Debe completar la configuración inicial para usar el sistema.",
                    QMessageBox.Information
                ).exec()
                return 0
    except Exception as e:
        crear_msgbox(
            None,
            "Advertencia",
            f"Error al verificar usuarios: {e}\nContinuando con login...",
            QMessageBox.Warning
        ).exec()
    
    ventana_principal = None
    
    try:
        while True:
            login = LoginDialog()
            resultado = login.exec()
            
            if resultado == QDialog.Accepted:
                usuario_actual = login.usuario
                

                # Limpiar ventana anterior si existe
                if ventana_principal:
                    ventana_principal.close()
                    ventana_principal.deleteLater()
                
                ventana_principal = MainWindow(usuario_actual)
                ventana_principal.show()
                app.exec()
                
                # Verificar si fue logout o cierre
                if hasattr(ventana_principal, 'logout') and ventana_principal.logout:
                    continue
                else:
                    break
            else:
                # Usuario canceló el login
                break
                
    except Exception as e:
        crear_msgbox(
            None,
            "Error Fatal",
            f"Ocurrió un error inesperado:\n{str(e)}",
            QMessageBox.Critical
        ).exec()
        return 1
    finally:
        # Asegurar limpieza de recursos
        if ventana_principal:
            ventana_principal.close()
            ventana_principal.deleteLater()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())