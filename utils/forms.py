from PySide6.QtWidgets import QLineEdit, QDateEdit, QComboBox, QCheckBox
from PySide6.QtCore import QDate


def limpiar_widgets(form):
    """Limpia todos los QLineEdit y QDateEdit de un formulario."""
    for widget in form.findChildren(QLineEdit):
        widget.clear()
    for widget in form.findChildren(QDateEdit):
        widget.setDate(QDate.currentDate())


def set_campos_editables(campos, estado: bool, campos_solo_lectura=None):
    """
    Habilita o bloquea una lista de campos.
    :param campos: lista de QLineEdit/QDateEdit/QComboBox/QCheckBox a habilitar o bloquear
    :param estado: True = habilitar, False = bloquear
    :param campos_solo_lectura: lista de campos que siempre deben quedar en solo lectura
    """
    for campo in campos:
        if isinstance(campo, (QLineEdit, QDateEdit)):
            campo.setReadOnly(not estado)
        elif isinstance(campo, QComboBox):
            campo.setEnabled(estado)  # habilita o bloquea el combo
        elif isinstance(campo, QCheckBox):
            campo.setEnabled(estado)  # habilita o bloquea el check
        else:
            try:
                campo.setEnabled(estado)  # fallback genérico
            except Exception:
                pass

    if campos_solo_lectura:
        for campo in campos_solo_lectura:
            if isinstance(campo, (QLineEdit, QDateEdit)):
                campo.setReadOnly(True)
            elif isinstance(campo, (QComboBox, QCheckBox)):
                campo.setEnabled(False)