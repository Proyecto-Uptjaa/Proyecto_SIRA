from utils.db import get_connection
from matplotlib import cm
from datetime import datetime

criterios_por_poblacion = {
    "Estudiantes": ["Por género", "Rango de edad", "Por sección", "Por grado", "Por ciudad de nacimiento", "Matricula por año escolar"],
    "Egresados": ["Por género", "Por año escolar de egreso"],
    "Secciones": ["Distribución por género", "Distribución por edad promedio", "Ocupación por sección", "Género por sección específica"],
    "Empleados": ["Por cargo", "Por nivel académico", "Rango de salario"],
}

class CriteriosReportes:
    
    # ============== ESTUDIANTES ==============
    @staticmethod
    def estudiantes_por_genero():
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT genero, COUNT(*)
            FROM estudiantes
            WHERE estado = 1 AND estatus_academico = 'Regular'
            GROUP BY genero
        """
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.close()
        etiquetas = [fila[0] for fila in datos]
        valores = [fila[1] for fila in datos]
        return etiquetas, valores
    
    @staticmethod
    def estudiantes_por_rango_edad(edad_min, edad_max):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT genero, COUNT(*)
            FROM estudiantes
            WHERE estado = 1 AND estatus_academico = 'Regular'
            AND TIMESTAMPDIFF(YEAR, fecha_nac_est, CURDATE()) BETWEEN %s AND %s
            GROUP BY genero
        """
        cursor.execute(query, (edad_min, edad_max))
        datos = cursor.fetchall()
        conn.close()
        etiquetas = [fila[0] for fila in datos]
        valores = [fila[1] for fila in datos]
        return etiquetas, valores
    
    @staticmethod
    def estudiantes_por_seccion():
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT CONCAT(s.grado, ' ', s.letra) AS seccion, COUNT(DISTINCT e.id) AS total
            FROM estudiantes e
            JOIN seccion_estudiante se ON e.id = se.estudiante_id
            JOIN secciones s ON se.seccion_id = s.id
            WHERE e.estado = 1 AND e.estatus_academico = 'Regular' AND s.activo = 1
            GROUP BY s.id
            ORDER BY s.grado, s.letra
        """
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.close()
        etiquetas = [fila[0] for fila in datos]
        valores = [fila[1] for fila in datos]
        return etiquetas, valores

    @staticmethod
    def estudiantes_por_grado():
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT s.grado, COUNT(DISTINCT e.id) AS total
            FROM estudiantes e
            JOIN seccion_estudiante se ON e.id = se.estudiante_id
            JOIN secciones s ON se.seccion_id = s.id
            WHERE e.estado = 1 AND e.estatus_academico = 'Regular' AND s.activo = 1
            GROUP BY s.grado
            ORDER BY s.grado
        """
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.close()
        etiquetas = [str(fila[0]) for fila in datos if fila[0] is not None]
        valores = [fila[1] for fila in datos if fila[0] is not None]
        return etiquetas, valores
   
    @staticmethod
    def estudiantes_por_ciudad():
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT city, COUNT(*)
            FROM estudiantes
            WHERE estado = 1 AND estatus_academico = 'Regular'
            GROUP BY city
            ORDER BY COUNT(*) DESC
            LIMIT 10
        """
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.close()
        etiquetas = [fila[0] if fila[0] else 'Sin especificar' for fila in datos]
        valores = [fila[1] for fila in datos]
        return etiquetas, valores
    
    @staticmethod
    def matricula_por_rango_anio(anio_inicio, anio_fin):
        """Muestra la matrícula total de estudiantes desde un año hasta otro"""
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT 
                CONCAT(a.anio_inicio, '/', a.anio_inicio + 1) AS año_escolar,
                COUNT(DISTINCT se.estudiante_id) AS total
            FROM anios_escolares a
            LEFT JOIN seccion_estudiante se ON se.año_asignacion = a.anio_inicio
            LEFT JOIN estudiantes e ON se.estudiante_id = e.id
            WHERE a.anio_inicio BETWEEN %s AND %s
            GROUP BY a.anio_inicio
            ORDER BY a.anio_inicio
        """
        cursor.execute(query, (anio_inicio, anio_fin))
        datos = cursor.fetchall()
        conn.close()
        etiquetas = [fila[0] for fila in datos]
        valores = [fila[1] for fila in datos]
        return etiquetas, valores
    
    # ============== EGRESADOS ==============
    @staticmethod
    def egresados_por_genero():
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT genero, COUNT(*)
            FROM estudiantes
            WHERE estatus_academico = 'Egresado'
            GROUP BY genero
        """
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.close()
        etiquetas = [fila[0] for fila in datos]
        valores = [fila[1] for fila in datos]
        return etiquetas, valores

    @staticmethod
    def egresados_por_anio_escolar():
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT 
                CONCAT(hs.año_inicio, '/', hs.año_inicio + 1) AS año_escolar,
                COUNT(DISTINCT hs.estudiante_id) AS total
            FROM historial_secciones hs
            JOIN estudiantes e ON hs.estudiante_id = e.id
            WHERE e.estatus_academico = 'Egresado'
            GROUP BY hs.año_inicio
            ORDER BY hs.año_inicio DESC
        """
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.close()
        etiquetas = [fila[0] for fila in datos]
        valores = [fila[1] for fila in datos]
        return etiquetas, valores

    # ============== SECCIONES ==============
    @staticmethod
    def secciones_por_genero():
        """Distribución por género en todas las secciones activas"""
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT 
                CONCAT(s.grado, ' ', s.letra) AS seccion,
                SUM(CASE WHEN e.genero = 'Masculino' THEN 1 ELSE 0 END) AS masculino,
                SUM(CASE WHEN e.genero = 'Femenino' THEN 1 ELSE 0 END) AS femenino
            FROM secciones s
            LEFT JOIN seccion_estudiante se ON s.id = se.seccion_id
            LEFT JOIN estudiantes e ON se.estudiante_id = e.id AND e.estado = 1
            WHERE s.activo = 1
            GROUP BY s.id
            ORDER BY s.grado, s.letra
        """
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.close()
        
        # Preparar datos para gráfico agrupado
        etiquetas = [f"{fila[0]}\nM:{fila[1]} F:{fila[2]}" for fila in datos]
        valores = [fila[1] + fila[2] for fila in datos]  # Total por sección
        return etiquetas, valores

    @staticmethod
    def obtener_secciones_activas():
        """Devuelve lista de secciones activas del año escolar actual"""
        from models.anio_model import AnioEscolarModel
        
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Obtener el año escolar actual
        anio_actual = AnioEscolarModel.obtener_actual()
        if not anio_actual:
            cursor.close()
            conn.close()
            return []
        
        query = """
            SELECT CONCAT(grado, ' ', letra) AS seccion
            FROM secciones
            WHERE activo = 1 AND año_escolar_id = %s
            ORDER BY grado, letra
        """
        cursor.execute(query, (anio_actual['id'],))
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        return [d['seccion'] for d in datos]

    @staticmethod
    def genero_por_seccion_especifica(seccion_nombre):
        """Muestra cuántos varones y hembras hay en una sección específica del año actual"""
        from models.anio_model import AnioEscolarModel
        
        conn = get_connection()
        cursor = conn.cursor()
        
        # Obtener el año escolar actual
        anio_actual = AnioEscolarModel.obtener_actual()
        if not anio_actual:
            cursor.close()
            conn.close()
            return [], []
        
        # Separar grado y letra del formato "1ero A"
        partes = seccion_nombre.strip().split()
        if len(partes) < 2:
            cursor.close()
            conn.close()
            return [], []
        
        grado = partes[0]
        letra = partes[1]
        
        query = """
            SELECT 
                e.genero,
                COUNT(*) AS total
            FROM estudiantes e
            JOIN seccion_estudiante se ON e.id = se.estudiante_id
            JOIN secciones s ON se.seccion_id = s.id
            WHERE s.grado = %s AND s.letra = %s 
            AND s.año_escolar_id = %s
            AND s.activo = 1 AND e.estado = 1
            GROUP BY e.genero
        """
        cursor.execute(query, (grado, letra, anio_actual['id']))
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        
        etiquetas = [fila[0] for fila in datos]
        valores = [fila[1] for fila in datos]
        return etiquetas, valores

    @staticmethod
    def secciones_por_edad_promedio():
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT 
                CONCAT(s.grado, ' ', s.letra) AS seccion,
                ROUND(AVG(TIMESTAMPDIFF(YEAR, e.fecha_nac_est, CURDATE())), 1) AS edad_promedio
            FROM secciones s
            LEFT JOIN seccion_estudiante se ON s.id = se.seccion_id
            LEFT JOIN estudiantes e ON se.estudiante_id = e.id AND e.estado = 1
            WHERE s.activo = 1
            GROUP BY s.id
            HAVING COUNT(e.id) > 0
            ORDER BY s.grado, s.letra
        """
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.close()
        etiquetas = [fila[0] for fila in datos]
        valores = [float(fila[1]) for fila in datos]
        return etiquetas, valores

    @staticmethod
    def secciones_ocupacion():
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT 
                CONCAT(s.grado, ' ', s.letra) AS seccion,
                COUNT(e.id) AS actuales,
                s.cupo_maximo AS cupo,
                ROUND((COUNT(e.id) / s.cupo_maximo) * 100, 1) AS porcentaje
            FROM secciones s
            LEFT JOIN seccion_estudiante se ON s.id = se.seccion_id
            LEFT JOIN estudiantes e ON se.estudiante_id = e.id AND e.estado = 1
            WHERE s.activo = 1
            GROUP BY s.id
            ORDER BY s.grado, s.letra
        """
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.close()
        etiquetas = [f"{fila[0]}\n{fila[1]}/{fila[2]}" for fila in datos]
        valores = [float(fila[3]) for fila in datos]  # Porcentaje de ocupación
        return etiquetas, valores

    # ============== EMPLEADOS ==============
    @staticmethod
    def empleados_por_cargo():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT cargo, COUNT(*) 
            FROM empleados 
            WHERE estado = 1
            GROUP BY cargo
            ORDER BY COUNT(*) DESC
        """)
        datos = cursor.fetchall()
        conn.close()
        etiquetas = [fila[0] for fila in datos]
        valores = [fila[1] for fila in datos]
        return etiquetas, valores
    
    @staticmethod
    def empleados_por_rango_salario(salario_min, salario_max):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT genero, COUNT(*)
            FROM empleados
            WHERE estado = 1
            AND salario BETWEEN %s AND %s
            GROUP BY genero
        """
        cursor.execute(query, (salario_min, salario_max))
        datos = cursor.fetchall()
        conn.close()
        etiquetas = [fila[0] for fila in datos]
        valores = [fila[1] for fila in datos]
        return etiquetas, valores
    
    @staticmethod
    def empleados_por_nivel_academico():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT titulo, COUNT(*) 
            FROM empleados 
            WHERE estado = 1
            GROUP BY titulo
            ORDER BY COUNT(*) DESC
        """)
        datos = cursor.fetchall()
        conn.close()
        etiquetas = [fila[0] if fila[0] else 'Sin especificar' for fila in datos]
        valores = [fila[1] for fila in datos]
        return etiquetas, valores

    # ============== MAPEO DE CONSULTAS ==============
    CONSULTAS = {
        # Estudiantes
        ("Estudiantes", "Por género"): (estudiantes_por_genero.__func__, []),
        ("Estudiantes", "Rango de edad"): (estudiantes_por_rango_edad.__func__, ["edad_min", "edad_max"]),
        ("Estudiantes", "Por sección"): (estudiantes_por_seccion.__func__, []),
        ("Estudiantes", "Por grado"): (estudiantes_por_grado.__func__, []),
        ("Estudiantes", "Por ciudad de nacimiento"): (estudiantes_por_ciudad.__func__, []),
        ("Estudiantes", "Matricula por año escolar"): (matricula_por_rango_anio.__func__, ["anio_inicio", "anio_fin"]),
        
        # Egresados
        ("Egresados", "Por género"): (egresados_por_genero.__func__, []),
        ("Egresados", "Por año escolar de egreso"): (egresados_por_anio_escolar.__func__, []),
        
        # Secciones
        ("Secciones", "Distribución por género"): (secciones_por_genero.__func__, []),
        ("Secciones", "Distribución por edad promedio"): (secciones_por_edad_promedio.__func__, []),
        ("Secciones", "Ocupación por sección"): (secciones_ocupacion.__func__, []),
        ("Secciones", "Género por sección específica"): (genero_por_seccion_especifica.__func__, ["seccion"]),
        
        # Empleados
        ("Empleados", "Por cargo"): (empleados_por_cargo.__func__, []),
        ("Empleados", "Por nivel académico"): (empleados_por_nivel_academico.__func__, []),
        ("Empleados", "Rango de salario"): (empleados_por_rango_salario.__func__, ["salario_min", "salario_max"]),
    }

    # ============== FUNCIONES DE GRÁFICOS ==============
    @staticmethod
    def grafica_torta(ax, etiquetas, valores, titulo):
        total = sum(valores)

        def autopct_func(pct, allvals):
            absolute = int(round(pct/100.*sum(allvals)))
            return f"{absolute}\n({pct:.1f}%)"

        colors = cm.Set3.colors
        explode = [0.05] * len(valores)

        wedges, texts, autotexts = ax.pie(
            valores,
            labels=etiquetas,
            autopct=lambda pct: autopct_func(pct, valores),
            startangle=90,
            colors=colors,
            wedgeprops={"edgecolor": "white", "linewidth": 2},
            textprops={"fontsize": 9},
            explode=explode,
            shadow=True
        )

        for autotext in autotexts:
            autotext.set_color("white")
            autotext.set_fontweight("bold")

        ax.text(
            0.5, -0.15, f"Total: {total}",
            ha="center", va="center",
            transform=ax.transAxes,
            fontsize=12, fontweight="bold"
        )

        ax.set_title(titulo, fontsize=14, fontweight="bold", pad=20)
        ax.axis("equal")

    @staticmethod
    def grafica_barras(ax, etiquetas, valores, titulo):
        colores = cm.tab10.colors

        bars = ax.bar(
            etiquetas,
            valores,
            color=colores[:len(etiquetas)],
            edgecolor="black",
            linewidth=1.2
        )

        for bar in bars:
            height = bar.get_height()
            ax.annotate(
                f'{height:.1f}' if isinstance(height, float) else f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=9, fontweight="bold"
            )

        ax.set_title(titulo, fontsize=14, fontweight="bold", pad=20)
        ax.set_ylabel("Cantidad", fontsize=11, fontweight="bold")
        ax.set_xticks(range(len(etiquetas)))
        ax.set_xticklabels(etiquetas, rotation=45, ha="right", fontsize=9)
        ax.set_facecolor("#f9f9f9")
        ax.grid(axis="y", linestyle="--", alpha=0.6)

        total = sum(valores)
        ax.text(
            0.5, -0.25, f"Total: {total:.0f}" if isinstance(total, float) else f"Total: {total}",
            ha="center", va="center",
            transform=ax.transAxes,
            fontsize=11, fontweight="bold"
        )

        ax.figure.tight_layout()

    @staticmethod
    def grafica_texto(ax, etiquetas, valores, titulo):
        ax.axis("off")
        ax.set_title(titulo, fontsize=14, fontweight="bold", pad=20)
        
        texto_lineas = [f"{e}: {v}" for e, v in zip(etiquetas, valores)]
        texto_lineas.append(f"\nTotal: {sum(valores)}")
        texto = "\n".join(texto_lineas)
        
        ax.text(0.5, 0.5, texto, ha="center", va="center", 
                fontsize=11, family="monospace",
                bbox=dict(boxstyle="round,pad=1", facecolor="lightgray", alpha=0.8))

    GRAFICAS = {
        "Torta": grafica_torta,
        "Barras": grafica_barras,
        "Reporte de texto": grafica_texto,
    }