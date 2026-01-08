import os
import io
from datetime import date, datetime

from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
)
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER

from PySide6.QtWidgets import QFileDialog, QMessageBox

from paths import ICON_DIR
from models.institucion_model import InstitucionModel
from openpyxl import Workbook
from utils.edad import calcular_edad
from utils.dialogs import crear_msgbox

# Estilos globales
styles = getSampleStyleSheet()

justificado = ParagraphStyle(
    name="Justificado",
    parent=styles["Normal"],
    alignment=TA_JUSTIFY,
    leading=16
)
centrado = ParagraphStyle(
    name="Centrado",
    parent=styles["Normal"],
    alignment=TA_CENTER,
    leading=16
)

page_width, page_height = letter


# UTILIDADES DE VALIDACIÓN Y CONVERSIÓN

def sanitizar_nombre_archivo(nombre: str) -> str:
    """
    Limpia caracteres inválidos de nombres de archivo.
    
    Args:
        nombre: Nombre original del archivo
        
    Returns:
        Nombre sanitizado sin caracteres problemáticos
    """
    caracteres_invalidos = r'<>:"/\|?*'
    for char in caracteres_invalidos:
        nombre = nombre.replace(char, '_')
    return nombre.strip()


def crear_carpeta_segura(ruta: str) -> tuple[bool, str]:
    """
    Crea una carpeta verificando permisos de escritura.
    
    Args:
        ruta: Ruta de la carpeta a crear
        
    Returns:
        Tuple (éxito, mensaje)
    """
    try:
        os.makedirs(ruta, exist_ok=True)
        
        # Verificar que sea escribible
        test_file = os.path.join(ruta, '.test_write')
        try:
            with open(test_file, 'w') as f:
                f.write('test')
            os.remove(test_file)
            return True, "Carpeta creada correctamente"
        except Exception as e:
            return False, f"La carpeta no tiene permisos de escritura: {e}"
            
    except Exception as e:
        return False, f"No se pudo crear la carpeta: {e}"


def convertir_fecha_string(fecha) -> str:
    """
    Convierte diferentes formatos de fecha a string DD/MM/YYYY.
    
    Args:
        fecha: date, datetime o string
        
    Returns:
        String con formato DD/MM/YYYY
    """
    if fecha is None:
        return "N/A"
    
    if isinstance(fecha, (date, datetime)):
        return fecha.strftime("%d/%m/%Y")
    
    # Si ya es string, intentar parsearlo para validar
    if isinstance(fecha, str):
        try:
            fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
            return fecha_obj.strftime("%d/%m/%Y")
        except:
            return str(fecha)
    
    return str(fecha)


def extraer_año_escolar(año_escolar: dict) -> tuple[int, int]:
    """
    Extrae años de inicio y fin del diccionario año_escolar.
    
    Args:
        año_escolar: Dict con datos del año escolar
        
    Returns:
        Tuple (año_inicio, año_fin)
    """
    if not año_escolar:
        año_actual = datetime.now().year
        return año_actual, año_actual + 1
    
    anio_inicio = año_escolar.get('anio_inicio')
    
    if isinstance(anio_inicio, (date, datetime)):
        año_inicio = anio_inicio.year
    elif isinstance(anio_inicio, str):
        try:
            año_inicio = int(anio_inicio.split('-')[0])
        except:
            año_inicio = datetime.now().year
    else:
        año_inicio = int(anio_inicio) if anio_inicio else datetime.now().year
    
    año_fin = año_inicio + 1
    return año_inicio, año_fin


def normalizar_cedula(cedula: str) -> str:
    """
    Normaliza formato de cédula respetando el prefijo existente.
    Si no tiene prefijo, agrega V-.
    
    Args:
        cedula: Cédula a normalizar
        
    Returns:
        Cédula con formato correcto
    """
    if not cedula:
        return "N/A"
    
    cedula = str(cedula).strip().upper()
    
    # Si ya tiene prefijo (V-, E-, J-, G-), mantenerlo
    if cedula[0] in ['V', 'E', 'J', 'G'] and len(cedula) > 1 and cedula[1] == '-':
        return cedula
    
    # Si no tiene prefijo, agregar V-
    return f"V-{cedula}"


def validar_datos_exportacion(datos: dict, campos_requeridos: list) -> tuple[bool, str]:
    """
    Valida que los datos tengan los campos requeridos para exportación.
    
    Args:
        datos: Dict con datos a validar
        campos_requeridos: Lista de campos que deben existir
        
    Returns:
        Tuple (es_válido, mensaje_error)
    """
    if not datos:
        return False, "No se proporcionaron datos"
    
    campos_faltantes = []
    for campo in campos_requeridos:
        if campo not in datos or datos[campo] is None or str(datos[campo]).strip() == "":
            campos_faltantes.append(campo)
    
    if campos_faltantes:
        return False, f"Faltan campos requeridos: {', '.join(campos_faltantes)}"
    
    return True, "Datos válidos"


# FUNCIONES DE ENCABEZADO Y PIE DE PÁGINA

def draw_centered(canvas, text, y, font="Helvetica", size=12):
    """Dibuja texto centrado en el canvas."""
    canvas.setFont(font, size)
    text_width = canvas.stringWidth(text, font, size)
    x_center = (page_width - text_width) / 2
    canvas.drawString(x_center, y, text)


