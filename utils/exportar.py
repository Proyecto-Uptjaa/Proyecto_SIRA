import os
import io
from datetime import date, datetime

from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
)
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from utils.edad import calcular_edad

from PySide6.QtWidgets import QFileDialog

from paths import ICON_DIR
from models.institucion_model import InstitucionModel
from openpyxl import Workbook
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER

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

def draw_centered(canvas, text, y, font="Helvetica", size=12):
    canvas.setFont(font, size)
    text_width = canvas.stringWidth(text, font, size)
    x_center = (page_width - text_width) / 2
    canvas.drawString(x_center, y, text)

def encabezado(canvas, doc, institucion_id=1):
    """
    Dibuja el encabezado con logo e institución en cada página del PDF.
    """
    logo_path = os.path.join(ICON_DIR, "logo_escuela_fondo.png")
    
    page_width, page_height = letter
    
    # Dimensiones del logo
    logo_width = 65
    logo_height = 60

    # Coordenadas
    x_center = (page_width - logo_width) / 2
    y_position = page_height - 180

    canvas.drawImage(
        logo_path,
        x=x_center,
        y=y_position,
        width=logo_width,
        height=logo_height,
        preserveAspectRatio=True
    )

    # Obtener datos de institución
    institucion = InstitucionModel.obtener_por_id(institucion_id)

    if institucion:
        nombre = institucion["nombre"].upper()
        codigo = institucion["codigo_dea"]

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
    page_width, page_height = letter

    font_name = "Helvetica"
    font_size = 10
    canvas.setFont(font_name, font_size)

    if institucion:
        direccion = institucion["direccion"].upper()
        telefono = institucion["telefono"]
        correo = institucion["correo"].upper()

        line1 = f"DIRECCIÓN: {direccion}"
        line2 = f"TELÉFONO: {telefono} | CORREO: {correo}"
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


### FORMATOS ESTUDIANTES ###

