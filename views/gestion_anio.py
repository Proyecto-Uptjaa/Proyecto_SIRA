from PySide6.QtWidgets import (
    QWidget, QMessageBox, QDialog
)
from ui_compiled.anio_escolar_ui import Ui_anio_escolar
from ui_compiled.confirmar_anio_ui import Ui_confirmar_anio
from models.anio_model import AnioEscolarModel


class GestionAniosPage(QWidget, Ui_anio_escolar):
    """Página de gestión de años escolares"""
    
    def __init__(self, usuario_actual, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.setupUi(self)
   
        self.btnAperturar_anio.clicked.connect(self.abrir_dialogo_apertura)

    def abrir_dialogo_apertura(self):
        """Abre el diálogo para aperturar un nuevo año escolar"""
        dialogo_apertura = ConfirmarAnioDialog(self.usuario_actual, self)
        dialogo_apertura.exec()


class ConfirmarAnioDialog(QDialog, Ui_confirmar_anio):
    """Diálogo para confirmar apertura de nuevo año escolar"""
    
    def __init__(self, usuario_actual, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.setupUi(self)
        self.setWindowTitle("Aperturar Nuevo Año Escolar")
        self.setModal(True)
        self.cargar_años_disponibles()
        self.btnAperturar.clicked.connect(self.confirmar_apertura)
        self.btnCancelar.clicked.connect(self.reject)

    def cargar_años_disponibles(self):
        """Carga los años disponibles en el combobox"""
        try:
            proximo_año = AnioEscolarModel.obtener_proximo_año()
            
            if hasattr(self, 'cbxAnio_nuevo'):
                if self.cbxAnio_nuevo.count() > 0:
                    self.cbxAnio_nuevo.clear()
                
                #año = proximo_año
                self.cbxAnio_nuevo.addItem(f"{proximo_año}-{proximo_año + 1}", proximo_año)
                
                self.cbxAnio_nuevo.setCurrentIndex(0)
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar años: {str(e)}")

    def confirmar_apertura(self):
        """Ejecuta la apertura del nuevo año escolar"""
        try:
            anio_seleccionado = self.cbxAnio_nuevo.currentData()
            
            if not anio_seleccionado:
                QMessageBox.warning(self, "Advertencia", "Debes seleccionar un año.")
                return

            # Confirmación
            respuesta = QMessageBox.question(
                self,
                "Confirmar Apertura",
                f"¿Deseas aperturar el año escolar {anio_seleccionado}-{anio_seleccionado + 1}?\n\n"
                "Se duplicarán todas las secciones del año anterior.\nEsta acción es irreversible, " \
                "debe estar seguro de hacerlo.",
                QMessageBox.Yes | QMessageBox.No
            )

            if respuesta == QMessageBox.No:
                return

            # Ejecutar apertura
            exito, mensaje = AnioEscolarModel.aperturar_nuevo(
                anio_inicio=anio_seleccionado,
                usuario_actual=self.usuario_actual,
                duplicar_secciones=True
            )

            if exito:
                QMessageBox.information(self, "Éxito", mensaje)
                self.accept()
            else:
                QMessageBox.critical(self, "Error", mensaje)
        
        except Exception as e:
            QMessageBox.critical(self, "Error Inesperado", f"Error: {str(e)}")