def encabezado(canvas, doc, institucion_id=1):
    """
    Dibuja el encabezado con logo e institución en cada página del PDF.
    """
    logo_path = os.path.join(ICON_DIR, "logo_escuela_fondo.png")
    
    # Verificar que el logo existe
    if not os.path.exists(logo_path):
        print(f"Advertencia: Logo no encontrado en {logo_path}")
        # Continuar sin logo
    else:
        # Dimensiones del logo
        logo_width = 65
        logo_height = 60

        # Coordenadas
        x_center = (page_width - logo_width) / 2
        y_position = page_height - 180

        try:
            canvas.drawImage(
                logo_path,
                x=x_center,
                y=y_position,
                width=logo_width,
                height=logo_height,
                preserveAspectRatio=True
            )
        except Exception as e:
            print(f"Error dibujando logo: {e}")

    # Obtener datos de institución
    institucion = InstitucionModel.obtener_por_id(institucion_id)

    if institucion:
        nombre = str(institucion.get("nombre", "")).upper()
        codigo = str(institucion.get("codigo_dea", ""))

        draw_centered(canvas, "REPÚBLICA BOLIVARIANA DE VENEZUELA", page_height - 50, "Helvetica", 10)
        draw_centered(canvas, "MINISTERIO DEL PODER POPULAR PARA LA EDUCACIÓN", page_height - 65, "Helvetica", 10)
        draw_centered(canvas, nombre, page_height - 80, "Helvetica", 10)
        draw_centered(canvas, f"CÓDIGO DEA: {codigo}", page_height - 95, "Helvetica", 10)
        draw_centered(canvas, "PUERTO LA CRUZ, EDO. ANZOÁTEGUI", page_height - 110, "Helvetica", 10)
    else:
        canvas.setFont("Helvetica-Bold", 12)
        fallback = "Institución no encontrada"
        text_width = canvas.stringWidth(fallback, "Helvetica-Bold", 12)
        x_center = (page_width - text_width) / 2
        canvas.drawString(x_center, page_height - 50, fallback)


def pie_pagina(canvas, doc, institucion_id=1):
    """
    Dibuja el pie de página con datos de la institución.
    """
    institucion = InstitucionModel.obtener_por_id(institucion_id)

    font_name = "Helvetica"
    font_size = 10
    canvas.setFont(font_name, font_size)

    if institucion:
        direccion = str(institucion.get("direccion", "")).upper()
        telefono = str(institucion.get("telefono", ""))
        correo = str(institucion.get("correo", "")).upper()

        line1 = f"DIRECCIÓN: {direccion}" if direccion else ""
        line2 = f"TELÉFONO: {telefono} | CORREO: {correo}" if telefono or correo else ""
    else:
        line1 = ""
        line2 = ""

    for i, line in enumerate([line1, line2]):
        if line.strip():
            text_width = canvas.stringWidth(line, font_name, font_size)
            x_center = (page_width - text_width) / 2
            y_pos = 45 - i * (font_size + 2)
            canvas.drawString(x_center, y_pos, line)


def encabezado_y_pie(canvas, doc):
    """
    Combina encabezado y pie de página.
    """
    encabezado(canvas, doc)
    pie_pagina(canvas, doc)


# FORMATOS ESTUDIANTES

def generar_constancia_estudios(estudiante: dict, institucion: dict) -> str:
    """
    Genera constancia de estudios para un estudiante.
    
    Args:
        estudiante: Dict con datos del estudiante
        institucion: Dict con datos de la institución
        
    Returns:
        Ruta del archivo generado
        
    Raises:
        ValueError: Si faltan datos requeridos
        IOError: Si hay error escribiendo el archivo
    """
    # Validar datos requeridos
    campos_est = ["Nombres", "Apellidos", "Cédula", "Grado", "Sección"]
    valido, mensaje = validar_datos_exportacion(estudiante, campos_est)
    if not valido:
        raise ValueError(f"Datos de estudiante incompletos: {mensaje}")
    
    campos_inst = ["director", "director_ci", "nombre"]
    valido, mensaje = validar_datos_exportacion(institucion, campos_inst)
    if not valido:
        raise ValueError(f"Datos de institución incompletos: {mensaje}")
    
    # Normalizar datos
    estudiante["Nombres"] = str(estudiante["Nombres"]).strip().upper()
    estudiante["Apellidos"] = str(estudiante["Apellidos"]).strip().upper()
    cedula_normalizada = normalizar_cedula(estudiante["Cédula"])
    
    # Crear carpeta
    carpeta = os.path.join(os.getcwd(), "exportados", "Constancias de estudios")
    ok, msg = crear_carpeta_segura(carpeta)
    if not ok:
        raise IOError(msg)

    # Nombre de archivo sanitizado
    nombre_base = sanitizar_nombre_archivo(f"Constancia_{estudiante['Cédula']}")
    nombre_archivo = os.path.join(carpeta, f"{nombre_base}.pdf")

    try:
        doc = SimpleDocTemplate(
            nombre_archivo,
            pagesize=letter,
            leftMargin=80,
            rightMargin=80,
            topMargin=180,
            bottomMargin=50
        )

        story = []

        # Título
        story.append(Paragraph("CONSTANCIA DE ESTUDIOS", styles["Title"]))
        story.append(Spacer(1, 16))

        # Texto principal
        director_ci = normalizar_cedula(institucion['director_ci'])
        texto = (
            f"El suscrito, Director <b>PROF. {institucion['director'].upper()}</b>, portador de la Cédula de Identidad "
            f"<b>{director_ci}</b>, de {institucion['nombre']}, hace constar que el(la) estudiante "
            f"<b>{estudiante['Apellidos']} {estudiante['Nombres']}</b>, "
            f"portador de la cédula escolar <b>CE-{cedula_normalizada}</b>, cursa actualmente el grado "
            f"<b>{estudiante['Grado']} Sección '{estudiante['Sección']}'</b> de Educación Primaria en esta institución.<br/><br/>"
        )
        story.append(Paragraph(texto, justificado))
        story.append(Spacer(1, 40))

        # Fecha
        fecha_hoy = date.today().strftime("%d/%m/%Y")
        texto_fecha = (
            "Constancia que se expide a petición de la parte interesada en la Ciudad de Puerto La Cruz, "
            f"a la fecha {fecha_hoy}."
        )
        story.append(Paragraph(texto_fecha, justificado))
        story.append(Spacer(1, 100))

        # Firma
        firma = f"________________________<br/>Prof. {institucion['director']}"
        story.append(Paragraph(firma, centrado))
        story.append(Spacer(1, 3))
        story.append(Paragraph(f"C.I. {director_ci}", centrado))
        story.append(Spacer(1, 3))
        story.append(Paragraph("Director", centrado))

        # Construir PDF
        doc.build(story, onFirstPage=encabezado_y_pie, onLaterPages=encabezado_y_pie)
        return nombre_archivo
        
    except Exception as e:
        raise IOError(f"Error generando PDF: {e}")


