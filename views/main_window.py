from PySide6.QtWidgets import (
    QMainWindow, QToolButton, QMenu, QGraphicsDropShadowEffect, QMessageBox,
    QSizePolicy, QLabel, QDialog
)
from PySide6.QtCore import QTimer, Qt, QSortFilterProxyModel
from PySide6.QtGui import QColor, QStandardItem, QStandardItemModel, QAction

from models.dashboard_model import DashboardModel
from utils.exportar import exportar_reporte_pdf
from utils.backup import BackupManager

from datetime import datetime, timedelta

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

import subprocess


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, usuario_actual, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.usuario_actual = usuario_actual
        self.logout = False
        
        # Inicializar lista de delegates para tooltips
        self.tooltip_delegates = []
        
        # Cargar año escolar actual
        self.año_escolar = AnioEscolarModel.obtener_actual()
        if not self.año_escolar:
            # Intentar crear año escolar por defecto
            ok, mensaje = AnioEscolarModel.inicializar_si_no_existe()
            if ok:
                self.año_escolar = AnioEscolarModel.obtener_actual()
            else:
                crear_msgbox(
                    self,
                    "Error crítico",
                    f"No se pudo inicializar año escolar: {mensaje}\n\n"
                    "La aplicación puede no funcionar correctamente.",
                    QMessageBox.Critical
                ).exec()
                # Crear año ficticio para evitar crashes
                self.año_escolar = {"id": 0, "nombre": "Sin año escolar"}
        
        self.setWindowTitle("SIRA - Sistema Interno de Registro Académico")
        
        self.configurar_permisos()
        self.lblBienvenida.setText(f"Bienvenido, {self.usuario_actual['username']}!")
        self.btnUsuario_home.setText(f"{self.usuario_actual['username']}")
        self.lblAnio_escolar_main.setText(f"Año escolar: {self.año_escolar['nombre']}")

        # Obtener widgets placeholder
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

        # Reemplazar placeholders
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

        # Configurar timer global (solo actualiza dashboard y auditoría)
        self.timer_global = QTimer(self)
        self.timer_global.timeout.connect(self.actualizar_dashboard)
        self.timer_global.timeout.connect(self.cargar_auditoria)
        self.timer_global.start(10000)  # cada 10 segundos
        self.actualizar_dashboard()
        
        # Configurar timer para backups automáticos (cada 3 días)
        self.timer_backup = QTimer(self)
        self.timer_backup.timeout.connect(self.realizar_backup_automatico)
        # 3 días = 259200000 milisegundos (3 * 24 * 60 * 60 * 1000)
        self.timer_backup.start(259200000)
        # Cargar info del último backup
        self.cargar_info_backup()

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
        self.btnUsuario_home.setPopupMode(QToolButton.InstantPopup)

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
        
        ## Sombras MODULO REPORTES ##
        crear_sombra_flotante(self.btnGenerarGrafica)
        crear_sombra_flotante(self.btnExportar_reporte)
        crear_sombra_flotante(self.frameCriterio, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.framePoblacion, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.frameTipoGrafica, blur_radius=8, y_offset=1)

        # Estado inicial reportes
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
        
        ## Sombras Gestion Usuarios ##
        crear_sombra_flotante(self.btnCrear_usuario)
        crear_sombra_flotante(self.btnActualizar_usuario)
        crear_sombra_flotante(self.btnDisable_usuario)
        
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
        self.btnBackup_manual.clicked.connect(self.realizar_backup_manual)
        crear_sombra_flotante(self.btnBackup_manual)
           
    def configurar_permisos(self):
        """Configura visibilidad de elementos según rol del usuario"""
        rol = self.usuario_actual.get("rol", "")
        if rol in ("admin", "Super admin"):
            self.btnAdmin.setVisible(True)
        else:
            self.btnAdmin.setVisible(False)

    def actualizar_dashboard(self):
        """Actualiza estadísticas del dashboard principal"""
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
            
            # Actualizar conteos en módulos (solo si están cargados)
            if hasattr(self, 'page_gestion_estudiantes'):
                self.page_gestion_estudiantes.actualizar_conteo()
            
            if hasattr(self, 'page_gestion_empleados'):
                self.page_gestion_empleados.actualizar_conteo()

        except Exception as err:
            print(f"Error en dashboard: {err}")

    def actualizar_anio_escolar(self):
        """
        Actualiza el año escolar actual después de aperturar uno nuevo.
        Llamado desde GestionAniosPage después de apertura exitosa.
        """
        try:
            self.año_escolar = AnioEscolarModel.obtener_actual()
            
            if self.año_escolar:
                self.lblAnio_escolar_main.setText(f"Año escolar: {self.año_escolar['nombre']}")
                
                # Actualizar año en páginas hijas
                if hasattr(self, 'page_gestion_estudiantes'):
                    self.page_gestion_estudiantes.año_escolar = self.año_escolar
                    self.page_gestion_estudiantes.database_estudiantes()
                
                if hasattr(self, 'page_gestion_secciones'):
                    self.page_gestion_secciones.año_escolar = self.año_escolar
                    self.page_gestion_secciones.database_secciones()
                
                if hasattr(self, 'page_egresados'):
                    self.page_egresados.año_escolar = self.año_escolar
                
                # Actualizar dashboard
                self.actualizar_dashboard()
                
        except Exception as e:
            print(f"Error actualizando año escolar: {e}")

    def aplicar_sombra(self, widget):
        """Aplica efecto de sombra a un widget"""
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(12)
        sombra.setXOffset(0)
        sombra.setYOffset(2)
        sombra.setColor(QColor(0, 0, 0, 50))
        widget.setGraphicsEffect(sombra)

    def cambiar_pagina_main(self, indice):
        """Cambia la página principal con efecto fade"""
        # Opción 1: Slide rápido 
        #self.stackMain.setCurrentIndexSlide(indice)
        
        # Opción 2: Push suave 
        #self.stackMain.setCurrentIndexPush(indice)
        
        # Opción 3: Sin animación 
        self.stackMain.setCurrentIndexInstant(indice)
        
    def cambiar_pagina_barra_lateral(self, indice):
        """Cambia la página de la barra lateral con efecto slide"""
        self.stackBarra_lateral.setCurrentIndexSlide(indice)
    
    ### MODULO REPORTES ###

    def actualizar_criterios(self):
        """Actualiza los criterios disponibles según la población seleccionada"""
        poblacion = self.cbxPoblacion.currentText()

        # Limpiar y agregar placeholder
        self.cbxCriterio.clear()
        self.cbxCriterio.addItem("Seleccione un criterio")
        model = self.cbxCriterio.model()
        item0 = model.item(0)
        if item0 is not None:
            item0.setEnabled(False)
            item0.setForeground(Qt.GlobalColor.gray)

        # Cargar criterios si hay población válida
        if poblacion in criterios_por_poblacion:
            self.cbxCriterio.addItems(criterios_por_poblacion[poblacion])
            self.cbxCriterio.setEnabled(True)
            self.cbxCriterio.setCurrentIndex(0)
        else:
            self.cbxCriterio.setEnabled(False)

        # Ocultar controles extra y limpiar gráfica
        self.lblMin.setVisible(False)
        self.lblMax.setVisible(False)
        self.spnMin.setVisible(False)
        self.spnMax.setVisible(False)
        self.cbxTipoGrafica.setEnabled(False)
        
        # Limpiar gráfica
        self.figure.clear()
        self.canvas.draw()

    def on_criterio_changed(self):
        """Maneja el cambio de criterio mostrando controles específicos"""
        idx = self.cbxCriterio.currentIndex()
        criterio = self.cbxCriterio.currentText() if idx > 0 else ""

        # Ocultar todos los controles primero
        self.lblMin.setVisible(False)
        self.lblMax.setVisible(False)
        self.spnMin.setVisible(False)
        self.spnMax.setVisible(False)
        
        if hasattr(self, 'cbxSeccion_reporte'):
            self.cbxSeccion_reporte.setVisible(False)
            if hasattr(self, 'frameSeccion_reporte'):
                self.frameSeccion_reporte.setVisible(False)
            if hasattr(self, 'lblSeccion_reporte'):
                self.lblSeccion_reporte.setVisible(False)

        # Mostrar controles según criterio
        if criterio == "Rango de edad":
            self.lblMin.setText("Edad mínima")
            self.lblMax.setText("Edad máxima")
            self.lblMin.setVisible(True)
            self.lblMax.setVisible(True)
            self.spnMin.setVisible(True)
            self.spnMax.setVisible(True)
            self.spnMin.setEnabled(True)
            self.spnMax.setEnabled(True)
            self.spnMin.setMinimum(0)
            self.spnMin.setMaximum(100)
            self.spnMax.setMinimum(0)
            self.spnMax.setMaximum(100)
            self.spnMin.setValue(3)
            self.spnMax.setValue(18)

        elif criterio == "Rango de salario":
            self.lblMin.setText("Salario mínimo")
            self.lblMax.setText("Salario máximo")
            self.lblMin.setVisible(True)
            self.lblMax.setVisible(True)
            self.spnMin.setVisible(True)
            self.spnMax.setVisible(True)
            self.spnMin.setEnabled(True)
            self.spnMax.setEnabled(True)
            self.spnMin.setMinimum(0)
            self.spnMin.setMaximum(999999)
            self.spnMax.setMinimum(0)
            self.spnMax.setMaximum(999999)
            self.spnMin.setValue(100)
            self.spnMax.setValue(5000)

        elif criterio == "Matricula por año escolar":
            self.lblMin.setText("Año inicio")
            self.lblMax.setText("Año fin")
            self.lblMin.setVisible(True)
            self.lblMax.setVisible(True)
            self.spnMin.setVisible(True)
            self.spnMax.setVisible(True)
            self.spnMin.setEnabled(True)
            self.spnMax.setEnabled(True)
            self.spnMin.setMinimum(2000)
            self.spnMin.setMaximum(2100)
            self.spnMax.setMinimum(2000)
            self.spnMax.setMaximum(2100)
            año_actual = datetime.now().year
            self.spnMin.setValue(año_actual - 5)
            self.spnMax.setValue(año_actual)

        elif criterio == "Género por sección específica":
            if hasattr(self, 'cbxSeccion_reporte'):
                secciones = CriteriosReportes.obtener_secciones_activas()
                self.cbxSeccion_reporte.clear()
                self.cbxSeccion_reporte.addItem("Seleccione una sección")
                self.cbxSeccion_reporte.addItems(secciones)
                self.cbxSeccion_reporte.setVisible(True)
                if hasattr(self, 'frameSeccion_reporte'):
                    self.frameSeccion_reporte.setVisible(True)
                if hasattr(self, 'lblSeccion_reporte'):
                    self.lblSeccion_reporte.setVisible(True)

        # Configurar tipos de gráfica
        if idx > 0:
            self.actualizar_tipos_grafica()
        else:
            self.cbxTipoGrafica.clear()
            self.cbxTipoGrafica.setEnabled(False)
        
        # Limpiar gráfica al cambiar criterio
        self.figure.clear()
        self.canvas.draw()

    def actualizar_tipos_grafica(self):
        """Actualiza los tipos de gráfica disponibles"""
        self.cbxTipoGrafica.clear()
        self.cbxTipoGrafica.addItem("Seleccione un tipo de gráfica")
        model = self.cbxTipoGrafica.model()
        item0 = model.item(0)
        if item0 is not None:
            item0.setEnabled(False)
            item0.setForeground(Qt.GlobalColor.gray)

        tipos = list(CriteriosReportes.GRAFICAS.keys())
        self.cbxTipoGrafica.addItems(tipos)
        self.cbxTipoGrafica.setEnabled(True)
        self.cbxTipoGrafica.setCurrentIndex(0)

    def actualizar_reporte(self):
        """Genera y muestra el reporte según criterios seleccionados"""
        poblacion = self.cbxPoblacion.currentText()
        idx_criterio = self.cbxCriterio.currentIndex()
        idx_tipo = self.cbxTipoGrafica.currentIndex()

        if not poblacion or idx_criterio <= 0 or idx_tipo <= 0:
            self.figure.clear()
            self.canvas.draw()
            return

        criterio = self.cbxCriterio.currentText()
        tipo = self.cbxTipoGrafica.currentText()

        # Validar rangos
        if criterio in ("Rango de edad", "Rango de salario", "Matricula por año escolar"):
            min_val = self.spnMin.value()
            max_val = self.spnMax.value()
            
            if min_val > max_val:
                crear_msgbox(
                    self,
                    "Rango inválido",
                    f"El valor mínimo ({min_val}) no puede ser mayor que el máximo ({max_val}).",
                    QMessageBox.Warning
                ).exec()
                return

        consulta_info = CriteriosReportes.CONSULTAS.get((poblacion, criterio))
        grafica = CriteriosReportes.GRAFICAS.get(tipo)

        # Limpiar completamente la figura antes de crear nueva gráfica
        self.figure.clear()
        
        ax = self.figure.add_subplot(111)

        etiquetas = []
        valores = []
        
        if consulta_info and grafica:
            consulta, params = consulta_info
            args = []
            titulo = f"{criterio} ({poblacion})"

            if "edad_min" in params and "edad_max" in params:
                args = [self.spnMin.value(), self.spnMax.value()]
                titulo += f" {args[0]}-{args[1]} años"

            elif "salario_min" in params and "salario_max" in params:
                args = [self.spnMin.value(), self.spnMax.value()]
                titulo += f" ${args[0]}-${args[1]}"

            elif "anio_inicio" in params and "anio_fin" in params:
                args = [self.spnMin.value(), self.spnMax.value()]
                titulo += f" ({args[0]}-{args[1]})"

            elif "seccion" in params:
                if hasattr(self, 'cbxSeccion_reporte') and self.cbxSeccion_reporte.currentIndex() > 0:
                    seccion = self.cbxSeccion_reporte.currentText()
                    args = [seccion]
                    titulo += f" - {seccion}"
                else:
                    ax.axis("off")
                    ax.text(0.5, 0.5, "Debe seleccionar una sección", ha="center", va="center", fontsize=12)
                    self.canvas.draw()
                    return

            try:
                etiquetas, valores = consulta(*args)
                
                if not etiquetas or not valores:
                    ax.axis("off")
                    ax.text(0.5, 0.5, "No hay datos disponibles para este criterio", 
                           ha="center", va="center", fontsize=12, color="gray")
                    self.canvas.draw()
                    return
                
                self.ultima_consulta = (etiquetas, valores)
                
                # Advertencia si se limitan datos
                if len(etiquetas) > 15 and tipo in ["Torta", "Barras"]:
                    titulo += "\n(Mostrando top 15)"
                
                grafica(ax, etiquetas, valores, titulo)
                
            except Exception as e:
                ax.axis("off")
                ax.text(0.5, 0.5, f"Error generando reporte:\n{str(e)}", 
                       ha="center", va="center", fontsize=10, color="red")
        else:
            ax.axis("off")
            ax.text(0.5, 0.5, "Combinación no soportada", ha="center", va="center", fontsize=12)

        self.canvas.draw()

    def on_exportar_reporte(self):
        """Exporta el reporte actual a PDF"""
        poblacion = self.cbxPoblacion.currentText()
        idx_criterio = self.cbxCriterio.currentIndex()
        idx_tipo = self.cbxTipoGrafica.currentIndex()
        
        if not poblacion or idx_criterio <= 0 or idx_tipo <= 0:
            crear_msgbox(
                self,
                "Sin datos",
                "Debe generar un reporte antes de exportar.",
                QMessageBox.Warning
            ).exec()
            return
        
        if not hasattr(self, "ultima_consulta") or not self.ultima_consulta[0]:
            crear_msgbox(
                self,
                "Sin datos",
                "No hay datos para exportar. Genere un reporte primero.",
                QMessageBox.Warning
            ).exec()
            return

        try:
            criterio = self.cbxCriterio.currentText()
            tipo = self.cbxTipoGrafica.currentText()
            etiquetas, valores = self.ultima_consulta
            total = sum(valores)
            titulo = f"{criterio} ({poblacion}) - {tipo}"

            archivo = exportar_reporte_pdf(self, self.figure, titulo, criterio, etiquetas, valores, total)
            
            crear_msgbox(
                self,
                "Éxito",
                f"Reporte exportado correctamente:\n{archivo}",
                QMessageBox.Information
            ).exec()
            
            # Abrir archivo
            subprocess.Popen(["xdg-open", archivo])
            
        except Exception as e:
            crear_msgbox(
                self,
                "Error",
                f"No se pudo exportar el reporte: {e}",
                QMessageBox.Critical
            ).exec()
    
    ### MODULO ADMIN ###
    
    def registro_usuario(self):
        """Abre ventana de registro de nuevo usuario"""
        ventana = RegistroUsuario(self.usuario_actual, self)
        if ventana.exec() == QDialog.Accepted:
            self.database_usuarios()
    
    def actualizar_usuario(self):
        """Abre ventana de actualización del usuario seleccionado"""
        index = self.tableW_usuarios.currentIndex()
        
        if not index.isValid():
            crear_msgbox(
                self,
                "Selección requerida",
                "Debe seleccionar un usuario de la tabla.",
                QMessageBox.Warning
            ).exec()
            return
        
        try:
            index_source = self.tableW_usuarios.model().mapToSource(index)
            fila = index_source.row()
            model = index_source.model()
            id_usuario = int(model.item(fila, 0).text())

            ventana = ActualizarUsuario(id_usuario, self.usuario_actual, self)
            ventana.datos_actualizados.connect(self.database_usuarios)
            ventana.exec()
            
        except Exception as e:
            crear_msgbox(
                self,
                "Error",
                f"No se pudo abrir actualización: {e}",
                QMessageBox.Critical
            ).exec()
    
    def cambiar_estado_usuario(self):
        """Cambia el estado activo/inactivo del usuario seleccionado"""
        index = self.tableW_usuarios.currentIndex()
        
        if not index.isValid():
            crear_msgbox(
                self,
                "Selección requerida",
                "Debe seleccionar un usuario de la tabla.",
                QMessageBox.Warning
            ).exec()
            return

        try:
            index_source = self.tableW_usuarios.model().mapToSource(index)
            fila = index_source.row()
            model = index_source.model()

            id_usuario = int(model.item(fila, 0).text())
            username = model.item(fila, 1).text()
            estado_actual_texto = model.item(fila, 3).text()

            # Convertir a booleano
            estado_actual = 1 if estado_actual_texto.lower() == "activo" else 0
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

            ok, mensaje = UsuarioModel.cambiar_estado(id_usuario, nuevo_estado, self.usuario_actual)

            if ok:
                crear_msgbox(
                    self,
                    "Éxito",
                    mensaje,
                    QMessageBox.Information
                ).exec()
                self.database_usuarios()
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
                f"Error al cambiar estado: {err}",
                QMessageBox.Critical
            ).exec()

    def database_usuarios(self):
        """Carga la tabla de usuarios desde la base de datos"""
        try:
            datos = UsuarioModel.listar()
            
            if not datos:
                # Crear modelo vacío
                model_vacio = QStandardItemModel(0, 7)
                model_vacio.setHorizontalHeaderLabels([
                    "ID", "Usuario", "Rol", "Estado", "Nombre Completo",
                    "Fecha de creación", "Ultima actualización"
                ])
                self.proxy_usuarios = QSortFilterProxyModel(self)
                self.proxy_usuarios.setSourceModel(model_vacio)
                self.tableW_usuarios.setModel(self.proxy_usuarios)
                return
            
            columnas = [
                "ID", "Usuario", "Rol", "Estado", "Nombre Completo",
                "Fecha de creación", "Ultima actualización"
            ]

            model = QStandardItemModel(len(datos), len(columnas))
            model.setHorizontalHeaderLabels(columnas)

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

            # Filtrar inactivos si checkbox está desmarcado
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
            crear_msgbox(
                self,
                "Error",
                f"No se pudo cargar la tabla de usuarios: {err}",
                QMessageBox.Critical
            ).exec()
    
    ### MODULO AUDITORIA ###
    
    def cargar_auditoria(self, limit=50):
        """Carga los últimos registros de auditoría"""
        try:
            datos = AuditoriaModel.listar(limit)
            
            if not datos:
                model_vacio = QStandardItemModel(0, 8)
                model_vacio.setHorizontalHeaderLabels([
                    "ID", "Usuario", "Acción", "Entidad", "Entidad ID",
                    "Referencia", "Descripción", "Fecha"
                ])
                self.tableW_auditoria.setModel(model_vacio)
                return
            
            columnas = ["ID", "Usuario", "Acción", "Entidad", "Entidad ID", "Referencia", "Descripción", "Fecha"]

            model = QStandardItemModel(len(datos), len(columnas))
            model.setHorizontalHeaderLabels(columnas)

            for fila, registro in enumerate(datos):
                items = [
                    QStandardItem(str(registro["id"])),
                    QStandardItem(registro["usuario"]),
                    QStandardItem(registro["accion"]),
                    QStandardItem(registro["entidad"]),
                    QStandardItem(str(registro["entidad_id"])),
                    QStandardItem(registro["referencia"] or ""),
                    QStandardItem(registro["descripcion"] or ""),
                    QStandardItem(str(registro["fecha"]))
                ]
                
                for col, item in enumerate(items):
                    item.setEditable(False)
                    model.setItem(fila, col, item)

            self.tableW_auditoria.setModel(model)
            self.tableW_auditoria.setSortingEnabled(True)
            self.tableW_auditoria.setAlternatingRowColors(True)

            # Ordenar por columna Fecha (índice 7) en orden descendente
            self.tableW_auditoria.sortByColumn(7, Qt.SortOrder.DescendingOrder)

            # Anchos personalizados
            anchos_auditoria = {
                0: 50, 1: 120, 2: 100, 3: 120, 4: 80, 5: 150, 6: 300, 7: 150
            }
            ajustar_columnas_tabla(self, self.tableW_auditoria, anchos_auditoria)

        except Exception as err:
            crear_msgbox(
                self,
                "Error",
                f"No se pudo cargar la auditoría: {err}",
                QMessageBox.Critical
            ).exec()
    
    ## DATOS INSTITUCION ##
    
    def set_campos_editables(self, estado: bool):
        """Habilita/deshabilita edición de campos de institución"""
        campos = [
            self.lneNombreInstitucion_admin, self.lneCodigoDEA_admin, self.lneCodigoDEP_admin,
            self.lneCodigoEST_admin, self.lneRIF_admin, self.lneDirInstitucion_admin,
            self.lneTlfInstitucion_admin, self.lneCorreoInstitucion_admin,
            self.lneDirector_institucion, self.lneCedula_director_institucion
        ]
        campos_solo_lectura = [self.lneUltimaActualizacion_admin]
        set_campos_editables(campos, estado, campos_solo_lectura)

    def cargar_datos_institucion(self):
        """Carga datos de la institución en el formulario"""
        try:
            datos = InstitucionModel.obtener_por_id(1)
            
            if not datos:
                ok, mensaje = InstitucionModel.inicializar_si_no_existe()
                if ok:
                    datos = InstitucionModel.obtener_por_id(1)
                else:
                    crear_msgbox(
                        self,
                        "Error",
                        f"No se pudo inicializar datos de institución: {mensaje}",
                        QMessageBox.Critical
                    ).exec()
                    return
            
            self.lneNombreInstitucion_admin.setText(str(datos.get("nombre", "")))
            self.lneCodigoDEA_admin.setText(str(datos.get("codigo_dea", "")))
            self.lneCodigoDEP_admin.setText(str(datos.get("codigo_dependencia", "")))
            self.lneCodigoEST_admin.setText(str(datos.get("codigo_estadistico", "")))
            self.lneRIF_admin.setText(str(datos.get("rif", "")))
            self.lneDirInstitucion_admin.setText(str(datos.get("direccion", "")))
            self.lneTlfInstitucion_admin.setText(str(datos.get("telefono", "")))
            self.lneCorreoInstitucion_admin.setText(str(datos.get("correo", "")))
            self.lneDirector_institucion.setText(str(datos.get("director", "")))
            self.lneCedula_director_institucion.setText(str(datos.get("director_ci", "")))
            
            fecha_act = datos.get("actualizado_en")
            if fecha_act:
                if hasattr(fecha_act, 'strftime'):
                    self.lneUltimaActualizacion_admin.setText(fecha_act.strftime("%d/%m/%Y %H:%M:%S"))
                else:
                    self.lneUltimaActualizacion_admin.setText(str(fecha_act))
            else:
                self.lneUltimaActualizacion_admin.setText("Sin actualizar")
                
        except Exception as err:
            crear_msgbox(
                self,
                "Error",
                f"No se pudieron cargar los datos: {err}",
                QMessageBox.Critical
            ).exec()

    def guardar_datos_institucion(self):
        """Guarda cambios en datos de la institución"""
        try:
            institucion_data = {
                "nombre": self.lneNombreInstitucion_admin.text().strip(),
                "codigo_dea": self.lneCodigoDEA_admin.text().strip(),
                "codigo_dependencia": self.lneCodigoDEP_admin.text().strip(),
                "codigo_estadistico": self.lneCodigoEST_admin.text().strip(),
                "rif": self.lneRIF_admin.text().strip(),
                "direccion": self.lneDirInstitucion_admin.text().strip(),
                "telefono": self.lneTlfInstitucion_admin.text().strip(),
                "correo": self.lneCorreoInstitucion_admin.text().strip(),
                "director": self.lneDirector_institucion.text().strip(),
                "director_ci": self.lneCedula_director_institucion.text().strip(),
            }

            ok, mensaje = InstitucionModel.actualizar(1, institucion_data, self.usuario_actual)

            if ok:
                crear_msgbox(
                    self,
                    "Éxito",
                    mensaje,
                    QMessageBox.Information
                ).exec()
                self.cargar_datos_institucion()
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
                f"No se pudo guardar cambios: {err}",
                QMessageBox.Critical
            ).exec()

    def toggle_edicion(self):
        """Alterna entre modo edición y guardado"""
        if self.btnModificar_institucion.text() == "Modificar datos":
            self.set_campos_editables(True)
            self.btnModificar_institucion.setText("Guardar")
        else:
            self.guardar_datos_institucion()
            self.set_campos_editables(False)
            self.btnModificar_institucion.setText("Modificar datos")
   
    ### MODULO BACKUP ###
    
    def cargar_info_backup(self):
        """Carga información del último backup realizado"""
        try:
            ultimo = BackupManager.obtener_ultimo_backup()
            total = BackupManager.contar_backups()
            
            if hasattr(self, 'lblUltimo_backup'):
                if ultimo:
                    fecha_str = ultimo['fecha'].strftime("%d/%m/%Y %H:%M:%S")
                    tipo_str = ultimo['tipo'].capitalize()
                    self.lblUltimo_backup.setText(
                        f"Último backup: {fecha_str}\n"
                        f"Tipo: {tipo_str}\n"
                        f"Tamaño: {ultimo['tamaño_mb']:.2f} MB\n"
                        f"Total de backups: {total}"
                    )
                else:
                    self.lblUltimo_backup.setText("No hay backups disponibles")
                    
        except Exception as e:
            print(f"Error cargando info de backup: {e}")
    
    def realizar_backup_manual(self):
        """Ejecuta backup manual cuando el usuario presiona el botón"""
        try:
            # Confirmación
            reply = crear_msgbox(
                self,
                "Confirmar backup",
                "¿Desea crear un backup manual de la base de datos?\n\n"
                "Este proceso puede tardar varios segundos dependiendo del tamaño de la base de datos.",
                QMessageBox.Question,
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.Yes
            )
            
            if reply.exec() != QMessageBox.StandardButton.Yes:
                return
            
            # Mostrar mensaje de progreso
            self.statusBar().showMessage("Creando backup manual...")
            
            # Crear backup
            ok, mensaje = BackupManager.crear_backup_manual()
            
            # Limpiar status bar
            self.statusBar().clearMessage()
            
            if ok:
                crear_msgbox(
                    self,
                    "Éxito",
                    mensaje,
                    QMessageBox.Information
                ).exec()
                
                # Actualizar información
                self.cargar_info_backup()
                
                # Abrir carpeta de backups
                reply_abrir = crear_msgbox(
                    self,
                    "Backup creado",
                    "¿Desea abrir la carpeta de backups?",
                    QMessageBox.Question,
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                    QMessageBox.StandardButton.No
                )
                
                if reply_abrir.exec() == QMessageBox.StandardButton.Yes:
                    import os
                    ruta_backups = os.path.abspath("backups")
                    subprocess.Popen(["xdg-open", ruta_backups])
            else:
                crear_msgbox(
                    self,
                    "Error",
                    f"No se pudo crear el backup:\n{mensaje}",
                    QMessageBox.Critical
                ).exec()
                
        except Exception as e:
            crear_msgbox(
                self,
                "Error",
                f"Error inesperado creando backup: {e}",
                QMessageBox.Critical
            ).exec()
    
    def realizar_backup_automatico(self):
        """Ejecuta backup automático periódicamente"""
        try:
            print("Iniciando backup automático...")
            ok, mensaje = BackupManager.crear_backup_automatico()
            
            if ok:
                print(f"Backup automático exitoso: {mensaje}")
                # Actualizar info si la página está visible
                if hasattr(self, 'stackMain') and self.stackMain.currentIndex() == 10:
                    self.cargar_info_backup()
            else:
                print(f"Error en backup automático: {mensaje}")
                
        except Exception as e:
            print(f"Error en backup automático: {e}")
    
    def cerrar_sesion(self):
        """Cierra la sesión actual y muestra login"""
        self.logout = True
        self.close()
    
    def closeEvent(self, event):
        """Limpia recursos al cerrar la ventana"""
        # Limpiar tooltips de delegates
        for delegate in self.tooltip_delegates:
            if hasattr(delegate, 'close_tooltip'):
                delegate.close_tooltip()
        
        # Detener timers
        if hasattr(self, 'timer_global'):
            self.timer_global.stop()
        if hasattr(self, 'timer_backup'):
            self.timer_backup.stop()
        
        super().closeEvent(event)