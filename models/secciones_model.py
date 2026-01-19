# models/secciones_model.py
from utils.db import get_connection
from models.anio_model import AnioEscolarModel
from models.auditoria_model import AuditoriaModel
from typing import Optional, Dict, List, Tuple


class SeccionesModel:
    """Modelo de secciones académicas."""
    
    NIVELES_VALIDOS = ["Inicial", "Primaria"]
    GRADOS_INICIAL = ["1er Nivel", "2do Nivel", "3er Nivel"]
    GRADOS_PRIMARIA = ["1ero", "2do", "3ero", "4to", "5to", "6to"]
    LETRAS_VALIDAS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + ["Única"]
    
    @staticmethod
    def obtener_todas(anio_escolar_id: int, solo_activas: bool = True) -> list:
        """
        Obtiene todas las secciones de un año escolar.
        """
        conn = get_connection()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor(dictionary=True)
            
            # Condición de filtro según parámetro
            filtro_activo = "AND s.activo = 1" if solo_activas else ""
            
            query = f"""
                SELECT 
                    s.id,
                    s.nivel,
                    s.grado,
                    s.letra,
                    s.salon,
                    s.cupo_maximo as cupo,
                    s.activo,
                    s.docente_id,
                    IFNULL(
                        CONCAT(e.nombres, ' ', e.apellidos),
                        'Sin asignar'
                    ) as docente_nombre,
                    COUNT(DISTINCT se.estudiante_id) as estudiantes_actuales
                FROM secciones s
                LEFT JOIN empleados e ON s.docente_id = e.id AND e.estado = 1
                LEFT JOIN seccion_estudiante se ON se.seccion_id = s.id
                LEFT JOIN estudiantes est ON se.estudiante_id = est.id AND est.estado = 1
                WHERE s.año_escolar_id = %s {filtro_activo}
                GROUP BY s.id, s.nivel, s.grado, s.letra, s.salon, s.cupo_maximo, 
                         s.activo, s.docente_id, e.nombres, e.apellidos
                ORDER BY s.nivel, s.grado, s.letra
            """
            cursor.execute(query, (anio_escolar_id,))
            resultados = cursor.fetchall()
            cursor.close()
            conn.close()
            return resultados
            
        except Exception as e:
            print(f"Error obteniendo secciones: {e}")
            if conn:
                conn.close()
            return []

    @staticmethod
    def crear(
        nivel: str, 
        grado: str, 
        letra: str, 
        salon: str, 
        cupo: int, 
        anio_escolar_id: int = None,
        usuario_actual: dict = None
    ) -> Tuple[bool, str]:
        """Crea una nueva sección con validaciones."""
        conexion = None
        cursor = None
        try:
            # --- VALIDACIONES ---
            
            # Validar nivel
            if nivel not in SeccionesModel.NIVELES_VALIDOS:
                return False, f"Nivel inválido. Opciones: {', '.join(SeccionesModel.NIVELES_VALIDOS)}"
            
            # Validar grado según nivel
            grados_validos = SeccionesModel.GRADOS_INICIAL if nivel == "Inicial" else SeccionesModel.GRADOS_PRIMARIA
            if grado not in grados_validos:
                return False, f"Grado inválido para {nivel}. Opciones: {', '.join(grados_validos)}"
            
            # Validar letra
            if letra not in SeccionesModel.LETRAS_VALIDAS:
                return False, "Letra de sección inválida (A-Z o Única)"
            
            # Validar cupo
            if not isinstance(cupo, int) or cupo < 1 or cupo > 50:
                return False, "El cupo debe ser un número entre 1 y 50"
            
            # --- CONEXIÓN BD ---
            
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos"
            
            cursor = conexion.cursor(dictionary=True)
            
            # Obtener año escolar
            if anio_escolar_id is None:
                anio_actual = AnioEscolarModel.obtener_actual()
                if not anio_actual:
                    return False, "No hay año escolar activo. Apertura uno primero."
                anio_escolar_id = anio_actual['id']
                nombre_anio = anio_actual['nombre']
            else:
                # Validar que el año exista
                cursor.execute("SELECT nombre FROM anios_escolares WHERE id = %s", (anio_escolar_id,))
                anio = cursor.fetchone()
                if not anio:
                    return False, f"Año escolar con ID {anio_escolar_id} no encontrado"
                nombre_anio = anio['nombre']
            
            # Verificar duplicados activos en ese año
            cursor.execute("""
                SELECT id FROM secciones
                WHERE nivel = %s AND grado = %s AND letra = %s 
                  AND año_escolar_id = %s AND activo = 1
            """, (nivel, grado, letra, anio_escolar_id))
            
            existente = cursor.fetchone()
            if existente:
                return False, f"Ya existe la sección {grado} {letra} ({nivel}) activa en {nombre_anio}"
            
            # --- CREAR SECCIÓN ---
            
            cursor.execute("""
                INSERT INTO secciones 
                (nivel, grado, letra, salon, cupo_maximo, año_escolar_id, activo)
                VALUES (%s, %s, %s, %s, %s, %s, 1)
            """, (nivel, grado, letra, salon or None, cupo, anio_escolar_id))
            
            conexion.commit()
            seccion_id = cursor.lastrowid
            
            # Auditoría
            if usuario_actual:
                AuditoriaModel.registrar(
                    usuario_id=usuario_actual["id"],
                    accion="INSERT",
                    entidad="secciones",
                    entidad_id=seccion_id,
                    referencia=f"{nivel} {grado} {letra}",
                    descripcion=f"Creó sección {grado} {letra} ({nivel}) en {nombre_anio} (Cupo: {cupo})"
                )
            
            return True, f"Sección {grado} {letra} creada correctamente"
            
        except Exception as e:
            if conexion:
                conexion.rollback()
            return False, f"Error al crear sección: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def reactivar(
        seccion_id: int, 
        salon: str = None, 
        cupo: int = None,
        usuario_actual: dict = None
    ) -> Tuple[bool, str]:
        """Reactiva una sección inactiva."""
        conexion = None
        cursor = None
        try:
            # Validar cupo si se proporciona
            if cupo is not None and (not isinstance(cupo, int) or cupo < 1 or cupo > 50):
                return False, "El cupo debe ser un número entre 1 y 50"
            
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos"
            
            cursor = conexion.cursor(dictionary=True)
            
            # Verificar que la sección existe y está inactiva
            cursor.execute("""
                SELECT s.*, a.nombre as año_nombre
                FROM secciones s
                JOIN anios_escolares a ON s.año_escolar_id = a.id
                WHERE s.id = %s AND s.activo = 0
            """, (seccion_id,))
            
            seccion = cursor.fetchone()
            if not seccion:
                return False, "Sección no encontrada o ya está activa"
            
            # Actualizar
            cursor.execute("""
                UPDATE secciones
                SET activo = 1, salon = %s, cupo_maximo = COALESCE(%s, cupo_maximo)
                WHERE id = %s
            """, (salon, cupo, seccion_id))
            
            conexion.commit()
            
            # Auditoría
            if usuario_actual:
                AuditoriaModel.registrar(
                    usuario_id=usuario_actual["id"],
                    accion="UPDATE",
                    entidad="secciones",
                    entidad_id=seccion_id,
                    referencia=f"{seccion['nivel']} {seccion['grado']} {seccion['letra']}",
                    descripcion=f"Reactivó sección {seccion['grado']} {seccion['letra']} en {seccion['año_nombre']}"
                )
            
            return True, f"Sección {seccion['grado']} {seccion['letra']} reactivada correctamente"
            
        except Exception as e:
            if conexion:
                conexion.rollback()
            return False, f"Error al reactivar sección: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def desactivar(seccion_id: int, usuario_actual: dict = None) -> Tuple[bool, str]:
        """Marca una sección como inactiva."""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos"
            
            cursor = conexion.cursor(dictionary=True)
            
            # Obtener datos antes de desactivar
            cursor.execute("""
                SELECT s.*, a.nombre as año_nombre,
                       COUNT(DISTINCT CASE WHEN e.estado = 1 THEN e.id END) as estudiantes_activos
                FROM secciones s
                JOIN anios_escolares a ON s.año_escolar_id = a.id
                LEFT JOIN seccion_estudiante se ON se.seccion_id = s.id
                LEFT JOIN estudiantes e ON e.id = se.estudiante_id
                WHERE s.id = %s
                GROUP BY s.id
            """, (seccion_id,))
            
            seccion = cursor.fetchone()
            if not seccion:
                return False, "Sección no encontrada"
            
            # Validar que no tenga estudiantes activos
            if seccion['estudiantes_activos'] > 0:
                return False, (
                    f"No se puede desactivar: hay {seccion['estudiantes_activos']} "
                    "estudiante(s) activo(s) en esta sección"
                )
            
            # Desactivar
            cursor.execute("UPDATE secciones SET activo = 0 WHERE id = %s", (seccion_id,))
            conexion.commit()
            
            # Auditoría
            if usuario_actual:
                AuditoriaModel.registrar(
                    usuario_id=usuario_actual["id"],
                    accion="UPDATE",
                    entidad="secciones",
                    entidad_id=seccion_id,
                    referencia=f"{seccion['nivel']} {seccion['grado']} {seccion['letra']}",
                    descripcion=f"Desactivó sección {seccion['grado']} {seccion['letra']} en {seccion['año_nombre']}"
                )
            
            return True, f"Sección {seccion['grado']} {seccion['letra']} desactivada correctamente"
            
        except Exception as e:
            if conexion:
                conexion.rollback()
            return False, f"Error al desactivar sección: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def obtener_años_disponibles() -> List[Dict]:
        """Devuelve todos los años con secciones activas."""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return []
            
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("""
                SELECT DISTINCT a.id, a.anio_inicio, a.nombre
                FROM secciones s
                JOIN anios_escolares a ON s.año_escolar_id = a.id
                WHERE s.activo = 1
                ORDER BY a.anio_inicio DESC
            """)
            
            años = cursor.fetchall()
            return años
            
        except Exception as e:
            print(f"Error en obtener_años_disponibles: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def obtener_por_clave(
        nivel: str, 
        grado: str, 
        letra: str, 
        anio_escolar_id: int = None
    ) -> Optional[Dict]:
        """Busca sección por nivel, grado y letra (case-insensitive)."""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return None
            
            cursor = conexion.cursor(dictionary=True)
            
            if anio_escolar_id:
                cursor.execute("""
                    SELECT * FROM secciones
                    WHERE LOWER(nivel)=LOWER(%s) 
                      AND LOWER(grado)=LOWER(%s) 
                      AND LOWER(letra)=LOWER(%s)
                      AND año_escolar_id = %s
                    LIMIT 1
                """, (nivel, grado, letra, anio_escolar_id))
            else:
                cursor.execute("""
                    SELECT * FROM secciones
                    WHERE LOWER(nivel)=LOWER(%s) 
                      AND LOWER(grado)=LOWER(%s) 
                      AND LOWER(letra)=LOWER(%s)
                    ORDER BY año_escolar_id DESC
                    LIMIT 1
                """, (nivel, grado, letra))
            
            seccion = cursor.fetchone()
            return seccion
            
        except Exception as e:
            print(f"Error en obtener_por_clave: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
    
    @staticmethod
    def obtener_por_id(seccion_id: int) -> Optional[Dict]:
        """Obtiene datos completos de una sección por su ID."""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return None
            
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("""
                SELECT s.*, a.nombre as año_nombre, a.anio_inicio,
                       COUNT(DISTINCT CASE WHEN e.estado = 1 THEN e.id END) as estudiantes_actuales
                FROM secciones s
                JOIN anios_escolares a ON s.año_escolar_id = a.id
                LEFT JOIN seccion_estudiante se ON se.seccion_id = s.id
                LEFT JOIN estudiantes e ON e.id = se.estudiante_id
                WHERE s.id = %s
                GROUP BY s.id
            """, (seccion_id,))
            
            return cursor.fetchone()
            
        except Exception as e:
            print(f"Error en obtener_por_id: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def asignar_docente(
        seccion_id: int, 
        empleado_id: int = None,
        usuario_actual: dict = None
    ) -> Tuple[bool, str]:
        """Asigna o desasigna un docente a una sección."""
        from models.emple_model import EmpleadoModel
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos"
            
            cursor = conexion.cursor(dictionary=True)
            
            # Obtener datos de la sección
            cursor.execute("""
                SELECT s.*, a.nombre as año_nombre
                FROM secciones s
                JOIN anios_escolares a ON s.año_escolar_id = a.id
                WHERE s.id = %s
            """, (seccion_id,))
            
            seccion = cursor.fetchone()
            if not seccion:
                return False, "Sección no encontrada"
            
            # Si se asigna docente, validar que existe y es docente
            docente_anterior_id = seccion['docente_id']
            
            if empleado_id:
                cursor.execute("""
                    SELECT id, cedula, nombres, apellidos, cargo 
                    FROM empleados 
                    WHERE id = %s AND estado = 1
                """, (empleado_id,))
                
                docente = cursor.fetchone()
                if not docente:
                    return False, "Empleado no encontrado o inactivo"
                
                if not EmpleadoModel.es_docente(docente['cargo']):
                    return False, f"El cargo {docente['cargo']} no es docente"
                
                descripcion = f"Asignó docente {docente['nombres']} {docente['apellidos']} a {seccion['grado']} {seccion['letra']}"
            else:
                descripcion = f"Desasignó docente de {seccion['grado']} {seccion['letra']}"
            
            # Actualizar
            cursor.execute("""
                UPDATE secciones 
                SET docente_id = %s
                WHERE id = %s
            """, (empleado_id, seccion_id))
            
            conexion.commit()
            
            # Auditoría
            if usuario_actual:
                AuditoriaModel.registrar(
                    usuario_id=usuario_actual["id"],
                    accion="UPDATE",
                    entidad="secciones",
                    entidad_id=seccion_id,
                    referencia=f"{seccion['nivel']} {seccion['grado']} {seccion['letra']}",
                    descripcion=descripcion
                )
            
            return True, "Docente asignado correctamente" if empleado_id else "Docente desasignado"
            
        except Exception as e:
            if conexion:
                conexion.rollback()
            return False, f"Error al asignar docente: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def obtener_docente_asignado(seccion_id: int) -> Optional[Dict]:
        """Obtiene información del docente asignado a una sección"""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return None
            
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("""
                SELECT e.id, e.cedula, e.nombres, e.apellidos, e.cargo,
                       CONCAT(e.nombres, ' ', e.apellidos) as nombre_completo
                FROM secciones s
                JOIN empleados e ON s.docente_id = e.id
                WHERE s.id = %s AND e.estado = 1
            """, (seccion_id,))
            
            return cursor.fetchone()
        except Exception as e:
            print(f"Error en obtener_docente_asignado: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()