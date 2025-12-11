# models/secciones_model.py
from utils.db import get_connection
from models.anio_model import AnioEscolarModel

class SeccionesModel:
    @staticmethod
    def obtener_todas(anio_escolar_id=None):
        """Devuelve todas las secciones activas (o solo del año indicado por ID)"""
        conn = get_connection()
        if not conn:
            return []
        cursor = conn.cursor(dictionary=True)
        if anio_escolar_id:
            cursor.execute("""
                SELECT s.id, s.nivel, s.grado, s.letra, s.salon, s.cupo_maximo as cupo,
                       s.maestra_id, s.año_escolar_id,
                       a.anio_inicio, a.nombre as año_nombre,
                       COALESCE(COUNT(e.id), 0) as estudiantes_actuales
                FROM secciones s
                JOIN anios_escolares a ON s.año_escolar_id = a.id
                LEFT JOIN seccion_estudiante se ON se.seccion_id = s.id
                LEFT JOIN estudiantes e ON e.id = se.estudiante_id AND e.estado = 1
                WHERE s.año_escolar_id = %s AND s.activo = 1
                GROUP BY s.id
                ORDER BY s.nivel, s.grado, s.letra
            """, (anio_escolar_id,))
        else:
            cursor.execute("""
                SELECT s.id, s.nivel, s.grado, s.letra, s.salon, s.cupo_maximo as cupo,
                       s.maestra_id, s.año_escolar_id,
                       a.anio_inicio, a.nombre as año_nombre,
                       COALESCE(COUNT(e.id), 0) as estudiantes_actuales
                FROM secciones s
                JOIN anios_escolares a ON s.año_escolar_id = a.id
                LEFT JOIN seccion_estudiante se ON se.seccion_id = s.id
                LEFT JOIN estudiantes e ON e.id = se.estudiante_id AND e.estado = 1
                WHERE s.activo = 1
                GROUP BY s.id
                ORDER BY a.anio_inicio DESC, s.nivel, s.grado, s.letra
            """)
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        return datos

    @staticmethod
    def crear(nivel, grado, letra, salon, cupo, anio_escolar_id=None):
        """Crea una nueva sección (no reactiva)"""
        conn = get_connection()
        if not conn:
            return False
        cursor = conn.cursor()
        try:
            # Si no se especifica el año, usar el actual
            if anio_escolar_id is None:
                anio_actual = AnioEscolarModel.obtener_actual()
                if anio_actual:
                    anio_escolar_id = anio_actual['id']
                else:
                    return False

            # Verificar si ya existe activa en ese año
            cursor.execute("""
                SELECT id FROM secciones
                WHERE nivel = %s AND grado = %s AND letra = %s AND año_escolar_id = %s AND activo = 1
            """, (nivel, grado, letra, anio_escolar_id))
            existente = cursor.fetchone()

            if existente:
                # Ya existe activa → no crear duplicado
                success = False
            else:
                # Crear nueva
                cursor.execute("""
                    INSERT INTO secciones 
                    (nivel, grado, letra, salon, cupo_maximo, año_escolar_id, activo)
                    VALUES (%s, %s, %s, %s, %s, %s, 1)
                """, (nivel, grado, letra, salon or None, cupo, anio_escolar_id))
                conn.commit()
                success = True

        except Exception as e:
            print("Error al crear sección:", e)
            success = False
        finally:
            cursor.close()
            conn.close()
        return success

    @staticmethod
    def reactivar(seccion_id, salon=None, cupo=None):
        """Reactiva una sección existente que está inactiva"""
        conn = get_connection()
        if not conn:
            return False
        cursor = conn.cursor()
        try:
            cursor.execute("""
                UPDATE secciones
                SET activo = 1, salon = %s, cupo_maximo = %s
                WHERE id = %s AND activo = 0
            """, (salon or None, cupo, seccion_id))
            conn.commit()
            success = cursor.rowcount > 0
        except Exception as e:
            print("Error al reactivar sección:", e)
            success = False
        finally:
            cursor.close()
            conn.close()
        return success

    @staticmethod
    def desactivar(seccion_id):
        """Marca una sección como inactiva"""
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
        """Devuelve todos los años con secciones activas"""
        conn = get_connection()
        if not conn:
            return []
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT DISTINCT a.id, a.anio_inicio, a.nombre
            FROM secciones s
            JOIN anios_escolares a ON s.año_escolar_id = a.id
            WHERE s.activo = 1
            ORDER BY a.anio_inicio DESC
        """)
        años = cursor.fetchall()
        cursor.close()
        conn.close()
        return años

    @staticmethod
    def obtener_por_clave(nivel: str, grado: str, letra: str, anio_escolar_id: int = None):
        """Retorna la sección si existe (caso-insensible)"""
        conn = get_connection()
        if not conn:
            return None
        try:
            cursor = conn.cursor(dictionary=True)
            if anio_escolar_id:
                cursor.execute("""
                    SELECT * FROM secciones
                    WHERE LOWER(nivel)=LOWER(%s) AND LOWER(grado)=LOWER(%s) AND LOWER(letra)=LOWER(%s)
                      AND año_escolar_id = %s
                    LIMIT 1
                """, (nivel, grado, letra, anio_escolar_id))
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