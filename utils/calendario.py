from utils.db import get_connection
from datetime import datetime, date


MESES = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
    }

def listar_eventos(anio_escolar, anio_actual=None):
    if anio_actual is None:
        anio_actual = date.today().year

    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT id, titulo, descripcion, fecha, tipo, repetir, anio_escolar
        FROM eventos
        WHERE anio_escolar = %s OR repetir = 'anual'
    """, (anio_escolar,))
    eventos = cursor.fetchall()

    cursor.close()
    conexion.close()

    eventos_ajustados = []
    for ev in eventos:
        fecha_base = ev["fecha"]

        # Asegurar que sea date
        if isinstance(fecha_base, str):
            fecha_base = datetime.strptime(fecha_base, "%Y-%m-%d").date()

        if ev["repetir"] == "anual":
            ev["fecha"] = fecha_base.replace(year=anio_actual)
        else:
            ev["fecha"] = fecha_base

        ev["fecha_str"] = ev["fecha"].strftime("%Y-%m-%d")
        eventos_ajustados.append(ev)

    # Ordenar por fecha
    eventos_ajustados.sort(key=lambda e: e["fecha"])

    return eventos_ajustados

def crear_evento(titulo, descripcion, fecha, tipo="otro", repetir="ninguno", anio_escolar=None):
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO eventos (titulo, descripcion, fecha, tipo, repetir, anio_escolar)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (titulo, descripcion, fecha, tipo, repetir, anio_escolar))
    conexion.commit()
    cursor.close()
    conexion.close()