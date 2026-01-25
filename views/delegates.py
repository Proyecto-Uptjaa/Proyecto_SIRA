from PySide6.QtWidgets import QStyledItemDelegate
from PySide6.QtGui import QColor, QBrush

class BaseEstadoDelegate(QStyledItemDelegate):
    def __init__(self, parent=None, estado_columna=16):
        super().__init__(parent)
        self.estado_columna = estado_columna

    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        try:
            model = index.model()
            # si es proxy, mapear al modelo fuente
            if hasattr(model, "sourceModel"):
                source_index = model.mapToSource(index)
                source_model = model.sourceModel()
            else:
                source_index = index
                source_model = model

            # comprobar que el modelo fuente tenga columnas y método item
            if not (hasattr(source_model, "item") and hasattr(source_model, "columnCount")):
                return

            # comprobar que la columna de estado exista en el modelo fuente
            if source_model.columnCount() <= self.estado_columna:
                return

            # obtener el item de la columna de estado de forma segura
            row = source_index.row()
            estado_item = source_model.item(row, self.estado_columna)
            if estado_item is None:
                return 

            activo = str(estado_item.text()).strip()
            if activo == "":
                return 

            # Solo aplicar fondo para inactivos
            val = activo.lower()
            if val in ("0", "inactivo", "false", "f", "no"):
                option.backgroundBrush = QBrush(QColor("#c2c2c2"))  # color para inactivos

        except Exception:
            return

class EstudianteDelegate(BaseEstadoDelegate):
    def __init__(self, parent=None, estado_columna=16):
        super().__init__(parent, estado_columna)

class EmpleadoDelegate(BaseEstadoDelegate):
    def __init__(self, parent=None, estado_columna=16):
        super().__init__(parent, estado_columna)

class UsuarioDelegate(BaseEstadoDelegate):
    def __init__(self, parent=None, estado_columna=16):
        super().__init__(parent, estado_columna)