import re
from PySide6.QtWidgets import QMessageBox

from models.institucion_model import InstitucionModel
from utils.dialogs import crear_msgbox


def cargar_datos_institucion(self):
    """Carga los datos de la institución en el formulario."""
    try:
        datos = InstitucionModel.obtener_por_id(1)
        
        if not datos:
            # Intentar inicializar si no existe
            ok, mensaje = InstitucionModel.inicializar_si_no_existe()
            if ok:
                datos = InstitucionModel.obtener_por_id(1)
            else:
                crear_msgbox(
                    self,
                    "Error",
                    f"No se pudo cargar datos de la institución: {mensaje}",
                    QMessageBox.Critical
                ).exec()
                return
        
        # Rellenar campos básicos (siempre presentes)
        self.lneNombreInstitucion_admin.setText(str(datos.get("nombre", "")))
        self.lneCodigoDEA_admin.setText(str(datos.get("codigo_dea", "")))
        self.lneDirInstitucion_admin.setText(str(datos.get("direccion", "")))
        self.lneTlfInstitucion_admin.setText(str(datos.get("telefono", "")))
        self.lneCorreoInstitucion_admin.setText(str(datos.get("correo", "")))
        
        # Campos opcionales (verificar si existen en la UI)
        if hasattr(self, 'lneCodigoDependencia_admin'):
            self.lneCodigoDependencia_admin.setText(str(datos.get("codigo_dependencia", "")))
        
        if hasattr(self, 'lneCodigoEstadistico_admin'):
            self.lneCodigoEstadistico_admin.setText(str(datos.get("codigo_estadistico", "")))
        
        if hasattr(self, 'lneRIF_admin'):
            self.lneRIF_admin.setText(str(datos.get("rif", "")))
        
        if hasattr(self, 'lneDirector_admin'):
            self.lneDirector_admin.setText(str(datos.get("director", "")))
        
        if hasattr(self, 'lneDirectorCI_admin'):
            self.lneDirectorCI_admin.setText(str(datos.get("director_ci", "")))
        
        # Última actualización (solo lectura)
        fecha_actualizacion = datos.get("actualizado_en")
        if fecha_actualizacion:
            if hasattr(fecha_actualizacion, 'strftime'):
                texto_fecha = fecha_actualizacion.strftime("%d-%m-%Y %H:%M:%S")
            else:
                texto_fecha = str(fecha_actualizacion)
            self.lneUltimaActualizacion_admin.setText(texto_fecha)
        else:
            self.lneUltimaActualizacion_admin.setText("Sin actualizar")
        
    except Exception as err:
        crear_msgbox(
            self,
            "Error",
            f"No se pudo cargar los datos: {err}",
            QMessageBox.Critical
        ).exec()


def set_campos_editables_institucion(self, estado: bool):
    """Habilita/deshabilita la edición de campos."""
    # Campos editables básicos
    campos = [
        self.lneNombreInstitucion_admin,
        self.lneCodigoDEA_admin,
        self.lneDirInstitucion_admin,
        self.lneTlfInstitucion_admin,
        self.lneCorreoInstitucion_admin
    ]
    
    # Campos opcionales
    if hasattr(self, 'lneCodigoDependencia_admin'):
        campos.append(self.lneCodigoDependencia_admin)
    
    if hasattr(self, 'lneCodigoEstadistico_admin'):
        campos.append(self.lneCodigoEstadistico_admin)
    
    if hasattr(self, 'lneRIF_admin'):
        campos.append(self.lneRIF_admin)
    
    if hasattr(self, 'lneDirector_admin'):
        campos.append(self.lneDirector_admin)
    
    if hasattr(self, 'lneDirectorCI_admin'):
        campos.append(self.lneDirectorCI_admin)
    
    # Aplicar estado
    for campo in campos:
        campo.setReadOnly(not estado)
        if estado:
            campo.setStyleSheet("background-color: white;")
        else:
            campo.setStyleSheet("background-color: #f0f0f0;")
    
    # Última actualización siempre solo lectura
    self.lneUltimaActualizacion_admin.setReadOnly(True)
    self.lneUltimaActualizacion_admin.setStyleSheet("background-color: #e0e0e0;")


def _validar_email_institucion(email: str) -> tuple[bool, str]:
    """Valida formato de email."""
    if not email:
        return True, ""  # Email opcional
    
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(patron, email):
        return False, "El formato del correo electrónico no es válido"
    
    return True, ""


def _validar_telefono_institucion(telefono: str) -> tuple[bool, str]:
    """Valida formato de teléfono."""
    if not telefono:
        return True, ""  # Teléfono opcional
    
    if not re.match(r'^[\d\-\+\(\)\s]+$', telefono):
        return False, "El teléfono solo puede contener números y caracteres: + - ( )"
    
    return True, ""


