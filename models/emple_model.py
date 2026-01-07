from utils.db import get_connection
from models.auditoria_model import AuditoriaModel
from typing import Optional, Dict, List, Tuple


class EmpleadoModel:
    """
    Modelo de empleados con conexión bajo demanda.
    Gestiona CRUD completo con auditoría automática y validaciones.
    """
    
    CARGO_OPCIONES = [
        "COCINERA I", "COCINERA II", "DOC II", "DOC III", "DOC IV", "DOC V",
        "DOC.(NG)/AULA", "DOC.(NG)/AULA BOLIV.", "DOC.II/AULA", "DOC. II./AULA BOLIV.",
        "DOC. III./AULA BOLIV.", "DOC. IV/AULA BOLIV.", "DOC. V/AULA BOLIV.", "DOC. VI/AULA BOLIV.",
        "DOC/NG", "OBRERO CERT.II", "OBRERO CERT.IV", "OBRERO GENERAL I",
        "OBRERO GENERAL III", "PROFESIONAL UNIVERSITARIO I", "TSU", "TSU EN EDUCACIÓN",
        "TSU EN EDUCACION BOLIV.", "TSU II"
    ]

    CARGOS_DOCENTES = [
        "DOC II", "DOC III", "DOC IV", "DOC V",
        "DOC.(NG)/AULA", "DOC.(NG)/AULA BOLIV.", "DOC.II/AULA", 
        "DOC. II./AULA BOLIV.", "DOC. III./AULA BOLIV.", 
        "DOC. IV/AULA BOLIV.", "DOC. V/AULA BOLIV.", 
        "DOC. VI/AULA BOLIV.", "DOC/NG",
        "TSU EN EDUCACIÓN", "TSU EN EDUCACION BOLIV."
    ]
    
    @staticmethod
    def es_docente(cargo: str) -> bool:
        """Verifica si un cargo es docente"""
        return cargo in EmpleadoModel.CARGOS_DOCENTES
    
    @staticmethod
    def listar_docentes_disponibles() -> List[Dict]:
        """Retorna empleados activos con cargos docentes"""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return []
            
            cursor = conexion.cursor(dictionary=True)
            
            # Construir placeholders para IN
            placeholders = ','.join(['%s'] * len(EmpleadoModel.CARGOS_DOCENTES))
            
            cursor.execute(f"""
                SELECT id, cedula, nombres, apellidos, cargo, 
                       CONCAT(nombres, ' ', apellidos) as nombre_completo
                FROM empleados
                WHERE cargo IN ({placeholders}) AND estado = 1
                ORDER BY apellidos, nombres
            """, tuple(EmpleadoModel.CARGOS_DOCENTES))
            
            return cursor.fetchall()
        except Exception as e:
            print(f"Error en listar_docentes_disponibles: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def guardar(empleado_data: dict, usuario_actual: dict) -> Tuple[bool, str]:
        """
        Registra un nuevo empleado en la BD.
        
        Args:
            empleado_data: Diccionario con datos del empleado
            usuario_actual: Usuario que realiza la acción
            
        Returns:
            (éxito: bool, mensaje: str)
        """
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos"
            
            cursor = conexion.cursor()

            # Validar cédula duplicada
            cursor.execute("SELECT id FROM empleados WHERE cedula = %s", (empleado_data["cedula"],))
            if cursor.fetchone():
                return False, f"Ya existe un empleado con cédula {empleado_data['cedula']}"

            # Insertar empleado
            sql_emple = """
                INSERT INTO empleados (
                    cedula, nombres, apellidos, fecha_nac, genero, direccion,
                    num_contact, correo, titulo, cargo, fecha_ingreso, num_carnet, rif, centro_votacion, codigo_rac
                )
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            valores_emple = (
                empleado_data["cedula"], empleado_data["nombres"], empleado_data["apellidos"], 
                empleado_data["fecha_nac"], empleado_data["genero"], empleado_data["direccion"], 
                empleado_data["num_contact"], empleado_data["correo"], empleado_data["titulo"], 
                empleado_data["cargo"], empleado_data["fecha_ingreso"], empleado_data["num_carnet"], 
                empleado_data["rif"], empleado_data["centro_votacion"], empleado_data["codigo_rac"]
            )
            cursor.execute(sql_emple, valores_emple)
            conexion.commit()

            # Obtener el ID recién insertado
            empleado_id = cursor.lastrowid

            # Auditoría
            AuditoriaModel.registrar(
                usuario_id=usuario_actual["id"],
                accion="INSERT",
                entidad="empleados",
                entidad_id=empleado_id,
                referencia=empleado_data["cedula"],
                descripcion=f"Registró empleado {empleado_data['nombres']} {empleado_data['apellidos']}"
            )
            
            return True, "Empleado registrado correctamente"

        except Exception as e:
            if conexion:
                conexion.rollback()
            return False, f"Error al guardar empleado: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
   
    @staticmethod
    def obtener_por_id(empleado_id: int) -> Optional[Dict]:
        """Obtiene datos completos de un empleado por su ID."""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return None
            
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("""
                SELECT cedula, nombres, apellidos, fecha_nac, genero, direccion, num_contact,
                       correo, titulo, cargo, fecha_ingreso, num_carnet, rif, centro_votacion, estado, codigo_rac
                FROM empleados
                WHERE id = %s
            """, (empleado_id,))
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
    def actualizar(empleado_id: int, data: dict, usuario_actual: dict) -> Tuple[bool, str]:
        """
        Actualiza datos de un empleado existente.
        
        Args:
            empleado_id: ID del empleado a actualizar
            data: Diccionario con nuevos datos
            usuario_actual: Usuario que realiza la acción
            
        Returns:
            (éxito: bool, mensaje: str)
        """
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos"
            
            cursor = conexion.cursor(dictionary=True)

            # Obtener datos actuales
            cursor.execute("SELECT * FROM empleados WHERE id=%s", (empleado_id,))
            empleado_actual = cursor.fetchone()
            
            if not empleado_actual:
                return False, "Empleado no encontrado"

            # Detectar cambios
            cambios = []
            for campo, nuevo_valor in data.items():
                valor_actual = empleado_actual.get(campo)
                if str(valor_actual) != str(nuevo_valor):
                    cambios.append(f"{campo}: '{valor_actual}' → '{nuevo_valor}'")

            # Ejecutar UPDATE
            cursor.execute("""
                UPDATE empleados
                SET nombres=%s, apellidos=%s, fecha_nac=%s, genero=%s,
                    direccion=%s, num_contact=%s, correo=%s, titulo=%s, cargo=%s, fecha_ingreso=%s,
                    num_carnet=%s, rif=%s, centro_votacion=%s, codigo_rac=%s
                WHERE id=%s
            """, (
                data["nombres"], data["apellidos"], data["fecha_nac"], data["genero"],
                data["direccion"], data["num_contact"], data["correo"], data["titulo"], data["cargo"],
                data["fecha_ingreso"], data["num_carnet"], data["rif"], data["centro_votacion"], 
                data["codigo_rac"], empleado_id
            ))
            conexion.commit()

            # Auditoría solo si hubo cambios
            if cambios:
                descripcion = "; ".join(cambios)
                AuditoriaModel.registrar(
                    usuario_id=usuario_actual["id"],
                    accion="UPDATE",
                    entidad="empleados",
                    entidad_id=empleado_id,
                    referencia=empleado_actual["cedula"],
                    descripcion=f"Actualizó: {descripcion}"
                )
            
            return True, "Empleado actualizado correctamente"

        except Exception as e:
            if conexion:
                conexion.rollback()
            return False, f"Error al actualizar: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def eliminar(empleado_id: int, usuario_actual: dict) -> Tuple[bool, str]:
        """
        Elimina un empleado de la BD.
        
        Args:
            empleado_id: ID del empleado
            usuario_actual: Usuario que realiza la acción
            
        Returns:
            (éxito: bool, mensaje: str)
        """
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return False, "Error de conexión a la base de datos"
            
            cursor = conexion.cursor(dictionary=True)

            # Obtener datos antes de borrar
            cursor.execute(
                "SELECT cedula, nombres, apellidos, cargo FROM empleados WHERE id=%s", 
                (empleado_id,)
            )
            empleado = cursor.fetchone()

            if not empleado:
                return False, "Empleado no encontrado"

            # Auditoría antes de eliminar
            AuditoriaModel.registrar(
                usuario_id=usuario_actual["id"],
                accion="DELETE",
                entidad="empleados",
                entidad_id=empleado_id,
                referencia=empleado["cedula"],
                descripcion=f"Eliminó empleado {empleado['nombres']} {empleado['apellidos']} ({empleado['cargo']})"
            )

            # Eliminar
            cursor.execute("DELETE FROM empleados WHERE id = %s", (empleado_id,))
            conexion.commit()

            return True, "Empleado eliminado correctamente"

        except Exception as e:
            if conexion:
                conexion.rollback()
            return False, f"Error al eliminar: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def listar() -> List[tuple]:
        """Lista todos los empleados con edad calculada."""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return []
            
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
        except Exception as e:
            print(f"Error en listar: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
    
    @staticmethod
    def listar_activos() -> List[Dict]:
        """Lista solo empleados activos (para exportaciones)."""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return []
            
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
        except Exception as e:
            print(f"Error en listar_activos: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()