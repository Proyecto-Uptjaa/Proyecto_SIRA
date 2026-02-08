from utils.db import get_connection
from models.auditoria_model import AuditoriaModel
from typing import Optional, Dict, List, Tuple


class AreaAprendizajeModel:
    """Modelo de Áreas de Aprendizaje."""

    @staticmethod
    def crear(
        nombre: str,
        abreviatura: str = None,
        usuario_actual: dict = None
    ) -> Tuple[bool, str]:
        """Crea una nueva área de aprendizaje."""
        
        if not nombre or len(nombre.strip()) < 3:
            return False, "El nombre del área debe tener al menos 3 caracteres."
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos."
            
            cursor = conexion.cursor(dictionary=True)
            
            # Verificar nombre único
            cursor.execute(
                "SELECT id FROM areas_aprendizaje WHERE nombre = %s",
                (nombre.strip(),)
            )
            if cursor.fetchone():
                return False, f"Ya existe un área con el nombre '{nombre}'."
            
            # Insertar
            cursor.execute("""
                INSERT INTO areas_aprendizaje (nombre, abreviatura, estado)
                VALUES (%s, %s, 1)
            """, (nombre.strip(), abreviatura.strip() if abreviatura else None))
            
            area_id = cursor.lastrowid
            conexion.commit()
            
            # Auditoría
            if usuario_actual:
                AuditoriaModel.registrar(
                    usuario_id=usuario_actual["id"],
                    accion="INSERT",
                    entidad="areas_aprendizaje",
                    entidad_id=area_id,
                    referencia=nombre.strip(),
                    descripcion=f"Área de aprendizaje creada: {nombre.strip()}"
                )
            
            return True, f"Área '{nombre.strip()}' creada correctamente."
            
        except Exception as e:
            if conexion:
                conexion.rollback()
            return False, f"Error al crear área: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def actualizar(
        area_id: int,
        nombre: str = None,
        abreviatura: str = None,
        usuario_actual: dict = None
    ) -> Tuple[bool, str]:
        """Actualiza un área de aprendizaje existente."""
        
        if not isinstance(area_id, int) or area_id <= 0:
            return False, "ID de área inválido."
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos."
            
            cursor = conexion.cursor(dictionary=True)
            
            # Verificar que existe
            cursor.execute("SELECT * FROM areas_aprendizaje WHERE id = %s", (area_id,))
            area = cursor.fetchone()
            if not area:
                return False, "Área no encontrada."
            
            # Verificar nombre único si cambia
            if nombre and nombre.strip() != area["nombre"]:
                cursor.execute(
                    "SELECT id FROM areas_aprendizaje WHERE nombre = %s AND id != %s",
                    (nombre.strip(), area_id)
                )
                if cursor.fetchone():
                    return False, f"Ya existe otra área con el nombre '{nombre}'."
            
            cursor.execute("""
                UPDATE areas_aprendizaje
                SET nombre = COALESCE(%s, nombre),
                    abreviatura = COALESCE(%s, abreviatura)
                WHERE id = %s
            """, (
                nombre.strip() if nombre else None,
                abreviatura.strip() if abreviatura else None,
                area_id
            ))
            
            conexion.commit()
            
            # Auditoría
            if usuario_actual:
                AuditoriaModel.registrar(
                    usuario_id=usuario_actual["id"],
                    accion="UPDATE",
                    entidad="areas_aprendizaje",
                    entidad_id=area_id,
                    referencia=nombre or area["nombre"],
                    descripcion=f"Área actualizada: {nombre or area['nombre']}"
                )
            
            return True, "Área actualizada correctamente."
            
        except Exception as e:
            if conexion:
                conexion.rollback()
            return False, f"Error al actualizar área: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def cambiar_estado(
        area_id: int,
        activo: bool,
        usuario_actual: dict = None
    ) -> Tuple[bool, str]:
        """Activa o desactiva un área de aprendizaje."""
        
        if not isinstance(area_id, int) or area_id <= 0:
            return False, "ID de área inválido."
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos."
            
            cursor = conexion.cursor(dictionary=True)
            
            cursor.execute("SELECT nombre FROM areas_aprendizaje WHERE id = %s", (area_id,))
            area = cursor.fetchone()
            if not area:
                return False, "Área no encontrada."
            
            cursor.execute(
                "UPDATE areas_aprendizaje SET estado = %s WHERE id = %s",
                (1 if activo else 0, area_id)
            )
            conexion.commit()
            
            # Auditoría
            if usuario_actual:
                accion_texto = "activada" if activo else "desactivada"
                AuditoriaModel.registrar(
                    usuario_id=usuario_actual["id"],
                    accion="STATUS_CHANGE",
                    entidad="areas_aprendizaje",
                    entidad_id=area_id,
                    referencia=area["nombre"],
                    descripcion=f"Área {accion_texto}: {area['nombre']}"
                )
            
            estado_texto = "activada" if activo else "desactivada"
            return True, f"Área {estado_texto} correctamente."
            
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
    def listar_todas(solo_activas: bool = True) -> List[Dict]:
        """Lista todas las áreas de aprendizaje."""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return []
            
            cursor = conexion.cursor(dictionary=True)
            
            filtro = "WHERE estado = 1" if solo_activas else ""
            cursor.execute(f"""
                SELECT id, nombre, abreviatura, estado
                FROM areas_aprendizaje {filtro}
                ORDER BY nombre
            """)
            
            return cursor.fetchall()
            
        except Exception as e:
            print(f"Error al listar áreas: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def obtener_por_id(area_id: int) -> Optional[Dict]:
        """Obtiene un área por su id."""
        if not isinstance(area_id, int) or area_id <= 0:
            return None
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return None
            
            cursor = conexion.cursor(dictionary=True)
            
            cursor.execute("""
                SELECT id, nombre, abreviatura, estado
                FROM areas_aprendizaje WHERE id = %s
            """, (area_id,))
            
            return cursor.fetchone()
            
        except Exception as e:
            print(f"Error al obtener área: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def obtener_materias_por_area(area_id: int) -> List[Dict]:
        """Obtiene las materias que pertenecen a un área de aprendizaje."""
        if not isinstance(area_id, int) or area_id <= 0:
            return []
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return []
            
            cursor = conexion.cursor(dictionary=True)
            
            cursor.execute("""
                SELECT id, nombre, abreviatura, tipo_evaluacion, estado
                FROM materias
                WHERE area_aprendizaje_id = %s AND estado = 1
                ORDER BY nombre
            """, (area_id,))
            
            return cursor.fetchall()
            
        except Exception as e:
            print(f"Error al obtener materias del área: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