def generar_buena_conducta(estudiante: dict, institucion: dict, año_escolar: dict) -> str:
    """
    Genera constancia de buena conducta para un estudiante.
    
    Args:
        estudiante: Dict con datos del estudiante
        institucion: Dict con datos de la institución
        año_escolar: Dict con datos del año escolar
        
    Returns:
        Ruta del archivo generado
        
    Raises:
        ValueError: Si faltan datos requeridos
        IOError: Si hay error escribiendo el archivo
    """
    # Validar datos
    campos_est = ["Nombres", "Apellidos", "Cédula", "Grado", "Sección"]
    valido, mensaje = validar_datos_exportacion(estudiante, campos_est)
    if not valido:
        raise ValueError(f"Datos de estudiante incompletos: {mensaje}")
    
    campos_inst = ["director", "director_ci", "nombre"]
    valido, mensaje = validar_datos_exportacion(institucion, campos_inst)
    if not valido:
        raise ValueError(f"Datos de institución incompletos: {mensaje}")
    
    # Extraer años
    año_inicio, año_fin = extraer_año_escolar(año_escolar)
    
    # Normalizar datos
    estudiante["Nombres"] = str(estudiante["Nombres"]).strip().upper()
    estudiante["Apellidos"] = str(estudiante["Apellidos"]).strip().upper()
    cedula_normalizada = normalizar_cedula(estudiante["Cédula"])

    # Crear carpeta
    carpeta = os.path.join(os.getcwd(), "exportados", "Constancias de buena conducta")
    ok, msg = crear_carpeta_segura(carpeta)
    if not ok:
        raise IOError(msg)

    nombre_base = sanitizar_nombre_archivo(f"Constancia_buena_conducta_{estudiante['Cédula']}")
    nombre_archivo = os.path.join(carpeta, f"{nombre_base}.pdf")

    try:
        doc = SimpleDocTemplate(
            nombre_archivo,
            pagesize=letter,
            leftMargin=80,
            rightMargin=80,
            topMargin=180,
            bottomMargin=50
        )

        story = []

        # Título
        story.append(Paragraph("CONSTANCIA DE BUENA CONDUCTA", styles["Title"]))
        story.append(Spacer(1, 16))

        # Texto principal
        director_ci = normalizar_cedula(institucion['director_ci'])
        texto = (
            f"El suscrito, Director <b>PROF. {institucion['director'].upper()}</b>, portador de la Cédula de Identidad "
            f"<b>{director_ci}</b>, de {institucion['nombre']}, que funciona en Puerto La Cruz, "
            f"hace constar que el alumno(a): <b>{estudiante['Apellidos']} {estudiante['Nombres']}</b>, "
            f"portador de la cédula de identidad <b>CE-{cedula_normalizada}</b>, estudiante del "
            f"<b>{estudiante['Grado']} Grado Sección '{estudiante['Sección']}'</b> "
            f"de Educación Primaria durante el Año Escolar {año_inicio}-{año_fin}, mantuvo una "
            f"<b>Buena Conducta</b> durante su permanencia en esta institución educativa.<br/><br/>"
        )
        story.append(Paragraph(texto, justificado))
        story.append(Spacer(1, 40))

        # Fecha
        fecha_hoy = date.today().strftime("%d/%m/%Y")
        texto_fecha = (
            "Constancia que se expide a petición de la parte interesada en la Ciudad de Puerto La Cruz, "
            f"a la fecha {fecha_hoy}."
        )
        story.append(Paragraph(texto_fecha, justificado))
        story.append(Spacer(1, 100))

        # Firma
        firma = f"________________________<br/>Prof. {institucion['director']}"
        story.append(Paragraph(firma, centrado))
        story.append(Spacer(1, 3))
        story.append(Paragraph(f"C.I. {director_ci}", centrado))
        story.append(Spacer(1, 3))
        story.append(Paragraph("Director", centrado))

        # Construir PDF
        doc.build(story, onFirstPage=encabezado_y_pie, onLaterPages=encabezado_y_pie)
        return nombre_archivo
        
    except Exception as e:
        raise IOError(f"Error generando PDF: {e}")


