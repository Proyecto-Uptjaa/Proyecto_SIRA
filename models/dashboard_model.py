# models/dashboard_model.py
from utils.db import get_connection
from typing import Dict, List, Optional


class DashboardModel:
    """Modelo de estadísticas para el dashboard."""

    @staticmethod
    def obtener_estadisticas_estudiantes() -> Dict:
        """Obtiene estadísticas de estudiantes regulares (excluye egresados)."""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return {
                    'total': 0,
                    'activos': 0,
                    'inactivos': 0,
                    'regulares': 0,
                    'retirados': 0
                }
            
            cursor = conexion.cursor(dictionary=True)
            # Solo contar estudiantes regulares (excluir egresados)
            cursor.execute("""
                SELECT 
                    COUNT(*) as total,
                    SUM(CASE WHEN estado = '1' THEN 1 ELSE 0 END) as activos,
                    SUM(CASE WHEN estado = '0' THEN 1 ELSE 0 END) as inactivos,
                    SUM(CASE WHEN estatus_academico = 'Regular' THEN 1 ELSE 0 END) as regulares,
                    SUM(CASE WHEN estatus_academico = 'Retirado' THEN 1 ELSE 0 END) as retirados
                FROM estudiantes
                WHERE estatus_academico != 'Egresado'
            """)
            resultado = cursor.fetchone()
            return resultado if resultado else {
                'total': 0,
                'activos': 0,
                'inactivos': 0,
                'regulares': 0,
                'retirados': 0
            }
        except Exception as e:
            print(f"Error al obtener estadísticas de estudiantes: {e}")
            return {
                'total': 0,
                'activos': 0,
                'inactivos': 0,
                'regulares': 0,
                'retirados': 0
            }
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    # Métodos individuales para compatibilidad
    @staticmethod
    def total_estudiantes_registrados() -> int:
        stats = DashboardModel.obtener_estadisticas_estudiantes()
        return stats.get('total', 0)

    @staticmethod
    def total_estudiantes_activos() -> int:
        stats = DashboardModel.obtener_estadisticas_estudiantes()
        return stats.get('activos', 0)

    @staticmethod
    def total_estudiantes_inactivos() -> int:
        stats = DashboardModel.obtener_estadisticas_estudiantes()
        return stats.get('inactivos', 0)
    
    @staticmethod
    def total_representantes() -> int:
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return 0
            cursor = conexion.cursor()
            cursor.execute("SELECT COUNT(*) FROM representantes")
            resultado = cursor.fetchone()
            return resultado[0] if resultado else 0
        except Exception as e:
            print(f"Error al contar representantes: {e}")
            return 0
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def seccion_mas_numerosa() -> Optional[Dict]:
        """Retorna la sección con más estudiantes del año actual"""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return None
            
            cursor = conexion.cursor(dictionary=True)
            
            # Obtener el año actual primero
            cursor.execute("SELECT id FROM años_escolares WHERE es_actual = 1 LIMIT 1")
            anio_actual = cursor.fetchone()
            
            if not anio_actual:
                return None
            
            cursor.execute("""
                SELECT 
                    s.nivel,
                    s.grado,
                    s.letra,
                    COUNT(DISTINCT se.estudiante_id) AS total
                FROM secciones s
                LEFT JOIN seccion_estudiante se ON s.id = se.seccion_id
                WHERE s.activo = 1 
                  AND s.año_escolar_id = %s
                GROUP BY s.id, s.nivel, s.grado, s.letra
                HAVING total > 0
                ORDER BY total DESC, s.grado, s.letra
                LIMIT 1
            """, (anio_actual['id'],))
            
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al obtener sección más numerosa: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def estudiantes_por_seccion() -> List[Dict]:
        """Retorna cantidad de estudiantes por sección del año actual"""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return []
            
            cursor = conexion.cursor(dictionary=True)
            
            # Obtener año actual
            cursor.execute("SELECT id FROM años_escolares WHERE es_actual = 1 LIMIT 1")
            anio_actual = cursor.fetchone()
            
            if not anio_actual:
                return []
            
            cursor.execute("""
                SELECT 
                    s.nivel,
                    s.grado,
                    s.letra,
                    COUNT(DISTINCT se.estudiante_id) AS total,
                    s.cupo_maximo
                FROM secciones s
                LEFT JOIN seccion_estudiante se ON s.id = se.seccion_id
                WHERE s.activo = 1 
                  AND s.año_escolar_id = %s
                GROUP BY s.id, s.nivel, s.grado, s.letra, s.cupo_maximo
                ORDER BY s.nivel, s.grado, s.letra
            """, (anio_actual['id'],))
            
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener estudiantes por sección: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def estudiantes_por_nivel() -> List[Dict]:
        """Retorna cantidad de estudiantes por nivel educativo del año actual"""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return []
            
            cursor = conexion.cursor(dictionary=True)
            
            # Obtener año actual
            cursor.execute("SELECT id FROM años_escolares WHERE es_actual = 1 LIMIT 1")
            anio_actual = cursor.fetchone()
            
            if not anio_actual:
                return []
            
            cursor.execute("""
                SELECT 
                    s.nivel,
                    COUNT(DISTINCT se.estudiante_id) AS total
                FROM secciones s
                LEFT JOIN seccion_estudiante se ON s.id = se.seccion_id
                WHERE s.activo = 1 
                  AND s.año_escolar_id = %s
                GROUP BY s.nivel
                ORDER BY 
                    CASE s.nivel
                        WHEN 'Maternal' THEN 1
                        WHEN 'Preescolar' THEN 2
                        WHEN 'Primaria' THEN 3
                        ELSE 4
                    END
            """, (anio_actual['id'],))
            
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener estudiantes por nivel: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def obtener_estadisticas_empleados() -> Dict:
        """Obtiene todas las estadísticas de empleados en una consulta"""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return {'total': 0, 'activos': 0, 'inactivos': 0}
            
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("""
                SELECT 
                    COUNT(*) as total,
                    SUM(CASE WHEN estado = '1' THEN 1 ELSE 0 END) as activos,
                    SUM(CASE WHEN estado = '0' THEN 1 ELSE 0 END) as inactivos
                FROM empleados
            """)
            resultado = cursor.fetchone()
            return resultado if resultado else {'total': 0, 'activos': 0, 'inactivos': 0}
        except Exception as e:
            print(f"Error al obtener estadísticas de empleados: {e}")
            return {'total': 0, 'activos': 0, 'inactivos': 0}
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    # Métodos individuales para compatibilidad
    @staticmethod
    def total_empleados_activos() -> int:
        stats = DashboardModel.obtener_estadisticas_empleados()
        return stats.get('activos', 0)
    
    @staticmethod
    def total_empleados_registrados() -> int:
        stats = DashboardModel.obtener_estadisticas_empleados()
        return stats.get('total', 0)
    
    @staticmethod
    def total_empleados_inactivos() -> int:
        stats = DashboardModel.obtener_estadisticas_empleados()
        return stats.get('inactivos', 0)
    
    @staticmethod
    def estudiantes_sin_seccion() -> int:
        """Cuenta estudiantes activos sin sección asignada en el año actual"""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return 0
            
            cursor = conexion.cursor()
            
            # Obtener año actual
            cursor.execute("SELECT id FROM años_escolares WHERE es_actual = 1 LIMIT 1")
            anio_actual = cursor.fetchone()
            
            if not anio_actual:
                return 0
            
            # Contar estudiantes activos sin asignación en el año actual
            cursor.execute("""
                SELECT COUNT(DISTINCT e.id)
                FROM estudiantes e
                WHERE e.estado = '1'
                  AND e.estatus_academico = 'Regular'
                  AND NOT EXISTS (
                      SELECT 1 
                      FROM seccion_estudiante se
                      INNER JOIN secciones s ON se.seccion_id = s.id
                      WHERE se.estudiante_id = e.id 
                        AND s.año_escolar_id = %s
                  )
            """, (anio_actual[0],))
            
            resultado = cursor.fetchone()
            return resultado[0] if resultado else 0
        except Exception as e:
            print(f"Error al contar estudiantes sin sección: {e}")
            return 0
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
    
    @staticmethod
    def empleados_sin_codigo_rac() -> int:
        """Cuenta empleados activos sin código RAC asignado"""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return 0
            
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT COUNT(*)
                FROM empleados
                WHERE estado = '1'
                  AND (codigo_rac IS NULL OR codigo_rac = '' OR TRIM(codigo_rac) = '')
            """)
            resultado = cursor.fetchone()
            return resultado[0] if resultado else 0
        except Exception as e:
            print(f"Error al contar empleados sin código RAC: {e}")
            return 0
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
    
    @staticmethod
    def secciones_con_cupo_disponible() -> int:
        """Cuenta secciones activas del año actual con cupos disponibles"""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return 0
            
            cursor = conexion.cursor()
            
            # Obtener año actual
            cursor.execute("SELECT id FROM años_escolares WHERE es_actual = 1 LIMIT 1")
            anio_actual = cursor.fetchone()
            
            if not anio_actual:
                return 0
            
            cursor.execute("""
                SELECT COUNT(*)
                FROM (
                    SELECT 
                        s.id,
                        s.cupo_maximo,
                        COUNT(DISTINCT se.estudiante_id) AS matriculados
                    FROM secciones s
                    LEFT JOIN seccion_estudiante se ON s.id = se.seccion_id
                    WHERE s.activo = 1 
                      AND s.año_escolar_id = %s
                      AND s.cupo_maximo > 0
                    GROUP BY s.id, s.cupo_maximo
                    HAVING matriculados < s.cupo_maximo
                ) AS secciones_disponibles
            """, (anio_actual[0],))
            
            resultado = cursor.fetchone()
            return resultado[0] if resultado else 0
        except Exception as e:
            print(f"Error al contar secciones con cupo: {e}")
            return 0
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
    
    @staticmethod
    def secciones_sin_docente() -> int:
        """Cuenta secciones activas del año actual sin docente asignado"""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return 0
            
            cursor = conexion.cursor()
            
            # Obtener año actual
            cursor.execute("SELECT id FROM años_escolares WHERE es_actual = 1 LIMIT 1")
            anio_actual = cursor.fetchone()
            
            if not anio_actual:
                return 0
            
            cursor.execute("""
                SELECT COUNT(*)
                FROM secciones
                WHERE activo = 1 
                  AND año_escolar_id = %s
                  AND (docente_id IS NULL OR docente_id = 0)
            """, (anio_actual[0],))
            
            resultado = cursor.fetchone()
            return resultado[0] if resultado else 0
        except Exception as e:
            print(f"Error al contar secciones sin docente: {e}")
            return 0
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()