from PySide6.QtWidgets import QWidget, QDialog
from ui_compiled.gestion_estudiantes_ui import Ui_gestion_estudiantes
from PySide6.QtWidgets import (
    QToolButton, QMenu, QMessageBox, QFileDialog
)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QStandardItem, QStandardItemModel

from models.dashboard_model import DashboardModel
from models.institucion_model import InstitucionModel
from utils.exportar import (
    generar_constancia_estudios, generar_buena_conducta,
    exportar_tabla_excel, exportar_estudiantes_excel, generar_constancia_inscripcion,
    generar_constancia_prosecucion_inicial)
from utils.sombras import crear_sombra_flotante
from utils.logo_manager import aplicar_logo_a_label
from utils.archivos import abrir_archivo

import os
from views.registro_estudiante import NuevoRegistro
from views.detalles_estudiante import DetallesEstudiante
from models.estu_model import EstudianteModel
from views.delegates import EstudianteDelegate
from utils.proxies import ProxyConEstado
from datetime import datetime
from utils.dialogs import crear_msgbox


class GestionEstudiantesPage(QWidget, Ui_gestion_estudiantes):
    """Página principal de gestión de estudiantes."""
    
    def __init__(self, usuario_actual, año_escolar, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.año_escolar = año_escolar
        
        self.setupUi(self)
        
        # Mostrar usuario conectado
        self.lblConectado_como.setText(f"Conectado como: {self.usuario_actual['username']}")
        
        # Configurar proxy para filtrado y ocultamiento de inactivos
        self.proxy_estudiantes = ProxyConEstado(columna_estado=16, parent=self)
        self.tableW_students.setModel(self.proxy_estudiantes)
        
        # Conectar controles de filtrado
        self.lneBuscar_estu.textChanged.connect(self.filtrar_tabla_estudiantes)
        self.cbxFiltro_estu.currentIndexChanged.connect(
            lambda _: self.filtrar_tabla_estudiantes(self.lneBuscar_estu.text())
        )
        self.chkMostrar_inactivos_estu.stateChanged.connect(
            lambda estado: self.proxy_estudiantes.setMostrarInactivos(bool(estado))
        )
        
        # Conectar botones de acción
        self.btnNuevo_students.clicked.connect(self.registro_estudiante)
        self.btnActualizar_db_estu.clicked.connect(self.database_estudiantes)
        self.btnDetalles_students.clicked.connect(self.DetallesEstudiante)
        self.btnEliminar_estudiante.clicked.connect(self.eliminar_estudiante)
        
        # Configurar menú de exportación
        self._configurar_menu_exportacion()
        
        # Cargar datos iniciales
        self.database_estudiantes()
        self.actualizar_conteo()
        
        # Configurar timer de actualización automática
        self.timer_actualizacion = QTimer(self)
        self.timer_actualizacion.timeout.connect(self.database_estudiantes)
        self.timer_actualizacion.timeout.connect(self.actualizar_conteo)
        self.timer_actualizacion.start(60000)  # Actualizar cada 60 segundos
        
        # Aplicar efectos visuales
        self._aplicar_sombras()

    def _aplicar_sombras(self):
        """Aplica sombras a elementos de la interfaz."""
        crear_sombra_flotante(self.btnNuevo_students)
        crear_sombra_flotante(self.btnDetalles_students)
        crear_sombra_flotante(self.btnExportar_estu)
        crear_sombra_flotante(self.btnActualizar_db_estu)
        crear_sombra_flotante(self.btnEliminar_estudiante, opacity=120)
        crear_sombra_flotante(self.frameFiltro_estu, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lneBuscar_estu, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.frameTabla_student, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lblTitulo_estu, blur_radius=5, y_offset=1)
        crear_sombra_flotante(self.lblLogo_estu, blur_radius=5, y_offset=1)
        
        # Aplicar logo institucional dinámico
        aplicar_logo_a_label(self.lblLogo_estu)
    
    def _configurar_menu_exportacion(self):
        """Configura el menú de exportación."""
        self.btnExportar_estu.setPopupMode(QToolButton.InstantPopup)
        menu_exportar_estu = QMenu(self.btnExportar_estu)
        
        # Agregar opciones de exportación
        menu_exportar_estu.addAction("Constancia de estudios", self.exportar_constancia_estudios)
        menu_exportar_estu.addAction("Constancia de buena conducta", self.exportar_buena_conducta)
        menu_exportar_estu.addAction("Constancia de inscripción", self.exportar_constancia_inscripcion)
        menu_exportar_estu.addAction("Constancia prosecución Educación Inicial", 
                                     self.exportar_constancia_prosecucion_inicial)
        menu_exportar_estu.addSeparator()
        menu_exportar_estu.addAction("Exportar tabla filtrada a Excel", self.exportar_excel_estudiantes)
        menu_exportar_estu.addAction("Exportar matrícula completa a Excel", 
                                     self.exportar_excel_estudiantes_bd)
        
        self.btnExportar_estu.setMenu(menu_exportar_estu)

    def actualizar_conteo(self):
        """Actualiza los contadores de estudiantes."""
        try:
            stats = DashboardModel.obtener_estadisticas_estudiantes()
            self.lblActivos_estu.setText(str(stats.get('activos', 0)))
            self.lblInactivos_estu.setText(str(stats.get('inactivos', 0)))
            self.lblTotalRegistros_estu.setText(str(stats.get('total', 0)))
        except Exception as err:
            print(f"Error actualizando conteo: {err}")

    def actualizar_conteo_desde_cache(self, activos: int, inactivos: int, total: int):
        """Actualiza contadores con datos ya consultados."""
        try:
            self.lblActivos_estu.setText(str(activos))
            self.lblInactivos_estu.setText(str(inactivos))
            self.lblTotalRegistros_estu.setText(str(total))
        except Exception as err:
            print(f"Error actualizando conteo desde cache: {err}")

    def registro_estudiante(self):
        """Abre el formulario de registro."""
        ventana = NuevoRegistro(self.usuario_actual, self.año_escolar, self)
        
        # Si se registró exitosamente, actualizar la interfaz
        if ventana.exec() == QDialog.Accepted:
            self.database_estudiantes()
            self.actualizar_conteo()
            
            # Actualizar tarjetas de secciones si existe la página
            if hasattr(self.parent(), 'page_gestion_secciones'):
                self.parent().page_gestion_secciones.actualizar_tarjetas()

    def DetallesEstudiante(self):
        """Abre la ventana de detalles del estudiante seleccionado"""
        # Obtener estudiante seleccionado
        estudiante_id = self._obtener_id_estudiante_seleccionado()
        if not estudiante_id:
            crear_msgbox(
                self,
                "Selección requerida",
                "Debe seleccionar un estudiante de la tabla.",
                QMessageBox.Warning
            ).exec()
            return

        # Abrir ventana de detalles
        ventana = DetallesEstudiante(
            estudiante_id, 
            self.usuario_actual, 
            self.año_escolar,
            es_egresado=False,  # Estudiantes regulares
            parent=self
        )
        
        # Actualizar tabla si se modificaron datos
        ventana.datos_actualizados.connect(self.database_estudiantes)
        ventana.datos_actualizados.connect(self.actualizar_conteo)
        ventana.exec()
        
        # Actualizar tarjetas de secciones después de cerrar detalles
        if hasattr(self.parent(), 'page_gestion_secciones'):
            self.parent().page_gestion_secciones.actualizar_tarjetas()

    def eliminar_estudiante(self):
        """Elimina el estudiante seleccionado de la base de datos"""
        # Obtener ID del estudiante seleccionado
        estudiante_id = self._obtener_id_estudiante_seleccionado()
        if not estudiante_id:
            crear_msgbox(
                self,
                "Selección requerida",
                "Debe seleccionar un estudiante de la tabla para eliminar.",
                QMessageBox.Warning
            ).exec()
            return

        # Confirmación de eliminación
        msg = crear_msgbox(
            self,
            "Confirmar eliminación",
            "¿Está seguro de eliminar este estudiante?\n\n"
            "Esta acción eliminará:\n"
            "- El registro del estudiante\n"
            "- Sus asignaciones a secciones\n"
            "- Su historial académico\n\n"
            "Esta acción NO se puede deshacer.",
            QMessageBox.Question,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if msg.exec() != QMessageBox.Yes:
            return

        try:
            # Intentar eliminar
            ok, mensaje = EstudianteModel.eliminar(estudiante_id, self.usuario_actual)

            if ok:
                crear_msgbox(
                    self,
                    "Éxito",
                    mensaje,
                    QMessageBox.Information,
                ).exec()
                
                # Refrescar interfaz
                self.database_estudiantes()
                self.actualizar_conteo()
                
                # Actualizar tarjetas de secciones
                if hasattr(self.parent(), 'page_gestion_secciones'):
                    self.parent().page_gestion_secciones.actualizar_tarjetas()
            else:
                crear_msgbox(
                    self,
                    "Error al eliminar",
                    mensaje,
                    QMessageBox.Warning,
                ).exec()

        except Exception as err:
            crear_msgbox(
                self,
                "Error inesperado",
                f"Error al eliminar estudiante:\n{err}",
                QMessageBox.Critical,
            ).exec()

    def database_estudiantes(self):
        """
        Carga los estudiantes del año actual en la tabla.
        Incluye información de sección y datos académicos.
        """
        try:
            # Obtener estudiantes del año escolar actual
            datos = EstudianteModel.listar(self.año_escolar['id'])

            # Definir columnas de la tabla
            columnas = [
                "ID", "Cédula", "Nombres", "Apellidos", "Fecha Nac.",
                "Edad", "Ciudad", "Género", "Dirección", "Tipo Educ.",
                "Grado", "Sección", "Docente", "TallaC",
                "TallaP", "TallaZ", "Estado", "Fecha Ingreso"
            ]

            # Crear modelo base
            model_estudiantes = QStandardItemModel(len(datos), len(columnas))
            model_estudiantes.setHorizontalHeaderLabels(columnas)

            # Poblar modelo con los datos
            for fila, registro in enumerate(datos):
                # Crear items para cada columna
                item_id = QStandardItem(str(registro["id"]))
                item_cedula = QStandardItem(registro["cedula"])
                item_nombres = QStandardItem(registro["nombres"])
                item_apellidos = QStandardItem(registro["apellidos"])
                
                # Formatear fecha de nacimiento
                fecha_nac_str = ""
                if registro["fecha_nac"]:
                    fecha_nac_str = registro["fecha_nac"].strftime("%d-%m-%Y")
                item_fecha = QStandardItem(fecha_nac_str)
                
                item_edad = QStandardItem(str(registro["edad"]))
                item_ciudad = QStandardItem(registro["ciudad"] or "")
                item_genero = QStandardItem(registro["genero"])
                item_direccion = QStandardItem(registro["direccion"] or "")
                item_tipo_edu = QStandardItem(registro["tipo_educacion"])
                item_grado = QStandardItem(registro["grado"])
                item_seccion = QStandardItem(registro["seccion"])
                item_docente = QStandardItem(registro["docente"] or "")
                item_tallaC = QStandardItem(registro["tallaC"] or "")
                item_tallaP = QStandardItem(registro["tallaP"] or "")
                item_tallaZ = QStandardItem(registro["tallaZ"] or "")
                item_estado = QStandardItem(registro["estado"])
                
                # Formatear fecha de ingreso
                fecha_ing_str = ""
                if registro["fecha_ingreso"]:
                    fecha_ing_str = registro["fecha_ingreso"].strftime("%d-%m-%Y")
                item_fecha_ing = QStandardItem(fecha_ing_str)

                # Lista de items en orden
                items = [
                    item_id, item_cedula, item_nombres, item_apellidos, item_fecha,
                    item_edad, item_ciudad, item_genero, item_direccion, item_tipo_edu,
                    item_grado, item_seccion, item_docente, item_tallaC,
                    item_tallaP, item_tallaZ, item_estado, item_fecha_ing
                ]

                # Agregar items al modelo (no editables)
                for col, item in enumerate(items):
                    item.setEditable(False)
                    model_estudiantes.setItem(fila, col, item)

            # Asignar modelo al proxy
            self.proxy_estudiantes.setSourceModel(model_estudiantes)

            # Configurar delegate personalizado para colores y formato
            delegate = EstudianteDelegate(self.tableW_students)
            self.tableW_students.setItemDelegate(delegate)

            # Configurar tabla
            self.tableW_students.setSortingEnabled(True)
            self.tableW_students.setAlternatingRowColors(True)
            self.tableW_students.setColumnHidden(0, True)  # Ocultar columna ID

            # Numeración vertical (filas)
            row_count = self.proxy_estudiantes.rowCount()
            for fila in range(row_count):
                self.proxy_estudiantes.setHeaderData(
                    fila, Qt.Vertical, str(fila + 1), Qt.DisplayRole
                )

        except Exception as err:
            print(f"Error en database_estudiantes: {err}")
            crear_msgbox(
                self,
                "Error al cargar datos",
                f"No se pudieron cargar los estudiantes:\n{err}",
                QMessageBox.Critical
            ).exec()
    
    def _obtener_id_estudiante_seleccionado(self):
        """Obtiene el ID del estudiante seleccionado en la tabla."""
        index = self.tableW_students.currentIndex()
        if not index.isValid():
            return None

        # Mapear al modelo base (pasando por el proxy)
        proxy = self.tableW_students.model()
        source_index = proxy.mapToSource(index)
        fila = source_index.row()

        # Obtener ID de la columna 0 (oculta)
        model = proxy.sourceModel()
        id_estudiante = int(model.item(fila, 0).text())
        
        return id_estudiante
    
    def obtener_estudiante_seleccionado(self):
        """Obtiene todos los datos del estudiante seleccionado."""
        index = self.tableW_students.currentIndex()
        if not index.isValid():
            return None

        # Obtener el proxy y mapear al modelo base
        proxy = self.tableW_students.model()
        source_index = proxy.mapToSource(index)
        fila = source_index.row()

        # Extraer datos de todas las columnas
        model = proxy.sourceModel()
        datos = {}
        
        for col in range(model.columnCount()):
            header = model.headerData(col, Qt.Horizontal)
            item = model.item(fila, col)
            valor = item.text() if item else ""
            datos[header] = valor
        
        return datos
    
    def filtrar_tabla_estudiantes(self, texto):
        """Filtra la tabla según el texto y campo seleccionado."""
        if not hasattr(self, "proxy_estudiantes"):
            return

        # Mapa entre índice del combo y columna real del modelo
        mapa_columnas = {
            0: -1,   # Todos los campos
            1: 1,    # Cédula
            2: 2,    # Nombres
            3: 3,    # Apellidos
            4: 4,    # Fecha Nac.
            5: 5,    # Edad
            6: 6,    # Ciudad
            7: 7,    # Género
            8: 8,    # Dirección
            9: 9,    # Tipo Educ.
            10: 10,  # Grado
            11: 11,  # Sección
            12: 12,  # Docente
            13: 13,  # TallaC
            14: 14,  # TallaP
            15: 15,  # TallaZ
            16: 17   # Fecha Ingreso (columna 16 es Estado, manejada por proxy)
        }

        # Obtener columna seleccionada en el combo
        idx_combo = self.cbxFiltro_estu.currentIndex()
        columna_real = mapa_columnas.get(idx_combo, -1)

        # Aplicar filtro al proxy
        self.proxy_estudiantes.setFilterKeyColumn(columna_real)
        self.proxy_estudiantes.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.proxy_estudiantes.setFilterRegularExpression(texto)
    
    def obtener_datos_tableview(self, view):
        """Extrae encabezados y filas visibles de un QTableView."""
        model = view.model()
        
        # Extraer encabezados
        encabezados = [
            model.headerData(c, Qt.Horizontal) 
            for c in range(model.columnCount())
        ]
        
        # Extraer filas visibles
        filas = []
        for r in range(model.rowCount()):
            fila = []
            for c in range(model.columnCount()):
                index = model.index(r, c)
                val = model.data(index, Qt.ItemDataRole.DisplayRole)
                fila.append("" if val is None else str(val))
            filas.append(fila)
        
        return encabezados, filas


    def _exportar_constancia_generica(self, funcion_generadora, nombre_constancia):
        """Función genérica para exportar constancias de estudiantes."""
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
            # Obtener datos de la institución
            institucion = InstitucionModel.obtener_por_id(1)
            
            # Generar la constancia
            archivo = funcion_generadora(estudiante, institucion, self.año_escolar)
            
            crear_msgbox(
                self,
                "Éxito",
                f"{nombre_constancia} generada correctamente:\n{archivo}",
                QMessageBox.Information
            ).exec()
            
            # Abrir el archivo
            abrir_archivo(archivo)
            
        except Exception as e:
            crear_msgbox(
                self,
                "Error",
                f"No se pudo generar {nombre_constancia.lower()}:\n{e}",
                QMessageBox.Critical
            ).exec()

    def exportar_constancia_estudios(self):
        """Genera constancia de estudios del estudiante seleccionado"""
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
            # Obtener datos de la institución
            institucion = InstitucionModel.obtener_por_id(1)
            
            # Generar la constancia
            archivo = generar_constancia_estudios(estudiante, institucion)
            
            crear_msgbox(
                self,
                "Éxito",
                f"Constancia de estudios generada correctamente:\n{archivo}",
                QMessageBox.Information
            ).exec()
            
            # Abrir el archivo
            abrir_archivo(archivo)
            
        except Exception as e:
            crear_msgbox(
                self,
                "Error",
                f"No se pudo generar constancia de estudios:\n{e}",
                QMessageBox.Critical
            ).exec()

    def exportar_constancia_inscripcion(self):
        """Genera constancia de inscripción del estudiante seleccionado"""
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
            # Obtener datos de la institución
            institucion = InstitucionModel.obtener_por_id(1)
            
            # Generar la constancia
            archivo = generar_constancia_inscripcion(estudiante, institucion)
            
            crear_msgbox(
                self,
                "Éxito",
                f"Constancia de inscripción generada correctamente:\n{archivo}",
                QMessageBox.Information
            ).exec()
            
            # Abrir el archivo
            abrir_archivo(archivo)
            
        except Exception as e:
            crear_msgbox(
                self,
                "Error",
                f"No se pudo generar constancia de inscripción:\n{e}",
                QMessageBox.Critical
            ).exec()
    
    def exportar_buena_conducta(self):
        """Genera constancia de buena conducta del estudiante seleccionado"""
        self._exportar_constancia_generica(
            generar_buena_conducta,
            "Constancia de buena conducta"
        )

    def exportar_excel_estudiantes(self):
        """Exporta la tabla filtrada actual a Excel"""
        try:
            # Verificar que haya datos
            if self.proxy_estudiantes.rowCount() == 0:
                crear_msgbox(
                    self,
                    "Tabla vacía",
                    "No hay datos para exportar. La tabla está vacía o filtrada completamente.",
                    QMessageBox.Warning
                ).exec()
                return
            
            # Obtener encabezados y filas desde la tabla
            encabezados, filas = self.obtener_datos_tableview(self.tableW_students)

            # Preguntar ubicación al usuario
            ruta, _ = QFileDialog.getSaveFileName(
                self,
                "Guardar reporte",
                f"estudiantes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                "Archivos Excel (*.xlsx)"
            )
            
            if not ruta:
                return  # Usuario canceló
            
            if not ruta.endswith(".xlsx"):
                ruta += ".xlsx"

            # Exportar usando helper de exportar.py
            archivo = exportar_tabla_excel(ruta, encabezados, filas)

            # Avisar y abrir
            crear_msgbox(
                self,
                "Éxito",
                f"Tabla exportada correctamente:\n{archivo}",
                QMessageBox.Information,
            ).exec()
            
            abrir_archivo(archivo)
            
        except Exception as e:
            crear_msgbox(
                self,
                "Error",
                f"No se pudo exportar la tabla:\n{e}",
                QMessageBox.Critical,
            ).exec()
    
    def exportar_excel_estudiantes_bd(self):
        """Exporta la matrícula completa (todos los estudiantes activos) a Excel"""
        try:
            # Obtener todos los estudiantes activos de la BD
            estudiantes = EstudianteModel.listar_activos()
            
            if not estudiantes:
                crear_msgbox(
                    self,
                    "Sin datos",
                    "No hay estudiantes activos para exportar.",
                    QMessageBox.Warning
                ).exec()
                return
            
            # Exportar usando función especializada
            archivo = exportar_estudiantes_excel(self, estudiantes)
            
            if not archivo:
                return  # Usuario canceló
            
            crear_msgbox(
                self,
                "Éxito",
                f"Matrícula completa exportada:\n{archivo}\n\n"
                f"Total de estudiantes: {len(estudiantes)}",
                QMessageBox.Information,
            ).exec()
            
            abrir_archivo(archivo)
            
        except Exception as e:
            crear_msgbox(
                self,
                "Error",
                f"No se pudo exportar la matrícula:\n{e}",
                QMessageBox.Critical,
            ).exec()

    def exportar_constancia_prosecucion_inicial(self):
        """Genera constancia de prosecución de inicial a primaria."""
        estudiante = self.obtener_estudiante_seleccionado()
        if not estudiante:
            crear_msgbox(
                self,
                "Selección requerida",
                "Debe seleccionar un estudiante de la tabla.",
                QMessageBox.Warning
            ).exec()
            return

        # Validar que esté en 1er grado
        grado_actual = estudiante.get('Grado', '').strip()
        if grado_actual != "1ero":
            crear_msgbox(
                self,
                "Estudiante no válido",
                "Esta constancia solo se puede generar para estudiantes que actualmente "
                "cursan 1er grado de primaria.\n\n"
                f"El estudiante seleccionado está en: {grado_actual}",
                QMessageBox.Warning
            ).exec()
            return

        try:
            # Obtener ID del estudiante
            id_estudiante = int(estudiante['ID'])
            
            # Obtener historial académico completo
            historial = EstudianteModel.obtener_historial_estudiante(id_estudiante)
            
            if not historial:
                crear_msgbox(
                    self,
                    "Sin historial",
                    "No se encontró historial académico para este estudiante.",
                    QMessageBox.Warning
                ).exec()
                return
            
            # Buscar si cursó 3er nivel de inicial el año anterior
            año_anterior = self.año_escolar['año_inicio'] - 1
            curso_inicial = False
            
            for registro in historial:
                # Verificar que sea 3er nivel de inicial
                grado = registro['grado'].lower().strip()
                nivel = registro['nivel'].lower().strip()
                año_historial = registro['año_inicio']
                
                # Validar: 3er nivel + año anterior + nivel inicial/preescolar
                if (nivel in ['inicial', 'preescolar'] and 
                    '3' in grado and 
                    año_historial == año_anterior):
                    curso_inicial = True
                    break
            
            if not curso_inicial:
                crear_msgbox(
                    self,
                    "No elegible",
                    f"Este estudiante no cursó 3er nivel de educación inicial "
                    f"en esta institución durante el año escolar {año_anterior}-{año_anterior+1}.\n\n"
                    "Esta constancia solo puede generarse para estudiantes promovidos "
                    "desde inicial en esta misma institución.",
                    QMessageBox.Warning
                ).exec()
                return

            # Si pasa todas las validaciones, generar la constancia
            institucion = InstitucionModel.obtener_por_id(1)
            
            año_escolar_inicial = {
                'año_inicio': año_anterior,
                'año_fin': año_anterior + 1
            }
            
            archivo = generar_constancia_prosecucion_inicial(
                estudiante, 
                institucion, 
                año_escolar_inicial
            )
            
            crear_msgbox(
                self,
                "Éxito",
                f"Constancia de prosecución generada correctamente:\n{archivo}",
                QMessageBox.Information
            ).exec()
            
            # Abrir el archivo
            abrir_archivo(archivo)
            
        except Exception as e:
            crear_msgbox(
                self,
                "Error",
                f"No se pudo generar la constancia:\n{e}",
                QMessageBox.Critical
            ).exec()