def generar_constancia_inscripcion(estudiante: dict, institucion: dict) -> str:
    """
    Genera constancia de inscripción para un estudiante.
    
    Args:
        estudiante: Dict con datos del estudiante
        institucion: Dict con datos de la institución
        
    Returns:
        Ruta del archivo generado
        
    Raises:
        ValueError: Si faltan datos requeridos
        IOError: Si hay error escribiendo el archivo
    """
    # Validar datos
    campos_est = ["Nombres", "Apellidos", "Cédula", "Grado", "Ciudad", "Fecha Nac.", "Fecha Ingreso"]
    valido, mensaje = validar_datos_exportacion(estudiante, campos_est)
    if not valido:
        raise ValueError(f"Datos de estudiante incompletos: {mensaje}")
    
    campos_inst = ["director", "director_ci"]
    valido, mensaje = validar_datos_exportacion(institucion, campos_inst)
    if not valido:
        raise ValueError(f"Datos de institución incompletos: {mensaje}")
    
    # Normalizar datos
    estudiante["Nombres"] = str(estudiante["Nombres"]).strip().upper()
    estudiante["Apellidos"] = str(estudiante["Apellidos"]).strip().upper()
    cedula_normalizada = normalizar_cedula(estudiante["Cédula"])
    
    # Convertir fechas
    fecha_nac_str = convertir_fecha_string(estudiante['Fecha Nac.'])
    fecha_ingreso_str = convertir_fecha_string(estudiante['Fecha Ingreso'])
    
    # Calcular edad
    try:
        fecha_nac = estudiante['Fecha Nac.']
        if isinstance(fecha_nac, (date, datetime)):
            edad = calcular_edad(fecha_nac)
        else:
            try:
                fecha_obj = datetime.strptime(fecha_nac_str, "%d/%m/%Y").date()
                edad = calcular_edad(fecha_obj)
            except:
                edad = "N/A"
    except:
        edad = "N/A"

    # Crear carpeta
    carpeta = os.path.join(os.getcwd(), "exportados", "Constancias de inscripcion")
    ok, msg = crear_carpeta_segura(carpeta)
    if not ok:
        raise IOError(msg)

    nombre_base = sanitizar_nombre_archivo(f"Constancia_inscripcion_{estudiante['Cédula']}")
    nombre_archivo = os.path.join(carpeta, f"{nombre_base}.pdf")

    try:
        doc = SimpleDocTemplate(
            nombre_archivo,
            pagesize=letter,
            leftMargin=80,
            rightMargin=80,
            topMargin=180,
            bottomMargin=50
        )

        story = []

        # Título
        story.append(Paragraph("CONSTANCIA DE INSCRIPCIÓN", styles["Title"]))
        story.append(Spacer(1, 16))

        # Texto principal
        texto = (
            f"La Dirección del plantel hace constar mediante la presente, que el Alumno(a): "
            f"<b>{estudiante['Apellidos']} {estudiante['Nombres']}</b>, nacido en {estudiante['Ciudad']} "
            f"en fecha {fecha_nac_str}, de {edad} años de edad, fué inscrito "
            f"en esta institución el día {fecha_ingreso_str} para cursar el <b>{estudiante['Grado']} Grado</b> "
            f"de Educación Primaria."
        )
        story.append(Paragraph(texto, justificado))
        story.append(Spacer(1, 40))

        # Fecha
        fecha_hoy = date.today().strftime("%d/%m/%Y")
        texto_fecha = (
            "Constancia que se expide a petición de la parte interesada en la Ciudad de Puerto La Cruz, "
            f"a la fecha {fecha_hoy}."
        )
        story.append(Paragraph(texto_fecha, justificado))
        story.append(Spacer(1, 100))

        # Firma
        director_ci = normalizar_cedula(institucion['director_ci'])
        firma = f"________________________<br/>Prof. {institucion['director']}"
        story.append(Paragraph(firma, centrado))
        story.append(Spacer(1, 3))
        story.append(Paragraph(f"C.I. {director_ci}", centrado))
        story.append(Spacer(1, 3))
        story.append(Paragraph("Director", centrado))

        # Construir PDF
        doc.build(story, onFirstPage=encabezado_y_pie, onLaterPages=encabezado_y_pie)
        return nombre_archivo
        
    except Exception as e:
        raise IOError(f"Error generando PDF: {e}")


def generar_constancia_prosecucion_inicial(estudiante: dict, institucion: dict, año_escolar: dict) -> str:
    """
    Genera constancia de prosecución de educación inicial a primaria.
    
    Args:
        estudiante: Dict con datos del estudiante
        institucion: Dict con datos de la institución
        año_escolar: Dict con datos del año escolar
        
    Returns:
        Ruta del archivo generado
        
    Raises:
        ValueError: Si faltan datos requeridos
        IOError: Si hay error escribiendo el archivo
    """
    # Validar datos
    campos_est = ["Nombres", "Apellidos", "Cédula", "Ciudad", "Fecha Nac."]
    valido, mensaje = validar_datos_exportacion(estudiante, campos_est)
    if not valido:
        raise ValueError(f"Datos de estudiante incompletos: {mensaje}")
    
    campos_inst = ["director", "director_ci", "nombre"]
    valido, mensaje = validar_datos_exportacion(institucion, campos_inst)
    if not valido:
        raise ValueError(f"Datos de institución incompletos: {mensaje}")
    
    # Extraer años
    año_inicio, año_fin = extraer_año_escolar(año_escolar)
    
    # Normalizar datos
    estudiante["Nombres"] = str(estudiante["Nombres"]).strip().upper()
    estudiante["Apellidos"] = str(estudiante["Apellidos"]).strip().upper()
    cedula_normalizada = normalizar_cedula(estudiante["Cédula"])
    
    # Convertir fecha
    fecha_nac_str = convertir_fecha_string(estudiante['Fecha Nac.'])
    
    # Crear carpeta
    carpeta = os.path.join(os.getcwd(), "exportados", "Constancias de prosecucion")
    ok, msg = crear_carpeta_segura(carpeta)
    if not ok:
        raise IOError(msg)

    nombre_base = sanitizar_nombre_archivo(f"Constancia_prosecucion_{estudiante['Cédula']}")
    nombre_archivo = os.path.join(carpeta, f"{nombre_base}.pdf")

    try:
        doc = SimpleDocTemplate(
            nombre_archivo,
            pagesize=letter,
            leftMargin=80,
            rightMargin=80,
            topMargin=180,
            bottomMargin=50
        )

        story = []

        # Título
        story.append(Paragraph("CONSTANCIA DE PROSECUCIÓN", styles["Title"]))
        story.append(Spacer(1, 16))

        # Texto principal
        director_ci = normalizar_cedula(institucion['director_ci'])
        texto = (
            f"Quien suscribe <b>{institucion['director'].upper()}</b> titular de la Cédula de Identidad "
            f"Nº <b>{director_ci}</b> Director(a) de la Institución Educativa "
            f"<b>{institucion['nombre'].upper()}</b>, ubicada en el Municipio JUAN ANTONIO SOTILLO de la Parroquia "
            f"PUERTO LA CRUZ adscrita al Centro de Desarrollo de la Calidad Educativa Estadal ANZOÁTEGUI. "
            f"Por la presente certifica que el (la) estudiante <b>{estudiante['Apellidos']} {estudiante['Nombres']}</b> "
            f"titular de Cédula Escolar <b>CE-{cedula_normalizada}</b>, nacido (a) en {estudiante['Ciudad']} "
            f"del Estado ANZOÁTEGUI en fecha <b>{fecha_nac_str}</b>, cursó el <b>3er nivel</b> de la etapa de "
            f"<b>Educación Inicial</b> durante el periodo escolar <b>{año_inicio}-{año_fin}</b>, siendo "
            f"promovido(a) a <b>primer grado de primaria</b>, previo cumplimiento a los requisitos establecidos "
            f"en la normativa legal vigente."
        )
        story.append(Paragraph(texto, justificado))
        story.append(Spacer(1, 40))

        # Fecha
        fecha_hoy = date.today().strftime("%d/%m/%Y")
        texto_fecha = f"Certificado que expide en Puerto La Cruz a la fecha {fecha_hoy}"
        story.append(Paragraph(texto_fecha, justificado))
        story.append(Spacer(1, 100))

        # Firma
        firma = f"________________________<br/>Prof. {institucion['director']}"
        story.append(Paragraph(firma, centrado))
        story.append(Spacer(1, 3))
        story.append(Paragraph(f"C.I. {director_ci}", centrado))
        story.append(Spacer(1, 3))
        story.append(Paragraph("Director", centrado))

        # Construir PDF
        doc.build(story, onFirstPage=encabezado_y_pie, onLaterPages=encabezado_y_pie)
        return nombre_archivo
        
    except Exception as e:
        raise IOError(f"Error generando PDF: {e}")


