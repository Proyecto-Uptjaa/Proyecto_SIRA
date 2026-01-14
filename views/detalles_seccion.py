from PySide6.QtWidgets import QWidget, QDialog
from ui_compiled.detalles_seccion_ui import Ui_detalle_seccion
from ui_compiled.mover_estudiante_ui import Ui_mover_estudiante
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Qt, QSortFilterProxyModel
from PySide6.QtGui import QStandardItem, QStandardItemModel

from models.estu_model import EstudianteModel
from models.anio_model import AnioEscolarModel
from models.secciones_model import SeccionesModel
from views.delegates import EstudianteDelegate
from datetime import datetime
from utils.dialogs import crear_msgbox
from utils.sombras import crear_sombra_flotante
from models.emple_model import EmpleadoModel


class DialogMoverEstudiante(QDialog, Ui_mover_estudiante):
    """Diálogo para mover estudiante a otra sección."""
    
    def __init__(self, secciones_disponibles, seccion_actual_id, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Mover estudiante a otra sección")
        self.seccion_seleccionada = None
        
        # Limpiar y cargar secciones
        self.cbxMover_estudiante.clear()
        
        # Agregar placeholder
        self.cbxMover_estudiante.addItem("Seleccione una sección")
        
        # Deshabilitar placeholder
        model = self.cbxMover_estudiante.model()
        item0 = model.item(0)
        if item0:
            item0.setEnabled(False)
            item0.setForeground(Qt.GlobalColor.gray)
        
        # Agregar secciones disponibles
        for sec in secciones_disponibles:
            texto = f"{sec['grado']} {sec['letra']}"
            self.cbxMover_estudiante.addItem(texto, sec['id'])
        
        # Seleccionar placeholder
        self.cbxMover_estudiante.setCurrentIndex(0)
        
        # Conectar botones
        self.buttonBox.accepted.connect(self.aceptar)
        self.buttonBox.rejected.connect(self.reject)

        # Sombras
        crear_sombra_flotante(self.cbxMover_estudiante, blur_radius=8, y_offset=1)
    
    def aceptar(self):
        """Valida y acepta la selección."""
        seccion_id = self.cbxMover_estudiante.currentData()
        if seccion_id and self.cbxMover_estudiante.currentIndex() > 0:
            self.seccion_seleccionada = seccion_id
            self.accept()
        else:
            crear_msgbox(
                self,
                "Selección requerida",
                "Debe seleccionar una sección de destino.",
                QMessageBox.Warning
            ).exec()


class DetallesSeccion(QWidget, Ui_detalle_seccion):
    """Ventana de detalles de una sección."""
    
    def __init__(self, usuario_actual, seccion_id, año_escolar, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.año_escolar = año_escolar
        self.seccion_id = int(seccion_id) if seccion_id is not None else None
        self.seccion_actual = None
        self.datos = []  # Lista de estudiantes actuales
        self.modo_edicion_docente = False  # Controla si está en modo edición
        self.setupUi(self)
        
        # Cargar datos de la sección
        self._cargar_datos_seccion()

        # Configurar combo docente en modo solo lectura
        self.cbxDocente_seccion.setEnabled(False)
        self._cargar_combo_docentes()

        # Conectar controles
        self.lneBuscar_detalle_seccion.textChanged.connect(self.filtrar_tabla_estudiantes)
        self.cbxFiltro_detalle_seccion.currentIndexChanged.connect(
            lambda _: self.filtrar_tabla_estudiantes(self.lneBuscar_detalle_seccion.text())
        )

        # Conectar botones
        self.btnMover_estudiante.clicked.connect(self.mover_estudiante)
        self.btnDesactivar_seccion.clicked.connect(self.desactivar_seccion)
        self.btnCambiar_docente.clicked.connect(self.toggle_modo_edicion_docente)
        
        # Conectar cambio de docente (solo se dispara en modo edición)
        self.cbxDocente_seccion.currentIndexChanged.connect(self._cambiar_docente)

        # Proxy para filtrado
        self.proxy_estudiantes = QSortFilterProxyModel(self)
        self.proxy_estudiantes.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.proxy_estudiantes.setFilterKeyColumn(-1)

        # Cargar tabla
        self.tableW_detalles_seccion()
        self.actualizar_conteo()
        
        # Sombras
        crear_sombra_flotante(self.btnMover_estudiante)
        crear_sombra_flotante(self.btnDesactivar_seccion)
        crear_sombra_flotante(self.btnCambiar_docente)
        crear_sombra_flotante(self.lneBuscar_detalle_seccion, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.frameDocente_seccion, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lblTitulo_detalle_seccion, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lblLogo_detalle_seccion, blur_radius=8, y_offset=1)
    
    def _cargar_datos_seccion(self):
        """Carga los datos de la sección."""
        try:
            seccion = SeccionesModel.obtener_por_id(self.seccion_id)
            if seccion:
                self.seccion_actual = seccion
                titulo = f"{seccion.get('grado', '')} {seccion.get('letra', '')}".strip()
                if hasattr(self, 'lblTitulo_detalle_seccion'):
                    self.lblTitulo_detalle_seccion.setText(titulo)
            else:
                if hasattr(self, 'lblTitulo_detalle_seccion'):
                    self.lblTitulo_detalle_seccion.setText("Detalle de sección")
        except Exception as e:
            print(f"Error cargando datos de sección: {e}")

    def _cargar_combo_docentes(self):
        """Carga el combo de docentes."""
        try:
            # Bloquear señales durante la carga inicial
            self.cbxDocente_seccion.blockSignals(True)
            
            self.cbxDocente_seccion.clear()
            self.cbxDocente_seccion.addItem("Sin docente asignado", None)
            
            # Obtener todos los docentes activos
            docentes = EmpleadoModel.listar_docentes_disponibles()
            for doc in docentes:
                nombre_completo = doc.get('nombre_completo', '')
                empleado_id = doc.get('id')
                self.cbxDocente_seccion.addItem(nombre_completo, empleado_id)
            
            # Seleccionar docente actual si existe
            docente_actual = SeccionesModel.obtener_docente_asignado(self.seccion_id)
            if docente_actual:
                docente_id = docente_actual.get('id')
                idx = self.cbxDocente_seccion.findData(docente_id)
                if idx >= 0:
                    self.cbxDocente_seccion.setCurrentIndex(idx)
                else:
                    # Si no se encuentra, significa que el docente está inactivo
                    # Agregarlo temporalmente para mostrar
                    nombre = docente_actual.get('nombre_completo', 'Docente inactivo')
                    self.cbxDocente_seccion.addItem(f"{nombre} (Inactivo)", docente_id)
                    self.cbxDocente_seccion.setCurrentIndex(self.cbxDocente_seccion.count() - 1)
            else:
                self.cbxDocente_seccion.setCurrentIndex(0)
            
            # Desbloquear señales
            self.cbxDocente_seccion.blockSignals(False)
            
        except Exception as e:
            print(f"Error cargando docentes: {e}")
            self.cbxDocente_seccion.blockSignals(False)

    def toggle_modo_edicion_docente(self):
        """Alterna entre modo lectura y modo edición del docente"""
        if not self.modo_edicion_docente:
            # Activar modo edición
            self.modo_edicion_docente = True
            self.cbxDocente_seccion.setEnabled(True)
            #self.btnCambiar_docente.setText("Cancelar")
            
            # Guardar selección actual por si cancela
            self.docente_anterior_idx = self.cbxDocente_seccion.currentIndex()
            
        else:
            # Cancelar edición (volver a modo lectura)
            self.modo_edicion_docente = False
            self.cbxDocente_seccion.setEnabled(False)
            #self.btnCambiar_docente.setText("Cambiar")
            
            # Restaurar selección anterior
            self.cbxDocente_seccion.blockSignals(True)
            self.cbxDocente_seccion.setCurrentIndex(self.docente_anterior_idx)
            self.cbxDocente_seccion.blockSignals(False)

    def _cambiar_docente(self, index):
        """Maneja el cambio de docente (solo en modo edición)"""
        # Solo procesar si está en modo edición y el cambio no es programático
        if not self.modo_edicion_docente:
            return
        
        # Evitar procesar durante carga inicial
        if index < 0:
            return
        
        empleado_id = self.cbxDocente_seccion.currentData()
        nombre_docente = self.cbxDocente_seccion.currentText()
        
        # Confirmar cambio
        if empleado_id:
            mensaje = f"¿Desea asignar a {nombre_docente} como docente de esta sección?"
        else:
            mensaje = "¿Desea desasignar el docente actual de esta sección?"
        
        confirmar = crear_msgbox(
            self,
            "Confirmar cambio de docente",
            mensaje,
            QMessageBox.Question,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if confirmar.exec() != QMessageBox.StandardButton.Yes:
            # Cancelar: restaurar selección anterior
            self.cbxDocente_seccion.blockSignals(True)
            self.cbxDocente_seccion.setCurrentIndex(self.docente_anterior_idx)
            self.cbxDocente_seccion.blockSignals(False)
            return
        
        # Aplicar cambio en la BD
        try:
            ok, msg = SeccionesModel.asignar_docente(
                self.seccion_id, 
                empleado_id, 
                self.usuario_actual
            )
            
            if ok:
                crear_msgbox(
                    self, 
                    "Éxito", 
                    msg, 
                    QMessageBox.Information
                ).exec()
                
                # Salir del modo edición
                self.modo_edicion_docente = False
                self.cbxDocente_seccion.setEnabled(False)
                self.btnCambiar_docente.setText("Cambiar")
                
                # Actualizar combo (por si cambió disponibilidad de docentes)
                self._cargar_combo_docentes()
                
            else:
                crear_msgbox(
                    self, 
                    "Error", 
                    msg, 
                    QMessageBox.Critical
                ).exec()
                
                # Restaurar selección anterior
                self.cbxDocente_seccion.blockSignals(True)
                self.cbxDocente_seccion.setCurrentIndex(self.docente_anterior_idx)
                self.cbxDocente_seccion.blockSignals(False)
                
        except Exception as err:
            crear_msgbox(
                self,
                "Error",
                f"Error al cambiar docente: {err}",
                QMessageBox.Critical
            ).exec()
            
            # Restaurar selección anterior
            self.cbxDocente_seccion.blockSignals(True)
            self.cbxDocente_seccion.setCurrentIndex(self.docente_anterior_idx)
            self.cbxDocente_seccion.blockSignals(False)

    def mover_estudiante(self):
        """Mueve un estudiante a otra sección del mismo grado."""
        # Validar selección
        estudiante = self.obtener_estudiante_seleccionado()
        if not estudiante:
            crear_msgbox(
                self,
                "Selección requerida",
                "Debe seleccionar un estudiante de la tabla.",
                QMessageBox.Warning
            ).exec()
            return
        
        estudiante_id = int(estudiante.get("ID", 0))
        if not estudiante_id:
            crear_msgbox(
                self,
                "Error",
                "No se pudo obtener el ID del estudiante.",
                QMessageBox.Critical
            ).exec()
            return
        
        # Validar datos de la sección actual
        if not self.seccion_actual:
            crear_msgbox(
                self,
                "Error",
                "No se pudo obtener información de la sección actual.",
                QMessageBox.Critical
            ).exec()
            return
        
        grado_actual = self.seccion_actual.get("grado")
        nivel_actual = self.seccion_actual.get("nivel")
        año_actual = AnioEscolarModel.obtener_actual()
        
        if not año_actual:
            crear_msgbox(
                self,
                "Error",
                "No hay año escolar activo.",
                QMessageBox.Critical
            ).exec()
            return
        
        # Obtener secciones del mismo grado y nivel
        todas_secciones = SeccionesModel.obtener_todas(año_actual["id"])
        
        secciones_disponibles = [
            sec for sec in todas_secciones
            if sec.get("grado") == grado_actual 
            and sec.get("nivel") == nivel_actual
            and sec.get("id") != self.seccion_id
            and sec.get("activo", 1) == 1
        ]
        
        if not secciones_disponibles:
            crear_msgbox(
                self,
                "Sin opciones",
                f"No hay otras secciones disponibles del grado {grado_actual}.",
                QMessageBox.Information
            ).exec()
            return
        
        # Abrir diálogo de selección
        dialog = DialogMoverEstudiante(secciones_disponibles, self.seccion_id, self)
        if dialog.exec() == QDialog.Accepted and dialog.seccion_seleccionada:
            nueva_seccion_id = dialog.seccion_seleccionada
            
            # Obtener información de la sección destino
            seccion_destino = next(
                (s for s in secciones_disponibles if s['id'] == nueva_seccion_id),
                None
            )
            destino_texto = f"{seccion_destino['grado']} {seccion_destino['letra']}" if seccion_destino else "sección seleccionada"
            
            estudiante_nombre = f"{estudiante.get('Nombres', '')} {estudiante.get('Apellidos', '')}"
            
            # Confirmar movimiento
            confirmar = crear_msgbox(
                self,
                "Confirmar movimiento",
                f"¿Está seguro de mover a {estudiante_nombre} a la sección {destino_texto}?",
                QMessageBox.Question,
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            
            if confirmar.exec() == QMessageBox.StandardButton.Yes:
                try:
                    # Mover estudiante
                    if EstudianteModel.asignar_a_seccion(
                        estudiante_id, 
                        nueva_seccion_id, 
                        año_actual["anio_inicio"]
                    ):
                        crear_msgbox(
                            self,
                            "Éxito",
                            f"Estudiante movido a la sección {destino_texto} correctamente.",
                            QMessageBox.Information
                        ).exec()
                        
                        # Actualizar tabla y conteo
                        self.tableW_detalles_seccion()
                        self.actualizar_conteo()
                        self.actualizar_tarjetas_secciones()
                    else:
                        crear_msgbox(
                            self,
                            "Error",
                            "No se pudo mover el estudiante.",
                            QMessageBox.Critical
                        ).exec()
                except Exception as err:
                    crear_msgbox(
                        self,
                        "Error",
                        f"Error al mover estudiante: {err}",
                        QMessageBox.Critical
                    ).exec()

    def actualizar_conteo(self):
        """Actualiza el contador de estudiantes."""
        try:
            if self.seccion_id is None:
                self.lblActivos_seccion.setText("0")
                return
            
            año = self.año_escolar['anio_inicio']
            estudiantes_activos = EstudianteModel.listar_por_seccion(
                self.seccion_id, 
                año, 
                incluir_inactivos=False
            )
            conteo = len(estudiantes_activos) if estudiantes_activos else 0
            self.lblActivos_seccion.setText(str(conteo))
        except Exception as err:
            print(f"Error actualizando conteo: {err}")
            self.lblActivos_seccion.setText("0")

    def tableW_detalles_seccion(self):
        """Carga la tabla de estudiantes."""
        try:
            # Obtener estudiantes de la sección
            if self.seccion_id is None:
                self.datos = []
            else:
                self.datos = EstudianteModel.listar_por_seccion(
                    self.seccion_id, 
                    self.año_escolar['anio_inicio']
                ) or []

            columnas = [
                "ID", "Cédula", "Nombres", "Apellidos", "Edad", "Género"
            ]

            # Crear modelo base
            model_estudiantes = QStandardItemModel(len(self.datos), len(columnas))
            model_estudiantes.setHorizontalHeaderLabels(columnas)

            # Poblar modelo
            for fila, registro in enumerate(self.datos):
                items = [
                    QStandardItem(str(registro.get("id", ""))),
                    QStandardItem(str(registro.get("cedula", ""))),
                    QStandardItem(str(registro.get("nombres", ""))),
                    QStandardItem(str(registro.get("apellidos", ""))),
                    QStandardItem(str(registro.get("edad", ""))),
                    QStandardItem(str(registro.get("genero", "") or ""))
                ]

                for col, item in enumerate(items):
                    item.setEditable(False)
                    model_estudiantes.setItem(fila, col, item)

            # Conectar al proxy
            self.proxy_estudiantes.setSourceModel(model_estudiantes)
            self.tableW_seccion.setModel(self.proxy_estudiantes)

            # Delegate
            delegate = EstudianteDelegate(self.tableW_seccion)
            self.tableW_seccion.setItemDelegate(delegate)

            # Configurar tabla
            self.tableW_seccion.setSortingEnabled(True)
            self.tableW_seccion.setAlternatingRowColors(True)
            self.tableW_seccion.setColumnHidden(0, True)

            # Numeración vertical
            for i in range(self.proxy_estudiantes.rowCount()):
                self.proxy_estudiantes.setHeaderData(i, Qt.Vertical, str(i + 1))

            self.actualizar_conteo()

        except Exception as err:
            print(f"Error en tableW_detalles_seccion: {err}")
    
    def obtener_estudiante_seleccionado(self):
        """Obtiene datos del estudiante seleccionado."""
        index = self.tableW_seccion.currentIndex()
        if not index.isValid():
            return None

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
        """Aplica filtro a la tabla de estudiantes."""
        if not hasattr(self, "proxy_estudiantes"):
            return

        # Mapa de columnas
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
        """Extrae datos de un QTableView."""
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

    def actualizar_tarjetas_secciones(self):
        """Actualiza las tarjetas de secciones."""
        if hasattr(self, 'gestion_secciones_ref'):
            if hasattr(self.gestion_secciones_ref, 'actualizar_tarjetas'):
                self.gestion_secciones_ref.actualizar_tarjetas()
                return
        
        # Buscar en jerarquía de parents
        parent = self.parent()
        while parent:
            if hasattr(parent, 'actualizar_tarjetas'):
                parent.actualizar_tarjetas()
                break
            elif hasattr(parent, 'page_gestion_secciones'):
                if hasattr(parent.page_gestion_secciones, 'actualizar_tarjetas'):
                    parent.page_gestion_secciones.actualizar_tarjetas()
                    break
            parent = parent.parent() if parent else None
    
    def desactivar_seccion(self):
        """Desactiva la sección."""
        # Confirmación inicial
        confirmar = crear_msgbox(
            self,
            "Confirmar desactivación",
            "¿Está seguro de desactivar esta sección?\n\n"
            "Solo se puede desactivar si no tiene estudiantes activos.",
            QMessageBox.Question,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if confirmar.exec() != QMessageBox.StandardButton.Yes:
            return
        
        try:
            # Intentar desactivar (el modelo valida estudiantes activos)
            ok, mensaje = SeccionesModel.desactivar(
                self.seccion_id, 
                usuario_actual=self.usuario_actual
            )
            
            if ok:
                crear_msgbox(
                    self,
                    "Éxito",
                    mensaje,
                    QMessageBox.Information
                ).exec()
                
                # Actualizar tarjetas y cerrar ventana
                self.actualizar_tarjetas_secciones()
                self.close()
            else:
                crear_msgbox(
                    self,
                    "No se puede desactivar",
                    mensaje,
                    QMessageBox.Warning
                ).exec()
                
        except Exception as err:
            crear_msgbox(
                self,
                "Error",
                f"Error al desactivar sección: {err}",
                QMessageBox.Critical
            ).exec()