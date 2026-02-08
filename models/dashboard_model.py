# models/dashboard_model.py
from utils.db import get_connection
from typing import Dict


class DashboardModel:
    """Modelo de estadísticas para el dashboard."""

    @staticmethod
    def obtener_todo_dashboard() -> Dict:
        """Obtiene todas las estadísticas del dashboard en una sola conexión."""
        
        resultado = {
            'estudiantes': {'total': 0, 'activos': 0, 'inactivos': 0, 'regulares': 0, 'retirados': 0},
            'empleados': {'total': 0, 'activos': 0, 'inactivos': 0},
            'usuarios': {'total': 0, 'activos': 0, 'inactivos': 0},
            'representantes_total': 0,
            'seccion_mas_numerosa': None,
            'estudiantes_sin_seccion': 0,
            'empleados_sin_rac': 0,
            'secciones_sin_docente': 0,
            'secciones_con_cupo': 0,
            'secciones_cupo_superado': [],
        }
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return resultado
            
            cursor = conexion.cursor(dictionary=True)
            
            # 1. Estadísticas de estudiantes (excluye egresados)
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
            row = cursor.fetchone()
            if row:
                resultado['estudiantes'] = row
            
            # 2. Estadísticas de empleados
            cursor.execute("""
                SELECT 
                    COUNT(*) as total,
                    SUM(CASE WHEN estado = '1' THEN 1 ELSE 0 END) as activos,
                    SUM(CASE WHEN estado = '0' THEN 1 ELSE 0 END) as inactivos
                FROM empleados
            """)
            row = cursor.fetchone()
            if row:
                resultado['empleados'] = row
            
            # 3. Estadísticas de usuarios
            cursor.execute("""
                SELECT 
                    COUNT(*) as total,
                    SUM(CASE WHEN estado = '1' THEN 1 ELSE 0 END) as activos,
                    SUM(CASE WHEN estado = '0' THEN 1 ELSE 0 END) as inactivos
                FROM usuarios
            """)
            row = cursor.fetchone()
            if row:
                resultado['usuarios'] = row
            
            # 4. Total representantes
            cursor.execute("SELECT COUNT(*) as total FROM representantes")
            row = cursor.fetchone()
            resultado['representantes_total'] = row['total'] if row else 0
            
            # 5. Obtener año actual
            cursor.execute("SELECT id FROM años_escolares WHERE es_actual = 1 LIMIT 1")
            anio_actual = cursor.fetchone()
            
            if anio_actual:
                anio_id = anio_actual['id']
                
                # 6. Sección más numerosa
                cursor.execute("""
                    SELECT s.nivel, s.grado, s.letra,
                           COUNT(DISTINCT se.estudiante_id) AS total
                    FROM secciones s
                    LEFT JOIN seccion_estudiante se ON s.id = se.seccion_id
                    WHERE s.activo = 1 AND s.año_escolar_id = %s
                    GROUP BY s.id, s.nivel, s.grado, s.letra
                    HAVING total > 0
                    ORDER BY total DESC, s.grado, s.letra
                    LIMIT 1
                """, (anio_id,))
                resultado['seccion_mas_numerosa'] = cursor.fetchone()
                
                # 7. Estudiantes sin sección
                cursor.execute("""
                    SELECT COUNT(DISTINCT e.id) as total
                    FROM estudiantes e
                    WHERE e.estado = '1'
                      AND e.estatus_academico = 'Regular'
                      AND NOT EXISTS (
                          SELECT 1 FROM seccion_estudiante se
                          INNER JOIN secciones s ON se.seccion_id = s.id
                          WHERE se.estudiante_id = e.id AND s.año_escolar_id = %s
                      )
                """, (anio_id,))
                row = cursor.fetchone()
                resultado['estudiantes_sin_seccion'] = row['total'] if row else 0
                
                # 8. Secciones sin docente
                cursor.execute("""
                    SELECT COUNT(*) as total
                    FROM secciones
                    WHERE activo = 1 AND año_escolar_id = %s
                      AND (docente_id IS NULL OR docente_id = 0)
                """, (anio_id,))
                row = cursor.fetchone()
                resultado['secciones_sin_docente'] = row['total'] if row else 0
                
                # 9. Secciones con cupo disponible
                cursor.execute("""
                    SELECT COUNT(*) as total FROM (
                        SELECT s.id
                        FROM secciones s
                        LEFT JOIN seccion_estudiante se ON s.id = se.seccion_id
                        WHERE s.activo = 1 AND s.año_escolar_id = %s AND s.cupo_maximo > 0
                        GROUP BY s.id, s.cupo_maximo
                        HAVING COUNT(DISTINCT se.estudiante_id) < s.cupo_maximo
                    ) AS sub
                """, (anio_id,))
                row = cursor.fetchone()
                resultado['secciones_con_cupo'] = row['total'] if row else 0
                
                # 10. Secciones con cupo superado
                cursor.execute("""
                    SELECT s.nivel, s.grado, s.letra, s.cupo_maximo,
                           COUNT(DISTINCT CASE WHEN est.estado = 1 THEN se.estudiante_id END) AS actuales
                    FROM secciones s
                    LEFT JOIN seccion_estudiante se ON s.id = se.seccion_id
                    LEFT JOIN estudiantes est ON se.estudiante_id = est.id
                    WHERE s.activo = 1 AND s.año_escolar_id = %s
                    GROUP BY s.id, s.nivel, s.grado, s.letra, s.cupo_maximo
                    HAVING actuales > s.cupo_maximo
                    ORDER BY s.nivel, s.grado, s.letra
                """, (anio_id,))
                resultado['secciones_cupo_superado'] = cursor.fetchall()
            
            # 11. Empleados sin código RAC
            cursor.execute("""
                SELECT COUNT(*) as total
                FROM empleados
                WHERE estado = '1'
                  AND (codigo_rac IS NULL OR TRIM(codigo_rac) = '')
            """)
            row = cursor.fetchone()
            resultado['empleados_sin_rac'] = row['total'] if row else 0
            
            return resultado
            
        except Exception as e:
            print(f"Error al obtener dashboard completo: {e}")
            return resultado
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    # --- Métodos de estadísticas por módulo (para refrescos locales) ---

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

    @staticmethod
    def obtener_estadisticas_empleados() -> Dict:
        """Obtiene estadísticas de empleados en una sola consulta."""
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