# FORMATOS EMPLEADOS

def generar_constancia_trabajo(empleado: dict, institucion: dict) -> str:
    """
    Genera constancia de trabajo para un empleado.
    
    Args:
        empleado: Dict con datos del empleado
        institucion: Dict con datos de la institución
        
    Returns:
        Ruta del archivo generado
        
    Raises:
        ValueError: Si faltan datos requeridos
        IOError: Si hay error escribiendo el archivo
    """
    # Validar datos
    campos_emp = ["Nombres", "Apellidos", "Cédula", "Cargo", "Fecha Ingreso"]
    valido, mensaje = validar_datos_exportacion(empleado, campos_emp)
    if not valido:
        raise ValueError(f"Datos de empleado incompletos: {mensaje}")
    
    campos_inst = ["director", "director_ci", "nombre"]
    valido, mensaje = validar_datos_exportacion(institucion, campos_inst)
    if not valido:
        raise ValueError(f"Datos de institución incompletos: {mensaje}")
    
    # Normalizar datos
    empleado["Nombres"] = str(empleado["Nombres"]).strip().upper()
    empleado["Apellidos"] = str(empleado["Apellidos"]).strip().upper()
    cedula_normalizada = normalizar_cedula(empleado["Cédula"])
    
    # Convertir fecha
    fecha_ingreso_str = convertir_fecha_string(empleado['Fecha Ingreso'])
    
    # Crear carpeta
    carpeta = os.path.join(os.getcwd(), "exportados", "Constancias de trabajo")
    ok, msg = crear_carpeta_segura(carpeta)
    if not ok:
        raise IOError(msg)

    nombre_base = sanitizar_nombre_archivo(f"ConstanciaTrabajo_{empleado['Cédula']}")
    nombre_archivo = os.path.join(carpeta, f"{nombre_base}.pdf")

    try:
        doc = SimpleDocTemplate(
            nombre_archivo,
            pagesize=letter,
            leftMargin=80,
            rightMargin=80,
            topMargin=180,
            bottomMargin=50
        )

        story = []

        # Título
        story.append(Paragraph("CONSTANCIA DE TRABAJO", styles["Title"]))
        story.append(Spacer(1, 16))

        # Texto principal
        director_ci = normalizar_cedula(institucion['director_ci'])
        texto = (
            f"Quien suscribe, {institucion['director']} Cédula de identidad {director_ci} "
            f"Director(a) de la {institucion['nombre']} hace constar "
            f"por medio de la presente que la ciudadana {empleado['Nombres']} {empleado['Apellidos']}, Cédula de Identidad "
            f"{cedula_normalizada} presta su servicio como {empleado['Cargo']} en esta institución desde "
            f"el {fecha_ingreso_str} hasta la presente fecha."
        )
        story.append(Paragraph(texto, justificado))
        story.append(Spacer(1, 40))

        # Fecha
        fecha_hoy = date.today().strftime("%d/%m/%Y")
        texto_fecha = (
            "Constancia que se expide a petición de la parte interesada en la ciudad de Puerto La Cruz, "
            f"a la fecha {fecha_hoy}."
        )
        story.append(Paragraph(texto_fecha, justificado))
        story.append(Spacer(1, 100))

        # Firma
        firma = f"________________________<br/>Prof. {institucion['director']}"
        story.append(Paragraph(firma, centrado))
        story.append(Spacer(1, 3))
        story.append(Paragraph(f"C.I. {director_ci}", centrado))
        story.append(Spacer(1, 3))
        story.append(Paragraph("Director", centrado))

        # Construir PDF
        doc.build(story, onFirstPage=encabezado_y_pie, onLaterPages=encabezado_y_pie)
        return nombre_archivo
        
    except Exception as e:
        raise IOError(f"Error generando PDF: {e}")


# REPORTES Y EXPORTACIONES

