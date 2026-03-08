# SIRA - Sistema de Información para el Registro Académico

<p align="center">
  <strong>Sistema integral de gestión académica para instituciones educativas de Educación Inicial y Primaria</strong>
</p>

---

**SIRA** (Sistema de Información para el Registro Académico) es una aplicación de escritorio multiplataforma desarrollada para la gestión integral de centros educativos. Permite administrar de forma eficiente el registro de estudiantes, empleados, representantes, secciones académicas, años escolares, materias, áreas de aprendizaje y calificaciones, proporcionando herramientas completas para el control académico institucional.

---

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)
![Database](https://img.shields.io/badge/Database-MySQL%208.0%2B-orange?logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active%20Development-success)
![Framework](https://img.shields.io/badge/Framework-PySide6%20(Qt%206)-brightgreen?logo=qt&logoColor=white)

---

## 📑 Tabla de Contenidos
- [Características Principales](#-características-principales)
- [Tecnologías Utilizadas](#️-tecnologías-utilizadas)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Configuración](#️-configuración)
- [Licencia](#-licencia)

## ✨ Características Principales

### 🔐 Autenticación y Control de Acceso
- Sistema de login seguro con encriptación de contraseñas mediante **bcrypt**
- Control de permisos basado en roles (**Administrador** / **Empleado**)
- Gestión de usuarios con estados activo/inactivo
- Bloqueo temporal tras intentos fallidos de inicio de sesión (3 intentos → 30 segundos de espera)
- Cambio de contraseñas y actualización de perfiles
- **Re-login sin reiniciar** la aplicación al cerrar sesión
- **Verificación de fecha/hora** del sistema vs servidor MySQL tras cada inicio de sesión

### 👨‍🎓 Gestión de Estudiantes
- Registro completo de estudiantes con validación de datos en tiempo real
- Generación automática de **cédula estudiantil** con formato único
- Asignación automática a secciones según grado y disponibilidad
- **Promoción automática masiva** de estudiantes entre años escolares
- Movimiento individual de estudiantes entre secciones
- **Devolución de estudiantes** a grado inferior (repitencia) con registro de observaciones
- Control de retiros con registro de motivos y generación de constancia
- Gestión de **egresados** (estudiantes que culminan 6to grado)
- Historial académico completo por estudiante
- Historial de calificaciones por materia y lapso
- Vinculación con **representantes** (búsqueda por cédula, creación, compartidos entre estudiantes)

### 👨‍👩‍👧 Gestión de Representantes
- Registro de representantes con datos de contacto completos
- Búsqueda de representantes existentes por cédula para reutilización
- Vinculación de múltiples estudiantes al mismo representante
- Creación de nuevos representantes desde la ficha del estudiante
- Conteo de hijos/representados por representante

### 💼 Gestión de Personal
- Registro y administración de empleados con ficha detallada
- Catálogo de **cargos predefinidos** (24 opciones: DOC II, TSU, OBRERO, COCINERA, etc.)
- Clasificación por **tipo de personal**: Administrativo, Docente, Obrero, Cocinera
- **Especialidades docentes**: Deporte, Teatro, Música, Danza
- Asignación de docentes a secciones académicas
- Control de fecha de ingreso y estado laboral (activo/inactivo)
- Fichas detalladas con información personal, laboral y adicional
- Cálculo automático de edad

### 🏫 Gestión de Secciones Académicas
- Creación de secciones por nivel (**Educación Inicial** y **Primaria**)
- Grados configurables: Inicial (1er, 2do, 3er Nivel) y Primaria (1ero a 6to)
- Asignación de letras de sección (A-Z o Única)
- **Interfaz visual con tarjetas** para cada sección (nivel, grado, letra, docente, ocupación)
- **Duplicación masiva** de secciones y materias entre años escolares
- Control de capacidad máxima de estudiantes por sección (1-50)
- Activación/desactivación y **reactivación** de secciones
- Búsqueda de texto en tarjetas (grado, letra, nivel, docente)
- Asignación y cambio de docente responsable
- Exportación de listados de estudiantes por sección

### 📅 Gestión de Años Escolares
- Apertura y cierre de períodos académicos
- Control de año escolar activo (solo uno puede estar activo)
- **Promoción automática** de estudiantes al crear nuevo año:
  - Estudiantes de 6to grado → Egresados
  - Resto → Promoción al grado siguiente
- Duplicación automática de secciones con materias asignadas al nuevo año
- Historial completo de años escolares anteriores

### 📚 Gestión de Materias y Áreas de Aprendizaje
- **Áreas de aprendizaje**: Agrupan materias por categoría (ej: Lenguaje, Matemáticas, Ciencias)
- Catálogo de materias configurable por nivel y grado (solo Primaria)
- Asignación de materias a secciones específicas con diálogo dedicado
- Sistema de evaluación **literal** (A, B, C, D, E)
- Activación/desactivación de materias y áreas
- Duplicación automática de materias al aperturar nuevo año escolar
- Gestión completa de áreas: crear, editar, activar/desactivar

### 📝 Gestión de Calificaciones (Solo Primaria)
- Selección de sección mediante **mini-tarjetas visuales**
- Registro de notas por **3 lapsos** académicos
- **Registro masivo** de notas por sección/materia/lapso en una sola transacción
- Sistema de notas literales: A (Excelente) a E (Deficiente)
- **Coloreo automático** en la tabla: verde (A/B), amarillo (C), rojo (D/E)
- **Cálculo automático de nota final** al completar los 3 lapsos
- Indicador de aprobación (A, B, C = Aprobado | D, E = Reprobado)
- Delegate personalizado para entrada de notas (solo A-E)
- Historial de calificaciones exportable a PDF

### 📄 Generación de Documentos PDF
- **Visor PDF integrado** (`QPdfView`) para previsualizar constancias dentro de la aplicación antes de exportar
- **Búsqueda con autocompletado** por nombre o cédula del estudiante/empleado (`QCompleter`)
- Generación automática con datos institucionales, logo y formato oficial

| Documento | Descripción |
|-----------|-------------|
| **Constancia de Estudios** | Certificación de inscripción activa del estudiante |
| **Constancia de Inscripción** | Confirmación de matrícula en el año escolar |
| **Constancia de Buena Conducta** | Certificación de comportamiento del estudiante |
| **Constancia de Retiro** | Documento de baja con motivo de retiro |
| **Constancia de Prosecución** | Transición de Inicial a Primaria |
| **Certificado de Promoción 6to** | Certificación de egreso a Educación Secundaria |
| **Historial Académico** | Trayectoria completa de secciones cursadas |
| **Historial de Calificaciones** | Notas por materia y lapso de cada año |
| **Listado de Sección** | Lista de estudiantes por sección con datos |
| **Constancia de Trabajo** | Certificación laboral para empleados |
| **Reporte Estadístico** | Gráficos y estadísticas en PDF |

### 📊 Exportación a Excel
- Exportación de tablas filtradas de estudiantes y empleados
- Exportación de **matrícula completa** del año escolar
- Exportación de **nómina completa** de empleados
- Exportación de listado de egresados
- **Reporte RAC** (Registro de Asignación de Cargos - Ministerio)

### 🔍 Búsqueda y Filtrado Avanzado
- Búsqueda en tiempo real por múltiples criterios
- Filtros por columna específica (nombre, cédula, grado, etc.)
- Opción para mostrar/ocultar registros inactivos
- Sistema de proxy inteligente para filtrado de tablas
- Ordenamiento por cualquier columna

### 📈 Dashboard y Reportes Estadísticos
- Panel principal con resumen estadístico y **actualización automática** (cada 60 segundos)
- **Widget de notificaciones inteligente** con alertas y avisos del sistema:
  - Estudiantes activos sin sección asignada
  - Secciones sin docente responsable
  - Secciones con cupo superado
  - Secciones de Primaria sin materias asignadas
  - Secciones activas sin estudiantes (vacías)
  - Notas pendientes por lapso (1°, 2°, 3°)
  - Empleados activos sin código RAC
  - Datos institucionales incompletos
  - Estudiantes retirados en el año actual
- Contadores de estudiantes (activos, inactivos, regulares, retirados, egresados)
- Contadores de empleados (activos/inactivos), usuarios y representantes
- Indicador de sección más numerosa del año escolar activo
- **Accesos directos** para registro rápido de estudiantes, empleados y secciones
- **Sistema de reportes configurables** con múltiples categorías:
  - **Estudiantes**: por género, rango de edad, sección, grado, ciudad, matrícula por rango de años
  - **Egresados**: por género, por año escolar de egreso
  - **Secciones**: por género, edad promedio, ocupación, sección específica
  - **Empleados**: por cargo, por nivel académico
- **Tres tipos de gráfica**: barras, torta y texto
- Exportación de reportes a **PDF** con gráfico y datos tabulares

### 🔒 Auditoría y Trazabilidad
- Registro automático de **todas las operaciones CRUD**
- Seguimiento de acciones por usuario
- Marcas de tiempo de creación y modificación
- Historial completo de cambios consultable (tabla paginada)
- Registro de accesos al sistema
- Registro de promociones, retiros, asignaciones y cambios de logo

### 💾 Sistema de Respaldos
- **Backups automáticos** programados (cada 3 días, mediante timer integrado)
- Backups manuales desde el menú de administración con apertura de carpeta
- **Restauración de backups** con diálogo de selección:
  - Lista de backups disponibles con fecha, tipo y tamaño
  - Opción de seleccionar archivo `.sql` externo
  - **Doble confirmación** de seguridad antes de restaurar
  - Cierre de sesión automático post-restauración
- Información del último backup y conteo total
- Formato SQL compatible con MySQL
- Rotación automática (máximo 30 backups guardados)

### 🖼️ Gestión de Logo Institucional
- Carga de logo durante la **configuración inicial** o desde Administración
- Validación de formato (PNG, JPG, JPEG, BMP), tamaño (máx. 500KB) y dimensiones (32-512px)
- **Redimensionamiento automático** si la imagen excede las dimensiones máximas
- **Caché global** en memoria para rendimiento óptimo
- Previsualización en tiempo real antes de guardar
- **Propagación automática** a login, todas las páginas de gestión y documentos PDF
- Fallback automático al logo embebido si no hay logo configurado

### ⚙️ Configuración Institucional
- Datos de la institución (nombre, RIF, dirección, teléfono, correo)
- Información del director y cédula
- Códigos oficiales (DEA, dependencia, estadístico)
- Logo institucional con gestión completa (subir, previsualizar, eliminar)
- Configuración única y centralizada
- Validación de campos (email, teléfono, RIF, CI)

### 🎨 Interfaz Gráfica Moderna
- Diseño intuitivo con **PySide6/Qt 6**
- **Fuente personalizada Inter** (9 variantes de peso) aplicada globalmente
- **Transiciones animadas** de deslizamiento entre módulos (`AnimatedStack`)
- Efectos visuales (sombras flotantes en widgets)
- **Tooltips personalizados** con estilo consistente
- Navegación fluida mediante barra lateral
- Iconografía consistente en todo el sistema
- Validación de formularios en tiempo real con QValidator
- Mensajes de confirmación y alertas contextuales en español
- **Manual de usuario integrado** accesible desde el menú de la aplicación (PDF)
- Diálogo **"Acerca de"** con información del sistema

---

## 🛠️ Tecnologías Utilizadas

### Lenguaje
| Tecnología | Versión | Descripción |
|------------|---------|-------------|
| **Python** | 3.10+ | Lenguaje principal del proyecto |

### Framework GUI
| Tecnología | Versión | Descripción |
|------------|---------|-------------|
| **PySide6** | 6.8.2 | Framework Qt 6 para interfaces gráficas modernas y multiplataforma |

### Base de Datos
| Tecnología | Versión | Descripción |
|------------|---------|-------------|
| **MySQL** | 8.0+ | Sistema de gestión de base de datos relacional |
| **mysql-connector-python** | 9.5.0 | Conector oficial de Python para MySQL |

### Bibliotecas Principales
| Biblioteca | Versión | Uso |
|------------|---------|-----|
| **bcrypt** | 5.0.0 | Encriptación y hashing seguro de contraseñas |
| **matplotlib** | 3.7+ | Generación de gráficos estadísticos para reportes |
| **ReportLab** | 4.4.5 | Creación de documentos PDF (constancias, certificados, reportes) |
| **openpyxl** | 3.1.5 | Exportación y manipulación de archivos Excel |
| **Pillow** | 12.0.0 | Procesamiento de imágenes (logo institucional) |
| **python-dotenv** | 1.2.1 | Gestión de variables de entorno y configuración |

### Herramientas de Desarrollo
| Herramienta | Versión | Uso |
|-------------|---------|-----|
| **PyInstaller** | 6.3.0 | Empaquetado de la aplicación en ejecutable standalone |
| **Qt Designer** | - | Diseño visual de interfaces (archivos .ui) |

---

## 📁 Estructura del Proyecto

```
Proyecto_SIRA/
├── main.py                  # Punto de entrada de la aplicación
├── paths.py                 # Configuración de rutas del sistema
├── compilar_ui.py           # Script para compilar archivos .ui a Python
├── requirements.txt         # Dependencias del proyecto
│
├── models/                  # Capa de datos (modelos)
│   ├── anio_model.py        # Gestión de años escolares
│   ├── areas_model.py       # Áreas de aprendizaje
│   ├── auditoria_model.py   # Registro de auditoría
│   ├── dashboard_model.py   # Estadísticas del dashboard
│   ├── emple_model.py       # Gestión de empleados
│   ├── estu_model.py        # Gestión de estudiantes
│   ├── institucion_model.py # Datos institucionales
│   ├── materias_model.py    # Gestión de materias
│   ├── notas_model.py       # Gestión de calificaciones
│   ├── registro_base.py     # Clase base de registros
│   ├── repre_model.py       # Gestión de representantes
│   ├── secciones_model.py   # Gestión de secciones
│   └── user_model.py        # Gestión de usuarios
│
├── views/                   # Capa de presentación (vistas)
│   ├── main_window.py       # Ventana principal y navegación
│   ├── login.py             # Pantalla de inicio de sesión
│   ├── config_inicial.py    # Asistente de configuración inicial
│   ├── gestion_estudiantes.py
│   ├── gestion_empleados.py
│   ├── gestion_secciones.py
│   ├── gestion_notas.py
│   ├── gestion_materias.py
│   ├── gestion_anio.py
│   ├── egresados.py
│   └── ...                  # Detalles, registros, delegates
│
├── utils/                   # Utilidades y herramientas
│   ├── conexion.py          # Conexión y verificación de BD
│   ├── db.py                # Pool de conexiones MySQL
│   ├── exportar.py          # Generación de PDF y Excel
│   ├── backup.py            # Gestión de respaldos
│   ├── reportes_config.py   # Configuración de reportes estadísticos
│   ├── logo_manager.py      # Caché y gestión del logo institucional
│   ├── animated_stack.py    # Transiciones animadas entre módulos
│   ├── tarjeta_seccion.py   # Widget de tarjeta de sección
│   ├── tarjeta_seccion_mini.py # Mini-tarjetas para selección de notas
│   ├── validaciones.py      # Validadores de formularios
│   ├── dialogs.py           # Diálogos personalizados
│   ├── forms.py             # Utilidades de formularios
│   ├── proxies.py           # Filtros proxy para tablas
│   ├── sombras.py           # Efectos visuales de sombra
│   ├── widgets.py           # Widgets personalizados (Switch, etc.)
│   ├── fonts.py             # Carga de fuentes personalizadas
│   ├── archivos.py          # Apertura de archivos del sistema
│   ├── edad.py              # Cálculo de edad
│   ├── fecha_validacion.py  # Validación de fecha/hora del sistema
│   └── security.py          # Seguridad y encriptación
│
├── ui_compiled/             # Interfaces compiladas desde Qt Designer
├── resources/               # Recursos estáticos
│   ├── fonts/               # Fuentes tipográficas (Inter)
│   ├── icons/               # Iconos e imágenes del sistema
│   └── ui/                  # Archivos .ui de Qt Designer
│
├── db/                      # Esquema de base de datos
│   └── schema.sql           # Estructura SQL completa (16 tablas)
│
├── backups/                 # Respaldos de la base de datos
└── exportados/              # Documentos PDF y Excel generados
    ├── Certificados de promocion/
    ├── Constancias de buena conducta/
    ├── Constancias de estudios/
    ├── Constancias de inscripcion/
    ├── Constancias de prosecucion inicial/
    ├── Constancias de retiro/
    ├── Constancias de trabajo/
    ├── Historial academico/
    └── Listados de secciones/
```

### 🗄️ Modelo de Base de Datos

La base de datos MySQL consta de **16 tablas** organizadas de la siguiente manera:

| Tabla                 | Descripción                                                                |
|-----------------------|----------------------------------------------------------------------------|
| `estudiantes`         | Registro de estudiantes con datos personales, académicos y estado          |
| `representantes`      | Datos de representantes legales vinculados a estudiantes                   |
| `empleados`           | Personal de la institución (docentes, administrativos, obreros, cocineras) |
| `usuarios`            | Cuentas de acceso al sistema con roles y permisos                          |
| `secciones`           | Secciones académicas por nivel, grado y año escolar                        |
| `seccion_estudiante`  | Relación muchos-a-muchos entre estudiantes y secciones                     |
| `seccion_materia`     | Relación muchos-a-muchos entre secciones y materias                        |
| `materias`            | Catálogo de materias con tipo de evaluación                                |
| `areas_aprendizaje`   | Áreas que agrupan materias por categoría                                   |
| `notas`               | Calificaciones por estudiante, materia y lapso                             |
| `notas_finales`       | Nota definitiva y estado de aprobación por materia                         |
| `anio_escolar`        | Períodos académicos con estado activo/cerrado                              |
| `historial_secciones` | Registro histórico de secciones cursadas por estudiante                    |
| `institucion`         | Datos institucionales, logo y códigos oficiales                            |
| `auditoria`           | Log de todas las operaciones realizadas en el sistema                      |
| `materia_grado`       | Relación entre materias y grados                                           |
---

## 📋 Requisitos Previos

Antes de instalar y ejecutar SIRA, asegúrate de tener instalado lo siguiente:

### Software Requerido
| Software | Versión Mínima | Enlace |
|----------|----------------|--------|
| **Python** | 3.10 o superior | [Descargar Python](https://www.python.org/downloads/) |
| **MySQL** | 8.0 o superior | [Descargar MySQL](https://dev.mysql.com/downloads/) |
| **pip** | (incluido con Python) | Gestor de paquetes |

### Sistemas Operativos Soportados
- ✅ **Windows** 10/11 (64 bits)
- ✅ **Linux** Ubuntu 20.04+, Debian 11+, Fedora 36+

### Requisitos de Hardware
| Recurso | Mínimo | Recomendado |
|---------|--------|-------------|
| **RAM** | 2 GB | 4 GB |
| **Almacenamiento** | 500 MB | 1 GB |
| **Resolución** | 1280x720 | 1920x1080 |

### Conocimientos Recomendados
- Conocimientos básicos de MySQL para configuración inicial
- Acceso de administrador/sudo para instalación de dependencias

## 📦 Instalación

Sigue estos pasos para instalar SIRA en tu sistema:

### 1️⃣ Descargar SIRA

1. Ve a la [página de Releases](https://github.com/Proyecto-Uptjaa/Proyecto_SIRA/releases) del proyecto
2. Descarga la última versión disponible:
   - **Windows:** `SIRA-vX.X.X-Windows.zip`
   - **Linux:** `SIRA-vX.X.X-Linux.zip`

### 2️⃣ Extraer los Archivos

<details>
<summary><strong>🪟 Windows</strong></summary>

1. Haz clic derecho en el archivo descargado → **Extraer todo...**
2. Elige una ubicación (ej: `C:\Archivos de programa\SIRA`)

</details>

<details>
<summary><strong>🐧 Linux</strong></summary>

```bash
# Extraer el archivo
unzip SIRA-vX.X.X-Linux.zip -d ~/SIRA

# Dar permisos de ejecución
cd ~/SIRA
chmod +x SIRA
```

</details>

### 3️⃣ Configurar la Base de Datos

#### Crear la Base de Datos en MySQL

```sql
-- Acceder a MySQL
mysql -u root -p

-- Dentro del prompt de MySQL, ejecutar:
CREATE DATABASE SIRA_DB CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
EXIT;
```

#### Importar la Estructura

Dentro de la carpeta extraída encontrarás `schema.sql`. Impórtalo:

<details>
<summary><strong>🪟 Windows (PowerShell)</strong></summary>

```powershell
cd "C:\Archivos de programa\SIRA"
mysql -u root -p SIRA_DB < schema.sql
```

</details>

<details>
<summary><strong>🐧 Linux</strong></summary>

```bash
cd ~/SIRA
mysql -u root -p SIRA_DB < schema.sql
```

</details>

> 💡 **Nota:** Ingresa la contraseña de tu usuario root de MySQL cuando se solicite.

### 4️⃣ Configurar el Archivo de Conexión

Crea un archivo llamado `.env` en la **misma carpeta donde está el ejecutable**:

```env
DB_HOST=localhost
DB_USER=root
DB_PASS=tu_contraseña_mysql
DB_NAME=SIRA_DB
```

> ⚠️ **Importante:** El archivo debe llamarse exactamente `.env` (con el punto al inicio).

### 5️⃣ Ejecutar SIRA

<details>
<summary><strong>🪟 Windows</strong></summary>

Doble clic en `SIRA.exe`

</details>

<details>
<summary><strong>🐧 Linux</strong></summary>

```bash
./SIRA
```

</details>

### 6️⃣ Configuración Inicial

Al ejecutar SIRA por primera vez, si no detecta usuarios en la base de datos, se mostrará automáticamente el **asistente de configuración inicial** de 4 pasos:

1. **Datos institucionales**: nombre de la institución, dirección, director, códigos oficiales
2. **Logo institucional**: selección y previsualización del logo (opcional)
3. **Año escolar**: configuración del año escolar inicial
4. **Usuario administrador**: creación del primer usuario administrador

> 📌 Si necesita reiniciar la configuración, puede vaciar la tabla `usuarios` en la base de datos y reiniciar la aplicación para que el asistente se muestre nuevamente.

---

## ⚙️ Configuración

### Archivo .env

El archivo `.env` debe estar ubicado en la **misma carpeta que el ejecutable**.

#### Estructura del Archivo

```env
# Configuración de conexión a MySQL
DB_HOST=localhost
DB_USER=root
DB_PASS=tu_contraseña_mysql
DB_NAME=SIRA_DB
```

#### Descripción de Variables

| Variable | Descripción | Valor por Defecto |
|----------|-------------|-------------------|
| `DB_HOST` | Dirección del servidor MySQL | `localhost` |
| `DB_USER` | Usuario de MySQL | `root` |
| `DB_PASS` | Contraseña de MySQL | *(requerido)* |
| `DB_NAME` | Nombre de la base de datos | `SIRA_DB` |

> ⚠️ **Importante:** 
> - El archivo `.env` NO debe tener extensión `.txt`
> - Guarda el archivo con codificación **UTF-8**
> - En Windows, asegúrate de mostrar extensiones de archivo para verificar

### Estructura de Carpetas

Después de la instalación, tu carpeta debe verse así:

```
SIRA/
├── SIRA.exe (Windows) o SIRA (Linux)    # Ejecutable principal
├── schema.sql                           # Estructura de la BD
├── .env                                 # Archivo de configuración
├── backups/                             # Respaldos automáticos y manuales
└── exportados/                          # Documentos generados
    ├── Certificados de promocion/
    ├── Constancias de buena conducta/
    ├── Constancias de estudios/
    ├── Constancias de inscripcion/
    ├── Constancias de prosecucion inicial/
    ├── Constancias de retiro/
    ├── Constancias de trabajo/
    ├── Historial academico/
    └── Listados de secciones/
```

### Crear Usuario MySQL Dedicado (Recomendado)

Para mayor seguridad, crea un usuario MySQL específico para SIRA:

```sql
-- Accede a MySQL como root
mysql -u root -p

-- Crea el usuario (cambia la contraseña)
CREATE USER 'sira_user'@'localhost' IDENTIFIED BY 'ContraseñaSegura123';

-- Dale permisos sobre la base de datos
GRANT ALL PRIVILEGES ON SIRA_DB.* TO 'sira_user'@'localhost';

-- Aplica los cambios
FLUSH PRIVILEGES;
EXIT;
```

Luego actualiza tu archivo `.env`:

```env
DB_HOST=localhost
DB_USER=sira_user
DB_PASS=ContraseñaSegura123
DB_NAME=SIRA_DB
```

### Configuración Institucional

Una vez iniciado SIRA con tu usuario administrador:

1. **Ir a Administración** → **Datos Institucionales**
2. **Completar información:**
   - Nombre de la institución
   - RIF de la institución
   - Dirección y teléfono
   - Nombre y cédula del director
   - Códigos oficiales (DEA, dependencia, estadístico)
   - Logo institucional (opcional)
3. **Guardar cambios**

> 📄 Esta información aparecerá en todas las constancias y certificados generados.

---

### 🔧 Solución de Problemas

<details>
<summary><strong>❌ "No se pudo conectar a la base de datos"</strong></summary>

- ✅ Verifica que MySQL esté ejecutándose
- ✅ Confirma que el archivo `.env` esté en la misma carpeta que el ejecutable
- ✅ Revisa que usuario y contraseña en `.env` sean correctos
- ✅ Asegúrate de que el usuario tenga permisos sobre la base de datos

</details>

<details>
<summary><strong>❌ "Unknown database 'SIRA_DB'"</strong></summary>

- ✅ Ejecuta: `CREATE DATABASE SIRA_DB CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;`
- ✅ Importa el archivo `schema.sql`

</details>

<details>
<summary><strong>❌ El programa no inicia en Linux</strong></summary>

- ✅ Dale permisos de ejecución: `chmod +x SIRA`
- ✅ Instala las dependencias del sistema si es necesario:
  ```bash
  sudo apt install libxcb-xinerama0 libxcb-cursor0
  ```

</details>

<details>
<summary><strong>❌ "Variables de entorno incompletas"</strong></summary>

- ✅ Verifica que el archivo se llame exactamente `.env` (con el punto)
- ✅ Confirma que todas las variables estén definidas
- ✅ No debe haber espacios alrededor del `=`

</details>

---

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT** - ver el archivo [LICENSE](LICENSE) para más detalles.

---

<p align="center">
  <strong>Desarrollado con ❤️ para la gestión educativa</strong>
  <br>
  <sub>© 2025-2026 Proyecto SIRA - UPTJAA</sub>
</p>
