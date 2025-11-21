from utils.db import get_connection
from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtGui import QIcon
import sys
from resources import resources_ui
from paths import resource_path
from views.main_window import MainWindow
from views.login import LoginDialog

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
    QToolTip {
        color: white;
        padding: 5px;
        font-size: 12px;
    }
""")
    app.setWindowIcon(QIcon(resource_path("resources/icons/aguacate.ico")))
    while True:
        login = LoginDialog()
        if login.exec() == QDialog.Accepted:
            usuario_actual = login.usuario
            ventana = MainWindow(usuario_actual)
            ventana.show()

            app.exec()   #corre el loop principal

            if ventana.logout:
                continue   # volver a mostrar login
            else:
                break      # salir del programa
        else:
            break