import re
from utils.db import get_connection
from models.auditoria_model import AuditoriaModel
from typing import Optional, Dict, Tuple


class InstitucionModel:
    """Modelo de la institución educativa (ID=1)."""
    
    @staticmethod
    def actualizar(institucion_id: int, data: dict, usuario_actual: dict) -> Tuple[bool, str]:
        """Actualiza los datos de la institución."""
        conexion = None
        cursor = None
        try:
            # --- VALIDACIONES ---
            
            # Validar campos obligatorios
            campos_requeridos = ["nombre", "codigo_dea", "direccion"]
            for campo in campos_requeridos:
                valor = data.get(campo, "").strip() if data.get(campo) else ""
                if not valor:
                    return False, f"El campo '{campo}' es obligatorio"
            
            # Validar email si se proporciona
            correo = data.get("correo", "").strip()
            if correo:
                patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                if not re.match(patron_email, correo):
                    return False, "El formato del correo electrónico no es válido"
            
            # Validar teléfono si se proporciona
            telefono = data.get("telefono", "").strip()
            if telefono:
                if not re.match(r'^[\d\-\+\(\)\s]+$', telefono):
                    return False, "El teléfono solo puede contener números y caracteres: + - ( )"
            
            # Validar RIF si se proporciona
            rif = data.get("rif", "").strip()
            if rif:
                # Formato: J-12345678-9 o similar
                if not re.match(r'^[JGVE]-?\d{8,9}-?\d?$', rif.upper()):
                    return False, "El formato del RIF no es válido (ej: J-12345678-9)"
            
            # Validar cédula del director si se proporciona
            director_ci = data.get("director_ci", "").strip()
            if director_ci:
                if not director_ci.replace(".", "").replace("-", "").isdigit():
                    return False, "La cédula del director debe ser numérica"
            
            # --- CONEXIÓN BD ---
            
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos"
            
            cursor = conexion.cursor(dictionary=True)

            # Obtener datos actuales antes de modificar
            cursor.execute("SELECT * FROM institucion WHERE id=%s", (institucion_id,))
            institucion_actual = cursor.fetchone()
            
            if not institucion_actual:
                return False, "Institución no encontrada"

            # Detectar cambios
            def normalizar(valor):
                """Normaliza valores para comparación"""
                if valor is None:
                    return None
                if isinstance(valor, str):
                    return valor.strip() or None
                return str(valor)

            cambios = []
            mapa_nombres = {
                "nombre": "Nombre",
                "codigo_dea": "Código DEA",
                "codigo_dependencia": "Código de Dependencia",
                "codigo_estadistico": "Código Estadístico",
                "rif": "RIF",
                "direccion": "Dirección",
                "telefono": "Teléfono",
                "correo": "Correo",
                "director": "Director",
                "director_ci": "CI Director"
            }
            
            for campo, nuevo_valor in data.items():
                if campo in institucion_actual:
                    valor_actual = institucion_actual.get(campo)
                    nuevo_norm = normalizar(nuevo_valor)
                    actual_norm = normalizar(valor_actual)
                    
                    if actual_norm != nuevo_norm:
                        nombre_campo = mapa_nombres.get(campo, campo)
                        cambios.append(f"{nombre_campo}: '{valor_actual or '(vacío)'}' → '{nuevo_valor or '(vacío)'}'")

            # Si no hay cambios, evitar UPDATE innecesario
            if not cambios:
                return True, "No se detectaron cambios en los datos"

            # Ejecutar UPDATE
            cursor.execute("""
                UPDATE institucion
                SET nombre=%s, codigo_dea=%s, codigo_dependencia=%s, codigo_estadistico=%s, 
                    rif=%s, direccion=%s, telefono=%s, correo=%s, director=%s, director_ci=%s
                WHERE id=%s
            """, (
                data.get("nombre", "").strip() or None,
                data.get("codigo_dea", "").strip() or None,
                data.get("codigo_dependencia", "").strip() or None,
                data.get("codigo_estadistico", "").strip() or None,
                data.get("rif", "").strip() or None,
                data.get("direccion", "").strip() or None,
                data.get("telefono", "").strip() or None,
                data.get("correo", "").strip() or None,
                data.get("director", "").strip() or None,
                data.get("director_ci", "").strip() or None,
                institucion_id
            ))
            conexion.commit()

            # Registrar en auditoría
            descripcion = "; ".join(cambios)
            AuditoriaModel.registrar(
                usuario_id=usuario_actual["id"],
                accion="UPDATE",
                entidad="institucion",
                entidad_id=institucion_id,
                referencia=data.get("nombre", institucion_actual["nombre"]),
                descripcion=f"Cambios: {descripcion}"
            )

            return True, "Datos de la institución actualizados correctamente"

        except Exception as e:
            if conexion:
                conexion.rollback()
            return False, f"Error al actualizar institución: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
    
    @staticmethod
    def obtener_por_id(institucion_id: int) -> Optional[Dict]:
        """Obtiene los datos de la institución."""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return None
            
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("""
                SELECT nombre, codigo_dea, codigo_dependencia, codigo_estadistico, 
                       rif, direccion, telefono, correo, director, director_ci, 
                       actualizado_en, logo
                FROM institucion
                WHERE id = %s
            """, (institucion_id,))
            
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
    def inicializar_si_no_existe() -> Tuple[bool, str]:
        """Crea el registro de institución si no existe (ID=1)."""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos"
            
            cursor = conexion.cursor()
            
            # Verificar si existe el registro
            cursor.execute("SELECT id FROM institucion WHERE id = 1")
            if cursor.fetchone():
                return True, "Institución ya inicializada"
            
            # Crear registro por defecto
            cursor.execute("""
                INSERT INTO institucion (id, nombre, codigo_dea, direccion)
                VALUES (1, 'Institución Educativa', 'DEA-000000', 'Dirección por definir')
            """)
            conexion.commit()
            
            return True, "Institución inicializada con datos por defecto"
            
        except Exception as e:
            if conexion:
                conexion.rollback()
            return False, f"Error al inicializar institución: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def guardar_logo(institucion_id: int, logo_bytes: bytes, usuario_actual: dict) -> Tuple[bool, str]:
        """Guarda el logo de la institución en la base de datos."""
        
        conexion = None
        cursor = None
        try:
            if not logo_bytes:
                return False, "No se proporcionaron datos de imagen"
            
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos"
            
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE institucion SET logo = %s WHERE id = %s",
                (logo_bytes, institucion_id)
            )
            conexion.commit()
            
            # Registrar en auditoría
            AuditoriaModel.registrar(
                usuario_id=usuario_actual["id"],
                accion="UPDATE",
                entidad="institucion",
                entidad_id=institucion_id,
                referencia="Logo institucional",
                descripcion="Se actualizó el logo de la institución"
            )
            
            return True, "Logo actualizado correctamente"
            
        except Exception as e:
            if conexion:
                conexion.rollback()
            return False, f"Error al guardar logo: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
    
    @staticmethod
    def obtener_logo(institucion_id: int = 1) -> Optional[bytes]:
        """Obtiene los bytes del logo de la institución."""
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return None
            
            cursor = conexion.cursor()
            cursor.execute("SELECT logo FROM institucion WHERE id = %s", (institucion_id,))
            resultado = cursor.fetchone()
            
            if resultado and resultado[0]:
                return bytes(resultado[0])
            return None
            
        except Exception as e:
            print(f"Error al obtener logo: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
    
    @staticmethod
    def eliminar_logo(institucion_id: int, usuario_actual: dict) -> Tuple[bool, str]:
        """Elimina el logo de la institución (establece NULL)."""
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos"
            
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE institucion SET logo = NULL WHERE id = %s",
                (institucion_id,)
            )
            conexion.commit()
            
            AuditoriaModel.registrar(
                usuario_id=usuario_actual["id"],
                accion="UPDATE",
                entidad="institucion",
                entidad_id=institucion_id,
                referencia="Logo institucional",
                descripcion="Se eliminó el logo de la institución"
            )
            
            return True, "Logo eliminado correctamente"
            
        except Exception as e:
            if conexion:
                conexion.rollback()
            return False, f"Error al eliminar logo: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()