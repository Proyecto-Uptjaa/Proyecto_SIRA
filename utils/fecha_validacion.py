from datetime import datetime, timedelta
from typing import Dict, Optional
from utils.db import get_connection


# Umbrales de tolerancia (en minutos y días)
UMBRAL_DIFERENCIA_SERVIDOR_MIN = 5      # Diferencia máxima aceptable con MySQL (minutos)
UMBRAL_FUTURO_DIAS = 1                  # Máximo de días en el futuro permitido
UMBRAL_PASADO_DIAS = 30                 # Máximo de días en el pasado vs última auditoría


def verificar_fecha_sistema() -> Dict:
    """Verifica la consistencia de la fecha/hora del sistema."""
    resultado = {
        'ok': True,
        'advertencias': [],
        'diferencia_servidor_min': None,
        'fecha_sistema': datetime.now(),
        'fecha_servidor': None,
        'ultima_auditoria': None,
    }

    conexion = None
    cursor = None
    try:
        conexion = get_connection()
        if not conexion:
            # Sin conexión no se puede verificar, no bloquear
            return resultado

        cursor = conexion.cursor(dictionary=True)
        fecha_sistema = datetime.now()

        # Verificación 1: Hora local vs MySQL NOW()
        cursor.execute("SELECT NOW() AS fecha_servidor")
        row = cursor.fetchone()
        if row and row.get('fecha_servidor'):
            fecha_servidor = row['fecha_servidor']
            if isinstance(fecha_servidor, str):
                fecha_servidor = datetime.strptime(fecha_servidor, "%Y-%m-%d %H:%M:%S")

            resultado['fecha_servidor'] = fecha_servidor
            diferencia = abs((fecha_sistema - fecha_servidor).total_seconds()) / 60.0
            resultado['diferencia_servidor_min'] = round(diferencia, 1)

            if diferencia > UMBRAL_DIFERENCIA_SERVIDOR_MIN:
                resultado['ok'] = False
                if fecha_sistema > fecha_servidor:
                    direccion = "adelantada"
                else:
                    direccion = "atrasada"

                if diferencia < 60:
                    texto_dif = f"{int(diferencia)} minutos"
                elif diferencia < 1440:
                    texto_dif = f"{diferencia / 60:.1f} horas"
                else:
                    texto_dif = f"{diferencia / 1440:.0f} días"

                resultado['advertencias'].append(
                    f"La hora del equipo está {direccion} {texto_dif} "
                    f"respecto al servidor de base de datos"
                )

        # Verificación 2: Hora local vs última auditoría
        cursor.execute(
            "SELECT fecha FROM auditoria ORDER BY fecha DESC LIMIT 1"
        )
        row = cursor.fetchone()
        if row and row.get('fecha'):
            ultima = row['fecha']
            if isinstance(ultima, str):
                ultima = datetime.strptime(ultima, "%Y-%m-%d %H:%M:%S")

            resultado['ultima_auditoria'] = ultima

            # Si la hora del sistema es muy anterior al último registro
            diferencia_audit = (ultima - fecha_sistema).total_seconds() / 86400.0  # días
            if diferencia_audit > UMBRAL_FUTURO_DIAS:
                resultado['ok'] = False
                resultado['advertencias'].append(
                    f"La fecha del equipo ({fecha_sistema.strftime('%d/%m/%Y %H:%M')}) "
                    f"es anterior al último registro del sistema "
                    f"({ultima.strftime('%d/%m/%Y %H:%M')})"
                )

            # Si la hora del sistema está muy en el futuro respecto al último registro
            diferencia_futuro = (fecha_sistema - ultima).total_seconds() / 86400.0
            if diferencia_futuro > UMBRAL_PASADO_DIAS:
                resultado['ok'] = False
                resultado['advertencias'].append(
                    f"Han pasado {int(diferencia_futuro)} días desde la última "
                    f"actividad registrada en el sistema — verifique la fecha del equipo"
                )

    except Exception as e:
        # Error al verificar: no bloquear, solo registrar
        print(f"Error al verificar fecha del sistema: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexion and conexion.is_connected():
            conexion.close()

    return resultado


def obtener_texto_advertencia(resultado: Dict) -> Optional[str]:
    """Genera un texto formateado para mostrar en el widget de notificaciones."""
    
    if resultado['ok']:
        return None

    lineas = ["⚠️ Advertencia de fecha/hora del equipo:"]
    for adv in resultado['advertencias']:
        lineas.append(f"  • {adv}")
    lineas.append("  Esto puede causar inconsistencias en los registros.")

    return "\n".join(lineas)