def exportar_reporte_pdf(parent, figure, titulo, criterio, etiquetas, valores, total) -> str:
    """
    Exporta un reporte estadístico a PDF con gráfica y tabla.
    
    Args:
        parent: Widget padre para el diálogo
        figure: Figura matplotlib con la gráfica
        titulo: Título del reporte
        criterio: Criterio usado para el reporte
        etiquetas: Lista de etiquetas de categorías
        valores: Lista de valores numéricos
        total: Total general
        
    Returns:
        Ruta del archivo generado o None si se canceló
    """
    try:
        sugerido = f"reporte_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        
        ruta, _ = QFileDialog.getSaveFileName(
            parent,
            "Guardar reporte",
            sugerido,
            "PDF Files (*.pdf)"
        )
        
        if not ruta:
            return None
            
        if not ruta.endswith(".pdf"):
            ruta += ".pdf"

        # Guardar la figura en memoria
        buf = io.BytesIO()
        figure.savefig(buf, format="png", bbox_inches="tight", dpi=150)
        buf.seek(0)

        # Documento
        doc = SimpleDocTemplate(
            ruta,
            pagesize=letter,
            leftMargin=80,
            rightMargin=80,
            topMargin=180,
            bottomMargin=50
        )
        
        story = []

        # Título y fecha
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
        story.append(Paragraph(f"<b>{titulo}</b>", styles["Title"]))
        story.append(Spacer(1, 10))
        story.append(Paragraph(f"Fecha de generación: {fecha}", styles["Normal"]))
        story.append(Spacer(1, 20))

        # Descripción
        descripcion = (
            f"Este reporte presenta un análisis de los estudiantes según el criterio "
            f"<b>{criterio}</b>. La gráfica y la tabla muestran la distribución de los datos "
            f"y el total general de registros considerados."
        )
        story.append(Paragraph(descripcion, justificado))
        story.append(Spacer(1, 20))

        # Tabla de datos
        data = [["Categoría", "Cantidad"]]
        for e, v in zip(etiquetas, valores):
            data.append([str(e), str(v)])
        data.append(["Total", str(total)])

        table = Table(data, hAlign="CENTER", colWidths=[200, 100])
        table.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#4F81BD")),
            ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
            ("ALIGN", (0,0), (-1,-1), "CENTER"),
            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
            ("GRID", (0,0), (-1,-1), 0.5, colors.black),
            ("BACKGROUND", (0,-1), (-1,-1), colors.lightgrey),
            ("FONTNAME", (0,-1), (-1,-1), "Helvetica-Bold"),
        ]))
        story.append(table)
        story.append(Spacer(1, 20))

        # Imagen de la gráfica
        story.append(Image(buf, width=400, height=300))
        story.append(Spacer(1, 10))

        # Observaciones
        story.append(Paragraph("<b>Observaciones:</b>", styles["Normal"]))
        story.append(Spacer(1, 12))
        for _ in range(3):
            story.append(Paragraph("_________________________________________________________", styles["Normal"]))
            story.append(Spacer(1, 12))

        # Construir PDF
        doc.build(story, onFirstPage=encabezado_y_pie, onLaterPages=encabezado_y_pie)
        buf.close()
        
        return ruta
        
    except Exception as e:
        if parent:
            crear_msgbox(
                parent,
                "Error",
                f"No se pudo exportar el reporte: {e}",
                QMessageBox.Critical
            ).exec()
        return None


def exportar_tabla_excel(nombre_archivo: str, encabezados: list, filas: list) -> str:
    """
    Exporta datos tabulares a un archivo Excel.
    
    Args:
        nombre_archivo: Ruta completa del archivo
        encabezados: Lista de nombres de columnas
        filas: Lista de listas con los datos
        
    Returns:
        Ruta del archivo generado
        
    Raises:
        IOError: Si hay error escribiendo el archivo
    """
    try:
        wb = Workbook()
        ws = wb.active
        ws.title = "Datos"

        # Escribir encabezados
        ws.append(encabezados)

        # Escribir filas (convertir objetos date/datetime a strings)
        for fila in filas:
            fila_procesada = []
            for celda in fila:
                if isinstance(celda, (date, datetime)):
                    fila_procesada.append(celda.strftime("%d/%m/%Y"))
                elif celda is None:
                    fila_procesada.append("")
                else:
                    fila_procesada.append(str(celda))
            ws.append(fila_procesada)

        # Guardar archivo
        wb.save(nombre_archivo)
        return nombre_archivo
        
    except Exception as e:
        raise IOError(f"Error generando archivo Excel: {e}")


def exportar_estudiantes_excel(parent, estudiantes: list) -> str:
    """
    Exporta lista de estudiantes a Excel.
    
    Args:
        parent: Widget padre para el diálogo
        estudiantes: Lista de diccionarios con datos de estudiantes
        
    Returns:
        Ruta del archivo generado o None si se canceló
    """
    if not estudiantes:
        if parent:
            crear_msgbox(
                parent,
                "Sin datos",
                "No hay estudiantes para exportar.",
                QMessageBox.Warning
            ).exec()
        return None

    try:
        sugerido = f"estudiantes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"

        ruta, _ = QFileDialog.getSaveFileName(
            parent,
            "Guardar reporte de estudiantes",
            sugerido,
            "Archivos Excel (*.xlsx)"
        )
        
        if not ruta:
            return None
            
        if not ruta.endswith(".xlsx"):
            ruta += ".xlsx"

        encabezados = list(estudiantes[0].keys())
        filas = [list(e.values()) for e in estudiantes]

        return exportar_tabla_excel(ruta, encabezados, filas)
        
    except Exception as e:
        if parent:
            crear_msgbox(
                parent,
                "Error",
                f"No se pudo exportar a Excel: {e}",
                QMessageBox.Critical
            ).exec()
        return None


def exportar_empleados_excel(parent, empleados: list) -> str:
    """
    Exporta lista de empleados a Excel.
    
    Args:
        parent: Widget padre para el diálogo
        empleados: Lista de diccionarios con datos de empleados
        
    Returns:
        Ruta del archivo generado o None si se canceló
    """
    if not empleados:
        if parent:
            crear_msgbox(
                parent,
                "Sin datos",
                "No hay empleados para exportar.",
                QMessageBox.Warning
            ).exec()
        return None

    try:
        sugerido = f"empleados_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"

        ruta, _ = QFileDialog.getSaveFileName(
            parent,
            "Guardar reporte de empleados",
            sugerido,
            "Archivos Excel (*.xlsx)"
        )
        
        if not ruta:
            return None
            
        if not ruta.endswith(".xlsx"):
            ruta += ".xlsx"

        encabezados = list(empleados[0].keys())
        filas = [list(e.values()) for e in empleados]

        return exportar_tabla_excel(ruta, encabezados, filas)
        
    except Exception as e:
        if parent:
            crear_msgbox(
                parent,
                "Error",
                f"No se pudo exportar a Excel: {e}",
                QMessageBox.Critical
            ).exec()
        return None


