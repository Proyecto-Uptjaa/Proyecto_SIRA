from utils.db import get_connection
from models.auditoria_model import AuditoriaModel

class InstitucionModel:
    @staticmethod
    def actualizar(institucion_id: int, data: dict, usuario_actual: dict):
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor(dictionary=True)

            # 1. Obtener datos actuales antes de modificar
            cursor.execute("SELECT * FROM institucion WHERE id=%s", (institucion_id,))
            institucion_actual = cursor.fetchone()
            if not institucion_actual:
                return False, "Institución no encontrada."

            # 2. Detectar cambios
            def normalizar(valor):
                if valor is None:
                    return None
                if isinstance(valor, str):
                    return valor.strip() or None
                return str(valor)

            cambios = []
            for campo, nuevo_valor in data.items():
                valor_actual = institucion_actual.get(campo)
                if normalizar(valor_actual) != normalizar(nuevo_valor):
                    cambios.append(f"{campo}: '{valor_actual}' → '{nuevo_valor}'")

            # 3. Ejecutar el UPDATE
            cursor.execute("""
                UPDATE institucion
                SET nombre=%s, codigo_dea=%s, direccion=%s, telefono=%s, correo=%s, director=%s, director_ci=%s
                WHERE id=%s
            """, (
                data["nombre"], data["codigo_dea"], data["direccion"],
                data["telefono"], data["correo"], data["director"], data["director_ci"], institucion_id
            ))
            conexion.commit()

            # 4. Registrar en auditoría si hubo cambios
            if cambios:
                descripcion = "; ".join(cambios)
                AuditoriaModel.registrar(
                    usuario_id=usuario_actual["id"],
                    accion="UPDATE",
                    entidad="institucion",
                    entidad_id=institucion_id,
                    referencia=data["nombre"],  # o institucion_actual["nombre"]
                    descripcion=f"Cambios: {descripcion}"
                )

            return True, "Datos actualizados correctamente."

        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
    @staticmethod
    def obtener_por_id(institucion_id: int):
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("""
                SELECT nombre, codigo_dea, direccion, telefono, correo, actualizado_en, director, director_ci
                FROM institucion
                WHERE id = %s
            """, (institucion_id,))
            return cursor.fetchone()
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()