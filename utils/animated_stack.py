from PySide6.QtWidgets import QStackedWidget
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Qt


class AnimatedStack(QStackedWidget):
    """QStackedWidget con transiciones animadas."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._animating = False
        
        # Ocultar todos los widgets excepto el actual
        self._setup_initial_visibility()
    
    def _setup_initial_visibility(self):
        """Oculta widgets excepto el actual."""
        current_index = self.currentIndex()
        for i in range(self.count()):
            widget = self.widget(i)
            if widget:
                widget.setVisible(i == current_index)
    
    def _hide_all_except(self, exception_index):
        """Oculta todos los widgets excepto el indicado."""
        for i in range(self.count()):
            if i != exception_index:
                widget = self.widget(i)
                if widget:
                    widget.hide()
    
    def setCurrentIndexSlide(self, index, duration=200):
        """Cambia de página con animación de deslizamiento."""
        if self._animating or index == self.currentIndex():
            return
        
        self._animating = True
        current = self.currentWidget()
        nextw = self.widget(index)
        
        if not current or not nextw:
            self.setCurrentIndex(index)
            self._animating = False
            return
        
        # Ocultar todos excepto current
        current_idx = self.currentIndex()
        self._hide_all_except(current_idx)
        
        geo = self.geometry()
        
        # Guardar y limpiar estilos durante la animación
        current_style = current.styleSheet()
        next_style = nextw.styleSheet()
        
        # Colocar nueva página fuera de la vista (derecha)
        nextw.setGeometry(geo.adjusted(geo.width(), 0, geo.width(), 0))
        nextw.setVisible(True)
        nextw.raise_()

        # Animación de salida (actual se mueve a izquierda)
        anim_out = QPropertyAnimation(current, b"geometry", self)
        anim_out.setDuration(duration)
        anim_out.setStartValue(geo)
        anim_out.setEndValue(geo.adjusted(-geo.width(), 0, -geo.width(), 0))
        anim_out.setEasingCurve(QEasingCurve.Type.OutCubic)

        # Animación de entrada (nueva entra desde derecha)
        anim_in = QPropertyAnimation(nextw, b"geometry", self)
        anim_in.setDuration(duration)
        anim_in.setStartValue(nextw.geometry())
        anim_in.setEndValue(geo)
        anim_in.setEasingCurve(QEasingCurve.Type.OutCubic)
        
        # Forzar repintado del contenedor y widgets durante la animación
        def on_value_changed():
            self.update()  # Repintar el container
            current.repaint()  # Repintado inmediato
            nextw.repaint()

        anim_out.valueChanged.connect(on_value_changed)
        anim_in.valueChanged.connect(on_value_changed)

        def on_finished():
            self.setCurrentIndex(index)
            nextw.setGeometry(geo)
            current.hide()
            self._hide_all_except(index)
            
            # Restaurar estilos originales
            current.setStyleSheet(current_style)
            nextw.setStyleSheet(next_style)
            
            self._animating = False

        anim_in.finished.connect(on_finished)
        
        anim_out.start()
        anim_in.start()

    def setCurrentIndexInstant(self, index):
        """Cambia de página sin animación."""
        if self._animating:
            return
        
        self.setCurrentIndex(index)
        self._hide_all_except(index)
        
        # Asegurar visibilidad de la página actual
        current = self.currentWidget()
        if current:
            current.show()
