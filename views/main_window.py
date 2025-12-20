from PySide6.QtWidgets import (
    QMainWindow, QToolButton, QMenu, QGraphicsDropShadowEffect, QMessageBox,
    QSizePolicy, QLabel
)
from PySide6.QtCore import QTimer, Qt, QSortFilterProxyModel
from PySide6.QtGui import QColor, QStandardItem, QStandardItemModel, QAction, QPalette

from paths import ICON_DIR
from models.dashboard_model import DashboardModel
from utils.exportar import exportar_reporte_pdf

import os

from views.delegates import UsuarioDelegate
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from utils.reportes_config import CriteriosReportes, criterios_por_poblacion
from views.registro_usuario import RegistroUsuario
from models.user_model import UsuarioModel
from views.actualizar_usuario import ActualizarUsuario
from models.auditoria_model import AuditoriaModel
from utils.forms import set_campos_editables, ajustar_columnas_tabla
from models.institucion_model import InstitucionModel
from models.anio_model import AnioEscolarModel
from ui_compiled.main_ui import Ui_MainWindow
from views.gestion_estudiantes import GestionEstudiantesPage
from views.gestion_empleados import GestionEmpleadosPage
from views.gestion_secciones import GestionSeccionesPage
from views.gestion_anio import GestionAniosPage
from views.egresados import Egresados
from utils.dialogs import crear_msgbox
from utils.sombras import crear_sombra_flotante


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, usuario_actual, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.año_escolar = AnioEscolarModel.obtener_actual()

        self.setWindowTitle("SIRA - Sistema Interno de Registro Académico")
        self.usuario_actual = usuario_actual
        self.logout = False
        
        # Inicializar lista de delegates para tooltips
        self.tooltip_delegates = []
        
        self.configurar_permisos()
        self.lblBienvenida.setText(f"Bienvenido, {self.usuario_actual['username']}!")
        self.btnUsuario_home.setText(f"{self.usuario_actual['username']}")
        self.lblAnio_escolar_main.setText(f"Año escolar: {self.año_escolar['nombre']}")

        # Obtener el widget vacío que está en el índice del stack
        placeholder_1 = self.stackMain.widget(1)
        placeholder_2 = self.stackMain.widget(2)
        placeholder_3 = self.stackMain.widget(3)
        placeholder_4 = self.stackMain.widget(4)
        placeholder_9 = self.stackMain.widget(9)

        # Crear páginas
        self.page_gestion_estudiantes = GestionEstudiantesPage(self.usuario_actual, self.año_escolar, self)
        self.page_gestion_secciones = GestionSeccionesPage(self.usuario_actual, self.año_escolar, self)
        self.page_egresados = Egresados(self.usuario_actual, self.año_escolar, self)
        self.page_gestion_empleados = GestionEmpleadosPage(self.usuario_actual, self)
        self.page_gestion_anios = GestionAniosPage(self.usuario_actual, self)

        # Reemplazar el placeholder por la página
        self.stackMain.removeWidget(placeholder_1)
        self.stackMain.removeWidget(placeholder_2)
        self.stackMain.removeWidget(placeholder_3)
        self.stackMain.removeWidget(placeholder_4)
        self.stackMain.removeWidget(placeholder_9)
        self.stackMain.insertWidget(1, self.page_gestion_estudiantes)
        self.stackMain.insertWidget(2, self.page_gestion_secciones)
        self.stackMain.insertWidget(3, self.page_egresados)
        self.stackMain.insertWidget(4, self.page_gestion_empleados)
        self.stackMain.insertWidget(9, self.page_gestion_anios)

        # Configurar un único timer
        self.timer_global = QTimer(self)
        self.timer_global.timeout.connect(self.actualizar_dashboard)
        # self.timer_global.timeout.connect(self.database_usuarios)
        # self.timer_global.timeout.connect(self.database_estudiantes)
        # self.timer_global.timeout.connect(self.database_empleados)
        self.timer_global.timeout.connect(self.cargar_auditoria)
        self.timer_global.start(10000)  # cada 10 segundos
        self.actualizar_dashboard()

        self.stackBarra_lateral.setCurrentIndex(0)
        self.stackMain.setCurrentIndex(0)

        self.aplicar_sombra(self.frMatricula_home)
        self.aplicar_sombra(self.frRepresentantes_home)
        self.aplicar_sombra(self.frTrabajadores_home)
        self.aplicar_sombra(self.frSeccion_home)

        ## Botones barra lateral ##
        self.btnHome.clicked.connect(lambda: self.cambiar_pagina_main(0))
        self.btnEstudiantes.clicked.connect(lambda: self.cambiar_pagina_barra_lateral(1))
        self.btnGestion_estudiantes.clicked.connect(lambda: self.cambiar_pagina_main(1))
        self.btnSecciones.clicked.connect(lambda: self.cambiar_pagina_main(2))
        self.btnEgresados.clicked.connect(lambda: self.cambiar_pagina_main(3))
        self.btnEmpleados.clicked.connect(lambda: self.cambiar_pagina_main(4))
        self.btnReportes.clicked.connect(lambda: self.cambiar_pagina_main(5))
        self.btnAdmin.clicked.connect(lambda: self.cambiar_pagina_barra_lateral(2))
        self.btnRegresar_estudiantes.clicked.connect(lambda: self.cambiar_pagina_barra_lateral(0))
        self.btnRegresar_admin.clicked.connect(lambda: self.cambiar_pagina_barra_lateral(0))
        
        menu_usuario = QMenu(self)
        accion_cerrar = QAction("Cerrar sesión", self)
        accion_cerrar.triggered.connect(self.cerrar_sesion)
        menu_usuario.addAction(accion_cerrar)
        self.btnUsuario_home.setMenu(menu_usuario)
        self.btnUsuario_home.setPopupMode(QToolButton.InstantPopup)  # abre el menú al hacer clic

        ## MODULO REPORTES ##
        self.ultima_consulta = ([], [])
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.canvas.updateGeometry()
        self.frGrafica_reportes.layout().addWidget(self.canvas)
        self.cbxPoblacion.currentIndexChanged.connect(self.actualizar_criterios)
        self.cbxCriterio.currentIndexChanged.connect(self.on_criterio_changed)
        self.btnGenerarGrafica.clicked.connect(self.actualizar_reporte)
        self.btnExportar_reporte.clicked.connect(self.on_exportar_reporte)
        ## Sombras de elementos MODULO REPORTES ##
        crear_sombra_flotante(self.btnGenerarGrafica)
        crear_sombra_flotante(self.btnExportar_reporte)
        crear_sombra_flotante(self.frameCriterio, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.framePoblacion, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.frameTipoGrafica, blur_radius=8, y_offset=1)

        # Estado inicial
        self.lblMin.setVisible(False)
        self.lblMax.setVisible(False)
        self.spnMin.setVisible(False)
        self.spnMax.setVisible(False)

        self.cbxCriterio.setEnabled(False)
        self.cbxTipoGrafica.setEnabled(False)

        ## Botones Admin ##
        #--Gestion Usuarios--#
        self.btnGestion_usuarios.clicked.connect(lambda: self.cambiar_pagina_main(6))
        self.database_usuarios()
        self.btnCrear_usuario.clicked.connect(self.registro_usuario)
        self.btnActualizar_usuario.clicked.connect(self.actualizar_usuario)
        self.btnDisable_usuario.clicked.connect(self.cambiar_estado_usuario)
        ## Sombras de elementos Gestion Usuarios ##
        crear_sombra_flotante(self.btnCrear_usuario)
        crear_sombra_flotante(self.btnActualizar_usuario)
        crear_sombra_flotante(self.btnDisable_usuario)
        
        # Conectar el checkbox para actualizar la tabla
        self.chkMostrar_inactivos_user.stateChanged.connect(self.database_usuarios)
        
        #--Auditoria--#
        self.btnAuditoria.clicked.connect(lambda: self.cambiar_pagina_main(7))
        self.cargar_auditoria()
        
        #--Datos Institucionales--#
        self.btnDatos_institucion.clicked.connect(lambda: self.cambiar_pagina_main(8))
        self.set_campos_editables(False)
        self.cargar_datos_institucion()
        self.btnModificar_institucion.clicked.connect(self.toggle_edicion)
        crear_sombra_flotante(self.btnModificar_institucion)

        #--Años escolares--#
        self.btnAnio_escolar.clicked.connect(lambda: self.cambiar_pagina_main(9))
        
        #--Copia seguridad--#
        self.btnCopia_seguridad.clicked.connect(lambda: self.cambiar_pagina_main(10))
           
    def configurar_permisos(self):
        rol = self.usuario_actual["rol"]
        if rol in ("super_admin", "admin"):
            self.btnAdmin.setVisible(True)
        else:
            self.btnAdmin.setVisible(False)

    def actualizar_dashboard(self):
        try:
            self.lblMatricula_home.setText(str(DashboardModel.total_estudiantes_activos()))
            self.lblRepresentantes_home.setText(str(DashboardModel.total_representantes()))
            self.lblEmpleados_home.setText(str(DashboardModel.total_empleados_activos()))

            resultado = DashboardModel.seccion_mas_numerosa()
            if resultado:
                grado = resultado["grado"]
                letra = resultado["letra"]
                total = resultado["total"]
                self.lblSeccion_home.setText(f"{grado} {letra} ({total})")
            else:
                self.lblSeccion_home.setText("Sin datos")
            ##Modulo estudiantes:
            self.page_gestion_estudiantes.actualizar_conteo()
            ##Modulo empleados:
            self.page_gestion_empleados.actualizar_conteo()

        except Exception as err:
            print(f"Error en dashboard: {err}")

    def aplicar_sombra(self, widget):
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(12) # difuminado
        sombra.setXOffset(0) # desplazamiento H
        sombra.setYOffset(2) # desplazamiento V
        sombra.setColor(QColor(0, 0, 0, 50)) # negro con transparencia
        widget.setGraphicsEffect(sombra)

    def cambiar_pagina_main(self, indice):
        self.stackMain.setCurrentIndexFade(indice)
    def cambiar_pagina_barra_lateral(self, indice):
        self.stackBarra_lateral.setCurrentIndexSlide(indice)
    
    ### MODULO REPORTES ###

    def actualizar_criterios(self):
        poblacion = self.cbxPoblacion.currentText()

        # Limpiar y agregar placeholder
        self.cbxCriterio.clear()
        self.cbxCriterio.addItem("Seleccione un criterio")
        # deshabilitar el placeholder para que no se pueda seleccionar desde el menú
        model = self.cbxCriterio.model()
        item0 = model.item(0)
        if item0 is not None:
            item0.setEnabled(False)
            item0.setForeground(Qt.GlobalColor.gray)

        # Cargar criterios si hay población válida
        if poblacion in criterios_por_poblacion:
            self.cbxCriterio.addItems(criterios_por_poblacion[poblacion])
            self.cbxCriterio.setEnabled(True)
            # Mantener el placeholder como selección inicial
            self.cbxCriterio.setCurrentIndex(0)
        else:
            self.cbxCriterio.setEnabled(False)

        # Ocultar controles extra
        self.lblMin.setVisible(False)
        self.lblMax.setVisible(False)
        self.spnMin.setVisible(False)
        self.spnMax.setVisible(False)

        # Bloquear tipo de gráfica hasta que el criterio sea válido (>0)
        self.cbxTipoGrafica.setEnabled(False)


    def on_criterio_changed(self):
        idx = self.cbxCriterio.currentIndex()
        criterio = self.cbxCriterio.currentText() if idx > 0 else ""  # vacío si es placeholder

        # Mostrar/ocultar controles por criterio
        if criterio == "Rango de edad":
            self.lblMin.setText("Edad mínima")
            self.lblMax.setText("Edad máxima")
            self.lblMin.setVisible(True); self.lblMax.setVisible(True)
            self.spnMin.setVisible(True); self.spnMax.setVisible(True)
            self.spnMin.setEnabled(True); self.spnMax.setEnabled(True)

        elif criterio == "Rango de salario":
            self.lblMin.setText("Salario mínimo")
            self.lblMax.setText("Salario máximo")
            self.lblMin.setVisible(True); self.lblMax.setVisible(True)
            self.spnMin.setVisible(True); self.spnMax.setVisible(True)
            self.spnMin.setEnabled(True); self.spnMax.setEnabled(True)

        else:
            self.lblMin.setVisible(False); self.lblMax.setVisible(False)
            self.spnMin.setVisible(False); self.spnMax.setVisible(False)
            self.spnMin.setEnabled(False); self.spnMax.setEnabled(False)

        # Configurar tipos de gráfica según validez del criterio
        if idx > 0:  # criterio válido (no placeholder)
            self.actualizar_tipos_grafica()
        else:
            self.cbxTipoGrafica.clear()
            self.cbxTipoGrafica.setEnabled(False)

    def actualizar_tipos_grafica(self):
        self.cbxTipoGrafica.clear()
        self.cbxTipoGrafica.addItem("Seleccione un tipo de gráfica")
        model = self.cbxTipoGrafica.model()
        item0 = model.item(0)
        if item0 is not None:
            item0.setEnabled(False)
            item0.setForeground(Qt.GlobalColor.gray)

        # Cargar tipos de gráfica
        tipos = list(CriteriosReportes.GRAFICAS.keys())
        self.cbxTipoGrafica.addItems(tipos)
        self.cbxTipoGrafica.setEnabled(True)
        self.cbxTipoGrafica.setCurrentIndex(0)


    def actualizar_reporte(self):
        poblacion = self.cbxPoblacion.currentText()
        idx_criterio = self.cbxCriterio.currentIndex()
        idx_tipo = self.cbxTipoGrafica.currentIndex()

        # Evitar placeholder o vacío
        if not poblacion or idx_criterio <= 0 or idx_tipo <= 0:
            self.figure.clear()
            self.canvas.draw()
            return

        criterio = self.cbxCriterio.currentText()
        tipo = self.cbxTipoGrafica.currentText()

        consulta_info = CriteriosReportes.CONSULTAS.get((poblacion, criterio))
        grafica = CriteriosReportes.GRAFICAS.get(tipo)

        self.figure.clear()
        ax = self.figure.add_subplot(111)

        etiquetas = []; valores = []
        if consulta_info and grafica:
            consulta, params = consulta_info
            args = []
            titulo = f"{criterio} ({poblacion})"

            if "edad_min" in params and "edad_max" in params:
                args = [self.spnMin.value(), self.spnMax.value()]
                titulo += f" {args[0]}-{args[1]} años"

            elif "salario_min" in params and "salario_max" in params:
                args = [self.spnMin.value(), self.spnMax.value()]
                titulo += f" {args[0]}-{args[1]}"

            etiquetas, valores = consulta(*args)
            self.ultima_consulta = (etiquetas, valores)
            grafica(ax, etiquetas, valores, titulo)
        else:
            ax.axis("off")
            ax.text(0.5, 0.5, "Combinación no soportada", ha="center", va="center", fontsize=12)

        self.canvas.draw()
        if etiquetas and valores:
            self.actualizar_resumen(etiquetas, valores)
        else:
            self.lblResumen_grafica.setText("")  # limpiar si no hay datos
   
    def on_exportar_reporte(self):
        poblacion = self.cbxPoblacion.currentText()
        idx_criterio = self.cbxCriterio.currentIndex()
        idx_tipo = self.cbxTipoGrafica.currentIndex()
        if not poblacion or idx_criterio <= 0 or idx_tipo <= 0 or not hasattr(self, "ultima_consulta"):
            return  # no exportar si no hay selección válida o datos

        criterio = self.cbxCriterio.currentText()
        tipo = self.cbxTipoGrafica.currentText()
        etiquetas, valores = self.ultima_consulta
        total = sum(valores)
        titulo = f"{criterio} ({poblacion}) - {tipo}"

        exportar_reporte_pdf(self, self.figure, titulo, criterio, etiquetas, valores, total)

    def actualizar_resumen(self, etiquetas, valores):
        total = sum(valores)
        n = len(valores)
        max_val = max(valores) if valores else 0
        min_val = min(valores) if valores else 0
        cat_max = etiquetas[valores.index(max_val)] if valores else "-"
        cat_min = etiquetas[valores.index(min_val)] if valores else "-"

        resumen = (
            f"<b>Resumen numérico</b><br>"
            f"Total de registros: {total}<br>"
            f"Número de categorías: {n}<br>"
            f"Máximo: {cat_max} ({max_val})<br>"
            f"Mínimo: {cat_min} ({min_val})"
        )
        self.lblResumen_grafica.setText(resumen)
    
    ### MODULO ADMIN ###
    
    def registro_usuario(self):
        ventana = RegistroUsuario(self.usuario_actual, self)
        ventana.exec() 
    
    def actualizar_usuario(self):
        # Obtener el índice seleccionado en la vista
        index = self.tableW_usuarios.currentIndex()
        if index.isValid():
            # Convertir al índice del modelo base (porque usamos proxy para ordenar/filtrar)
            index_source = self.tableW_usuarios.model().mapToSource(index)
            fila = index_source.row()

            # Obtener el ID desde la columna 0 del modelo base
            model = index_source.model()
            id_usuario = int(model.item(fila, 0).text())

            # Abrir la ventana de actualizacion
            ventana = ActualizarUsuario(id_usuario, self.usuario_actual, self)  # ya no pasamos self.conexion
            ventana.datos_actualizados.connect(self.database_usuarios)  # refresca tabla al emitirse
            ventana.exec()
    
    def cambiar_estado_usuario(self):
        # Obtener índice seleccionado
        index = self.tableW_usuarios.currentIndex()
        if not index.isValid():
            msg = crear_msgbox(
                self,
                "Cambiar estado",
                "Seleccione un usuario primero.",
                QMessageBox.Warning,
            )
            msg.exec()
            return

        # Mapear al modelo base
        index_source = self.tableW_usuarios.model().mapToSource(index)
        fila = index_source.row()
        model = index_source.model()

        # ID del usuario (columna 0)
        id_usuario = int(model.item(fila, 0).text())
        username = model.item(fila, 1).text()        
        estado_actual_texto = model.item(fila, 3).text()   

        # Convertir a booleano
        estado_actual = 1 if estado_actual_texto.lower() == "activo" else 0

        # Determinar nuevo estado
        nuevo_estado = 0 if estado_actual == 1 else 1
        nuevo_estado_texto = "Activo" if nuevo_estado == 1 else "Inactivo"

        # Confirmación
        reply = crear_msgbox(
            self,
            "Confirmar cambio de estado",
            f"¿Está seguro de cambiar el estado del usuario '{username}' "
            f"de {estado_actual_texto} a {nuevo_estado_texto}?",
            QMessageBox.Question,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply.exec() != QMessageBox.StandardButton.Yes:
            return

        try:
            ok, mensaje = UsuarioModel.cambiar_estado(id_usuario, nuevo_estado, self.usuario_actual)

            if ok:
                msg = crear_msgbox(
                    self,
                    "Éxito",
                    mensaje,
                    QMessageBox.Information   # icono
                )
                msg.exec()
                self.database_usuarios()  # refrescar tabla
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
                    QMessageBox.Critical   # icono
                )
            msg.exec()
            

    def database_usuarios(self):
        
            try:
                datos = UsuarioModel.listar() 
                columnas = [
                    "ID", "Usuario", "Rol", "Estado", "Nombre Completo",
                    "Fecha de creación", "Ultima actualización"
                ]

                # Crear modelo base
                model = QStandardItemModel(len(datos), len(columnas))
                model.setHorizontalHeaderLabels(columnas)

                # Poblar modelo
                for fila, registro in enumerate(datos):
                    for col, valor in enumerate(registro):
                        item = QStandardItem(str(valor))
                        item.setEditable(False)
                        model.setItem(fila, col, item)

                # Proxy
                self.proxy_usuarios = QSortFilterProxyModel(self)
                self.proxy_usuarios.setSourceModel(model)
                self.proxy_usuarios.setSortCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
                self.proxy_usuarios.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)

                if hasattr(self, 'chkMostrar_inactivos_user') and not self.chkMostrar_inactivos_user.isChecked():
                    self.proxy_usuarios.setFilterRegularExpression("^Activo$")
                    self.proxy_usuarios.setFilterKeyColumn(3)

                delegate = UsuarioDelegate(self.tableW_usuarios)
                self.tableW_usuarios.setItemDelegate(delegate)

                self.tableW_usuarios.setModel(self.proxy_usuarios)
                self.tableW_usuarios.setSortingEnabled(True)
                self.tableW_usuarios.setAlternatingRowColors(True)
                self.tableW_usuarios.setColumnHidden(0, True)

                # Numeración vertical
                row_count = self.proxy_usuarios.rowCount()
                for fila in range(row_count):
                    self.proxy_usuarios.setHeaderData(fila, Qt.Vertical, str(fila + 1))

            except Exception as err:
                print(f"Error en database_usuarios: {err}")
    
    def obtener_usuario_seleccionado(self):
        index = self.tableW_usuarios.currentIndex()
        if not index.isValid():
            return None

        # Obtener el proxy de la tabla
        proxy = self.tableW_usuarios.model()
        source_index = proxy.mapToSource(index)
        fila = source_index.row()

        model = proxy.sourceModel()
        datos = {}
        for col in range(model.columnCount()):
            header = model.headerData(col, Qt.Horizontal)
            valor = model.item(fila, col).text()
            datos[header] = valor
        return datos
    
    def filtrar_tabla_usuarios(self, texto):
        if hasattr(self, "proxy_usuarios"):
            self.proxy_usuarios.setFilterKeyColumn(-1)
            self.proxy_usuarios.setFilterRegularExpression(texto)
    
    ### MODULO AUDITORIA ###
    def cargar_auditoria(self, limit=50):
        try:
            datos = AuditoriaModel.listar(limit)
            columnas = ["ID", "Usuario", "Acción", "Entidad", "Entidad ID", "Referencia", "Descripción", "Fecha"]

            model = QStandardItemModel(len(datos), len(columnas))
            model.setHorizontalHeaderLabels(columnas)

            for fila, registro in enumerate(datos):
                model.setItem(fila, 0, QStandardItem(str(registro["id"])))
                model.setItem(fila, 1, QStandardItem(registro["usuario"]))
                model.setItem(fila, 2, QStandardItem(registro["accion"]))
                model.setItem(fila, 3, QStandardItem(registro["entidad"]))
                model.setItem(fila, 4, QStandardItem(str(registro["entidad_id"])))
                model.setItem(fila, 5, QStandardItem(registro["referencia"] or ""))
                model.setItem(fila, 6, QStandardItem(registro["descripcion"] or ""))
                model.setItem(fila, 7, QStandardItem(str(registro["fecha"])))

            self.tableW_auditoria.setModel(model)
            self.tableW_auditoria.setSortingEnabled(True)
            self.tableW_auditoria.setAlternatingRowColors(True)

            # Definir anchos personalizados para cada columna
            anchos_auditoria = {
                0: 50,   # ID
                1: 120,  # Usuario
                2: 100,  # Acción
                3: 120,  # Entidad
                4: 80,   # Entidad ID
                5: 150,  # Referencia
                6: 300,  # Descripción (más ancho)
                7: 150   # Fecha
            }
            
            # Usar la función importada
            ajustar_columnas_tabla(self, self.tableW_auditoria, anchos_auditoria)

        except Exception as err:
            msg = crear_msgbox(
                self,
                "Error",
                f"No se pudo cargar la auditoría: {err}",
                QMessageBox.Critical
            )
            msg.exec()
    
    def closeEvent(self, event):
        """Limpiar tooltips al cerrar la ventana."""
        for delegate in self.tooltip_delegates:
            if hasattr(delegate, 'close_tooltip'):
                delegate.close_tooltip()
        super().closeEvent(event)
    
    ## DATOS INSTITUCION ##
    def set_campos_editables(self, estado: bool):
        campos = [
            self.lneNombreInstitucion_admin, self.lneCodigoDEA_admin, self.lneCodigoDEP_admin, self.lneCodigoEST_admin,
            self.lneRIF_admin, self.lneDirInstitucion_admin, self.lneTlfInstitucion_admin, self.lneCorreoInstitucion_admin,
            self.lneDirector_institucion, self.lneCedula_director_institucion
        ]
        campos_solo_lectura = [self.lneUltimaActualizacion_admin]
        set_campos_editables(campos, estado, campos_solo_lectura)

    def cargar_datos_institucion(self):
        try:
            datos = InstitucionModel.obtener_por_id(1)
            if datos:
                self.lneNombreInstitucion_admin.setText(str(datos["nombre"]))
                self.lneCodigoDEA_admin.setText(str(datos["codigo_dea"]))
                self.lneCodigoDEP_admin.setText(str(datos["codigo_dependencia"]))
                self.lneCodigoEST_admin.setText(str(datos["codigo_estadistico"]))
                self.lneRIF_admin.setText(str(datos["rif"]))
                self.lneDirInstitucion_admin.setText(str(datos["direccion"]))
                self.lneTlfInstitucion_admin.setText(str(datos["telefono"]))
                self.lneCorreoInstitucion_admin.setText(str(datos["correo"]))
                self.lneDirector_institucion.setText(str(datos["director"]))
                self.lneCedula_director_institucion.setText(str(datos["director_ci"]))
                self.lneUltimaActualizacion_admin.setText(str(datos["actualizado_en"]))
        except Exception as err:
            msg = crear_msgbox(
                self,
                "Error",
                f"No se pudieron cargar los datos: {err}",
                QMessageBox.Critical,
            )
            msg.exec()

    def guardar_datos_institucion(self):
        try:
            institucion_data = {
                "nombre": self.lneNombreInstitucion_admin.text(),
                "codigo_dea": self.lneCodigoDEA_admin.text(),
                "codigo_dependencia": self.lneCodigoDEP_admin.text(),
                "codigo_estadistico": self.lneCodigoEST_admin.text(),
                "rif": self.lneRIF_admin.text(),
                "direccion": self.lneDirInstitucion_admin.text(),
                "telefono": self.lneTlfInstitucion_admin.text(),
                "correo": self.lneCorreoInstitucion_admin.text(),
                "director": self.lneDirector_institucion.text(),
                "director_ci": self.lneCedula_director_institucion.text(),
            }

            InstitucionModel.actualizar(1, institucion_data, self.usuario_actual)

            msg = crear_msgbox(
                self,
                "Éxito",
                "Datos de la institución actualizados correctamente.",
                QMessageBox.Information,
            )
            msg.exec()
            self.cargar_datos_institucion()  # refrescar

        except Exception as err:
            msg = crear_msgbox(
                self,
                "Error",
                f"No se pudo guardar cambios: {err}",
                QMessageBox.Critical,
            )
            msg.exec()

    def toggle_edicion(self):
        if self.btnModificar_institucion.text() == "Modificar datos":
            self.set_campos_editables(True)
            self.btnModificar_institucion.setText("Guardar")
        else:
            self.guardar_datos_institucion()
            self.set_campos_editables(False)
            self.btnModificar_institucion.setText("Modificar datos")
   
    def cerrar_sesion(self):
        
        # Cierra la ventana actual
        self.logout = True
        self.close()
        
        # Abre la ventana de login
        #self.login = LoginDialog()
        #self.login.show()