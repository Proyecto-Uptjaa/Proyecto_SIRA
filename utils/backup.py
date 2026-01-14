import os
import subprocess
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from typing import Tuple, Optional

# Cargar variables de entorno
load_dotenv()


class BackupManager:
    """Gestor de backups de la base de datos."""
    
    BACKUP_DIR = Path("backups")
    MAX_BACKUPS = 30
    
    @staticmethod
    def get_db_credentials() -> Tuple[Optional[str], Optional[str], Optional[str], Optional[str]]:
        """Obtiene credenciales de BD desde variables de entorno."""
        host = os.getenv("DB_HOST")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASS")
        database = os.getenv("DB_NAME")
        
        return host, user, password, database
    
    @staticmethod
    def crear_carpeta_backup():
        """Crea la carpeta de backups si no existe."""
        try:
            BackupManager.BACKUP_DIR.mkdir(parents=True, exist_ok=True)
            return True, "Carpeta de backups creada/verificada"
        except Exception as e:
            return False, f"Error creando carpeta de backups: {e}"
    
    @staticmethod
    def limpiar_backups_antiguos():
        """Elimina backups antiguos, mantiene solo los últimos MAX_BACKUPS."""
        try:
            backups = sorted(
                BackupManager.BACKUP_DIR.glob("backup_*.sql"),
                key=lambda x: x.stat().st_mtime,
                reverse=True
            )
            
            # Eliminar los que excedan el límite
            for backup_antiguo in backups[BackupManager.MAX_BACKUPS:]:
                backup_antiguo.unlink()
                print(f"Backup antiguo eliminado: {backup_antiguo.name}")
                
        except Exception as e:
            print(f"Error limpiando backups antiguos: {e}")
    
    @staticmethod
    def crear_backup_manual() -> Tuple[bool, str]:
        """Crea un backup manual de la BD."""
        try:
            # Validar credenciales
            host, user, password, database = BackupManager.get_db_credentials()
            
            if not all([host, user, password, database]):
                return False, "Credenciales de BD incompletas en archivo .env"
            
            # Crear carpeta de backups
            ok, mensaje = BackupManager.crear_carpeta_backup()
            if not ok:
                return False, mensaje
            
            # Generar nombre de archivo con timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            archivo_backup = BackupManager.BACKUP_DIR / f"backup_manual_{timestamp}.sql"
            
            # Comando mysqldump
            comando = [
                "mysqldump",
                f"--host={host}",
                f"--user={user}",
                f"--password={password}",
                "--single-transaction",  # Para tablas InnoDB sin bloquear
                "--routines",  # Incluir procedimientos almacenados
                "--triggers",  # Incluir triggers
                "--events",    # Incluir eventos
                database
            ]
            
            # Ejecutar mysqldump y guardar en archivo
            with open(archivo_backup, 'w', encoding='utf-8') as f:
                resultado = subprocess.run(
                    comando,
                    stdout=f,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=300  # Timeout de 5 minutos
                )
            
            if resultado.returncode != 0:
                # Eliminar archivo si falló
                if archivo_backup.exists():
                    archivo_backup.unlink()
                return False, f"Error ejecutando mysqldump: {resultado.stderr}"
            
            # Verificar que el archivo se creó correctamente
            if not archivo_backup.exists() or archivo_backup.stat().st_size == 0:
                return False, "El archivo de backup está vacío o no se creó"
            
            # Limpiar backups antiguos
            BackupManager.limpiar_backups_antiguos()
            
            tamaño_mb = archivo_backup.stat().st_size / (1024 * 1024)
            return True, f"Backup manual creado exitosamente:\n{archivo_backup.name}\nTamaño: {tamaño_mb:.2f} MB"
            
        except subprocess.TimeoutExpired:
            return False, "El proceso de backup tardó demasiado (timeout 5 min)"
        except FileNotFoundError:
            return False, "mysqldump no está instalado o no se encuentra en el PATH del sistema"
        except Exception as e:
            return False, f"Error inesperado creando backup: {e}"
    
    @staticmethod
    def crear_backup_automatico() -> Tuple[bool, str]:
        """Crea un backup automático de la BD."""
        try:
            # Validar credenciales
            host, user, password, database = BackupManager.get_db_credentials()
            
            if not all([host, user, password, database]):
                return False, "Credenciales de BD incompletas en archivo .env"
            
            # Crear carpeta de backups
            ok, mensaje = BackupManager.crear_carpeta_backup()
            if not ok:
                return False, mensaje
            
            # Generar nombre de archivo con timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            archivo_backup = BackupManager.BACKUP_DIR / f"backup_auto_{timestamp}.sql"
            
            # Comando mysqldump
            comando = [
                "mysqldump",
                f"--host={host}",
                f"--user={user}",
                f"--password={password}",
                "--single-transaction",
                "--routines",
                "--triggers",
                "--events",
                database
            ]
            
            # Ejecutar mysqldump y guardar en archivo
            with open(archivo_backup, 'w', encoding='utf-8') as f:
                resultado = subprocess.run(
                    comando,
                    stdout=f,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=300
                )
            
            if resultado.returncode != 0:
                if archivo_backup.exists():
                    archivo_backup.unlink()
                return False, f"Error ejecutando mysqldump: {resultado.stderr}"
            
            if not archivo_backup.exists() or archivo_backup.stat().st_size == 0:
                return False, "El archivo de backup está vacío o no se creó"
            
            # Limpiar backups antiguos
            BackupManager.limpiar_backups_antiguos()
            
            tamaño_mb = archivo_backup.stat().st_size / (1024 * 1024)
            print(f"Backup automático creado: {archivo_backup.name} ({tamaño_mb:.2f} MB)")
            return True, f"Backup automático creado: {archivo_backup.name}"
            
        except subprocess.TimeoutExpired:
            return False, "El proceso de backup tardó demasiado (timeout 5 min)"
        except FileNotFoundError:
            return False, "mysqldump no está instalado"
        except Exception as e:
            return False, f"Error inesperado: {e}"
    
    @staticmethod
    def obtener_ultimo_backup() -> Optional[dict]:
        """Retorna info del último backup o None si no hay."""
        try:
            if not BackupManager.BACKUP_DIR.exists():
                return None
            
            backups = sorted(
                BackupManager.BACKUP_DIR.glob("backup_*.sql"),
                key=lambda x: x.stat().st_mtime,
                reverse=True
            )
            
            if not backups:
                return None
            
            ultimo = backups[0]
            stats = ultimo.stat()
            
            return {
                "nombre": ultimo.name,
                "ruta": str(ultimo),
                "tamaño_mb": stats.st_size / (1024 * 1024),
                "fecha": datetime.fromtimestamp(stats.st_mtime),
                "tipo": "manual" if "manual" in ultimo.name else "automático"
            }
            
        except Exception as e:
            print(f"Error obteniendo último backup: {e}")
            return None
    
    @staticmethod
    def contar_backups() -> int:
        """Cuenta el total de backups existentes."""
        try:
            if not BackupManager.BACKUP_DIR.exists():
                return 0
            return len(list(BackupManager.BACKUP_DIR.glob("backup_*.sql")))
        except Exception:
            return 0
