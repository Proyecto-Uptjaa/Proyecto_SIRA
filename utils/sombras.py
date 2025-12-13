from PySide6.QtWidgets import QGraphicsDropShadowEffect
from PySide6.QtGui import QColor

def crear_sombra_flotante(widget, blur_radius=10, y_offset=2, opacity=80):
    """Crea y aplica un QGraphicsDropShadowEffect a un widget dado."""
    sombra = QGraphicsDropShadowEffect(widget)
    sombra.setBlurRadius(blur_radius)
    sombra.setXOffset(0)
    sombra.setYOffset(y_offset)
    # El color (0, 0, 0) es negro. El último valor es el canal alfa (transparencia, 0-255)
    sombra.setColor(QColor(0, 0, 0, opacity)) 
    widget.setGraphicsEffect(sombra)