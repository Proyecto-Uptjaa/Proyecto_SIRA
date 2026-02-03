from PySide6.QtWidgets import (
    QWidget, QMessageBox, QHBoxLayout, QSpacerItem, QSizePolicy,
    QHeaderView, QStyledItemDelegate, QLineEdit
)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QStandardItemModel, QStandardItem, QColor

from ui_compiled.gestion_notas_ui import Ui_gestion_notas
from models.secciones_model import SeccionesModel
from models.materias_model import MateriasModel
from models.notas_model import NotasModel
from models.anio_model import AnioEscolarModel
from utils.tarjeta_seccion_mini import TarjetaSeccionMini
from utils.sombras import crear_sombra_flotante
from utils.dialogs import crear_msgbox


class NotaDelegate(QStyledItemDelegate):
    """Delegate para edición de notas literales (A-E)."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def createEditor(self, parent, option, index):
        """Crea el editor para notas literales A-E."""
        editor = QLineEdit(parent)
        editor.setAlignment(Qt.AlignCenter)
        editor.setPlaceholderText("A-E")
        editor.setMaxLength(1)
        return editor
    
    def setEditorData(self, editor, index):
        """Carga el valor actual en el editor."""
        valor = index.data(Qt.DisplayRole)
        if valor and valor != "-":
            editor.setText(str(valor))
    
    def setModelData(self, editor, model, index):
        """Guarda el valor del editor en el modelo."""
        texto = editor.text().strip().upper()
        
        if not texto:
            model.setData(index, None, Qt.DisplayRole)
            model.setData(index, None, Qt.UserRole)
            model.setData(index, QColor("white"), Qt.BackgroundRole)
            return
        
        # Solo notas literales A-E
        validas = ["A", "B", "C", "D", "E"]
        if texto in validas:
            model.setData(index, texto, Qt.DisplayRole)
            model.setData(index, texto, Qt.UserRole)
            # Colorear según calificación
            if texto in ["A", "B"]:
                model.setData(index, QColor("#d5f5e3"), Qt.BackgroundRole)  # Verde claro
            elif texto == "C":
                model.setData(index, QColor("#fef9e7"), Qt.BackgroundRole)  # Amarillo claro
            else:  # D, E
                model.setData(index, QColor("#fadbd8"), Qt.BackgroundRole)  # Rojo claro


class GestionNotasPage(QWidget, Ui_gestion_notas):
    """Página de gestión de calificaciones."""
    
    def __init__(self, usuario_actual, año_escolar, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.año_escolar = año_escolar
        self.seccion_actual = None
        self.materia_actual = None
        self.tarjetas = []
        self.modelo_notas = None
        self.delegate_notas = None
        self.contenedor_tarjetas = None
        self.layout_tarjetas = None
        
        self.setupUi(self)
        
        # Configurar año escolar en título
        if año_escolar:
            self.lblAnio_escolar_notas.setText(f"Año escolar: {año_escolar.get('nombre', '')}")
        
        # Reconfigurar el scroll area para que funcione correctamente
        self._configurar_scroll_secciones()
        
        # Configurar controles
        self.setup_controles()
        
        # Cargar secciones
        self.cargar_secciones()
        
        # Aplicar sombras
        self._aplicar_sombras()
    
    def _configurar_scroll_secciones(self):
        """Reconfigura el scroll area para las tarjetas de secciones."""
        # Configurar políticas del scroll
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        
        # Crear un nuevo widget contenedor con layout horizontal
        nuevo_contenedor = QWidget()
        nuevo_contenedor.setStyleSheet("background-color: transparent;")
        
        layout_contenedor = QHBoxLayout(nuevo_contenedor)
        layout_contenedor.setSpacing(10)
        layout_contenedor.setContentsMargins(10, 5, 10, 5)
        layout_contenedor.setAlignment(Qt.AlignLeft)  # Alinear a la izquierda
        
        # Reemplazar el widget del scroll area
        self.scrollArea.setWidget(nuevo_contenedor)
        
        # Guardar referencia al contenedor de tarjetas
        self.contenedor_tarjetas = nuevo_contenedor
        self.layout_tarjetas = layout_contenedor
        
        # Configurar controles
        self.setup_controles()
        
        # Cargar secciones
        self.cargar_secciones()
        
        # Aplicar sombras
        self._aplicar_sombras()
    
    def _aplicar_sombras(self):
        """Aplica efectos visuales."""
        crear_sombra_flotante(self.btnGuardar_notas)
        crear_sombra_flotante(self.frameTabla_notas, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lblTitulo_notas, blur_radius=5, y_offset=1)
        crear_sombra_flotante(self.lblLogo_notas, blur_radius=5, y_offset=1)
    
    def refrescar(self):
        """Refresca la página completa (llamar después de cambios en secciones/materias)."""
        # Recargar secciones
        self.cargar_secciones()
        
        # Si hay una sección seleccionada, recargar sus materias
        if self.seccion_actual:
            self.cargar_materias_seccion(self.seccion_actual["id"])
    
    def setup_controles(self):
        """Configura los controles de la vista."""
        # Ocultar filtro de nivel (solo Primaria tiene notas)
        self.frameFiltro_nivel_notas.setVisible(False)
        
        # Conectar filtros
        self.lneBuscar_seccion_notas.textChanged.connect(self.filtrar_secciones)
        
        # Conectar selector de materia
        self.cbxMateria_notas.currentIndexChanged.connect(self.on_materia_changed)
        
        # Conectar botón guardar
        self.btnGuardar_notas.clicked.connect(self.guardar_notas)
        
        # Limpiar panel inferior inicialmente
        self.lblGrado_notas.setText("Seleccione una sección")
        self.lblDocente_notas.setText("")
        self.cbxMateria_notas.setEnabled(False)
        self.btnGuardar_notas.setEnabled(False)
        
        # Configurar tabla
        self.tableW_notas.setAlternatingRowColors(True)
        self.tableW_notas.horizontalHeader().setStretchLastSection(True)
    
    def cargar_secciones(self):
        """Carga las secciones del año actual."""
        if not self.año_escolar:
            return
        
        # Limpiar tarjetas anteriores
        self.limpiar_tarjetas()
        
        # Obtener secciones (solo Primaria - Inicial no tiene notas)
        todas = SeccionesModel.obtener_todas(
            self.año_escolar["id"], 
            solo_activas=True
        )
        secciones = [s for s in todas if s.get("nivel") == "Primaria"]
        
        # Usar el layout del contenedor configurado
        layout = self.layout_tarjetas
        
        # Crear tarjetas
        for seccion in secciones:
            tarjeta = TarjetaSeccionMini(seccion)
            tarjeta.clicked.connect(self.on_seccion_clicked)
            layout.addWidget(tarjeta)
            self.tarjetas.append(tarjeta)
        
        # Ajustar tamaño del contenedor según cantidad de tarjetas
        if secciones:
            ancho_total = len(secciones) * 110 + 20  # 100px tarjeta + 10px spacing + márgenes
            self.contenedor_tarjetas.setMinimumWidth(ancho_total)
    
    def limpiar_tarjetas(self):
        """Elimina todas las tarjetas del contenedor."""
        layout = self.layout_tarjetas
        if layout:
            while layout.count():
                item = layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
        self.tarjetas = []
    
    def filtrar_secciones(self):
        """Filtra las tarjetas según búsqueda (solo Primaria)."""
        texto_busqueda = self.lneBuscar_seccion_notas.text().lower().strip()
        
        tarjetas_visibles = 0
        for tarjeta in self.tarjetas:
            visible = True
            
            # Filtrar por texto (grado o docente)
            if texto_busqueda:
                grado_letra = tarjeta.get_grado_letra().lower()
                docente = tarjeta.seccion_data.get("docente_nombre", "").lower()
                if texto_busqueda not in grado_letra and texto_busqueda not in docente:
                    visible = False
            
            tarjeta.setVisible(visible)
            if visible:
                tarjetas_visibles += 1
        
        # Ajustar ancho del contenedor según tarjetas visibles
        ancho_necesario = tarjetas_visibles * 110 + 20
        self.contenedor_tarjetas.setMinimumWidth(ancho_necesario)
    
    def on_seccion_clicked(self, seccion_data):
        """Maneja el clic en una tarjeta de sección."""
        # Deseleccionar todas las tarjetas
        for tarjeta in self.tarjetas:
            tarjeta.seleccionada = False
        
        # Seleccionar la tarjeta clickeada
        for tarjeta in self.tarjetas:
            if tarjeta.seccion_id == seccion_data["id"]:
                tarjeta.seleccionada = True
                break
        
        # Guardar sección actual
        self.seccion_actual = seccion_data
        
        # Actualizar información
        grado_info = f"{seccion_data['grado']} \"{seccion_data['letra']}\" - {seccion_data['nivel']}"
        self.lblGrado_notas.setText(grado_info)
        
        docente = seccion_data.get("docente_nombre", "Sin asignar")
        self.lblDocente_notas.setText(f"Docente: {docente}")
        
        # Cargar materias de la sección
        self.cargar_materias_seccion(seccion_data["id"])
    
    def cargar_materias_seccion(self, seccion_id):
        """Carga las materias asignadas a la sección."""
        materias = MateriasModel.obtener_materias_seccion(seccion_id)
        
        self.cbxMateria_notas.clear()
        
        if not materias:
            self.cbxMateria_notas.addItem("Sin materias asignadas")
            self.cbxMateria_notas.setEnabled(False)
            self.btnGuardar_notas.setEnabled(False)
            self.limpiar_tabla_notas()
            return
        
        for materia in materias:
            self.cbxMateria_notas.addItem(
                materia["nombre"],
                userData=materia
            )
        
        self.cbxMateria_notas.setEnabled(True)
        self.btnGuardar_notas.setEnabled(True)
        
        # Cargar notas de la primera materia
        if materias:
            self.on_materia_changed(0)
    
    def on_materia_changed(self, index):
        """Maneja el cambio de materia seleccionada."""
        if index < 0 or not self.seccion_actual:
            return
        
        materia_data = self.cbxMateria_notas.currentData()
        if not materia_data:
            return
        
        self.materia_actual = materia_data
        self.cargar_tabla_notas()
    
    def cargar_tabla_notas(self):
        """Carga la tabla de notas para la sección y materia actual."""
        if not self.seccion_actual or not self.materia_actual:
            return
        
        # Obtener notas
        notas = NotasModel.obtener_notas_seccion_materia(
            self.seccion_actual["id"],
            self.materia_actual["id"]
        )
        
        # Crear modelo
        self.modelo_notas = QStandardItemModel()
        self.modelo_notas.setHorizontalHeaderLabels([
            "ID", "Sec-Mat ID", "Cédula", "Estudiante", 
            "Lapso 1", "Lapso 2", "Lapso 3", "Final"
        ])
        
        for nota in notas:
            # Solo procesar si coincide la materia
            if nota.get("materia_id") != self.materia_actual["id"]:
                continue
            
            fila = [
                QStandardItem(str(nota["estudiante_id"])),
                QStandardItem(str(nota["seccion_materia_id"])),
                QStandardItem(nota.get("cedula") or "-"),
                QStandardItem(nota.get("nombre_completo", "")),
            ]
            
            # Notas por lapso (siempre literal A-E)
            for lapso in [1, 2, 3]:
                valor = nota.get(f"lapso_{lapso}_lit")
                texto = valor if valor else "-"
                
                item = QStandardItem(texto)
                item.setTextAlignment(Qt.AlignCenter)
                item.setData(valor, Qt.UserRole)
                
                # Colorear según calificación
                if valor:
                    if valor in ["A", "B"]:
                        item.setBackground(QColor("#d5f5e3"))  # Verde claro
                    elif valor == "C":
                        item.setBackground(QColor("#fef9e7"))  # Amarillo claro
                    else:  # D, E
                        item.setBackground(QColor("#fadbd8"))  # Rojo claro
                
                fila.append(item)
            
            # Nota final (literal)
            final = nota.get("nota_final_literal")
            texto_final = final if final else "-"
            
            item_final = QStandardItem(texto_final)
            item_final.setTextAlignment(Qt.AlignCenter)
            item_final.setFlags(item_final.flags() & ~Qt.ItemIsEditable)  # No editable
            fila.append(item_final)
            
            # Centrar columnas fijas
            fila[0].setTextAlignment(Qt.AlignCenter)
            fila[1].setTextAlignment(Qt.AlignCenter)
            fila[2].setTextAlignment(Qt.AlignCenter)
            
            self.modelo_notas.appendRow(fila)
        
        # Configurar delegate para edición (notas literales)
        self.delegate_notas = NotaDelegate(self)
        for col in [4, 5, 6]:  # Columnas de lapsos
            self.tableW_notas.setItemDelegateForColumn(col, self.delegate_notas)
        
        self.tableW_notas.setModel(self.modelo_notas)
        
        # Ocultar columnas de IDs
        self.tableW_notas.setColumnHidden(0, True)
        self.tableW_notas.setColumnHidden(1, True)
        
        # Ajustar anchos
        self.tableW_notas.setColumnWidth(2, 100)
        self.tableW_notas.setColumnWidth(3, 250)
        self.tableW_notas.setColumnWidth(4, 80)
        self.tableW_notas.setColumnWidth(5, 80)
        self.tableW_notas.setColumnWidth(6, 80)
        self.tableW_notas.setColumnWidth(7, 80)
        
        # Stretch última columna
        header = self.tableW_notas.horizontalHeader()
        header.setStretchLastSection(True)
    
    def limpiar_tabla_notas(self):
        """Limpia la tabla de notas."""
        modelo_vacio = QStandardItemModel()
        modelo_vacio.setHorizontalHeaderLabels(["Sin datos"])
        self.tableW_notas.setModel(modelo_vacio)
    
    def guardar_notas(self):
        """Guarda todas las notas modificadas."""
        if not self.modelo_notas or not self.seccion_actual or not self.materia_actual:
            crear_msgbox(
                self, "Aviso",
                "Seleccione una sección y materia primero.",
                QMessageBox.Information
            ).exec()
            return
        
        # Determinar qué lapso(s) guardar según el filtro
        filtro_lapso = self.cbxFiltro_lapso_notas.currentText()
        lapsos_a_guardar = []
        
        if filtro_lapso == "Todos":
            lapsos_a_guardar = [1, 2, 3]
        elif filtro_lapso == "1ero":
            lapsos_a_guardar = [1]
        elif filtro_lapso == "2do":
            lapsos_a_guardar = [2]
        elif filtro_lapso == "3ro":
            lapsos_a_guardar = [3]
        else:
            lapsos_a_guardar = [1, 2, 3]
        
        notas_a_guardar = []
        
        # Recorrer el modelo
        for row in range(self.modelo_notas.rowCount()):
            estudiante_id = int(self.modelo_notas.item(row, 0).text())
            seccion_materia_id = int(self.modelo_notas.item(row, 1).text())
            
            for lapso in lapsos_a_guardar:
                col = 3 + lapso  # Columnas 4, 5, 6
                item = self.modelo_notas.item(row, col)
                valor = item.data(Qt.UserRole)
                
                if valor is not None:
                    nota_data = {
                        "estudiante_id": estudiante_id,
                        "seccion_materia_id": seccion_materia_id,
                        "lapso": lapso,
                        "nota_literal": valor  # Siempre literal
                    }
                    
                    notas_a_guardar.append(nota_data)
        
        if not notas_a_guardar:
            crear_msgbox(
                self, "Aviso",
                "No hay notas para guardar.",
                QMessageBox.Information
            ).exec()
            return
        
        # Guardar
        ok, msg, cantidad = NotasModel.registrar_notas_masivo(
            notas_a_guardar,
            self.usuario_actual
        )
        
        if ok:
            crear_msgbox(
                self, "Éxito",
                f"Se guardaron {cantidad} notas correctamente.",
                QMessageBox.Information
            ).exec()
            # Recargar tabla para ver cambios
            self.cargar_tabla_notas()
        else:
            crear_msgbox(self, "Error", msg, QMessageBox.Warning).exec()
    
    def closeEvent(self, event):
        """Limpieza al cerrar."""
        event.accept()