def generar_certificado_promocion_sexto(estudiante: dict, institucion: dict, año_escolar_egreso: str) -> str:
    """
    Genera certificado de promoción de 6to grado a 1er año de secundaria.
    Solo para estudiantes egresados que completaron 6to grado en esta institución.
    
    Args:
        estudiante: Dict con datos del estudiante
        institucion: Dict con datos de la institución
        año_escolar_egreso: String con formato "2023/2024"
        
    Returns:
        Ruta del archivo generado
        
    Raises:
        ValueError: Si faltan datos requeridos
        IOError: Si hay error escribiendo el archivo
    """
    # Validar datos
    campos_est = ["Nombres", "Apellidos", "Cédula", "Ciudad", "Fecha Nac."]
    valido, mensaje = validar_datos_exportacion(estudiante, campos_est)
    if not valido:
        raise ValueError(f"Datos de estudiante incompletos: {mensaje}")
    
    campos_inst = ["director", "director_ci", "nombre"]
    valido, mensaje = validar_datos_exportacion(institucion, campos_inst)
    if not valido:
        raise ValueError(f"Datos de institución incompletos: {mensaje}")
    
    if not año_escolar_egreso:
        raise ValueError("Año escolar de egreso no proporcionado")
    
    # Normalizar datos
    estudiante["Nombres"] = str(estudiante["Nombres"]).strip().upper()
    estudiante["Apellidos"] = str(estudiante["Apellidos"]).strip().upper()
    cedula_normalizada = normalizar_cedula(estudiante["Cédula"])
    
    # Convertir fecha
    fecha_nac_str = convertir_fecha_string(estudiante['Fecha Nac.'])
    
    # Extraer año escolar (formato: "2023/2024" -> "2023-2024")
    año_periodo = str(año_escolar_egreso).replace('/', '-')
    
    # Crear carpeta
    carpeta = os.path.join(os.getcwd(), "exportados", "Certificados de promocion")
    ok, msg = crear_carpeta_segura(carpeta)
    if not ok:
        raise IOError(msg)

    nombre_base = sanitizar_nombre_archivo(f"Certificado_promocion_{estudiante['Cédula']}")
    nombre_archivo = os.path.join(carpeta, f"{nombre_base}.pdf")

    try:
        doc = SimpleDocTemplate(
            nombre_archivo,
            pagesize=letter,
            leftMargin=80,
            rightMargin=80,
            topMargin=180,
            bottomMargin=50
        )

        story = []

        # Título
        story.append(Paragraph("CERTIFICADO DE PROMOCIÓN", styles["Title"]))
        story.append(Spacer(1, 16))

        # Texto principal
        director_ci = normalizar_cedula(institucion['director_ci'])
        ultima_seccion = estudiante.get('ultima_seccion', 'N/A')
        
        texto = (
            f"Quien suscribe <b>{institucion['director'].upper()}</b> titular de la Cédula de Identidad "
            f"Nº <b>{director_ci}</b> Director(a) de la Institución Educativa "
            f"<b>{institucion['nombre'].upper()}</b>, ubicada en el Municipio JUAN ANTONIO SOTILLO de la Parroquia "
            f"PUERTO LA CRUZ adscrita al Centro de Desarrollo de la Calidad Educativa Estadal ANZOÁTEGUI. "
            f"Por la presente certifica que el (la) estudiante <b>{estudiante['Apellidos']} {estudiante['Nombres']}</b> "
            f"titular de Cédula Escolar Nº <b>CE-{cedula_normalizada}</b>, nacido (a) en el Municipio "
            f"<b>{estudiante['Ciudad']}</b> del Estado ANZOÁTEGUI, en fecha <b>{fecha_nac_str}</b>, cursó el "
            f"<b>6to Grado</b> correspondiéndole el literal <b>{ultima_seccion}</b> "
            f"durante el periodo escolar <b>{año_periodo}</b>, siendo promovido(a) al <b>1er Año del Nivel de "
            f"Educación Media</b>, previo cumplimiento a los requisitos establecidos en la normativa legal vigente."
        )
        story.append(Paragraph(texto, justificado))
        story.append(Spacer(1, 40))

        # Fecha de expedición
        fecha_hoy = date.today()
        dia = fecha_hoy.day
        mes_nombre = fecha_hoy.strftime("%B").upper()
        meses = {
            'JANUARY': 'ENERO', 'FEBRUARY': 'FEBRERO', 'MARCH': 'MARZO',
            'APRIL': 'ABRIL', 'MAY': 'MAYO', 'JUNE': 'JUNIO',
            'JULY': 'JULIO', 'AUGUST': 'AGOSTO', 'SEPTEMBER': 'SEPTIEMBRE',
            'OCTOBER': 'OCTUBRE', 'NOVEMBER': 'NOVIEMBRE', 'DECEMBER': 'DICIEMBRE'
        }
        mes_es = meses.get(mes_nombre, mes_nombre)
        año = fecha_hoy.year
        
        texto_fecha = f"Certificado que se expide en PUERTO LA CRUZ, a los {dia} días del mes de {mes_es} de {año}"
        story.append(Paragraph(texto_fecha, justificado))
        story.append(Spacer(1, 100))

        # Firma
        firma = f"________________________<br/>Prof. {institucion['director']}"
        story.append(Paragraph(firma, centrado))
        story.append(Spacer(1, 3))
        story.append(Paragraph(f"C.I. {director_ci}", centrado))
        story.append(Spacer(1, 3))
        story.append(Paragraph("Director", centrado))

        # Construir PDF
        doc.build(story, onFirstPage=encabezado_y_pie, onLaterPages=encabezado_y_pie)
        return nombre_archivo
        
    except Exception as e:
        raise IOError(f"Error generando PDF: {e}")

