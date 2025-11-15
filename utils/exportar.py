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

from PySide6.QtWidgets import QFileDialog   # 👈 cambio aquí

from paths import ICON_DIR
from models.institucion_model import InstitucionModel
from openpyxl import Workbook
from models.institucion_model import InstitucionModel
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
    x_center = (page_width - logo_width) / 2   # centrado horizontal
    y_position = page_height - 180             # ajusta según dónde quieras debajo del encabezado

    canvas.drawImage(
        logo_path,
        x=x_center,
        y=y_position,
        width=logo_width,
        height=logo_height,
        preserveAspectRatio=True
    )

    # --- Obtener datos de institución ---
    institucion = InstitucionModel.obtener_por_id(institucion_id)
    page_width, page_height = letter

    if institucion:
        nombre = institucion["nombre"].upper()
        codigo = institucion["codigo_dea"]
        direccion = institucion["direccion"]
        telefono = institucion["telefono"]
        correo = institucion["correo"]
        director = institucion["director"]

        draw_centered(canvas, "REPÚBLICA BOLIVARIANA DE VENEZUELA", page_height - 50, "Helvetica", 10)
        draw_centered(canvas, "MINISTERIO DEL PODER POPULAR PARA LA EDUCACIÓN", page_height - 65, "Helvetica", 10)
        draw_centered(canvas, nombre, page_height - 80, "Helvetica", 10)
        draw_centered(canvas, f"CÓDIGO DEA: {codigo}", page_height - 95, "Helvetica", 10)
        draw_centered(canvas, "PUERTO LA CRUZ, EDO. ANZOÁTEGUI", page_height - 110, "Helvetica", 10)


    else:
        # fallback si no encuentra institución
        canvas.setFont("Helvetica-Bold", 12)
        fallback = "Institución no encontrada"
        text_width = canvas.stringWidth(fallback, "Helvetica-Bold", 12)
        x_center = (page_width - text_width) / 2
        canvas.drawString(x_center, page_height - 50, fallback)

def pie_pagina(canvas, doc, institucion_id=1):
    # --- Obtener datos de institución ---
    institucion = InstitucionModel.obtener_por_id(institucion_id)
    page_width, page_height = letter

    # Texto del pie de página
    font_name = "Helvetica"
    font_size = 10
    canvas.setFont(font_name, font_size)

    if institucion:
        direccion = institucion["direccion"].upper()
        telefono = institucion["telefono"]
        correo = institucion["correo"].upper()

        # datos generales de la institución
        line1 = f"DIRECCIÓN: {direccion}"
        line2 = f"TELÉFONO: {telefono} | CORREO: {correo}"
    else:
        line1 = ""
        line2 = ""

    # Dibujar cada línea centrada
    for i, line in enumerate([line1, line2]):
        if line.strip():
            text_width = canvas.stringWidth(line, font_name, font_size)
            x_center = (page_width - text_width) / 2
            y_pos = 45 - i * (font_size + 2)  # separación proporcional al tamaño de fuente
            canvas.drawString(x_center, y_pos, line)

def encabezado_y_pie(canvas, doc):
    encabezado(canvas, doc)   # tu método genérico de encabezado
    pie_pagina(canvas, doc)   # tu método de pie de página

### FORMATOS ESTUDIANTES ###

def generar_constancia_estudios(estudiante: dict) -> str:
    estudiante["Nombres"], estudiante["Apellidos"] = estudiante["Nombres"].upper(), estudiante["Apellidos"].upper()
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

    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("CONSTANCIA DE ESTUDIO", styles["Title"]))
    story.append(Spacer(1, 20))

    texto = (
        f"Se hace constar que el(la) estudiante <b>{estudiante['Nombres']} {estudiante['Apellidos']}</b>, "
        f"titular de la cédula escolar <b>{estudiante['Cédula']}</b>, cursa actualmente el grado "
        f"<b>{estudiante['Grado']} sección {estudiante['Sección']}</b> en esta institución.<br/><br/>"
    )
    story.append(Paragraph(texto, styles["Normal"]))
    story.append(Spacer(1, 40))

    fecha_hoy = date.today().strftime("%d/%m/%Y")
    texto_fecha = (
        f"Constancia que se expide a petición de la parte interesada en la ciudad de Puerto La Cruz, "
        f"a la fecha {fecha_hoy}."
    )
    story.append(Paragraph(texto_fecha, styles["Normal"]))
    story.append(Spacer(1, 40))

    story.append(Paragraph("________________________<br/>Director(a)", styles["Normal"]))

    # Construir PDF con encabezado en todas las páginas
    doc.build(story, onFirstPage=encabezado, onLaterPages=encabezado)
    return nombre_archivo

