from PySide6.QtWidgets import QWidget, QMessageBox, QDialog
from PySide6.QtCore import Qt
from ui_compiled.anio_escolar_ui import Ui_anio_escolar
from ui_compiled.confirmar_anio_ui import Ui_confirmar_anio
from models.anio_model import AnioEscolarModel
from utils.sombras import crear_sombra_flotante
from utils.dialogs import crear_msgbox


class GestionAniosPage(QWidget, Ui_anio_escolar):
    """Página de gestión de años escolares."""
    
    def __init__(self, usuario_actual, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.setupUi(self)
        
        # Conectar botón de apertura
        if hasattr(self, 'btnAperturar_anio'):
            self.btnAperturar_anio.clicked.connect(self.abrir_dialogo_apertura)
            crear_sombra_flotante(self.btnAperturar_anio)
            crear_sombra_flotante(self.lblTitulo_anios, blur_radius=5, y_offset=1)
            crear_sombra_flotante(self.lblLogo_anios, blur_radius=5, y_offset=1)

    def abrir_dialogo_apertura(self):
        """Abre el diálogo para aperturar un nuevo año."""
        # Validar permisos (solo administrador)
        if self.usuario_actual.get("rol") != "admin":
            crear_msgbox(
                self,
                "Acceso denegado",
                "Solo los administradores pueden aperturar años escolares.",
                QMessageBox.Warning
            ).exec()
            return
        
        # Abrir diálogo de confirmación
        dialogo_apertura = ConfirmarAnioDialog(self.usuario_actual, self)
        if dialogo_apertura.exec() == QDialog.Accepted:
            # Notificar a MainWindow para actualizar otras vistas
            if self.parent() and hasattr(self.parent(), 'actualizar_anio_escolar'):
                self.parent().actualizar_anio_escolar()


class ConfirmarAnioDialog(QDialog, Ui_confirmar_anio):
    """Diálogo para confirmar apertura de nuevo año escolar."""
    
    def __init__(self, usuario_actual, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.setupUi(self)
        self.setWindowTitle("Aperturar Nuevo Año Escolar")
        self.setModal(True)
        
        # Conectar botones
        if hasattr(self, 'btnAperturar'):
            self.btnAperturar.clicked.connect(self.confirmar_apertura)
            crear_sombra_flotante(self.btnAperturar)
        
        if hasattr(self, 'btnCancelar'):
            self.btnCancelar.clicked.connect(self.reject)
            crear_sombra_flotante(self.btnCancelar)
        
        # Cargar año disponible
        self.cargar_años_disponibles()

    def cargar_años_disponibles(self):
        """Carga el próximo año disponible."""
        try:
            proximo_año = AnioEscolarModel.obtener_proximo_año()
            
            if hasattr(self, 'cbxAnio_nuevo'):
                self.cbxAnio_nuevo.clear()
                self.cbxAnio_nuevo.addItem(
                    f"{proximo_año}-{proximo_año + 1}", 
                    proximo_año
                )
                self.cbxAnio_nuevo.setCurrentIndex(0)
            
            # Actualizar label informativo si existe
            if hasattr(self, 'lblInfo_apertura'):
                self.lblInfo_apertura.setText(
                    f"Se creará el año escolar {proximo_año}-{proximo_año + 1}.\n\n"
                    "✓ Todas las secciones del año anterior serán duplicadas\n"
                    "✓ Los estudiantes serán promovidos automáticamente\n"
                    "✓ El año anterior quedará como histórico"
                )
            
        except Exception as e:
            crear_msgbox(
                self,
                "Error",
                f"Error al cargar años: {e}",
                QMessageBox.Critical
            ).exec()

    def confirmar_apertura(self):
        """Ejecuta la apertura del nuevo año."""
        try:
            anio_seleccionado = self.cbxAnio_nuevo.currentData()
            
            if not anio_seleccionado:
                crear_msgbox(
                    self,
                    "Selección requerida",
                    "Debe seleccionar un año para aperturar.",
                    QMessageBox.Warning
                ).exec()
                return

            # Confirmación final
            confirmar = crear_msgbox(
                self,
                "Confirmar Apertura",
                f"¿Desea aperturar el año escolar {anio_seleccionado}-{anio_seleccionado + 1}?\n\n"
                "✓ Se duplicarán todas las secciones del año anterior\n"
                "✓ Los estudiantes serán promovidos automáticamente\n"
                "✓ El año anterior se marcará como histórico\n"
                "✓ Esta acción es irreversible\n\n"
                "¿Está completamente seguro?",
                QMessageBox.Question,
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )

            if confirmar.exec() != QMessageBox.StandardButton.Yes:
                return

            # Deshabilitar botón para evitar doble clic
            if hasattr(self, 'btnAperturar'):
                self.btnAperturar.setEnabled(False)
                self.btnAperturar.setText("Aperturando...")

            # Ejecutar apertura con duplicación y promoción
            ok, mensaje = AnioEscolarModel.aperturar_nuevo(
                anio_inicio=anio_seleccionado,
                usuario_actual=self.usuario_actual,
                duplicar_secciones=True
            )

            # Reactivar botón
            if hasattr(self, 'btnAperturar'):
                self.btnAperturar.setEnabled(True)
                self.btnAperturar.setText("Aperturar")

            if ok:
                crear_msgbox(
                    self,
                    "Éxito",
                    mensaje,
                    QMessageBox.Information
                ).exec()
                self.accept()
            else:
                crear_msgbox(
                    self,
                    "Error",
                    mensaje,
                    QMessageBox.Critical
                ).exec()
        
        except Exception as e:
            # Reactivar botón en caso de error
            if hasattr(self, 'btnAperturar'):
                self.btnAperturar.setEnabled(True)
                self.btnAperturar.setText("Aperturar")
            
            crear_msgbox(
                self,
                "Error Inesperado",
                f"Error al aperturar año: {e}",
                QMessageBox.Critical
            ).exec()