def generar_constancia_retiro(estudiante: dict, institucion: dict, año_escolar: dict, motivo_retiro: str = None) -> str:
    """
    Genera constancia de retiro para un estudiante que sale de la institución.
    
    Args:
        estudiante: Dict con datos del estudiante
        institucion: Dict con datos de la institución
        año_escolar: Dict con datos del año escolar
        motivo_retiro: Motivo del retiro (opcional)
        
    Returns:
        Ruta del archivo generado
        
    Raises:
        ValueError: Si faltan datos requeridos
        IOError: Si hay error escribiendo el archivo
    """
    # Validar datos
    campos_est = ["Nombres", "Apellidos", "Cédula", "Grado", "Ciudad", "Fecha Nac."]
    valido, mensaje = validar_datos_exportacion(estudiante, campos_est)
    if not valido:
        raise ValueError(f"Datos de estudiante incompletos: {mensaje}")
    
    campos_inst = ["director", "director_ci", "nombre"]
    valido, mensaje = validar_datos_exportacion(institucion, campos_inst)
    if not valido:
        raise ValueError(f"Datos de institución incompletos: {mensaje}")
    
    # Extraer años
    año_inicio, año_fin = extraer_año_escolar(año_escolar)
    
    # Normalizar datos
    estudiante["Nombres"] = str(estudiante["Nombres"]).strip().upper()
    estudiante["Apellidos"] = str(estudiante["Apellidos"]).strip().upper()
    cedula_normalizada = normalizar_cedula(estudiante["Cédula"])
    
    # Convertir fecha
    fecha_nac_str = convertir_fecha_string(estudiante['Fecha Nac.'])
    
    # Calcular edad
    try:
        if isinstance(estudiante['Fecha Nac.'], (date, datetime)):
            edad = calcular_edad(estudiante['Fecha Nac.'])
        else:
            fecha_obj = datetime.strptime(str(estudiante['Fecha Nac.']), "%d/%m/%Y").date()
            edad = calcular_edad(fecha_obj)
    except:
        edad = "N/A"
    
    # Motivo por defecto si no se proporciona
    if not motivo_retiro:
        motivo_retiro = "es retirado de la institución a solicitud de su representante siendo Promovido al siguiente grado"
    
    # Crear carpeta
    carpeta = os.path.join(os.getcwd(), "exportados", "Constancias de retiro")
    ok, msg = crear_carpeta_segura(carpeta)
    if not ok:
        raise IOError(msg)

    nombre_base = sanitizar_nombre_archivo(f"Constancia_retiro_{estudiante['Cédula']}")
    nombre_archivo = os.path.join(carpeta, f"{nombre_base}.pdf")

    try:
        doc = SimpleDocTemplate(
            nombre_archivo,
            pagesize=letter,
            leftMargin=80,
            rightMargin=80,
            topMargin=180,
            bottomMargin=50
        )

        story = []

        # Título
        story.append(Paragraph("CONSTANCIA DE RETIRO", styles["Title"]))
        story.append(Spacer(1, 20))

        # Texto principal
        director_ci = normalizar_cedula(institucion['director_ci'])
        
        # Determinar género para el artículo
        genero = estudiante.get("Género", "").lower()
        articulo = "el" if genero == "masculino" else "la"
        
        # Determinar si es nivel (Inicial) o grado (Primaria)
        tipo_educacion = estudiante.get("Tipo Educ.", "").lower()
        if "primaria" in tipo_educacion:
            grado_texto = f"{estudiante['Grado']} grado"
            
        texto = (
            f"La Dirección del plantel hace constar mediante la presente, que {articulo} Alumno(a): "
            f"<b>{estudiante['Apellidos']} {estudiante['Nombres']}</b>, "
            f"nacido(a) en <b>{estudiante['Ciudad'].upper()}</b> él <b>{fecha_nac_str}</b> "
            f"y de <b>{edad} año(s)</b> de edad, estudiante regular del <b>{grado_texto}</b> "
            f"para el año escolar <b>{año_inicio}-{año_fin}</b>, {motivo_retiro}.<br/><br/>"
        )
        story.append(Paragraph(texto, justificado))
        story.append(Spacer(1, 20))

        # Fecha actual
        fecha_hoy = date.today()
        dia = fecha_hoy.day
        mes_nombre = fecha_hoy.strftime("%B").upper()
        
        # Traducir mes al español
        meses = {
            'JANUARY': 'ENERO', 'FEBRUARY': 'FEBRERO', 'MARCH': 'MARZO',
            'APRIL': 'ABRIL', 'MAY': 'MAYO', 'JUNE': 'JUNIO',
            'JULY': 'JULIO', 'AUGUST': 'AGOSTO', 'SEPTEMBER': 'SEPTIEMBRE',
            'OCTOBER': 'OCTUBRE', 'NOVEMBER': 'NOVIEMBRE', 'DECEMBER': 'DICIEMBRE'
        }
        mes_es = meses.get(mes_nombre, mes_nombre)
        año = fecha_hoy.year
        
        texto_fecha = (
            f"Se expide constancia a solicitud de la parte interesada en Puerto La Cruz "
            f"a los <b>{dia}</b> días del mes de <b>{mes_es}</b> del año <b>{año}</b>."
        )
        story.append(Paragraph(texto_fecha, justificado))
        story.append(Spacer(1, 100))

        # Firma
        firma_texto = f"________________________<br/>Prof. {institucion['director']}"
        story.append(Paragraph(firma_texto, centrado))
        story.append(Spacer(1, 3))
        story.append(Paragraph(f"C.I. {director_ci}", centrado))
        story.append(Spacer(1, 3))
        story.append(Paragraph("Director", centrado))

        # Construir PDF
        doc.build(story, onFirstPage=encabezado_y_pie, onLaterPages=encabezado_y_pie)
        return nombre_archivo
        
    except Exception as e:
        raise IOError(f"Error generando PDF: {e}")
