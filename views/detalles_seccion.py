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


class DialogMoverEstudiante(QDialog, Ui_mover_estudiante):
    """Diálogo para mover estudiante a otra sección"""
    def __init__(self, secciones_disponibles, seccion_actual_id, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Mover estudiante a otra sección")
        self.seccion_seleccionada = None
        
        # Limpiar el combo box y cargar secciones disponibles
        self.cbxMover_estudiante.clear()
        
        # Agregar placeholder
        self.cbxMover_estudiante.addItem("Seleccione una sección")
        
        # Deshabilitar placeholder
        model = self.cbxMover_estudiante.model()
        item0 = model.item(0)
        if item0 is not None:
            item0.setEnabled(False)
            item0.setForeground(Qt.GlobalColor.gray)
        
        # Agregar secciones disponibles
        for sec in secciones_disponibles:
            texto = f"{sec['grado']} {sec['letra']}"
            self.cbxMover_estudiante.addItem(texto, sec['id'])
        
        # Establecer placeholder como selección inicial
        self.cbxMover_estudiante.setCurrentIndex(0)
        
        # Conectar botones
        self.buttonBox.accepted.connect(self.aceptar)
        self.buttonBox.rejected.connect(self.reject)
    
    def aceptar(self):
        """Valida que se haya seleccionado una sección antes de aceptar"""
        seccion_id = self.cbxMover_estudiante.currentData()
        if seccion_id and self.cbxMover_estudiante.currentIndex() > 0:
            self.seccion_seleccionada = seccion_id
            self.accept()
        else:
            msg = crear_msgbox(
                self,
                "Seleccionar sección",
                "Debe seleccionar una sección de destino.",
                QMessageBox.Warning
            )
            msg.exec()


class DetallesSeccion(QWidget, Ui_detalle_seccion):
    def __init__(self, usuario_actual, seccion_id, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.seccion_id = int(seccion_id) if seccion_id is not None else None
        self.seccion_actual = None  # Guardar datos de la sección actual
        self.setupUi(self)
        
        # Mostrar título con grado y letra de la sección
        try:
            secciones = SeccionesModel.obtener_todas()
            sec = next((s for s in secciones if int(s.get("id", 0)) == int(self.seccion_id)), None)
            if sec:
                self.seccion_actual = sec  # Guardar datos de la sección
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

        # Conectar botón de mover estudiante
        self.btnMover_estudiante.clicked.connect(self.mover_estudiante)
        self.btnDesactivar_seccion.clicked.connect(self.desactivar_seccion)

        # Proxy para filtrado
        self.proxy_estudiantes = QSortFilterProxyModel(self)
        self.proxy_estudiantes.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.proxy_estudiantes.setFilterKeyColumn(-1)

        self.tableW_detalles_seccion()
        self.actualizar_conteo()  # Actualizar conteo después de cargar la tabla

    def mover_estudiante(self):
        """Mueve un estudiante seleccionado a otra sección del mismo grado"""
        # Obtener estudiante seleccionado
        estudiante = self.obtener_estudiante_seleccionado()
        if not estudiante:
            msg = crear_msgbox(
                self,
                "Seleccionar estudiante",
                "Debe seleccionar un estudiante de la tabla.",
                QMessageBox.Warning
            )
            msg.exec()
            return
        
        estudiante_id = int(estudiante.get("ID", 0))
        if not estudiante_id:
            msg = crear_msgbox(
                self,
                "Error",
                "No se pudo obtener el ID del estudiante.",
                QMessageBox.Critical
            )
            msg.exec()
            return
        
        # Obtener secciones del mismo grado
        if not self.seccion_actual:
            msg = crear_msgbox(
                self,
                "Error",
                "No se pudo obtener información de la sección actual.",
                QMessageBox.Critical
            )
            msg.exec()
            return
        
        grado_actual = self.seccion_actual.get("grado")
        nivel_actual = self.seccion_actual.get("nivel")
        año = AnioEscolarModel.obtener_actual("anio_inicio")
        
        # Obtener todas las secciones activas del año
        todas_secciones = SeccionesModel.obtener_todas(año)
        
        # Filtrar secciones del mismo grado y nivel, excluyendo la actual
        secciones_disponibles = [
            sec for sec in todas_secciones
            if sec.get("grado") == grado_actual 
            and sec.get("nivel") == nivel_actual
            and sec.get("id") != self.seccion_id
            and sec.get("activo", 1) == 1  # Solo secciones activas
        ]
        
        if not secciones_disponibles:
            msg = crear_msgbox(
                self,
                "Sin opciones",
                f"No hay otras secciones disponibles del grado {grado_actual}.",
                QMessageBox.Information
            )
            msg.exec()
            return
        
        # Abrir diálogo para seleccionar sección destino
        dialog = DialogMoverEstudiante(secciones_disponibles, self.seccion_id, self)
        if dialog.exec() == QDialog.Accepted and dialog.seccion_seleccionada:
            nueva_seccion_id = dialog.seccion_seleccionada
            
            # Obtener información de la sección destino para el mensaje
            seccion_destino = next(
                (s for s in secciones_disponibles if s['id'] == nueva_seccion_id),
                None
            )
            if seccion_destino:
                destino_texto = f"{seccion_destino['grado']} {seccion_destino['letra']}"
            else:
                destino_texto = "sección seleccionada"
            
            estudiante_nombre = f"{estudiante.get('Nombres', '')} {estudiante.get('Apellidos', '')}"
            
            # Confirmar acción
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
                    # Mover estudiante a la nueva sección
                    if EstudianteModel.asignar_a_seccion(estudiante_id, nueva_seccion_id, año):
                        msg = crear_msgbox(
                            self,
                            "Éxito",
                            f"Estudiante movido a la sección {destino_texto} correctamente.",
                            QMessageBox.Information
                        )
                        msg.exec()
                        
                        # Actualizar tabla y conteo
                        self.tableW_detalles_seccion()
                        self.actualizar_conteo()
                        
                        # Actualizar tarjetas en GestionSeccionesPage si está disponible
                        self.actualizar_tarjetas_secciones()
                    else:
                        msg = crear_msgbox(
                            self,
                            "Error",
                            "No se pudo mover el estudiante.",
                            QMessageBox.Critical
                        )
                        msg.exec()
                except Exception as err:
                    msg = crear_msgbox(
                        self,
                        "Error",
                        f"Error al mover estudiante: {err}",
                        QMessageBox.Critical
                    )
                    msg.exec()

    def actualizar_conteo(self):
        try:
            if self.seccion_id is None:
                self.lblActivos_seccion.setText("0")
            else:
                año = datetime.now().year
                estudiantes_activos = EstudianteModel.listar_por_seccion(
                    self.seccion_id, año, incluir_inactivos=False
                )
                conteo = len(estudiantes_activos) if estudiantes_activos else 0
                self.lblActivos_seccion.setText(str(conteo))
        except Exception as err:
            print(f"Error actualizando conteo: {err}")
            self.lblActivos_seccion.setText("0")


    def tableW_detalles_seccion(self):
        try:
            # Traer estudiantes asignados a la sección (usa año actual)
            if self.seccion_id is None:
                datos = []
            else:
                año = AnioEscolarModel.obtener_actual()
                self.datos = EstudianteModel.listar_por_seccion(self.seccion_id, año["anio_inicio"]) or []
                datos = self.datos   

            columnas = [
                "ID", "Cédula", "Nombres", "Apellidos",
                "Edad", "Género"
            ]

            # Crear modelo base (source model)
            model_estudiantes = QStandardItemModel(len(datos), len(columnas))
            model_estudiantes.setHorizontalHeaderLabels(columnas)

            # Poblar modelo
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

            # Delegate
            delegate = EstudianteDelegate(self.tableW_seccion)
            self.tableW_seccion.setItemDelegate(delegate)

            # Configurar tabla
            self.tableW_seccion.setSortingEnabled(True)
            self.tableW_seccion.setAlternatingRowColors(True)
            self.tableW_seccion.setColumnHidden(0, True)  # ocultar ID

            # Numeración vertical
            # Debe establecerse en el modelo que usa la vista -> el proxy
            for i in range(self.proxy_estudiantes.rowCount()):
                self.proxy_estudiantes.setHeaderData(i, Qt.Vertical, str(i + 1), Qt.DisplayRole)

            # Actualizar conteo de estudiantes activos
            self.actualizar_conteo()

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

    def actualizar_tarjetas_secciones(self):
        """Busca y actualiza las tarjetas de secciones usando la referencia guardada"""
        # Usar la referencia guardada
        if hasattr(self, 'gestion_secciones_ref'):
            if hasattr(self.gestion_secciones_ref, 'actualizar_tarjetas'):
                self.gestion_secciones_ref.actualizar_tarjetas()
                return
        
        # Si no hay referencia, buscar en el parent
        if hasattr(self.parent(), 'actualizar_tarjetas'):
            self.parent().actualizar_tarjetas()
        # Si el parent es MainWindow, buscar GestionSeccionesPage
        elif hasattr(self.parent(), 'page_gestion_secciones'):
            if hasattr(self.parent().page_gestion_secciones, 'actualizar_tarjetas'):
                self.parent().page_gestion_secciones.actualizar_tarjetas()
        # Buscar recursivamente en la jerarquía de parents
        else:
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
        confirm = crear_msgbox(
            self,
            "Confirmación",
            "¿Seguro/a que desea inactivar esta sección?",
            QMessageBox.Question,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        if confirm.exec() == QMessageBox.StandardButton.Yes:

            if self.datos:
                msg = crear_msgbox(
                    self,
                    "No se puede desactivar sección",
                    "No es posible desactivar secciones con estudiantes activos.\n"
                    "Mueva los estudiantes de seccion, e intente desactivarla nuevamente.",
                    QMessageBox.Information
                )
                msg.exec()
                return
            else:
                SeccionesModel.desactivar(self.seccion_id)
                msg = crear_msgbox(
                    self,
                    "Sección desactivada",
                    "La sección se ha inactivado correctamente!",
                    QMessageBox.Information
                )
                msg.exec()
                self.close()
        else:
            return