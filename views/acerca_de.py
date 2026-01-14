from ui_compiled.acerca_de_ui import Ui_Acerca_de
from utils.sombras import crear_sombra_flotante
from PySide6.QtWidgets import QDialog

class Acerca_de(QDialog, Ui_Acerca_de):
    """Ventana 'Acerca de SIRA'."""
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowTitle("Acerca de SIRA")

        # Conectar botones
        self.btnCerrar.clicked.connect(self.reject)
        # Sombras
        crear_sombra_flotante(self.btnCerrar)
        crear_sombra_flotante(self.lblLogo_SIRA_acercade, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lblLogo_UPTJAA_acercade, blur_radius=8, y_offset=1)
