from utils.db import get_connection
from models.auditoria_model import AuditoriaModel
from typing import Optional, Dict, List, Tuple


class MateriasModel:
    """Modelo de materias."""

    # Grados válidos (solo Primaria - Inicial no tiene materias formales)
    GRADOS_PRIMARIA = ["1ero", "2do", "3ero", "4to", "5to", "6to"]
    
    # Notas literales válidas (A-E)
    NOTAS_LITERALES = ["A", "B", "C", "D", "E"]

    @staticmethod
    def crear(
        nombre: str,
        abreviatura: str = None,
        tipo_evaluacion: str = "numerico",
        grados: List[Dict] = None,
        usuario_actual: dict = None
    ) -> Tuple[bool, str]:
        """Crea una nueva materia con sus grados asociados."""
        
        # Validaciones
        if not nombre or len(nombre.strip()) < 2:
            return False, "El nombre de la materia es requerido."
        
        if tipo_evaluacion not in ("numerico", "literal"):
            return False, "Tipo de evaluación debe ser 'numerico' o 'literal'."
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos."
            
            cursor = conexion.cursor(dictionary=True)
            
            # Verificar nombre único
            cursor.execute(
                "SELECT id FROM materias WHERE nombre = %s",
                (nombre.strip(),)
            )
            if cursor.fetchone():
                return False, f"Ya existe una materia con el nombre '{nombre}'."
            
            # Insertar materia
            cursor.execute("""
                INSERT INTO materias (nombre, abreviatura, tipo_evaluacion, estado)
                VALUES (%s, %s, %s, 1)
            """, (nombre.strip(), abreviatura, tipo_evaluacion))
            
            materia_id = cursor.lastrowid
            
            # Insertar grados asociados
            if grados:
                for grado_info in grados:
                    nivel = grado_info.get("nivel")
                    grado = grado_info.get("grado")
                    if nivel and grado:
                        cursor.execute("""
                            INSERT INTO materia_grado (materia_id, nivel, grado)
                            VALUES (%s, %s, %s)
                        """, (materia_id, nivel, grado))
            
            conexion.commit()
            
            # Auditoría
            if usuario_actual:
                grados_str = f" ({len(grados)} grados)" if grados else ""
                AuditoriaModel.registrar(
                    usuario_id=usuario_actual["id"],
                    accion="INSERT",
                    entidad="materias",
                    entidad_id=materia_id,
                    referencia=nombre,
                    descripcion=f"Materia creada: {nombre}{grados_str}"
                )
            
            return True, f"Materia '{nombre}' creada correctamente."
            
        except Exception as e:
            if conexion:
                conexion.rollback()
            return False, f"Error al crear materia: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def actualizar(
        materia_id: int,
        nombre: str = None,
        abreviatura: str = None,
        tipo_evaluacion: str = None,
        grados: List[Dict] = None,
        usuario_actual: dict = None
    ) -> Tuple[bool, str]:
        """Actualiza una materia existente."""
        
        if not isinstance(materia_id, int) or materia_id <= 0:
            return False, "ID de materia inválido."
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos."
            
            cursor = conexion.cursor(dictionary=True)
            
            # Verificar que existe
            cursor.execute("SELECT * FROM materias WHERE id = %s", (materia_id,))
            materia = cursor.fetchone()
            if not materia:
                return False, "Materia no encontrada."
            
            # Verificar nombre único si cambia
            if nombre and nombre.strip() != materia["nombre"]:
                cursor.execute(
                    "SELECT id FROM materias WHERE nombre = %s AND id != %s",
                    (nombre.strip(), materia_id)
                )
                if cursor.fetchone():
                    return False, f"Ya existe otra materia con el nombre '{nombre}'."
            
            # Actualizar materia
            cursor.execute("""
                UPDATE materias
                SET nombre = COALESCE(%s, nombre),
                    abreviatura = COALESCE(%s, abreviatura),
                    tipo_evaluacion = COALESCE(%s, tipo_evaluacion)
                WHERE id = %s
            """, (nombre, abreviatura, tipo_evaluacion, materia_id))
            
            # Actualizar grados si se proporcionan
            if grados is not None:
                # Eliminar grados anteriores
                cursor.execute(
                    "DELETE FROM materia_grado WHERE materia_id = %s",
                    (materia_id,)
                )
                # Insertar nuevos grados
                for grado_info in grados:
                    nivel = grado_info.get("nivel")
                    grado = grado_info.get("grado")
                    if nivel and grado:
                        cursor.execute("""
                            INSERT INTO materia_grado (materia_id, nivel, grado)
                            VALUES (%s, %s, %s)
                        """, (materia_id, nivel, grado))
            
            conexion.commit()
            
            # Auditoría
            if usuario_actual:
                AuditoriaModel.registrar(
                    usuario_id=usuario_actual["id"],
                    accion="UPDATE",
                    entidad="materias",
                    entidad_id=materia_id,
                    referencia=nombre or materia["nombre"],
                    descripcion=f"Materia actualizada: {nombre or materia['nombre']}"
                )
            
            return True, "Materia actualizada correctamente."
            
        except Exception as e:
            if conexion:
                conexion.rollback()
            return False, f"Error al actualizar materia: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def cambiar_estado(
        materia_id: int,
        activo: bool,
        usuario_actual: dict = None
    ) -> Tuple[bool, str]:
        """Activa o desactiva una materia."""
        
        if not isinstance(materia_id, int) or materia_id <= 0:
            return False, "ID de materia inválido."
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos."
            
            cursor = conexion.cursor(dictionary=True)
            
            # Verificar que existe
            cursor.execute("SELECT nombre FROM materias WHERE id = %s", (materia_id,))
            materia = cursor.fetchone()
            if not materia:
                return False, "Materia no encontrada."
            
            # Actualizar estado
            cursor.execute(
                "UPDATE materias SET estado = %s WHERE id = %s",
                (1 if activo else 0, materia_id)
            )
            conexion.commit()
            
            # Auditoría
            if usuario_actual:
                accion = "ACTIVAR" if activo else "DESACTIVAR"
                AuditoriaModel.registrar(
                    usuario_id=usuario_actual["id"],
                    accion="STATUS_CHANGE",
                    entidad="materias",
                    entidad_id=materia_id,
                    referencia=materia["nombre"],
                    descripcion=f"Materia {accion.lower()}da: {materia['nombre']}"
                )
            
            estado_texto = "activada" if activo else "desactivada"
            return True, f"Materia {estado_texto} correctamente."
            
        except Exception as e:
            if conexion:
                conexion.rollback()
            return False, f"Error al cambiar estado: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def obtener_por_id(materia_id: int) -> Optional[Dict]:
        """Obtiene una materia por su ID con sus grados asociados."""
       
        if not isinstance(materia_id, int) or materia_id <= 0:
            return None
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return None
            
            cursor = conexion.cursor(dictionary=True)
            
            cursor.execute("""
                SELECT id, nombre, abreviatura, tipo_evaluacion, estado
                FROM materias WHERE id = %s
            """, (materia_id,))
            materia = cursor.fetchone()
            
            if materia:
                # Obtener grados asociados
                cursor.execute("""
                    SELECT nivel, grado FROM materia_grado
                    WHERE materia_id = %s
                    ORDER BY nivel, grado
                """, (materia_id,))
                materia["grados"] = cursor.fetchall()
            
            return materia
            
        except Exception as e:
            print(f"Error al obtener materia: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def listar_todas(solo_activas: bool = True) -> List[Dict]:
        """Lista todas las materias con sus grados."""
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return []
            
            cursor = conexion.cursor(dictionary=True)
            
            filtro = "WHERE estado = 1" if solo_activas else ""
            cursor.execute(f"""
                SELECT id, nombre, abreviatura, tipo_evaluacion, estado
                FROM materias {filtro}
                ORDER BY nombre
            """)
            materias = cursor.fetchall()
            
            # Obtener grados para cada materia
            for materia in materias:
                cursor.execute("""
                    SELECT nivel, grado FROM materia_grado
                    WHERE materia_id = %s
                    ORDER BY nivel, grado
                """, (materia["id"],))
                materia["grados"] = cursor.fetchall()
                
                # Crear resumen de grados
                grados_resumidos = []
                for g in materia["grados"]:
                    grados_resumidos.append(f"{g['nivel'][:3]}-{g['grado']}")
                materia["grados_resumen"] = ", ".join(grados_resumidos) if grados_resumidos else "Sin asignar"
            
            return materias
            
        except Exception as e:
            print(f"Error al listar materias: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def obtener_por_nivel_grado(nivel: str, grado: str) -> List[Dict]:
        """
        Obtiene las materias configuradas para un nivel y grado específico.
        (para mostrar qué materias se pueden asignar a una sección).
        """
        if not nivel or not grado:
            return []
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return []
            
            cursor = conexion.cursor(dictionary=True)
            
            cursor.execute("""
                SELECT m.id, m.nombre, m.abreviatura, m.tipo_evaluacion
                FROM materias m
                JOIN materia_grado mg ON m.id = mg.materia_id
                WHERE mg.nivel = %s AND mg.grado = %s AND m.estado = 1
                ORDER BY m.nombre
            """, (nivel, grado))
            
            return cursor.fetchall()
            
        except Exception as e:
            print(f"Error al obtener materias por nivel/grado: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def asignar_a_seccion(
        seccion_id: int,
        materias_ids: List[int],
        usuario_actual: dict = None
    ) -> Tuple[bool, str]:
        """
        Asigna materias a una sección específica.
        Reemplaza las asignaciones anteriores.
        """
        if not isinstance(seccion_id, int) or seccion_id <= 0:
            return False, "ID de sección inválido."
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos."
            
            cursor = conexion.cursor(dictionary=True)
            
            # Verificar que la sección existe
            cursor.execute("""
                SELECT s.id, s.nivel, s.grado, s.letra, ae.nombre as año
                FROM secciones s
                JOIN años_escolares ae ON s.año_escolar_id = ae.id
                WHERE s.id = %s
            """, (seccion_id,))
            seccion = cursor.fetchone()
            if not seccion:
                return False, "Sección no encontrada."
            
            # Eliminar asignaciones anteriores
            cursor.execute(
                "DELETE FROM seccion_materia WHERE seccion_id = %s",
                (seccion_id,)
            )
            
            # Insertar nuevas asignaciones
            for materia_id in materias_ids:
                cursor.execute("""
                    INSERT INTO seccion_materia (seccion_id, materia_id)
                    VALUES (%s, %s)
                """, (seccion_id, materia_id))
            
            conexion.commit()
            
            # Auditoría
            if usuario_actual:
                seccion_nombre = f"{seccion['grado']} {seccion['letra']}"
                AuditoriaModel.registrar(
                    usuario_id=usuario_actual["id"],
                    accion="UPDATE",
                    entidad="seccion_materia",
                    entidad_id=seccion_id,
                    referencia=seccion_nombre,
                    descripcion=f"Materias asignadas a {seccion_nombre}: {len(materias_ids)} materias"
                )
            
            return True, f"{len(materias_ids)} materias asignadas correctamente."
            
        except Exception as e:
            if conexion:
                conexion.rollback()
            return False, f"Error al asignar materias: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def obtener_materias_seccion(seccion_id: int) -> List[Dict]:
        """Obtiene las materias asignadas a una sección."""
        if not isinstance(seccion_id, int) or seccion_id <= 0:
            return []
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return []
            
            cursor = conexion.cursor(dictionary=True)
            
            cursor.execute("""
                SELECT sm.id as seccion_materia_id, m.id, m.nombre, 
                       m.abreviatura, m.tipo_evaluacion
                FROM seccion_materia sm
                JOIN materias m ON sm.materia_id = m.id
                WHERE sm.seccion_id = %s AND m.estado = 1
                ORDER BY m.nombre
            """, (seccion_id,))
            
            return cursor.fetchall()
            
        except Exception as e:
            print(f"Error al obtener materias de sección: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def obtener_ids_materias_seccion(seccion_id: int) -> List[int]:
        """Obtiene solo los IDs de materias asignadas a una sección."""
        materias = MateriasModel.obtener_materias_seccion(seccion_id)
        return [m["id"] for m in materias]

    @staticmethod
    def duplicar_materias_seccion(
        seccion_origen_id: int,
        seccion_destino_id: int
    ) -> Tuple[bool, str]:
        """
        Copia las materias de una sección a otra.
        (Aplica al duplicar secciones para un nuevo año).
        """
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos."
            
            cursor = conexion.cursor(dictionary=True)
            
            # Obtener materias de origen
            cursor.execute("""
                SELECT materia_id FROM seccion_materia
                WHERE seccion_id = %s
            """, (seccion_origen_id,))
            materias = cursor.fetchall()
            
            if not materias:
                return True, "No hay materias para duplicar."
            
            # Insertar en destino
            for m in materias:
                cursor.execute("""
                    INSERT IGNORE INTO seccion_materia (seccion_id, materia_id)
                    VALUES (%s, %s)
                """, (seccion_destino_id, m["materia_id"]))
            
            conexion.commit()
            return True, f"{len(materias)} materias duplicadas."
            
        except Exception as e:
            if conexion:
                conexion.rollback()
            return False, f"Error al duplicar materias: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
