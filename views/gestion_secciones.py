# views/gestion_secciones.py
from PySide6.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, QMessageBox, QInputDialog, QDialog, QVBoxLayout
)
from PySide6.QtCore import Qt
from utils.tarjeta_seccion import TarjetaSeccion
from ui_compiled.secciones_ui import Ui_secciones
from models.secciones_model import SeccionesModel
from views.crear_seccion import CrearSeccion
from views.detalles_seccion import DetallesSeccion


class GestionSeccionesPage(QWidget, Ui_secciones):
    def __init__(self, usuario_actual, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
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
        
        # Contar tarjetas visibles por nivel para ocultar separadores vacíos
        tarjetas_visibles_por_nivel = {}
        
        # Filtrar cada tarjeta
        for i, (tarjeta, datos) in enumerate(zip(self.tarjetas, self.tarjetas_data)):
            # Buscar en los campos relevantes
            grado = str(datos.get("grado", "")).lower()
            letra = str(datos.get("letra", "")).lower()
            nivel = str(datos.get("nivel", "")).lower()
            #salon = str(datos.get("salon", "")).lower()
            maestra = str(datos.get("maestra", "vacante")).lower()
            
            # Buscar coincidencias
            coincide = (
                texto in grado or
                texto in letra or
                texto in nivel or
                #texto in salon or
                texto in maestra or
                texto in f"{grado} {letra}" or
                texto in f"{nivel} {grado} {letra}"
            )
            
            tarjeta.setVisible(coincide)
            
            # Contar tarjetas visibles por nivel
            if coincide:
                nivel_key = datos.get("nivel", "")
                tarjetas_visibles_por_nivel[nivel_key] = tarjetas_visibles_por_nivel.get(nivel_key, 0) + 1
        
        # Ocultar separadores de nivel si no hay tarjetas visibles en ese nivel
        for separador in self.separadores_nivel:
            texto_separador = separador.text()
            # Extraer el nivel del texto del separador (formato: "─── Nivel ───")
            nivel_sep = texto_separador.replace("───", "").replace("───", "").strip()
            if nivel_sep not in tarjetas_visibles_por_nivel or tarjetas_visibles_por_nivel[nivel_sep] == 0:
                separador.setVisible(False)
            else:
                separador.setVisible(True)
        
        # Ocultar filas vacías (filas que no tienen tarjetas visibles)
        # Necesitamos mapear qué tarjetas están en qué filas
        # Por simplicidad, ocultamos filas si todas sus tarjetas están ocultas
        for fila in self.filas_tarjetas:
            # Verificar si alguna tarjeta en esta fila está visible
            tiene_visible = False
            layout_fila = fila.layout()
            if layout_fila:
                for i in range(layout_fila.count()):
                    item = layout_fila.itemAt(i)
                    if item and item.widget():
                        widget = item.widget()
                        # Si es una tarjeta y está visible
                        if isinstance(widget, TarjetaSeccion) and widget.isVisible():
                            tiene_visible = True
                            break
            fila.setVisible(tiene_visible)

    def cargar_secciones(self):
        # Limpiar
        for i in reversed(range(self.verticalLayout_contenido.count())):
            w = self.verticalLayout_contenido.itemAt(i).widget()
            if w:
                w.deleteLater()
        self.tarjetas.clear()
        self.tarjetas_data.clear()
        self.separadores_nivel.clear()
        self.filas_tarjetas.clear()

        todas = SeccionesModel.obtener_todas()

        layout_fila_actual = None
        contador_tarjetas_fila = 0        # ← NUEVO: contador para máximo 3 por fila
        nivel_anterior = None
        año_anterior = None

        for sec in sorted(todas, key=lambda s: (
            -s["año_inicio"],  # más reciente arriba
            0 if s["nivel"] == "Inicial" else 1,  # Inicial siempre arriba
            s["grado"],
            s["letra"] if s["letra"] != "Única" else "Z"
        )):

            # Separador de nivel
            if sec["nivel"] != nivel_anterior:
                lbl = QLabel(f"─── {sec['nivel']} ───")
                lbl.setStyleSheet("font-size: 20px; font-weight: bold; color: #3498db; padding: 10px 0;")
                lbl.setAlignment(Qt.AlignCenter)
                self.verticalLayout_contenido.addWidget(lbl)
                self.separadores_nivel.append(lbl)  # Guardar referencia
                nivel_anterior = sec["nivel"]
                layout_fila_actual = None
                contador_tarjetas_fila = 0

            # NUEVA FILA CADA 3 TARJETAS O AL CAMBIAR DE NIVEL/AÑO
            if layout_fila_actual is None or contador_tarjetas_fila >= 3:
                fila = QWidget()
                layout_fila_actual = QHBoxLayout(fila)
                layout_fila_actual.setSpacing(20)
                layout_fila_actual.setContentsMargins(10, 8, 10, 8)
                layout_fila_actual.addStretch()  # para que queden centradas
                self.verticalLayout_contenido.addWidget(fila)
                self.filas_tarjetas.append(fila)  # Guardar referencia
                contador_tarjetas_fila = 0

            # Crear y agregar tarjeta
            tarjeta = TarjetaSeccion(sec)
            # Guardar datos de la sección para filtrado
            self.tarjetas_data.append(sec)
            # conectar a la señal correcta que emite el id de la sección
            tarjeta.clic_en_ver_estudiantes.connect(lambda sid, s=sec: self.abrir_detalle(sid))
            tarjeta.clic_en_editar.connect(lambda _, s=sec: self.editar_seccion(s["id"]))
            
            # Insertar antes del stretch final
            layout_fila_actual.insertWidget(layout_fila_actual.count() - 1, tarjeta)
            self.tarjetas.append(tarjeta)

            contador_tarjetas_fila += 1

        # Al final, un stretch para que todo quede arriba
        self.verticalLayout_contenido.addStretch()

    def nueva_seccion(self):
        ventana = CrearSeccion(self.usuario_actual, self)
        # CrearSeccion se encarga de validar/crear la sección y hace self.accept() si todo fue bien.
        if ventana.exec() == QDialog.Accepted:
            # Recargar listado después de crear correctamente
            self.cargar_secciones()

    def abrir_detalle(self, seccion_id):
        """Abrir ventana de DetallesSeccion sin cambiar su tamaño ni título diseñados."""
        try:
            # Crear la vista como ventana independiente (sin parent) para que use su propio diseño/tamaño
            detalle_widget = DetallesSeccion(self.usuario_actual, seccion_id, parent=None)

            # Mantener referencia para evitar que Python la recoja como basura
            if not hasattr(self, "_detalle_windows"):
                self._detalle_windows = []
            self._detalle_windows.append(detalle_widget)

            # El widget se encarga de su propio título/size; mostrar como ventana independiente
            detalle_widget.setAttribute(Qt.WA_DeleteOnClose)
            detalle_widget.show()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo abrir detalle de sección: {e}")

    def editar_seccion(self, seccion_id):
        """Placeholder: abrir editor de sección (puedes implementar edición en CrearSeccion)."""
        # Aquí puedes abrir un diálogo para editar; por ahora reusa CrearSeccion si la implementas para edición.
        dlg = CrearSeccion(self.usuario_actual, self)
        # TODO: cargar datos de la sección en el diálogo para editar
        if dlg.exec() == QDialog.Accepted:
            self.cargar_secciones()

    def actualizar_tarjetas(self):
        """Actualiza el conteo de estudiantes en todas las tarjetas"""
        # Obtener datos actualizados de las secciones
        todas = SeccionesModel.obtener_todas()
        
        # Crear un diccionario con los datos actualizados por ID de sección
        datos_actualizados = {sec["id"]: sec for sec in todas}
        
        # Actualizar cada tarjeta existente
        for i, tarjeta in enumerate(self.tarjetas):
            seccion_id = tarjeta.seccion_id
            if seccion_id in datos_actualizados:
                datos_nuevos = datos_actualizados[seccion_id]
                estudiantes_actuales = datos_nuevos.get("estudiantes_actuales", 0)
                tarjeta.actualizar_conteo_estudiantes(estudiantes_actuales)
                # También actualizar los datos guardados para el filtrado
                self.tarjetas_data[i]["estudiantes_actuales"] = estudiantes_actuales