# models/estudiante_model.py
from utils.db import get_connection
from models.auditoria_model import AuditoriaModel
from models.anio_model import AnioEscolarModel
from datetime import datetime
from typing import Optional, Dict, List, Tuple


class EstudianteModel:
    """Modelo de estudiantes del sistema."""

    @staticmethod
    def generar_cedula_estudiantil(fecha_nac, cedula_madre: str) -> Optional[str]:
        """
        Genera cédula estudiantil única.
        Formato: {num_hijo}{año_nac}{cedula_madre}
        """
        # Validaciones de entrada
        if not fecha_nac or not cedula_madre:
            print("Error: fecha_nac o cedula_madre vacíos")
            return None
        
        if not isinstance(cedula_madre, str) or len(cedula_madre) < 6:
            print(f"Error: cedula_madre inválida: {cedula_madre}")
            return None
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return None
                
            cursor = conexion.cursor()

            # 1. Contar cuántos hijos tiene esta madre registrados
            cursor.execute(
                "SELECT COUNT(*) FROM estudiantes WHERE madre_ci = %s", 
                (cedula_madre,)
            )
            hijos_actuales = cursor.fetchone()[0]
            
            # 2. Extraer año de nacimiento (últimos 2 dígitos)
            anio = fecha_nac.year
            anio_dos = str(anio)[-2:]
            
            # 3. Determinar prefijo según número de hijo
            prefijo = "1"  # Por defecto es el primer hijo
            
            if hijos_actuales > 0:
                # Si ya tiene hijos, verificar cuántos nacieron el mismo año
                cursor.execute("""
                    SELECT COUNT(*) FROM estudiantes
                    WHERE madre_ci = %s AND YEAR(fecha_nac_est) = %s
                """, (cedula_madre, anio))
                mismos_anio = cursor.fetchone()[0]
                
                # El prefijo será: (hermanos del mismo año) + 1
                prefijo = str(mismos_anio + 1)
            
            # 4. Construir cédula final
            cedula_final = f"{prefijo}{anio_dos}{cedula_madre}"
            
            return cedula_final
            
        except Exception as e:
            print(f"Error generando cédula estudiantil: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def obtener_por_id(estudiante_id: int) -> Optional[Dict]:
        """Obtiene datos completos de un estudiante por su ID."""
        if not isinstance(estudiante_id, int) or estudiante_id <= 0:
            return None
            
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return None
                
            cursor = conexion.cursor(dictionary=True, buffered=True)
            
            # Query completa con LEFT JOIN para datos opcionales
            cursor.execute("""
                SELECT 
                    -- Datos básicos del estudiante
                    e.id, e.cedula, e.nombres, e.apellidos, e.fecha_nac_est, 
                    e.city, e.genero, e.direccion, e.fecha_ingreso, e.docente, 
                    e.tallaC, e.tallaP, e.tallaZ,
                    
                    -- Datos de padres
                    e.padre, e.padre_ci, e.ocupacion_padre, 
                    e.madre, e.madre_ci, e.ocupacion_madre,
                    
                    -- Estado académico y retiro
                    e.representante_id, e.estado, e.estatus_academico,
                    e.motivo_retiro, e.fecha_retiro,
                    
                    -- Sección actual (puede ser NULL si no tiene asignación)
                    COALESCE(s.nivel, 'Sin asignar') AS tipo_educacion,
                    COALESCE(s.grado, 'Sin asignar') AS grado,
                    COALESCE(s.letra, 'Sin asignar') AS seccion,
                    se.seccion_id, se.año_asignacion,
                    
                    -- Docente asignado a la sección
                    COALESCE(CONCAT(emp.nombres, ' ', emp.apellidos), 'Sin docente asignado') AS docente_seccion,
                    
                    -- Para egresados: último grado cursado
                    (SELECT CONCAT(sh.grado, ' ', sh.letra)
                     FROM historial_secciones hs
                     JOIN secciones sh ON hs.seccion_id = sh.id
                     WHERE hs.estudiante_id = e.id
                     ORDER BY hs.año_inicio DESC
                     LIMIT 1) AS ultimo_grado,
                    
                    -- Para egresados: año de egreso (formato YYYY/YYYY)
                    (SELECT CONCAT(hs.año_inicio, '/', hs.año_inicio + 1)
                     FROM historial_secciones hs
                     WHERE hs.estudiante_id = e.id
                     ORDER BY hs.año_inicio DESC
                     LIMIT 1) AS año_egreso
                     
                FROM estudiantes e
                LEFT JOIN seccion_estudiante se ON e.id = se.estudiante_id
                LEFT JOIN secciones s ON se.seccion_id = s.id
                LEFT JOIN empleados emp ON s.docente_id = emp.id
                WHERE e.id = %s
                ORDER BY se.año_asignacion DESC
                LIMIT 1
            """, (estudiante_id,))
            
            return cursor.fetchone()
            
        except Exception as e:
            print(f"Error obteniendo estudiante por ID: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def guardar(
        estudiante_data: dict, 
        representante_data: dict, 
        usuario_actual: dict, 
        seccion_id: int = None
    ) -> Tuple[bool, str]:
        """Registra un nuevo estudiante con su representante."""
        # Validaciones básicas
        if not estudiante_data.get("cedula") or not estudiante_data.get("nombres"):
            return False, "Faltan datos obligatorios del estudiante"
        
        if not representante_data.get("cedula_repre"):
            return False, "Falta cédula del representante"
        
        if not usuario_actual or 'id' not in usuario_actual:
            return False, "Usuario inválido"
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a BD"
                
            cursor = conexion.cursor(dictionary=True)
            conexion.start_transaction()  # Iniciar transacción explícita

            # 1. BUSCAR O CREAR REPRESENTANTE
            # Verificar si ya existe por cédula
            cursor.execute(
                "SELECT id FROM representantes WHERE cedula_repre = %s", 
                (representante_data["cedula_repre"],)
            )
            row = cursor.fetchone()
            
            if row:
                # Representante ya existe, reutilizar su ID
                representante_id = row["id"]
            else:
                # Crear nuevo representante
                sql_repre = """
                    INSERT INTO representantes (
                        cedula_repre, nombres_repre, apellidos_repre, fecha_nac_repre,
                        genero_repre, direccion_repre, num_contact_repre, correo_repre, observacion
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                valores_repre = (
                    representante_data["cedula_repre"],
                    representante_data["nombres_repre"],
                    representante_data["apellidos_repre"],
                    representante_data["fecha_nac_repre"],
                    representante_data["genero_repre"],
                    representante_data["direccion_repre"],
                    representante_data["num_contact_repre"],
                    representante_data["correo_repre"],
                    representante_data["observacion"],
                )
                cursor.execute(sql_repre, valores_repre)
                representante_id = cursor.lastrowid

            # 2. INSERTAR ESTUDIANTE
            # Nota: NO insertamos tipo_educacion, grado, seccion (esos están en seccion_estudiante)
            sql_estu = """
                INSERT INTO estudiantes (
                    cedula, apellidos, nombres, fecha_nac_est, city, genero, 
                    direccion, fecha_ingreso, docente, tallaC, tallaP, tallaZ, 
                    madre, madre_ci, ocupacion_madre, 
                    padre, padre_ci, ocupacion_padre, 
                    representante_id
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, %s, %s
                )
            """
            valores_estu = (
                estudiante_data["cedula"],
                estudiante_data["apellidos"],
                estudiante_data["nombres"],
                estudiante_data["fecha_nac_est"],
                estudiante_data["city"],
                estudiante_data["genero"],
                estudiante_data["direccion"],
                estudiante_data["fecha_ingreso"],
                estudiante_data["docente"],
                estudiante_data["tallaC"],
                estudiante_data["tallaP"],
                estudiante_data["tallaZ"],
                estudiante_data["madre"],
                estudiante_data["madre_ci"],
                estudiante_data["ocupacion_madre"],
                estudiante_data["padre"],
                estudiante_data["padre_ci"],
                estudiante_data["ocupacion_padre"],
                representante_id
            )
            cursor.execute(sql_estu, valores_estu)
            estudiante_id = cursor.lastrowid

            # 3. ASIGNAR A SECCIÓN (si se especificó)
            if seccion_id:
                # Obtener año actual del sistema
                anio_info = AnioEscolarModel.obtener_actual()
                if not anio_info:
                    conexion.rollback()
                    return False, "No hay año escolar activo"
                
                año_actual = anio_info['anio_inicio']
                
                # Insertar en tabla intermedia
                cursor.execute("""
                    INSERT INTO seccion_estudiante (estudiante_id, seccion_id, año_asignacion)
                    VALUES (%s, %s, %s)
                """, (estudiante_id, seccion_id, año_actual))
                
                # Registrar en historial
                cursor.execute("""
                    INSERT INTO historial_secciones (estudiante_id, seccion_id, año_inicio, fecha_asignacion)
                    VALUES (%s, %s, %s, CURDATE())
                """, (estudiante_id, seccion_id, año_actual))

            # 4. COMMIT DE LA TRANSACCIÓN
            conexion.commit()

            # 5. AUDITORÍA (fuera de la transacción para no bloquear)
            AuditoriaModel.registrar(
                usuario_id=usuario_actual["id"],
                accion="INSERT",
                entidad="estudiantes",
                entidad_id=estudiante_id,
                referencia=estudiante_data["cedula"],
                descripcion=f"Nuevo estudiante: {estudiante_data['nombres']} {estudiante_data['apellidos']}"
            )

            return True, "Estudiante registrado correctamente."

        except Exception as e:
            if conexion:
                conexion.rollback()
            print(f"Error en guardar estudiante: {e}")
            return False, f"Error al guardar: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def actualizar(
        estudiante_id: int, 
        data: dict, 
        usuario_actual: dict, 
        seccion_id: int = None
    ) -> Tuple[bool, str]:
        """Actualiza datos de un estudiante existente."""
        # Validaciones
        if not isinstance(estudiante_id, int) or estudiante_id <= 0:
            return False, "ID de estudiante inválido"
        
        if not usuario_actual or 'id' not in usuario_actual:
            return False, "Usuario inválido"
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión"
                
            cursor = conexion.cursor(dictionary=True)
            conexion.start_transaction()

            # 1. OBTENER DATOS ACTUALES (para comparar cambios)
            cursor.execute("SELECT * FROM estudiantes WHERE id = %s", (estudiante_id,))
            estudiante_actual = cursor.fetchone()
            
            if not estudiante_actual:
                conexion.rollback()
                return False, "Estudiante no encontrado"

            # 2. DETECTAR CAMBIOS EN CAMPOS BÁSICOS
            cambios = []
            campos_actualizables = [
                "nombres", "apellidos", "fecha_nac_est", "city", "genero", 
                "direccion", "fecha_ingreso", "docente", "tallaC", "tallaP", 
                "tallaZ", "padre", "padre_ci", "ocupacion_padre", 
                "madre", "madre_ci", "ocupacion_madre"
            ]
            
            for campo in campos_actualizables:
                if campo in data:
                    nuevo_valor = data[campo]
                    valor_actual = estudiante_actual.get(campo)
                    
                    # Comparar valores (convertir a string para evitar errores de tipo)
                    if str(valor_actual) != str(nuevo_valor):
                        cambios.append(f"{campo}: '{valor_actual}' → '{nuevo_valor}'")

            # 3. EJECUTAR UPDATE DE CAMPOS BÁSICOS
            if cambios:  # Solo actualizar si hay cambios
                cursor.execute("""
                    UPDATE estudiantes
                    SET nombres = %s, apellidos = %s, fecha_nac_est = %s, 
                        city = %s, genero = %s, direccion = %s, 
                        fecha_ingreso = %s, docente = %s,
                        tallaC = %s, tallaP = %s, tallaZ = %s, 
                        padre = %s, padre_ci = %s, ocupacion_padre = %s, 
                        madre = %s, madre_ci = %s, ocupacion_madre = %s
                    WHERE id = %s
                """, (
                    data.get("nombres"),
                    data.get("apellidos"),
                    data.get("fecha_nac_est"),
                    data.get("city"),
                    data.get("genero"),
                    data.get("direccion"),
                    data.get("fecha_ingreso"),
                    data.get("docente"),
                    data.get("tallaC"),
                    data.get("tallaP"),
                    data.get("tallaZ"),
                    data.get("padre"),
                    data.get("padre_ci"),
                    data.get("ocupacion_padre"),
                    data.get("madre"),
                    data.get("madre_ci"),
                    data.get("ocupacion_madre"),
                    estudiante_id
                ))

            # 4. MANEJO DE CAMBIO DE SECCIÓN
            # Determinar el ID final de sección (puede venir explícito o deducirse de data)
            final_seccion_id = seccion_id
            
            # Obtener año actual
            anio_info = AnioEscolarModel.obtener_actual()
            if not anio_info:
                conexion.rollback()
                return False, "No hay año escolar activo"
            
            anio_id = anio_info['id']
            anio_num = anio_info['anio_inicio']
            
            # Si no viene seccion_id pero vienen tipo_educacion, grado, seccion en data
            # intentar resolver el ID de la sección
            if not final_seccion_id and all(k in data for k in ["tipo_educacion", "grado", "seccion"]):
                nivel = data["tipo_educacion"]
                grado = data["grado"]
                letra = data["seccion"]
                
                # Solo buscar si no es "Sin asignar"
                if nivel != "Sin asignar" and grado != "Sin asignar" and letra != "Sin asignar":
                    cursor.execute("""
                        SELECT id FROM secciones 
                        WHERE nivel = %s AND grado = %s AND letra = %s 
                          AND año_escolar_id = %s
                        LIMIT 1
                    """, (nivel, grado, letra, anio_id))
                    
                    row = cursor.fetchone()
                    if row:
                        final_seccion_id = row['id']

            # Si tenemos un ID de sección válido, proceder con la asignación
            if final_seccion_id:
                # 4.1. Eliminar asignaciones previas del año actual
                cursor.execute("""
                    DELETE FROM seccion_estudiante 
                    WHERE estudiante_id = %s AND año_asignacion = %s
                """, (estudiante_id, anio_num))
                
                # 4.2. Insertar nueva asignación
                cursor.execute("""
                    INSERT INTO seccion_estudiante (estudiante_id, seccion_id, año_asignacion)
                    VALUES (%s, %s, %s)
                """, (estudiante_id, final_seccion_id, anio_num))
                
                # 4.3. Actualizar historial (idempotente por año)
                cursor.execute("""
                    INSERT INTO historial_secciones (estudiante_id, seccion_id, año_inicio, fecha_asignacion)
                    VALUES (%s, %s, %s, CURDATE())
                    ON DUPLICATE KEY UPDATE 
                        seccion_id = VALUES(seccion_id),
                        fecha_asignacion = CURDATE()
                """, (estudiante_id, final_seccion_id, anio_num))
                
                cambios.append(f"Asignado a sección ID {final_seccion_id} (año {anio_num})")

            # 5. COMMIT DE LA TRANSACCIÓN
            conexion.commit()

            # 6. AUDITORÍA (si hubo cambios)
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

        except Exception as e:
            if conexion:
                conexion.rollback()
            print(f"Error actualizando estudiante: {e}")
            return False, f"Error al actualizar: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def eliminar(estudiante_id: int, usuario_actual: dict) -> Tuple[bool, str]:
        """Elimina un estudiante y sus relaciones."""
        # Validaciones
        if not isinstance(estudiante_id, int) or estudiante_id <= 0:
            return False, "ID inválido"
        
        if not usuario_actual or 'id' not in usuario_actual:
            return False, "Usuario inválido"
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión"
                
            cursor = conexion.cursor(dictionary=True)
            conexion.start_transaction()

            # 1. OBTENER DATOS DEL ESTUDIANTE
            cursor.execute("SELECT * FROM estudiantes WHERE id = %s", (estudiante_id,))
            estudiante = cursor.fetchone()
            
            if not estudiante:
                conexion.rollback()
                return False, "Estudiante no encontrado"

            id_representante = estudiante["representante_id"]

            # 2. CONTAR HIJOS DEL REPRESENTANTE
            cursor.execute(
                "SELECT COUNT(*) as total FROM estudiantes WHERE representante_id = %s", 
                (id_representante,)
            )
            hijos_count = cursor.fetchone()["total"]

            # 3. OBTENER INFO DE SECCIÓN PARA AUDITORÍA
            cursor.execute("""
                SELECT 
                    COALESCE(s.grado, '-') AS grado, 
                    COALESCE(s.letra, '-') AS seccion
                FROM estudiantes e
                LEFT JOIN seccion_estudiante se ON e.id = se.estudiante_id
                LEFT JOIN secciones s ON se.seccion_id = s.id
                WHERE e.id = %s
                LIMIT 1
            """, (estudiante_id,))
            seccion_info = cursor.fetchone()

            # 4. AUDITORÍA (antes de eliminar)
            descripcion = (
                f"Eliminado: {estudiante['nombres']} {estudiante['apellidos']} "
                f"(Grado: {seccion_info['grado']}, Sección: {seccion_info['seccion']})"
            )
            
            AuditoriaModel.registrar(
                usuario_id=usuario_actual["id"],
                accion="DELETE",
                entidad="estudiantes",
                entidad_id=estudiante_id,
                referencia=estudiante["cedula"],
                descripcion=descripcion
            )

            # 5. ELIMINAR RELACIONES (seccion_estudiante, historial)
            cursor.execute(
                "DELETE FROM seccion_estudiante WHERE estudiante_id = %s", 
                (estudiante_id,)
            )
            cursor.execute(
                "DELETE FROM historial_secciones WHERE estudiante_id = %s",
                (estudiante_id,)
            )

            # 6. ELIMINAR ESTUDIANTE
            cursor.execute("DELETE FROM estudiantes WHERE id = %s", (estudiante_id,))

            # 7. ELIMINAR REPRESENTANTE SI ERA EL ÚNICO HIJO
            if hijos_count == 1:
                cursor.execute("DELETE FROM representantes WHERE id = %s", (id_representante,))

            # 8. COMMIT
            conexion.commit()
            
            return True, "Estudiante eliminado correctamente."

        except Exception as e:
            if conexion:
                conexion.rollback()
            print(f"Error eliminando estudiante: {e}")
            return False, f"Error al eliminar: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def listar(anio_escolar_id: int = None) -> List[Dict]:
        """Lista estudiantes regulares del año escolar especificado (None = actual)."""
        conexion = None
        cursor = None
        try:
            # Si no se especifica año, obtener el actual
            if anio_escolar_id is None:
                anio_actual = AnioEscolarModel.obtener_actual()
                anio_escolar_id = anio_actual['id'] if anio_actual else None
                
                if not anio_escolar_id:
                    return []  # No hay año activo
            
            conexion = get_connection()
            if not conexion:
                return []
            
            cursor = conexion.cursor(dictionary=True)

            # 1. Obtener el año numérico (para filtrar asignaciones)
            cursor.execute(
                "SELECT anio_inicio FROM anios_escolares WHERE id = %s", 
                (anio_escolar_id,)
            )
            row_anio = cursor.fetchone()
            
            if not row_anio:
                return []
            
            target_year = row_anio['anio_inicio']

            # 2. Listar estudiantes con asignación en ese año
            cursor.execute("""
                SELECT 
                    e.id,
                    e.cedula,
                    e.nombres,
                    e.apellidos,
                    e.fecha_nac_est,
                    TIMESTAMPDIFF(YEAR, e.fecha_nac_est, CURDATE()) AS edad,
                    e.city,
                    e.genero,
                    e.direccion,
                    COALESCE(CONCAT(emp.nombres, ' ', emp.apellidos), 'Sin asignar') AS docente,
                    e.tallaC,
                    e.tallaP,
                    e.tallaZ,
                    e.fecha_ingreso,
                    
                    -- Sección actual (puede ser NULL)
                    COALESCE(s.nivel, 'Sin asignar') AS tipo_educacion,
                    COALESCE(s.grado, 'Sin asignar') AS grado,
                    COALESCE(s.letra, 'Sin asignar') AS seccion,
                    
                    e.estatus_academico,
                    CASE WHEN e.estado = 1 THEN 'Activo' ELSE 'Inactivo' END AS estado
                    
                FROM estudiantes e
                LEFT JOIN seccion_estudiante se 
                    ON e.id = se.estudiante_id AND se.año_asignacion = %s
                LEFT JOIN secciones s 
                    ON se.seccion_id = s.id AND s.año_escolar_id = %s
                LEFT JOIN empleados emp ON s.docente_id = emp.id
                WHERE e.estatus_academico = 'Regular'
                ORDER BY e.apellidos, e.nombres
            """, (target_year, anio_escolar_id))

            return cursor.fetchall()
            
        except Exception as e:
            print(f"Error listando estudiantes: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
    
    @staticmethod
    def listar_activos() -> List[Dict]:
        """Lista todos los estudiantes activos del sistema."""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return []
                
            cursor = conexion.cursor(dictionary=True)
            
            cursor.execute("""
                SELECT 
                    e.id, e.cedula, e.nombres, e.apellidos, e.fecha_nac_est,
                    TIMESTAMPDIFF(YEAR, e.fecha_nac_est, CURDATE()) AS edad,
                    e.city, e.genero, e.direccion, e.fecha_ingreso,
                    
                    -- Sección (última asignación)
                    COALESCE(s.nivel, 'Sin asignar') AS tipo_educacion,
                    COALESCE(s.grado, 'Sin asignar') AS grado,
                    COALESCE(s.letra, 'Sin asignar') AS seccion,
                    
                    e.docente, e.tallaC, e.tallaP, e.tallaZ, 
                    e.padre, e.padre_ci, e.ocupacion_padre, 
                    e.madre, e.madre_ci, e.ocupacion_madre,
                    e.estatus_academico,
                    CASE WHEN e.estado = 1 THEN 'Activo' ELSE 'Inactivo' END AS estado,
                    
                    -- Datos del representante
                    r.cedula_repre, r.nombres_repre, r.apellidos_repre,
                    r.num_contact_repre, r.observacion
                    
                FROM estudiantes e
                LEFT JOIN seccion_estudiante se ON e.id = se.estudiante_id
                LEFT JOIN secciones s ON se.seccion_id = s.id
                JOIN representantes r ON e.representante_id = r.id
                WHERE e.estado = 1
                ORDER BY e.apellidos, e.nombres
            """)
            
            return cursor.fetchall()
            
        except Exception as e:
            print(f"Error listando activos: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def obtener_secciones_activas(año: int) -> List[Dict]:
        """Obtiene todas las secciones activas de un año escolar."""
        if not isinstance(año, int) or año < 2000:
            return []
            
        conn = get_connection()
        if not conn:
            return []
            
        try:
            cursor = conn.cursor(dictionary=True)
            
            # Obtener secciones del año especificado
            cursor.execute("""
                SELECT s.id, s.nivel, s.grado, s.letra
                FROM secciones s
                INNER JOIN anios_escolares a ON s.año_escolar_id = a.id
                WHERE a.anio_inicio = %s AND s.activo = 1
                ORDER BY 
                    -- Ordenar por nivel (Inicial primero, luego Primaria)
                    FIELD(s.nivel, 'Inicial', 'Primaria'),
                    s.grado, 
                    s.letra
            """, (año,))
            
            resultado = cursor.fetchall()
            return resultado
            
        except Exception as e:
            print(f"Error cargando secciones: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def asignar_a_seccion(
        estudiante_id: int, 
        seccion_id: int, 
        año_actual: int
    ) -> bool:
        """Asigna un estudiante a una sección específica."""
        # Validaciones
        if not all(isinstance(x, int) and x > 0 for x in [estudiante_id, seccion_id, año_actual]):
            return False
        
        conn = get_connection()
        if not conn:
            return False
            
        cursor = None
        try:
            cursor = conn.cursor()
            conn.start_transaction()
            
            # 1. Eliminar asignaciones previas del año actual
            cursor.execute("""
                DELETE FROM seccion_estudiante 
                WHERE estudiante_id = %s AND año_asignacion = %s
            """, (estudiante_id, año_actual))
            
            # 2. Insertar nueva asignación
            cursor.execute("""
                INSERT INTO seccion_estudiante (estudiante_id, seccion_id, año_asignacion)
                VALUES (%s, %s, %s)
            """, (estudiante_id, seccion_id, año_actual))

            # 3. Actualizar historial (idempotente)
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
    def listar_por_seccion(
        seccion_id: int, 
        año: int = None, 
        incluir_inactivos: bool = False
    ) -> List[Dict]:
        """Lista estudiantes asignados a una sección específica."""
        if not isinstance(seccion_id, int) or seccion_id <= 0:
            return []
            
        conn = get_connection()
        if not conn:
            return []
            
        try:
            # Si no se especifica año, usar el actual
            if año is None:
                año = datetime.now().year
            
            cursor = conn.cursor(dictionary=True)
            
            # Query base
            sql = """
                SELECT 
                    e.id, 
                    e.cedula, 
                    e.nombres, 
                    e.apellidos,
                    TIMESTAMPDIFF(YEAR, e.fecha_nac_est, CURDATE()) AS edad,
                    e.genero,
                    CASE WHEN e.estado = 1 THEN 'Activo' ELSE 'Inactivo' END AS estado,
                    se.seccion_id
                FROM seccion_estudiante se
                JOIN estudiantes e ON e.id = se.estudiante_id
                WHERE se.seccion_id = %s AND se.año_asignacion = %s
            """
            
            # Filtrar inactivos si es necesario
            if not incluir_inactivos:
                sql += " AND e.estado = 1"
            
            sql += " ORDER BY e.apellidos, e.nombres"
            
            cursor.execute(sql, (seccion_id, año))
            filas = cursor.fetchall()
            
            return filas
            
        except Exception as e:
            print(f"Error en listar_por_seccion: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def promover_masivo(
        anio_anterior_id: int, 
        nuevo_anio_id: int
    ) -> Tuple[bool, str]:
        """Promoción masiva de estudiantes al aperturar nuevo año escolar."""
        # Validaciones
        if not all(isinstance(x, int) and x > 0 for x in [anio_anterior_id, nuevo_anio_id]):
            return False, "IDs de años inválidos"
        
        conn = get_connection()
        if not conn:
            return False, "Error de conexión"
        
        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            conn.start_transaction()
            
            # 1. OBTENER ESTUDIANTES ACTIVOS DEL AÑO ANTERIOR
            cursor.execute("""
                SELECT 
                    e.id, 
                    e.estatus_academico, 
                    s.nivel, 
                    s.grado, 
                    s.letra
                FROM estudiantes e
                JOIN seccion_estudiante se ON e.id = se.estudiante_id
                JOIN secciones s ON se.seccion_id = s.id
                WHERE s.año_escolar_id = %s 
                  AND e.estado = 1
                  AND e.estatus_academico = 'Regular'
                ORDER BY s.nivel, s.grado, s.letra
            """, (anio_anterior_id,))
            
            estudiantes = cursor.fetchall()
            
            if not estudiantes:
                conn.rollback()
                return True, "No hay estudiantes para promover"
            
            # 2. TABLA DE PROGRESIÓN DE GRADOS
            # Mapea (nivel_actual, grado_actual) → (nuevo_nivel, nuevo_grado)
            # IMPORTANTE: Los nombres deben coincidir con SeccionesModel.GRADOS_INICIAL y GRADOS_PRIMARIA
            progression = {
                # Educación Inicial
                ('Inicial', '1er Nivel'): ('Inicial', '2do Nivel'),
                ('Inicial', '2do Nivel'): ('Inicial', '3er Nivel'),
                ('Inicial', '3er Nivel'): ('Primaria', '1ero'),
                
                # Educación Primaria
                ('Primaria', '1ero'): ('Primaria', '2do'),
                ('Primaria', '2do'):  ('Primaria', '3ero'),
                ('Primaria', '3ero'): ('Primaria', '4to'),
                ('Primaria', '4to'):  ('Primaria', '5to'),
                ('Primaria', '5to'):  ('Primaria', '6to'),
                ('Primaria', '6to'):  ('Egresado', 'Egresado'),  # Marca especial
            }
            
            # 3. OBTENER AÑO NUMÉRICO DEL NUEVO AÑO ESCOLAR
            cursor.execute(
                "SELECT anio_inicio FROM anios_escolares WHERE id = %s", 
                (nuevo_anio_id,)
            )
            row_anio = cursor.fetchone()
            
            if not row_anio:
                conn.rollback()
                return False, "Año escolar destino no encontrado"
            
            year_assign = row_anio['anio_inicio']

            # 4. CACHE DE SECCIONES DEL NUEVO AÑO
            # Para evitar consultas repetidas
            # Key: (nivel, grado, letra) → Value: seccion_id
            nuevas_secciones_cache = {}
            
            # Contadores de resultados
            count_promovidos = 0
            count_egresados = 0
            count_sin_seccion = 0
            
            # 5. PROCESAR CADA ESTUDIANTE
            for est in estudiantes:
                nivel_actual = est['nivel']
                grado_actual = est['grado']
                letra_actual = est['letra']
                
                # 5.1. Buscar progresión en la tabla
                # Intentar match exacto primero
                target = progression.get((nivel_actual, grado_actual))
                
                # Si no hay match exacto, intentar match parcial (case-insensitive)
                if not target:
                    for key, val in progression.items():
                        k_nivel, k_grado = key
                        # Comparación flexible
                        if (k_nivel.lower() == nivel_actual.lower() and 
                            k_grado.lower() == grado_actual.lower()):
                            target = val
                            break
                
                # Si no se encuentra progresión, saltar estudiante
                if not target:
                    print(f"⚠️ Sin progresión definida para: {nivel_actual} {grado_actual}")
                    count_sin_seccion += 1
                    continue

                nuevo_nivel, nuevo_grado = target
                
                # 5.2. CASO ESPECIAL: EGRESADOS
                if nuevo_nivel == 'Egresado':
                    cursor.execute("""
                        UPDATE estudiantes 
                        SET estatus_academico = 'Egresado'
                        WHERE id = %s
                    """, (est['id'],))
                    count_egresados += 1
                    continue
                
                # 5.3. BUSCAR SECCIÓN DESTINO EN NUEVO AÑO
                cache_key = (nuevo_nivel, nuevo_grado, letra_actual)
                
                if cache_key in nuevas_secciones_cache:
                    nueva_seccion_id = nuevas_secciones_cache[cache_key]
                else:
                    # Buscar en BD
                    cursor.execute("""
                        SELECT id FROM secciones
                        WHERE año_escolar_id = %s 
                          AND nivel = %s 
                          AND grado = %s 
                          AND letra = %s
                          AND activo = 1
                        LIMIT 1
                    """, (nuevo_anio_id, nuevo_nivel, nuevo_grado, letra_actual))
                    
                    row = cursor.fetchone()
                    nueva_seccion_id = row['id'] if row else None
                    nuevas_secciones_cache[cache_key] = nueva_seccion_id
                
                # 5.4. ASIGNAR A NUEVA SECCIÓN
                if nueva_seccion_id:
                    # Insertar en seccion_estudiante
                    cursor.execute("""
                        INSERT INTO seccion_estudiante (estudiante_id, seccion_id, año_asignacion)
                        VALUES (%s, %s, %s)
                    """, (est['id'], nueva_seccion_id, year_assign))

                    # Actualizar historial
                    cursor.execute("""
                        INSERT INTO historial_secciones (estudiante_id, seccion_id, año_inicio, fecha_asignacion)
                        VALUES (%s, %s, %s, CURDATE())
                        ON DUPLICATE KEY UPDATE 
                            seccion_id = VALUES(seccion_id),
                            fecha_asignacion = CURDATE()
                    """, (est['id'], nueva_seccion_id, year_assign))

                    count_promovidos += 1
                else:
                    # La sección destino no existe (ej: falta crear 2do A)
                    print(f"⚠️ Sección no encontrada: {nuevo_nivel} {nuevo_grado} {letra_actual}")
                    count_sin_seccion += 1

            # 6. COMMIT DE TODA LA TRANSACCIÓN
            conn.commit()
            
            # 7. CONSTRUIR MENSAJE DE RESULTADO
            mensaje = f"Promoción completada: {count_promovidos} promovidos"
            
            if count_egresados > 0:
                mensaje += f", {count_egresados} egresados"
            
            if count_sin_seccion > 0:
                mensaje += f" ({count_sin_seccion} sin sección destino)"
            
            return True, mensaje

        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Error en promoción masiva: {e}")
            return False, f"Error en promoción: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    @staticmethod
    def listar_egresados() -> List[Dict]:
        """Lista todos los estudiantes egresados del sistema."""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return []
                
            cursor = conexion.cursor(dictionary=True)

            cursor.execute("""
                SELECT 
                    e.id, 
                    e.cedula, 
                    e.nombres, 
                    e.apellidos, 
                    e.fecha_nac_est,
                    TIMESTAMPDIFF(YEAR, e.fecha_nac_est, CURDATE()) AS edad,
                    e.city, 
                    e.genero, 
                    e.direccion,
                    
                    -- Último grado cursado (desde historial)
                    (SELECT CONCAT(s.grado, ' ', s.letra)
                     FROM historial_secciones hs
                     JOIN secciones s ON hs.seccion_id = s.id
                     WHERE hs.estudiante_id = e.id
                     ORDER BY hs.año_inicio DESC
                     LIMIT 1) AS ultimo_grado,
                    
                    -- Última sección
                    (SELECT s.letra
                     FROM historial_secciones hs
                     JOIN secciones s ON hs.seccion_id = s.id
                     WHERE hs.estudiante_id = e.id
                     ORDER BY hs.año_inicio DESC
                     LIMIT 1) AS ultima_seccion,
                    
                    -- Año de egreso (formato YYYY/YYYY)
                    (SELECT CONCAT(hs.año_inicio, '/', hs.año_inicio + 1)
                     FROM historial_secciones hs
                     WHERE hs.estudiante_id = e.id
                     ORDER BY hs.año_inicio DESC
                     LIMIT 1) AS fecha_egreso
                     
                FROM estudiantes e
                WHERE e.estatus_academico = 'Egresado'
                ORDER BY e.apellidos, e.nombres
            """)

            return cursor.fetchall()
            
        except Exception as e:
            print(f"Error listando egresados: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def devolver_estudiante(
        estudiante_id: int, 
        seccion_destino_id: int, 
        año_actual: int, 
        usuario_actual: dict
    ) -> Tuple[bool, str]:
        """
        DEVUELVE un estudiante a un grado anterior (repitencia).
        """
        # Validaciones
        if not all(isinstance(x, int) and x > 0 for x in [estudiante_id, seccion_destino_id, año_actual]):
            return False, "Parámetros inválidos"
        
        if not usuario_actual or 'id' not in usuario_actual:
            return False, "Usuario inválido"
        
        conn = get_connection()
        if not conn:
            return False, "Error de conexión"
        
        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            conn.start_transaction()
            
            # 1. OBTENER DATOS DEL ESTUDIANTE Y ASIGNACIÓN ACTUAL
            cursor.execute("""
                SELECT 
                    e.cedula, 
                    e.nombres, 
                    e.apellidos,
                    s_actual.nivel AS nivel_actual, 
                    s_actual.grado AS grado_actual,
                    s_actual.letra AS letra_actual,
                    se.seccion_id AS seccion_actual_id
                FROM estudiantes e
                LEFT JOIN seccion_estudiante se 
                    ON e.id = se.estudiante_id AND se.año_asignacion = %s
                LEFT JOIN secciones s_actual ON se.seccion_id = s_actual.id
                WHERE e.id = %s
            """, (año_actual, estudiante_id))
            
            estudiante = cursor.fetchone()
            
            if not estudiante:
                conn.rollback()
                return False, "Estudiante no encontrado"
            
            # 2. OBTENER DATOS DE LA SECCIÓN DESTINO
            cursor.execute("""
                SELECT nivel, grado, letra 
                FROM secciones 
                WHERE id = %s
            """, (seccion_destino_id,))
            
            seccion_destino = cursor.fetchone()
            
            if not seccion_destino:
                conn.rollback()
                return False, "Sección destino no encontrada"
            
            # 3. VALIDACIÓN OPCIONAL: verificar que es un grado igual o anterior
            # (puedes comentar esto si quieres permitir cualquier movimiento)
            # Por ahora, solo verificamos que exista la sección
            
            # 4. ELIMINAR ASIGNACIÓN ACTUAL DEL AÑO
            if estudiante['seccion_actual_id']:
                cursor.execute("""
                    DELETE FROM seccion_estudiante 
                    WHERE estudiante_id = %s AND año_asignacion = %s
                """, (estudiante_id, año_actual))
            
            # 5. ASIGNAR A SECCIÓN DE REPITENCIA
            cursor.execute("""
                INSERT INTO seccion_estudiante (estudiante_id, seccion_id, año_asignacion)
                VALUES (%s, %s, %s)
            """, (estudiante_id, seccion_destino_id, año_actual))
            
            # 6. ACTUALIZAR HISTORIAL
            # IMPORTANTE: Esto permite tener 2+ registros del mismo grado (repitencia)
            cursor.execute("""
                INSERT INTO historial_secciones 
                    (estudiante_id, seccion_id, año_inicio, fecha_asignacion)
                VALUES (%s, %s, %s, CURDATE())
                ON DUPLICATE KEY UPDATE 
                    seccion_id = VALUES(seccion_id),
                    fecha_asignacion = CURDATE()
            """, (estudiante_id, seccion_destino_id, año_actual))
            
            # 7. COMMIT
            conn.commit()
            
            # 8. AUDITORÍA
            descripcion = (
                f"Estudiante devuelto de {estudiante['grado_actual']} {estudiante['letra_actual']} "
                f"a {seccion_destino['grado']} {seccion_destino['letra']} "
                f"(Repitencia año {año_actual})"
            )
            
            AuditoriaModel.registrar(
                usuario_id=usuario_actual["id"],
                accion="UPDATE",
                entidad="estudiantes",
                entidad_id=estudiante_id,
                referencia=estudiante["cedula"],
                descripcion=descripcion
            )
            
            mensaje = (
                f"Estudiante {estudiante['nombres']} {estudiante['apellidos']} "
                f"devuelto a {seccion_destino['grado']} {seccion_destino['letra']}"
            )
            return True, mensaje
            
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Error al devolver estudiante: {e}")
            return False, f"Error: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    @staticmethod
    def obtener_historial_estudiante(estudiante_id: int) -> List[Dict]:
        """Obtiene el historial académico completo de un estudiante."""
        if not isinstance(estudiante_id, int) or estudiante_id <= 0:
            return []
            
        conn = get_connection()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor(dictionary=True)
            
            cursor.execute("""
                SELECT 
                    hs.año_inicio,
                    s.nivel,
                    s.grado,
                    s.letra,
                    hs.fecha_asignacion,
                    CONCAT(hs.año_inicio, '/', hs.año_inicio + 1) AS año_escolar,
                    COALESCE(CONCAT(e.nombres, ' ', e.apellidos), 'Sin docente') AS docente
                FROM historial_secciones hs
                JOIN secciones s ON hs.seccion_id = s.id
                LEFT JOIN empleados e ON s.docente_id = e.id
                WHERE hs.estudiante_id = %s
                ORDER BY hs.año_inicio DESC
            """, (estudiante_id,))
            
            resultado = cursor.fetchall()
            return resultado
            
        except Exception as e:
            print(f"Error obteniendo historial: {e}")
            return []
        finally:
            cursor.close()
            conn.close()