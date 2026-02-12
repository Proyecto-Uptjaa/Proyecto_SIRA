import os
from typing import Optional, Tuple

from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QBuffer, QByteArray, QIODevice

from models.institucion_model import InstitucionModel


# Configuración del logo
LOGO_MAX_SIZE_KB = 500          # Tamaño máximo del archivo en KB
LOGO_MAX_DIMENSION = 512        # Dimensión máxima en píxeles (ancho o alto)
LOGO_FORMATOS_VALIDOS = (".png", ".jpg", ".jpeg", ".bmp")
LOGO_FILTRO_DIALOGO = "Imágenes (*.png *.jpg *.jpeg *.bmp)"

# Caché global del logo
_logo_cache: Optional[QPixmap] = None
_logo_bytes_cache: Optional[bytes] = None


def validar_imagen(ruta: str) -> Tuple[bool, str]:
    """Valida que un archivo de imagen cumpla los requisitos."""
    if not os.path.exists(ruta):
        return False, "El archivo no existe."
    
    # Validar extensión
    _, ext = os.path.splitext(ruta)
    if ext.lower() not in LOGO_FORMATOS_VALIDOS:
        formatos = ", ".join(LOGO_FORMATOS_VALIDOS)
        return False, f"Formato no soportado. Use: {formatos}"
    
    # Validar tamaño del archivo
    tamaño_kb = os.path.getsize(ruta) / 1024
    if tamaño_kb > LOGO_MAX_SIZE_KB * 4:  # Permitir hasta 4x porque se redimensiona
        return False, f"El archivo es demasiado grande (máx. {LOGO_MAX_SIZE_KB * 4} KB)."
    
    # Validar que sea una imagen válida
    pixmap = QPixmap(ruta)
    if pixmap.isNull():
        return False, "No se pudo leer la imagen. El archivo podría estar dañado."
    
    # Validar dimensiones mínimas
    if pixmap.width() < 32 or pixmap.height() < 32:
        return False, "La imagen es demasiado pequeña (mínimo 32x32 píxeles)."
    
    return True, "Imagen válida."


def procesar_imagen(ruta: str) -> Tuple[Optional[bytes], str]:
    """Carga una imagen, la redimensiona si es necesario y la convierte a bytes PNG."""
    # Validar primero
    valido, msg = validar_imagen(ruta)
    if not valido:
        return None, msg
    
    pixmap = QPixmap(ruta)
    
    # Redimensionar si excede las dimensiones máximas
    if pixmap.width() > LOGO_MAX_DIMENSION or pixmap.height() > LOGO_MAX_DIMENSION:
        pixmap = pixmap.scaled(
            LOGO_MAX_DIMENSION, LOGO_MAX_DIMENSION,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
    
    # Convertir a bytes PNG
    byte_array = QByteArray()
    buffer = QBuffer(byte_array)
    buffer.open(QIODevice.OpenModeFlag.WriteOnly)
    pixmap.save(buffer, "PNG", quality=90)
    buffer.close()
    
    datos = bytes(byte_array.data())
    
    # Verificar tamaño final
    tamaño_kb = len(datos) / 1024
    if tamaño_kb > LOGO_MAX_SIZE_KB:
        # Intentar reducir más
        factor = 0.8
        while tamaño_kb > LOGO_MAX_SIZE_KB and factor > 0.3:
            new_w = int(pixmap.width() * factor)
            new_h = int(pixmap.height() * factor)
            pixmap_reducido = pixmap.scaled(
                new_w, new_h,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            byte_array = QByteArray()
            buffer = QBuffer(byte_array)
            buffer.open(QIODevice.OpenModeFlag.WriteOnly)
            pixmap_reducido.save(buffer, "PNG", quality=85)
            buffer.close()
            datos = bytes(byte_array.data())
            tamaño_kb = len(datos) / 1024
            factor -= 0.1
        
        if tamaño_kb > LOGO_MAX_SIZE_KB:
            return None, f"No se pudo reducir la imagen por debajo de {LOGO_MAX_SIZE_KB} KB."
    
    return datos, "Imagen procesada correctamente."


def bytes_a_pixmap(datos: bytes) -> Optional[QPixmap]:
    """Convierte bytes de imagen a QPixmap."""
    if not datos:
        return None
    
    pixmap = QPixmap()
    if pixmap.loadFromData(datos):
        return pixmap
    return None


def obtener_logo_pixmap(forzar_recarga: bool = False) -> Optional[QPixmap]:
    """Obtiene el logo institucional como QPixmap, usando caché."""
    global _logo_cache, _logo_bytes_cache
    
    if not forzar_recarga and _logo_cache is not None:
        return _logo_cache
    
    # Cargar desde BD
    datos = InstitucionModel.obtener_logo()
    
    if datos:
        pixmap = bytes_a_pixmap(datos)
        if pixmap and not pixmap.isNull():
            _logo_cache = pixmap
            _logo_bytes_cache = datos
            return pixmap
    
    # No hay logo en BD
    _logo_cache = None
    _logo_bytes_cache = None
    return None


def obtener_logo_bytes(forzar_recarga: bool = False) -> Optional[bytes]:
    """Obtiene los bytes del logo institucional, usando caché."""
    global _logo_cache, _logo_bytes_cache
    
    if not forzar_recarga and _logo_bytes_cache is not None:
        return _logo_bytes_cache
    
    # Forzar recarga del pixmap (que también carga los bytes)
    obtener_logo_pixmap(forzar_recarga=True)
    return _logo_bytes_cache


def invalidar_cache():
    """Limpia la caché del logo para forzar recarga."""
    global _logo_cache, _logo_bytes_cache
    _logo_cache = None
    _logo_bytes_cache = None


def aplicar_logo_a_label(label, ancho: int = 50, alto: int = 61, 
                         usar_fallback: bool = True) -> bool:
    """Aplica el logo institucional a un QLabel, escalado al tamaño indicado."""
    pixmap = obtener_logo_pixmap()
    
    if pixmap and not pixmap.isNull():
        scaled = pixmap.scaled(
            ancho, alto,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        label.setPixmap(scaled)
        return True
    
    if usar_fallback:
        # Usar logo por defecto embebido en recursos
        fallback = QPixmap(":/logos/logo_escuela_sinFondo.png")
        if not fallback.isNull():
            scaled = fallback.scaled(
                ancho, alto,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            label.setPixmap(scaled)
    
    return False
