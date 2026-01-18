# SIRA - Sistema Interno de Registro Académico



**SIRA** (Sistema Interno de Registro Académico) es una aplicación de escritorio desarrollada para la gestión integral de centros educativos. Permite administrar de forma eficiente el registro de estudiantes, empleados, usuarios administrativos, secciones académicas y años escolares, proporcionando herramientas completas para el control académico institucional.

---

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)
![Database](https://img.shields.io/badge/Database-MySQL%208.0%2B-orange?logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success)
![Framework](https://img.shields.io/badge/Framework-PySide6-brightgreen?logo=qt&logoColor=white)

---

## 📑 Tabla de Contenidos
- [Características principales](#características-principales)
- [Tecnologías Utilizadas](#️-tecnologías-utilizadas)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Configuración](#️-configuración)
- [Licencia](#-licencia)

## **Características principales**

### 🔐 Autenticación y Control de Acceso
- Sistema de login seguro con encriptación de contraseñas mediante bcrypt
- Control de permisos basado en roles (Administrador / Empleado)
- Gestión de usuarios con estados activo/inactivo
- Cambio de contraseñas y actualización de perfiles

### 👥 Gestión de Estudiantes
- Registro completo de estudiantes con validación de datos
- Generación automática de cédula estudiantil
- Asignación automática a secciones según grado
- Gestión de representantes con datos de contacto
- Promoción automática masiva de estudiantes entre años escolares
- Movimiento individual de estudiantes entre secciones
- Control de retiros y egresados
- Historial académico completo por estudiante

### 💼 Gestión de Personal
- Registro y administración de empleados
- Cargos predefinidos (Director, Coordinador, Docente, etc.)
- Control de fecha de ingreso y estado laboral
- Fichas detalladas de empleados

### 🏫 Gestión de Secciones Académicas
- Creación de secciones por grado (Inicial, Primaria)
- Duplicación masiva de secciones entre años escolares
- Capacidad máxima de estudiantes por sección
- Activación/desactivación de secciones
- Visualización de estudiantes inscritos por sección

### 📅 Gestión de Años Escolares
- Apertura y cierre de períodos académicos
- Promoción automática de estudiantes al crear nuevo año
- Control de año escolar activo
- Historial de años anteriores

### 📄 Generación de Documentos PDF
- **Para Estudiantes:**
  - Constancia de estudios
  - Constancia de inscripción
  - Constancia de buena conducta
  - Constancia de retiro
  - Constancia de prosecución (Inicial a Primaria)
  - Certificado de promoción de 6to grado
  - Historial académico completo
- **Para Empleados:**
  - Constancia de trabajo

### 📊 Exportación a Excel
- Exportación de tablas filtradas de estudiantes
- Exportación de tablas filtradas de empleados
- Exportación de matrícula completa
- Reporte RAC (Ministerio)

### 🔍 Búsqueda y Filtrado Avanzado
- Búsqueda en tiempo real por múltiples criterios
- Filtros para mostrar/ocultar registros inactivos
- Sistema de proxy para tablas con filtrado inteligente
- Ordenamiento por columnas

### 📈 Dashboard y Estadísticas
- Gráficos estadísticos con matplotlib
- Resumen de estudiantes activos e inactivos
- Resumen de empleados por cargo
- Visualización de distribución por sección

### 🔒 Auditoría y Trazabilidad
- Registro automático de todas las operaciones CRUD
- Seguimiento de acciones por usuario
- Marcas de tiempo de creación y modificación
- Historial completo de cambios

### ⚙️ Configuración Institucional
- Datos de la institución (nombre, director, contacto)
- Personalización de encabezados en documentos
- Configuración única y centralizada

### 🎨 Interfaz Gráfica Moderna
- Diseño intuitivo con PySide6/Qt
- Efectos visuales
- Navegación fluida entre módulos
- Validación de formularios en tiempo real
- Mensajes de confirmación y alertas contextuales


## 🛠️ Tecnologías Utilizadas

### Lenguaje
- **Python 3.12** - Lenguaje principal del proyecto

### Framework GUI
- **PySide6 6.8.2** - Framework Qt para interfaces gráficas modernas y multiplataforma

### Base de Datos
- **MySQL** - Sistema de gestión de base de datos relacional
- **mysql-connector-python 9.5.0** - Conector Python para MySQL

### Bibliotecas Principales
- **bcrypt 5.0.0** - Encriptación y hashing seguro de contraseñas
- **matplotlib 3.7+** - Generación de gráficos estadísticos
- **ReportLab 4.4.5** - Creación de documentos PDF (constancias, certificados, reportes)
- **openpyxl 3.1.5** - Exportación y manipulación de archivos Excel
- **python-dotenv 1.2.1** - Gestión de variables de entorno y configuración

### Herramientas de Desarrollo
- **PyInstaller 6.3.0** - Empaquetado de la aplicación en ejecutable standalone

---

## 📋 Requisitos Previos

Antes de instalar y ejecutar SIRA, asegúrate de tener instalado lo siguiente:

### Software Requerido
- **Python 3.8 o superior** - [Descargar Python](https://www.python.org/downloads/)
- **MySQL 8.0 o superior** - [Descargar MySQL](https://dev.mysql.com/downloads/)
- **pip** - Gestor de paquetes de Python (incluido con Python)

### Sistema Operativo
- Windows 10/11
- Linux (Ubuntu 20.04+, Debian, Fedora)

### Espacio en Disco
- Mínimo 500 MB libres para la aplicación y dependencias
- Espacio adicional según tamaño de la base de datos

### Conocimientos Recomendados
- Conocimientos básicos de MySQL para configuración inicial
- Acceso de administrador/sudo para instalación de dependencias

## 📦 Instalación

Sigue estos pasos para instalar SIRA en tu sistema:

### 1️⃣ Descargar SIRA

1. Ve a la [página de Releases](https://github.com/Proyecto-Uptjaa/Proyecto_SIRA/releases) del proyecto
2. Descarga la última versión disponible:
   - **Windows:** `SIRA-v1.0.0-Windows.zip`
   - **Linux:** `SIRA-v1.0.0-Linux.zip`

### 2️⃣ Extraer los Archivos

**Windows:**
- Haz clic derecho en el archivo descargado → **Extraer todo...**
- Elige una ubicación (ej: `C:\Archivos de programa\SIRA`)

**Linux:**
```bash
# Extraer el archivo
unzip SIRA-v1.0.0-Linux.zip -d ~/SIRA

# Dar permisos de ejecución
cd ~/SIRA
chmod +x SIRA
```

### 3️⃣ Configurar la Base de Datos

#### Crear la Base de Datos en MySQL

**Windows (PowerShell o CMD):**
```powershell
# Acceder a MySQL
mysql -u root -p

# Dentro del prompt de MySQL, ejecutar:
CREATE DATABASE sira_db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
EXIT;
```

**Linux:**
```bash
# Acceder a MySQL
mysql -u root -p

# Dentro del prompt de MySQL, ejecutar:
CREATE DATABASE sira_db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
EXIT;
```

#### Importar la Estructura de la Base de Datos

Dentro de la carpeta extraída encontrarás un archivo llamado schema.sql. Impórtalo:

**Windows:**
```powershell
# Navegar a la carpeta de SIRA
cd "C:\Archivos de programa\SIRA"

# Importar la estructura
mysql -u root -p sira_db < schema.sql
```

**Linux:**
```bash
# Navegar a la carpeta de SIRA
cd ~/SIRA

# Importar la estructura
mysql -u root -p sira_db < schema.sql
```

> 💡 **Nota:** Cuando te pida la contraseña, ingresa la contraseña de tu usuario root de MySQL.

### 4️⃣ Configurar el Archivo de Conexión

Crea un archivo llamado .env en la **misma carpeta donde está el ejecutable** de SIRA.

**Windows:**
```powershell
# Dentro de la carpeta de SIRA
notepad .env
```

**Linux:**
```bash
# Dentro de la carpeta de SIRA
nano .env
```

Copia y pega el siguiente contenido, **reemplazando los valores** con tus datos de MySQL:

```env
DB_HOST=localhost
DB_USER=root
DB_PASS=tu_contraseña_mysql
DB_NAME=sira_db
```

Guarda el archivo (en Notepad: Archivo → Guardar, en nano: `Ctrl+O`, `Enter`, `Ctrl+X`).

### 5️⃣ Ejecutar SIRA por Primera Vez

**Windows:**
- Doble clic en `SIRA.exe`

**Linux:**
```bash
./SIRA
```

### 6️⃣ Crear Usuario Administrador

Al ejecutar SIRA por primera vez, si no detecta usuarios:
1. Cierra el programa
2. Ejecuta el script de inicialización incluido:

**Windows:**
```powershell
init_admin.exe
```

**Linux:**
```bash
./init_admin
```

3. Sigue las instrucciones para crear tu usuario administrador
4. Vuelve a ejecutar SIRA e inicia sesión con tus credenciales

---

## ⚙️ Configuración

### Archivo .env

El archivo .env debe estar ubicado en la **misma carpeta que el ejecutable** `SIRA.exe` (Windows) o `SIRA` (Linux).

#### Estructura del Archivo

```env
# Configuración de conexión a MySQL
DB_HOST=localhost
DB_USER=root
DB_PASS=tu_contraseña_mysql
DB_NAME=sira_db
```

#### Descripción de Variables

| Variable | Descripción | Valor Recomendado |
|----------|-------------|-------------------|
| `DB_HOST` | Dirección del servidor MySQL | `localhost` (si MySQL está en la misma PC) |
| `DB_USER` | Usuario de MySQL | `root` (o tu usuario MySQL) |
| `DB_PASS` | Contraseña de MySQL | Tu contraseña de MySQL |
| `DB_NAME` | Nombre de la base de datos | `sira_db` (no cambiar) |

#### Ejemplo de Configuración

```env
DB_HOST=localhost
DB_USER=root
DB_PASS=MiContraseña123
DB_NAME=sira_db
```

> ⚠️ **Importante:** 
> - El archivo .env NO debe tener extensión `.txt`
> - En Windows, asegúrate de mostrar extensiones de archivo para verificar
> - Guarda el archivo con codificación UTF-8

### Estructura de Carpetas

Después de extraer, tu carpeta debe verse así:

```
SIRA/
├── SIRA.exe (Windows) o SIRA (Linux)
├── init_admin.exe (Windows) o init_admin (Linux)
├── schema.sql
├── .env (lo creas tú)
└── ... (otros archivos del sistema)
```

### Configuración de MySQL

#### Crear Usuario Específico (Recomendado)

Para mayor seguridad, crea un usuario MySQL dedicado para SIRA:

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

Luego actualiza tu archivo .env:

```env
DB_HOST=localhost
DB_USER=sira_user
DB_PASS=ContraseñaSegura123
DB_NAME=sira_db
```

### Configuración Institucional

Una vez iniciado SIRA con tu usuario administrador:

1. **Ir a Administración:**
   - Clic en el botón **Admin** en la barra lateral
   - Selecciona **Datos Institucionales**

2. **Completar Información:**
   - Nombre de la institución
   - RIF de la institución
   - Dirección y datos de contacto
   - Nombre y cédula del director

3. **Guardar:**
   - Clic en **Modificar datos**
   - Edita los campos
   - Clic en **Guardar cambios**

> 📄 **Nota:** Esta información aparecerá en todas las constancias y certificados generados por el sistema.

### Solución de Problemas

#### "No se pudo conectar a la base de datos"
- ✅ Verifica que MySQL esté ejecutándose
- ✅ Confirma que el archivo .env esté en la misma carpeta que el ejecutable
- ✅ Revisa que usuario y contraseña en .env sean correctos

#### "Unknown database 'sira_db'"
- ✅ Asegúrate de haber ejecutado el comando `CREATE DATABASE sira_db;`
- ✅ Verifica que importaste el archivo schema.sql

#### El programa no inicia en Linux
- ✅ Dale permisos de ejecución: `chmod +x SIRA`
- ✅ Instala las dependencias del sistema si es necesario

#### "Error: Variables de entorno incompletas"
- ✅ Verifica que el archivo se llame exactamente .env (con el punto al inicio)
- ✅ Confirma que todas las variables estén definidas (DB_HOST, DB_USER, DB_PASS, DB_NAME)

---
## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.
