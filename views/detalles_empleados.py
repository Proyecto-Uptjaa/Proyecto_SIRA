from models.registro_base import RegistroBase

from utils.widgets import Switch
from utils.exportar import generar_constancia_trabajo
import os
from utils.edad import calcular_edad
from utils.forms import set_campos_editables
from utils.dialogs import crear_msgbox

from models.emple_model import EmpleadoModel
from views.delegates import EmpleadoDelegate
from ui_compiled.ficha_emple_ui import Ui_ficha_emple
from PySide6.QtWidgets import QDialog, QMessageBox, QMenu, QToolButton
from PySide6.QtCore import Qt, QDate, Signal


class DetallesEmpleado(QDialog, Ui_ficha_emple):
    datos_actualizados = Signal()

    def __init__(self, id_empleado, usuario_actual, parent=None):
        super().__init__(parent)
        self.setupUi(self)   # 👈 esto mete todos los widgets en self

        self.usuario_actual = usuario_actual
        self.setWindowTitle("Ficha de empleado v0.5")
        self.id = id_empleado
        self.id_empleado = id_empleado
        self.stackFicha_emple.setCurrentIndex(0)
        
        # Variable para evitar bucles en las señales
        self.actualizando_switch = False
        
        # Cargar datos primero
        self.cargar_datos()
        
        # Inicializar el switch después de cargar datos
        self.switchActivo = Switch()
        self.switchActivo.setFixedSize(50, 25)
        self.contenedorSwitch_emple.layout().addWidget(self.switchActivo)
        
        # Conectar señales de botones
        self.btnDatosPersonales_ficha_emple.clicked.connect(lambda: self.cambiar_pagina_ficha_empleado(0))
        self.btnDatosLaborales_ficha_emple.clicked.connect(lambda: self.cambiar_pagina_ficha_empleado(1))
        self.btnModificar_ficha_emple.clicked.connect(self.toggle_edicion)
        self.btnEliminar_ficha_emple.clicked.connect(self.eliminar_empleado)
        
        # Conectar señales de fechas para cálculo de edad
        self.lneFechaNac_ficha_emple.dateChanged.connect(self.actualizar_edad_empleado)
        
        # Configurar botón de exportar
        self.btnExportar_ficha_emple.setPopupMode(QToolButton.InstantPopup)
        menu_exportar = QMenu(self.btnExportar_ficha_emple)
        menu_exportar.addAction("Constancia de trabajo", self.exportar_constancia)
        #menu_exportar.addAction("Exportar a Excel", self.exportar_excel)
        #menu_exportar.addAction("Exportar a CSV", self.exportar_csv)
        self.btnExportar_ficha_emple.setMenu(menu_exportar)
        
        # Bloquear campos y configurar estado inicial
        self.set_campos_editables(False)
        self.lneCedula_ficha_emple.setReadOnly(True)
        
        # Establecer el estado inicial del switch sin disparar eventos
        self.actualizando_switch = True
        self.switchActivo.setChecked(bool(self.empleado_actual.get("Estado", 1)))  # ahora la clave es 'estado'
        self.actualizando_switch = False
        
        # Conectar la señal del switch después de establecer el estado inicial
        self.switchActivo.stateChanged.connect(self.cambiar_estado_empleado)

    def cambiar_estado_empleado(self, state):
        if self.actualizando_switch:
            return

        nuevo_estado = 1 if state == Qt.Checked else 0
        estado_actual = int(self.empleado_actual.get("Estado", 1))  # ahora la clave es 'estado'
        if nuevo_estado == estado_actual:
            return

        texto = "activar" if nuevo_estado else "desactivar"

        msg = crear_msgbox(
                self,
                "Confirmar acción",
                f"¿Seguro que deseas {texto} a este empleado?",
                QMessageBox.Question,
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )

        if msg.exec() == QMessageBox.StandardButton.Yes:
            try:
                base = RegistroBase()
                ok, mensaje = base.cambiar_estado("empleados", self.id, nuevo_estado, self.usuario_actual)

                if ok:
                    # Mantén el estado como número en empleado_actual
                    self.empleado_actual["Estado"] = nuevo_estado
                    self.lblEstado_ficha_emple.setText("Activo" if nuevo_estado else "Inactivo")
                    dlg = crear_msgbox(
                        self,
                        "Éxito",
                        f"Empleado {texto}do correctamente.",
                        QMessageBox.Information,
                    )
                    dlg.exec()
                else:
                    dlg = crear_msgbox(
                        self,
                        "Error",
                        f"No se pudo guardar {texto} al empleado: {mensaje}",
                        QMessageBox.Critical,
                    )
                    dlg.exec()
                    self.revertir_switch()

            except Exception as e:
                dlg = crear_msgbox(
                        self,
                        "Error",
                        f"Error inesperado: {str(e)}",
                        QMessageBox.Critical,
                    )
                dlg.exec()
                self.revertir_switch()
        else:
            self.revertir_switch()
    
    def revertir_switch(self):
        """Método auxiliar para revertir el estado del switch de manera segura"""
        self.actualizando_switch = True
        estado = bool(self.empleado_actual["Estado"])
        self.switchActivo.setChecked(bool(self.empleado_actual["Estado"]))  # ahora la clave es 'estado'
        self.lblEstado_ficha_emple.setText("Activo" if estado else "Inactivo")
        self.actualizando_switch = False

    def exportar_constancia(self):
        try:
            empleado = {
                "Cédula": self.lneCedula_ficha_emple.text(),
                "Nombres": self.lneNombres_ficha_emple.text(),
                "Apellidos": self.lneApellidos_ficha_emple.text(),
                "Fecha Ingreso": self.lneFechaIngreso_ficha_emple.text(),
                "Cargo": self.lneCargo_ficha_emple.text(),
                "Salario": self.lneSalario_ficha_emple.text()
            }
            archivo = generar_constancia_trabajo(empleado)
            os.startfile(archivo)  # Windows
        except Exception as e:
            msg = crear_msgbox(
                    self,
                    "Error",
                    f"Error al exportar constancia: {e}",
                    QMessageBox.Critical,
                )
            msg.exec()

    def actualizar_edad_empleado(self):
        fecha_nac = self.lneFechaNac_ficha_emple.date().toPython()
        edad = calcular_edad(fecha_nac)
        self.lneEdad_ficha_emple.setText(str(edad))

    def cambiar_pagina_ficha_empleado(self, indice):
        self.stackFicha_emple.setCurrentIndex(indice)

    def set_campos_editables(self, estado: bool):
        campos = [
            self.lneNombres_ficha_emple, self.lneApellidos_ficha_emple, self.lneFechaNac_ficha_emple,
            self.lneGenero_ficha_emple, self.lneDir_ficha_emple,
            self.lneNum_ficha_emple, self.lneCorreo_ficha_emple, self.cbxTitulo_ficha_emple,
            self.lneCargo_ficha_emple, self.lneFechaIngreso_ficha_emple, self.lneSalario_ficha_emple
        ]
        campos_solo_lectura = [self.lneEdad_ficha_emple]
        set_campos_editables(campos, estado, campos_solo_lectura)

    def cargar_datos(self):
        datos = EmpleadoModel.obtener_por_id(self.id)

        # Guardar estado actual
        self.empleado_actual = {
            "ID": self.id,
            "Cédula": str(datos["cedula"]) if datos else "",
            "Estado": datos["estado"] if datos else 1
        }
        # Mostrar estado en el label
        estado_texto = "Activo" if self.empleado_actual["Estado"] else "Inactivo"
        self.lblEstado_ficha_emple.setText(estado_texto)

        if datos:
            self.lneCedula_ficha_emple.setText(str(datos["cedula"]))
            self.lneNombres_ficha_emple.setText(str(datos["nombres"]))
            self.lneApellidos_ficha_emple.setText(str(datos["apellidos"]))
            fecha_emple = datos["fecha_nac"]
            qdate_emple = QDate(fecha_emple.year, fecha_emple.month, fecha_emple.day)
            self.lneFechaNac_ficha_emple.setDate(qdate_emple)
            self.lneEdad_ficha_emple.setText(str(calcular_edad(fecha_emple)))
            self.lneGenero_ficha_emple.setText(str(datos["genero"]))
            self.lneDir_ficha_emple.setText(str(datos["direccion"]))
            self.lneNum_ficha_emple.setText(str(datos["num_contact"]))
            self.lneCorreo_ficha_emple.setText(str(datos["correo"]))
            index = self.cbxTitulo_ficha_emple.findText(str(datos["titulo"]))
            if index >= 0:
                self.cbxTitulo_ficha_emple.setCurrentIndex(index)
            self.lneCargo_ficha_emple.setText(str(datos["cargo"]))
            fecha_ing = datos["fecha_ingreso"]
            qdate_ing = QDate(fecha_ing.year, fecha_ing.month, fecha_ing.day)
            self.lneFechaIngreso_ficha_emple.setDate(qdate_ing)
            self.lneSalario_ficha_emple.setText(str(datos["salario"]))

    def guardar_datos(self):
        try:

            # --- Datos empleado ---
            empleado_data = {
                "nombres": self.lneNombres_ficha_emple.text(),
                "apellidos": self.lneApellidos_ficha_emple.text(),
                "fecha_nac": self.lneFechaNac_ficha_emple.date().toPython(),
                "genero": self.lneGenero_ficha_emple.text(),
                "direccion": self.lneDir_ficha_emple.text(),
                "num_contact": self.lneNum_ficha_emple.text(),
                "correo": self.lneCorreo_ficha_emple.text(),
                "titulo": self.cbxTitulo_ficha_emple.currentText().strip(),
                "cargo": self.lneCargo_ficha_emple.text(),
                "fecha_ingreso": self.lneFechaIngreso_ficha_emple.text(),
                "salario": self.lneSalario_ficha_emple.text(),
            }
            EmpleadoModel.actualizar(self.id, empleado_data, self.usuario_actual)

            msg = crear_msgbox(
                    self,
                    "Éxito",
                    "Datos actualizados correctamente.",
                    QMessageBox.Information,
                )
            msg.exec()

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
        if self.btnModificar_ficha_emple.text() == "Modificar":
            self.set_campos_editables(True)
            self.btnModificar_ficha_emple.setText("Guardar")
        else:
            self.guardar_datos()
            self.set_campos_editables(False)
            self.btnModificar_ficha_emple.setText("Modificar")

    def eliminar_empleado(self):
        msg = crear_msgbox(
                self,
                "Confirmar eliminación",
                "¿Está seguro de eliminar este empleado?",
                QMessageBox.Question,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        if msg.exec() != QMessageBox.StandardButton.Yes:
            return

        try:
            ok, mensaje = EmpleadoModel.eliminar(self.id_empleado, self.usuario_actual)

            if ok:
                dlg = crear_msgbox(
                    self,
                    "Éxito",
                    mensaje,
                    QMessageBox.Information,
                    )
                dlg.exec()
                self.datos_actualizados.emit()
                self.accept()
                
            else:
                dlg = crear_msgbox(
                    self,
                    "Error",
                    mensaje,
                    QMessageBox.Warning,
                    )
                dlg.exec()

        except Exception as err:
            dlg = crear_msgbox(
                    self,
                    "Error",
                    f"Error en la BD: {err}",
                    QMessageBox.Critical,
                )
            dlg.exec()