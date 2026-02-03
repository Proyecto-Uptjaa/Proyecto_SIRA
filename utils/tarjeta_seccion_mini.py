from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QGraphicsDropShadowEffect
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont, QColor


class TarjetaSeccionMini(QWidget):
    """Widget de mini-tarjeta para selección de sección en notas."""
    
    clicked = Signal(dict)  # Emite los datos de la sección
    
    def __init__(self, seccion_data: dict, parent=None):
        super().__init__(parent)
        self.seccion_data = seccion_data
        self.seccion_id = seccion_data.get("id")
        self._seleccionada = False
        
        self.setFixedSize(100, 70)
        self.setObjectName("tarjetaMini")
        self.setCursor(Qt.PointingHandCursor)
        self.setAttribute(Qt.WA_StyledBackground, True)
        
        self.setup_ui()
        self.aplicar_estilo()
    
    def setup_ui(self):
        """Configura la interfaz de la tarjeta."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(2)
        
        # Grado
        grado = self.seccion_data.get("grado", "")
        lbl_grado = QLabel(grado)
        lbl_grado.setFont(QFont("Segoe UI", 9))
        lbl_grado.setAlignment(Qt.AlignCenter)
        lbl_grado.setObjectName("lblGrado")
        layout.addWidget(lbl_grado)
        
        # Letra (grande)
        letra = self.seccion_data.get("letra", "")
        lbl_letra = QLabel(letra)
        lbl_letra.setFont(QFont("Segoe UI", 16, QFont.Bold))
        lbl_letra.setAlignment(Qt.AlignCenter)
        lbl_letra.setObjectName("lblLetra")
        layout.addWidget(lbl_letra)
        
        # Ocupación
        estudiantes = self.seccion_data.get("estudiantes_actuales", 0)
        cupo = self.seccion_data.get("cupo", 30)
        lbl_ocupacion = QLabel(f"{estudiantes}/{cupo}")
        lbl_ocupacion.setFont(QFont("Segoe UI", 8))
        lbl_ocupacion.setAlignment(Qt.AlignCenter)
        lbl_ocupacion.setObjectName("lblOcupacion")
        layout.addWidget(lbl_ocupacion)
    
    def aplicar_estilo(self):
        """Aplica estilos CSS."""
        self._actualizar_estilo()
        
        # Sombra
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(8)
        sombra.setXOffset(0)
        sombra.setYOffset(2)
        sombra.setColor(QColor(0, 0, 0, 40))
        self.setGraphicsEffect(sombra)
    
    def _actualizar_estilo(self):
        """Actualiza el estilo según el estado de selección."""
        if self._seleccionada:
            self.setStyleSheet("""
                QWidget#tarjetaMini {
                    background-color: #2980b9;
                    border: 2px solid #1a5276;
                    border-radius: 10px;
                }
                QLabel {
                    background: transparent;
                    color: white;
                }
            """)
        else:
            self.setStyleSheet("""
                QWidget#tarjetaMini {
                    background-color: white;
                    border: 1px solid #e0e0e0;
                    border-radius: 10px;
                }
                QWidget#tarjetaMini:hover {
                    border: 2px solid #3498db;
                }
                QLabel {
                    background: transparent;
                    color: #2c3e50;
                }
                #lblOcupacion {
                    color: #7f8c8d;
                }
            """)
    
    @property
    def seleccionada(self):
        return self._seleccionada
    
    @seleccionada.setter
    def seleccionada(self, valor):
        self._seleccionada = valor
        self._actualizar_estilo()
    
    def mousePressEvent(self, event):
        """Maneja el clic en la tarjeta."""
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self.seccion_data)
        super().mousePressEvent(event)
    
    def get_nivel(self):
        """Retorna el nivel de la sección."""
        return self.seccion_data.get("nivel", "")
    
    def get_grado_letra(self):
        """Retorna grado y letra concatenados."""
        return f"{self.seccion_data.get('grado', '')} {self.seccion_data.get('letra', '')}".strip()
