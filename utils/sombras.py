from PySide6.QtWidgets import QGraphicsDropShadowEffect
from PySide6.QtGui import QColor

def crear_sombra_flotante(widget, blur_radius=10, y_offset=2, opacity=80):
    """Aplica un efecto de sombra flotante a un widget."""
    sombra = QGraphicsDropShadowEffect(widget)
    sombra.setBlurRadius(blur_radius)
    sombra.setXOffset(0)
    sombra.setYOffset(y_offset)
    sombra.setColor(QColor(0, 0, 0, opacity))
    widget.setGraphicsEffect(sombra)