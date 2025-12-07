# views/gestion_secciones.py
from PySide6.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, QMessageBox, QInputDialog, QDialog, QVBoxLayout
)
from PySide6.QtCore import Qt
from utils.tarjeta_seccion import TarjetaSeccion
from ui_compiled.secciones_ui import Ui_secciones
from models.secciones_model import SeccionesModel
from views.crear_seccion import CrearSeccion
from views.detalles_seccion import DetallesSeccion


class GestionSeccionesPage(QWidget, Ui_secciones):
    def __init__(self, usuario_actual, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.setupUi(self)

        self.scrollArea_secciones.setWidgetResizable(True)
        self.scrollArea_secciones.setAlignment(Qt.AlignTop)
        self.tarjetas = []

        # Botones
        self.btnCrear_seccion.clicked.connect(self.nueva_seccion)
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
            # conectar a la señal correcta que emite el id de la sección
            tarjeta.clic_en_ver_estudiantes.connect(lambda sid, s=sec: self.abrir_detalle(sid))
            tarjeta.clic_en_editar.connect(lambda _, s=sec: self.editar_seccion(s["id"]))
            
            # Insertar antes del stretch final
            layout_fila_actual.insertWidget(layout_fila_actual.count() - 1, tarjeta)
            self.tarjetas.append(tarjeta)

            contador_tarjetas_fila += 1

        # Al final, un stretch para que todo quede arriba
        self.verticalLayout_contenido.addStretch()

    def nueva_seccion(self):
        ventana = CrearSeccion(self.usuario_actual, self)
        # CrearSeccion se encarga de validar/crear la sección y hace self.accept() si todo fue bien.
        if ventana.exec() == QDialog.Accepted:
            # Recargar listado después de crear correctamente
            self.cargar_secciones()

    def abrir_detalle(self, seccion_id):
        """Abrir ventana de DetallesSeccion sin cambiar su tamaño ni título diseñados."""
        try:
            # Crear la vista como ventana independiente (sin parent) para que use su propio diseño/tamaño
            detalle_widget = DetallesSeccion(self.usuario_actual, seccion_id, parent=None)

            # Mantener referencia para evitar que Python la recoja como basura
            if not hasattr(self, "_detalle_windows"):
                self._detalle_windows = []
            self._detalle_windows.append(detalle_widget)

            # El widget se encarga de su propio título/size; mostrar como ventana independiente
            detalle_widget.setAttribute(Qt.WA_DeleteOnClose)
            detalle_widget.show()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo abrir detalle de sección: {e}")

    def editar_seccion(self, seccion_id):
        """Placeholder: abrir editor de sección (puedes implementar edición en CrearSeccion)."""
        # Aquí puedes abrir un diálogo para editar; por ahora reusa CrearSeccion si la implementas para edición.
        dlg = CrearSeccion(self.usuario_actual, self)
        # TODO: cargar datos de la sección en el diálogo para editar
        if dlg.exec() == QDialog.Accepted:
            self.cargar_secciones()