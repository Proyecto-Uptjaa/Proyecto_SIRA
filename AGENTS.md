## 1. Introducción al Proyecto

- **Nombre del Proyecto**: SIRA (Sistema Interno de Registro Académico).
- **Descripción**: Aplicación de escritorio para la gestión interna de un centro educativo. Maneja registros de estudiantes, empleados, usuarios administrativos, secciones académicas, años escolares, auditoría de acciones y exportaciones (PDF/Excel).
- **Objetivo Principal**: Automatizar el registro, consulta y reporte de datos académicos, asegurando trazabilidad mediante auditoría.
- **Estado Actual**: Proyecto en desarrollo como trabajo universitario en Python. Incluye funcionalidades completas para autenticación, CRUD en entidades clave y procesos masivos como promoción de estudiantes.
- **Idioma**: Código en inglés/español mixto (UI en español, código en inglés con comentarios en español).

## 2. Arquitectura General

- **Patrón de Diseño**: MVC implícito (Modelos en `models/`, Vistas en `ui_compiled/` y `views/`, lógica en páginas).
- **Flujo Principal**:
  1. `main.py` lanza la aplicación y muestra `LoginDialog`.
  2. Autenticación exitosa carga `MainWindow` con permisos según rol.
  3. Navegación mediante stack de widgets para cada módulo.
- **Base de Datos**: MySQL. Conexión bajo demanda (`utils/db.py`) con credenciales en `.env`.
- **Seguridad**: Hashing de contraseñas con bcrypt. Estados activo/inactivo. Auditoría automática.
- **UI**: PySide6 + Qt Designer. Efectos visuales (sombras flotantes), proxies para tablas, gráficos con matplotlib.

## 3. Componentes Clave

### 3.1. Módulos Principales
- Autenticación (`login.py`)
- Ventana principal y dashboard (`main_window.py`)
- Gestión de estudiantes (`gestion_estudiantes.py`, `registro_estudiante.py`)
- Gestión de empleados (`gestion_empleados.py`, `registro_empleado.py`)
- Gestión de usuarios (`registro_usuario.py`, `actualizar_usuario.py`)
- Gestión de secciones (`gestion_secciones.py`)
- Gestión de años escolares (`gestion_anio.py`, `anio_model.py`)
- Configuración de institución (`institucion_model.py`)
- Auditoría (`auditoria_model.py`)

### 3.2. Modelos (`models/`)
- `UsuarioModel`: CRUD usuarios + hashing bcrypt
- `EstudianteModel`: Generación de cédula estudiantil, promoción masiva
- `EmpleadoModel`: Cargos predefinidos
- `RepresentanteModel`: Datos del representante
- `SeccionesModel`: Creación/duplicación/desactivación de secciones
- `AnioEscolarModel`: Apertura/cierre de años, promoción automática
- `AuditoriaModel`: Registro automático de acciones
- `InstitucionModel`: Datos únicos de la institución (ID=1)

### 3.3. Utilidades (`utils/`)
- `db.py`: Conexión MySQL
- `security.py`: Funciones bcrypt
- `proxies.py`: Proxy para filtrar inactivos en tablas
- `exportar.py`: Formatos de exportacion

## 4. Funcionalidades Clave

- Registro de estudiante con generación automática de cédula y asignación a sección.
- Promoción masiva al aperturar nuevo año escolar (duplicación de secciones + movimiento de estudiantes).
- Exportación a Excel (tablas filtradas y matrícula completa) y PDF (constancias).
- Filtros avanzados en tablas (texto + mostrar/ocultar inactivos).
- Auditoría automática en casi todas las operaciones CRUD.
- Control de permisos por rol (administrador vs empleado).

## 5. Dependencias Principales

- PySide6
- mysql-connector-python
- bcrypt
- python-dotenv
- matplotlib
- openpyxl
- Otras menores: re, datetime, subprocess

## 6. Directrices para Agentes IA

- Mantén el estilo de código claro, directo y profesional.
- Usa conexiones bajo demanda y registra siempre en auditoría los cambios relevantes.
- No modifiques el esquema de base de datos sin indicar migraciones.
- Respeta el patrón actual de separación (models, views, utils).
- Cuando propongas nuevo código, intégralo con los componentes existentes (señales/slots Qt, validaciones, mensajes QMessageBox).