import re
from ui_compiled.crear_seccion_ui import Ui_crear_seccion
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Qt
from models.secciones_model import SeccionesModel
from models.materias_model import MateriasModel
from models.anio_model import AnioEscolarModel
from utils.dialogs import crear_msgbox
from utils.sombras import crear_sombra_flotante
from datetime import datetime


class CrearSeccion(QDialog, Ui_crear_seccion):
    """Diálogo para crear nuevas secciones."""
    
    def __init__(self, usuario_actual, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.materias_seleccionadas = []  # IDs de materias a asignar

        self.setupUi(self)
        self.setWindowTitle("Crear nueva sección")

        # Conectar botones
        self.btnCrear_seccion.clicked.connect(self.guardar_en_bd)
        self.btnCancelar_crear_seccion.clicked.connect(self.reject)
        self.btnAsignar_materias.clicked.connect(self.abrir_dialogo_materias)

        # Aplicar sombras
        crear_sombra_flotante(self.btnCrear_seccion)
        crear_sombra_flotante(self.btnCancelar_crear_seccion)
        crear_sombra_flotante(self.btnAsignar_materias)
        crear_sombra_flotante(self.lneCupo_crear_seccion, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lneSalon_crear_seccion, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.frameRol_login_2, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.frameRol_login_3, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.frameRol_login_4, blur_radius=8, y_offset=1)

        # Conectar señales
        self.cbxNivel_crear_seccion.currentIndexChanged.connect(self.on_nivel_changed)
        self.cbxGrado_crear_seccion.currentIndexChanged.connect(self.on_grado_changed)

        # Inicializar combos vacíos
        self._inicializar_combos()
        
        # Deshabilitar botón de materias hasta seleccionar nivel/grado
        self.btnAsignar_materias.setEnabled(False)
        self._actualizar_texto_boton_materias()

        # Obtener año escolar actual
        self.anio_escolar_actual = AnioEscolarModel.obtener_actual()
        if not self.anio_escolar_actual:
            crear_msgbox(
                self,
                "Sin año activo",
                "No hay año escolar activo. Debe aperturar uno primero.",
                QMessageBox.Critical
            ).exec()
            self.reject()
            return
    
    def _inicializar_combos(self):
        """Configura estado inicial de los combos."""
        # Grado y letra deshabilitados hasta seleccionar nivel
        self.cbxGrado_crear_seccion.clear()
        self.cbxLetra_crear_seccion.clear()
        self.cbxGrado_crear_seccion.setEnabled(False)
        self.cbxLetra_crear_seccion.setEnabled(False)

    def guardar_en_bd(self):
        """Valida y guarda la sección en la BD."""
        # --- RECOLECTAR DATOS ---
        nivel = self.cbxNivel_crear_seccion.currentText().strip()
        grado = self.cbxGrado_crear_seccion.currentText().strip()
        letra = self.cbxLetra_crear_seccion.currentText().strip()
        salon = self.lneSalon_crear_seccion.text().strip() or None
        cupo_text = self.lneCupo_crear_seccion.text().strip()

        # --- VALIDACIONES ---
        
        # Validar campos obligatorios
        if not nivel or nivel == "Seleccione nivel":
            crear_msgbox(
                self,
                "Campo requerido",
                "Debe seleccionar un nivel educativo.",
                QMessageBox.Warning
            ).exec()
            return
        
        if not grado:
            crear_msgbox(
                self,
                "Campo requerido",
                "Debe seleccionar un grado.",
                QMessageBox.Warning
            ).exec()
            return
        
        if not letra:
            crear_msgbox(
                self,
                "Campo requerido",
                "Debe seleccionar una letra de sección.",
                QMessageBox.Warning
            ).exec()
            return

        # Validar cupo
        if not cupo_text:
            crear_msgbox(
                self,
                "Campo requerido",
                "Debe ingresar el cupo máximo de estudiantes.",
                QMessageBox.Warning
            ).exec()
            return
        
        try:
            cupo = int(cupo_text)
            if cupo < 1 or cupo > 50:
                crear_msgbox(
                    self,
                    "Cupo inválido",
                    "El cupo debe estar entre 1 y 50 estudiantes.",
                    QMessageBox.Warning
                ).exec()
                return
        except ValueError:
            crear_msgbox(
                self,
                "Cupo inválido",
                "El cupo debe ser un número entero.",
                QMessageBox.Warning
            ).exec()
            return

        # --- VERIFICAR DUPLICADOS ---
        
        existente = SeccionesModel.obtener_por_clave(
            nivel,
            grado,
            letra,
            self.anio_escolar_actual['id']
        )

        try:
            if existente:
                if existente['activo'] == 0:
                    # Sección existe pero está inactiva -> preguntar si reactivar
                    confirmar = crear_msgbox(
                        self,
                        "Sección inactiva",
                        f"La sección {grado} {letra} ({nivel}) ya existe pero está inactiva.\n\n"
                        "¿Desea reactivarla?",
                        QMessageBox.Question,
                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                        QMessageBox.StandardButton.Yes
                    )
                    
                    if confirmar.exec() == QMessageBox.StandardButton.Yes:
                        ok, mensaje = SeccionesModel.reactivar(
                            existente['id'],
                            salon=salon,
                            cupo=cupo,
                            usuario_actual=self.usuario_actual
                        )
                        
                        if ok:
                            # Asignar materias si se seleccionaron
                            if self.materias_seleccionadas:
                                MateriasModel.asignar_a_seccion(
                                    existente['id'],
                                    self.materias_seleccionadas,
                                    self.usuario_actual
                                )
                                mensaje += f"\n{len(self.materias_seleccionadas)} materias asignadas."
                            
                            crear_msgbox(
                                self,
                                "Éxito",
                                mensaje,
                                QMessageBox.Information
                            ).exec()
                            self.accept()
                        else:
                            crear_msgbox(
                                self,
                                "Error",
                                mensaje,
                                QMessageBox.Critical
                            ).exec()
                    return
                else:
                    # Sección ya existe y está activa
                    crear_msgbox(
                        self,
                        "Sección existente",
                        f"Ya existe una sección activa {grado} {letra} ({nivel}) "
                        f"en el año {self.anio_escolar_actual['nombre']}.",
                        QMessageBox.Warning
                    ).exec()
                    return

            # --- CREAR NUEVA SECCIÓN ---
            
            ok, mensaje = SeccionesModel.crear(
                nivel=nivel,
                grado=grado,
                letra=letra,
                salon=salon,
                cupo=cupo,
                anio_escolar_id=self.anio_escolar_actual['id'],
                usuario_actual=self.usuario_actual
            )
            
            if ok:
                # Asignar materias si se seleccionaron
                if self.materias_seleccionadas:
                    # Obtener el ID de la sección recién creada
                    nueva_seccion = SeccionesModel.obtener_por_clave(
                        nivel, grado, letra, self.anio_escolar_actual['id']
                    )
                    if nueva_seccion:
                        MateriasModel.asignar_a_seccion(
                            nueva_seccion['id'],
                            self.materias_seleccionadas,
                            self.usuario_actual
                        )
                        mensaje += f"\n{len(self.materias_seleccionadas)} materias asignadas."
                
                crear_msgbox(
                    self,
                    "Éxito",
                    mensaje,
                    QMessageBox.Information
                ).exec()
                self.accept()
            else:
                crear_msgbox(
                    self,
                    "Error",
                    mensaje,
                    QMessageBox.Warning
                ).exec()

        except Exception as err:
            crear_msgbox(
                self,
                "Error inesperado",
                f"No se pudo guardar la sección: {err}",
                QMessageBox.Critical
            ).exec()

    def on_nivel_changed(self, index):
        """Actualiza grados disponibles según el nivel seleccionado"""
        nivel = self.cbxNivel_crear_seccion.currentText().strip()
        
        # Limpiar y bloquear letra
        self.cbxLetra_crear_seccion.clear()
        self.cbxLetra_crear_seccion.setEnabled(False)

        # Si no hay selección válida, bloquear grado
        if not nivel or nivel == "Seleccione nivel":
            self.cbxGrado_crear_seccion.clear()
            self.cbxGrado_crear_seccion.setEnabled(False)
            return

        # Poblar grados según nivel
        self.cbxGrado_crear_seccion.clear()
        
        if "Primaria" in nivel:
            grados = SeccionesModel.GRADOS_PRIMARIA
        elif "Inicial" in nivel:
            grados = SeccionesModel.GRADOS_INICIAL
        else:
            grados = []

        # Agregar placeholder
        self.cbxGrado_crear_seccion.addItem("Seleccione grado")
        
        # Deshabilitar placeholder
        model = self.cbxGrado_crear_seccion.model()
        item0 = model.item(0)
        if item0:
            item0.setEnabled(False)
            item0.setForeground(Qt.GlobalColor.gray)
        
        # Agregar grados
        self.cbxGrado_crear_seccion.addItems(grados)
        
        # Habilitar y seleccionar placeholder
        self.cbxGrado_crear_seccion.setEnabled(True)
        self.cbxGrado_crear_seccion.setCurrentIndex(0)

    def actualizar_grados(self, nivel):
        """Método de compatibilidad (alias de on_nivel_changed)"""
        self.on_nivel_changed(self.cbxNivel_crear_seccion.currentIndex())

    def on_grado_changed(self, index):
        """Habilita y pobla letras cuando se selecciona un grado válido"""
        # Si es placeholder o inválido, bloquear letras y materias
        if index is None or index <= 0:
            self.cbxLetra_crear_seccion.clear()
            self.cbxLetra_crear_seccion.setEnabled(False)
            self.btnAsignar_materias.setEnabled(False)
            self.btnAsignar_materias.setVisible(False)  # Ocultar para Inicial
            self.materias_seleccionadas = []
            self._actualizar_texto_boton_materias()
            return

        grado_text = self.cbxGrado_crear_seccion.currentText().strip()
        if not grado_text or grado_text == "Seleccione grado":
            self.cbxLetra_crear_seccion.clear()
            self.cbxLetra_crear_seccion.setEnabled(False)
            self.btnAsignar_materias.setEnabled(False)
            self.btnAsignar_materias.setVisible(False)
            self.materias_seleccionadas = []
            self._actualizar_texto_boton_materias()
            return

        # Verificar si es Primaria (solo Primaria tiene materias)
        nivel = self.cbxNivel_crear_seccion.currentText().strip()
        es_primaria = "Primaria" in nivel
        
        # Habilitar botón de materias solo para Primaria
        self.btnAsignar_materias.setVisible(es_primaria)
        self.btnAsignar_materias.setEnabled(es_primaria)
        self.materias_seleccionadas = []
        self._actualizar_texto_boton_materias()

        # Poblar letras
        self.cbxLetra_crear_seccion.clear()
        
        # Agregar placeholder
        self.cbxLetra_crear_seccion.addItem("Seleccione letra")
        
        # Deshabilitar placeholder
        model = self.cbxLetra_crear_seccion.model()
        item0 = model.item(0)
        if item0:
            item0.setEnabled(False)
            item0.setForeground(Qt.GlobalColor.gray)
        
        # Agregar letras según nivel/grado
        # "Única" solo aplica para 1er Nivel y 2do Nivel de Inicial
        if nivel == "Inicial" and grado_text in ("1er Nivel", "2do Nivel"):
            letras = ["A", "B", "C", "D", "E", "F", "Única"]
        else:
            letras = ["A", "B", "C", "D", "E", "F"]
        self.cbxLetra_crear_seccion.addItems(letras)
        
        # Habilitar y seleccionar placeholder
        self.cbxLetra_crear_seccion.setEnabled(True)
        self.cbxLetra_crear_seccion.setCurrentIndex(0)

    def abrir_dialogo_materias(self):
        """Abre el diálogo para asignar materias a la sección."""
        nivel = self.cbxNivel_crear_seccion.currentText().strip()
        grado = self.cbxGrado_crear_seccion.currentText().strip()
        
        if not nivel or nivel == "Seleccione nivel" or not grado or grado == "Seleccione grado":
            crear_msgbox(
                self,
                "Aviso",
                "Debe seleccionar un nivel y grado antes de asignar materias.",
                QMessageBox.Information
            ).exec()
            return
        
        from views.asignar_materias import AsignarMateriasDialog
        
        dialogo = AsignarMateriasDialog(
            seccion_id=None,  # Es nueva sección, aún no tiene ID
            nivel=nivel,
            grado=grado,
            usuario_actual=self.usuario_actual,
            parent=self
        )
        
        # Pre-marcar materias ya seleccionadas
        for chk in dialogo.checkboxes:
            if chk.property("materia_id") in self.materias_seleccionadas:
                chk.setChecked(True)
        
        if dialogo.exec() == QDialog.Accepted:
            self.materias_seleccionadas = dialogo.get_materias_seleccionadas()
            self._actualizar_texto_boton_materias()

    def _actualizar_texto_boton_materias(self):
        """Actualiza el texto del botón según las materias seleccionadas."""
        cantidad = len(self.materias_seleccionadas)
        if cantidad > 0:
            self.btnAsignar_materias.setText(f"Materias ({cantidad})")
            self.btnAsignar_materias.setStyleSheet("""
                QPushButton {
                    background-color: #27ae60;
                    color: white;
                    border: none;
                    padding: 4px 6px;
                    border-radius: 12px;
                }
                QPushButton:hover { background-color: #1e8449; }
            """)
        else:
            self.btnAsignar_materias.setText("Asignar Materias")
            self.btnAsignar_materias.setStyleSheet("background-color: #2980b9;")