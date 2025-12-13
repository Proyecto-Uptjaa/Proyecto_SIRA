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
            resultado = cursor.fetchone()
            return resultado
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def obtener_por_id(anio_id: int) -> Optional[Dict]:
        """Obtiene un año escolar específico por ID"""
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
            resultado = cursor.fetchone()
            return resultado
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
            resultados = cursor.fetchall()
            return resultados
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
        """
        from models.estu_model import EstudianteModel # Import local to avoid circular ref
        conn = get_connection()
        if not conn:
            return False, "Error de conexión a la base de datos."
        
        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)

            # 1. Validar que no exista ya ese año
            cursor.execute(
                "SELECT id FROM anios_escolares WHERE anio_inicio = %s", 
                (anio_inicio,)
            )
            if cursor.fetchone():
                return False, f"El año escolar {anio_inicio}-{anio_inicio+1} ya existe."

            # 2. Desactivar año actual (si existe)
            cursor.execute("UPDATE anios_escolares SET es_actual = 0 WHERE es_actual = 1")

            # 3. Crear nuevo año como activo
            anio_fin = anio_inicio + 1
            nombre = f"{anio_inicio}-{anio_fin}"
            fecha_inicio = fecha_inicio or datetime.now().strftime('%Y-%m-%d')
            
            cursor.execute("""
                INSERT INTO anios_escolares 
                (anio_inicio, anio_fin, nombre, fecha_inicio, estado, es_actual, creado_por, creado_en)
                VALUES (%s, %s, %s, %s, 'activo', 1, %s, NOW())
            """, (anio_inicio, anio_fin, nombre, fecha_inicio, usuario_actual["id"]))
            
            nuevo_anio_id = cursor.lastrowid

            # 4. Duplicar secciones del año anterior (si se pidió)
            if duplicar_secciones:
                # Obtener el ID del año anterior
                cursor.execute("""
                    SELECT id FROM anios_escolares 
                    WHERE anio_inicio = %s
                    LIMIT 1
                """, (anio_inicio - 1,))
                anio_anterior = cursor.fetchone()
                
                if anio_anterior:
                    # Obtener todas las secciones del año anterior
                    cursor.execute("""
                        SELECT nivel, grado, letra, salon, cupo_maximo, maestra_id
                        FROM secciones 
                        WHERE año_escolar_id = %s AND activo = 1
                    """, (anio_anterior['id'],))
                    
                    secciones_anterior = cursor.fetchall()
                    
                    # Duplicarlas para el nuevo año
                    for seccion in secciones_anterior:
                        cursor.execute("""
                            INSERT INTO secciones 
                            (nivel, grado, letra, salon, cupo_maximo, maestra_id, año_escolar_id, activo)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, 1)
                        """, (
                            seccion['nivel'],
                            seccion['grado'],
                            seccion['letra'],
                            seccion['salon'],
                            seccion['cupo_maximo'],
                            None,  # Sin maestro asignado aún
                            nuevo_anio_id
                        ))

            conn.commit()

            # 5. Promocionar estudiantes del año anterior
            msg_promocion = ""
            if anio_anterior:
                # Nota: Pasamos duplicar_secciones=True implícitamente si llegamos aquí y anio_anterior existe
                # Pero la función promover_masivo requiere que las secciones destino ya existan.
                # Como acabamos de duplicarlas (paso 4), deberían existir.
                ok_promo, msg_promo = EstudianteModel.promover_masivo(anio_anterior['id'], nuevo_anio_id)
                msg_promocion = f" ({msg_promo})"

            conn.commit()

            # 6. Auditoría
            AuditoriaModel.registrar(
                usuario_id=usuario_actual["id"],
                accion="APERTURA_AÑO",
                entidad="anios_escolares",
                entidad_id=nuevo_anio_id,
                referencia=nombre,
                descripcion=f"Apertura año {nombre}. Secciones duplicadas. {msg_promocion}"
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
    def cerrar_anio_actual(usuario_actual: Dict) -> Tuple[bool, str]:
        """Marca el año actual como 'cerrado' y quita la bandera es_actual"""
        conn = get_connection()
        if not conn:
            return False, "Error de conexión a la base de datos."
        
        cursor = None
        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE anios_escolares 
                SET estado = 'cerrado', es_actual = 0, cerrado_en = NOW(), cerrado_por = %s
                WHERE es_actual = 1
            """, (usuario_actual["id"],))
            
            if cursor.rowcount == 0:
                return False, "No hay año escolar activo para cerrar."

            conn.commit()

            AuditoriaModel.registrar(
                usuario_id=usuario_actual["id"],
                accion="CIERRE_ANIO",
                entidad="anios_escolares",
                entidad_id=None,
                referencia="año actual",
                descripcion="Cierre oficial del año escolar activo"
            )

            return True, "Año escolar cerrado correctamente."

        except Exception as e:
            if conn:
                conn.rollback()
            return False, f"Error al cerrar año: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    @staticmethod
    def obtener_proximo_año() -> int:
        """Calcula el próximo año a aperturar basándose en el actual"""
        conn = get_connection()
        if not conn:
            return datetime.now().year + 1
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT anio_inicio FROM anios_escolares ORDER BY anio_inicio DESC LIMIT 1")
            resultado = cursor.fetchone()
            cursor.close()
            conn.close()
            
            if resultado:
                return resultado[0] + 1
            else:
                return datetime.now().year
        except:
            return datetime.now().year + 1