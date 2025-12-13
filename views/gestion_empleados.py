from PySide6.QtWidgets import (
     QToolButton, QMenu, QMessageBox, QFileDialog, QWidget
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel

from models.dashboard_model import DashboardModel
from utils.exportar import (
    generar_constancia_trabajo,
    exportar_tabla_excel, exportar_empleados_excel
)
from utils.sombras import crear_sombra_flotante
import os

from views.delegates import EmpleadoDelegate
from views.registro_empleado import RegistroEmpleado
from models.emple_model import EmpleadoModel
from views.detalles_empleados import DetallesEmpleado
from utils.proxies import ProxyConEstado
from utils.dialogs import crear_msgbox
from datetime import datetime
from ui_compiled.gestion_empleados_ui import Ui_gestion_empleados


class GestionEmpleadosPage(QWidget, Ui_gestion_empleados):
    def __init__(self, usuario_actual, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.setupUi(self)

        # Botones empleados ###
        self.proxy_empleados = ProxyConEstado(columna_estado=16, parent=self)
        self.tableW_emple.setModel(self.proxy_empleados)

        self.chkMostrar_inactivos_emple.stateChanged.connect(
        lambda estado: self.proxy_empleados.setMostrarInactivos(bool(estado))
        )
        
        self.database_empleados()
        self.lneBuscar_emple.textChanged.connect(self.filtrar_tabla_empleados)
        self.cbxFiltro_emple.currentIndexChanged.connect(lambda _: self.filtrar_tabla_empleados(self.lneBuscar_emple.text()))
        self.btnNuevo_emple.clicked.connect(self.registro_empleados)
        self.btnActualizar_db_emple.clicked.connect(self.database_empleados)
        self.btnDetalles_emple.clicked.connect(self.DetallesEmpleados)
        self.btnEliminar_emple.clicked.connect(self.eliminar_empleado)

        self.btnExportar_emple.setPopupMode(QToolButton.InstantPopup)
        menu_exportar_emple = QMenu(self.btnExportar_emple)
        menu_exportar_emple.addAction("Constancia de trabajo PDF", self.exportar_constancia_empleado)
        menu_exportar_emple.addAction("Exportar tabla filtrada a Excel", self.exportar_excel_empleados)
        menu_exportar_emple.addAction("Exportar BD completa a Excel", self.exportar_excel_empleados_bd)
        self.btnExportar_emple.setMenu(menu_exportar_emple)

        ## Sombras de elementos ##
        crear_sombra_flotante(self.btnNuevo_emple)
        crear_sombra_flotante(self.btnDetalles_emple)
        crear_sombra_flotante(self.btnExportar_emple)
        crear_sombra_flotante(self.btnEliminar_emple, opacity=120)
        crear_sombra_flotante(self.frameFiltro_estu_4, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lneBuscar_emple, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.frameTabla_emple, blur_radius=8, y_offset=1)
        
    def actualizar_conteo(self):
        self.lblActivos_emple.setText(str(DashboardModel.total_empleados_activos()))
        self.lblInactivos_emple.setText(str(DashboardModel.total_empleados_inactivos()))
        self.lblTotalRegistros_emple.setText(str(DashboardModel.total_empleados_registrados()))

    def obtener_datos_tableview(self, view):
        """
        Extrae encabezados y filas de un QTableView.
        """
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
        if hasattr(self, "proxy_empleados"):
            # Mapa entre índice del combo y columna real del modelo
            # Opción 0 = Todos, luego cada campo visible
            mapa_columnas = {
                0: -1,   # Todos
                1: 1,    # Cédula
                2: 2,    # Nombres
                3: 3,    # Apellidos
                4: 4,    # Fecha Nac.
                5: 5,    # Edad
                6: 6,    # Genero
                7: 7,    # Direccion
                8: 8,    # Telefono
                9: 9,    # Correo
                10: 10,  # Titulo
                11: 11,  # Cargo
                12: 12,  # Fecha ingreso
                13: 13,  # Num carnet
                14: 14,  # RIF
                15: 15,  # Codigo RAC
                # La columna 16 es "estado", la maneja el proxy personalizado
            }

            idx_combo = self.cbxFiltro_emple.currentIndex()
            columna_real = mapa_columnas.get(idx_combo, -1)

            self.proxy_empleados.setFilterKeyColumn(columna_real)
            self.proxy_empleados.setFilterCaseSensitivity(Qt.CaseInsensitive)
            self.proxy_empleados.setFilterRegularExpression(texto)

    
    def registro_empleados(self):
        ventana = RegistroEmpleado(self.usuario_actual, self)
        ventana.exec()
    
    def DetallesEmpleados(self):
        # Obtener el índice seleccionado en la vista
        index = self.tableW_emple.currentIndex()
        if index.isValid():
            # Convertir al índice del modelo base (porque usamos proxy para ordenar/filtrar)
            index_source = self.tableW_emple.model().mapToSource(index)
            fila = index_source.row()

            # Obtener el ID desde la columna 0 del modelo base
            model = index_source.model()
            id_empleado = int(model.item(fila, 0).text())

            # Abrir la ventana de detalles
            ventana = DetallesEmpleado(id_empleado, self.usuario_actual, self)
            ventana.datos_actualizados.connect(self.database_empleados)  # refresca tabla al emitirse
            ventana.exec()
    
    def eliminar_empleado(self):
        # Obtener índice seleccionado
        index = self.tableW_emple.currentIndex()
        if not index.isValid():
            msg = crear_msgbox(
                self,
                "Eliminar",
                "Seleccione un empleado primero.",
                QMessageBox.Warning
            )
            msg.exec()
            return

        # Mapear al modelo base
        index_source = self.tableW_emple.model().mapToSource(index)
        fila = index_source.row()
        model = index_source.model()

        # ID del empleado (columna 0)
        empleado_id = int(model.item(fila, 0).text())

        # Confirmación usando crear_msgbox
        reply = crear_msgbox(
            self,
            "Confirmar eliminación",
            "¿Está seguro de eliminar este empleado?",
            QMessageBox.Question,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if reply.exec() != QMessageBox.StandardButton.Yes:
            return

        try:
            ok, mensaje = EmpleadoModel.eliminar(empleado_id, self.usuario_actual)

            if ok:
                msg = crear_msgbox(
                    self,
                    "Éxito",
                    mensaje,
                    QMessageBox.Information
                )
                msg.exec()
                self.database_empleados()  # refrescar tabla
            else:
                msg = crear_msgbox(
                    self,
                    "Error",
                    mensaje,
                    QMessageBox.Warning
                )
                msg.exec()

        except Exception as err:
            msg = crear_msgbox(
                self,
                "Error",
                f"Error en la BD: {err}",
                QMessageBox.Critical
            )
            msg.exec()

    def database_empleados(self):
        
            try:
                datos = EmpleadoModel.listar() 
                columnas = [
                    "ID", "Cédula", "Nombres", "Apellidos", "Fecha Nac.",
                    "Edad", "Género", "Dirección", "Teléfono",
                    "Correo", "Titulo", "Cargo", "Fecha Ingreso", "Num.Carnet", "RIF","codigo_rac", "Estado"
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

                # Proxy
                self.proxy_empleados.setSourceModel(model_empleados)
                
                # Delegate
                delegate = EmpleadoDelegate(self.tableW_emple)
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
        index = self.tableW_emple.currentIndex()
        if not index.isValid():
            return None

        # Obtener el proxy de la tabla
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
        empleado = self.obtener_empleado_seleccionado()
        if not empleado:
            QMessageBox.warning(self, "Atención", "Debe seleccionar un empleado.")
            return

        try:
            archivo = generar_constancia_trabajo(empleado)
            os.startfile(archivo)  # Windows
            # Para Linux/Mac: subprocess.call(["xdg-open", archivo]) o ["open", archivo]
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo generar la constancia: {e}")
    
    def exportar_excel_empleados(self):
        try:
            # Obtener encabezados y filas desde la tabla
            encabezados, filas = self.obtener_datos_tableview(self.tableW_emple)

            # Preguntar ubicación al usuario
            ruta, _ = QFileDialog.getSaveFileName(
                self,
                "Guardar reporte",
                f"empleados_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                "Archivos Excel (*.xlsx)"
            )
            if not ruta:
                return  # usuario canceló
            if not ruta.endswith(".xlsx"):
                ruta += ".xlsx"

            # Exportar usando tu helper de exportar.py
            archivo = exportar_tabla_excel(ruta, encabezados, filas)

            # Avisar y abrir
            QMessageBox.information(self, "Éxito", f"Archivo exportado: {archivo}")
            os.startfile(archivo)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo exportar: {e}")
    
    def exportar_excel_empleados_bd(self):
        try:
            empleados = EmpleadoModel.listar_activos()
            archivo = exportar_empleados_excel(self, empleados)
            if not archivo:
                return  # usuario canceló
            QMessageBox.information(self, "Éxito", f"Archivo exportado: {archivo}")
            os.startfile(archivo)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo exportar: {e}")