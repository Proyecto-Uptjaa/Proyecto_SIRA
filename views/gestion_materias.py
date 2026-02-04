from PySide6.QtWidgets import (
    QWidget, QDialog, QMessageBox, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton,
    QFrame, QScrollArea, QGridLayout
)
from PySide6.QtCore import Qt, QTimer, QSize
from PySide6.QtGui import QStandardItemModel, QStandardItem, QFont, QIcon

from ui_compiled.gestion_materias_ui import Ui_gestion_materias
from models.materias_model import MateriasModel
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
        self.proxy_materias = ProxyConEstado(columna_estado=4, parent=self)
        self.tableW_materias.setModel(self.proxy_materias)
        
        # Configurar delegate para colorear inactivas
        self.delegate_materias = BaseEstadoDelegate(parent=self, estado_columna=4)
        self.tableW_materias.setItemDelegate(self.delegate_materias)
        
        # Conectar controles
        self.chkMostrar_inactivas_materias.stateChanged.connect(
            lambda estado: self.proxy_materias.setMostrarInactivos(bool(estado))
        )
        self.btnNueva_materia.clicked.connect(self.nueva_materia)
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
    
    def _aplicar_sombras(self):
        crear_sombra_flotante(self.btnNueva_materia)
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
            "ID", "Nombre", "Abreviatura", "Tipo", "Estado", "Grados"
        ])
        
        for materia in materias:
            estado_texto = "Activo" if materia["estado"] else "Inactivo"
            fila = [
                QStandardItem(str(materia["id"])),
                QStandardItem(materia["nombre"]),
                QStandardItem(materia.get("abreviatura") or "-"),
                QStandardItem("Literal (A-E)"),  # Todas son literales ahora
                QStandardItem(estado_texto),
                QStandardItem(materia.get("grados_resumen", "Sin asignar"))
            ]
            
            # Centrar algunas columnas
            fila[0].setTextAlignment(Qt.AlignCenter)
            fila[2].setTextAlignment(Qt.AlignCenter)
            fila[3].setTextAlignment(Qt.AlignCenter)
            fila[4].setTextAlignment(Qt.AlignCenter)
            
            # Guardar datos extras
            fila[0].setData(materia, Qt.UserRole)
            
            modelo.appendRow(fila)
        
        self.proxy_materias.setSourceModel(modelo)
        
        # Ocultar columna ID, Tipo y estado interno
        self.tableW_materias.setColumnHidden(0, True)
        self.tableW_materias.setColumnHidden(3, True)  # Ocultar tipo (todas son literales)
        
        # Ajustar anchos
        self.tableW_materias.setColumnWidth(1, 200)   # Nombre
        self.tableW_materias.setColumnWidth(2, 80)    # Abreviatura
        self.tableW_materias.setColumnWidth(4, 80)    # Estado
        self.tableW_materias.setColumnWidth(5, 300)   # Grados
    
    def filtrar_tabla(self, texto):
        """Filtra la tabla por texto de búsqueda."""
        columna = self.cbxFiltro_materias.currentIndex()
        # Mapear índice del combo a columna real
        # 0=Todos, 1=Nombre, 2=Abreviatura, 3=Estado, 4=Grados
        columnas_filtro = {
            0: -1,  # Todas
            1: 1,   # Nombre
            2: 2,   # Abreviatura
            3: 4,   # Estado
            4: 5    # Grados
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
        
        resp = QMessageBox.question(
            self, "Confirmar",
            f"¿Está seguro de {accion} la materia '{materia['nombre']}'?\n\n"
            f"La materia se {accion_texto} inmediatamente.",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if resp == QMessageBox.Yes:
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
        self.setFixedSize(450, 520)
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
                usuario_actual=self.usuario_actual
            )
        else:
            # Crear
            ok, msg = MateriasModel.crear(
                nombre=nombre,
                abreviatura=abreviatura,
                tipo_evaluacion=tipo_evaluacion,
                grados=grados,
                usuario_actual=self.usuario_actual
            )
        
        if ok:
            crear_msgbox(self, "Éxito", msg, QMessageBox.Information).exec()
            self.accept()
        else:
            crear_msgbox(self, "Error", msg, QMessageBox.Warning).exec()
