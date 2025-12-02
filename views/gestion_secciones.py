# views/gestion_secciones.py
from PySide6.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, QMessageBox, QInputDialog
)
from PySide6.QtCore import Qt
from utils.tarjeta_seccion import TarjetaSeccion
from ui_compiled.secciones_ui import Ui_secciones
from models.secciones_model import SeccionesModel

class GestionSeccionesPage(QWidget, Ui_secciones):
    def __init__(self, usuario_actual, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.setupUi(self)

        self.scrollArea_secciones.setWidgetResizable(True)
        self.scrollArea_secciones.setAlignment(Qt.AlignTop)
        self.tarjetas = []

        # Botones
        #self.btnCrearSeccion.clicked.connect(self.nueva_seccion)
        #self.lneBuscar.textChanged.connect(self.cargar_secciones)  # filtro en tiempo real

        self.cargar_secciones()

    def cargar_secciones(self):
        # Limpiar
        for i in reversed(range(self.verticalLayout_contenido.count())):
            w = self.verticalLayout_contenido.itemAt(i).widget()
            if w:
                w.deleteLater()
        self.tarjetas.clear()

        todas = SeccionesModel.obtener_todas()

        layout_fila_actual = None
        contador_tarjetas_fila = 0        # ← NUEVO: contador para máximo 3 por fila
        nivel_anterior = None
        año_anterior = None

        for sec in sorted(todas, key=lambda s: (
            -s["año_inicio"],  # más reciente arriba
            0 if s["nivel"] == "Inicial" else 1,  # Inicial siempre arriba
            s["grado"],
            s["letra"] if s["letra"] != "Única" else "Z"
        )):

            # Separador de nivel
            if sec["nivel"] != nivel_anterior:
                lbl = QLabel(f"─── {sec['nivel']} ───")
                lbl.setStyleSheet("font-size: 20px; font-weight: bold; color: #3498db; padding: 10px 0;")
                lbl.setAlignment(Qt.AlignCenter)
                self.verticalLayout_contenido.addWidget(lbl)
                nivel_anterior = sec["nivel"]
                layout_fila_actual = None
                contador_tarjetas_fila = 0

            # NUEVA FILA CADA 3 TARJETAS O AL CAMBIAR DE NIVEL/AÑO
            if layout_fila_actual is None or contador_tarjetas_fila >= 3:
                fila = QWidget()
                layout_fila_actual = QHBoxLayout(fila)
                layout_fila_actual.setSpacing(20)
                layout_fila_actual.setContentsMargins(10, 8, 10, 8)
                layout_fila_actual.addStretch()  # para que queden centradas
                self.verticalLayout_contenido.addWidget(fila)
                contador_tarjetas_fila = 0

            # Crear y agregar tarjeta
            tarjeta = TarjetaSeccion(sec)
            tarjeta.clicked.connect(lambda _, s=sec: self.abrir_detalle(s["id"]))
            tarjeta.clic_en_editar.connect(lambda _, s=sec: self.editar_seccion(s["id"]))
            
            # Insertar antes del stretch final
            layout_fila_actual.insertWidget(layout_fila_actual.count() - 1, tarjeta)
            self.tarjetas.append(tarjeta)

            contador_tarjetas_fila += 1

        # Al final, un stretch para que todo quede arriba
        self.verticalLayout_contenido.addStretch()

    def nueva_seccion(self):
        nivel, ok1 = QInputDialog.getItem(self, "Nivel", "Nivel:", ["Inicial", "Primaria"], 0, False)
        if not ok1: return
        grado, ok2 = QInputDialog.getText(self, "Grado", "Grado (ej: 5to, 1er Nivel):")
        if not ok2: return
        letra, ok3 = QInputDialog.getText(self, "Letra", "Letra (A, B, Única):")
        if not ok3: return
        salon, ok4 = QInputDialog.getText(self, "Salón", "Salón (opcional):")
        cupo, ok5 = QInputDialog.getInt(self, "Cupo", "Cupo máximo:", 30, 20, 40)
        if not ok5: return

        if SeccionesModel.crear(nivel, grado.strip(), letra.strip(), salon.strip() or None, cupo):
            QMessageBox.information(self, "Éxito", "Sección creada")
            self.cargar_secciones()
        else:
            QMessageBox.critical(self, "Error", "No se pudo crear la sección")

    def abrir_detalle(self, seccion_id):
        # Aquí abres tu diálogo de estudiantes
        print("Detalle sección:", seccion_id)

    def editar_seccion(self, seccion_id):
        # Próximo paso
        print("Editar sección:", seccion_id)