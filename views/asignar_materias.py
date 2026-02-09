from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QCheckBox, QMessageBox, QWidget
)
from PySide6.QtCore import Qt

from ui_compiled.asignar_materias_ui import Ui_asignar_materias
from models.materias_model import MateriasModel
from utils.dialogs import crear_msgbox
from utils.sombras import crear_sombra_flotante


class AsignarMateriasDialog(QDialog, Ui_asignar_materias):
    """Diálogo para asignar materias a una sección."""
    
    def __init__(
        self, 
        seccion_id: int,
        nivel: str,
        grado: str,
        usuario_actual: dict,
        parent=None
    ):
        super().__init__(parent)
        self.seccion_id = seccion_id
        self.nivel = nivel
        self.grado = grado
        self.usuario_actual = usuario_actual
        self.checkboxes = []
        
        self.setupUi(self)
        self.setWindowTitle(f"Asignar Materias - {grado}")
        
        # Actualizar título
        self.lblTitulo_asignar_materia.setText(f"Materias para {nivel} - {grado}")
        
        # Configurar UI
        self.setup_materias()
        
        # Conectar botones
        self.btnGuardar_asignar_materias.clicked.connect(self.guardar)
        self.btnCancelar_asignar_materias.clicked.connect(self.reject)
        self.chkSelec_todas.stateChanged.connect(self.toggle_todas)
        
        # Aplicar sombras
        crear_sombra_flotante(self.btnGuardar_asignar_materias)
        crear_sombra_flotante(self.btnCancelar_asignar_materias)
    
    def setup_materias(self):
        """Configura los checkboxes de materias."""
        # Limpiar checkbox de ejemplo del diseñador
        if self.chkAsignar_materia:
            self.chkAsignar_materia.setVisible(False)
        
        # Obtener materias disponibles para este nivel/grado
        materias_disponibles = MateriasModel.obtener_por_nivel_grado(
            self.nivel, self.grado
        )
        
        # Obtener materias ya asignadas a la sección
        materias_asignadas = []
        if self.seccion_id:
            materias_asignadas = MateriasModel.obtener_ids_materias_seccion(self.seccion_id)
        
        # Obtener el layout del widget contenedor
        layout = self.widget_asignar_materia.layout()
        
        if not materias_disponibles:
            # Mostrar mensaje si no hay materias configuradas
            from PySide6.QtWidgets import QLabel
            lbl = QLabel("No hay materias configuradas para este grado.\n"
                        "Configure las materias en Administración → Materias.")
            lbl.setStyleSheet("color: #e74c3c; font-style: italic;")
            lbl.setWordWrap(True)
            layout.addWidget(lbl)
            return
        
        # Crear checkbox por cada materia
        for materia in materias_disponibles:
            chk = QCheckBox(materia["nombre"])
            chk.setProperty("materia_id", materia["id"])
            chk.setStyleSheet("""
                QCheckBox {
                    spacing: 8px;
                    font-size: 12px;
                    padding: 5px;
                }
                QCheckBox::indicator {
                    width: 20px;
                    height: 20px;
                    border: 2px solid #2c3e50;
                    border-radius: 5px;
                    background: white;
                }
                QCheckBox::indicator:checked {
                    background: #2980b9;
                    border-color: #1565C0;
                }
                QCheckBox::indicator:hover {
                    border-color: #1565C0;
                }
            """)
            
            # Marcar si ya está asignada
            if materia["id"] in materias_asignadas:
                chk.setChecked(True)
            
            layout.addWidget(chk)
            self.checkboxes.append(chk)
        
        # Agregar spacer al final
        layout.addStretch()
        
        # Verificar estado de "Seleccionar todas"
        self.actualizar_estado_selec_todas()
    
    def toggle_todas(self, estado):
        """Marca o desmarca todas las materias."""
        for chk in self.checkboxes:
            chk.setChecked(bool(estado))
    
    def actualizar_estado_selec_todas(self):
        """Actualiza el checkbox de seleccionar todas según el estado actual."""
        if not self.checkboxes:
            return
        
        todas_marcadas = all(chk.isChecked() for chk in self.checkboxes)
        self.chkSelec_todas.blockSignals(True)
        self.chkSelec_todas.setChecked(todas_marcadas)
        self.chkSelec_todas.blockSignals(False)
    
    def obtener_materias_seleccionadas(self):
        """Retorna lista de IDs de materias seleccionadas."""
        return [
            chk.property("materia_id")
            for chk in self.checkboxes
            if chk.isChecked()
        ]
    
    def guardar(self):
        """Guarda las materias asignadas."""
        materias_ids = self.obtener_materias_seleccionadas()
        
        if not materias_ids:
            msg = crear_msgbox(
                self, "Confirmar",
                "No ha seleccionado ninguna materia.\n"
                "¿Desea continuar sin asignar materias?",
                QMessageBox.Question,
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            if msg.exec() == QMessageBox.StandardButton.No:
                return
        
        # Si es una sección nueva (sin ID), solo retornar las selecciones
        if not self.seccion_id:
            self.materias_seleccionadas = materias_ids
            self.accept()
            return
        
        # Guardar en BD
        ok, msg = MateriasModel.asignar_a_seccion(
            self.seccion_id,
            materias_ids,
            self.usuario_actual
        )
        
        if ok:
            crear_msgbox(self, "Éxito", msg, QMessageBox.Information).exec()
            self.accept()
        else:
            crear_msgbox(self, "Error", msg, QMessageBox.Warning).exec()
    
    def get_materias_seleccionadas(self):
        """Retorna las materias seleccionadas (para uso externo)."""
        if hasattr(self, 'materias_seleccionadas'):
            return self.materias_seleccionadas
        return self.obtener_materias_seleccionadas()
