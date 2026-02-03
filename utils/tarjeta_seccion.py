from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QFrame, QGraphicsDropShadowEffect
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont, QColor


class TarjetaSeccion(QWidget):
    """Widget de tarjeta para mostrar info de una sección."""
    
    clicked = Signal()
    clic_en_ver_estudiantes = Signal(int)
    clic_en_editar = Signal(int)

    def __init__(self, seccion_data: dict, parent=None):
        super().__init__(parent)
        self.seccion_data = seccion_data   # se guardan los datos de la sección
        self.seccion_id = seccion_data["id"]

        self.setFixedSize(290, 170)        # tamaño fijo recomendado
        self.setObjectName("tarjetaSeccion")
        
        # para que reciba clics
        self.setCursor(Qt.PointingHandCursor)   # cambia el cursor a manito
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.setup_ui()
        self.aplicar_estilo()
    

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(8)

        # 1. Título grande
        titulo = QLabel(f"{self.seccion_data['grado']} - {self.seccion_data['letra']}")
        titulo.setFont(QFont("Segoe UI", 14, QFont.Bold))
        titulo.setObjectName("tituloTarjeta")
        layout.addWidget(titulo)

        # 2. Línea separadora sutil
        linea = QFrame()
        linea.setFrameShape(QFrame.HLine)
        linea.setStyleSheet("color: #e0e0e0;")
        layout.addWidget(linea)

        # 3. Información en filas
        docente = self.seccion_data.get("docente_nombre", "Sin asignar")
        lbl_docente = QLabel(f"👨‍🏫 Docente: {docente}")
        lbl_docente.setObjectName("lblDocente")
        layout.addWidget(lbl_docente)

        ocupacion = f"{self.seccion_data['estudiantes_actuales']} / {self.seccion_data['cupo']}"
        self.lbl_estudiantes = QLabel(f"👥 Estudiantes: {ocupacion}")
        layout.addWidget(self.lbl_estudiantes)

        salon = self.seccion_data.get("salon", "No asignado")
        lbl_salon = QLabel(f"🏫 Salón: {salon}")
        layout.addWidget(lbl_salon)

        # 4. Espacio flexible para empujar botones abajo
        layout.addStretch()

        # 5. Botones en fila horizontal
        botones_layout = QHBoxLayout()
        botones_layout.addStretch()

        layout.addLayout(botones_layout)

    def aplicar_estilo(self):
        self.setStyleSheet("""
            QWidget#tarjetaSeccion {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 15px;
            }
            QWidget#tarjetaSeccion:hover {
                border: 2px solid #3498db;
            }
            #tituloTarjeta {
                color: #2c3e50;
            }
            #lblDocente {
                color: #27ae60;
            }
            QLabel {
                background: transparent;
            }
        """)

        # Aplicar sombra
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(12)
        sombra.setXOffset(0)
        sombra.setYOffset(2)
        sombra.setColor(QColor(0, 0, 0, 50))
        self.setGraphicsEffect(sombra)

        # Si el docente está sin asignar → rojo
        docente_nombre = self.seccion_data.get("docente_nombre", "")
        if docente_nombre in ("Vacante", None, "", "Sin asignar"):
            self.findChild(QLabel, "lblDocente").setStyleSheet("color: #e74c3c;")

    def actualizar_conteo_estudiantes(self, estudiantes_actuales):
        """Actualiza el conteo de estudiantes."""
        self.seccion_data['estudiantes_actuales'] = estudiantes_actuales
        ocupacion = f"{estudiantes_actuales} / {self.seccion_data['cupo']}"
        self.lbl_estudiantes.setText(f"👥 Estudiantes: {ocupacion}")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clic_en_ver_estudiantes.emit(self.seccion_id)
        super().mousePressEvent(event)