def _validar_rif_institucion(rif: str) -> tuple[bool, str]:
    """Valida formato de RIF."""
    if not rif:
        return True, ""  # RIF opcional
    
    # Formato: J-12345678-9 o similar
    if not re.match(r'^[JGVE]-?\d{8,9}-?\d?$', rif.upper()):
        return False, "El formato del RIF no es válido (ej: J-12345678-9)"
    
    return True, ""


def guardar_datos_institucion(self):
    """Valida y guarda los datos de la institución en MainWindow"""
    try:
        # --- RECOLECTAR DATOS ---
        nombre = self.lneNombreInstitucion_admin.text().strip()
        codigo_dea = self.lneCodigoDEA_admin.text().strip()
        direccion = self.lneDirInstitucion_admin.text().strip()
        telefono = self.lneTlfInstitucion_admin.text().strip()
        correo = self.lneCorreoInstitucion_admin.text().strip()
        
        # Campos opcionales
        codigo_dep = ""
        codigo_est = ""
        rif = ""
        director = ""
        director_ci = ""
        
        if hasattr(self, 'lneCodigoDependencia_admin'):
            codigo_dep = self.lneCodigoDependencia_admin.text().strip()
        
        if hasattr(self, 'lneCodigoEstadistico_admin'):
            codigo_est = self.lneCodigoEstadistico_admin.text().strip()
        
        if hasattr(self, 'lneRIF_admin'):
            rif = self.lneRIF_admin.text().strip()
        
        if hasattr(self, 'lneDirector_admin'):
            director = self.lneDirector_admin.text().strip()
        
        if hasattr(self, 'lneDirectorCI_admin'):
            director_ci = self.lneDirectorCI_admin.text().strip()

        # --- VALIDACIONES ---
        
        # Campos obligatorios
        if not nombre:
            crear_msgbox(
                self,
                "Campo requerido",
                "El nombre de la institución es obligatorio.",
                QMessageBox.Warning
            ).exec()
            return
        
        if not codigo_dea:
            crear_msgbox(
                self,
                "Campo requerido",
                "El código DEA es obligatorio.",
                QMessageBox.Warning
            ).exec()
            return
        
        if not direccion:
            crear_msgbox(
                self,
                "Campo requerido",
                "La dirección es obligatoria.",
                QMessageBox.Warning
            ).exec()
            return

        # Validar email
        email_valido, msg_email = _validar_email_institucion(correo)
        if not email_valido:
            crear_msgbox(
                self,
                "Email inválido",
                msg_email,
                QMessageBox.Warning
            ).exec()
            return

        # Validar teléfono
        tel_valido, msg_tel = _validar_telefono_institucion(telefono)
        if not tel_valido:
            crear_msgbox(
                self,
                "Teléfono inválido",
                msg_tel,
                QMessageBox.Warning
            ).exec()
            return

        # Validar RIF
        rif_valido, msg_rif = _validar_rif_institucion(rif)
        if not rif_valido:
            crear_msgbox(
                self,
                "RIF inválido",
                msg_rif,
                QMessageBox.Warning
            ).exec()
            return

        # Validar cédula del director (opcional)
        if director_ci:
            ci_limpia = director_ci.replace(".", "").replace("-", "")
            if not ci_limpia.isdigit():
                crear_msgbox(
                    self,
                    "Cédula inválida",
                    "La cédula del director debe ser numérica.",
                    QMessageBox.Warning
                ).exec()
                return

        # --- PREPARAR DATOS ---
        institucion_data = {
            "nombre": nombre,
            "codigo_dea": codigo_dea,
            "codigo_dependencia": codigo_dep,
            "codigo_estadistico": codigo_est,
            "rif": rif,
            "direccion": direccion,
            "telefono": telefono,
            "correo": correo,
            "director": director,
            "director_ci": director_ci,
        }

        # --- GUARDAR EN BD ---
        ok, mensaje = InstitucionModel.actualizar(1, institucion_data, self.usuario_actual)

        if ok:
            crear_msgbox(
                self,
                "Éxito",
                mensaje,
                QMessageBox.Information
            ).exec()

            # Refrescar datos
            cargar_datos_institucion(self)
        else:
            crear_msgbox(
                self,
                "Error al guardar",
                mensaje,
                QMessageBox.Warning
            ).exec()

    except Exception as err:
        crear_msgbox(
            self,
            "Error inesperado",
            f"No se pudo guardar cambios: {err}",
            QMessageBox.Critical
        ).exec()


def toggle_edicion_institucion(self):
    """Alterna entre modo edición y guardado en MainWindow"""
    if self.btnModificar_institucion.text() == "Modificar datos":
        set_campos_editables_institucion(self, True)
        self.btnModificar_institucion.setText("Guardar")
    else:
        guardar_datos_institucion(self)
        set_campos_editables_institucion(self, False)
        self.btnModificar_institucion.setText("Modificar datos")