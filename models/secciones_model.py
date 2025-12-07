# models/secciones_model.py
from utils.db import get_connection

class SeccionesModel:
    @staticmethod
    def obtener_todas(año_inicio=None):
        """Devuelve todas las secciones activas (o solo del año indicado)"""
        conn = get_connection()
        if not conn:
            return []
        cursor = conn.cursor(dictionary=True)
        if año_inicio:
            cursor.execute("""
                SELECT s.id, s.nivel, s.grado, s.letra, s.salon, s.cupo_maximo as cupo,
                       s.maestra_id, s.año_inicio,
                       COALESCE(COUNT(e.id), 0) as estudiantes_actuales
                FROM secciones s
                LEFT JOIN seccion_estudiante se ON se.seccion_id = s.id AND YEAR(se.fecha_asignacion) = %s
                LEFT JOIN estudiantes e ON e.id = se.estudiante_id AND e.estado = 1
                WHERE s.año_inicio = %s AND s.activo = 1
                GROUP BY s.id
                ORDER BY s.nivel, s.grado, s.letra
            """, (año_inicio, año_inicio))
        else:
            cursor.execute("""
                SELECT s.id, s.nivel, s.grado, s.letra, s.salon, s.cupo_maximo as cupo,
                       s.maestra_id, s.año_inicio,
                       COALESCE(COUNT(e.id), 0) as estudiantes_actuales
                FROM secciones s
                LEFT JOIN seccion_estudiante se ON se.seccion_id = s.id AND YEAR(se.fecha_asignacion) = s.año_inicio
                LEFT JOIN estudiantes e ON e.id = se.estudiante_id AND e.estado = 1
                WHERE s.activo = 1
                GROUP BY s.id
                ORDER BY s.año_inicio DESC, s.nivel, s.grado, s.letra
            """)
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        return datos

    @staticmethod
    def crear(nivel, grado, letra, salon, cupo, año_inicio=None):
        conn = get_connection()
        if not conn:
            return False
        cursor = conn.cursor()
        if año_inicio is None:
            cursor.execute("SELECT YEAR(CURDATE())")
            año_inicio = cursor.fetchone()[0]
        try:
            cursor.execute("""
                INSERT INTO secciones 
                (nivel, grado, letra, salon, cupo_maximo, año_inicio, activo)
                VALUES (%s, %s, %s, %s, %s, %s, 1)
            """, (nivel, grado, letra, salon or None, cupo, año_inicio or año_inicio))
            conn.commit()
            success = True
        except Exception as e:
            print("Error al crear sección:", e)
            success = False
        cursor.close()
        conn.close()
        return success

    @staticmethod
    def eliminar(seccion_id):
        conn = get_connection()
        if not conn:
            return False
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE secciones SET activo = 0 WHERE id = %s", (seccion_id,))
            conn.commit()
            success = True
        except:
            success = False
        cursor.close()
        conn.close()
        return success

    @staticmethod
    def obtener_años_disponibles():
        conn = get_connection()
        if not conn:
            return []
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT año_inicio FROM secciones WHERE activo = 1 ORDER BY año_inicio DESC")
        años = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return años

    # --- Nuevo método: buscar sección por nivel, grado, letra (y opcionalmente año) ---
    @staticmethod
    def obtener_por_clave(nivel: str, grado: str, letra: str, año_inicio: int = None):
        """Retorna la fila de la sección si existe (caso-insensible en valores)."""
        conn = get_connection()
        if not conn:
            return None
        try:
            cursor = conn.cursor(dictionary=True)
            if año_inicio:
                cursor.execute("""
                    SELECT * FROM secciones
                    WHERE LOWER(nivel)=LOWER(%s) AND LOWER(grado)=LOWER(%s) AND LOWER(letra)=LOWER(%s)
                      AND año_inicio = %s
                    LIMIT 1
                """, (nivel, grado, letra, año_inicio))
            else:
                cursor.execute("""
                    SELECT * FROM secciones
                    WHERE LOWER(nivel)=LOWER(%s) AND LOWER(grado)=LOWER(%s) AND LOWER(letra)=LOWER(%s)
                    LIMIT 1
                """, (nivel, grado, letra))
            row = cursor.fetchone()
            cursor.close()
            conn.close()
            return row
        except Exception as e:
            print("Error en obtener_por_clave:", e)
            try:
                cursor.close()
                conn.close()
            except:
                pass
            return None