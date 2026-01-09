from PySide6.QtWidgets import QLineEdit, QDateEdit, QComboBox, QCheckBox, QWidget, QVBoxLayout, QLabel, QStyledItemDelegate, QApplication
from PySide6.QtCore import QDate, Qt, QTimer, QEvent, QPoint, QObject
from PySide6.QtGui import QColor, QPalette, QCursor


class CustomTooltipWidget(QWidget):
    """Widget personalizado para mostrar tooltips con fondo sólido."""
    
    # Variable de clase para rastrear la instancia activa
    _active_tooltip = None
    
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
        try:
            self.hide()
            self.close()
            self.deleteLater()
        except RuntimeError:
            pass
    
    @classmethod
    def show_tooltip(cls, text, position=None):
        """Muestra un tooltip en la posición especificada."""
        # Cerrar tooltip anterior si existe
        cls.close_active_tooltip()
        
        if not text or not text.strip():
            return None
        
        # Crear nuevo tooltip
        tooltip = cls(text)
        cls._active_tooltip = tooltip
        
        # Posicionar
        if position is None:
            position = QCursor.pos()
        tooltip.move(position.x() + 10, position.y() + 10)
        tooltip.show()
        
        return tooltip
    
    @classmethod
    def close_active_tooltip(cls):
        """Cierra el tooltip activo de forma segura."""
        if cls._active_tooltip:
            try:
                if cls._active_tooltip.isVisible():
                    cls._active_tooltip.hide()
                cls._active_tooltip.close()
                cls._active_tooltip.deleteLater()
            except RuntimeError:
                pass
            finally:
                cls._active_tooltip = None


class GlobalTooltipEventFilter(QObject):
    """Event filter global para interceptar y personalizar todos los tooltips."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.last_widget = None
        self.hide_timer = QTimer(self)
        self.hide_timer.timeout.connect(self.check_mouse_position)
        self.hide_timer.setInterval(100)  # Verificar cada 100ms
    
    def eventFilter(self, obj, event):
        if event.type() == QEvent.ToolTip:
            # Obtener el texto del tooltip
            tooltip_text = obj.toolTip()
            
            if tooltip_text and tooltip_text.strip():
                # Mostrar tooltip personalizado
                CustomTooltipWidget.show_tooltip(tooltip_text, event.globalPos())
                self.last_widget = obj
                self.hide_timer.start()
                return True  # Consumir el evento para evitar tooltip nativo
        
        elif event.type() == QEvent.Leave:
            # Cerrar tooltip al salir del widget
            if obj == self.last_widget:
                CustomTooltipWidget.close_active_tooltip()
                self.hide_timer.stop()
                self.last_widget = None
        
        return super().eventFilter(obj, event)
    
    def check_mouse_position(self):
        """Verifica si el mouse sigue sobre el widget con tooltip."""
        if self.last_widget:
            try:
                # Verificar si el widget sigue siendo válido
                if not self.last_widget.isVisible():
                    CustomTooltipWidget.close_active_tooltip()
                    self.hide_timer.stop()
                    self.last_widget = None
                    return
                
                # Verificar si el mouse está fuera del widget
                local_pos = self.last_widget.mapFromGlobal(QCursor.pos())
                if not self.last_widget.rect().contains(local_pos):
                    CustomTooltipWidget.close_active_tooltip()
                    self.hide_timer.stop()
                    self.last_widget = None
            except RuntimeError:
                # El widget fue eliminado
                CustomTooltipWidget.close_active_tooltip()
                self.hide_timer.stop()
                self.last_widget = None


class TooltipDelegate(QStyledItemDelegate):
    """Delegate que muestra el contenido completo de la celda en un tooltip personalizado."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.last_index = None
    
    def helpEvent(self, event, view, option, index):
        if event.type() == QEvent.ToolTip:
            # Verificar si es el mismo índice
            if self.last_index == index:
                return True
            
            # Cerrar tooltip anterior
            CustomTooltipWidget.close_active_tooltip()
            
            texto = index.data(Qt.DisplayRole)
            if texto and str(texto).strip():
                # Mostrar tooltip usando el sistema global
                CustomTooltipWidget.show_tooltip(str(texto), event.globalPos())
                self.last_index = index
                return True
                
        elif event.type() == QEvent.Leave:
            # Cerrar tooltip al salir de la vista
            CustomTooltipWidget.close_active_tooltip()
            self.last_index = None
        
        return super().helpEvent(event, view, option, index)
    
    def close_tooltip(self):
        """Cierra el tooltip de forma segura."""
        CustomTooltipWidget.close_active_tooltip()
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


class TooltipEventFilter(QObject):
    """Event filter para cerrar tooltips al salir de tablas."""
    
    def __init__(self, parent_widget):
        super().__init__()
        self.parent_widget = parent_widget
    
    def eventFilter(self, obj, event):
        if event.type() == QEvent.Leave:
            # Cerrar tooltip global
            CustomTooltipWidget.close_active_tooltip()
            
            # Cerrar tooltips de delegates
            if hasattr(self.parent_widget, 'tooltip_delegates'):
                for delegate in self.parent_widget.tooltip_delegates:
                    if hasattr(delegate, 'close_tooltip'):
                        delegate.close_tooltip()
        return False