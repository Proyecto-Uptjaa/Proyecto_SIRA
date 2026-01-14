"""
Script de inicialización del sistema SIRA.
Crea el primer usuario administrador.
"""

import sys
import os
from pathlib import Path

# Agregar el directorio raíz al path para importar módulos
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

from utils.db import get_connection
import bcrypt
from getpass import getpass


def verificar_usuarios_existentes():
    """Verifica si existen usuarios en el sistema."""
    conexion = None
    cursor = None
    try:
        conexion = get_connection()
        if not conexion:
            print("❌ Error: No se pudo conectar a la base de datos")
            return None
        
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM usuarios")
        resultado = cursor.fetchone()
        return resultado[0]
    except Exception as e:
        print(f"❌ Error al verificar usuarios: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conexion and conexion.is_connected():
            conexion.close()


def crear_admin_inicial():
    """Crea el primer usuario administrador."""
    print("=" * 60)
    print("🔧 INICIALIZACIÓN DEL SISTEMA SIRA")
    print("=" * 60)
    print("\nEste script creará el primer usuario administrador.")
    print("Asegúrese de que la base de datos esté correctamente configurada.\n")
    
    # Verificar usuarios existentes
    total_usuarios = verificar_usuarios_existentes()
    
    if total_usuarios is None:
        print("\n❌ No se pudo verificar el estado de la base de datos.")
        return False
    
    if total_usuarios > 0:
        print(f"\n⚠️  ADVERTENCIA: Ya existen {total_usuarios} usuario(s) en el sistema.")
        respuesta = input("¿Desea crear un administrador adicional? (s/n): ").lower()
        if respuesta != 's':
            print("\n❌ Operación cancelada.")
            return False
    
    print("\n📝 Ingrese los datos del administrador:\n")
    
    # Solicitar datos
    nombre_completo = input("Nombre completo: ").strip()
    if not nombre_completo:
        print("❌ El nombre completo es obligatorio.")
        return False
    
    username = input("Nombre de usuario: ").strip()
    if not username:
        print("❌ El nombre de usuario es obligatorio.")
        return False
    
    # Verificar username duplicado
    if verificar_username_duplicado(username):
        print(f"❌ El usuario '{username}' ya existe en el sistema.")
        return False
    
    # Solicitar contraseña con confirmación
    while True:
        password = getpass("Contraseña: ")
        if len(password) < 6:
            print("❌ La contraseña debe tener al menos 6 caracteres.")
            continue
        
        password_confirm = getpass("Confirmar contraseña: ")
        if password != password_confirm:
            print("❌ Las contraseñas no coinciden. Intente nuevamente.")
            continue
        
        break
    
    # Confirmar creación
    print("\n" + "=" * 60)
    print("📋 RESUMEN:")
    print(f"   Nombre completo: {nombre_completo}")
    print(f"   Username: {username}")
    print(f"   Rol: admin")
    print("=" * 60)
    
    confirmacion = input("\n¿Confirmar creación del usuario? (s/n): ").lower()
    if confirmacion != 's':
        print("\n❌ Operación cancelada.")
        return False
    
    # Crear usuario
    conexion = None
    cursor = None
    try:
        conexion = get_connection()
        if not conexion:
            print("\n❌ Error de conexión a la base de datos")
            return False
        
        cursor = conexion.cursor()
        
        # Hashear contraseña
        password_hash = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")
        
        # Insertar usuario
        sql = """
            INSERT INTO usuarios (nombre_completo, username, password_hash, rol, estado)
            VALUES (%s, %s, %s, 'admin', 1)
        """
        valores = (nombre_completo, username, password_hash)
        
        cursor.execute(sql, valores)
        conexion.commit()
        
        print("\n✅ Usuario administrador creado exitosamente!")
        print(f"\n🔐 Credenciales de acceso:")
        print(f"   Usuario: {username}")
        print(f"   Contraseña: [la que configuró]")
        print(f"\n⚠️  Guarde estas credenciales en un lugar seguro.")
        
        return True
        
    except Exception as e:
        if conexion:
            conexion.rollback()
        print(f"\n❌ Error al crear usuario: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conexion and conexion.is_connected():
            conexion.close()


def verificar_username_duplicado(username):
    """Verifica si un username ya existe."""
    conexion = None
    cursor = None
    try:
        conexion = get_connection()
        if not conexion:
            return False
        
        cursor = conexion.cursor()
        cursor.execute("SELECT id FROM usuarios WHERE username = %s", (username,))
        return cursor.fetchone() is not None
    except Exception:
        return False
    finally:
        if cursor:
            cursor.close()
        if conexion and conexion.is_connected():
            conexion.close()


if __name__ == "__main__":
    try:
        exito = crear_admin_inicial()
        sys.exit(0 if exito else 1)
    except KeyboardInterrupt:
        print("\n\n❌ Operación cancelada por el usuario.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        sys.exit(1)