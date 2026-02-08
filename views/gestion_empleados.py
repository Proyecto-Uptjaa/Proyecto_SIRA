import os
from datetime import datetime

from PySide6.QtWidgets import QToolButton, QMenu, QMessageBox, QFileDialog, QWidget
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QStandardItem, QStandardItemModel

from ui_compiled.gestion_empleados_ui import Ui_gestion_empleados
from models.emple_model import EmpleadoModel
from models.dashboard_model import DashboardModel
from models.institucion_model import InstitucionModel
from views.registro_empleado import RegistroEmpleado
from views.detalles_empleados import DetallesEmpleado
from views.delegates import EmpleadoDelegate
from utils.proxies import ProxyConEstado
from utils.sombras import crear_sombra_flotante
from utils.dialogs import crear_msgbox
from utils.archivos import abrir_archivo
from utils.exportar import (
    generar_constancia_trabajo,
    exportar_tabla_excel, 
    exportar_empleados_excel,
    generar_reporte_rac
)


class GestionEmpleadosPage(QWidget, Ui_gestion_empleados):
    """Página de gestión de empleados."""
    
    def __init__(self, usuario_actual, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.setupUi(self)
        
        # Mostrar usuario conectado
        self.lblConectado_como.setText(f"Conectado como: {self.usuario_actual['username']}")

        # Configurar proxy para filtrado
        self.proxy_empleados = ProxyConEstado(columna_estado=19, parent=self)
        self.tableW_emple.setModel(self.proxy_empleados)

        # Conectar controles
        self.chkMostrar_inactivos_emple.stateChanged.connect(
            lambda estado: self.proxy_empleados.setMostrarInactivos(bool(estado))
        )
        self.lneBuscar_emple.textChanged.connect(self.filtrar_tabla_empleados)
        self.cbxFiltro_emple.currentIndexChanged.connect(
            lambda _: self.filtrar_tabla_empleados(self.lneBuscar_emple.text())
        )
        
        # Conectar botones
        self.btnNuevo_emple.clicked.connect(self.registro_empleados)
        self.btnActualizar_db_emple.clicked.connect(self.database_empleados)
        self.btnDetalles_emple.clicked.connect(self.DetallesEmpleados)
        self.btnEliminar_emple.clicked.connect(self.eliminar_empleado)

        # Configurar menú de exportación
        self._configurar_menu_exportacion()
        
        # Cargar datos iniciales
        self.database_empleados()
        self.actualizar_conteo()

        # Configurar timer de actualización automática
        self.timer_actualizacion = QTimer(self)
        self.timer_actualizacion.timeout.connect(self.database_empleados)
        self.timer_actualizacion.timeout.connect(self.actualizar_conteo)
        self.timer_actualizacion.start(60000)  # Actualizar cada 60 segundos

        # Aplicar efectos visuales
        self._aplicar_sombras()
    
    def _aplicar_sombras(self):
        """Aplica sombras a elementos de la interfaz."""
        crear_sombra_flotante(self.btnNuevo_emple)
        crear_sombra_flotante(self.btnDetalles_emple)
        crear_sombra_flotante(self.btnExportar_emple)
        crear_sombra_flotante(self.btnEliminar_emple, opacity=120)
        crear_sombra_flotante(self.btnActualizar_db_emple)
        crear_sombra_flotante(self.frameFiltro_estu_4, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lneBuscar_emple, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.frameTabla_emple, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lblTitulo_emple, blur_radius=5, y_offset=1)
        crear_sombra_flotante(self.lblLogo_emple, blur_radius=5, y_offset=1)
    
    def _configurar_menu_exportacion(self):
        """Configura el menú de exportación."""
        self.btnExportar_emple.setPopupMode(QToolButton.InstantPopup)
        menu_exportar_emple = QMenu(self.btnExportar_emple)
        menu_exportar_emple.addAction("Constancia de trabajo PDF", self.exportar_constancia_empleado)
        menu_exportar_emple.addAction("Exportar tabla filtrada a Excel", self.exportar_excel_empleados)
        menu_exportar_emple.addAction("Exportar BD completa a Excel", self.exportar_excel_empleados_bd)
        menu_exportar_emple.addSeparator()
        menu_exportar_emple.addAction("Reporte RAC (Ministerio)", self.exportar_reporte_rac)
        self.btnExportar_emple.setMenu(menu_exportar_emple)
        
    def actualizar_conteo(self):
        """Actualiza los contadores de empleados."""
        try:
            stats = DashboardModel.obtener_estadisticas_empleados()
            self.lblActivos_emple.setText(str(stats.get('activos', 0)))
            self.lblInactivos_emple.setText(str(stats.get('inactivos', 0)))
            self.lblTotalRegistros_emple.setText(str(stats.get('total', 0)))
        except Exception as e:
            print(f"Error actualizando conteo: {e}")

    def actualizar_conteo_desde_cache(self, activos: int, inactivos: int, total: int):
        """Actualiza contadores con datos ya consultados."""
        try:
            self.lblActivos_emple.setText(str(activos))
            self.lblInactivos_emple.setText(str(inactivos))
            self.lblTotalRegistros_emple.setText(str(total))
        except Exception as err:
            print(f"Error actualizando conteo desde cache: {err}")

    def obtener_datos_tableview(self, view):
        """Extrae encabezados y filas visibles de un QTableView."""
        model = view.model()
        encabezados = [model.headerData(c, Qt.Horizontal) for c in range(model.columnCount())]
        filas = []
        for r in range(model.rowCount()):
            fila = []
            for c in range(model.columnCount()):
                index = model.index(r, c)
                val = model.data(index, Qt.ItemDataRole.DisplayRole)
                fila.append("" if val is None else str(val))
            filas.append(fila)
        return encabezados, filas

    def filtrar_tabla_empleados(self, texto):
        """Aplica filtro a la tabla según texto y columna seleccionada."""
        if not hasattr(self, "proxy_empleados"):
            return

        # Mapa de columnas
        mapa_columnas = {
            0: -1,   # Todos
            1: 1,    # Cédula
            2: 2,    # Nombres
            3: 3,    # Apellidos
            4: 4,    # Fecha Nac.
            5: 5,    # Edad
            6: 6,    # Género
            7: 7,    # Dirección
            8: 8,    # Teléfono
            9: 9,    # Correo
            10: 10,  # Título
            11: 11,  # Cargo
            12: 12,  # Fecha ingreso
            13: 13,  # Num carnet
            14: 14,  # RIF
            15: 15,  # Código RAC
        }

        idx_combo = self.cbxFiltro_emple.currentIndex()
        columna_real = mapa_columnas.get(idx_combo, -1)

        self.proxy_empleados.setFilterKeyColumn(columna_real)
        self.proxy_empleados.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.proxy_empleados.setFilterRegularExpression(texto)
    
    def registro_empleados(self):
        """Abre el formulario de registro de nuevo empleado."""
        ventana = RegistroEmpleado(self.usuario_actual, self)
        if ventana.exec():
            self.database_empleados()
            self.actualizar_conteo()
    
    def DetallesEmpleados(self):
        """Abre la ventana de detalles del empleado seleccionado."""
        index = self.tableW_emple.currentIndex()
        
        if not index.isValid():
            crear_msgbox(
                self,
                "Selección requerida",
                "Debe seleccionar un empleado de la tabla.",
                QMessageBox.Warning
            ).exec()
            return

        # Mapear al modelo base
        index_source = self.tableW_emple.model().mapToSource(index)
        fila = index_source.row()
        model = index_source.model()
        id_empleado = int(model.item(fila, 0).text())

        # Abrir detalles
        ventana = DetallesEmpleado(id_empleado, self.usuario_actual, self)
        ventana.datos_actualizados.connect(self.database_empleados)
        ventana.datos_actualizados.connect(self.actualizar_conteo)
        ventana.exec()
    
    def eliminar_empleado(self):
        """Elimina el empleado seleccionado tras confirmación."""
        index = self.tableW_emple.currentIndex()
        
        if not index.isValid():
            crear_msgbox(
                self,
                "Selección requerida",
                "Debe seleccionar un empleado primero.",
                QMessageBox.Warning
            ).exec()
            return

        # Mapear al modelo base
        index_source = self.tableW_emple.model().mapToSource(index)
        fila = index_source.row()
        model = index_source.model()
        empleado_id = int(model.item(fila, 0).text())

        # Confirmación
        reply = crear_msgbox(
            self,
            "Confirmar eliminación",
            "¿Está seguro de eliminar este empleado?\n\n"
            "Esta acción no se puede deshacer.",
            QMessageBox.Question,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if reply.exec() != QMessageBox.StandardButton.Yes:
            return

        try:
            ok, mensaje = EmpleadoModel.eliminar(empleado_id, self.usuario_actual)

            if ok:
                crear_msgbox(
                    self,
                    "Éxito",
                    mensaje,
                    QMessageBox.Information
                ).exec()
                self.database_empleados()
                self.actualizar_conteo()
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
                "Error",
                f"Error en la BD: {err}",
                QMessageBox.Critical
            ).exec()

    def database_empleados(self):
        """Carga la lista completa de empleados en la tabla."""
        try:
            datos = EmpleadoModel.listar() 
            columnas = [
                "ID", "Cédula", "Nombres", "Apellidos", "Fecha Nac.",
                "Edad", "Género", "Dirección", "Teléfono",
                "Correo", "Título", "Cargo", "Fecha Ingreso", "Num.Carnet", "RIF", "Código RAC",
                "Horas Acad.", "Horas Adm.", "Tipo Personal", "Estado"
            ]

            # Crear modelo base
            model_empleados = QStandardItemModel(len(datos), len(columnas))
            model_empleados.setHorizontalHeaderLabels(columnas)

            # Poblar modelo
            for fila, registro in enumerate(datos):
                for col, valor in enumerate(registro):
                    item = QStandardItem(str(valor))
                    item.setEditable(False)
                    model_empleados.setItem(fila, col, item)

            # Asignar al proxy
            self.proxy_empleados.setSourceModel(model_empleados)
            
            # Delegate personalizado (columna estado = 19)
            delegate = EmpleadoDelegate(self.tableW_emple, estado_columna=19)
            self.tableW_emple.setItemDelegate(delegate)

            # Configurar tabla
            self.tableW_emple.setSortingEnabled(True)
            self.tableW_emple.setAlternatingRowColors(True)
            self.tableW_emple.setColumnHidden(0, True)

            # Numeración vertical
            row_count = self.proxy_empleados.rowCount()
            for fila in range(row_count):
                self.proxy_empleados.setHeaderData(fila, Qt.Vertical, str(fila + 1))

        except Exception as err:
            print(f"Error en database_empleados: {err}")
    
    def obtener_empleado_seleccionado(self):
        """Obtiene todos los datos del empleado seleccionado."""
        index = self.tableW_emple.currentIndex()
        if not index.isValid():
            return None

        proxy = self.tableW_emple.model()
        source_index = proxy.mapToSource(index)
        fila = source_index.row()

        model = proxy.sourceModel()
        datos = {}
        for col in range(model.columnCount()):
            header = model.headerData(col, Qt.Horizontal)
            valor = model.item(fila, col).text()
            datos[header] = valor
        return datos
    
    def exportar_constancia_empleado(self):
        """Genera constancia de trabajo en PDF del empleado seleccionado."""
        empleado = self.obtener_empleado_seleccionado()
        
        if not empleado:
            crear_msgbox(
                self,
                "Selección requerida",
                "Debe seleccionar un empleado de la tabla.",
                QMessageBox.Warning
            ).exec()
            return

        try:
            institucion = InstitucionModel.obtener_por_id(1)
            archivo = generar_constancia_trabajo(empleado, institucion)
            
            crear_msgbox(
                self,
                "Éxito",
                f"Constancia generada correctamente:\n{archivo}",
                QMessageBox.Information
            ).exec()
            
            abrir_archivo(archivo)
            
        except Exception as e:
            crear_msgbox(
                self,
                "Error",
                f"No se pudo generar la constancia:\n{e}",
                QMessageBox.Critical
            ).exec()
    
    def exportar_excel_empleados(self):
        """Exporta la tabla filtrada actual a Excel."""
        try:
            # Validar que haya datos
            if self.proxy_empleados.rowCount() == 0:
                crear_msgbox(
                    self,
                    "Tabla vacía",
                    "No hay datos para exportar.",
                    QMessageBox.Warning
                ).exec()
                return
            
            # Obtener encabezados y filas
            encabezados, filas = self.obtener_datos_tableview(self.tableW_emple)

            # Preguntar ubicación
            ruta, _ = QFileDialog.getSaveFileName(
                self,
                "Guardar reporte",
                f"empleados_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                "Archivos Excel (*.xlsx)"
            )
            
            if not ruta:
                return
            
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
            
            abrir_archivo(archivo)
            
        except Exception as e:
            crear_msgbox(
                self,
                "Error",
                f"No se pudo exportar:\n{e}",
                QMessageBox.Critical
            ).exec()
    
    def exportar_excel_empleados_bd(self):
        """Exporta la lista completa de empleados activos a Excel."""
        try:
            empleados = EmpleadoModel.listar_activos()
            
            if not empleados:
                crear_msgbox(
                    self,
                    "Sin datos",
                    "No hay empleados activos para exportar.",
                    QMessageBox.Warning
                ).exec()
                return
            
            archivo = exportar_empleados_excel(self, empleados)
            
            if not archivo:
                return  # Usuario canceló
            
            crear_msgbox(
                self,
                "Éxito",
                f"Archivo exportado correctamente:\n{archivo}\n\n"
                f"Total de empleados: {len(empleados)}",
                QMessageBox.Information
            ).exec()
            
            abrir_archivo(archivo)
            
        except Exception as e:
            crear_msgbox(
                self,
                "Error",
                f"No se pudo exportar:\n{e}",
                QMessageBox.Critical
            ).exec()
    
    def exportar_reporte_rac(self):
        """Genera reporte RAC (Registro de Asignación de Cargos) en formato Excel."""
        try:
            # Obtener todos los empleados activos
            empleados = EmpleadoModel.listar_activos()
            
            if not empleados:
                crear_msgbox(
                    self,
                    "Sin datos",
                    "No hay empleados activos para generar el reporte RAC.",
                    QMessageBox.Warning
                ).exec()
                return
            
            # Obtener datos de la institución
            institucion = InstitucionModel.obtener_por_id(1)
            
            if not institucion:
                crear_msgbox(
                    self,
                    "Error",
                    "No se pudieron cargar los datos de la institución.\n"
                    "Asegúrese de configurar los datos institucionales.",
                    QMessageBox.Warning
                ).exec()
                return
            
            # Generar reporte
            archivo = generar_reporte_rac(self, empleados, institucion)
            
            if archivo:
                abrir_archivo(archivo)
            
        except Exception as e:
            crear_msgbox(
                self,
                "Error",
                f"No se pudo generar el reporte RAC:\n{e}",
                QMessageBox.Critical
            ).exec()