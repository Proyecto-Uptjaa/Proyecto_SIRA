from utils.db import get_connection
from matplotlib import cm

criterios_por_poblacion = {
    "Estudiantes": ["Rango de edad", "Por sección", "Por grado", "Por ciudad de nacimiento", "Por género"],
    "Empleados": ["Por cargo", "Por nivel académico", "Rango de salario"],
}
class CriteriosReportes:
    @staticmethod
    def estudiantes_por_genero():
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT genero, COUNT(*)
            FROM estudiantes
            WHERE estado = 1
            GROUP BY genero
        """
        cursor.execute(query)
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
            SELECT seccion, COUNT(*)
            FROM estudiantes
            WHERE estado = 1
            GROUP BY seccion
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
            SELECT grado, COUNT(*)
            FROM estudiantes
            WHERE estado = 1
            GROUP BY grado
            ORDER BY grado
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
            WHERE estado = 1
            GROUP BY city
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
            WHERE estado = 1
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
    def empleados_por_cargo():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT cargo, COUNT(*) 
            FROM empleados 
            WHERE estado = 1
            GROUP BY cargo
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
        """)
        datos = cursor.fetchall()
        conn.close()
        etiquetas = [fila[0] for fila in datos]
        valores = [fila[1] for fila in datos]
        return etiquetas, valores

    CONSULTAS = {
    ("Estudiantes", "Por género"): (estudiantes_por_genero.__func__, []),
    ("Estudiantes", "Rango de edad"): (estudiantes_por_rango_edad.__func__, ["edad_min", "edad_max"]),
    ("Estudiantes", "Por sección"): (estudiantes_por_seccion.__func__, []),
    ("Estudiantes", "Por grado"): (estudiantes_por_grado.__func__, []),
    ("Estudiantes", "Por ciudad de nacimiento"): (estudiantes_por_ciudad.__func__, []),
    ("Empleados", "Por cargo"): (empleados_por_cargo.__func__, []),
    ("Empleados", "Por nivel académico"): (empleados_por_nivel_academico.__func__, []),
    ("Empleados", "Rango de salario"): (empleados_por_rango_salario.__func__, ["salario_min", "salario_max"]),
}


    @staticmethod
    def grafica_torta(ax, etiquetas, valores, titulo):
        total = sum(valores)

        def autopct_func(pct, allvals):
            absolute = int(round(pct/100.*sum(allvals)))
            return f"{absolute} ({pct:.1f}%)"

        # Paleta de colores más vistosa
        colors = cm.tab20.colors  # puedes probar: cm.Paired.colors, cm.Pastel1.colors, etc.
        
        explode = [0.05] * len(valores)  # separa todas las porciones un poco

        wedges, texts, autotexts = ax.pie(
            valores,
            labels=etiquetas,
            autopct=lambda pct: autopct_func(pct, valores),
            startangle=90,
            colors=colors,              # 🎨 paleta
            wedgeprops={"edgecolor": "white"},  # bordes blancos entre sectores
            textprops={"fontsize": 10},  # tamaño de etiquetas
            explode=explode,
            shadow=True
        )

        # Mejorar estilo de los porcentajes
        for autotext in autotexts:
            autotext.set_color("white")
            autotext.set_fontweight("bold")

        # Texto del total
        ax.text(
            0.5, -0.1, f"Total general: {total}",
            ha="center", va="center",
            transform=ax.transAxes,
            fontsize=11, fontweight="bold"
        )

        # Título con estilo
        ax.set_title(titulo, fontsize=14, fontweight="bold")
        ax.axis("equal")  # círculo perfecto

    @staticmethod
    def grafica_barras(ax, etiquetas, valores, titulo):
        # 🎨 Otras paletas de colores: tab10, tab20, Set1, Dark2)
        colores = cm.tab10.colors  

        bars = ax.bar(
            etiquetas,
            valores,
            color=colores[:len(etiquetas)],   # asigna colores distintos
            #edgecolor="black",                # bordes definidos
            linewidth=1.2
        )

        # Mostrar valores dentro de cada barra
        for bar in bars:
            height = bar.get_height()
            ax.annotate(
                f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, -15),  # desplaza hacia abajo, dentro de la barra
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=9, color="white", fontweight="bold"
            )

        # Título y etiquetas
        ax.set_title(titulo, fontsize=14, fontweight="bold")
        ax.set_ylabel("Cantidad", fontsize=12)

        # Etiquetas horizontales
        ax.set_xticks(range(len(etiquetas)))
        ax.set_xticklabels(etiquetas, rotation=0, ha="center")

        # Fondo y grilla para más claridad
        ax.set_facecolor("#f9f9f9")
        ax.grid(axis="y", linestyle="--", alpha=0.6)

        # Total general debajo
        total = sum(valores)
        ax.text(
            0.5, -0.15, f"Total general: {total}",
            ha="center", va="center",
            transform=ax.transAxes,
            fontsize=10, fontweight="bold"
        )

        # Ajustar márgenes automáticamente
        ax.figure.tight_layout()

    def grafica_texto(ax, etiquetas, valores, titulo):
        ax.axis("off")
        texto = "\n".join(f"{e}: {v}" for e, v in zip(etiquetas, valores))
        ax.text(0.5, 0.5, texto, ha="center", va="center", fontsize=12)

    GRAFICAS = {
        "Torta": grafica_torta,
        "Barras": grafica_barras,
        "Reporte de texto": grafica_texto,
    }