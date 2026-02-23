from PySide6.QtWidgets import QWidget, QDialog, QToolButton, QMenu, QMessageBox, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel

from ui_compiled.Egresados_ui import Ui_Egresados
from models.estu_model import EstudianteModel
from models.institucion_model import InstitucionModel
from utils.exportar import (
    generar_buena_conducta, 
    exportar_tabla_excel, 
    generar_certificado_promocion_sexto
)
from utils.sombras import crear_sombra_flotante
from utils.logo_manager import aplicar_logo_a_label
from utils.dialogs import crear_msgbox
from utils.archivos import abrir_archivo
from views.detalles_estudiante import DetallesEstudiante
from views.delegates import EstudianteDelegate
from utils.proxies import ProxyConEstado

from datetime import datetime


class Egresados(QWidget, Ui_Egresados):
    """Página de gestión de estudiantes egresados."""
    
    def __init__(self, usuario_actual, año_escolar, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.año_escolar = año_escolar
        self.setupUi(self)
        
        # Mostrar usuario conectado
        self.lblConectado_como.setText(f"Conectado como: {self.usuario_actual['username']}")
        
        # Configurar filtros
        self.lneBuscar_egresados.textChanged.connect(self.filtrar_tabla_egresados)
        self.cbxFiltro_egresados.currentIndexChanged.connect(
            lambda _: self.filtrar_tabla_egresados(self.lneBuscar_egresados.text())
        )
       
        # Configurar proxy (sin columna de estado porque todos son egresados)
        self.proxy_egresados = ProxyConEstado(columna_estado=-1, parent=self)
        self.tableW_egresados.setModel(self.proxy_egresados)

        # Cargar datos iniciales
        self.database_egresados()

        self.aplicar_sombras()
        
        # Conectar botones
        self.btnActualizar_db_egresados.clicked.connect(self.database_egresados)
        self.btnDetalles_egresados.clicked.connect(self.abrir_detalles_estudiante)
        
        # Configurar menú de exportación
        self.btnExportar_egresados.setPopupMode(QToolButton.InstantPopup)
        menu_exportar = QMenu(self.btnExportar_egresados)
        menu_exportar.addAction("Constancia de buena conducta", self.exportar_buena_conducta)
        menu_exportar.addAction("Certificado promoción 6to a Secundaria", self.exportar_certificado_promocion_sexto)
        menu_exportar.addAction("Exportar tabla filtrada a Excel", self.exportar_excel_egresados)
        self.btnExportar_egresados.setMenu(menu_exportar)
        
        # Aplicar logo institucional dinámico
        aplicar_logo_a_label(self.lblLogo_egresados)
    
    def aplicar_sombras(self):
        # Aplicar efectos visuales
        crear_sombra_flotante(self.btnDetalles_egresados)
        crear_sombra_flotante(self.btnExportar_egresados)
        crear_sombra_flotante(self.btnActualizar_db_egresados)
        crear_sombra_flotante(self.frameFiltro_egresados, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lneBuscar_egresados, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.frameTabla_egresados, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lblTitulo_egresados, blur_radius=5, y_offset=1)
        crear_sombra_flotante(self.lblLogo_egresados, blur_radius=5, y_offset=1)

    def database_egresados(self):
        """Carga la tabla de egresados."""
        try:
            datos = EstudianteModel.listar_egresados()

            if not datos:
                # Crear modelo vacío
                model_vacio = QStandardItemModel(0, 12)
                model_vacio.setHorizontalHeaderLabels([
                    "ID", "Cédula", "Nombres", "Apellidos", "Fecha Nac.",
                    "Edad", "Ciudad", "Género", "Dirección",
                    "Último Grado", "Última Sección", "Fecha Egreso"
                ])
                self.proxy_egresados.setSourceModel(model_vacio)
                self.lblTotalRegistros_egresados.setText("0")
                return

            columnas = [
                "ID", "Cédula", "Nombres", "Apellidos", "Fecha Nac.",
                "Edad", "Ciudad", "Género", "Dirección",
                "Último Grado", "Última Sección", "Fecha Egreso"
            ]

            model_egresados = QStandardItemModel(len(datos), len(columnas))
            model_egresados.setHorizontalHeaderLabels(columnas)

            for fila, registro in enumerate(datos):
                # Formatear fecha de nacimiento
                fecha_nac = ""
                if registro.get("fecha_nac"):
                    if hasattr(registro["fecha_nac"], 'strftime'):
                        fecha_nac = registro["fecha_nac"].strftime("%d-%m-%Y")
                    else:
                        fecha_nac = str(registro["fecha_nac"])

                # Crear items
                items = [
                    QStandardItem(str(registro.get("id", ""))),
                    QStandardItem(registro.get("cedula", "")),
                    QStandardItem(registro.get("nombres", "")),
                    QStandardItem(registro.get("apellidos", "")),
                    QStandardItem(fecha_nac),
                    QStandardItem(str(registro.get("edad", ""))),
                    QStandardItem(registro.get("ciudad", "") or ""),
                    QStandardItem(registro.get("genero", "")),
                    QStandardItem(registro.get("direccion", "") or ""),
                    QStandardItem(registro.get("ultimo_grado", "") or "N/A"),
                    QStandardItem(registro.get("ultima_seccion", "") or "N/A"),
                    QStandardItem(registro.get("fecha_egreso", "") or "N/A")
                ]

                for col, item in enumerate(items):
                    item.setEditable(False)
                    model_egresados.setItem(fila, col, item)

            # Configurar modelo y vista
            self.proxy_egresados.setSourceModel(model_egresados)

            delegate = EstudianteDelegate(self.tableW_egresados)
            self.tableW_egresados.setItemDelegate(delegate)

            self.tableW_egresados.setSortingEnabled(True)
            self.tableW_egresados.setAlternatingRowColors(True)
            self.tableW_egresados.setColumnHidden(0, True)  # Ocultar ID

            # Numeración de filas
            row_count = self.proxy_egresados.rowCount()
            for fila in range(row_count):
                self.proxy_egresados.setHeaderData(
                    fila, Qt.Vertical, str(fila + 1), Qt.DisplayRole
                )

            # Actualizar contador
            self.lblTotalRegistros_egresados.setText(str(len(datos)))

        except Exception as err:
            crear_msgbox(
                self,
                "Error",
                f"No se pudo cargar la tabla de egresados: {err}",
                QMessageBox.Critical
            ).exec()

    def abrir_detalles_estudiante(self):
        """Abre detalles del estudiante seleccionado."""
        index = self.tableW_egresados.currentIndex()
        
        if not index.isValid():
            crear_msgbox(
                self,
                "Selección requerida",
                "Debe seleccionar un estudiante de la tabla.",
                QMessageBox.Warning
            ).exec()
            return

        try:
            # Mapear al modelo fuente
            index_source = self.tableW_egresados.model().mapToSource(index)
            fila = index_source.row()
            model = index_source.model()
            
            # Obtener ID del estudiante
            id_estudiante = int(model.item(fila, 0).text())

            # Abrir ventana de detalles en modo egresado
            ventana = DetallesEstudiante(
                id_estudiante, 
                self.usuario_actual, 
                self.año_escolar,
                es_egresado=True,  # Modo solo lectura para egresados
                parent=self
            )
            ventana.datos_actualizados.connect(self.database_egresados)
            ventana.exec()

        except Exception as e:
            crear_msgbox(
                self,
                "Error",
                f"No se pudo abrir los detalles: {e}",
                QMessageBox.Critical
            ).exec()

    def obtener_estudiante_seleccionado(self) -> dict:
        """Obtiene los datos del estudiante seleccionado en la tabla."""
        index = self.tableW_egresados.currentIndex()
        if not index.isValid():
            return None

        try:
            proxy = self.tableW_egresados.model()
            source_index = proxy.mapToSource(index)
            fila = source_index.row()
            model = proxy.sourceModel()

            # Obtener ID y buscar en BD
            id_estudiante = int(model.item(fila, 0).text())
            
            # Obtener datos completos desde el modelo
            datos_db = EstudianteModel.obtener_por_id(id_estudiante)
            
            if not datos_db:
                return None
            
            return datos_db

        except Exception as e:
            print(f"Error obteniendo estudiante seleccionado: {e}")
            return None
    
    def filtrar_tabla_egresados(self, texto):
        """Filtra la tabla según el texto ingresado y la columna seleccionada"""
        if not hasattr(self, "proxy_egresados"):
            return

        # Mapeo de índices del combo a columnas reales
        mapa_columnas = {
            0: -1,   # Todos
            1: 1,    # Cédula
            2: 2,    # Nombres
            3: 3,    # Apellidos
            4: 4,    # Fecha Nac.
            5: 5,    # Edad
            6: 6,    # Ciudad
            7: 7,    # Género
            8: 8,    # Dirección
            9: 9,    # Último Grado
            10: 10,  # Última Sección
            11: 11   # Fecha Egreso
        }

        idx_combo = self.cbxFiltro_egresados.currentIndex()
        columna_real = mapa_columnas.get(idx_combo, -1)

        self.proxy_egresados.setFilterKeyColumn(columna_real)
        self.proxy_egresados.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.proxy_egresados.setFilterRegularExpression(texto)
    
    def obtener_datos_tableview(self, view):
        """Extrae datos visibles de un QTableView para exportación"""
        model = view.model()
        
        if not model:
            return [], []
        
        # Encabezados
        encabezados = []
        for c in range(model.columnCount()):
            header = model.headerData(c, Qt.Horizontal)
            encabezados.append(str(header) if header else "")
        
        # Filas visibles
        filas = []
        for r in range(model.rowCount()):
            fila = []
            for c in range(model.columnCount()):
                index = model.index(r, c)
                val = model.data(index, Qt.ItemDataRole.DisplayRole)
                fila.append("" if val is None else str(val))
            filas.append(fila)
        
        return encabezados, filas

    def exportar_excel_egresados(self):
        """Exporta la tabla filtrada a Excel"""
        try:
            encabezados, filas = self.obtener_datos_tableview(self.tableW_egresados)
            
            if not filas:
                crear_msgbox(
                    self,
                    "Tabla vacía",
                    "No hay datos para exportar.",
                    QMessageBox.Warning
                ).exec()
                return

            # Diálogo para guardar archivo
            ruta, _ = QFileDialog.getSaveFileName(
                self,
                "Guardar reporte de egresados",
                f"egresados_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                "Archivos Excel (*.xlsx)"
            )
            
            if not ruta:
                return  # Usuario canceló
            
            if not ruta.endswith(".xlsx"):
                ruta += ".xlsx"

            # Exportar
            archivo = exportar_tabla_excel(ruta, encabezados, filas)

            crear_msgbox(
                self,
                "Éxito",
                f"Archivo exportado correctamente:\n{archivo}",
                QMessageBox.Information
            ).exec()
            
            # Abrir archivo
            abrir_archivo(archivo)

        except Exception as e:
            crear_msgbox(
                self,
                "Error",
                f"No se pudo exportar: {e}",
                QMessageBox.Critical
            ).exec()

    def exportar_buena_conducta(self):
        """Genera constancia de buena conducta para el estudiante seleccionado"""
        estudiante = self.obtener_estudiante_seleccionado()
        
        if not estudiante:
            crear_msgbox(
                self,
                "Selección requerida",
                "Debe seleccionar un estudiante de la tabla.",
                QMessageBox.Warning
            ).exec()
            return

        try:
            # Verificar que sea egresado
            if estudiante.get("estatus_academico") != "Egresado":
                crear_msgbox(
                    self,
                    "Estudiante no válido",
                    "El estudiante seleccionado no está marcado como egresado.",
                    QMessageBox.Warning
                ).exec()
                return

            # Obtener datos de la institución
            institucion = InstitucionModel.obtener_por_id(1)
            
            if not institucion:
                crear_msgbox(
                    self,
                    "Error",
                    "No se encontraron datos de la institución.",
                    QMessageBox.Critical
                ).exec()
                return

            # Generar constancia
            archivo = generar_buena_conducta(estudiante, institucion)
            
            crear_msgbox(
                self,
                "Éxito",
                f"Constancia generada correctamente:\n{archivo}",
                QMessageBox.Information
            ).exec()
            
            # Abrir archivo
            abrir_archivo(archivo)

        except Exception as e:
            crear_msgbox(
                self,
                "Error",
                f"No se pudo generar la constancia: {e}",
                QMessageBox.Critical
            ).exec()

    def exportar_certificado_promocion_sexto(self):
        """
        Genera certificado de promoción de 6to grado a 1er año de secundaria.
        Solo válido para estudiantes egresados que cursaron 6to grado EN ESTA INSTITUCIÓN.
        """
        estudiante = self.obtener_estudiante_seleccionado()
        
        if not estudiante:
            crear_msgbox(
                self,
                "Selección requerida",
                "Debe seleccionar un estudiante de la tabla.",
                QMessageBox.Warning
            ).exec()
            return

        try:
            # Verificar que sea egresado
            if estudiante.get("estatus_academico") != "Egresado":
                crear_msgbox(
                    self,
                    "No elegible",
                    "El estudiante seleccionado no está marcado como egresado.",
                    QMessageBox.Warning
                ).exec()
                return

            # Obtener ID del estudiante
            id_estudiante = estudiante['id']
            
            # Obtener historial académico
            historial = EstudianteModel.obtener_historial_estudiante(id_estudiante)
            
            if not historial:
                crear_msgbox(
                    self,
                    "Sin historial",
                    "No se encontró historial académico para este estudiante.",
                    QMessageBox.Warning
                ).exec()
                return
            
            # Buscar el registro de 6to grado (el más reciente con 6to)
            curso_sexto = None
            for registro in historial:
                grado = registro['grado'].lower().strip()
                nivel = registro['nivel'].lower().strip()
                
                # Verificar que sea 6to grado de primaria
                if 'primaria' in nivel and '6' in grado:
                    curso_sexto = registro
                    break
            
            if not curso_sexto:
                crear_msgbox(
                    self,
                    "No elegible",
                    "Este estudiante no cursó 6to grado en esta institución.\n\n"
                    "Este certificado solo puede generarse para estudiantes que "
                    "completaron 6to grado de primaria en esta institución.",
                    QMessageBox.Warning
                ).exec()
                return
            
            # Preparar datos adicionales del estudiante
            estudiante['ultima_seccion'] = curso_sexto['letra']
            
            # Obtener datos de la institución
            institucion = InstitucionModel.obtener_por_id(1)
            
            if not institucion:
                crear_msgbox(
                    self,
                    "Error",
                    "No se encontraron datos de la institución.",
                    QMessageBox.Critical
                ).exec()
                return
            
            # Generar certificado
            archivo = generar_certificado_promocion_sexto(
                estudiante,
                institucion,
                curso_sexto['año_escolar']
            )
            
            crear_msgbox(
                self,
                "Éxito",
                f"Certificado generado exitosamente:\n{archivo}",
                QMessageBox.Information
            ).exec()
            
            # Abrir archivo
            abrir_archivo(archivo)
            
        except Exception as e:
            crear_msgbox(
                self,
                "Error",
                f"No se pudo generar el certificado: {e}",
                QMessageBox.Critical
            ).exec()
