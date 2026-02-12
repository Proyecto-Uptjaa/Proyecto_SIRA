from PySide6.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, QMessageBox, QDialog
)
from PySide6.QtCore import Qt, QTimer
from utils.tarjeta_seccion import TarjetaSeccion
from ui_compiled.secciones_ui import Ui_secciones
from models.secciones_model import SeccionesModel
from models.anio_model import AnioEscolarModel
from views.crear_seccion import CrearSeccion
from views.detalles_seccion import DetallesSeccion
from utils.sombras import crear_sombra_flotante
from utils.logo_manager import aplicar_logo_a_label
from utils.dialogs import crear_msgbox


class GestionSeccionesPage(QWidget, Ui_secciones):
    """Página de gestión de secciones académicas."""
    
    def __init__(self, usuario_actual, año_escolar, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.año_escolar = año_escolar
        self.setupUi(self)
        
        # Mostrar usuario conectado
        self.lblConectado_como.setText(f"Conectado como: {self.usuario_actual['username']}")

        self.scrollArea_secciones.setWidgetResizable(True)
        self.scrollArea_secciones.setAlignment(Qt.AlignTop)
        
        # Almacenamiento de referencias
        self.tarjetas = []
        self.tarjetas_data = []
        self.separadores_nivel = []
        self.filas_tarjetas = []
        
        # Ventanas de detalles abiertas
        self._detalle_windows = []

        # Conectar botones
        self.btnCrear_seccion.clicked.connect(self.nueva_seccion)
        self.lneBuscar_seccion.textChanged.connect(self.filtrar_tarjetas)

        # Cargar datos iniciales
        self.cargar_secciones()
        
        # Timer para actualización automática (cada 60 segundos)
        self.timer_actualizar = QTimer(self)
        self.timer_actualizar.timeout.connect(self.actualizar_tarjetas)
        self.timer_actualizar.start(60000)

        # Aplicar efectos visuales
        crear_sombra_flotante(self.btnCrear_seccion)
        crear_sombra_flotante(self.lneBuscar_seccion, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lblTitulo_secciones, blur_radius=5, y_offset=1)
        crear_sombra_flotante(self.lblLogo_secciones, blur_radius=5, y_offset=1)
        
        # Aplicar logo institucional dinámico
        aplicar_logo_a_label(self.lblLogo_secciones)

    def closeEvent(self, event):
        """Detiene el timer al cerrar."""
        if hasattr(self, 'timer_actualizar'):
            self.timer_actualizar.stop()
        event.accept()

    def filtrar_tarjetas(self, texto_busqueda: str):
        """Filtra las tarjetas según el texto de búsqueda."""
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
        for tarjeta, datos in zip(self.tarjetas, self.tarjetas_data):
            grado = str(datos.get("grado", "")).lower()
            letra = str(datos.get("letra", "")).lower()
            nivel = str(datos.get("nivel", "")).lower()
            docente = str(datos.get("docente_nombre", "sin asignar")).lower()
            
            # Buscar coincidencias
            coincide = (
                texto in grado or
                texto in letra or
                texto in nivel or
                texto in docente or
                texto in f"{grado} {letra}" or
                texto in f"{nivel} {grado} {letra}"
            )
            
            tarjeta.setVisible(coincide)
            
            # Contar visibles por nivel
            if coincide:
                tarjetas_visibles_por_nivel[nivel] = tarjetas_visibles_por_nivel.get(nivel, 0) + 1
    
        # Ocultar separadores sin resultados
        for separador in self.separadores_nivel:
            texto_separador = separador.text()
            nivel_sep = texto_separador.replace("───", "").strip()
            tiene_resultados = tarjetas_visibles_por_nivel.get(nivel_sep, 0) > 0
            separador.setVisible(tiene_resultados)
        
        # Ocultar filas vacías
        for fila in self.filas_tarjetas:
            tiene_visible = False
            layout_fila = fila.layout()
            if layout_fila:
                for i in range(layout_fila.count()):
                    widget = layout_fila.itemAt(i).widget()
                    if widget and widget.isVisible():
                        tiene_visible = True
                        break
            fila.setVisible(tiene_visible)

    def cargar_secciones(self):
        """Carga y muestra las secciones del año actual."""
        try:
            # Limpiar layout
            for i in reversed(range(self.verticalLayout_contenido.count())):
                widget = self.verticalLayout_contenido.itemAt(i).widget()
                if widget:
                    widget.deleteLater()
            
            # Limpiar referencias
            self.tarjetas.clear()
            self.tarjetas_data.clear()
            self.separadores_nivel.clear()
            self.filas_tarjetas.clear()

            # Obtener año escolar actual
            anio_actual = AnioEscolarModel.obtener_actual()
            
            if not anio_actual:
                lbl_error = QLabel("⚠️ No hay año escolar activo. Apertura uno primero.")
                lbl_error.setStyleSheet("color: red; font-weight: bold; padding: 20px;")
                lbl_error.setAlignment(Qt.AlignCenter)
                self.verticalLayout_contenido.addWidget(lbl_error)
                return

            # Obtener secciones del año actual
            todas = SeccionesModel.obtener_todas(anio_actual['id'])

            if not todas:
                lbl_sin_secciones = QLabel("📋 No hay secciones registradas para este año.")
                lbl_sin_secciones.setStyleSheet("color: #7f8c8d; padding: 20px;")
                lbl_sin_secciones.setAlignment(Qt.AlignCenter)
                self.verticalLayout_contenido.addWidget(lbl_sin_secciones)
                self.verticalLayout_contenido.addStretch()
                return

            # Organizar tarjetas
            layout_fila_actual = None
            contador_tarjetas_fila = 0
            nivel_anterior = None

            # Ordenar: nivel (Inicial primero), grado, letra
            for sec in sorted(todas, key=lambda s: (
                0 if s["nivel"] == "Inicial" else 1,
                s["grado"],
                s["letra"] if s["letra"] != "Única" else "ZZZ"  # Única al final
            )):
                # Separador de nivel
                if sec["nivel"] != nivel_anterior:
                    lbl = QLabel(f"─── {sec['nivel'].upper()} ───")
                    lbl.setStyleSheet(
                        "font-size: 20px; font-weight: bold; "
                        "color: #2c3e50; padding: 10px 0;"
                    )
                    lbl.setAlignment(Qt.AlignCenter)
                    self.verticalLayout_contenido.addWidget(lbl)
                    self.separadores_nivel.append(lbl)
                    nivel_anterior = sec["nivel"]
                    layout_fila_actual = None
                    contador_tarjetas_fila = 0

                # Nueva fila cada 3 tarjetas
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
                tarjeta.clic_en_ver_estudiantes.connect(
                    lambda sid, s=sec: self.abrir_detalle(sid)
                )
                
                layout_fila_actual.insertWidget(layout_fila_actual.count() - 1, tarjeta)
                self.tarjetas.append(tarjeta)
                self.tarjetas_data.append(sec)
                contador_tarjetas_fila += 1

            # Stretch final
            self.verticalLayout_contenido.addStretch()
            
        except Exception as e:
            crear_msgbox(
                self,
                "Error",
                f"No se pudo cargar las secciones:\n{e}",
                QMessageBox.Critical
            ).exec()

    def nueva_seccion(self):
        """Abre diálogo para crear nueva sección."""
        # Validar que haya año activo
        anio_actual = AnioEscolarModel.obtener_actual()
        if not anio_actual:
            crear_msgbox(
                self,
                "Sin año activo",
                "Debe aperturar un año escolar antes de crear secciones.",
                QMessageBox.Warning
            ).exec()
            return
        
        ventana = CrearSeccion(self.usuario_actual, self)
        if ventana.exec() == QDialog.Accepted:
            self.cargar_secciones()
            self.actualizar_pagina_notas()

    def abrir_detalle(self, seccion_id: int):
        """Abre la ventana de detalles de sección"""
        try:
            detalle_widget = DetallesSeccion(
                self.usuario_actual, 
                seccion_id, 
                self.año_escolar, 
                parent=None
            )
            detalle_widget.gestion_secciones_ref = self

            # Mantener referencia
            self._detalle_windows.append(detalle_widget)

            # Auto-limpiar al cerrar
            detalle_widget.setAttribute(Qt.WA_DeleteOnClose)
            detalle_widget.destroyed.connect(
                lambda: self._detalle_windows.remove(detalle_widget) 
                if detalle_widget in self._detalle_windows else None
            )
            detalle_widget.destroyed.connect(self.cargar_secciones)

            detalle_widget.show()

        except Exception as e:
            crear_msgbox(
                self,
                "Error",
                f"No se pudo abrir detalle de sección:\n{e}",
                QMessageBox.Critical
            ).exec()

    def actualizar_tarjetas(self):
        """Actualiza el conteo de estudiantes en las tarjetas."""
        try:
            anio_actual = AnioEscolarModel.obtener_actual()
            if not anio_actual:
                return

            # Obtener datos actualizados
            todas = SeccionesModel.obtener_todas(anio_actual['id'])
            datos_actualizados = {sec["id"]: sec for sec in todas}
            
            # Actualizar solo el conteo en cada tarjeta
            for i, tarjeta in enumerate(self.tarjetas):
                seccion_id = tarjeta.seccion_id
                if seccion_id in datos_actualizados:
                    datos_nuevos = datos_actualizados[seccion_id]
                    estudiantes_actuales = datos_nuevos.get("estudiantes_actuales", 0)
                    tarjeta.actualizar_conteo_estudiantes(estudiantes_actuales)
                    
                    # Actualizar datos locales
                    if i < len(self.tarjetas_data):
                        self.tarjetas_data[i]["estudiantes_actuales"] = estudiantes_actuales
                        
        except Exception as e:
            print(f"Error actualizando tarjetas: {e}")
    
    def actualizar_pagina_notas(self):
        """Busca y actualiza la página de notas en el parent."""
        parent = self.parent()
        while parent:
            if hasattr(parent, 'page_gestion_notas'):
                if hasattr(parent.page_gestion_notas, 'refrescar'):
                    parent.page_gestion_notas.refrescar()
                    break
            parent = parent.parent() if parent else None