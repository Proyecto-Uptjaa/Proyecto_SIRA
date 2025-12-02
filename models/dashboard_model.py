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
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("""
                SELECT s.grado, s.letra, COUNT(se.estudiante_id) AS total
                FROM secciones s
                LEFT JOIN seccion_estudiante se ON s.id = se.seccion_id
                WHERE s.activo = 1
                GROUP BY s.id, s.grado, s.letra
                ORDER BY total DESC
                LIMIT 1
            """)
            resultado = cursor.fetchone()
            # Retorna un diccionario con grado, letra, total
            return resultado
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()

    @staticmethod
    def estudiantes_por_seccion():
        """Retorna cantidad de estudiantes por sección (útil para gráficos)"""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("""
                SELECT s.grado, s.letra, COUNT(se.estudiante_id) AS total
                FROM secciones s
                LEFT JOIN seccion_estudiante se ON s.id = se.seccion_id
                WHERE s.activo = 1 AND s.año_inicio = YEAR(CURDATE())
                GROUP BY s.id, s.grado, s.letra
                ORDER BY s.grado, s.letra
            """)
            return cursor.fetchall()
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()

    @staticmethod
    def estudiantes_por_nivel():
        """Retorna cantidad de estudiantes por nivel educativo"""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("""
                SELECT s.nivel, COUNT(se.estudiante_id) AS total
                FROM secciones s
                LEFT JOIN seccion_estudiante se ON s.id = se.seccion_id
                WHERE s.activo = 1 AND s.año_inicio = YEAR(CURDATE())
                GROUP BY s.nivel
                ORDER BY s.nivel
            """)
            return cursor.fetchall()
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