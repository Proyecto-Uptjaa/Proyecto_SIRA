from utils.db import get_connection
from typing import List, Dict, Optional


class AuditoriaModel:
    """Sistema de auditoría del sistema."""
    
    @staticmethod
    def listar(limit: int = 50, offset: int = 0) -> List[Dict]:
        """Lista registros de auditoría con paginación."""
        if not isinstance(limit, int) or limit <= 0 or limit > 1000:
            limit = 50
        if not isinstance(offset, int) or offset < 0:
            offset = 0
            
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return []
                
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("""
                SELECT a.id,
                       u.username AS usuario,
                       a.accion,
                       a.entidad,
                       a.entidad_id,
                       a.referencia,
                       a.descripcion,
                       a.fecha
                FROM auditoria a
                JOIN usuarios u ON a.usuario_id = u.id
                ORDER BY a.fecha DESC
                LIMIT %s OFFSET %s
            """, (limit, offset))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al listar auditoría: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
    
    @staticmethod
    def registrar(
        usuario_id: int,
        accion: str,
        entidad: str,
        entidad_id: Optional[int],
        referencia: str,
        descripcion: str = ""
    ) -> bool:
        """Registra una acción en el sistema de auditoría."""
        # Validaciones estrictas
        if not isinstance(usuario_id, int) or usuario_id <= 0:
            print(f"Error auditoría: usuario_id inválido ({usuario_id})")
            return False
        
        if not accion or not isinstance(accion, str) or len(accion) > 50:
            print(f"Error auditoría: accion inválida ({accion})")
            return False
        
        if not entidad or not isinstance(entidad, str) or len(entidad) > 50:
            print(f"Error auditoría: entidad inválida ({entidad})")
            return False
        
        if entidad_id is not None and (not isinstance(entidad_id, int) or entidad_id <= 0):
            print(f"Error auditoría: entidad_id inválido ({entidad_id})")
            return False
        
        if not referencia or not isinstance(referencia, str):
            referencia = "N/A"
        if len(referencia) > 100:
            referencia = referencia[:97] + "..."
        
        if not isinstance(descripcion, str):
            descripcion = ""
        if len(descripcion) > 500:
            descripcion = descripcion[:497] + "..."
        
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                print("Error auditoría: no hay conexión a BD")
                return False
                
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO auditoria 
                (usuario_id, accion, entidad, entidad_id, referencia, descripcion, fecha)
                VALUES (%s, %s, %s, %s, %s, %s, NOW())
            """, (usuario_id, accion, entidad, entidad_id, referencia, descripcion))
            
            conexion.commit()
            return True
            
        except Exception as e:
            print(f"Error al registrar auditoría: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
    
    @staticmethod
    def contar_total() -> int:
        """Cuenta el total de registros de auditoría."""
        conexion = None
        cursor = None
        try:
            conexion = get_connection()
            if not conexion:
                return 0
                
            cursor = conexion.cursor()
            cursor.execute("SELECT COUNT(*) FROM auditoria")
            resultado = cursor.fetchone()
            return resultado[0] if resultado else 0
        except Exception as e:
            print(f"Error al contar auditoría: {e}")
            return 0
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()