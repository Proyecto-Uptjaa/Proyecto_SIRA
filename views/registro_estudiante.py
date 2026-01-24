import re
from datetime import date

from utils.dialogs import crear_msgbox
from utils.forms import limpiar_widgets
from utils.edad import calcular_edad
from utils.sombras import crear_sombra_flotante
from ui_compiled.registro_estu_ui import Ui_registro_estu
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import QDate

from models.repre_model import RepresentanteModel
from models.estu_model import EstudianteModel


class NuevoRegistro(QDialog, Ui_registro_estu):
    """Formulario de registro de nuevos estudiantes."""
    
    def __init__(self, usuario_actual, año_escolar, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.año_escolar = año_escolar

        self.setupUi(self)

        # Configuración inicial de la ventana
        self.setWindowTitle("Nuevo registro de estudiante")
        self.stackRegistro_estudiante.setCurrentIndex(0)
        
        # Conectar botones de navegación y acciones
        self.btnGenCedula_reg_estu.clicked.connect(self.generar_cedula_estudiantil)
        self.btnGuardar_reg_estu.clicked.connect(self.guardar_en_bd)
        self.btnConsult_ci_repre.clicked.connect(self.buscar_representante)
        self.btnStudentDatos_registro.clicked.connect(lambda: self.cambiar_pagina_registro_estudiante(0))
        self.btnRepre_registro.clicked.connect(lambda: self.cambiar_pagina_registro_estudiante(1))
        self.btnLimpiar_reg_estu.clicked.connect(self.limpiar_formulario)

        # Conectar cálculo automático de edad cuando cambia la fecha
        self.lneFechaNac_reg_estu.dateChanged.connect(self.actualizar_edad_estudiante)
        self.lneFechaNac_reg_estu_repre.dateChanged.connect(self.actualizar_edad_representante)

        # Variable para almacenar la cédula generada
        self.cedula_estudiantil_generada = None

        # Cargar secciones disponibles del año escolar actual
        self.cargar_secciones_en_combos()
        
        # Conectar los combos en cascada (nivel → grado → sección)
        self.cbxTipoEdu_reg_estu.currentTextChanged.connect(self.actualizar_grados)
        self.cbxGrado_reg_estu.currentTextChanged.connect(self.actualizar_secciones)
        
        # Actualizar grados si hay un valor por defecto seleccionado
        nivel_actual = self.cbxTipoEdu_reg_estu.currentText()
        if nivel_actual:
            self.actualizar_grados(nivel_actual)
        
        # Aplicar efectos visuales (sombras flotantes)
        self._aplicar_sombras()

    def _aplicar_sombras(self):
        """Aplica sombras a elementos de la interfaz."""
        crear_sombra_flotante(self.btnGenCedula_reg_estu)
        crear_sombra_flotante(self.btnGuardar_reg_estu)
        crear_sombra_flotante(self.btnLimpiar_reg_estu)
        crear_sombra_flotante(self.btnConsult_ci_repre)
        crear_sombra_flotante(self.btnStudentDatos_registro)
        crear_sombra_flotante(self.btnRepre_registro)
        crear_sombra_flotante(self.lneCedula_reg_estu, blur_radius=8, y_offset=1)
        crear_sombra_flotante(self.lblTitulo_reg_estu, blur_radius=5, y_offset=1)
        crear_sombra_flotante(self.lblLogo_reg_estu, blur_radius=5, y_offset=1)

    def limpiar_formulario(self):
        """Limpia los campos y resetea el formulario."""
        limpiar_widgets(self)
        self.cedula_estudiantil_generada = None
        self.stackRegistro_estudiante.setCurrentIndex(0)
    
    def cargar_secciones_en_combos(self):
        """Carga las secciones activas en los combos."""
        secciones = EstudianteModel.obtener_secciones_activas(self.año_escolar['año_inicio'])

        # Limpiar combos existentes
        self.cbxTipoEdu_reg_estu.clear()
        self.cbxGrado_reg_estu.clear()
        self.cbxSeccion_reg_estu.clear()

        # Estructuras para organizar las secciones
        niveles = set()
        self.grados_por_nivel = {}
        self.secciones_por_grado = {}

        # Organizar las secciones en estructuras jerárquicas
        for sec in secciones:
            nivel = sec["nivel"]
            grado = sec["grado"]
            letra = sec["letra"]

            # Agregar nivel único
            if nivel not in niveles:
                niveles.add(nivel)
                self.cbxTipoEdu_reg_estu.addItem(nivel)

            # Agrupar grados por nivel
            if nivel not in self.grados_por_nivel:
                self.grados_por_nivel[nivel] = set()
            self.grados_por_nivel[nivel].add(grado)

            # Agrupar secciones por grado (guardando letra e id)
            clave = f"{nivel}_{grado}"
            if clave not in self.secciones_por_grado:
                self.secciones_por_grado[clave] = []
            self.secciones_por_grado[clave].append({
                "letra": letra,
                "id": sec["id"]
            })

    def actualizar_grados(self, nivel):
        """Actualiza el combo de grados según el nivel seleccionado."""
        if not nivel:
            return
        
        self.cbxGrado_reg_estu.clear()
        grados = sorted(self.grados_por_nivel.get(nivel, set()))
        
        for g in grados:
            self.cbxGrado_reg_estu.addItem(g)
        
        # Limpiar secciones al cambiar grado
        self.actualizar_secciones("")

    def actualizar_secciones(self, grado):
        """Actualiza el combo de secciones según nivel y grado seleccionados."""
        if not grado:
            self.cbxSeccion_reg_estu.clear()
            return
        
        nivel = self.cbxTipoEdu_reg_estu.currentText()
        clave = f"{nivel}_{grado}"
        self.cbxSeccion_reg_estu.clear()
        
        opciones = self.secciones_por_grado.get(clave, [])
        for opt in opciones:
            # Guardar la letra como texto visible y el ID como dato asociado
            self.cbxSeccion_reg_estu.addItem(opt["letra"], opt["id"])

    def actualizar_edad_estudiante(self):
        """Calcula y muestra la edad del estudiante basándose en su fecha de nacimiento"""
        qdate = self.lneFechaNac_reg_estu.date()
        fecha_nac = qdate.toPython()
        
        # Validar que la fecha no sea futura
        if fecha_nac > date.today():
            self.lneEdad_reg_estu.setText("0")
            return
        
        edad = calcular_edad(fecha_nac)
        self.lneEdad_reg_estu.setText(str(edad))

    def actualizar_edad_representante(self):
        """Calcula y muestra la edad del representante basándose en su fecha de nacimiento"""
        qdate = self.lneFechaNac_reg_estu_repre.date()
        fecha_nac = qdate.toPython()
        
        # Validar que la fecha no sea futura
        if fecha_nac > date.today():
            self.lneEdad_reg_estu_repre.setText("0")
            return
        
        edad = calcular_edad(fecha_nac)
        self.lneEdad_reg_estu_repre.setText(str(edad))

    def buscar_representante(self):
        """
        Busca un representante existente por cédula y pre-llena el formulario.
        Útil cuando varios hermanos comparten representante.
        """
        cedula_repre = self.lneCedula_reg_estu_repre.text().strip()
        
        # Validar que haya ingresado una cédula
        if not cedula_repre:
            crear_msgbox(
                self,
                "Campo vacío",
                "Ingrese una cédula para buscar.",
                QMessageBox.Warning,
            ).exec()
            return
        
        # Validar formato de cédula (solo números)
        if not cedula_repre.isdigit():
            crear_msgbox(
                self,
                "Cédula inválida",
                "La cédula debe contener solo números.",
                QMessageBox.Warning,
            ).exec()
            return

        try:
            repre = RepresentanteModel.buscar_por_cedula(cedula_repre)
            
            if repre:
                # Pre-llenar todos los campos del representante
                self.lneApellido_reg_estu_repre.setText(repre["apellidos"])
                self.lneNombre_reg_estu_repre.setText(repre["nombres"])

                # Convertir fecha a QDate
                fecha_repre = repre["fecha_nac"]
                if isinstance(fecha_repre, date):
                    self.lneFechaNac_reg_estu_repre.setDate(QDate.fromPyDate(fecha_repre))
                else:
                    y, m, d = map(int, str(fecha_repre).split("-"))
                    self.lneFechaNac_reg_estu_repre.setDate(QDate(y, m, d))
                
                # Seleccionar género en el combo
                index_genero_repre = self.cbxGenero_reg_estu_repre.findText(repre["genero"])
                if index_genero_repre >= 0:
                    self.cbxGenero_reg_estu_repre.setCurrentIndex(index_genero_repre)
            
                # Resto de datos
                self.lneDir_reg_estu_repre.setText(repre["direccion"])
                self.lneNum_reg_estu_repre.setText(repre["num_contact"])
                self.lneCorreo_reg_estu_repre.setText(repre["email"])
                self.lneObser_reg_estu_repre.setText(repre["observacion"])

                crear_msgbox(
                    self,
                    "Encontrado",
                    "Datos del representante cargados correctamente.",
                    QMessageBox.Information,
                ).exec()
            else:
                crear_msgbox(
                    self,
                    "No encontrado",
                    "No existe representante con esa cédula. Complete los datos manualmente.",
                    QMessageBox.Information,
                ).exec()

        except Exception as err:
            crear_msgbox(
                self,
                "Error",
                f"No se pudo buscar: {err}",
                QMessageBox.Critical,
            ).exec()
    
    def cambiar_pagina_registro_estudiante(self, indice):
        """Cambia entre las páginas del formulario (Estudiante/Representante)"""
        self.stackRegistro_estudiante.setCurrentIndex(indice)
    
    def generar_cedula_estudiantil(self):
        """
        Genera una cédula estudiantil única basada en:
        - Número de hijo
        - Año de nacimiento
        - Cédula de la madre
        """
        qdate = self.lneFechaNac_reg_estu.date()
        fecha_nac = qdate.toPython()
        cedula_madre = self.lneCI_madre_reg_estu.text().strip()

        # Validar campos requeridos
        if not fecha_nac or not cedula_madre:
            crear_msgbox(
                self,
                "Campos incompletos",
                "Debe ingresar fecha de nacimiento del estudiante y cédula de la madre.",
                QMessageBox.Warning,
            ).exec()
            return
        
        # Validar formato de cédula madre
        if not cedula_madre.isdigit() or len(cedula_madre) < 6:
            crear_msgbox(
                self,
                "Cédula inválida",
                "La cédula de la madre debe contener al menos 6 dígitos numéricos.",
                QMessageBox.Warning,
            ).exec()
            return
        
        # Validar que la fecha no sea futura
        if fecha_nac > date.today():
            crear_msgbox(
                self,
                "Fecha inválida",
                "La fecha de nacimiento no puede ser futura.",
                QMessageBox.Warning,
            ).exec()
            return

        try:
            cedula = EstudianteModel.generar_cedula_estudiantil(fecha_nac, cedula_madre)

            if cedula:
                self.cedula_estudiantil_generada = cedula
                self.lneCedula_reg_estu.setText(cedula)
                
                crear_msgbox(
                    self,
                    "Cédula generada",
                    f"Cédula estudiantil generada: {cedula}",
                    QMessageBox.Information,
                ).exec()
            else:
                crear_msgbox(
                    self,
                    "Error",
                    "No se pudo generar la cédula estudiantil.",
                    QMessageBox.Warning,
                ).exec()

        except Exception as err:
            crear_msgbox(
                self,
                "Error",
                f"No se pudo generar: {err}",
                QMessageBox.Critical,
            ).exec()
    
    def validar_texto_solo_letras(self, texto, nombre_campo):
        """Valida que un texto contenga solo letras y espacios."""
        if not texto:
            return False, ""
        
        # Validar que solo tenga letras, espacios y caracteres latinos
        if not re.match(r'^[A-Za-zÁÉÍÓÚÑáéíóúñ\s]+$', texto):
            crear_msgbox(
                self,
                "Formato inválido",
                f"El campo '{nombre_campo}' solo puede contener letras y espacios.",
                QMessageBox.Warning,
            ).exec()
            return False, ""
        
        # Normalizar: capitalizar cada palabra
        texto_normalizado = " ".join(p.capitalize() for p in texto.split())
        return True, texto_normalizado
    
    def validar_email(self, email):
        """Valida formato de email."""
        if not email:
            return True  # Email opcional
        
        # Patrón básico de validación de email
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
    
    def validar_telefono(self, telefono):
        """Valida formato de teléfono (solo números y guiones)."""
        if not telefono:
            return True  # Teléfono opcional
        
        # Solo números y guiones permitidos
        if not re.match(r'^[\d\-]+$', telefono):
            crear_msgbox(
                self,
                "Teléfono inválido",
                "El teléfono solo puede contener números y guiones.",
                QMessageBox.Warning,
            ).exec()
            return False
        
        return True
    
    def guardar_en_bd(self):
        """
        Guarda el estudiante y su representante en la base de datos.
        Realiza validaciones exhaustivas antes de guardar.
        """
        # Validar que se haya generado la cédula estudiantil
        if not self.cedula_estudiantil_generada:
            crear_msgbox(
                self,
                "Falta generar cédula",
                "Debe generar la cédula estudiantil antes de guardar.",
                QMessageBox.Warning,
            ).exec()
            return

        # --- VALIDACIÓN Y RECOLECCIÓN DE DATOS DEL ESTUDIANTE ---
        
        # Validar nombres y apellidos del estudiante
        nombres = self.lneNombre_reg_estu.text().strip()
        apellidos = self.lneApellido_reg_estu.text().strip()
        
        valido_nombres, nombres_norm = self.validar_texto_solo_letras(nombres, "Nombres del estudiante")
        valido_apellidos, apellidos_norm = self.validar_texto_solo_letras(apellidos, "Apellidos del estudiante")
        
        if not valido_nombres or not valido_apellidos:
            return
        
        # Validar nombre de la madre
        madre = self.lneMadre_reg_estu.text().strip()
        valido_madre, madre_norm = self.validar_texto_solo_letras(madre, "Nombre de la madre")
        if not valido_madre:
            return
        
        # Validar nombre del padre (opcional)
        padre = self.lnePadre_reg_estu.text().strip()
        if padre:
            valido_padre, padre_norm = self.validar_texto_solo_letras(padre, "Nombre del padre")
            if not valido_padre:
                return
        else:
            padre_norm = ""
        
        # Validar fecha de nacimiento no sea futura
        fecha_nac = self.lneFechaNac_reg_estu.date().toPython()
        if fecha_nac > date.today():
            crear_msgbox(
                self,
                "Fecha inválida",
                "La fecha de nacimiento del estudiante no puede ser futura.",
                QMessageBox.Warning,
            ).exec()
            return
        
        # Recolectar datos del estudiante
        estudiante_data = {
            "cedula": self.cedula_estudiantil_generada,
            "apellidos": apellidos_norm,
            "nombres": nombres_norm,
            "fecha_nac": fecha_nac,
            "ciudad": self.lneCity_reg_estu.text().strip(),
            "genero": self.cbxGenero_reg_estu.currentText().strip(),
            "direccion": self.lneDir_reg_estu.text().strip(),
            "fecha_ingreso": self.lneFechaIng_reg_estu.date().toPython(),
            "tallaC": self.lneTallaC_reg_estu.text().strip(),
            "tallaP": self.lneTallaP_reg_estu.text().strip(),
            "tallaZ": self.lneTallaZ_reg_estu.text().strip(),
            "madre": madre_norm,
            "madre_ci": self.lneCI_madre_reg_estu.text().strip(),
            "ocupacion_madre": self.lneOcup_madre_reg_estu.text().strip(),
            "padre": padre_norm,
            "padre_ci": self.lneCI_padre_reg_estu.text().strip(),
            "ocupacion_padre": self.lneOcup_padre_reg_estu.text().strip(),
        }

        # --- VALIDACIÓN Y RECOLECCIÓN DE DATOS DEL REPRESENTANTE ---
        
        # Validar nombres y apellidos del representante
        nombres_repre = self.lneNombre_reg_estu_repre.text().strip()
        apellidos_repre = self.lneApellido_reg_estu_repre.text().strip()
        
        valido_nombres_repre, nombres_repre_norm = self.validar_texto_solo_letras(
            nombres_repre, "Nombres del representante"
        )
        valido_apellidos_repre, apellidos_repre_norm = self.validar_texto_solo_letras(
            apellidos_repre, "Apellidos del representante"
        )
        
        if not valido_nombres_repre or not valido_apellidos_repre:
            return
        
        # Validar cédula del representante
        cedula_repre = self.lneCedula_reg_estu_repre.text().strip()
        if not cedula_repre or not cedula_repre.isdigit():
            crear_msgbox(
                self,
                "Cédula inválida",
                "La cédula del representante debe contener solo números.",
                QMessageBox.Warning,
            ).exec()
            return
        
        # Validar teléfono
        telefono = self.lneNum_reg_estu_repre.text().strip()
        if not self.validar_telefono(telefono):
            return
        
        # Validar email
        email = self.lneCorreo_reg_estu_repre.text().strip()
        if not self.validar_email(email):
            return
        
        # Validar fecha de nacimiento del representante
        fecha_nac_repre = self.lneFechaNac_reg_estu_repre.date().toPython()
        if fecha_nac_repre > date.today():
            crear_msgbox(
                self,
                "Fecha inválida",
                "La fecha de nacimiento del representante no puede ser futura.",
                QMessageBox.Warning,
            ).exec()
            return
        
        # Recolectar datos del representante
        representante_data = {
            "cedula": cedula_repre,
            "apellidos": apellidos_repre_norm,
            "nombres": nombres_repre_norm,
            "fecha_nac": fecha_nac_repre,
            "genero": self.cbxGenero_reg_estu_repre.currentText().strip(),
            "direccion": self.lneDir_reg_estu_repre.text().strip(),
            "num_contact": telefono,
            "email": email,
            "observacion": self.lneObser_reg_estu_repre.text().strip(),
        }

        # Validar campos obligatorios
        if not estudiante_data["nombres"] or not estudiante_data["apellidos"] or not estudiante_data["madre"]:
            crear_msgbox(
                self,
                "Campos incompletos",
                "Por favor complete los campos obligatorios:\n- Nombres\n- Apellidos\n- Nombre de la madre",
                QMessageBox.Warning,
            ).exec()
            return
        
        # Validar que haya seleccionado una sección
        seccion_id = self.cbxSeccion_reg_estu.currentData()
        if not seccion_id:
            crear_msgbox(
                self,
                "Falta sección",
                "Debe seleccionar una sección válida para el estudiante.",
                QMessageBox.Warning,
            ).exec()
            return
        
        try:
            # Guardar en la base de datos
            ok, mensaje = EstudianteModel.guardar(
                estudiante_data, 
                representante_data, 
                self.usuario_actual, 
                seccion_id
            )
            
            if ok:
                crear_msgbox(
                    self,
                    "Éxito",
                    "Estudiante registrado y asignado a sección correctamente.",
                    QMessageBox.Information,
                ).exec()
                
                # Limpiar formulario y cerrar
                self.limpiar_formulario()
                self.accept()  # Cerrar con código de aceptación
            else:
                crear_msgbox(
                    self,
                    "Error al guardar",
                    f"No se pudo guardar el estudiante:\n{mensaje}",
                    QMessageBox.Critical,
                ).exec()
                
        except Exception as err:
            crear_msgbox(
                self,
                "Error inesperado",
                f"Ocurrió un error al guardar:\n{err}",
                QMessageBox.Critical,
            ).exec()
