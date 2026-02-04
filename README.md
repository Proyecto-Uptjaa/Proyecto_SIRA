# SIRA - Sistema de Información para el Registro Académico

<p align="center">
  <strong>Sistema integral de gestión académica para instituciones educativas de Educación Inicial y Primaria</strong>
</p>

---

**SIRA** (Sistema de Información para el Registro Académico) es una aplicación de escritorio multiplataforma desarrollada para la gestión integral de centros educativos. Permite administrar de forma eficiente el registro de estudiantes, empleados, representantes, secciones académicas, años escolares, materias y calificaciones, proporcionando herramientas completas para el control académico institucional.

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
- [Módulos del Sistema](#-módulos-del-sistema)
- [Tecnologías Utilizadas](#️-tecnologías-utilizadas)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Configuración](#️-configuración)
- [Licencia](#-licencia)

## ✨ Características Principales

### 🔐 Autenticación y Control de Acceso
- Sistema de login seguro con encriptación de contraseñas mediante **bcrypt**
- Control de permisos basado en roles (**Administrador** / **Empleado**)
- Gestión de usuarios con estados activo/inactivo
- Bloqueo temporal tras intentos fallidos de inicio de sesión
- Cambio de contraseñas y actualización de perfiles

### 👨‍🎓 Gestión de Estudiantes
- Registro completo de estudiantes con validación de datos en tiempo real
- Generación automática de **cédula estudiantil** con formato único
- Asignación automática a secciones según grado y disponibilidad
- **Promoción automática masiva** de estudiantes entre años escolares
- Movimiento individual de estudiantes entre secciones
- Control de retiros con registro de motivos
- Gestión de **egresados** (estudiantes que culminan 6to grado)
- Historial académico completo por estudiante
- Historial de calificaciones por materia y lapso

### 💼 Gestión de Personal
- Registro y administración de empleados con ficha detallada
- Catálogo de **cargos predefinidos**
- Asignación de docentes a secciones académicas
- Control de fecha de ingreso y estado laboral (activo/inactivo)
- Fichas detalladas con información completa del empleado

### 🏫 Gestión de Secciones Académicas
- Creación de secciones por nivel (**Educación Inicial** y **Primaria**)
- Grados configurables: Inicial (1er, 2do, 3er Nivel) y Primaria (1ero a 6to)
- Asignación de letras de sección (A-Z o Única)
- **Duplicación masiva** de secciones entre años escolares
- Control de capacidad máxima de estudiantes por sección (1-50)
- Activación/desactivación de secciones
- Visualización de estudiantes inscritos por sección
- Exportación de listados de estudiantes por sección

### 📅 Gestión de Años Escolares
- Apertura y cierre de períodos académicos
- Control de año escolar activo (solo uno puede estar activo)
- **Promoción automática** de estudiantes al crear nuevo año:
  - Estudiantes de 6to grado → Egresados
  - Resto → Promoción al grado siguiente
- Duplicación automática de secciones al nuevo año
- Historial completo de años escolares anteriores

### 📚 Gestión de Materias (Solo Primaria)
- Catálogo de materias configurable por grado
- Asignación de materias a secciones específicas
- Sistema de evaluación **literal** (A, B, C, D, E)
- Activación/desactivación de materias
- Resumen visual de grados asociados a cada materia

### 📝 Gestión de Calificaciones (Solo Primaria)
- Registro de notas por **3 lapsos** académicos
- Sistema de notas literales: A (Excelente) a E (Deficiente)
- **Cálculo automático de nota final** al completar los 3 lapsos
- Indicador de aprobación (A, B, C = Aprobado | D, E = Reprobado)
- Visualización por sección y materia
- Registro de usuario que carga las notas
- Historial de calificaciones exportable a PDF

### 📄 Generación de Documentos PDF
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
- Exportación de tablas filtradas de estudiantes
- Exportación de tablas filtradas de empleados
- Exportación de matrícula completa del año escolar
- Exportación de listado de egresados
- **Reporte RAC** (Registro de Asignación de Cargos - Ministerio)

### 🔍 Búsqueda y Filtrado Avanzado
- Búsqueda en tiempo real por múltiples criterios
- Filtros por columna específica (nombre, cédula, grado, etc.)
- Opción para mostrar/ocultar registros inactivos
- Sistema de proxy inteligente para filtrado de tablas
- Ordenamiento por cualquier columna

### 📈 Dashboard y Estadísticas
- Panel principal con resumen estadístico
- Contadores de estudiantes (activos, inactivos, Egresados)
- Contadores de empleados (activos/inactivos, por cargo)
- **Gráficos interactivos** con matplotlib:
  - Distribución por nivel educativo
  - Distribución por grado
  - Distribución por sección
  - Género de estudiantes
  - Comparativas entre períodos

### 🔒 Auditoría y Trazabilidad
- Registro automático de **todas las operaciones CRUD**
- Seguimiento de acciones por usuario
- Marcas de tiempo de creación y modificación
- Historial completo de cambios consultable
- Registro de accesos al sistema

### 💾 Sistema de Respaldos
- **Backups automáticos** programados (cada 3 días)
- Backups manuales desde el menú de administración
- Formato SQL compatible con MySQL
- Rotación automática (máximo 30 backups guardados)

### ⚙️ Configuración Institucional
- Datos de la institución (nombre, RIF, dirección)
- Información del director y cédula
- Códigos oficiales (DEA, dependencia, estadístico)
- Logo institucional (aparece en todos los documentos)
- Configuración única y centralizada

### 🎨 Interfaz Gráfica Moderna
- Diseño intuitivo con **PySide6/Qt 6**
- Efectos visuales (sombras, animaciones de transición)
- Navegación fluida mediante barra lateral
- Iconografía consistente en todo el sistema
- Validación de formularios en tiempo real
- Mensajes de confirmación y alertas contextuales

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
| **matplotlib** | 3.7+ | Generación de gráficos estadísticos interactivos |
| **ReportLab** | 4.4.5 | Creación de documentos PDF (constancias, certificados) |
| **openpyxl** | 3.1.5 | Exportación y manipulación de archivos Excel |
| **python-dotenv** | 1.2.1 | Gestión de variables de entorno y configuración |

### Herramientas de Desarrollo
| Herramienta | Versión | Uso |
|-------------|---------|-----|
| **PyInstaller** | 6.3.0 | Empaquetado de la aplicación en ejecutable standalone |
| **Qt Designer** | - | Diseño visual de interfaces (archivos .ui) |

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
CREATE DATABASE sira_db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
EXIT;
```

#### Importar la Estructura

Dentro de la carpeta extraída encontrarás `schema.sql`. Impórtalo:

<details>
<summary><strong>🪟 Windows (PowerShell)</strong></summary>

```powershell
cd "C:\Archivos de programa\SIRA"
mysql -u root -p sira_db < schema.sql
```

</details>

<details>
<summary><strong>🐧 Linux</strong></summary>

```bash
cd ~/SIRA
mysql -u root -p sira_db < schema.sql
```

</details>

> 💡 **Nota:** Ingresa la contraseña de tu usuario root de MySQL cuando se solicite.

### 4️⃣ Configurar el Archivo de Conexión

Crea un archivo llamado `.env` en la **misma carpeta donde está el ejecutable**:

```env
DB_HOST=localhost
DB_USER=root
DB_PASS=tu_contraseña_mysql
DB_NAME=sira_db
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

Al ejecutar SIRA por primera vez, si no detecta usuarios en la base de datos:

1. Se mostrará automáticamente el **asistente de configuración inicial**
2. Complete los datos de la institución (nombre, director, códigos)
3. Cree el usuario administrador principal
4. ¡Listo! Ya puede iniciar sesión y usar el sistema

> 📌 Si por alguna razón necesita reiniciar la configuración, puede ejecutar `init_admin.exe` (Windows) o `./init_admin` (Linux).

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
DB_NAME=sira_db
```

#### Descripción de Variables

| Variable | Descripción | Valor por Defecto |
|----------|-------------|-------------------|
| `DB_HOST` | Dirección del servidor MySQL | `localhost` |
| `DB_USER` | Usuario de MySQL | `root` |
| `DB_PASS` | Contraseña de MySQL | *(requerido)* |
| `DB_NAME` | Nombre de la base de datos | `sira_db` |

> ⚠️ **Importante:** 
> - El archivo `.env` NO debe tener extensión `.txt`
> - Guarda el archivo con codificación **UTF-8**
> - En Windows, asegúrate de mostrar extensiones de archivo para verificar

### Estructura de Carpetas

Después de la instalación, tu carpeta debe verse así:

```
SIRA/
├── SIRA.exe (Windows) o SIRA (Linux)    # Ejecutable principal
├── init_admin.exe / init_admin          # Script de inicialización
├── schema.sql                           # Estructura de la BD
├── .env                                 # Archivo de configuración
├── backups/                             # Respaldos automáticos
└── exportados/                          # Documentos generados
    ├── Constancias de estudios/
    ├── Constancias de inscripcion/
    ├── Constancias de trabajo/
    ├── Certificados de promocion/
    ├── Historial academico/
    ├── Listados de secciones/
    └── ...
```

### Crear Usuario MySQL Dedicado (Recomendado)

Para mayor seguridad, crea un usuario MySQL específico para SIRA:

```sql
-- Accede a MySQL como root
mysql -u root -p

-- Crea el usuario (cambia la contraseña)
CREATE USER 'sira_user'@'localhost' IDENTIFIED BY 'ContraseñaSegura123';

-- Dale permisos sobre la base de datos
GRANT ALL PRIVILEGES ON sira_db.* TO 'sira_user'@'localhost';

-- Aplica los cambios
FLUSH PRIVILEGES;
EXIT;
```

Luego actualiza tu archivo `.env`:

```env
DB_HOST=localhost
DB_USER=sira_user
DB_PASS=ContraseñaSegura123
DB_NAME=sira_db
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
<summary><strong>❌ "Unknown database 'sira_db'"</strong></summary>

- ✅ Ejecuta: `CREATE DATABASE sira_db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;`
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
  <sub>© 2024-2026 Proyecto SIRA - UPTJAA</sub>
</p>
