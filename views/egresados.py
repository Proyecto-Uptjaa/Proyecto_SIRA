from PySide6.QtWidgets import QWidget, QDialog
from ui_compiled.Egresados_ui import Ui_Egresados
from PySide6.QtWidgets import (
    QToolButton, QMenu, QMessageBox, QFileDialog
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel

from models.dashboard_model import DashboardModel
from models.institucion_model import InstitucionModel
from utils.exportar import (
    generar_constancia_estudios, generar_buena_conducta,
    exportar_tabla_excel, exportar_estudiantes_excel,)
from utils.sombras import crear_sombra_flotante

import os
import subprocess
from views.detalles_estudiante import DetallesEstudiante
from models.estu_model import EstudianteModel
from views.delegates import EstudianteDelegate
from utils.proxies import ProxyConEstado
from datetime import datetime
from utils.dialogs import crear_msgbox


class Egresados(QWidget, Ui_Egresados):
    def __init__(self, usuario_actual, año_escolar, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.año_escolar = año_escolar
        self.setupUi(self)
        
        # Modulo EGRESADOS
        self.lneBuscar_egresados.textChanged.connect(self.filtrar_tabla_egresados)
        self.cbxFiltro_egresados.currentIndexChanged.connect(lambda _: self.filtrar_tabla_egresados(self.lneBuscar_egresados.text()))
       
        self.proxy_egresados = ProxyConEstado(columna_estado=-1, parent=self)  # Sin columna estado para egresados
        self.tableW_egresados.setModel(self.proxy_egresados)

        self.database_egresados()
        self.btnActualizar_db_egresados.clicked.connect(self.database_egresados)
        self.btnDetalles_egresados.clicked.connect(self.DetallesEstudiante)
        
        self.btnExportar_egresados.setPopupMode(QToolButton.InstantPopup)
        menu_exportar_egresados = QMenu(self.btnExportar_egresados)
        menu_exportar_egresados.addAction("Constancia de buena conducta", self.exportar_buena_conducta)
        menu_exportar_egresados.addAction("Exportar tabla filtrada a Excel", self.exportar_excel_egresados)
        self.btnExportar_egresados.setMenu(menu_exportar_egresados)

        ## Sombras de elementos ##
        crear_sombra_flotante(self.btnDetalles_egresados)
        crear_sombra_flotante(self.btnExportar_egresados)
        crear_sombra_flotante(self.frameFiltro_egresados, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lneBuscar_egresados, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.frameTabla_egresados, blur_radius=8, y_offset=1)

    def exportar_buena_conducta(self):
        estudiante = self.obtener_estudiante_seleccionado()
        if not estudiante:
            QMessageBox.warning(self, "Atención", "Debe seleccionar un estudiante.")
            return

        try:
            institucion = InstitucionModel.obtener_por_id(1)
            archivo = generar_buena_conducta(estudiante, institucion)
            subprocess.Popen(["xdg-open", archivo])
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo generar la constancia: {e}")

    def DetallesEstudiante(self):
        index = self.tableW_egresados.currentIndex()
        if index.isValid():
            index_source = self.tableW_egresados.model().mapToSource(index)
            fila = index_source.row()

            model = index_source.model()
            id_estudiante = int(model.item(fila, 0).text())

            ventana = DetallesEstudiante(
                id_estudiante, 
                self.usuario_actual, 
                self.año_escolar,
                es_egresado=True,  # Indicar que es egresado
                parent=self
            )
            ventana.datos_actualizados.connect(self.database_egresados)
            ventana.exec()

    def database_egresados(self):
        try:
            datos = EstudianteModel.listar_egresados()

            columnas = [
                "ID", "Cédula", "Nombres", "Apellidos", "Fecha Nac.",
                "Edad", "Ciudad", "Género", "Dirección",
                "Último Grado", "Última Sección", "Fecha Egreso"
            ]

            model_egresados = QStandardItemModel(len(datos), len(columnas))
            model_egresados.setHorizontalHeaderLabels(columnas)

            for fila, registro in enumerate(datos):
                item_id = QStandardItem(str(registro["id"]))
                item_cedula = QStandardItem(registro["cedula"])
                item_nombres = QStandardItem(registro["nombres"])
                item_apellidos = QStandardItem(registro["apellidos"])
                item_fecha = QStandardItem(registro["fecha_nac_est"].strftime("%d/%m/%Y") if registro["fecha_nac_est"] else "")
                item_edad = QStandardItem(str(registro["edad"]))
                item_ciudad = QStandardItem(registro["city"] or "")
                item_genero = QStandardItem(registro["genero"])
                item_direccion = QStandardItem(registro["direccion"] or "")
                item_grado = QStandardItem(registro["ultimo_grado"] or "N/A")
                item_seccion = QStandardItem(registro["ultima_seccion"] or "N/A")
                item_fecha_egreso = QStandardItem(registro["fecha_egreso"] or "N/A")

                items = [
                    item_id, item_cedula, item_nombres, item_apellidos, item_fecha,
                    item_edad, item_ciudad, item_genero, item_direccion,
                    item_grado, item_seccion, item_fecha_egreso
                ]

                for col, item in enumerate(items):
                    item.setEditable(False)
                    model_egresados.setItem(fila, col, item)

            self.proxy_egresados.setSourceModel(model_egresados)

            delegate = EstudianteDelegate(self.tableW_egresados)
            self.tableW_egresados.setItemDelegate(delegate)

            self.tableW_egresados.setSortingEnabled(True)
            self.tableW_egresados.setAlternatingRowColors(True)
            self.tableW_egresados.setColumnHidden(0, True)

            row_count = self.proxy_egresados.rowCount()
            for fila in range(row_count):
                self.proxy_egresados.setHeaderData(fila, Qt.Vertical, str(fila + 1), Qt.DisplayRole)

            # Actualizar label de conteo
            self.lblTotalRegistros_egresados.setText(str(len(datos)))

        except Exception as err:
            print(f"Error en database_egresados: {err}")
    
    def obtener_estudiante_seleccionado(self):
        index = self.tableW_egresados.currentIndex()
        if not index.isValid():
            return None

        proxy = self.tableW_egresados.model()
        source_index = proxy.mapToSource(index)
        fila = source_index.row()

        model = proxy.sourceModel()
        datos = {}
        for col in range(model.columnCount()):
            header = model.headerData(col, Qt.Horizontal)
            valor = model.item(fila, col).text()
            datos[header] = valor
        return datos
    
    def filtrar_tabla_egresados(self, texto):
        if hasattr(self, "proxy_egresados"):
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

    def exportar_excel_egresados(self):
        try:
            encabezados, filas = self.obtener_datos_tableview(self.tableW_egresados)

            ruta, _ = QFileDialog.getSaveFileName(
                self,
                "Guardar reporte",
                f"egresados_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                "Archivos Excel (*.xlsx)"
            )
            if not ruta:
                return
            if not ruta.endswith(".xlsx"):
                ruta += ".xlsx"

            archivo = exportar_tabla_excel(ruta, encabezados, filas)

            msg = crear_msgbox(
                self,
                "Éxito",
                f"Archivo exportado: {archivo}",
                QMessageBox.Information,
            )
            msg.exec()
            subprocess.Popen(["xdg-open", archivo])
        except Exception as e:
            msg = crear_msgbox(
                self,
                "Error",
                f"No se pudo exportar: {e}",
                QMessageBox.Critical,
            )
            msg.exec()
