from models.institucion_model import InstitucionModel
from utils.forms import set_campos_editables
from utils.dialogs import crear_msgbox

from PySide6.QtWidgets import QMessageBox

    
def set_campos_editables(self, estado: bool):
        campos = [
            self.lneNombreInstitucion_admin, self.lneCodigoDEA_admin, self.lneDirInstitucion_admin,
            self.lneTlfInstitucion_admin, self.lneCorreoInstitucion_admin
        ]
        campos_solo_lectura = [self.lneUltimaActualizacion_admin]
        set_campos_editables(campos, estado, campos_solo_lectura)

def obtener_datos_institucion():
    return InstitucionModel.obtener_por_id(1)


def guardar_datos(self):
    try:
        institucion_data = {
            "nombre": self.lneNombreInstitucion_admin.text(),
            "codigo_dea": self.lneCodigoDEA_admin.text(),
            "direccion": self.lneDirInstitucion_admin.text(),
            "telefono": self.lneTlfInstitucion_admin.text(),
            "correo": self.lneCorreoInstitucion_admin.text(),
        }

        # Actualizar siempre el mismo registro (ejemplo: id=1)
        InstitucionModel.actualizar(1, institucion_data, self.usuario_actual)

        msg = crear_msgbox(
                self,
                "Éxito",
                "Datos de la institución actualizados correctamente.",
                QMessageBox.Information,
            )
        msg.exec()

        # Refrescar campo de última actualización
        self.cargar_datos()

    except Exception as err:
        msg = crear_msgbox(
                self,
                "Error",
                f"No se pudo guardar cambios: {err}",
                QMessageBox.Critical,
            )
        msg.exec()

def toggle_edicion(self):
    """Alterna entre modo edición y guardado"""
    if self.btnModificar_institucion.text() == "Modificar datos":
        self.set_campos_editables(True)
        self.btnModificar_institucion.setText("Guardar")
    else:
        self.guardar_datos()
        self.set_campos_editables(False)
        self.btnModificar_institucion.setText("Modificar datos")