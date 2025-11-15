from PySide6.QtWidgets import QWidget
from ui_compiled.gestion_estudiantes_ui import Ui_gestion_estudiantes
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

import os
from views.registro_estudiante import NuevoRegistro
from views.detalles_estudiante import DetallesEstudiante
from models.estu_model import EstudianteModel
from views.delegates import EstudianteDelegate
from utils.proxies import ProxyConEstado
from datetime import datetime
from utils.dialogs import crear_msgbox


class GestionEstudiantesPage(QWidget, Ui_gestion_estudiantes):
    def __init__(self, usuario_actual, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        institucion = InstitucionModel.obtener_por_id(1) 
        self.setupUi(self)
        
        # Modulo ESTUDIANTES
        self.lneBuscar_estu.textChanged.connect(self.filtrar_tabla_estudiantes)
        self.cbxFiltro_estu.currentIndexChanged.connect(lambda _: self.filtrar_tabla_estudiantes(self.lneBuscar_estu.text()))
        self.btnNuevo_students.clicked.connect(self.registro_estudiante)
       
        self.proxy_estudiantes = ProxyConEstado(columna_estado=17, parent=self)
        self.tableW_students.setModel(self.proxy_estudiantes)

        self.chkMostrar_inactivos_estu.stateChanged.connect(
        lambda estado: self.proxy_estudiantes.setMostrarInactivos(bool(estado))
        )

        self.database_estudiantes()
        self.btnActualizar_db_estu.clicked.connect(self.database_estudiantes)
        self.btnDetalles_students.clicked.connect(self.DetallesEstudiante)
        self.btnEliminar_estudiante.clicked.connect(self.eliminar_estudiante)
        
        self.btnExportar_estu.setPopupMode(QToolButton.InstantPopup)
        menu_exportar_estu = QMenu(self.btnExportar_estu)
        menu_exportar_estu.addAction("Constancia de buena conducta", self.exportar_buena_conducta)
        menu_exportar_estu.addAction("Exportar tabla filtrada a Excel", self.exportar_excel_estudiantes)
        menu_exportar_estu.addAction("Exportar matricula completa a Excel", self.exportar_excel_estudiantes_bd)
        self.btnExportar_estu.setMenu(menu_exportar_estu)

    def actualizar_conteo(self):
        self.lblActivos_estu.setText(str(DashboardModel.total_estudiantes_activos()))
        self.lblInactivos_estu.setText(str(DashboardModel.total_estudiantes_inactivos()))
        self.lblTotalRegistros_estu.setText(str(DashboardModel.total_estudiantes_registrados()))

    def exportar_constancia_estudios(self):
        estudiante = self.obtener_estudiante_seleccionado()
        if not estudiante:
            QMessageBox.warning(self, "Atención", "Debe seleccionar un estudiante.")
            return

        try:
            # Si tu sistema solo maneja una institución fija, llamas directo al modelo
            institucion = InstitucionModel.obtener_por_id(1)  # o el ID fijo que uses

            # Pasas el estudiante y los datos de la institución
            archivo = generar_constancia_estudios(estudiante, institucion)
            os.startfile(archivo)  # Windows
            # Para Linux/Mac: subprocess.call(["xdg-open", archivo]) o ["open", archivo])
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo generar la constancia: {e}")
    
    def exportar_buena_conducta(self):
        estudiante = self.obtener_estudiante_seleccionado()
        if not estudiante:
            QMessageBox.warning(self, "Atención", "Debe seleccionar un estudiante.")
            return

        try:
            # Obtienes el dict de institución una sola vez
            institucion = InstitucionModel.obtener_por_id(1)  # ID fijo

            # Pasas el estudiante y el dict de institución
            archivo = generar_buena_conducta(estudiante, institucion)
            os.startfile(archivo)  # Windows
            # Para Linux/Mac: subprocess.call(["xdg-open", archivo]) o ["open", archivo])
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo generar la constancia: {e}")

    def registro_estudiante(self):
        ventana = NuevoRegistro(self.usuario_actual, self)
        ventana.exec() #Modal: Se bloquea la ventana principal
    def DetallesEstudiante(self):
        # Obtener el índice seleccionado en la vista
        index = self.tableW_students.currentIndex()
        if index.isValid():
            # Convertir al índice del modelo base (porque usamos proxy para ordenar/filtrar)
            index_source = self.tableW_students.model().mapToSource(index)
            fila = index_source.row()

            # Obtener el ID desde la columna 0 del modelo base
            model = index_source.model()
            id_estudiante = int(model.item(fila, 0).text())

            # Abrir la ventana de detalles
            ventana = DetallesEstudiante(id_estudiante, self.usuario_actual, self)  # ya no pasamos self.conexion
            ventana.datos_actualizados.connect(self.database_estudiantes)
            ventana.exec()
    
    from PySide6.QtWidgets import QMessageBox

    def eliminar_estudiante(self):
        # Obtener índice seleccionado
        index = self.tableW_students.currentIndex()
        if not index.isValid():
            msg = crear_msgbox(
                self,
                "Eliminar",
                "Seleccione un estudiante primero.",
                QMessageBox.Warning,
            )
            msg.exec()
            return

        # Mapear al modelo base
        index_source = self.tableW_students.model().mapToSource(index)
        fila = index_source.row()
        model = index_source.model()

        # ID del estudiante (columna 0)
        id_estudiante = int(model.item(fila, 0).text())

        # Confirmación
        msg = crear_msgbox(
            self,
            "Confirmar eliminación",
            "¿Está seguro de eliminar este estudiante?",
            QMessageBox.Question,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if msg.exec() != QMessageBox.Yes:
            return

        try:
            ok, mensaje = EstudianteModel.eliminar(id_estudiante, self.usuario_actual)

            if ok:
                msg = crear_msgbox(
                    self,
                    "Éxito",
                    mensaje,
                    QMessageBox.Information,
                )
                msg.exec()
                self.database_estudiantes()  # refrescar tabla
            else:
                msg = crear_msgbox(
                    self,
                    "Error",
                    mensaje,
                    QMessageBox.Warning,
                )
                msg.exec()

        except Exception as err:
            msg = crear_msgbox(
                    self,
                    "Error",
                    f"Error en la BD: {err}",
                    QMessageBox.Critical,
                )
            msg.exec()


    def database_estudiantes(self):
        try:
            datos = EstudianteModel.listar()
            columnas = [
                "ID", "Cédula", "Nombres", "Apellidos", "Fecha Nac.",
                "Edad", "Ciudad", "Género", "Dirección", "Teléfono",
                "Correo", "Grado", "Sección", "Docente", "TallaC",
                "TallaP", "TallaZ", "Estado"
            ]

            # Crear modelo base
            model_estudiantes = QStandardItemModel(len(datos), len(columnas))
            model_estudiantes.setHorizontalHeaderLabels(columnas)

            # Poblar modelo
            for fila, registro in enumerate(datos):
                for col, valor in enumerate(registro):
                    item = QStandardItem(str(valor))
                    item.setEditable(False)
                    model_estudiantes.setItem(fila, col, item)

            self.proxy_estudiantes.setSourceModel(model_estudiantes)


            # Delegate
            delegate = EstudianteDelegate(self.tableW_students)
            self.tableW_students.setItemDelegate(delegate)

            # Configurar tabla
            
            self.tableW_students.setSortingEnabled(True)
            self.tableW_students.setAlternatingRowColors(True)
            self.tableW_students.setColumnHidden(0, True)  # ocultar ID

            # Numeración vertical
            row_count = self.proxy_estudiantes.rowCount()
            for fila in range(row_count):
                self.proxy_estudiantes.setHeaderData(fila, Qt.Vertical, str(fila + 1))

        except Exception as err:
            print(f"Error en database_estudiantes: {err}")
    
    def obtener_estudiante_seleccionado(self):
        index = self.tableW_students.currentIndex()
        if not index.isValid():
            return None

        # Obtener el proxy de la tabla
        proxy = self.tableW_students.model()
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
                4: 4,    # Fecha Nac.
                5: 5,    # Edad
                6: 6,    # Ciudad
                7: 7,    # Género
                8: 8,    # Dirección
                9: 9,    # Teléfono
                10: 10,  # Correo
                11: 11,  # Grado
                12: 12,  # Sección
                13: 13,  # Docente
                14: 14,  # TallaC
                15: 15,  # TallaP
                16: 16   # TallaZ
                # La columna 17 es "estado", la maneja tu proxy personalizado
            }

            idx_combo = self.cbxFiltro_estu.currentIndex()
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

    def exportar_excel_estudiantes(self):
        try:
            # 1) Obtener encabezados y filas desde la tabla
            encabezados, filas = self.obtener_datos_tableview(self.tableW_students)

            # 2) Preguntar ubicación al usuario
            ruta, _ = QFileDialog.getSaveFileName(
                self,
                "Guardar reporte",
                f"estudiantes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                "Archivos Excel (*.xlsx)"
            )
            if not ruta:
                return  # usuario canceló
            if not ruta.endswith(".xlsx"):
                ruta += ".xlsx"

            # 3) Exportar usando tu helper de exportar.py
            archivo = exportar_tabla_excel(ruta, encabezados, filas)

            # 4) Avisar y abrir
            msg = crear_msgbox(
                    self,
                    "Éxito",
                    f"Archivo exportado: {archivo}",
                    QMessageBox.Information,
                )
            msg.exec()
            os.startfile(archivo)
        except Exception as e:
            msg = crear_msgbox(
                    self,
                    "Error",
                    f"No se pudo exportar: {e}",
                    QMessageBox.Critical,
                )
            msg.exec()
    
    def exportar_excel_estudiantes_bd(self):
        try:
            estudiantes = EstudianteModel.listar_activos()
            archivo = exportar_estudiantes_excel(self, estudiantes)
            if not archivo:
                return  # usuario canceló
            msg = crear_msgbox(
                    self,
                    "Éxito",
                    f"Archivo exportado: {archivo}",
                    QMessageBox.Information,
                )
            msg.exec()
            os.startfile(archivo)
        except Exception as e:
            msg = crear_msgbox(
                    self,
                    "Error",
                    f"No se pudo exportar: {e}",
                    QMessageBox.Critical,
                )
            msg.exec()
