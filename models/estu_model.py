# models/estudiante_model.py
from utils.db import get_connection
from models.auditoria_model import AuditoriaModel
from models.anio_model import AnioEscolarModel
from datetime import datetime

class EstudianteModel:
    """Modelo de estudiantes con conexión bajo demanda."""

    @staticmethod
    def generar_cedula_estudiantil(fecha_nac, cedula_madre: str) -> str:
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor()

            # Contar hijos actuales
            hijos_actuales = 0
            prefijo = 1
            if cedula_madre:
                cursor.execute("SELECT COUNT(*) FROM estudiantes WHERE madre_ci = %s", (cedula_madre,))
                hijos_actuales = cursor.fetchone()[0]
                # Año nacimiento
                anio = fecha_nac.year
                anio_dos = str(anio)[-2:]
                if hijos_actuales > 0:
                    # Si ya hay otro hijo en ese año
                    mismos_anio = 0
                    cursor.execute("""
                        SELECT COUNT(*) FROM estudiantes
                        WHERE madre_ci = %s AND YEAR(fecha_nac_est) = %s
                    """, (cedula_madre, anio))
                    mismos_anio = cursor.fetchone()[0]
                    prefijo = str(mismos_anio + 1)

                return f"{prefijo}{anio_dos}{cedula_madre}" # Ej: 2 15 12345678
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()

    @staticmethod
    def obtener_por_id(estudiante_id: int):
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor(dictionary=True, buffered=True)
            cursor.execute("""
                SELECT e.id, e.cedula, e.nombres, e.apellidos, e.fecha_nac_est, e.city, e.genero, 
                       e.direccion, e.fecha_ingreso, e.docente, e.tallaC, e.tallaP, e.tallaZ,
                       e.padre, e.padre_ci, e.ocupacion_padre, e.madre, e.madre_ci, e.ocupacion_madre, 
                       e.representante_id, e.estado, e.estatus_academico,
                       COALESCE(s.nivel, 'Sin asignar') AS tipo_educacion,
                       COALESCE(s.grado, 'Sin asignar') AS grado,
                       COALESCE(s.letra, 'Sin asignar') AS seccion,
                       se.seccion_id, se.año_asignacion
                FROM estudiantes e
                LEFT JOIN seccion_estudiante se ON e.id = se.estudiante_id
                LEFT JOIN secciones s ON se.seccion_id = s.id
                WHERE e.id = %s
                ORDER BY se.año_asignacion DESC
                LIMIT 1
            """, (estudiante_id,))
            return cursor.fetchone()
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()

    @staticmethod
    def guardar(estudiante_data: dict, representante_data: dict, usuario_actual: dict, seccion_id: int = None):
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor(dictionary=True)

            # 1. Insertar o recuperar representante
            cursor.execute("SELECT id FROM representantes WHERE cedula_repre = %s", (representante_data["cedula_repre"],))
            row = cursor.fetchone()
            if row:
                representante_id = row["id"]
            else:
                sql_repre = """
                    INSERT INTO representantes (cedula_repre, nombres_repre, apellidos_repre, fecha_nac_repre,
                                                genero_repre, direccion_repre, num_contact_repre, correo_repre, observacion)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """
                valores_repre = (
                    representante_data["cedula_repre"], representante_data["nombres_repre"], representante_data["apellidos_repre"],
                    representante_data["fecha_nac_repre"], representante_data["genero_repre"], representante_data["direccion_repre"],
                    representante_data["num_contact_repre"], representante_data["correo_repre"], representante_data["observacion"],
                )
                cursor.execute(sql_repre, valores_repre)
                representante_id = cursor.lastrowid

            # 2. Insertar estudiante (SIN tipo_educacion, grado, seccion)
            sql_estu = """
                INSERT INTO estudiantes (cedula, apellidos, nombres, fecha_nac_est, city, genero, direccion, fecha_ingreso,
                                        docente, tallaC, tallaP, tallaZ, madre, madre_ci,
                                        ocupacion_madre, padre, padre_ci, ocupacion_padre, representante_id)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            valores_estu = (
                estudiante_data["cedula"], estudiante_data["apellidos"], estudiante_data["nombres"], estudiante_data["fecha_nac_est"],
                estudiante_data["city"], estudiante_data["genero"], estudiante_data["direccion"], estudiante_data["fecha_ingreso"],
                estudiante_data["docente"], estudiante_data["tallaC"], estudiante_data["tallaP"], estudiante_data["tallaZ"], 
                estudiante_data["madre"], estudiante_data["madre_ci"], estudiante_data["ocupacion_madre"], 
                estudiante_data["padre"], estudiante_data["padre_ci"], estudiante_data["ocupacion_padre"],
                representante_id
            )
            cursor.execute(sql_estu, valores_estu)
            estudiante_id = cursor.lastrowid

            # 3. Asignar a sección si viene especificada
            if seccion_id:
                cursor.execute("""
                    INSERT INTO seccion_estudiante (estudiante_id, seccion_id, año_asignacion)
                    VALUES (%s, %s, CURDATE())
                """, (estudiante_id, seccion_id))

            # 4. Auditoría
            AuditoriaModel.registrar(
                usuario_id=usuario_actual["id"],
                accion="INSERT",
                entidad="estudiantes",
                entidad_id=estudiante_id,
                referencia=estudiante_data["cedula"],
                descripcion=f"Se registró estudiante {estudiante_data['nombres']} {estudiante_data['apellidos']}"
            )

            conexion.commit()
            return True, "Registro de estudiante realizado correctamente."

        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def actualizar(estudiante_id: int, data: dict, usuario_actual: dict, seccion_id: int = None):
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor(dictionary=True)

            # 1. Obtener datos actuales antes de modificar
            cursor.execute("SELECT * FROM estudiantes WHERE id=%s", (estudiante_id,))
            estudiante_actual = cursor.fetchone()
            if not estudiante_actual:
                return False, "Estudiante no encontrado."

            # 2. Detectar cambios (solo campos que existen en estudiantes)
            cambios = []
            campos_validos = ["nombres", "apellidos", "fecha_nac_est", "city", "genero", "direccion", 
                             "fecha_ingreso", "docente", "tallaC", "tallaP", "tallaZ", "padre", "padre_ci", 
                             "ocupacion_padre", "madre", "madre_ci", "ocupacion_madre"]
            
            for campo in campos_validos:
                if campo in data:
                    nuevo_valor = data[campo]
                    valor_actual = estudiante_actual.get(campo)
                    if str(valor_actual) != str(nuevo_valor):
                        cambios.append(f"{campo}: '{valor_actual}' → '{nuevo_valor}'")

            # 3. Ejecutar UPDATE (SIN tipo_educacion, grado, seccion)
            cursor.execute("""
                UPDATE estudiantes
                SET nombres=%s, apellidos=%s, fecha_nac_est=%s, city=%s, genero=%s,
                    direccion=%s, fecha_ingreso=%s, docente=%s,
                    tallaC=%s, tallaP=%s, tallaZ=%s, padre=%s, padre_ci=%s, ocupacion_padre=%s, 
                    madre=%s, madre_ci=%s, ocupacion_madre=%s
                WHERE id=%s
            """, (
                data.get("nombres"), data.get("apellidos"), data.get("fecha_nac_est"), 
                data.get("city"), data.get("genero"), data.get("direccion"), 
                data.get("fecha_ingreso"), data.get("docente"), data.get("tallaC"), 
                data.get("tallaP"), data.get("tallaZ"), data.get("padre"), data.get("padre_ci"), 
                data.get("ocupacion_padre"), data.get("madre"), data.get("madre_ci"), 
                data.get("ocupacion_madre"), estudiante_id
            ))

            # 4. Si cambió la sección, actualizar en seccion_estudiante
            # Primero intentamos resolver el ID de sección si no viene, pero vienen los datos textuales
            final_seccion_id = seccion_id
            
            # Importar modelo de año escolar aquí para evitar ciclos
            from models.anio_model import AnioEscolarModel
            
            anio_info = AnioEscolarModel.obtener_actual()
            if anio_info:
                anio_id = anio_info['id']
                anio_num = anio_info['anio_inicio']
                
                if not final_seccion_id and all(k in data for k in ["tipo_educacion", "grado", "seccion"]):
                    nivel = data["tipo_educacion"]
                    grado = data["grado"]
                    letra = data["seccion"]
                    
                    if nivel != "Sin asignar" and grado != "Sin asignar" and letra != "Sin asignar":
                        cursor.execute("""
                            SELECT id FROM secciones 
                            WHERE nivel=%s AND grado=%s AND letra=%s AND año_escolar_id=%s
                        """, (nivel, grado, letra, anio_id))
                        row = cursor.fetchone()
                        if row:
                            final_seccion_id = row['id']

                # Si tenemos un ID validado, procedemos a asignar
                if final_seccion_id:
                    
                    # 4.1. Eliminar asignaciones previas de este año
                    cursor.execute("""
                        DELETE FROM seccion_estudiante 
                        WHERE estudiante_id = %s AND año_asignacion = %s
                    """, (estudiante_id, anio_num))
                    
                    # 4.2. Insertar nueva
                    cursor.execute("""
                        INSERT INTO seccion_estudiante (estudiante_id, seccion_id, año_asignacion)
                        VALUES (%s, %s, %s)
                    """, (estudiante_id, final_seccion_id, anio_num))
                    
                    # 4.3. Historial
                    cursor.execute("""
                        INSERT INTO historial_secciones (estudiante_id, seccion_id, año_inicio, fecha_asignacion)
                        VALUES (%s, %s, %s, CURDATE())
                        ON DUPLICATE KEY UPDATE 
                            seccion_id = VALUES(seccion_id),
                            fecha_asignacion = CURDATE()
                    """, (estudiante_id, final_seccion_id, anio_num))
                    
                    cambios.append(f"Sección: Asignado a seccion_id {final_seccion_id} ({anio_num})")

            conexion.commit()

            # 5. Registrar auditoría si hubo cambios
            if cambios:
                descripcion = "; ".join(cambios)
                AuditoriaModel.registrar(
                    usuario_id=usuario_actual["id"],
                    accion="UPDATE",
                    entidad="estudiantes",
                    entidad_id=estudiante_id,
                    referencia=estudiante_actual["cedula"],
                    descripcion=f"Cambios: {descripcion}"
                )

            return True, "Estudiante actualizado correctamente."

        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def eliminar(estudiante_id: int, usuario_actual: dict):
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor(dictionary=True)

            # 1. Obtener datos del estudiante
            cursor.execute("SELECT * FROM estudiantes WHERE id = %s", (estudiante_id,))
            estudiante = cursor.fetchone()
            if not estudiante:
                return False, "No se encontró el estudiante en la BD."

            id_representante = estudiante["representante_id"]

            # 2. Contar hijos del representante
            cursor.execute("SELECT COUNT(*) as total FROM estudiantes WHERE representante_id = %s", (id_representante,))
            hijos_count = cursor.fetchone()["total"]

            # 3. Obtener grado/sección para auditoría
            cursor.execute("""
                SELECT COALESCE(s.grado, '-') AS grado, COALESCE(s.letra, '-') AS seccion
                FROM estudiantes e
                LEFT JOIN seccion_estudiante se ON e.id = se.estudiante_id
                LEFT JOIN secciones s ON se.seccion_id = s.id
                WHERE e.id = %s
            """, (estudiante_id,))
            seccion_info = cursor.fetchone()

            # 4. Registrar auditoría
            AuditoriaModel.registrar(
                usuario_id=usuario_actual["id"],
                accion="DELETE",
                entidad="estudiantes",
                entidad_id=estudiante_id,
                referencia=estudiante["cedula"],
                descripcion=f"Se eliminó estudiante {estudiante['nombres']} {estudiante['apellidos']} (grado: {seccion_info['grado']}, sección: {seccion_info['seccion']})"
            )

            # 5. Eliminar de seccion_estudiante
            cursor.execute("DELETE FROM seccion_estudiante WHERE estudiante_id = %s", (estudiante_id,))

            # 6. Eliminar estudiante
            cursor.execute("DELETE FROM estudiantes WHERE id = %s", (estudiante_id,))

            # 7. Si era el único hijo, eliminar representante
            if hijos_count == 1:
                cursor.execute("DELETE FROM representantes WHERE id = %s", (id_representante,))

            conexion.commit()
            return True, "Eliminación realizada correctamente."

        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def listar(anio_escolar_id=None):
        """Lista todos los estudiantes del año especificado"""
        conexion = None
        cursor = None
        try:
            if anio_escolar_id is None:
                # Obtener el año actual del sistema
                anio_actual = AnioEscolarModel.obtener_actual()
                anio_escolar_id = anio_actual['id'] if anio_actual else None
                
                if not anio_escolar_id:
                    return []
            
            conexion = get_connection()
            cursor = conexion.cursor(dictionary=True)

            # 1. Obtener el año inicio del año escolar solicitado
            cursor.execute("SELECT anio_inicio FROM anios_escolares WHERE id = %s", (anio_escolar_id,))
            row_anio = cursor.fetchone()
            if not row_anio:
                return []
            target_year = row_anio['anio_inicio']

            # 2. Listar estudiantes con asignación en ese año
            cursor.execute("""
                SELECT 
                    e.id, e.cedula, e.nombres, e.apellidos, e.fecha_nac_est,
                    TIMESTAMPDIFF(YEAR, e.fecha_nac_est, CURDATE()) AS edad,
                    e.city, e.genero, e.direccion, e.docente,
                    e.tallaC, e.tallaP, e.tallaZ,
                    COALESCE(s.nivel, 'Sin asignar') AS tipo_educacion,
                    COALESCE(s.grado, 'Sin asignar') AS grado,
                    COALESCE(s.letra, 'Sin asignar') AS seccion,
                    e.estatus_academico,
                    CASE WHEN e.estado = 1 THEN 'Activo' ELSE 'Inactivo' END AS estado
                FROM estudiantes e
                LEFT JOIN seccion_estudiante se ON e.id = se.estudiante_id AND se.año_asignacion = %s
                LEFT JOIN secciones s ON se.seccion_id = s.id AND s.año_escolar_id = %s
                WHERE e.estatus_academico = 'Regular'
                ORDER BY e.apellidos, e.nombres
            """, (target_year, anio_escolar_id,))

            return cursor.fetchall()
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()
    
    @staticmethod
    def listar_activos():
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("""
                SELECT e.id, e.cedula, e.nombres, e.apellidos, e.fecha_nac_est,
                    TIMESTAMPDIFF(YEAR, e.fecha_nac_est, CURDATE()) AS edad,
                    e.city, e.genero, e.direccion, e.fecha_ingreso,
                    COALESCE(s.nivel, 'Sin asignar') AS tipo_educacion,
                    COALESCE(s.grado, 'Sin asignar') AS grado,
                    COALESCE(s.letra, 'Sin asignar') AS seccion,
                    e.docente, e.tallaC, e.tallaP, e.tallaZ, e.padre,
                    e.padre_ci, e.ocupacion_padre, e.madre, e.madre_ci, e.ocupacion_madre,
                    e.estatus_academico,
                    CASE WHEN e.estado = 1 THEN 'Activo' ELSE 'Inactivo' END AS estado,
                    r.cedula_repre, r.nombres_repre, r.apellidos_repre,
                    r.num_contact_repre, r.observacion
                FROM estudiantes e
                LEFT JOIN seccion_estudiante se ON e.id = se.estudiante_id
                LEFT JOIN secciones s ON se.seccion_id = s.id
                JOIN representantes r ON e.representante_id = r.id
                WHERE e.estado = 1
            """)
            return cursor.fetchall()
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()

    @staticmethod
    def obtener_secciones_activas(año):
        """Devuelve todas las secciones activas del año para los combos de registro"""
        conn = get_connection()
        if not conn:
            return []
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT s.id, s.nivel, s.grado, s.letra
                FROM secciones s
                INNER JOIN anios_escolares a ON s.año_escolar_id = a.id
                WHERE a.anio_inicio = %s AND s.activo = 1
                ORDER BY 
                    FIELD(s.nivel, 'Inicial', 'Primaria'),
                    s.grado, s.letra
            """, (año,))
            resultado = cursor.fetchall()
            cursor.close()
            conn.close()
            return resultado
        except Exception as e:
            print(f"Error cargando secciones: {e}")
            return []

    @staticmethod
    def asignar_a_seccion(estudiante_id, seccion_id, año_actual):
        """Asigna el estudiante a una sección, eliminando asignaciones previas del año actual"""
        conn = get_connection()
        if not conn:
            return False
        cursor = None
        try:
            cursor = conn.cursor()
            #año_actual = datetime.now().year
            
            # 1. Eliminar todas las asignaciones del estudiante del año actual
            cursor.execute("""
                DELETE FROM seccion_estudiante 
                WHERE estudiante_id = %s AND año_asignacion = %s
            """, (estudiante_id, año_actual))
            
            # 2. Insertar la nueva asignación
            cursor.execute("""
                INSERT INTO seccion_estudiante (estudiante_id, seccion_id, año_asignacion)
                VALUES (%s, %s, %s)
            """, (estudiante_id, seccion_id, año_actual))

            # 3. Registrar en Historial (Idempotente para el año)
            cursor.execute("""
                INSERT INTO historial_secciones (estudiante_id, seccion_id, año_inicio, fecha_asignacion)
                VALUES (%s, %s, %s, CURDATE())
                ON DUPLICATE KEY UPDATE 
                    seccion_id = VALUES(seccion_id),
                    fecha_asignacion = CURDATE()
            """, (estudiante_id, seccion_id, año_actual))
            
            conn.commit()
            return True
        except Exception as e:
            print(f"Error asignando sección: {e}")
            if conn:
                conn.rollback()
            return False
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    @staticmethod
    def listar_por_seccion(seccion_id, año, incluir_inactivos=False):
        """
        Devuelve los estudiantes asignados a una seccion (filtrados por año de año_asignacion).
        Si año es None usa el año actual.
        """
        conn = get_connection()
        if not conn:
            return []
        try:
            if año is None:
                año = datetime.now().year
            cursor = conn.cursor(dictionary=True)
            sql = """
                SELECT e.id, e.cedula, e.nombres, e.apellidos,
                       TIMESTAMPDIFF(YEAR, e.fecha_nac_est, CURDATE()) AS edad,
                       e.genero,
                       CASE WHEN e.estado = 1 THEN 'Activo' ELSE 'Inactivo' END AS estado,
                       se.seccion_id
                FROM seccion_estudiante se
                JOIN estudiantes e ON e.id = se.estudiante_id
                WHERE se.seccion_id = %s AND se.año_asignacion = %s
            """
            if not incluir_inactivos:
                sql += " AND e.estado = 1"
            sql += " ORDER BY e.apellidos, e.nombres"
            cursor.execute(sql, (seccion_id, año))
            filas = cursor.fetchall()
            cursor.close()
            conn.close()
            return filas
        except Exception as e:
            print(f"Error en listar_por_seccion: {e}")
            try:
                cursor.close()
                conn.close()
            except:
                pass
            return []

    @staticmethod
    def promover_masivo(anio_anterior_id, nuevo_anio_id):
        """
        Promueve a los estudiantes del año anterior al siguiente grado en el nuevo año.
        """
        conn = get_connection()
        if not conn:
            return False, "Error de conexión"
        
        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            
            # 1. Obtener estudiantes activos del año anterior con su sección
            cursor.execute("""
                SELECT e.id, e.estatus_academico, s.nivel, s.grado, s.letra
                FROM estudiantes e
                JOIN seccion_estudiante se ON e.id = se.estudiante_id
                JOIN secciones s ON se.seccion_id = s.id
                WHERE s.año_escolar_id = %s AND e.estado = 1
            """, (anio_anterior_id,))
            estudiantes = cursor.fetchall()
            
            # 2. Mapa de progresión de grados
            # (Nivel, Grado Actual) -> (Nuevo Nivel, Nuevo Grado)
            # Nota: Ajustar según los nombres exactos en BD
            progression = {
                # Inicial / Preescolar
                ('Inicial', '1er nivel'): ('Inicial', '2do nivel'),
                ('Inicial', '2do nivel'): ('Inicial', '3er nivel'),
                ('Inicial', '3er nivel'): ('Primaria', '1ero'),
                
                # Primaria
                ('Primaria', '1ero'): ('Primaria', '2do'),
                ('Primaria', '2do'):  ('Primaria', '3ro'),
                ('Primaria', '3ro'):  ('Primaria', '4to'),
                ('Primaria', '4to'):  ('Primaria', '5to'),
                ('Primaria', '5to'):  ('Primaria', '6to'),
                ('Primaria', '6to'):  ('Egresado', 'Egresado'),
            }
            
            # Cache de nuevas secciones para no buscar mil veces
            # Key: (nivel, grado, letra) -> Value: seccion_id
            nuevas_secciones_cache = {}
            
            count_promovidos = 0
            count_egresados = 0
            
            for est in estudiantes:
                nivel_actual = est['nivel']
                grado_actual = est['grado']
                letra_actual = est['letra']
                
                # Normalizar keys si es necesario (el diccionario usa tuplas exactas)
                # Intento de búsqueda flexible
                target = None
                
                # Buscar en el mapa
                for key, val in progression.items():
                    # Comparación case-insensitive parcial o exacta
                    k_nivel, k_grado = key
                    if k_nivel.lower() in nivel_actual.lower() and k_grado.lower() == grado_actual.lower():
                        target = val
                        break
                
                # Si no está en el mapa, intentar lógica genérica o saltar
                if not target:
                    # Intento "1" -> "2", etc si son numéricos puros
                    # Pero tus grados son "1ero", "2do"... 
                    continue

                nuevo_nivel, nuevo_grado = target
                
                
                # Obtener el AÑO (número) del nuevo año escolar para la asignación
                cursor.execute("SELECT anio_inicio FROM anios_escolares WHERE id = %s", (nuevo_anio_id,))
                row_anio = cursor.fetchone()
                if not row_anio:
                     continue # Should not happen
                year_assign = row_anio['anio_inicio']


                if nuevo_nivel == 'Egresado':
                    # Marcar como egresado
                    cursor.execute("""
                        UPDATE estudiantes 
                        SET estatus_academico = 'Egresado'
                        WHERE id = %s
                    """, (est['id'],))
                    count_egresados += 1
                else:
                    # Buscar la sección destino en el nuevo año
                    cache_key = (nuevo_nivel, nuevo_grado, letra_actual)
                    if cache_key in nuevas_secciones_cache:
                        nueva_seccion_id = nuevas_secciones_cache[cache_key]
                    else:
                        cursor.execute("""
                            SELECT id FROM secciones
                            WHERE año_escolar_id = %s 
                              AND nivel = %s 
                              AND grado = %s 
                              AND letra = %s
                            LIMIT 1
                        """, (nuevo_anio_id, nuevo_nivel, nuevo_grado, letra_actual))
                        row = cursor.fetchone()
                        nueva_seccion_id = row['id'] if row else None
                        nuevas_secciones_cache[cache_key] = nueva_seccion_id
                    
                    if nueva_seccion_id:
                        # Asignar a la nueva sección USANDO EL AÑO CORRECTO
                        cursor.execute("""
                            INSERT INTO seccion_estudiante (estudiante_id, seccion_id, año_asignacion)
                            VALUES (%s, %s, %s)
                        """, (est['id'], nueva_seccion_id, year_assign))

                        # Registrar en Historial
                        cursor.execute("""
                            INSERT INTO historial_secciones (estudiante_id, seccion_id, año_inicio, fecha_asignacion)
                            VALUES (%s, %s, %s, CURDATE())
                            ON DUPLICATE KEY UPDATE 
                                seccion_id = VALUES(seccion_id),
                                fecha_asignacion = CURDATE()
                        """, (est['id'], nueva_seccion_id, year_assign))

                        count_promovidos += 1
                    else:
                        # No existe la sección destino (ej: pasaba de 6to A a 1er Año A pero no existe 1er Año)
                        # Se queda sin asignar o se maneja error. Por ahora solo log/skip.
                        pass

            conn.commit()
            return True, f"Promoción finalizada: {count_promovidos} promovidos, {count_egresados} egresados."

        except Exception as e:
            if conn: conn.rollback()
            return False, f"Error en promoción masiva: {e}"
        finally:
            if cursor: cursor.close()
            if conn: conn.close()