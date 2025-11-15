from PySide6.QtWidgets import QStackedWidget, QGraphicsOpacityEffect, QLabel
from PySide6.QtCore import QPropertyAnimation, QEasingCurve

class AnimatedStack(QStackedWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def setCurrentIndexSlide(self, index, duration=250):
        current = self.currentWidget()
        nextw = self.widget(index)
        geo = self.geometry()

        # Colocar la nueva página fuera de la vista (a la derecha)
        nextw.setGeometry(geo.adjusted(geo.width(), 0, geo.width(), 0))
        nextw.show()

        # Animación de salida
        anim_out = QPropertyAnimation(current, b"geometry", self)
        anim_out.setDuration(duration)
        anim_out.setStartValue(geo)
        anim_out.setEndValue(geo.adjusted(-geo.width(), 0, -geo.width(), 0))
        anim_out.setEasingCurve(QEasingCurve.OutCubic)

        # Animación de entrada
        anim_in = QPropertyAnimation(nextw, b"geometry", self)
        anim_in.setDuration(duration)
        anim_in.setStartValue(nextw.geometry())
        anim_in.setEndValue(geo)
        anim_in.setEasingCurve(QEasingCurve.OutCubic)
        #anim_in.setEasingCurve(QEasingCurve.InOutQuad)

        anim_out.start()
        anim_in.start()

        # Cambiar índice lógico
        self.setCurrentIndex(index)

    

    def setCurrentIndexFade(self, index, duration=150):
        current = self.currentWidget()
        nextw = self.widget(index)

        eff_out = QGraphicsOpacityEffect(current)
        current.setGraphicsEffect(eff_out)
        eff_in = QGraphicsOpacityEffect(nextw)
        nextw.setGraphicsEffect(eff_in)

        anim_out = QPropertyAnimation(eff_out, b"opacity", self)
        anim_out.setDuration(duration)
        anim_out.setStartValue(1)
        anim_out.setEndValue(0)

        anim_in = QPropertyAnimation(eff_in, b"opacity", self)
        anim_in.setDuration(duration)
        anim_in.setStartValue(0)
        anim_in.setEndValue(1)

        def on_out_finished():
            self.setCurrentIndex(index)
            anim_in.start()

        def on_in_finished():
            # 🔹 limpiar efectos para que no sigan activos
            current.setGraphicsEffect(None)
            nextw.setGraphicsEffect(None)

        anim_out.finished.connect(on_out_finished)
        anim_in.finished.connect(on_in_finished)

        anim_out.start()

    def setCurrentIndexFadeOverlay(self, index, duration=300):
        current = self.currentWidget()
        nextw = self.widget(index)

        # Capturar pixmaps
        pm_current = current.grab()
        pm_next = nextw.grab()

        geo = self.geometry()

        # Labels temporales
        lbl_current = QLabel(self)
        lbl_current.setPixmap(pm_current)
        lbl_current.setGeometry(geo)
        lbl_current.show()

        lbl_next = QLabel(self)
        lbl_next.setPixmap(pm_next)
        lbl_next.setGeometry(geo)
        lbl_next.setWindowOpacity(0.0)
        lbl_next.show()

        # Animación fade in/out
        anim_out = QPropertyAnimation(lbl_current, b"windowOpacity", self)
        anim_out.setDuration(duration)
        anim_out.setStartValue(1.0)
        anim_out.setEndValue(0.0)
        anim_out.setEasingCurve(QEasingCurve.InOutQuad)

        anim_in = QPropertyAnimation(lbl_next, b"windowOpacity", self)
        anim_in.setDuration(duration)
        anim_in.setStartValue(0.0)
        anim_in.setEndValue(1.0)
        anim_in.setEasingCurve(QEasingCurve.InOutQuad)

        def finish():
            self.setCurrentIndex(index)
            lbl_current.deleteLater()
            lbl_next.deleteLater()

        anim_in.finished.connect(finish)

        anim_out.start()
        anim_in.start()
