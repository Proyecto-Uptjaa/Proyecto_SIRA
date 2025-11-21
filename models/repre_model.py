# models/representante_model.py
from utils.db import get_connection

class RepresentanteModel:
    """Operaciones sobre representantes, con conexión bajo demanda."""

    @staticmethod
    def buscar_por_cedula(cedula_repre: str):
        """Devuelve un dict con los datos del representante o None si no existe."""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM representantes WHERE cedula_repre = %s", (cedula_repre,))
            return cursor.fetchone()
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()

    @staticmethod
    def obtener_representante(representante_id: int):
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("""
                SELECT cedula_repre, nombres_repre, apellidos_repre, fecha_nac_repre,
                       genero_repre, direccion_repre, num_contact_repre, correo_repre, observacion
                FROM representantes
                WHERE id = %s
            """, (representante_id,))
            return cursor.fetchone()
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()

    @staticmethod
    def actualizar_representante(representante_id: int, data: dict):
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor()
            cursor.execute("""
                UPDATE representantes
                SET nombres_repre=%s, apellidos_repre=%s, fecha_nac_repre=%s, genero_repre=%s,
                    direccion_repre=%s, num_contact_repre=%s, correo_repre=%s, observacion=%s
                WHERE id=%s
            """, (
                data["nombres_repre"], data["apellidos_repre"], data["fecha_nac_repre"], data["genero_repre"],
                data["direccion_repre"], data["num_contact_repre"], data["correo_repre"], data["observacion"],
                representante_id
            ))
            conexion.commit()
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()

    @staticmethod
    def obtener_representante_id(estudiante_id: int):
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor()
            cursor.execute("SELECT representante_id FROM estudiantes WHERE id=%s", (estudiante_id,))
            row = cursor.fetchone()
            return row[0] if row else None
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()