from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Qt

QMSGBOX_STYLE = """
    QMessageBox {
        background-color: white;
        color: black;
    }
    QLabel {
        color: black;
    }
    QPushButton {
        min-width: 60px;
        padding: 5px;
        background-color: #2980b9;
        color: #F3F6FF;
        border: none;
        padding: 8px 6px;
        border-radius: 10px;
        font-weight: bold;
    }
"""

def crear_msgbox(parent, titulo, texto, icono, botones=None, default=None):
    msg = QMessageBox(parent)
    msg.setWindowTitle(titulo)
    msg.setText(texto)
    msg.setIcon(icono)

    # 👇 Si no se pasan botones, usar Ok por defecto
    if botones is None:
        botones = QMessageBox.Ok
    msg.setStandardButtons(botones)

    if default:
        msg.setDefaultButton(default)

    msg.setStyleSheet(QMSGBOX_STYLE)
    for btn in msg.buttons():
        btn.setCursor(Qt.PointingHandCursor)
    return msg