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
    def __init__(self, usuario_actual, año_escolar, parent=None):
        super().__init__(parent)
        self.usuario_actual = usuario_actual
        self.año_escolar = año_escolar

        self.setupUi(self)   # esto mete todos los widgets en self

        # Ventana Registro Estudiante
        self.setWindowTitle("Nuevo registro de estudiante")
        self.stackRegistro_estudiante.setCurrentIndex(0)
        # Botones
        self.btnGenCedula_reg_estu.clicked.connect(self.generar_cedula_estudiantil)
        self.btnGuardar_reg_estu.clicked.connect(self.guardar_en_bd)
        self.btnConsult_ci_repre.clicked.connect(self.buscar_representante)
        self.btnStudentDatos_registro.clicked.connect(lambda: self.cambiar_pagina_registro_estudiante(0))
        self.btnRepre_registro.clicked.connect(lambda: self.cambiar_pagina_registro_estudiante(1))
        self.btnLimpiar_reg_estu.clicked.connect(self.limpiar_formulario)

        # Conectar cálculo automático de edad
        self.lneFechaNac_reg_estu.dateChanged.connect(self.actualizar_edad_estudiante)
        self.lneFechaNac_reg_estu_repre.dateChanged.connect(self.actualizar_edad_representante)

        # Variable para almacenar la cédula generada
        self.cedula_estudiantil_generada = None

        # ---Cargar secciones reales desde la BD ---
        self.cargar_secciones_en_combos()
        # Conectar los combos en cascada (nivel → grado → sección)
        self.cbxTipoEdu_reg_estu.currentTextChanged.connect(self.actualizar_grados)
        self.cbxGrado_reg_estu.currentTextChanged.connect(self.actualizar_secciones)
        
        # Actualizar grados si hay un valor por defecto seleccionado
        nivel_actual = self.cbxTipoEdu_reg_estu.currentText()
        if nivel_actual:
            self.actualizar_grados(nivel_actual)
        
        ## Sombras de elementos ##
        crear_sombra_flotante(self.btnGenCedula_reg_estu)
        crear_sombra_flotante(self.btnGuardar_reg_estu)
        crear_sombra_flotante(self.btnLimpiar_reg_estu)
        crear_sombra_flotante(self.btnConsult_ci_repre)
        crear_sombra_flotante(self.btnStudentDatos_registro)
        crear_sombra_flotante(self.btnRepre_registro)
        crear_sombra_flotante(self.lneCedula_reg_estu, blur_radius=8, y_offset=1)

    def limpiar_formulario(self):
        limpiar_widgets(self)
        self.cedula_estudiantil_generada = None
    
    def cargar_secciones_en_combos(self):
        secciones = EstudianteModel.obtener_secciones_activas(self.año_escolar['anio_inicio'])

        self.cbxTipoEdu_reg_estu.clear()
        self.cbxGrado_reg_estu.clear()
        self.cbxSeccion_reg_estu.clear()

        niveles = set()
        self.grados_por_nivel = {}
        self.secciones_por_grado = {}

        for sec in secciones:
            nivel = sec["nivel"]
            grado = sec["grado"]
            letra = sec["letra"]

            # Nivel
            if nivel not in niveles:
                niveles.add(nivel)
                self.cbxTipoEdu_reg_estu.addItem(nivel)

            # Grados por nivel
            if nivel not in self.grados_por_nivel:
                self.grados_por_nivel[nivel] = set()
            self.grados_por_nivel[nivel].add(grado)

            # Secciones por grado (guardando letra e id)
            clave = f"{nivel}_{grado}"
            if clave not in self.secciones_por_grado:
                self.secciones_por_grado[clave] = []
            self.secciones_por_grado[clave].append({
                "letra": letra,
                "id": sec["id"]
            })

    def actualizar_grados(self, nivel):
        if not nivel:
            return
        self.cbxGrado_reg_estu.clear()
        grados = sorted(self.grados_por_nivel.get(nivel, set()))
        for g in grados:
            self.cbxGrado_reg_estu.addItem(g)
        self.actualizar_secciones("")  # limpia secciones

    def actualizar_secciones(self, grado):
        if not grado:
            self.cbxSeccion_reg_estu.clear()
            return
        nivel = self.cbxTipoEdu_reg_estu.currentText()
        clave = f"{nivel}_{grado}"
        self.cbxSeccion_reg_estu.clear()
        opciones = self.secciones_por_grado.get(clave, [])
        for opt in opciones:
            self.cbxSeccion_reg_estu.addItem(opt["letra"], opt["id"])

    # --- Funciones de cálculo de edad ---
    def actualizar_edad_estudiante(self):
        qdate = self.lneFechaNac_reg_estu.date()
        fecha_nac = qdate.toPython()
        edad = calcular_edad(fecha_nac)
        self.lneEdad_reg_estu.setText(str(edad))

    def actualizar_edad_representante(self):
        qdate = self.lneFechaNac_reg_estu_repre.date()
        fecha_nac = qdate.toPython()
        edad = calcular_edad(fecha_nac)
        self.lneEdad_reg_estu_repre.setText(str(edad))


    def buscar_representante(self):
        cedula_repre = self.lneCedula_reg_estu_repre.text().strip()
        if not cedula_repre:
            msg = crear_msgbox(
                    self,
                    "Campo vacío",
                    "Ingrese una cédula para buscar.",
                    QMessageBox.Warning,
                )
            msg.exec()
            return

        try:
            repre = RepresentanteModel.buscar_por_cedula(cedula_repre)
            if repre:
                # Rellenar los campos del formulario
                self.lneApellido_reg_estu_repre.setText(repre["apellidos_repre"])
                self.lneNombre_reg_estu_repre.setText(repre["nombres_repre"])

                fecha_repre = repre["fecha_nac_repre"]
                if isinstance(fecha_repre, date):
                    self.lneFechaNac_reg_estu_repre.setDate(QDate.fromPyDate(fecha_repre))
                else:
                    y, m, d = map(int, str(fecha_repre).split("-"))
                    self.lneFechaNac_reg_estu_repre.setDate(QDate(y, m, d))
                index_genero_repre = self.cbxGenero_reg_estu_repre.findText(repre["genero_repre"])
                if index_genero_repre >= 0:
                    self.cbxGenero_reg_estu_repre.setCurrentIndex(index_genero_repre)
            
                self.lneDir_reg_estu_repre.setText(repre["direccion_repre"])
                self.lneNum_reg_estu_repre.setText(repre["num_contact_repre"])
                self.lneCorreo_reg_estu_repre.setText(repre["correo_repre"])
                self.lneObser_reg_estu_repre.setText(repre["observacion"])

                msg = crear_msgbox(
                    self,
                    "Encontrado",
                    "Datos del representante cargados.",
                    QMessageBox.Information,
                )
                msg.exec()
            else:
                msg = crear_msgbox(
                    self,
                    "No encontrado",
                    "No existe representante con esa cédula.",
                    QMessageBox.Information,
                )
                msg.exec()

        except Exception as err:
            msg = crear_msgbox(
                    self,
                    "Error",
                    f"No se pudo buscar: {err}",
                    QMessageBox.Critical,
                )
            msg.exec()
    
    def cambiar_pagina_registro_estudiante(self, indice):
        self.stackRegistro_estudiante.setCurrentIndex(indice)
    
    def generar_cedula_estudiantil(self):
        qdate = self.lneFechaNac_reg_estu.date()
        fecha_nac = qdate.toPython()
        cedula_madre = self.lneCI_madre_reg_estu.text().strip()

        if not fecha_nac or not cedula_madre:
            msg = crear_msgbox(
                    self,
                    "Campos incompletos",
                    "Debe ingresar fecha de nacimiento de estudiante y cédula de la madre",
                    QMessageBox.Warning,
                )
            msg.exec()
            return

        try:
            cedula = EstudianteModel.generar_cedula_estudiantil(fecha_nac, cedula_madre)

            if cedula:
                self.cedula_estudiantil_generada = cedula
                self.lneCedula_reg_estu.setText(cedula)
            else:
                msg = crear_msgbox(
                    self,
                    "Error",
                    "No se pudo generar la cédula estudiantil.",
                    QMessageBox.Warning,
                )
                msg.exec()

        except Exception as err:
            msg = crear_msgbox(
                    self,
                    "Error",
                    f"No se pudo generar: {err}",
                    QMessageBox.Critical,
                )
            msg.exec()
    
    def guardar_en_bd(self):
        if not self.cedula_estudiantil_generada:
            msg = crear_msgbox(
                    self,
                    "Falta generar",
                    "Debe generar la cédula estudiantil antes de guardar.",
                    QMessageBox.Warning,
                )
            msg.exec()
            return

        # --- Datos estudiante ---
        nombres = self.lneNombre_reg_estu.text().strip()
        apellidos = self.lneApellido_reg_estu.text().strip()
        campos = [nombres, apellidos]
        # Validar que solo tenga letras y espacios
        if not all(re.match(r'^[A-Za-zÁÉÍÓÚÑáéíóúñ\s]+$', campo) for campo in campos):
            msg = crear_msgbox(
                    self,
                    "Error",
                    "Los campos de texto solo pueden contener letras y espacios.",
                    QMessageBox.Warning,
                )
            msg.exec()
            return
        nombres = " ".join(p.capitalize() for p in nombres.split())
        apellidos = " ".join(p.capitalize() for p in apellidos.split())
        
        estudiante_data = {
            "cedula": self.cedula_estudiantil_generada,
            "apellidos": apellidos,
            "nombres": nombres,
            "fecha_nac_est": self.lneFechaNac_reg_estu.date().toPython(),
            "city": self.lneCity_reg_estu.text().strip(),
            "genero": self.cbxGenero_reg_estu.currentText().strip(),
            "direccion": self.lneDir_reg_estu.text().strip(),
            "fecha_ingreso": self.lneFechaIng_reg_estu.date().toPython(),
            "docente": self.lneDocente_reg_estu.text().strip(),
            "tallaC": self.lneTallaC_reg_estu.text().strip(),
            "tallaP": self.lneTallaP_reg_estu.text().strip(),
            "tallaZ": self.lneTallaZ_reg_estu.text().strip(),
            "madre": self.lneMadre_reg_estu.text().strip(),
            "madre_ci": self.lneCI_madre_reg_estu.text().strip(),
            "ocupacion_madre": self.lneOcup_madre_reg_estu.text().strip(),
            "padre": self.lnePadre_reg_estu.text().strip(),
            "padre_ci": self.lneCI_padre_reg_estu.text().strip(),
            "ocupacion_padre": self.lneOcup_padre_reg_estu.text().strip(),
        }

        # --- Datos representante ---
        nombres_repre = self.lneNombre_reg_estu_repre.text().strip()
        apellidos_repre = self.lneApellido_reg_estu_repre.text().strip()
        campos_repre = [nombres_repre, apellidos_repre]
        # Validar que solo tenga letras y espacios
        if not all(re.match(r'^[A-Za-zÁÉÍÓÚÑáéíóúñ\s]+$', campo) for campo in campos_repre):
            msg = crear_msgbox(
                    self,
                    "Error",
                    "Los campos de texto solo pueden contener letras y espacios.",
                    QMessageBox.Warning,
                )
            msg.exec()
            return
        nombres_repre = " ".join(p.capitalize() for p in nombres_repre.split())
        apellidos_repre = " ".join(p.capitalize() for p in apellidos_repre.split())

        representante_data = {
            "cedula_repre": self.lneCedula_reg_estu_repre.text().strip(),
            "apellidos_repre": apellidos_repre,  # ← Cambié el orden
            "nombres_repre": nombres_repre,
            "fecha_nac_repre": self.lneFechaNac_reg_estu_repre.date().toPython(),
            "genero_repre": self.cbxGenero_reg_estu_repre.currentText().strip(),
            "direccion_repre": self.lneDir_reg_estu_repre.text().strip(),
            "num_contact_repre": self.lneNum_reg_estu_repre.text().strip(),
            "correo_repre": self.lneCorreo_reg_estu_repre.text().strip(),
            "observacion": self.lneObser_reg_estu_repre.text().strip(),
        }

        if not estudiante_data["nombres"] or not estudiante_data["apellidos"] or not estudiante_data["madre"]:
            msg = crear_msgbox(
                    self,
                    "Campos incompletos",
                    "Por favor completa los campos obligatorios.",
                    QMessageBox.Warning,
                )
            msg.exec()
            return
        
        # Validar que haya seleccionado una sección
        seccion_id = self.cbxSeccion_reg_estu.currentData()
        if not seccion_id:
            crear_msgbox(self, "Falta sección", "Debe seleccionar una sección válida.", QMessageBox.Warning).exec()
            return
        
        try:
            # Guardar estudiante y representante
            ok, mensaje = EstudianteModel.guardar(estudiante_data, representante_data, self.usuario_actual, seccion_id)
            
            if ok:
                msg = crear_msgbox(
                        self,
                        "Éxito",
                        "Estudiante registrado y asignado a sección correctamente.",
                        QMessageBox.Information,
                    )
                msg.exec()
                self.limpiar_formulario()
                self.close()
            else:
                msg = crear_msgbox(
                        self,
                        "Error",
                        f"No se pudo guardar: {mensaje}",
                        QMessageBox.Critical,
                    )
                msg.exec()
                
        except Exception as err:
            msg = crear_msgbox(
                    self,
                    "Error",
                    f"No se pudo guardar: {err}",
                    QMessageBox.Critical,
                )
            msg.exec()
