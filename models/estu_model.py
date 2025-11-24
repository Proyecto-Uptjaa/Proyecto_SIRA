# models/estudiante_model.py
from utils.db import get_connection
from models.auditoria_model import AuditoriaModel

class EstudianteModel:
    """Modelo de estudiantes con conexión bajo demanda."""
    tipos_de_educacion = {"Inicial": ["1er nivel", "2do nivel", "3er nivel"],
                              "Primaria": ["1ero", "2do", "3ro", "4to", "5to", "6to"]}

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
    def guardar(estudiante_data: dict, representante_data: dict, usuario_actual: dict):
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor(dictionary=True)

            # 1. Insertar o recuperar representante (sin auditoría)
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

            # 2. Insertar estudiante
            sql_estu = """
                INSERT INTO estudiantes (cedula, apellidos, nombres, fecha_nac_est, city, genero, direccion,
                                        tipo_educacion, grado, seccion, docente, tallaC, tallaP, tallaZ, madre, madre_ci,
                                        ocupacion_madre, padre, padre_ci, ocupacion_padre, representante_id)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            valores_estu = (
                estudiante_data["cedula"], estudiante_data["apellidos"], estudiante_data["nombres"], estudiante_data["fecha_nac_est"],
                estudiante_data["city"], estudiante_data["genero"], estudiante_data["direccion"],
                estudiante_data["tipo_educacion"], estudiante_data["grado"], estudiante_data["seccion"], estudiante_data["docente"],
                estudiante_data["tallaC"], estudiante_data["tallaP"], estudiante_data["tallaZ"], estudiante_data["madre"],estudiante_data["madre_ci"], 
                estudiante_data["ocupacion_madre"], estudiante_data["padre"],estudiante_data["padre_ci"], estudiante_data["ocupacion_padre"],
                representante_id
            )
            cursor.execute(sql_estu, valores_estu)
            estudiante_id = cursor.lastrowid

            # 3. Auditoría: solo estudiante
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
    def obtener_por_id(estudiante_id: int):
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("""
                SELECT cedula, nombres, apellidos, fecha_nac_est, city, genero, direccion,
                       tipo_educacion, grado, seccion, docente, tallaC, tallaP, tallaZ,
                       padre, padre_ci, ocupacion_padre, madre, madre_ci, ocupacion_madre, representante_id, estado
                FROM estudiantes
                WHERE id = %s
            """, (estudiante_id,))
            return cursor.fetchone()
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()

    @staticmethod
    def actualizar(estudiante_id: int, data: dict, usuario_actual: dict):
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

            # 2. Detectar cambios
            cambios = []
            for campo, nuevo_valor in data.items():
                valor_actual = estudiante_actual.get(campo)
                if str(valor_actual) != str(nuevo_valor):  # comparar como string para evitar problemas de tipos
                    cambios.append(f"{campo}: '{valor_actual}' → '{nuevo_valor}'")

            # 3. Ejecutar el UPDATE
            cursor.execute("""
                UPDATE estudiantes
                SET nombres=%s, apellidos=%s, fecha_nac_est=%s, city=%s, genero=%s,
                    direccion=%s, tipo_educacion=%s, grado=%s, seccion=%s, docente=%s,
                    tallaC=%s, tallaP=%s, tallaZ=%s, padre=%s, padre_ci=%s, ocupacion_padre=%s, madre=%s, madre_ci=%s,
                    ocupacion_madre=%s
                WHERE id=%s
            """, (
                data["nombres"], data["apellidos"], data["fecha_nac_est"], data["city"], data["genero"],
                data["direccion"], data["tipo_educacion"], data["grado"], data["seccion"],
                data["docente"], data["tallaC"], data["tallaP"], data["tallaZ"],
                data["padre"], data["padre_ci"], data["ocupacion_padre"], data["madre"], data["madre_ci"], data["ocupacion_madre"],
                estudiante_id
            ))
            conexion.commit()

            # 4. Registrar en auditoría si hubo cambios
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

            # 1. Obtener datos del estudiante antes de borrar
            cursor.execute("SELECT * FROM estudiantes WHERE id = %s", (estudiante_id,))
            estudiante = cursor.fetchone()
            if not estudiante:
                return False, "No se encontró el estudiante en la BD."

            id_representante = estudiante["representante_id"]

            # 2. Contar hijos del representante
            cursor.execute("SELECT COUNT(*) as total FROM estudiantes WHERE representante_id = %s", (id_representante,))
            hijos_count = cursor.fetchone()["total"]

            # 3. Registrar en auditoría (antes de eliminar)
            AuditoriaModel.registrar(
                usuario_id=usuario_actual["id"],
                accion="DELETE",
                entidad="estudiantes",
                entidad_id=estudiante_id,
                referencia=estudiante["cedula"],
                descripcion=f"Se eliminó estudiante {estudiante['nombres']} {estudiante['apellidos']} (grado: {estudiante['grado']}, sección: {estudiante['seccion']})"
            )

            # 4. Eliminar estudiante
            cursor.execute("DELETE FROM estudiantes WHERE id = %s", (estudiante_id,))

            # 5. Si era el único hijo, eliminar representante
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
    def listar():
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT id, cedula, nombres, apellidos, fecha_nac_est,
                       TIMESTAMPDIFF(YEAR, fecha_nac_est, CURDATE()) AS edad,
                       city, genero, direccion, tipo_educacion,
                       grado, seccion, docente, tallaC, tallaP, tallaZ, 
                       CASE WHEN estado = 1 THEN 'Activo' ELSE 'Inactivo' END AS estado
                FROM estudiantes
            """)
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
                    e.city, e.genero, e.direccion, e.tipo_educacion,
                    e.grado, e.seccion, e.docente, e.tallaC, e.tallaP, e.tallaZ, e.padre,
                    e.padre_ci, e.ocupacion_padre, e.madre, e.madre_ci, ocupacion_madre,
                    CASE WHEN e.estado = 1 THEN 'Activo' ELSE 'Inactivo' END AS estado,
                    r.cedula_repre,
                    r.nombres_repre,
                    r.apellidos_repre,
                    r.num_contact_repre
                    r.observacion
                FROM estudiantes e
                JOIN representantes r ON e.representante_id = r.id
                WHERE e.estado = 1
            """)
            return cursor.fetchall()
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()