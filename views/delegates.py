from PySide6.QtWidgets import QStyledItemDelegate
from PySide6.QtGui import QColor, QBrush

class EstudianteDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        # Obtener el modelo fuente y el índice original
        source_model = index.model().sourceModel()
        source_index = index.model().mapToSource(index)
        
        # Obtener el valor de la columna "Activo" (columna 17)
        activo = source_model.item(source_index.row(), 17).text()
        
        if activo == "Inactivo":
            # Color gris claro para estudiantes inactivos
            option.backgroundBrush = QBrush(QColor(220, 220, 220))

class EmpleadoDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        # Obtener el modelo fuente y el índice original
        source_model = index.model().sourceModel()
        source_index = index.model().mapToSource(index)
        
        # Obtener el valor de la columna "Activo" (columna 14)
        activo = source_model.item(source_index.row(), 14).text()
        
        if activo == "Inactivo":
            # Color gris claro para empleados inactivos
            option.backgroundBrush = QBrush(QColor(220, 220, 220))

class UsuarioDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        # Obtener el modelo fuente y el índice original
        source_model = index.model().sourceModel()
        source_index = index.model().mapToSource(index)
        
        # Obtener el valor de la columna "Activo" (columna 3)
        activo = source_model.item(source_index.row(), 3).text()
        
        if activo == "Inactivo":
            # Color gris claro para empleados inactivos
            option.backgroundBrush = QBrush(QColor(220, 220, 220))