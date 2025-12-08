from utils.db import get_connection
from models.auditoria_model import AuditoriaModel

class EmpleadoModel:
    """Modelo de empleados con conexión bajo demanda."""
    CARGO_OPCIONES = [
        "COCINERA I", "COCINERA II", "DOC II", "DOC III", "DOC IV", "DOC V",
        "DOC.(NG)/AULA", "DOC.(NG)/AULA BOLIV.", "DOC.II/AULA", "DOC. II./AULA BOLIV.",
        "DOC. III./AULA BOLIV.", "DOC. IV/AULA BOLIV.", "DOC. V/AULA BOLIV.", "DOC. VI/AULA BOLIV.",
        "DOC/NG", "OBRERO CERT.II", "OBRERO CERT.IV", "OBRERO GENERAL I",
        "OBRERO GENERAL III", "PROFESIONAL UNIVERSITARIO I", "TSU", "TSU EN EDUCACIÓN",
        "TSU EN EDUCACION BOLIV.", "TSU II"
    ]

    @staticmethod
    def guardar(empleado_data: dict, usuario_actual: dict):
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor()

            # 1. Insertar empleado
            sql_emple = """
                INSERT INTO empleados (
                    cedula, nombres, apellidos, fecha_nac, genero, direccion,
                    num_contact, correo, titulo, cargo, fecha_ingreso, num_carnet, rif, centro_votacion, codigo_rac
                )
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            valores_emple = (
                empleado_data["cedula"], empleado_data["nombres"], empleado_data["apellidos"], empleado_data["fecha_nac"],
                empleado_data["genero"], empleado_data["direccion"], empleado_data["num_contact"],
                empleado_data["correo"], empleado_data["titulo"], empleado_data["cargo"], empleado_data["fecha_ingreso"],
                empleado_data["num_carnet"], empleado_data["rif"], empleado_data["centro_votacion"], empleado_data["codigo_rac"]
            )
            cursor.execute(sql_emple, valores_emple)
            conexion.commit()

            # Obtener el ID recién insertado
            empleado_id = cursor.lastrowid

            # 2. Registrar en auditoría
            AuditoriaModel.registrar(
                usuario_id=usuario_actual["id"],   # el que está logueado
                accion="INSERT",
                entidad="empleados",
                entidad_id=empleado_id,
                referencia=empleado_data["cedula"],
                descripcion=f"Se registró empleado {empleado_data['nombres']} {empleado_data['apellidos']}"
            )

        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
   
    @staticmethod
    def obtener_por_id(empleado_id: int):
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("""
                SELECT cedula, nombres, apellidos, fecha_nac, genero, direccion, num_contact,
                       correo, titulo, cargo, fecha_ingreso, num_carnet, rif, centro_votacion, estado, codigo_rac
                FROM empleados
                WHERE id = %s
            """, (empleado_id,))
            return cursor.fetchone()
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()

    @staticmethod
    def actualizar(empleado_id: int, data: dict, usuario_actual: dict):
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor(dictionary=True)

            # 1. Obtener datos actuales
            cursor.execute("SELECT * FROM empleados WHERE id=%s", (empleado_id,))
            empleado_actual = cursor.fetchone()
            if not empleado_actual:
                raise Exception("Empleado no encontrado")

            # 2. Detectar cambios
            cambios = []
            for campo, nuevo_valor in data.items():
                valor_actual = empleado_actual.get(campo)
                if str(valor_actual) != str(nuevo_valor):  # comparar como string para evitar problemas de tipos
                    cambios.append(f"{campo}: '{valor_actual}' → '{nuevo_valor}'")

            # 3. Ejecutar el UPDATE
            cursor.execute("""
                UPDATE empleados
                SET nombres=%s, apellidos=%s, fecha_nac=%s, genero=%s,
                    direccion=%s, num_contact=%s, correo=%s, titulo=%s, cargo=%s, fecha_ingreso=%s,
                    num_carnet=%s, rif=%s, centro_votacion=%s, codigo_rac=%s
                WHERE id=%s
            """, (
                data["nombres"], data["apellidos"], data["fecha_nac"], data["genero"],
                data["direccion"], data["num_contact"], data["correo"], data["titulo"], data["cargo"],
                data["fecha_ingreso"], data["num_carnet"], data["rif"], data["centro_votacion"], data["codigo_rac"],
                empleado_id
            ))
            conexion.commit()

            # 4. Registrar en auditoría si hubo cambios
            if cambios:
                descripcion = "; ".join(cambios)
                AuditoriaModel.registrar(
                    usuario_id=usuario_actual["id"],
                    accion="UPDATE",
                    entidad="empleados",
                    entidad_id=empleado_id,
                    referencia=empleado_actual["cedula"],
                    descripcion=f"Cambios: {descripcion}"
                )

        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def eliminar(empleado_id: int, usuario_actual: dict):
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor(dictionary=True)

            # 1. Obtener datos antes de borrar
            cursor.execute("SELECT cedula, nombres, apellidos, cargo FROM empleados WHERE id=%s", (empleado_id,))
            empleado = cursor.fetchone()

            if not empleado:
                return False, "Empleado no encontrado."

            # 2. Registrar en auditoría (antes de eliminar)
            AuditoriaModel.registrar(
                usuario_id=usuario_actual["id"],
                accion="DELETE",
                entidad="empleados",
                entidad_id=empleado_id,
                referencia=empleado["cedula"],
                descripcion=f"Se eliminó empleado {empleado['nombres']} {empleado['apellidos']} (cargo: {empleado['cargo']})"
            )

            # 3. Eliminar
            cursor.execute("DELETE FROM empleados WHERE id = %s", (empleado_id,))
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
                SELECT id, cedula, nombres, apellidos, fecha_nac,
                       TIMESTAMPDIFF(YEAR, fecha_nac, CURDATE()) AS edad,
                       genero, direccion, num_contact, correo,
                       titulo, cargo, fecha_ingreso, num_carnet, rif, codigo_rac, 
                        CASE WHEN estado = 1 THEN 'Activo' ELSE 'Inactivo' END AS estado
                FROM empleados
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
                SELECT id, cedula, nombres, apellidos, fecha_nac,
                       TIMESTAMPDIFF(YEAR, fecha_nac, CURDATE()) AS edad,
                       genero, direccion, num_contact, correo,
                       titulo, cargo, fecha_ingreso, num_carnet, rif, centro_votacion, codigo_rac, 
                        CASE WHEN estado = 1 THEN 'Activo' ELSE 'Inactivo' END AS estado
                FROM empleados
                WHERE estado = 1
            """)
            return cursor.fetchall()
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()