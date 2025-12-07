from PySide6.QtWidgets import QWidget
from ui_compiled.detalles_seccion_ui import Ui_detalle_seccion
from PySide6.QtWidgets import (
    QToolButton, QMenu, QMessageBox, QFileDialog
)
from PySide6.QtCore import Qt, QSortFilterProxyModel
from PySide6.QtGui import QStandardItem, QStandardItemModel

from models.dashboard_model import DashboardModel
from models.institucion_model import InstitucionModel
from models.estu_model import EstudianteModel

import os
import subprocess
from views.registro_estudiante import NuevoRegistro
from views.detalles_estudiante import DetallesEstudiante
from models.secciones_model import SeccionesModel
from views.delegates import EstudianteDelegate
from utils.proxies import ProxyConEstado
from datetime import datetime
from utils.dialogs import crear_msgbox


class DetallesSeccion(QWidget, Ui_detalle_seccion):
    def __init__(self, usuario_actual, seccion_id, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.seccion_id = int(seccion_id) if seccion_id is not None else None
        self.setupUi(self)
        
        # Mostrar título con grado y letra de la sección
        try:
            secciones = SeccionesModel.obtener_todas()
            sec = next((s for s in secciones if int(s.get("id", 0)) == int(self.seccion_id)), None)
            if sec:
                titulo = f"{sec.get('grado', '')} {sec.get('letra', '')}".strip()
            else:
                titulo = "Detalle de sección"
            try:
                self.lblTitulo_detalle_seccion.setText(titulo)
            except Exception:
                pass
        except Exception:
            pass

        self.lneBuscar_detalle_seccion.textChanged.connect(self.filtrar_tabla_estudiantes)
        self.cbxFiltro_detalle_seccion.currentIndexChanged.connect(lambda _: self.filtrar_tabla_estudiantes(self.lneBuscar_detalle_seccion.text()))

        # Proxy para filtrado
        self.proxy_estudiantes = QSortFilterProxyModel(self)
        self.proxy_estudiantes.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.proxy_estudiantes.setFilterKeyColumn(-1)

        self.tableW_detalles_seccion()

    def actualizar_conteo(self):
        try:
            self.lblActivos_seccion.setText(str(DashboardModel.total_estudiantes_activos()))
        except Exception as err:
            print(f"Error actualizando conteo: {err}")


    def tableW_detalles_seccion(self):
        try:
            # Traer estudiantes asignados a la sección (usa año actual)
            if self.seccion_id is None:
                datos = []
            else:
                año = datetime.now().year
                datos = EstudianteModel.listar_por_seccion(self.seccion_id, año) or []

            # Columnas que dejaste en la UI
            columnas = [
                "ID", "Cédula", "Nombres", "Apellidos",
                "Edad", "Género"
            ]

            # Crear modelo base (source model)
            model_estudiantes = QStandardItemModel(len(datos), len(columnas))
            model_estudiantes.setHorizontalHeaderLabels(columnas)

            # Poblar modelo (solo las columnas necesarias)
            for fila, registro in enumerate(datos):
                item_id = QStandardItem(str(registro.get("id", "")))
                item_cedula = QStandardItem(str(registro.get("cedula", "")))
                item_nombres = QStandardItem(str(registro.get("nombres", "")))
                item_apellidos = QStandardItem(str(registro.get("apellidos", "")))
                item_edad = QStandardItem(str(registro.get("edad", "")))
                item_genero = QStandardItem(str(registro.get("genero", "") or ""))

                items = [
                    item_id, item_cedula, item_nombres, item_apellidos, item_edad, item_genero
                ]

                for col, item in enumerate(items):
                    item.setEditable(False)
                    model_estudiantes.setItem(fila, col, item)

            # Conectar modelo al proxy y la vista
            self.proxy_estudiantes.setSourceModel(model_estudiantes)
            self.tableW_seccion.setModel(self.proxy_estudiantes)

            # Delegate (si usas uno)
            delegate = EstudianteDelegate(self.tableW_seccion)
            self.tableW_seccion.setItemDelegate(delegate)

            # Configurar tabla
            self.tableW_seccion.setSortingEnabled(True)
            self.tableW_seccion.setAlternatingRowColors(True)
            self.tableW_seccion.setColumnHidden(0, True)  # ocultar ID

            # Numeración vertical (mostrar 1..N en la cabecera izquierda)
            # Debe establecerse en el modelo que usa la vista -> el proxy
            for i in range(self.proxy_estudiantes.rowCount()):
                self.proxy_estudiantes.setHeaderData(i, Qt.Vertical, str(i + 1), Qt.DisplayRole)

        except Exception as err:
            print(f"Error en database_estudiantes: {err}")
    
    def obtener_estudiante_seleccionado(self):
        index = self.tableW_seccion.currentIndex()
        if not index.isValid():
            return None

        # Obtener el proxy de la tabla
        proxy = self.tableW_seccion.model()
        source_index = proxy.mapToSource(index)
        fila = source_index.row()

        model = proxy.sourceModel()
        datos = {}
        for col in range(model.columnCount()):
            header = model.headerData(col, Qt.Horizontal)
            valor = model.item(fila, col).text()
            datos[header] = valor
        return datos
    
    def filtrar_tabla_estudiantes(self, texto):
        if hasattr(self, "proxy_estudiantes"):
            # Mapa entre índice del combo y columna real del modelo
            # Opción 0 = Todos, luego cada campo visible
            mapa_columnas = {
                0: -1,   # Todos
                1: 1,    # Cédula
                2: 2,    # Nombres
                3: 3,    # Apellidos
                4: 4,    # Edad
                5: 5,    # Género
            }

            idx_combo = self.cbxFiltro_detalle_seccion.currentIndex()
            columna_real = mapa_columnas.get(idx_combo, -1)

            self.proxy_estudiantes.setFilterKeyColumn(columna_real)
            self.proxy_estudiantes.setFilterCaseSensitivity(Qt.CaseInsensitive)
            self.proxy_estudiantes.setFilterRegularExpression(texto)
    
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