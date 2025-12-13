from PySide6.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, QMessageBox, QDialog, QVBoxLayout
)
from PySide6.QtCore import Qt, QTimer
from utils.tarjeta_seccion import TarjetaSeccion
from ui_compiled.secciones_ui import Ui_secciones
from models.secciones_model import SeccionesModel
from models.anio_model import AnioEscolarModel
from views.crear_seccion import CrearSeccion
from views.detalles_seccion import DetallesSeccion
from utils.sombras import crear_sombra_flotante


class GestionSeccionesPage(QWidget, Ui_secciones):
    def __init__(self, usuario_actual, año_escolar, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.año_escolar = año_escolar
        self.setupUi(self)

        self.scrollArea_secciones.setWidgetResizable(True)
        self.scrollArea_secciones.setAlignment(Qt.AlignTop)
        self.tarjetas = []
        self.tarjetas_data = []  # Guardar datos de cada tarjeta para filtrado
        self.separadores_nivel = []  # Guardar referencias a los separadores
        self.filas_tarjetas = []  # Guardar referencias a las filas (QWidget con QHBoxLayout)

        # Botones
        self.btnCrear_seccion.clicked.connect(self.nueva_seccion)
        # Conectar búsqueda
        self.lneBuscar_seccion.textChanged.connect(self.filtrar_tarjetas)

        self.cargar_secciones()
        
        # Timer para actualizar tarjetas periódicamente
        self.timer_actualizar = QTimer(self)
        self.timer_actualizar.timeout.connect(self.actualizar_tarjetas)
        self.timer_actualizar.start(15000)  # 15 segundos

        ## Sombras de elementos ##
        crear_sombra_flotante(self.btnCrear_seccion)
        crear_sombra_flotante(self.lneBuscar_seccion, blur_radius=8, y_offset=1)

    def filtrar_tarjetas(self, texto_busqueda):
        """Filtra las tarjetas según el texto de búsqueda"""
        texto = texto_busqueda.lower().strip()
        
        # Si está vacío, mostrar todas
        if not texto:
            for tarjeta in self.tarjetas:
                tarjeta.setVisible(True)
            for separador in self.separadores_nivel:
                separador.setVisible(True)
            for fila in self.filas_tarjetas:
                fila.setVisible(True)
            return
        
        # Contar tarjetas visibles por nivel
        tarjetas_visibles_por_nivel = {}
        
        # Filtrar cada tarjeta
        for i, (tarjeta, datos) in enumerate(zip(self.tarjetas, self.tarjetas_data)):
            grado = str(datos.get("grado", "")).lower()
            letra = str(datos.get("letra", "")).lower()
            nivel = str(datos.get("nivel", "")).lower()
            maestra = str(datos.get("maestra_nombre", "vacante")).lower()
            
            # Buscar coincidencias
            coincide = (
                texto in grado or
                texto in letra or
                texto in nivel or
                texto in maestra or
                texto in f"{grado} {letra}" or
                texto in f"{nivel} {grado} {letra}"
            )
            
            tarjeta.setVisible(coincide)
            
            # Contar tarjetas visibles por nivel
            if coincide:
                nivel_key = datos.get("nivel", "")
                tarjetas_visibles_por_nivel[nivel_key] = tarjetas_visibles_por_nivel.get(nivel_key, 0) + 1
        
        # Ocultar separadores de nivel si no hay tarjetas visibles
        for separador in self.separadores_nivel:
            texto_separador = separador.text()
            nivel_sep = texto_separador.replace("───", "").strip()
            if nivel_sep not in tarjetas_visibles_por_nivel or tarjetas_visibles_por_nivel[nivel_sep] == 0:
                separador.setVisible(False)
            else:
                separador.setVisible(True)
        
        # Ocultar filas vacías
        for fila in self.filas_tarjetas:
            tiene_visible = False
            layout_fila = fila.layout()
            if layout_fila:
                for i in range(layout_fila.count()):
                    item = layout_fila.itemAt(i)
                    if item and item.widget():
                        widget = item.widget()
                        if isinstance(widget, TarjetaSeccion) and widget.isVisible():
                            tiene_visible = True
                            break
            fila.setVisible(tiene_visible)

    def cargar_secciones(self):
        """Carga las secciones del año escolar actual"""
        # Limpiar
        for i in reversed(range(self.verticalLayout_contenido.count())):
            w = self.verticalLayout_contenido.itemAt(i).widget()
            if w:
                w.deleteLater()
        self.tarjetas.clear()
        self.tarjetas_data.clear()
        self.separadores_nivel.clear()
        self.filas_tarjetas.clear()

        # Obtener año escolar actual
        anio_actual = AnioEscolarModel.obtener_actual()
        
        if not anio_actual:
            lbl_error = QLabel("⚠️ No hay año escolar activo. Por favor, apertura uno primero.")
            lbl_error.setStyleSheet("color: red; font-weight: bold; padding: 20px;")
            lbl_error.setAlignment(Qt.AlignCenter)
            self.verticalLayout_contenido.addWidget(lbl_error)
            return

        # Obtener secciones del año actual por su ID
        todas = SeccionesModel.obtener_todas(anio_actual['id'])

        if not todas:
            lbl_sin_secciones = QLabel("📋 No hay secciones registradas para este año.")
            lbl_sin_secciones.setStyleSheet("color: #7f8c8d; padding: 20px;")
            lbl_sin_secciones.setAlignment(Qt.AlignCenter)
            self.verticalLayout_contenido.addWidget(lbl_sin_secciones)
            self.verticalLayout_contenido.addStretch()
            return

        layout_fila_actual = None
        contador_tarjetas_fila = 0
        nivel_anterior = None

        # Ordenar por: nivel, grado, letra
        for sec in sorted(todas, key=lambda s: (
            0 if s["nivel"] == "Inicial" else 1,  # Inicial siempre arriba
            s["grado"],
            s["letra"] if s["letra"] != "Única" else "Z"
        )):

            # Separador de nivel
            
            if sec["nivel"] != nivel_anterior:
                lbl = QLabel(f"─── {sec['nivel'].upper()} ───")
                lbl.setStyleSheet("font-size: 20px; font-weight: bold; color: #2c3e50; padding: 10px 0;")
                lbl.setAlignment(Qt.AlignCenter)
                self.verticalLayout_contenido.addWidget(lbl)
                self.separadores_nivel.append(lbl)
                nivel_anterior = sec["nivel"]
                layout_fila_actual = None
                contador_tarjetas_fila = 0

            # Nueva fila cada 3 tarjetas o al cambiar de nivel
            if layout_fila_actual is None or contador_tarjetas_fila >= 3:
                fila = QWidget()
                layout_fila_actual = QHBoxLayout(fila)
                layout_fila_actual.setSpacing(20)
                layout_fila_actual.setContentsMargins(10, 8, 10, 8)
                layout_fila_actual.addStretch()
                self.verticalLayout_contenido.addWidget(fila)
                self.filas_tarjetas.append(fila)
                contador_tarjetas_fila = 0

            # Crear tarjeta
            tarjeta = TarjetaSeccion(sec)
            self.tarjetas_data.append(sec)
            tarjeta.clic_en_ver_estudiantes.connect(lambda sid, s=sec: self.abrir_detalle(sid))
            #tarjeta.clic_en_editar.connect(lambda _, s=sec: self.editar_seccion(s["id"]))
            
            layout_fila_actual.insertWidget(layout_fila_actual.count() - 1, tarjeta)
            self.tarjetas.append(tarjeta)
            contador_tarjetas_fila += 1

        # Stretch final
        self.verticalLayout_contenido.addStretch()

    def nueva_seccion(self):
        """Abre el diálogo para crear una nueva sección"""
        ventana = CrearSeccion(self.usuario_actual, self)
        if ventana.exec() == QDialog.Accepted:
            self.cargar_secciones()

    def abrir_detalle(self, seccion_id):
        """Abre la ventana de detalles de sección"""
        try:
            detalle_widget = DetallesSeccion(self.usuario_actual, seccion_id, self.año_escolar, parent=None)
            detalle_widget.gestion_secciones_ref = self

            if not hasattr(self, "_detalle_windows"):
                self._detalle_windows = []
            self._detalle_windows.append(detalle_widget)

            detalle_widget.setAttribute(Qt.WA_DeleteOnClose)
            detalle_widget.show()
            detalle_widget.destroyed.connect(self.cargar_secciones)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo abrir detalle de sección: {e}")

    def editar_seccion(self, seccion_id):
        """Abre el editor de sección"""
        dlg = CrearSeccion(self.usuario_actual, self)
        if dlg.exec() == QDialog.Accepted:
            self.cargar_secciones()

    def actualizar_tarjetas(self):
        """Actualiza el conteo de estudiantes en las tarjetas"""
        anio_actual = AnioEscolarModel.obtener_actual()
        if not anio_actual:
            return

        todas = SeccionesModel.obtener_todas(anio_actual['id'])
        datos_actualizados = {sec["id"]: sec for sec in todas}
        
        for i, tarjeta in enumerate(self.tarjetas):
            seccion_id = tarjeta.seccion_id
            if seccion_id in datos_actualizados:
                datos_nuevos = datos_actualizados[seccion_id]
                estudiantes_actuales = datos_nuevos.get("estudiantes_actuales", 0)
                tarjeta.actualizar_conteo_estudiantes(estudiantes_actuales)
                self.tarjetas_data[i]["estudiantes_actuales"] = estudiantes_actuales