from ui_compiled.acerca_de_ui import Ui_Acerca_de
from utils.sombras import crear_sombra_flotante
from PySide6.QtWidgets import QDialog

class Acerca_de(QDialog, Ui_Acerca_de):
    """
    Ventana de información "Acerca de SIRA".
    """
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowTitle("Acerca de SIRA")

        # Conectar botones
        self.btnCerrar.clicked.connect(self.reject)
        # Sombras
        crear_sombra_flotante(self.btnCerrar)
