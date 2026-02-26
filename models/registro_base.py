# models/registro_base.py
from utils.db import get_connection
from models.auditoria_model import AuditoriaModel

class RegistroBase:
    """Operaciones genéricas sobre registros."""

    # Tablas permitidas para cambio de estado
    TABLAS_VALIDAS = {"usuarios", "estudiantes", "empleados", "secciones", "representantes"}

    @staticmethod
    def cambiar_estado(tabla: str, id_registro: int, nuevo_estado: int, usuario_actual: dict):
        if tabla not in RegistroBase.TABLAS_VALIDAS:
            return False, f"Tabla '{tabla}' no permitida para cambio de estado"

        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos"
            cursor = conexion.cursor(dictionary=True)

            # 1. Obtener datos actuales antes de modificar
            cursor.execute(f"SELECT * FROM {tabla} WHERE id=%s", (id_registro,))
            registro_actual = cursor.fetchone()
            if not registro_actual:
                return False, f"Registro no encontrado en {tabla} con id={id_registro}"

            # 2. Actualizar estado (0/1 en BD)
            cursor.execute(f"UPDATE {tabla} SET estado=%s WHERE id=%s", (nuevo_estado, id_registro))
            conexion.commit()

            # 3. Registrar en auditoría
            referencia = None
            for campo in ("cedula", "username", "correo", "nombre", "nombres"):
                if campo in registro_actual:
                    referencia = registro_actual[campo]
                    break

            # Convertir a texto legible para la auditoría
            valor_estado = registro_actual.get("estado")
            estado_anterior = "Activo" if str(valor_estado) in ("1", "Activo") else "Inactivo"
            estado_nuevo = "Activo" if nuevo_estado == 1 else "Inactivo"

            AuditoriaModel.registrar(
                usuario_id=usuario_actual["id"],
                accion="UPDATE",
                entidad=tabla,
                entidad_id=id_registro,
                referencia=referencia,
                descripcion=f"Se cambió estado: {estado_anterior} → {estado_nuevo}"
            )

            return True, "Estado actualizado correctamente."

        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()