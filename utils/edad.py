from datetime import date

def calcular_edad(fecha_nac: date) -> int:
    """Devuelve la edad en años a partir de una fecha de nacimiento."""
    hoy = date.today()
    return hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))