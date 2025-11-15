# models/dashboard_model.py
from utils.db import get_connection

class DashboardModel:
    """Modelo para estadísticas del dashboard.
       Cada método abre y cierra su propia conexión.
    """

    @staticmethod
    def total_estudiantes_registrados():
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor()
            cursor.execute("SELECT COUNT(*) FROM estudiantes")
            return cursor.fetchone()[0]
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()


    @staticmethod
    def total_estudiantes_activos():
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor()
            cursor.execute("SELECT COUNT(*) FROM estudiantes WHERE estado = '1'")
            return cursor.fetchone()[0]
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()

    @staticmethod
    def total_estudiantes_inactivos():
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor()
            cursor.execute("SELECT COUNT(*) FROM estudiantes WHERE estado = '0'")
            return cursor.fetchone()[0]
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()
    
    @staticmethod
    def total_representantes():
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor()
            cursor.execute("SELECT COUNT(*) FROM representantes")
            return cursor.fetchone()[0]
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()

    @staticmethod
    def seccion_mas_numerosa():
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT grado, seccion, COUNT(*) AS total
                FROM estudiantes
                GROUP BY grado, seccion
                ORDER BY total DESC
                LIMIT 1
            """)
            return cursor.fetchone()  # (grado, seccion, total) o None
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()
    
    @staticmethod
    def total_empleados_activos():
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor()
            cursor.execute("SELECT COUNT(*) FROM empleados WHERE estado = '1'")
            return cursor.fetchone()[0]
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()
    
    @staticmethod
    def total_empleados_registrados():
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor()
            cursor.execute("SELECT COUNT(*) FROM empleados")
            return cursor.fetchone()[0]
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()
    
    @staticmethod
    def total_empleados_inactivos():
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor()
            cursor.execute("SELECT COUNT(*) FROM empleados WHERE estado = '0'")
            return cursor.fetchone()[0]
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()