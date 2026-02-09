from PySide6.QtWidgets import (
    QWidget, QDialog, QMessageBox, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton,
    QFrame, QScrollArea, QGridLayout, QTableWidget, QTableWidgetItem,
    QHeaderView, QAbstractItemView
)
from PySide6.QtCore import Qt, QTimer, QSize
from PySide6.QtGui import QStandardItemModel, QStandardItem, QFont, QIcon

from ui_compiled.gestion_materias_ui import Ui_gestion_materias
from models.materias_model import MateriasModel
from models.areas_model import AreaAprendizajeModel
from views.delegates import BaseEstadoDelegate
from utils.sombras import crear_sombra_flotante
from utils.dialogs import crear_msgbox
from utils.proxies import ProxyConEstado


class GestionMateriasPage(QWidget, Ui_gestion_materias):
    """Página de gestión de materias."""
    
    def __init__(self, usuario_actual, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.setupUi(self)
        
        # Mostrar usuario conectado
        self.lblConectado_como.setText(f"Conectado como: {self.usuario_actual['username']}")
        
        # Configurar proxy para filtrado
        self.proxy_materias = ProxyConEstado(columna_estado=5, parent=self)
        self.tableW_materias.setModel(self.proxy_materias)
        
        # Configurar delegate para colorear inactivas
        self.delegate_materias = BaseEstadoDelegate(parent=self, estado_columna=5)
        self.tableW_materias.setItemDelegate(self.delegate_materias)
        
        # Conectar controles
        self.chkMostrar_inactivas_materias.stateChanged.connect(
            lambda estado: self.proxy_materias.setMostrarInactivos(bool(estado))
        )
        self.btnNueva_materia.clicked.connect(self.nueva_materia)
        self.btnGestion_areas.clicked.connect(self.abrir_gestion_areas)
        self.btnActualizar_tabla_materias.clicked.connect(self.cargar_materias)
        self.btnEditar_materia.clicked.connect(self.editar_materia)
        self.btnDesactivar_materia.clicked.connect(self.cambiar_estado_materia)
        self.lneBuscar_materias.textChanged.connect(self.filtrar_tabla)
        self.cbxFiltro_materias.currentIndexChanged.connect(
            lambda _: self.filtrar_tabla(self.lneBuscar_materias.text())
        )
        
        # Actualizar el botón cuando cambia la selección
        self.tableW_materias.selectionModel().selectionChanged.connect(
            self.actualizar_texto_boton_estado
        )
        
        # Cargar datos iniciales
        self.cargar_materias()
        
        # Timer de actualización
        self.timer_actualizacion = QTimer(self)
        self.timer_actualizacion.timeout.connect(self.cargar_materias)
        self.timer_actualizacion.start(30000)  # Cada 30 segundos
        
        # Aplicar sombras
        self._aplicar_sombras()
    
    def abrir_gestion_areas(self):
        """Abre el diálogo de gestión de áreas de aprendizaje."""
        dialogo = DialogoGestionAreas(self.usuario_actual, parent=self)
        dialogo.exec()
        # Recargar materias por si cambió algo
        self.cargar_materias()
    
    def _aplicar_sombras(self):
        crear_sombra_flotante(self.btnNueva_materia)
        crear_sombra_flotante(self.btnGestion_areas)
        crear_sombra_flotante(self.btnEditar_materia)
        crear_sombra_flotante(self.btnDesactivar_materia, opacity=120)
        crear_sombra_flotante(self.btnActualizar_tabla_materias)
        crear_sombra_flotante(self.frameTabla_materias, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lneBuscar_materias, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lblTitulo_materias, blur_radius=5, y_offset=1)
        crear_sombra_flotante(self.lblLogo_materias, blur_radius=5, y_offset=1)
    
    def cargar_materias(self):
        """Carga las materias en la tabla."""
        materias = MateriasModel.listar_todas(solo_activas=False)
        
        # Crear modelo
        modelo = QStandardItemModel()
        modelo.setHorizontalHeaderLabels([
            "ID", "Nombre", "Abreviatura", "Área de Aprendizaje",
            "Tipo", "Estado", "Grados"
        ])
        
        for materia in materias:
            estado_texto = "Activo" if materia["estado"] else "Inactivo"
            area_nombre = materia.get("area_nombre") or "Sin asignar"
            fila = [
                QStandardItem(str(materia["id"])),
                QStandardItem(materia["nombre"]),
                QStandardItem(materia.get("abreviatura") or "-"),
                QStandardItem(area_nombre),
                QStandardItem("Literal (A-E)"),
                QStandardItem(estado_texto),
                QStandardItem(materia.get("grados_resumen", "Sin asignar"))
            ]
            
            # Centrar algunas columnas
            fila[0].setTextAlignment(Qt.AlignCenter)
            fila[2].setTextAlignment(Qt.AlignCenter)
            fila[4].setTextAlignment(Qt.AlignCenter)
            fila[5].setTextAlignment(Qt.AlignCenter)
            
            # Guardar datos extras
            fila[0].setData(materia, Qt.UserRole)
            
            modelo.appendRow(fila)
        
        self.proxy_materias.setSourceModel(modelo)
        
        # Ocultar columna ID y Tipo
        self.tableW_materias.setColumnHidden(0, True)
        self.tableW_materias.setColumnHidden(4, True)  # Ocultar tipo (todas son literales)
        
        # Ajustar anchos
        self.tableW_materias.setColumnWidth(1, 180)   # Nombre
        self.tableW_materias.setColumnWidth(2, 80)    # Abreviatura
        self.tableW_materias.setColumnWidth(3, 200)   # Área de Aprendizaje
        self.tableW_materias.setColumnWidth(5, 80)    # Estado
        self.tableW_materias.setColumnWidth(6, 230)   # Grados
    
    def filtrar_tabla(self, texto):
        """Filtra la tabla por texto de búsqueda."""
        columna = self.cbxFiltro_materias.currentIndex()
        # Mapear índice del combo a columna real
        # 0=Todos, 1=Nombre, 2=Abreviatura, 3=Estado, 4=Grados
        columnas_filtro = {
            0: -1,  # Todas
            1: 1,   # Nombre
            2: 2,   # Abreviatura
            3: 5,   # Estado
            4: 6    # Grados
        }
        columna_real = columnas_filtro.get(columna, -1)
        
        self.proxy_materias.setFilterKeyColumn(columna_real)
        self.proxy_materias.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.proxy_materias.setFilterFixedString(texto)
    
    def obtener_materia_seleccionada(self):
        """Obtiene la materia seleccionada en la tabla."""
        indices = self.tableW_materias.selectionModel().selectedRows()
        if not indices:
            return None
        
        # Obtener el índice real del modelo fuente
        indice_proxy = indices[0]
        indice_source = self.proxy_materias.mapToSource(indice_proxy)
        modelo = self.proxy_materias.sourceModel()
        
        # Obtener datos de la primera columna (ID)
        item = modelo.item(indice_source.row(), 0)
        return item.data(Qt.UserRole) if item else None
    
    def nueva_materia(self):
        """Abre el diálogo para crear nueva materia."""
        dialogo = DialogoMateria(self.usuario_actual, parent=self)
        if dialogo.exec() == QDialog.Accepted:
            self.cargar_materias()
    
    def editar_materia(self):
        """Edita la materia seleccionada."""
        materia = self.obtener_materia_seleccionada()
        if not materia:
            crear_msgbox(
                self, "Aviso", 
                "Seleccione una materia para editar.",
                QMessageBox.Information
            ).exec()
            return
        
        dialogo = DialogoMateria(self.usuario_actual, materia=materia, parent=self)
        if dialogo.exec() == QDialog.Accepted:
            self.cargar_materias()
    
    def cambiar_estado_materia(self):
        """Activa o desactiva la materia seleccionada."""
        materia = self.obtener_materia_seleccionada()
        if not materia:
            crear_msgbox(
                self, "Aviso",
                "Seleccione una materia.",
                QMessageBox.Information
            ).exec()
            return
        
        # El estado viene en materia["estado"] como 1/0 o True/False
        estado_actual = bool(materia["estado"])
        accion = "desactivar" if estado_actual else "activar"
        accion_texto = "desactivará" if estado_actual else "activará"
        
        msg = crear_msgbox(
            self, "Confirmar",
            f"¿Está seguro de {accion} la materia '{materia['nombre']}'?\n\n"
            f"La materia se {accion_texto} inmediatamente.",
            QMessageBox.Question,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if msg.exec() == QMessageBox.StandardButton.Yes:
            ok, msg = MateriasModel.cambiar_estado(
                materia["id"],
                not estado_actual,
                self.usuario_actual
            )
            
            if ok:
                crear_msgbox(self, "Éxito", msg, QMessageBox.Information).exec()
                self.cargar_materias()
                # Actualizar el texto del botón según el nuevo estado
                self.actualizar_texto_boton_estado()
            else:
                crear_msgbox(self, "Error", msg, QMessageBox.Warning).exec()
    
    def actualizar_texto_boton_estado(self):
        """Actualiza el texto del botón de activar/desactivar según la selección."""
        materia = self.obtener_materia_seleccionada()
        if materia:
            estado_actual = bool(materia["estado"])
            if estado_actual:
                self.btnDesactivar_materia.setText("Desactivar")
                self.btnDesactivar_materia.setIcon(QIcon(":/icons/cancelar_w2.png"))
                self.btnDesactivar_materia.setIconSize(QSize(18, 18))
                self.btnDesactivar_materia.setStyleSheet("""
                    QPushButton {
                        background-color: #e74c3c;
                        color: #FFFFFF;
                        border: none;
                        padding: 8px 6px;
                        border-radius: 14px;
                    }
                    QPushButton:hover {
                        background-color: #C0392B
                    }
                """)
            else:
                self.btnDesactivar_materia.setText("Activar")
                self.btnDesactivar_materia.setIcon(QIcon(":/icons/confirm_white.png"))
                self.btnDesactivar_materia.setIconSize(QSize(18, 18))
                self.btnDesactivar_materia.setStyleSheet("""
                    QPushButton {
                        background-color: #27ae60;
                        color: #FFFFFF;
                        border: none;
                        padding: 8px 6px;
                        border-radius: 14px;
                    }
                    QPushButton:hover {
                        background-color: #1e8449
                    }
                """)
        else:
            self.btnDesactivar_materia.setText("Desactivar")
            self.btnDesactivar_materia.setIcon(QIcon(":/icons/cancelar_w2.png"))
            self.btnDesactivar_materia.setIconSize(QSize(18, 18))
    
    def closeEvent(self, event):
        """Detiene el timer al cerrar."""
        if hasattr(self, 'timer_actualizacion'):
            self.timer_actualizacion.stop()
        event.accept()


class DialogoMateria(QDialog):
    """Diálogo para crear o editar una materia (solo para Primaria)."""
    
    GRADOS_PRIMARIA = ["1ero", "2do", "3ero", "4to", "5to", "6to"]
    
    def __init__(self, usuario_actual, materia=None, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.materia = materia
        self.checkboxes_grados = {}
        
        self.setWindowTitle("Nueva Materia" if not materia else "Editar Materia")
        self.setFixedSize(450, 600)
        self.setStyleSheet("background-color: #f5f6fa;")
        
        self.setup_ui()
        
        if materia:
            self.cargar_datos_materia()
    
    def setup_ui(self):
        """Configura la interfaz del diálogo."""
        layout = QVBoxLayout(self)
        layout.setSpacing(5)
        layout.setContentsMargins(20, 10, 20, 10)
        
        # Título
        titulo = QLabel("Nueva Materia" if not self.materia else "Editar Materia")
        titulo.setFont(QFont("Segoe UI", 14, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(titulo)
        
        # Nombre
        layout.addWidget(QLabel("Nombre de la materia:"))
        self.txt_nombre = QLineEdit()
        self.txt_nombre.setPlaceholderText("Ej: Matemática")
        self.txt_nombre.setFixedHeight(30)
        self.txt_nombre.setStyleSheet(self._estilo_input())
        layout.addWidget(self.txt_nombre)
        
        # Abreviatura
        layout.addWidget(QLabel("Abreviatura (opcional):"))
        self.txt_abreviatura = QLineEdit()
        self.txt_abreviatura.setPlaceholderText("Ej: MAT")
        self.txt_abreviatura.setMaxLength(10)
        self.txt_abreviatura.setFixedHeight(30)
        self.txt_abreviatura.setStyleSheet(self._estilo_input())
        layout.addWidget(self.txt_abreviatura)
        
        # Nota: Todas las materias de Primaria usan evaluación literal (A-E)
        layout.addWidget(QLabel("Nota: La evaluación es literal (A, B, C, D, E)"))
        
        # Grados aplicables (solo Primaria)
        layout.addWidget(QLabel("Grados de Primaria donde aplica esta materia:"))
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setMinimumHeight(120)
        scroll.setMaximumHeight(150)
        scroll.setStyleSheet("QScrollArea { border: 1px solid #ccc; border-radius: 8px; background-color: white; }")
        
        contenedor_grados = QWidget()
        grid = QGridLayout(contenedor_grados)
        grid.setSpacing(8)
        grid.setContentsMargins(10, 10, 10, 10)
        
        # Solo Primaria (Inicial no tiene materias formales)
        for i, grado in enumerate(self.GRADOS_PRIMARIA):
            chk = QCheckBox(grado)
            self.checkboxes_grados[("Primaria", grado)] = chk
            grid.addWidget(chk, i // 3, i % 3)
        
        scroll.setWidget(contenedor_grados)
        layout.addWidget(scroll)
        
        # Checkbox seleccionar todos
        self.chk_todos = QCheckBox("Seleccionar todos los grados")
        self.chk_todos.stateChanged.connect(self.toggle_todos_grados)
        layout.addWidget(self.chk_todos)
        
        # Área de Aprendizaje (obligatorio)
        layout.addWidget(QLabel("Área de Aprendizaje:"))
        self.cbx_area = QComboBox()
        self.cbx_area.setFixedHeight(30)
        self.cbx_area.setStyleSheet(self._estilo_input())
        self._cargar_areas()
        layout.addWidget(self.cbx_area)
        
        layout.addStretch()
        
        # Botones
        frame_botones = QFrame()
        frame_botones.setStyleSheet("border: none;")
        h_layout = QHBoxLayout(frame_botones)
        
        btn_cancelar = QPushButton("Cancelar")
        btn_cancelar.setFixedHeight(35)
        btn_cancelar.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: #2980b9;
                border: 1.5px solid #2980b9;
                padding: 5px 15px;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #e3f2fd; }
        """)
        btn_cancelar.clicked.connect(self.reject)
        
        btn_guardar = QPushButton("Guardar")
        btn_guardar.setFixedHeight(35)
        btn_guardar.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                padding: 5px 15px;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #1e8449; }
        """)
        btn_guardar.clicked.connect(self.guardar)
        
        h_layout.addWidget(btn_cancelar)
        h_layout.addWidget(btn_guardar)
        layout.addWidget(frame_botones)
    
    def _estilo_input(self):
        return """
            QLineEdit, QComboBox {
                border: 2px solid #2980b9;
                border-radius: 10px;
                padding: 5px 8px;
                background-color: white;
            }
        """
    
    def _cargar_areas(self):
        """Carga las áreas de aprendizaje activas en el combobox."""
        self.cbx_area.clear()
        self.cbx_area.addItem("-- Seleccione un área --", None)
        
        areas = AreaAprendizajeModel.listar_todas(solo_activas=True)
        for area in areas:
            self.cbx_area.addItem(area["nombre"], area["id"])
    
    def toggle_todos_grados(self, estado):
        """Marca o desmarca todos los checkboxes."""
        for chk in self.checkboxes_grados.values():
            chk.setChecked(bool(estado))
    
    def cargar_datos_materia(self):
        """Carga los datos de la materia a editar."""
        self.txt_nombre.setText(self.materia["nombre"])
        self.txt_abreviatura.setText(self.materia.get("abreviatura") or "")
        
        # Marcar grados existentes (solo Primaria)
        for grado_info in self.materia.get("grados", []):
            if grado_info["nivel"] == "Primaria":  # Ignorar grados de Inicial si existen
                key = (grado_info["nivel"], grado_info["grado"])
                if key in self.checkboxes_grados:
                    self.checkboxes_grados[key].setChecked(True)
        
        # Seleccionar área de aprendizaje
        area_id = self.materia.get("area_aprendizaje_id")
        if area_id:
            idx = self.cbx_area.findData(area_id)
            if idx >= 0:
                self.cbx_area.setCurrentIndex(idx)
    
    def obtener_grados_seleccionados(self):
        """Retorna lista de grados seleccionados."""
        grados = []
        for (nivel, grado), chk in self.checkboxes_grados.items():
            if chk.isChecked():
                grados.append({"nivel": nivel, "grado": grado})
        return grados
    
    def guardar(self):
        """Guarda la materia."""
        nombre = self.txt_nombre.text().strip()
        if not nombre:
            crear_msgbox(
                self, "Error",
                "El nombre de la materia es requerido.",
                QMessageBox.Warning
            ).exec()
            return
        
        # Validar área de aprendizaje
        area_id = self.cbx_area.currentData()
        if not area_id:
            crear_msgbox(
                self, "Error",
                "Debe seleccionar un Área de Aprendizaje.",
                QMessageBox.Warning
            ).exec()
            return
        
        abreviatura = self.txt_abreviatura.text().strip() or None
        tipo_evaluacion = "literal"  # Siempre literal para Primaria (A-E)
        grados = self.obtener_grados_seleccionados()
        
        if self.materia:
            # Actualizar
            ok, msg = MateriasModel.actualizar(
                self.materia["id"],
                nombre=nombre,
                abreviatura=abreviatura,
                tipo_evaluacion=tipo_evaluacion,
                grados=grados,
                area_aprendizaje_id=area_id,
                usuario_actual=self.usuario_actual
            )
        else:
            # Crear
            ok, msg = MateriasModel.crear(
                nombre=nombre,
                abreviatura=abreviatura,
                tipo_evaluacion=tipo_evaluacion,
                grados=grados,
                area_aprendizaje_id=area_id,
                usuario_actual=self.usuario_actual
            )
        
        if ok:
            crear_msgbox(self, "Éxito", msg, QMessageBox.Information).exec()
            self.accept()
        else:
            crear_msgbox(self, "Error", msg, QMessageBox.Warning).exec()


class DialogoGestionAreas(QDialog):
    """Diálogo para gestionar Áreas de Aprendizaje."""
    
    def __init__(self, usuario_actual, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        
        self.setWindowTitle("Gestión de Áreas de Aprendizaje")
        self.setFixedSize(600, 500)
        self.setStyleSheet("background-color: #f5f6fa;")
        
        self.setup_ui()
        self.cargar_areas()
    
    def setup_ui(self):
        """Configura la interfaz del diálogo."""
        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(15, 10, 15, 10)
        
        # Título
        titulo = QLabel("Áreas de Aprendizaje")
        titulo.setFont(QFont("Segoe UI", 14, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(titulo)
        
        # Frame de registro
        frame_form = QFrame()
        frame_form.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 1px solid #d5dbdb;
                border-radius: 10px;
            }
        """)
        form_layout = QVBoxLayout(frame_form)
        form_layout.setContentsMargins(12, 10, 12, 10)
        form_layout.setSpacing(6)
        
        lbl_nombre = QLabel("Nombre del área:")
        lbl_nombre.setStyleSheet("border: none;")
        form_layout.addWidget(lbl_nombre)
        
        h_form = QHBoxLayout()
        self.txt_nombre_area = QLineEdit()
        self.txt_nombre_area.setPlaceholderText("Ej: Lenguaje, Comunicación y Cultura")
        self.txt_nombre_area.setFixedHeight(30)
        self.txt_nombre_area.setStyleSheet("""
            QLineEdit {
                border: 2px solid #2980b9;
                border-radius: 10px;
                padding: 5px 8px;
                background-color: white;
            }
        """)
        h_form.addWidget(self.txt_nombre_area)
        
        self.txt_abrev_area = QLineEdit()
        self.txt_abrev_area.setPlaceholderText("Abrev. (opc.)")
        self.txt_abrev_area.setFixedHeight(30)
        self.txt_abrev_area.setMaxLength(15)
        self.txt_abrev_area.setFixedWidth(120)
        self.txt_abrev_area.setStyleSheet("""
            QLineEdit {
                border: 2px solid #2980b9;
                border-radius: 10px;
                padding: 5px 8px;
                background-color: white;
            }
        """)
        h_form.addWidget(self.txt_abrev_area)
        
        form_layout.addLayout(h_form)
        
        # Botones de acción
        h_botones = QHBoxLayout()
        
        self.btn_guardar_area = QPushButton("Agregar")
        self.btn_guardar_area.setFixedHeight(32)
        self.btn_guardar_area.setCursor(Qt.PointingHandCursor)
        self.btn_guardar_area.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                padding: 5px 15px;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #1e8449; }
        """)
        self.btn_guardar_area.clicked.connect(self.guardar_area)
        h_botones.addWidget(self.btn_guardar_area)
        
        self.btn_editar_area = QPushButton("Actualizar")
        self.btn_editar_area.setFixedHeight(32)
        self.btn_editar_area.setCursor(Qt.PointingHandCursor)
        self.btn_editar_area.setEnabled(False)
        self.btn_editar_area.setStyleSheet("""
            QPushButton {
                background-color: #2980b9;
                color: white;
                border: none;
                padding: 5px 15px;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #0D47A1; }
            QPushButton:disabled { background-color: #bdc3c7; }
        """)
        self.btn_editar_area.clicked.connect(self.actualizar_area)
        h_botones.addWidget(self.btn_editar_area)
        
        self.btn_estado_area = QPushButton("Desactivar")
        self.btn_estado_area.setFixedHeight(32)
        self.btn_estado_area.setCursor(Qt.PointingHandCursor)
        self.btn_estado_area.setEnabled(False)
        self.btn_estado_area.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 5px 15px;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #C0392B; }
            QPushButton:disabled { background-color: #bdc3c7; }
        """)
        self.btn_estado_area.clicked.connect(self.cambiar_estado_area)
        h_botones.addWidget(self.btn_estado_area)
        
        self.btn_cancelar_edicion = QPushButton("Cancelar")
        self.btn_cancelar_edicion.setFixedHeight(32)
        self.btn_cancelar_edicion.setCursor(Qt.PointingHandCursor)
        self.btn_cancelar_edicion.setVisible(False)
        self.btn_cancelar_edicion.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: #e74c3c;
                border: 1.5px solid #e74c3c;
                padding: 5px 15px;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #fce4e4; }
        """)
        self.btn_cancelar_edicion.clicked.connect(self.cancelar_edicion)
        h_botones.addWidget(self.btn_cancelar_edicion)
        
        form_layout.addLayout(h_botones)
        layout.addWidget(frame_form)
        
        # Checkbox mostrar inactivas
        self.chk_mostrar_inactivas = QCheckBox("Mostrar inactivas")
        self.chk_mostrar_inactivas.setFont(QFont("Segoe UI", 10))
        self.chk_mostrar_inactivas.stateChanged.connect(self.cargar_areas)
        layout.addWidget(self.chk_mostrar_inactivas)
        
        # Tabla de áreas
        self.tabla_areas = QTableWidget()
        self.tabla_areas.setColumnCount(4)
        self.tabla_areas.setHorizontalHeaderLabels(["ID", "Nombre", "Abreviatura", "Estado"])
        self.tabla_areas.setColumnHidden(0, True)
        self.tabla_areas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_areas.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_areas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_areas.setAlternatingRowColors(True)
        self.tabla_areas.horizontalHeader().setStretchLastSection(True)
        self.tabla_areas.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tabla_areas.setColumnWidth(2, 100)
        self.tabla_areas.setColumnWidth(3, 80)
        self.tabla_areas.setStyleSheet("""
            QTableWidget {
                background-color: #F7F9FC;
                gridline-color: #E3E8EF;
                color: #0B1321;
                alternate-background-color: #E3F2FD;
                selection-background-color: #2980b9;
                selection-color: #FFFFFF;
                border: 1px solid #CBD5E1;
                border-radius: 8px;
            }
            QHeaderView::section {
                background-color: #ECF0F1;
                color: #2C3E50;
                font-weight: bold;
                border: none;
                padding: 6px;
            }
        """)
        self.tabla_areas.selectionModel().selectionChanged.connect(self.on_seleccion_area)
        layout.addWidget(self.tabla_areas)
        
        # Botón cerrar
        btn_cerrar = QPushButton("Cerrar")
        btn_cerrar.setFixedHeight(35)
        btn_cerrar.setCursor(Qt.PointingHandCursor)
        btn_cerrar.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: #2980b9;
                border: 1.5px solid #2980b9;
                padding: 5px 15px;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #e3f2fd; }
        """)
        btn_cerrar.clicked.connect(self.accept)
        layout.addWidget(btn_cerrar, alignment=Qt.AlignRight)
        
        # Estado de edición
        self.area_editando_id = None
    
    def cargar_areas(self):
        """Carga las áreas en la tabla."""
        solo_activas = not self.chk_mostrar_inactivas.isChecked()
        areas = AreaAprendizajeModel.listar_todas(solo_activas=solo_activas)
        
        self.tabla_areas.setRowCount(0)
        for area in areas:
            row = self.tabla_areas.rowCount()
            self.tabla_areas.insertRow(row)
            
            item_id = QTableWidgetItem(str(area["id"]))
            item_nombre = QTableWidgetItem(area["nombre"])
            item_abrev = QTableWidgetItem(area.get("abreviatura") or "-")
            item_estado = QTableWidgetItem("Activo" if area["estado"] else "Inactivo")
            
            item_id.setTextAlignment(Qt.AlignCenter)
            item_abrev.setTextAlignment(Qt.AlignCenter)
            item_estado.setTextAlignment(Qt.AlignCenter)
            
            # Colorear inactivas
            if not area["estado"]:
                from PySide6.QtGui import QColor
                color_inactivo = QColor(220, 220, 220)
                for item in [item_id, item_nombre, item_abrev, item_estado]:
                    item.setBackground(color_inactivo)
            
            self.tabla_areas.setItem(row, 0, item_id)
            self.tabla_areas.setItem(row, 1, item_nombre)
            self.tabla_areas.setItem(row, 2, item_abrev)
            self.tabla_areas.setItem(row, 3, item_estado)
    
    def on_seleccion_area(self):
        """Maneja la selección de un área en la tabla."""
        fila = self.tabla_areas.currentRow()
        if fila < 0:
            self.btn_editar_area.setEnabled(False)
            self.btn_estado_area.setEnabled(False)
            return
        
        self.btn_editar_area.setEnabled(True)
        self.btn_estado_area.setEnabled(True)
        
        # Actualizar texto del botón de estado
        estado_texto = self.tabla_areas.item(fila, 3).text()
        if estado_texto == "Activo":
            self.btn_estado_area.setText("Desactivar")
            self.btn_estado_area.setStyleSheet("""
                QPushButton {
                    background-color: #e74c3c;
                    color: white;
                    border: none;
                    padding: 5px 15px;
                    border-radius: 10px;
                    font-weight: bold;
                }
                QPushButton:hover { background-color: #C0392B; }
            """)
        else:
            self.btn_estado_area.setText("Activar")
            self.btn_estado_area.setStyleSheet("""
                QPushButton {
                    background-color: #27ae60;
                    color: white;
                    border: none;
                    padding: 5px 15px;
                    border-radius: 10px;
                    font-weight: bold;
                }
                QPushButton:hover { background-color: #1e8449; }
            """)
    
    def guardar_area(self):
        """Crea una nueva área de aprendizaje."""
        nombre = self.txt_nombre_area.text().strip()
        if not nombre:
            crear_msgbox(self, "Error", "El nombre del área es requerido.", QMessageBox.Warning).exec()
            return
        
        abreviatura = self.txt_abrev_area.text().strip() or None
        
        ok, msg = AreaAprendizajeModel.crear(
            nombre=nombre,
            abreviatura=abreviatura,
            usuario_actual=self.usuario_actual
        )
        
        if ok:
            crear_msgbox(self, "Éxito", msg, QMessageBox.Information).exec()
            self.txt_nombre_area.clear()
            self.txt_abrev_area.clear()
            self.cargar_areas()
        else:
            crear_msgbox(self, "Error", msg, QMessageBox.Warning).exec()
    
    def actualizar_area(self):
        """Inicia o ejecuta la edición de un área."""
        fila = self.tabla_areas.currentRow()
        if fila < 0:
            return
        
        area_id = int(self.tabla_areas.item(fila, 0).text())
        
        if self.area_editando_id is None:
            # Iniciar edición: cargar datos en el formulario
            self.area_editando_id = area_id
            self.txt_nombre_area.setText(self.tabla_areas.item(fila, 1).text())
            abrev = self.tabla_areas.item(fila, 2).text()
            self.txt_abrev_area.setText(abrev if abrev != "-" else "")
            
            self.btn_guardar_area.setEnabled(False)
            self.btn_editar_area.setText("Guardar cambios")
            self.btn_cancelar_edicion.setVisible(True)
        else:
            # Guardar cambios
            nombre = self.txt_nombre_area.text().strip()
            if not nombre:
                crear_msgbox(self, "Error", "El nombre es requerido.", QMessageBox.Warning).exec()
                return
            
            abreviatura = self.txt_abrev_area.text().strip() or None
            
            ok, msg = AreaAprendizajeModel.actualizar(
                area_id=self.area_editando_id,
                nombre=nombre,
                abreviatura=abreviatura,
                usuario_actual=self.usuario_actual
            )
            
            if ok:
                crear_msgbox(self, "Éxito", msg, QMessageBox.Information).exec()
                self.cancelar_edicion()
                self.cargar_areas()
            else:
                crear_msgbox(self, "Error", msg, QMessageBox.Warning).exec()
    
    def cancelar_edicion(self):
        """Cancela la edición y restaura el formulario."""
        self.area_editando_id = None
        self.txt_nombre_area.clear()
        self.txt_abrev_area.clear()
        self.btn_guardar_area.setEnabled(True)
        self.btn_editar_area.setText("Actualizar")
        self.btn_cancelar_edicion.setVisible(False)
    
    def cambiar_estado_area(self):
        """Activa o desactiva el área seleccionada."""
        fila = self.tabla_areas.currentRow()
        if fila < 0:
            return
        
        area_id = int(self.tabla_areas.item(fila, 0).text())
        nombre = self.tabla_areas.item(fila, 1).text()
        estado_actual = self.tabla_areas.item(fila, 3).text() == "Activo"
        accion = "desactivar" if estado_actual else "activar"
        
        msg = crear_msgbox(
            self, "Confirmar",
            f"¿Está seguro de {accion} el área '{nombre}'?",
            QMessageBox.Question,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if msg.exec() == QMessageBox.StandardButton.Yes:
            ok, msg = AreaAprendizajeModel.cambiar_estado(
                area_id=area_id,
                activo=not estado_actual,
                usuario_actual=self.usuario_actual
            )
            
            if ok:
                crear_msgbox(self, "Éxito", msg, QMessageBox.Information).exec()
                self.cargar_areas()
            else:
                crear_msgbox(self, "Error", msg, QMessageBox.Warning).exec()
