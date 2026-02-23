import re
from datetime import date

from utils.forms import limpiar_widgets
from utils.edad import calcular_edad
from utils.dialogs import crear_msgbox
from utils.sombras import crear_sombra_flotante
from utils.logo_manager import aplicar_logo_a_label

from ui_compiled.registro_emple_ui import Ui_registro_emple
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import QRegularExpression, Qt
from PySide6.QtGui import QDoubleValidator, QIntValidator, QRegularExpressionValidator

from models.emple_model import EmpleadoModel


class RegistroEmpleado(QDialog, Ui_registro_emple):
    """Formulario de registro de nuevos empleados."""
    
    def __init__(self, usuario_actual, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual

        self.setupUi(self)

        # Configuración de ventana
        self.setWindowTitle("Nuevo registro de empleado")
        self.stackRegistro_emple.setCurrentIndex(0)

        self.aplicar_QValidator()

        # Cargar opciones de cargo, tipo de personal y especialidades
        self.cargar_cargos()
        self.cargar_tipos_personal()
        self.cargar_tipos_especialidades()
        self.aplicar_sombras()

        # Limpiar campo de profesión
        self.lneProfesion_reg_emple.clear()

        # Conectar botones
        self.btnGuardar_reg_emple.clicked.connect(self.guardar_en_bd)

        self.btnLimpiar_reg_emple.clicked.connect(self.limpiar_formulario)

        # Conectar cálculo automático de edad
        self.lneFechaNac_reg_emple.dateChanged.connect(self.actualizar_edad_empleado)
        
        # Aplicar logo institucional dinámico
        aplicar_logo_a_label(self.lblLogo_reg_emple)
    
    def aplicar_sombras(self):
        # Aplicar efectos visuales
        crear_sombra_flotante(self.btnGuardar_reg_emple)
        crear_sombra_flotante(self.btnLimpiar_reg_emple)
        crear_sombra_flotante(self.lneCedula_reg_emple, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lblTitulo_reg_emple, blur_radius=5, y_offset=1)
        crear_sombra_flotante(self.lblLogo_reg_emple, blur_radius=5, y_offset=1)
        crear_sombra_flotante(self.stackRegistro_emple, blur_radius=5, y_offset=1)
    
    def aplicar_QValidator(self):
        """Aplica validadores a los campos de entrada."""
        regex = QRegularExpression(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$")
        validator = QRegularExpressionValidator(regex)
        self.lneCedula_reg_emple.setValidator(QIntValidator())  
        self.lneNum_reg_emple.setValidator(QIntValidator())
        self.lneNombres_reg_emple.setValidator(validator)
        self.lneApellidos_reg_emple.setValidator(validator)
        self.lneHoras_aca_reg_emple.setValidator(QDoubleValidator(0.0, 99.0, 2))
        self.lneHoras_adm_reg_emple.setValidator(QDoubleValidator(0.0, 99.0, 2))
    
    def cargar_cargos(self):
        """Carga las opciones de cargo ordenadas."""
        cargos_ordenados = sorted(EmpleadoModel.CARGO_OPCIONES)
        
        self.cbxCargo_reg_emple.clear()
        self.cbxCargo_reg_emple.addItem("Seleccione un cargo")
        
        # Deshabilitar placeholder
        model = self.cbxCargo_reg_emple.model()
        item0 = model.item(0)
        if item0:
            item0.setEnabled(False)
            item0.setForeground(Qt.GlobalColor.gray)
        
        self.cbxCargo_reg_emple.addItems(cargos_ordenados)
        self.cbxCargo_reg_emple.setMaxVisibleItems(10)
        self.cbxCargo_reg_emple.setCurrentIndex(0)
    
    def cargar_tipos_personal(self):
        """Carga las opciones de tipo de personal ordenadas."""
        tipos_personal_ordenados = sorted(EmpleadoModel.TIPO_PERSONAL_OPCIONES)
        
        self.cbxTipoPersonal_reg_emple.clear()
        self.cbxTipoPersonal_reg_emple.addItem("Seleccione un tipo de personal")
        
        # Deshabilitar placeholder
        model = self.cbxTipoPersonal_reg_emple.model()
        item0 = model.item(0)
        if item0:
            item0.setEnabled(False)
            item0.setForeground(Qt.GlobalColor.gray)
        
        self.cbxTipoPersonal_reg_emple.addItems(tipos_personal_ordenados)
        self.cbxTipoPersonal_reg_emple.setMaxVisibleItems(10)
        self.cbxTipoPersonal_reg_emple.setCurrentIndex(0)
    
    def cargar_tipos_especialidades(self):
        """Carga las opciones de tipo de especialidades ordenadas."""
        tipos_especialidades_ordenados = sorted(EmpleadoModel.TIPO_ESPECIALIDADES)
        
        self.cbxEspecialidad_reg_emple.clear()
        self.cbxEspecialidad_reg_emple.addItem("N/A")
        self.cbxEspecialidad_reg_emple.addItems(tipos_especialidades_ordenados)
        self.cbxEspecialidad_reg_emple.setMaxVisibleItems(8)
        self.cbxEspecialidad_reg_emple.setCurrentIndex(0)

    def limpiar_formulario(self):
        """Limpia todos los campos del formulario."""
        limpiar_widgets(self)
        self.cbxCargo_reg_emple.setCurrentIndex(0)
        self.cbxTipoPersonal_reg_emple.setCurrentIndex(0)
        self.cbxEspecialidad_reg_emple.setCurrentIndex(0)
        self.lneProfesion_reg_emple.clear()
        self.stackRegistro_emple.setCurrentIndex(0)

    def actualizar_edad_empleado(self):
        """Calcula y muestra la edad del empleado."""
        fecha_nac = self.lneFechaNac_reg_emple.date().toPython()
        
        # Validar que no sea futura
        if fecha_nac > date.today():
            self.lneEdad_reg_emple.setText("0")
            return
        
        edad = calcular_edad(fecha_nac)
        self.lneEdad_reg_emple.setText(str(edad))

    def _validar_texto_solo_letras(self, texto, nombre_campo):
        """Valida que el texto contenga solo letras y espacios"""
        if not texto:
            return False, ""
        
        if not re.match(r'^[A-Za-zÁÉÍÓÚÑáéíóúñ\s]+$', texto):
            crear_msgbox(
                self,
                "Formato inválido",
                f"El campo '{nombre_campo}' solo puede contener letras y espacios.",
                QMessageBox.Warning,
            ).exec()
            return False, ""
        
        texto_norm = " ".join(p.capitalize() for p in texto.split())
        return True, texto_norm
    
    def _validar_email(self, email):
        """Valida formato de email (opcional)"""
        if not email:
            return True  # Email opcional
        
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron, email):
            crear_msgbox(
                self,
                "Email inválido",
                "El formato del correo electrónico no es válido.",
                QMessageBox.Warning,
            ).exec()
            return False
        
        return True
    
    def _validar_telefono(self, telefono):
        """Valida formato de teléfono (opcional)"""
        if not telefono:
            return True
        
        if not re.match(r'^[\d\-]+$', telefono):
            crear_msgbox(
                self,
                "Teléfono inválido",
                "El teléfono solo puede contener números y guiones.",
                QMessageBox.Warning,
            ).exec()
            return False
        
        return True
    
    def _validar_cedula(self, cedula):
        """Valida formato de cédula (solo números)"""
        if not cedula:
            return False
        
        if not cedula.isdigit() or len(cedula) < 6:
            crear_msgbox(
                self,
                "Cédula inválida",
                "La cédula debe contener al menos 6 dígitos numéricos.",
                QMessageBox.Warning,
            ).exec()
            return False
        
        return True
    
    def _validar_horas_decimales(self, texto, nombre_campo):
        """Valida y normaliza formato de horas (acepta coma o punto, convierte a punto para BD)"""
        if not texto:
            return True, None
        
        # Reemplazar coma por punto para validación
        texto_normalizado = texto.strip().replace(',', '.')
        
        try:
            valor = float(texto_normalizado)
            
            # Validar rango (0-99.99)
            if valor < 0 or valor > 99.99:
                crear_msgbox(
                    self,
                    "Valor inválido",
                    f"El campo '{nombre_campo}' debe estar entre 0 y 99,99 horas.",
                    QMessageBox.Warning,
                ).exec()
                return False, None
            
            # Validar máximo 2 decimales
            if len(texto_normalizado.split('.')[-1]) > 2:
                crear_msgbox(
                    self,
                    "Formato inválido",
                    f"El campo '{nombre_campo}' solo puede tener hasta 2 decimales.",
                    QMessageBox.Warning,
                ).exec()
                return False, None
            
            # Retornar valor float para la BD
            return True, valor
            
        except ValueError:
            crear_msgbox(
                self,
                "Formato inválido",
                f"El campo '{nombre_campo}' debe ser un número válido (use coma para decimales).",
                QMessageBox.Warning,
            ).exec()
            return False, None

    def guardar_en_bd(self):
        """Guarda el empleado en la BD tras validar todos los campos"""
        
        # --- VALIDACIÓN DE DATOS PERSONALES ---
        
        # Validar cédula
        cedula = self.lneCedula_reg_emple.text().strip()
        if not self._validar_cedula(cedula):
            return
        
        # Validar nombres y apellidos
        nombres = self.lneNombres_reg_emple.text().strip()
        apellidos = self.lneApellidos_reg_emple.text().strip()
        
        valido_nombres, nombres_norm = self._validar_texto_solo_letras(nombres, "Nombres")
        valido_apellidos, apellidos_norm = self._validar_texto_solo_letras(apellidos, "Apellidos")
        
        if not valido_nombres or not valido_apellidos:
            return
        
        # Validar fecha de nacimiento
        fecha_nac = self.lneFechaNac_reg_emple.date().toPython()
        if fecha_nac > date.today():
            crear_msgbox(
                self,
                "Fecha inválida",
                "La fecha de nacimiento no puede ser futura.",
                QMessageBox.Warning,
            ).exec()
            return
        
        # Validar género seleccionado
        genero = self.cbxGenero_reg_emple.currentText().strip()
        if not genero or genero == "Seleccione":
            crear_msgbox(
                self,
                "Campo requerido",
                "Debe seleccionar el género del empleado.",
                QMessageBox.Warning,
            ).exec()
            return
        
        # Validar teléfono
        telefono = self.lneNum_reg_emple.text().strip()
        if not self._validar_telefono(telefono):
            return
        
        # Validar email
        email = self.lneCorreo_reg_emple.text().strip()
        if not self._validar_email(email):
            return
        
        # --- VALIDACIÓN DE DATOS LABORALES ---
        
        # Validar cargo seleccionado
        cargo = self.cbxCargo_reg_emple.currentText().strip()
        if cargo == "Seleccione un cargo" or not cargo:
            crear_msgbox(
                self,
                "Campo requerido",
                "Debe seleccionar un cargo válido.",
                QMessageBox.Warning,
            ).exec()
            return
        
        # Validar título seleccionado
        nivel_instruccion = self.cbxNivel_instruccion_reg_emple.currentText().strip()
        if not nivel_instruccion or nivel_instruccion == "Seleccione":
            crear_msgbox(
                self,
                "Campo requerido",
                "Debe seleccionar el título académico.",
                QMessageBox.Warning,
            ).exec()
            return
        
        # Validar fecha de ingreso
        fecha_ingreso = self.lneFechaIngreso_reg_emple.date().toPython()
        
        # Validar que no sea futura
        if fecha_ingreso > date.today():
            crear_msgbox(
                self,
                "Fecha inválida",
                "La fecha de ingreso no puede ser futura.",
                QMessageBox.Warning,
            ).exec()
            return
        
        # Validar tipo de personal seleccionado
        tipo_personal = self.cbxTipoPersonal_reg_emple.currentText().strip()
        if not tipo_personal or tipo_personal == "Seleccione":
            crear_msgbox(
                self,
                "Campo requerido",
                "Debe seleccionar el tipo de personal.",
                QMessageBox.Warning,
            ).exec()
            return
        
        # --- RECOLECTAR DATOS ---
        # Validar y procesar horas académicas
        horas_acad_text = self.lneHoras_aca_reg_emple.text().strip()
        if horas_acad_text:
            valido, horas_acad = self._validar_horas_decimales(horas_acad_text, "Horas Académicas")
            if not valido:
                return
        else:
            horas_acad = None
        
        # Validar y procesar horas administrativas
        horas_adm_text = self.lneHoras_adm_reg_emple.text().strip()
        if horas_adm_text:
            valido, horas_adm = self._validar_horas_decimales(horas_adm_text, "Horas Administrativas")
            if not valido:
                return
        else:
            horas_adm = None
        
        # Procesar especialidad (si es N/A, guardar como None)
        especialidad_text = self.cbxEspecialidad_reg_emple.currentText().strip()
        especialidad = None if especialidad_text == "N/A" else especialidad_text
        
        # Procesar profesión
        profesion_text = self.lneProfesion_reg_emple.text().strip()
        profesion = profesion_text if profesion_text else None
        
        # Procesar talla de zapatos (int o None)
        talla_z_text = self.lneTallaZ_reg_emple.text().strip()
        talla_zapatos = int(talla_z_text) if talla_z_text and talla_z_text.isdigit() else None
        
        empleado_data = {
            "cedula": cedula,
            "apellidos": apellidos_norm,
            "nombres": nombres_norm,
            "fecha_nac": fecha_nac,
            "genero": genero,
            "direccion": self.lneDir_reg_emple.text().strip(),
            "num_contact": telefono,
            "correo": email,
            "nivel_instruccion": nivel_instruccion,
            "cargo": cargo,
            "fecha_ingreso": fecha_ingreso,
            "num_carnet": self.lneCarnet_reg_emple.text().strip(),
            "rif": self.lneRIF_reg_emple.text().strip(),  
            "centro_votacion": self.lneCentroV_reg_emple.text().strip(),
            "codigo_rac": self.lneRAC_reg_emple.text().strip(),
            "horas_acad": horas_acad,
            "horas_adm": horas_adm,
            "tipo_personal": self.cbxTipoPersonal_reg_emple.currentText().strip(),
            "especialidad": especialidad,
            "lugar_nacimiento": self.lneLugarNac_reg_emple.text().strip() or None,
            "profesion": profesion,
            "talla_camisa": self.lneTallaC_reg_emple.text().strip() or None,
            "talla_pantalon": self.lneTallaP_reg_emple.text().strip() or None,
            "talla_zapatos": talla_zapatos,
            "actividad": self.lneActividad.text().strip() or None,
            "cultural": self.lneCultural.text().strip() or None,
            "tipo_vivienda": self.lneTipo_vivienda.text().strip() or None,
            "condicion_vivienda": self.lneCondicion_vivienda.text().strip() or None,
            "material_vivienda": self.lneMaterial_vivienda.text().strip() or None,
            "tipo_enfermedad": self.lneTipo_enfermedad.text().strip() or None,
            "medicamento": self.lneMedicamento.text().strip() or None,
            "discapacidad": self.lneDiscapacidad.text().strip() or None,
        }

        # Validar campos obligatorios finales
        if not all([nombres_norm, apellidos_norm, cedula]):
            crear_msgbox(
                self,
                "Campos incompletos",
                "Complete los campos obligatorios:\n- Cédula\n- Nombres\n- Apellidos",
                QMessageBox.Warning,
            ).exec()
            return

        # --- GUARDAR EN BD ---
        try:
            ok, mensaje = EmpleadoModel.guardar(empleado_data, self.usuario_actual)
            
            if ok:
                crear_msgbox(
                    self,
                    "Éxito",
                    mensaje,
                    QMessageBox.Information,
                ).exec()
                self.accept()  # Cerrar con código de éxito
            else:
                crear_msgbox(
                    self,
                    "Error al guardar",
                    mensaje,
                    QMessageBox.Warning,
                ).exec()
                
        except Exception as err:
            crear_msgbox(
                self,
                "Error inesperado",
                f"No se pudo guardar: {err}",
                QMessageBox.Critical,
            ).exec()
