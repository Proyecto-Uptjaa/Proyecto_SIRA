from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QPainter, QColor, QBrush
from PySide6.QtWidgets import QCheckBox

class Switch(QCheckBox):
    def __init__(self, parent=None, color_on="#27ae60", color_off="#cccccc"):
        super().__init__(parent)
        self.setChecked(True)
        self.setCursor(Qt.PointingHandCursor)
        self.color_on = color_on
        self.color_off = color_off

        # Repintar cuando cambia el estado
        self.stateChanged.connect(self.update)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Fondo del switch
        rect = QRectF(0, 0, self.width(), self.height())
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(QColor(self.color_on if self.isChecked() else self.color_off)))
        painter.drawRoundedRect(rect, self.height() / 2, self.height() / 2)

        # Círculo blanco
        r = self.height() - 4
        x = self.width() - r - 2 if self.isChecked() else 2
        painter.setBrush(QBrush(QColor("white")))
        painter.drawEllipse(x, 2, r, r)

    def mousePressEvent(self, event):
        # Cambiar el estado con cualquier clic dentro del área del switch
        if event.button() == Qt.LeftButton:
            self.setChecked(not self.isChecked())
            event.accept()
