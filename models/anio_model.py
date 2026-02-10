from utils.db import get_connection
from models.auditoria_model import AuditoriaModel
from typing import Optional, Dict, List, Tuple
from datetime import datetime


class AnioEscolarModel:
    """Modelo de años escolares."""

    @staticmethod
    def obtener_actual() -> Optional[Dict]:
        """Devuelve el año escolar actual (es_actual = 1)."""
        conn = get_connection()
        if not conn:
            return None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT id, año_inicio, año_fin, nombre, fecha_inicio, fecha_fin,
                       estado, es_actual, creado_en, creado_por, cerrado_en, cerrado_por
                FROM años_escolares 
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
        """Obtiene un año escolar por ID."""
        if not isinstance(anio_id, int) or anio_id <= 0:
            return None
            
        conn = get_connection()
        if not conn:
            return None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT id, año_inicio, año_fin, nombre, fecha_inicio, fecha_fin,
                       estado, es_actual, creado_en, creado_por, cerrado_en, cerrado_por
                FROM años_escolares 
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
                SELECT id, año_inicio, año_fin, nombre, fecha_inicio, fecha_fin,
                       estado, es_actual, creado_en, creado_por, cerrado_en, cerrado_por
                FROM años_escolares 
                ORDER BY año_inicio {orden}
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
        año_inicio: int,
        usuario_actual: Dict,
        fecha_inicio: Optional[str] = None,
        duplicar_secciones: bool = True
    ) -> Tuple[bool, str]:
        """
        Apertura un nuevo año escolar.
        Desactiva el anterior, duplica secciones y promociona estudiantes.
        """
        # Validaciones de entrada
        if not isinstance(año_inicio, int) or año_inicio < 2000 or año_inicio > 2100:
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
                "SELECT id, nombre FROM años_escolares WHERE año_inicio = %s", 
                (año_inicio,)
            )
            if cursor.fetchone():
                conn.rollback()
                return False, f"El año escolar {año_inicio}-{año_inicio+1} ya existe."

            # 2. Obtener año actual antes de desactivarlo
            cursor.execute("""
                SELECT id, nombre FROM años_escolares 
                WHERE es_actual = 1 
                LIMIT 1
            """)
            anio_anterior = cursor.fetchone()

            # 3. Cerrar y desactivar año actual
            cursor.execute("""
                UPDATE años_escolares 
                SET es_actual = 0,
                    estado = 'cerrado',
                    cerrado_en = NOW(),
                    cerrado_por = %s
                WHERE es_actual = 1
            """, (usuario_actual["id"],))

            # 4. Crear nuevo año como activo
            año_fin = año_inicio + 1
            nombre = f"{año_inicio}-{año_fin}"
            fecha_inicio = fecha_inicio or datetime.now().strftime('%Y-%m-%d')
            
            cursor.execute("""
                INSERT INTO años_escolares 
                (año_inicio, año_fin, nombre, fecha_inicio, estado, es_actual, creado_por, creado_en)
                VALUES (%s, %s, %s, %s, 'activo', 1, %s, NOW())
            """, (año_inicio, año_fin, nombre, fecha_inicio, usuario_actual["id"]))
            
            nuevo_anio_id = cursor.lastrowid
            secciones_duplicadas = 0

            # 5. Crear secciones para el nuevo año basándose en la progresión
            # Se calculan las secciones que necesitará el nuevo año según 
            # la tabla de progresión de grados.
            if duplicar_secciones and anio_anterior:

                # Tabla de progresión de grados
                progression = {
                    ('Inicial', '1er Nivel'): ('Inicial', '2do Nivel'),
                    ('Inicial', '2do Nivel'): ('Inicial', '3er Nivel'),
                    ('Inicial', '3er Nivel'): ('Primaria', '1ero'),
                    ('Primaria', '1ero'): ('Primaria', '2do'),
                    ('Primaria', '2do'):  ('Primaria', '3ero'),
                    ('Primaria', '3ero'): ('Primaria', '4to'),
                    ('Primaria', '4to'):  ('Primaria', '5to'),
                    ('Primaria', '5to'):  ('Primaria', '6to'),
                    ('Primaria', '6to'):  ('Egresado', 'Egresado'),
                }

                # Obtener secciones activas del año anterior con conteo de estudiantes
                cursor.execute("""
                    SELECT s.id, s.nivel, s.grado, s.letra, s.salon, s.cupo_maximo,
                           COUNT(DISTINCT CASE WHEN e.estado = 1 AND e.estatus_academico = 'Regular'
                                 THEN se.estudiante_id END) AS cant_estudiantes
                    FROM secciones s
                    LEFT JOIN seccion_estudiante se ON se.seccion_id = s.id
                    LEFT JOIN estudiantes e ON se.estudiante_id = e.id
                    WHERE s.año_escolar_id = %s AND s.activo = 1
                    GROUP BY s.id, s.nivel, s.grado, s.letra, s.salon, s.cupo_maximo
                    ORDER BY s.nivel, s.grado, s.letra
                """, (anio_anterior['id'],))
                secciones_anterior = cursor.fetchall()

                # Calcular qué secciones necesita el nuevo año:
                # - Secciones destino de la progresión (donde irán los estudiantes promovidos)
                # - Sección de nuevo ingreso: 1er Nivel Única (siempre debe existir)
                secciones_a_crear = {}  # {(nivel, grado, letra): cupo_maximo}

                for seccion in secciones_anterior:
                    nivel = seccion['nivel']
                    grado = seccion['grado']
                    letra = seccion['letra']
                    cupo = seccion['cupo_maximo'] or 30

                    target = progression.get((nivel, grado))
                    if not target or target[0] == 'Egresado':
                        continue  # 6to -> Egresados, no necesita sección nueva

                    nuevo_nivel, nuevo_grado = target

                    # Resolver la letra destino:
                    # "Única" solo se usa en 1er Nivel. Al promover se mapea a "A".
                    if letra == "Única":
                        nueva_letra = "A"
                    else:
                        nueva_letra = letra

                    clave = (nuevo_nivel, nuevo_grado, nueva_letra)
                    if clave not in secciones_a_crear:
                        secciones_a_crear[clave] = cupo

                # Asegurar que siempre exista 1er Nivel Única para nuevos ingresos
                clave_1er = ('Inicial', '1er Nivel', 'Única')
                if clave_1er not in secciones_a_crear:
                    secciones_a_crear[clave_1er] = 30

                # Crear las secciones calculadas en el nuevo año
                mapa_secciones_nuevas = {}  # {(nivel, grado, letra): seccion_id}
                for (nivel, grado, letra), cupo in secciones_a_crear.items():
                    # Verificar que no exista ya (por si se duplicó)
                    cursor.execute("""
                        SELECT id FROM secciones
                        WHERE año_escolar_id = %s AND nivel = %s
                          AND grado = %s AND letra = %s
                    """, (nuevo_anio_id, nivel, grado, letra))
                    existente = cursor.fetchone()

                    if existente:
                        mapa_secciones_nuevas[(nivel, grado, letra)] = existente['id']
                    else:
                        cursor.execute("""
                            INSERT INTO secciones
                            (nivel, grado, letra, cupo_maximo, año_escolar_id, activo)
                            VALUES (%s, %s, %s, %s, %s, 1)
                        """, (nivel, grado, letra, cupo, nuevo_anio_id))
                        mapa_secciones_nuevas[(nivel, grado, letra)] = cursor.lastrowid
                        secciones_duplicadas += 1

                # Duplicar materias: asignar las materias que correspondan al grado destino
                # Buscar materias de la sección origen y copiar a la sección destino equivalente
                for seccion_ant in secciones_anterior:
                    nivel = seccion_ant['nivel']
                    grado = seccion_ant['grado']
                    letra = seccion_ant['letra']

                    target = progression.get((nivel, grado))
                    if not target or target[0] == 'Egresado':
                        continue

                    nuevo_nivel, nuevo_grado = target
                    nueva_letra = "A" if letra == "Única" else letra
                    clave_dest = (nuevo_nivel, nuevo_grado, nueva_letra)

                    if clave_dest in mapa_secciones_nuevas:
                        seccion_destino_id = mapa_secciones_nuevas[clave_dest]
                        # Copiar materias de una sección del mismo grado destino del año anterior
                        # (buscar sección del año anterior que tenga el mismo nivel/grado destino)
                        cursor.execute("""
                            SELECT id FROM secciones
                            WHERE año_escolar_id = %s AND nivel = %s AND grado = %s AND activo = 1
                            LIMIT 1
                        """, (anio_anterior['id'], nuevo_nivel, nuevo_grado))
                        sec_ref = cursor.fetchone()
                        if sec_ref:
                            # Copiar materias de esa sección de referencia
                            cursor.execute("""
                                SELECT materia_id FROM seccion_materia
                                WHERE seccion_id = %s
                            """, (sec_ref['id'],))
                            materias_ref = cursor.fetchall()
                            for mat in materias_ref:
                                cursor.execute("""
                                    INSERT IGNORE INTO seccion_materia (seccion_id, materia_id)
                                    VALUES (%s, %s)
                                """, (seccion_destino_id, mat['materia_id']))

            # 6. Promocionar estudiantes (import local para evitar circular)
            msg_promocion = ""
            if anio_anterior:
                from models.estu_model import EstudianteModel
                
                ok_promo, msg_promo = EstudianteModel.promover_masivo(
                    anio_anterior['id'], 
                    nuevo_anio_id,
                    conn=conn,
                    cursor=cursor
                )
                
                if ok_promo:
                    msg_promocion = f" {msg_promo}"
                else:
                    # Rollback completo de toda la transacción
                    conn.rollback()
                    return False, f"Error en promoción de estudiantes: {msg_promo}"

            # Commit de toda la transacción (año + secciones + promociones)
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
                entidad="años_escolares",
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
        """Calcula el próximo año a aperturar."""
        conn = get_connection()
        if not conn:
            return datetime.now().year
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT año_inicio 
                FROM años_escolares 
                ORDER BY año_inicio DESC 
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