def generar_buena_conducta(estudiante: dict, institucion: dict) -> str:
    estudiante["Nombres"] = estudiante["Nombres"].upper()
    estudiante["Apellidos"] = estudiante["Apellidos"].upper()

    carpeta = os.path.join(os.getcwd(), "exportados", "Constancias de buena conducta")
    os.makedirs(carpeta, exist_ok=True)

    nombre_archivo = os.path.join(carpeta, f"Constancia_buena_conducta_{estudiante['Cédula']}.pdf")

    # Obtener datos de institución
    nombre_inst = institucion.get("nombre", "la institución")

    doc = SimpleDocTemplate(
        nombre_archivo,
        pagesize=letter,
        leftMargin=80,
        rightMargin=80,
        topMargin=180,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()
    story = []

    # Título
    story.append(Paragraph("CONSTANCIA DE BUENA CONDUCTA", styles["Title"]))
    story.append(Spacer(1, 16))

    # Texto principal con datos de institución
    nombre_inst = institucion.get("nombre", "la institución")

    texto = (
        f"El suscrito, Director <b>PROF. {institucion['director'].upper()}</b>, portador de la Cédula de Identidad <b>V-{institucion["director_ci"]}</b>, "
        f"de la {nombre_inst}, que funciona en Puerto La Cruz, hace constar que el alumno(a): "
        f"<b>{estudiante['Apellidos']} {estudiante['Nombres']}</b>, "
        f"portador de la cédula de identidad <b>CE-{estudiante['Cédula']}</b>, estudiante del "
        f"<b>{estudiante['Grado']} Grado sección '{estudiante['Sección']}'</b> "
        f"de Educación Primaria durante el Año Escolar 2025 - 2026 se pudo observar, que mantuvo una "
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
    firma = f"________________________<br/>Prof. {institucion["director"]}"
    story.append(Paragraph(firma, centrado))
    story.append(Spacer(1, 3))

    story.append(Paragraph(f"C.I. V-{institucion["director_ci"]}", centrado))
    story.append(Spacer(1, 3))

    story.append(Paragraph("Director", centrado))

    # Construir PDF
    doc.build(story, onFirstPage=encabezado_y_pie, onLaterPages=encabezado_y_pie)
    return nombre_archivo




def generar_constancia_trabajo(empleado: dict) -> str:
    carpeta = os.path.join(os.getcwd(), "exportados", "Constancias de trabajo")
    os.makedirs(carpeta, exist_ok=True)

    nombre_archivo = os.path.join(carpeta, f"ConstanciaTrabajo_{empleado['Cédula']}.pdf")

    doc = SimpleDocTemplate(
        nombre_archivo,
        pagesize=letter,
        leftMargin=80,
        rightMargin=80,
        topMargin=100,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()
    story = []

    # Título
    story.append(Paragraph("CONSTANCIA DE TRABAJO", styles["Title"]))
    story.append(Spacer(1, 20))

    # Texto principal
    texto = (
        f"Se hace constar por medio de la presente que el(la) ciudadano(a) "
        f"<b>{empleado['Nombres']} {empleado['Apellidos']}</b>, titular de la cédula de identidad "
        f"N° <b>{empleado['Cédula']}</b>, labora en esta institución desde la fecha "
        f"<b>{empleado['Fecha Ingreso']}</b>, desempeñando el cargo de "
        f"<b>{empleado['Cargo']}</b> y devengando un salario mensual de "
        f"<b>{empleado['Salario']} Bs.</b>.<br/><br/>"
    )
    story.append(Paragraph(texto, styles["Normal"]))
    story.append(Spacer(1, 40))

    # Fecha y lugar
    fecha_hoy = date.today().strftime("%d/%m/%Y")
    texto_fecha = (
        f"Constancia que se expide a petición de la parte interesada en la ciudad de Puerto La Cruz, "
        f"a la fecha {fecha_hoy}."
    )
    story.append(Paragraph(texto_fecha, styles["Normal"]))
    story.append(Spacer(1, 40))

    # Firma
    story.append(Paragraph("________________________<br/>Director(a)", styles["Normal"]))

    # Construir PDF con encabezado en todas las páginas
    doc.build(story, onFirstPage=encabezado, onLaterPages=encabezado)
    return nombre_archivo


def exportar_reporte_pdf(parent, figure, titulo, criterio, etiquetas, valores, total):
    ruta, _ = QFileDialog.getSaveFileName(
        parent,
        "Guardar reporte",
        "",
        "PDF Files (*.pdf)"
    )
    if not ruta:
        return
    if not ruta.endswith(".pdf"):
        ruta += ".pdf"

    # Guardar la figura en memoria
    buf = io.BytesIO()
    figure.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)

    # Documento
    doc = SimpleDocTemplate(
        ruta,
        pagesize=letter,
        leftMargin=80,
        rightMargin=80,
        topMargin=100,   # 👈 deja espacio para el encabezado
        bottomMargin=50
    )
    styles = getSampleStyleSheet()
    story = []

    # Título y fecha
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
    story.append(Paragraph(f"<b>{titulo}</b>"))
    story.append(Paragraph(f"Fecha de generación: {fecha}", styles["Normal"]))
    story.append(Spacer(1, 20))

    # Descripción
    descripcion = (
        f"Este reporte presenta un análisis de los estudiantes según el criterio "
        f"<b>{criterio}</b>. La gráfica y la tabla muestran la distribución de los datos "
        f"y el total general de registros considerados."
    )
    story.append(Paragraph(descripcion, styles["Normal"]))
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

    # Observaciones: líneas vacías para escribir a mano
    story.append(Paragraph("<b>Observaciones:</b>", styles["Normal"]))
    story.append(Spacer(1, 12))
    for _ in range(2):
        story.append(Paragraph("_________________________________________________________", styles["Normal"]))
        story.append(Spacer(1, 12))

    # Construir PDF con encabezado en todas las páginas
    doc.build(story, onFirstPage=encabezado, onLaterPages=encabezado)



def exportar_tabla_excel(nombre_archivo: str, encabezados: list, filas: list) -> str:
    """
    Exporta datos tabulares a un archivo Excel.
    :param nombre_archivo: ruta completa del archivo .xlsx
    :param encabezados: lista con los nombres de las columnas
    :param filas: lista de listas o tuplas con los datos
    :return: ruta del archivo generado
    """
    wb = Workbook()
    ws = wb.active
    ws.title = "Datos"

    # Escribir encabezados
    ws.append(encabezados)

    # Escribir filas
    for fila in filas:
        ws.append(fila)

    # Guardar archivo
    wb.save(nombre_archivo)
    return nombre_archivo

def exportar_estudiantes_excel(parent, estudiantes: list) -> str:
    """
    Exporta lista de estudiantes a Excel, preguntando ubicación al usuario.
    :param parent: ventana padre (ej. self en MainWindow)
    :param estudiantes: lista de diccionarios con datos de estudiantes
    :return: ruta del archivo generado o None si se canceló
    """
    # Sugerir un nombre por defecto con timestamp
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
        return None  # no hay datos

    # Tomar las claves del primer diccionario como encabezados
    encabezados = list(estudiantes[0].keys())

    # Tomar los valores de cada diccionario en el mismo orden
    filas = [list(e.values()) for e in estudiantes]

    return exportar_tabla_excel(ruta, encabezados, filas)

def exportar_empleados_excel(parent, empleados: list) -> str:

    # Sugerir un nombre por defecto con timestamp
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
        return None  # no hay datos

    # Tomar las claves del primer diccionario como encabezados
    encabezados = list(empleados[0].keys())

    # Tomar los valores de cada diccionario en el mismo orden
    filas = [list(e.values()) for e in empleados]

    return exportar_tabla_excel(ruta, encabezados, filas)