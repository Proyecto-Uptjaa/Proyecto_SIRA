import re
from utils.db import get_connection
from models.auditoria_model import AuditoriaModel
from typing import Optional, Dict, Tuple

class RepresentanteModel:
    """
    Modelo de representantes.
    La creación se maneja en EstudianteModel.guardar().
    """

    @staticmethod
    def buscar_por_cedula(cedula: str) -> Optional[Dict]:
        """Busca un representante por su cédula."""
        if not cedula or not isinstance(cedula, str):
            return None
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return None
                
            cursor = conexion.cursor(dictionary=True)
            cursor.execute(
                "SELECT * FROM representantes WHERE cedula = %s", 
                (cedula.strip(),)
            )
            return cursor.fetchone()
            
        except Exception as e:
            print(f"Error buscando representante por cédula: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def obtener_representante(representante_id: int) -> Optional[Dict]:
        """Obtiene datos de un representante por su ID."""
        if not isinstance(representante_id, int) or representante_id <= 0:
            return None
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return None
                
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("""
                SELECT cedula, nombres, apellidos_repre, fecha_nac_repre,
                       genero_repre, direccion_repre, num_contact_repre, correo_repre, observacion
                FROM representantes
                WHERE id = %s
            """, (representante_id,))
            
            return cursor.fetchone()
            
        except Exception as e:
            print(f"Error obteniendo representante: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def actualizar_representante(
        representante_id: int, 
        data: dict, 
        usuario_actual: dict
    ) -> Tuple[bool, str]:
        """Actualiza datos de un representante."""
        # Validaciones
        if not isinstance(representante_id, int) or representante_id <= 0:
            return False, "ID de representante inválido"
        
        if not usuario_actual or 'id' not in usuario_actual:
            return False, "Usuario inválido"
        
        if not data:
            return False, "No hay datos para actualizar"
        
        conexion = None
        cursor = None
        try:
            # Validar email si se proporciona
            correo = data.get("email", "").strip()
            if correo:
                patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                if not re.match(patron_email, correo):
                    return False, "El formato del correo electrónico no es válido"
            
            # Validar teléfono si se proporciona
            telefono = data.get("num_contact", "").strip()
            if telefono:
                if not re.match(r'^[\d\-\+\(\)\s]+$', telefono):
                    return False, "El teléfono solo puede contener números y caracteres: + - ( )"
            
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos"
                
            cursor = conexion.cursor(dictionary=True)
            conexion.start_transaction()

            # Obtener datos actuales
            cursor.execute(
                "SELECT * FROM representantes WHERE id = %s", 
                (representante_id,)
            )
            representante_actual = cursor.fetchone()
            
            if not representante_actual:
                conexion.rollback()
                return False, "Representante no encontrado"

            # Detectar cambios
            cambios = []
            campos_actualizables = [
                "nombres", "apellidos", "fecha_nac", "genero",
                "direccion", "num_contact", "email", "observacion"
            ]
            
            mapa_nombres = {
                "nombres": "Nombres",
                "apellidos": "Apellidos",
                "fecha_nac": "Fecha de Nacimiento",
                "genero": "Género",
                "direccion": "Dirección",
                "num_contact": "Teléfono",
                "email": "Correo",
                "observacion": "Observación"
            }
            
            for campo in campos_actualizables:
                if campo in data:
                    nuevo_valor = data[campo]
                    valor_actual = representante_actual.get(campo)
                    
                    # Normalizar para comparación
                    nuevo_norm = str(nuevo_valor).strip() if nuevo_valor else ""
                    actual_norm = str(valor_actual).strip() if valor_actual else ""
                    
                    if actual_norm != nuevo_norm:
                        nombre_campo = mapa_nombres.get(campo, campo)
                        cambios.append(
                            f"{nombre_campo}: '{valor_actual or '(vacío)'}' → '{nuevo_valor or '(vacío)'}'"
                        )

            # Si no hay cambios, evitar UPDATE innecesario
            if not cambios:
                conexion.rollback()
                return True, "No se detectaron cambios en los datos"

            # Ejecutar UPDATE
            cursor.execute("""
                UPDATE representantes
                SET nombres=%s, apellidos_repre=%s, fecha_nac_repre=%s, genero_repre=%s,
                    direccion_repre=%s, num_contact_repre=%s, correo_repre=%s, observacion=%s
                WHERE id=%s
            """, (
                data.get("nombres"),
                data.get("apellidos"),
                data.get("fecha_nac"),
                data.get("genero"),
                data.get("direccion"),
                data.get("num_contact"),
                data.get("email"),
                data.get("observacion"),
                representante_id
            ))
            
            conexion.commit()

            # Auditoría
            descripcion = "; ".join(cambios)
            AuditoriaModel.registrar(
                usuario_id=usuario_actual["id"],
                accion="UPDATE",
                entidad="representantes",
                entidad_id=representante_id,
                referencia=representante_actual["cedula"],
                descripcion=f"Cambios: {descripcion}"
            )

            return True, "Representante actualizado correctamente"

        except Exception as e:
            if conexion:
                conexion.rollback()
            print(f"Error actualizando representante: {e}")
            return False, f"Error al actualizar: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def obtener_representante_id(estudiante_id: int) -> Optional[int]:
        """Obtiene el ID del representante asociado a un estudiante."""
        if not isinstance(estudiante_id, int) or estudiante_id <= 0:
            return None
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return None
                
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT representante_id FROM estudiantes WHERE id=%s", 
                (estudiante_id,)
            )
            row = cursor.fetchone()
            return row[0] if row else None
            
        except Exception as e:
            print(f"Error obteniendo representante_id: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def contar_hijos(representante_id: int) -> int:
        """Cuenta cuántos estudiantes tiene asociados un representante."""
        if not isinstance(representante_id, int) or representante_id <= 0:
            return 0
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return 0
                
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT COUNT(*) FROM estudiantes WHERE representante_id = %s",
                (representante_id,)
            )
            row = cursor.fetchone()
            return row[0] if row else 0
            
        except Exception as e:
            print(f"Error contando hijos: {e}")
            return 0
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def obtener_estudiantes_del_representante(representante_id: int) -> list:
        """Obtiene lista de estudiantes asociados a un representante."""
        if not isinstance(representante_id, int) or representante_id <= 0:
            return []
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return []
                
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("""
                SELECT 
                    id, 
                    cedula, 
                    nombres, 
                    apellidos,
                    TIMESTAMPDIFF(YEAR, fecha_nac, CURDATE()) AS edad,
                    estatus_academico,
                    CASE WHEN estado = 1 THEN 'Activo' ELSE 'Inactivo' END AS estado
                FROM estudiantes
                WHERE representante_id = %s
                ORDER BY apellidos, nombres
            """, (representante_id,))
            
            return cursor.fetchall()
            
        except Exception as e:
            print(f"Error obteniendo estudiantes del representante: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()