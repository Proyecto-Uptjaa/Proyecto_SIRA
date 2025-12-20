from PySide6.QtWidgets import QLineEdit, QDateEdit, QComboBox, QCheckBox, QWidget, QVBoxLayout, QLabel, QStyledItemDelegate
from PySide6.QtCore import QDate, Qt, QTimer, QEvent
from PySide6.QtGui import QColor, QPalette


class CustomTooltipWidget(QWidget):
    """Widget personalizado para mostrar tooltips con fondo sólido."""
    
    def __init__(self, text, parent=None):
        super().__init__(parent, Qt.ToolTip | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, False)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self.setAttribute(Qt.WA_DeleteOnClose)
        
        # Layout y label
        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 6, 8, 6)
        
        self.label = QLabel(text)
        self.label.setWordWrap(True)
        self.label.setMaximumWidth(400)
        layout.addWidget(self.label)
        
        # Estilo forzado con QPalette
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#2b2b2b"))
        palette.setColor(QPalette.WindowText, QColor("#ffffff"))
        self.setPalette(palette)
        
        # Estilo adicional
        self.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b;
                border: 1px solid #555555;
                border-radius: 4px;
            }
            QLabel {
                color: white;
                background-color: transparent;
                font-size: 11px;
                padding: 2px;
            }
        """)
        
        # Timer para auto-cerrar el tooltip
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hide_tooltip)
        self.timer.setSingleShot(True)
        self.timer.start(5000)  # Auto-cerrar después de 5 segundos
        
        self.adjustSize()
    
    def hide_tooltip(self):
        """Oculta y cierra el tooltip de forma segura."""
        self.hide()
        self.close()
        self.deleteLater()


class TooltipDelegate(QStyledItemDelegate):
    """Delegate que muestra el contenido completo de la celda en un tooltip personalizado."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.tooltip_widget = None
        self.last_index = None
    
    def helpEvent(self, event, view, option, index):
        if event.type() == QEvent.ToolTip:
            # Verificar si el tooltip widget aún existe y es válido
            tooltip_exists = False
            try:
                if self.tooltip_widget and self.tooltip_widget.isVisible():
                    tooltip_exists = True
            except RuntimeError:
                # El objeto C++ fue eliminado, limpiar la referencia
                self.tooltip_widget = None
                self.last_index = None
            
            # Verificar si es el mismo índice y el tooltip aún existe
            if self.last_index == index and tooltip_exists:
                return True
            
            # Cerrar tooltip anterior si existe
            self.close_tooltip()
            
            texto = index.data(Qt.DisplayRole)
            if texto and str(texto).strip():
                # Crear y mostrar tooltip personalizado
                self.tooltip_widget = CustomTooltipWidget(str(texto), view)
                self.last_index = index
                
                # Posicionar el tooltip cerca del cursor
                pos = event.globalPos()
                self.tooltip_widget.move(pos.x() + 10, pos.y() + 10)
                self.tooltip_widget.show()
                
                return True
                
        elif event.type() == QEvent.Leave:
            # Cerrar tooltip al salir de la vista
            self.close_tooltip()
        
        return super().helpEvent(event, view, option, index)
    
    def close_tooltip(self):
        """Cierra el tooltip de forma segura."""
        if self.tooltip_widget:
            try:
                # Verificar si el objeto C++ aún existe antes de acceder
                if self.tooltip_widget.isVisible():
                    self.tooltip_widget.hide()
                self.tooltip_widget.close()
                self.tooltip_widget.deleteLater()
            except RuntimeError:
                # El objeto C++ ya fue eliminado, solo limpiar la referencia
                pass
            finally:
                self.tooltip_widget = None
                self.last_index = None


def limpiar_widgets(form):
    """Limpia todos los QLineEdit y QDateEdit de un formulario."""
    for widget in form.findChildren(QLineEdit):
        widget.clear()
    for widget in form.findChildren(QDateEdit):
        widget.setDate(QDate.currentDate())


def set_campos_editables(campos, estado: bool, campos_solo_lectura=None):
    """
    Habilita o bloquea una lista de campos.
    :param campos: lista de QLineEdit/QDateEdit/QComboBox/QCheckBox a habilitar o bloquear
    :param estado: True = habilitar, False = bloquear
    :param campos_solo_lectura: lista de campos que siempre deben quedar en solo lectura
    """
    for campo in campos:
        if isinstance(campo, (QLineEdit, QDateEdit)):
            campo.setReadOnly(not estado)
        elif isinstance(campo, QComboBox):
            campo.setEnabled(estado)  # habilita o bloquea el combo
        elif isinstance(campo, QCheckBox):
            campo.setEnabled(estado)  # habilita o bloquea el check
        else:
            try:
                campo.setEnabled(estado)  # fallback genérico
            except Exception:
                pass

    if campos_solo_lectura:
        for campo in campos_solo_lectura:
            if isinstance(campo, (QLineEdit, QDateEdit)):
                campo.setReadOnly(True)
            elif isinstance(campo, (QComboBox, QCheckBox)):
                campo.setEnabled(False)


def ajustar_columnas_tabla(parent_widget, tabla, anchos_columnas=None, stretch_last=False):
    """
    Ajusta el tamaño de las columnas de una tabla con anchos personalizados y tooltips.
    
    Args:
        parent_widget: Widget padre que mantiene la lista de delegates
        tabla: QTableView o QTableWidget
        anchos_columnas: Dict con {indice_columna: ancho_en_pixeles} o None para auto
        stretch_last: Si True, la última columna se estira para llenar el espacio
    """
    # Aplicar delegate para tooltips personalizados
    tooltip_delegate = TooltipDelegate(tabla)
    tabla.setItemDelegate(tooltip_delegate)
    
    # Guardar referencia al delegate en el widget padre
    if not hasattr(parent_widget, 'tooltip_delegates'):
        parent_widget.tooltip_delegates = []
    parent_widget.tooltip_delegates.append(tooltip_delegate)
    
    if anchos_columnas:
        # Establecer anchos personalizados
        for col, ancho in anchos_columnas.items():
            tabla.setColumnWidth(col, ancho)
    else:
        # Ajuste automático al contenido
        tabla.resizeColumnsToContents()
    
    if stretch_last:
        tabla.horizontalHeader().setStretchLastSection(True)
    
    # Desactivar word wrap para que el tooltip funcione mejor
    tabla.setWordWrap(False)
    
    # Habilitar mouse tracking para tooltips
    tabla.setMouseTracking(True)
    
    # Instalar event filter si no existe
    if not tabla.viewport().findChild(QWidget, "tooltip_filter"):
        filter_obj = TooltipEventFilter(parent_widget)
        filter_obj.setObjectName("tooltip_filter")
        tabla.viewport().installEventFilter(filter_obj)


class TooltipEventFilter(QWidget):
    """Event filter para cerrar tooltips al salir de tablas."""
    
    def __init__(self, parent_widget):
        super().__init__()
        self.parent_widget = parent_widget
    
    def eventFilter(self, obj, event):
        if event.type() == QEvent.Leave:
            # Cerrar todos los tooltips activos
            if hasattr(self.parent_widget, 'tooltip_delegates'):
                for delegate in self.parent_widget.tooltip_delegates:
                    if hasattr(delegate, 'close_tooltip'):
                        delegate.close_tooltip()
        return False