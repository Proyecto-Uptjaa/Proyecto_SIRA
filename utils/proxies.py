from PySide6.QtCore import QSortFilterProxyModel, Qt

class ProxyConEstado(QSortFilterProxyModel):
    def __init__(self, columna_estado, parent=None):
        super().__init__(parent)
        self.mostrar_inactivos = False
        self.columna_estado = columna_estado

    def setMostrarInactivos(self, valor: bool):
        self.mostrar_inactivos = valor
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row, source_parent):
        # Filtro de texto (buscador)
        if not super().filterAcceptsRow(source_row, source_parent):
            return False

        # Filtro de estado
        if not self.mostrar_inactivos:
            idx = self.sourceModel().index(source_row, self.columna_estado, source_parent)
            estado = self.sourceModel().data(idx, Qt.DisplayRole)
            if estado and str(estado).strip().lower() == "inactivo":
                return False

        return True