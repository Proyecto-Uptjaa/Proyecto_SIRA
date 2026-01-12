from utils.db import get_connection
from models.auditoria_model import AuditoriaModel
from typing import Optional, Dict, List, Tuple
from datetime import datetime


class AnioEscolarModel:
    """Gestión completa del ciclo de años escolares"""

    @staticmethod
    def obtener_actual() -> Optional[Dict]:
        """Devuelve el año escolar marcado como actual (es_actual = 1)"""
        conn = get_connection()
        if not conn:
            return None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT id, anio_inicio, anio_fin, nombre, fecha_inicio, fecha_fin,
                       estado, es_actual, creado_en, creado_por, cerrado_en, cerrado_por
                FROM anios_escolares 
                WHERE es_actual = 1
                LIMIT 1
            """)
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al obtener año actual: {e}")
            return None
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def obtener_por_id(anio_id: int) -> Optional[Dict]:
        """Obtiene un año escolar específico por ID"""
        if not isinstance(anio_id, int) or anio_id <= 0:
            return None
            
        conn = get_connection()
        if not conn:
            return None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT id, anio_inicio, anio_fin, nombre, fecha_inicio, fecha_fin,
                       estado, es_actual, creado_en, creado_por, cerrado_en, cerrado_por
                FROM anios_escolares 
                WHERE id = %s
            """, (anio_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al obtener año por ID: {e}")
            return None
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def listar_todos(order_desc: bool = True) -> List[Dict]:
        """Lista todos los años escolares"""
        conn = get_connection()
        if not conn:
            return []
        try:
            cursor = conn.cursor(dictionary=True)
            orden = "DESC" if order_desc else "ASC"
            cursor.execute(f"""
                SELECT id, anio_inicio, anio_fin, nombre, fecha_inicio, fecha_fin,
                       estado, es_actual, creado_en, creado_por, cerrado_en, cerrado_por
                FROM anios_escolares 
                ORDER BY anio_inicio {orden}
            """)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al listar años escolares: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def aperturar_nuevo(
        anio_inicio: int,
        usuario_actual: Dict,
        fecha_inicio: Optional[str] = None,
        duplicar_secciones: bool = True
    ) -> Tuple[bool, str]:
        """
        Apertura oficial del nuevo año escolar.
        Solo permite un año activo a la vez.
        - Crea el nuevo año como activo
        - Desactiva el año anterior
        - Duplica secciones si se solicita
        - Promociona estudiantes automáticamente
        """
        # Validaciones de entrada
        if not isinstance(anio_inicio, int) or anio_inicio < 2000 or anio_inicio > 2100:
            return False, "Año de inicio inválido."
        
        if not usuario_actual or 'id' not in usuario_actual:
            return False, "Usuario no válido."
        
        if fecha_inicio:
            try:
                datetime.strptime(fecha_inicio, '%Y-%m-%d')
            except ValueError:
                return False, "Formato de fecha inválido (debe ser YYYY-MM-DD)."
        
        conn = get_connection()
        if not conn:
            return False, "Error de conexión a la base de datos."
        
        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            
            # Iniciar transacción explícita
            conn.start_transaction()

            # 1. Validar que no exista ya ese año
            cursor.execute(
                "SELECT id, nombre FROM anios_escolares WHERE anio_inicio = %s", 
                (anio_inicio,)
            )
            if cursor.fetchone():
                conn.rollback()
                return False, f"El año escolar {anio_inicio}-{anio_inicio+1} ya existe."

            # 2. Obtener año actual antes de desactivarlo
            cursor.execute("""
                SELECT id, nombre FROM anios_escolares 
                WHERE es_actual = 1 
                LIMIT 1
            """)
            anio_anterior = cursor.fetchone()

            # 3. Desactivar año actual
            cursor.execute("""
                UPDATE anios_escolares 
                SET es_actual = 0 
                WHERE es_actual = 1
            """)

            # 4. Crear nuevo año como activo
            anio_fin = anio_inicio + 1
            nombre = f"{anio_inicio}-{anio_fin}"
            fecha_inicio = fecha_inicio or datetime.now().strftime('%Y-%m-%d')
            
            cursor.execute("""
                INSERT INTO anios_escolares 
                (anio_inicio, anio_fin, nombre, fecha_inicio, estado, es_actual, creado_por, creado_en)
                VALUES (%s, %s, %s, %s, 'activo', 1, %s, NOW())
            """, (anio_inicio, anio_fin, nombre, fecha_inicio, usuario_actual["id"]))
            
            nuevo_anio_id = cursor.lastrowid
            secciones_duplicadas = 0

            # 5. Duplicar secciones del año anterior (si existe y se solicitó)
            if duplicar_secciones and anio_anterior:
                cursor.execute("""
                    SELECT nivel, grado, letra, salon, cupo_maximo, docente_id
                    FROM secciones 
                    WHERE año_escolar_id = %s AND activo = 1
                """, (anio_anterior['id'],))
                
                secciones_anterior = cursor.fetchall()
                
                for seccion in secciones_anterior:
                    cursor.execute("""
                        INSERT INTO secciones 
                        (nivel, grado, letra, salon, cupo_maximo, docente_id, año_escolar_id, activo)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, 1)
                    """, (
                        seccion['nivel'],
                        seccion['grado'],
                        seccion['letra'],
                        seccion['salon'],
                        seccion['cupo_maximo'],
                        None,  # Sin maestro asignado
                        nuevo_anio_id
                    ))
                    secciones_duplicadas += 1

            # 6. Promocionar estudiantes (import local para evitar circular)
            msg_promocion = ""
            if anio_anterior:
                from models.estu_model import EstudianteModel
                
                ok_promo, msg_promo = EstudianteModel.promover_masivo(
                    anio_anterior['id'], 
                    nuevo_anio_id
                )
                
                if ok_promo:
                    msg_promocion = f" {msg_promo}"
                else:
                    # Si falla la promoción, hacer rollback
                    conn.rollback()
                    return False, f"Error en promoción de estudiantes: {msg_promo}"

            # Commit de toda la transacción
            conn.commit()

            # 7. Auditoría
            descripcion = f"Apertura año {nombre}."
            if secciones_duplicadas > 0:
                descripcion += f" {secciones_duplicadas} secciones duplicadas."
            if msg_promocion:
                descripcion += msg_promocion
                
            AuditoriaModel.registrar(
                usuario_id=usuario_actual["id"],
                accion="APERTURA_AÑO",
                entidad="anios_escolares",
                entidad_id=nuevo_anio_id,
                referencia=nombre,
                descripcion=descripcion
            )

            return True, f"Año escolar {nombre} aperturado correctamente.{msg_promocion}"

        except Exception as e:
            if conn:
                conn.rollback()
            return False, f"Error al aperturar año: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    @staticmethod
    def obtener_proximo_año() -> int:
        """Calcula el próximo año a aperturar basándose en el más reciente"""
        conn = get_connection()
        if not conn:
            return datetime.now().year
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT anio_inicio 
                FROM anios_escolares 
                ORDER BY anio_inicio DESC 
                LIMIT 1
            """)
            resultado = cursor.fetchone()
            
            if resultado:
                return resultado[0] + 1
            else:
                # Si no hay años, devolver el año actual
                return datetime.now().year
                
        except Exception as e:
            print(f"Error al obtener próximo año: {e}")
            return datetime.now().year
        finally:
            cursor.close()
            conn.close()