def generar_constancia_estudios(estudiante: dict, institucion: dict) -> str:
    """
    Genera constancia de estudios para un estudiante.
    """
    estudiante["Nombres"] = estudiante["Nombres"].upper()
    estudiante["Apellidos"] = estudiante["Apellidos"].upper()
    
    carpeta = os.path.join(os.getcwd(), "exportados", "Constancias de estudios")
    os.makedirs(carpeta, exist_ok=True)

    nombre_archivo = os.path.join(carpeta, f"Constancia_{estudiante['Cédula']}.pdf")

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
    texto = (
        f"El suscrito, Director <b>PROF. {institucion['director'].upper()}</b>, portador de la Cédula de Identidad "
        f"<b>V-{institucion['director_ci']}</b>, de {institucion['nombre']}, hace constar que el(la) estudiante "
        f"<b>{estudiante['Apellidos']} {estudiante['Nombres']}</b>, "
        f"portador de la cédula escolar <b>CE-{estudiante['Cédula']}</b>, cursa actualmente el grado "
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

    story.append(Paragraph(f"C.I. V-{institucion['director_ci']}", centrado))
    story.append(Spacer(1, 3))

    story.append(Paragraph("Director", centrado))

    # Construir PDF
    doc.build(story, onFirstPage=encabezado_y_pie, onLaterPages=encabezado_y_pie)
    return nombre_archivo


def generar_buena_conducta(estudiante: dict, institucion: dict, año_escolar: dict) -> str:
    """
    Genera constancia de buena conducta para un estudiante.
    """
    # Extraer el año como entero
    if isinstance(año_escolar['anio_inicio'], (date, datetime)):
        año_inicio = año_escolar['anio_inicio'].year
    else:
        año_inicio = int(año_escolar['anio_inicio'])
    
    año_fin = año_inicio + 1
    
    estudiante["Nombres"] = estudiante["Nombres"].upper()
    estudiante["Apellidos"] = estudiante["Apellidos"].upper()

    carpeta = os.path.join(os.getcwd(), "exportados", "Constancias de buena conducta")
    os.makedirs(carpeta, exist_ok=True)

    nombre_archivo = os.path.join(carpeta, f"Constancia_buena_conducta_{estudiante['Cédula']}.pdf")

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
    texto = (
        f"El suscrito, Director <b>PROF. {institucion['director'].upper()}</b>, portador de la Cédula de Identidad "
        f"<b>V-{institucion['director_ci']}</b>, de {institucion['nombre']}, que funciona en Puerto La Cruz, "
        f"hace constar que el alumno(a): <b>{estudiante['Apellidos']} {estudiante['Nombres']}</b>, "
        f"portador de la cédula de identidad <b>CE-{estudiante['Cédula']}</b>, estudiante del "
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

    story.append(Paragraph(f"C.I. V-{institucion['director_ci']}", centrado))
    story.append(Spacer(1, 3))

    story.append(Paragraph("Director", centrado))

    # Construir PDF
    doc.build(story, onFirstPage=encabezado_y_pie, onLaterPages=encabezado_y_pie)
    return nombre_archivo

def generar_constancia_inscripcion(estudiante: dict, institucion: dict) -> str:
    """
    Genera constancia de inscripcion para un estudiante.
    """
    
    estudiante["Nombres"] = estudiante["Nombres"].upper()
    estudiante["Apellidos"] = estudiante["Apellidos"].upper()
    
    # Convertir fecha de nacimiento si es necesario
    fecha_nac = estudiante['Fecha Nac.']
    if isinstance(fecha_nac, (date, datetime)):
        fecha_nac_str = fecha_nac.strftime("%d/%m/%Y")
        edad = calcular_edad(fecha_nac)
    else:
        fecha_nac_str = str(fecha_nac)
        # Intentar parsear la fecha string para calcular edad
        try:
            fecha_obj = datetime.strptime(fecha_nac_str, "%d/%m/%Y").date()
            edad = calcular_edad(fecha_obj)
        except:
            edad = "N/A"
   
    # Convertir fecha de ingreso si es necesario
    fecha_ingreso = estudiante['Fecha Ingreso']
    if isinstance(fecha_ingreso, (date, datetime)):
        fecha_ingreso_str = fecha_ingreso.strftime("%d/%m/%Y")
    else:
        fecha_ingreso_str = str(fecha_ingreso)
    
    carpeta = os.path.join(os.getcwd(), "exportados", "Constancias de inscripcion")
    os.makedirs(carpeta, exist_ok=True)

    nombre_archivo = os.path.join(carpeta, f"Constancia_inscripcion_{estudiante['Cédula']}.pdf")

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
    firma = f"________________________<br/>Prof. {institucion['director']}"
    story.append(Paragraph(firma, centrado))
    story.append(Spacer(1, 3))

    story.append(Paragraph(f"C.I. V-{institucion['director_ci']}", centrado))
    story.append(Spacer(1, 3))

    story.append(Paragraph("Director", centrado))

    # Construir PDF
    doc.build(story, onFirstPage=encabezado_y_pie, onLaterPages=encabezado_y_pie)
    return nombre_archivo


### FORMATOS EMPLEADOS ###

def generar_constancia_trabajo(empleado: dict, institucion: dict) -> str:
    """
    Genera constancia de trabajo para un empleado.
    """
    empleado["Nombres"] = empleado["Nombres"].upper()
    empleado["Apellidos"] = empleado["Apellidos"].upper()
    
    carpeta = os.path.join(os.getcwd(), "exportados", "Constancias de trabajo")
    os.makedirs(carpeta, exist_ok=True)

    nombre_archivo = os.path.join(carpeta, f"ConstanciaTrabajo_{empleado['Cédula']}.pdf")

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

    # Convertir fecha si es necesario
    fecha_ingreso = empleado['Fecha Ingreso']
    if isinstance(fecha_ingreso, (date, datetime)):
        fecha_ingreso_str = fecha_ingreso.strftime("%d/%m/%Y")
    else:
        fecha_ingreso_str = str(fecha_ingreso)

    # Texto principal
    texto = (
        f"Quien suscribe, {institucion['director']} Cédula de identidad {institucion['director_ci']} "
        f"Director(a) de la {institucion['nombre']} hace constar "
        f"por medio de la presente que la ciudadana {empleado['Nombres']} {empleado['Apellidos']}, Cédula de Identidad "
        f"{empleado['Cédula']} presta su servicio como {empleado["Cargo"]} en esta institución desde "
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

    story.append(Paragraph(f"C.I. V-{institucion['director_ci']}", centrado))
    story.append(Spacer(1, 3))

    story.append(Paragraph("Director", centrado))

    # Construir PDF
    doc.build(story, onFirstPage=encabezado_y_pie, onLaterPages=encabezado_y_pie)
    return nombre_archivo


### REPORTES Y EXPORTACIONES ###

def exportar_reporte_pdf(parent, figure, titulo, criterio, etiquetas, valores, total):
    """
    Exporta un reporte estadístico a PDF con gráfica y tabla.
    """
    ruta, _ = QFileDialog.getSaveFileName(
        parent,
        "Guardar reporte",
        f"reporte_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
        "PDF Files (*.pdf)"
    )
    if not ruta:
        return
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


def exportar_tabla_excel(nombre_archivo: str, encabezados: list, filas: list) -> str:
    """
    Exporta datos tabulares a un archivo Excel.
    """
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
            else:
                fila_procesada.append(celda)
        ws.append(fila_procesada)

    # Guardar archivo
    wb.save(nombre_archivo)
    return nombre_archivo


def exportar_estudiantes_excel(parent, estudiantes: list) -> str:
    """
    Exporta lista de estudiantes a Excel.
    """
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

    if not estudiantes:
        return None

    encabezados = list(estudiantes[0].keys())
    filas = [list(e.values()) for e in estudiantes]

    return exportar_tabla_excel(ruta, encabezados, filas)


def exportar_empleados_excel(parent, empleados: list) -> str:
    """
    Exporta lista de empleados a Excel.
    """
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

    if not empleados:
        return None

    encabezados = list(empleados[0].keys())
    filas = [list(e.values()) for e in empleados]

    return exportar_tabla_excel(ruta, encabezados, filas)