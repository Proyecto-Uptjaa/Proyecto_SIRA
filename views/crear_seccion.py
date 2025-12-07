import re
from ui_compiled.crear_seccion_ui import Ui_crear_seccion
from PySide6.QtWidgets import QDialog, QMessageBox
from models.secciones_model import SeccionesModel
from utils.dialogs import crear_msgbox
from datetime import datetime


class CrearSeccion(QDialog, Ui_crear_seccion):
    def __init__(self, usuario_actual, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual

        self.setupUi(self)   # esto mete todos los widgets en self

        # Ventana Registro usuario
        self.setWindowTitle("Crear nueva sección")

        # Botones
        self.btnCrear_seccion.clicked.connect(self.guardar_en_bd)
        self.btnCancelar_crear_seccion.clicked.connect(self.reject)

        # señales: solo reaccionan cuando el usuario elige algo
        self.cbxNivel_crear_seccion.currentIndexChanged.connect(self.on_nivel_changed)
        self.cbxGrado_crear_seccion.currentIndexChanged.connect(self.on_grado_changed)

        # dejar los combos vacíos y deshabilitados hasta selección
        self.cbxGrado_crear_seccion.clear()
        self.cbxLetra_crear_seccion.clear()
        self.cbxGrado_crear_seccion.setEnabled(False)
        self.cbxLetra_crear_seccion.setEnabled(False)

    def guardar_en_bd(self):
        # --- Datos seccion ---
        nivel = self.cbxNivel_crear_seccion.currentText().strip()
        grado = self.cbxGrado_crear_seccion.currentText().strip()
        letra = self.cbxLetra_crear_seccion.currentText().strip()
        salon = self.lneSalon_crear_seccion.text().strip() or None
        cupo_text = self.lneCupo_crear_seccion.text().strip()
        anio_text = self.lneAnio_crear_seccion.text().strip()

        try:
            cupo = int(cupo_text) if cupo_text else None
        except ValueError:
            crear_msgbox(self, "Error", "Cupo debe ser un número.", QMessageBox.Warning).exec()
            return

        try:
            año = int(anio_text) if anio_text else datetime.now().year
        except ValueError:
            crear_msgbox(self, "Error", "Año inválido.", QMessageBox.Warning).exec()
            return

        if not nivel or not grado or not letra:
            msg = crear_msgbox(
                    self,
                    "Campos incompletos",
                    "Por favor, completa los campos obligatorios (nivel, grado, letra).",
                    QMessageBox.Warning,
                )
            msg.exec()
            return

        # Normalizar para la búsqueda (mantener presentación original para insertar)
        nivel_norm = nivel.strip()
        grado_norm = grado.strip()
        letra_norm = letra.strip()

        # Verificar si ya existe la sección con la misma clave y año
        existente = SeccionesModel.obtener_por_clave(nivel_norm, grado_norm, letra_norm, año)
        if existente:
            crear_msgbox(
                self,
                "Sección existente",
                f"Ya existe una sección con nivel='{nivel}', grado='{grado}', letra='{letra}' para el año {año} (id={existente.get('id')}).",
                QMessageBox.Warning
            ).exec()
            return

        try:
            ok = SeccionesModel.crear(nivel=nivel, grado=grado, letra=letra, salon=salon, cupo=cupo, año_inicio=año)
            if ok:
                crear_msgbox(self, "Éxito", "Sección creada correctamente.", QMessageBox.Information).exec()
                self.accept()
            else:
                crear_msgbox(self, "Error", "No se pudo crear la sección. Revisa la consola.", QMessageBox.Critical).exec()
        except Exception as err:
            crear_msgbox(self, "Error", f"No se pudo guardar: {err}", QMessageBox.Critical).exec()

    def on_nivel_changed(self, index):
        """Se ejecuta cuando el usuario selecciona un nivel; pobla grados y habilita el combo."""
        nivel = self.cbxNivel_crear_seccion.currentText().strip()
        # limpiar y bloquear letra siempre que cambie nivel
        self.cbxLetra_crear_seccion.clear()
        self.cbxLetra_crear_seccion.setEnabled(False)

        if not nivel:
            self.cbxGrado_crear_seccion.clear()
            self.cbxGrado_crear_seccion.setEnabled(False)
            return

        # poblar grados según nivel (usando la función ya existente)
        self.cbxGrado_crear_seccion.clear()

        n = nivel.lower()
        if "primaria" in n:
            opciones = ["1ero", "2do", "3ro", "4to", "5to", "6to"]
        elif "inicial" in n or "pre" in n:
            opciones = ["1er nivel", "2do nivel", "3er nivel"]
        else:
            opciones = ["1", "2", "3", "4", "5", "6"]

        # insertar opción vacía primero para que el combo quede visualmente vacío
        self.cbxGrado_crear_seccion.addItem("")
        for g in opciones:
            self.cbxGrado_crear_seccion.addItem(str(g))

        self.cbxGrado_crear_seccion.setEnabled(True)
        # forzar índice al placeholder vacío
        self.cbxGrado_crear_seccion.setCurrentIndex(0)

    def actualizar_grados(self, nivel):
        """Compatibilidad: mantiene comportamiento previo si se llama directamente."""
        self.on_nivel_changed(self.cbxNivel_crear_seccion.currentIndex())

    def on_grado_changed(self, index):
        """Habilitar y poblar letras cuando el usuario selecciona un grado válido."""
        if index is None or index < 0:
            self.cbxLetra_crear_seccion.clear()
            self.cbxLetra_crear_seccion.setEnabled(False)
            return

        # si se seleccionó el placeholder (índice 0), deshabilitar letras
        if index == 0:
            self.cbxLetra_crear_seccion.clear()
            self.cbxLetra_crear_seccion.setEnabled(False)
            return

        grado_text = self.cbxGrado_crear_seccion.currentText().strip()
        if not grado_text:
            self.cbxLetra_crear_seccion.clear()
            self.cbxLetra_crear_seccion.setEnabled(False)
            return

        # poblar letras con placeholder vacío primero
        self.cbxLetra_crear_seccion.clear()
        self.cbxLetra_crear_seccion.addItem("")
        letras = ["A", "B", "C", "D", "E", "F"]
        for l in letras:
            self.cbxLetra_crear_seccion.addItem(l)

        self.cbxLetra_crear_seccion.setEnabled(True)
        self.cbxLetra_crear_seccion.setCurrentIndex(0)