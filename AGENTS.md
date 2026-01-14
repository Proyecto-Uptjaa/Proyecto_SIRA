# AGENTS.md — Documentación para Agentes IA

---

## 1. Información General del Proyecto

| Aspecto | Detalle |
|---------|---------|
| **Nombre** | SIRA (Sistema Interno de Registro Académico) |
| **Tipo** | Aplicación de escritorio multiplataforma |
| **Lenguaje** | Python 3.10+ |
| **Framework UI** | PySide6 (Qt 6) con archivos .ui de Qt Designer |
| **Base de Datos** | MySQL 8.0 |
| **Estado** | En desarrollo activo (proyecto universitario) |
| **Licencia** | MIT License |
| **Idioma UI** | Español |
| **Idioma Código** | Inglés (nombres) con comentarios en español |

### Objetivo Principal
Automatizar la gestión académica de un centro educativo: registro de estudiantes, empleados, secciones, años escolares, generación de constancias PDF, exportación a Excel, y auditoría completa de todas las operaciones.

---

## 2. Arquitectura del Sistema

### 2.1 Patrón de Diseño
**MVC Implícito** con separación clara:
```
├── models/          # Lógica de negocio y acceso a datos
├── views/           # Controladores de UI (conectan modelos con UI)
├── ui_compiled/     # Clases Python generadas desde archivos .ui
├── resources/ui/    # Archivos .ui originales (Qt Designer)
├── utils/           # Utilidades transversales
└── main.py          # Punto de entrada
```

### 2.2 Flujo de Ejecución Principal
```
main.py
   ↓
LoginDialog (autenticación con bcrypt)
   ↓ [credenciales válidas]
MainWindow (carga permisos según rol)
   ↓
QStackedWidget (navegación entre módulos)
   ├── Dashboard (estadísticas + gráficos)
   ├── Gestión de Estudiantes
   ├── Gestión de Secciones
   ├── Gestión de Empleados
   ├── Gestión de Años Escolares
   ├── Egresados
   ├── Reportes (gráficos matplotlib)
   └── Administración (usuarios, institución, auditoría)
```

### 2.3 Conexión a Base de Datos
- **Patrón**: Conexiones bajo demanda (no pool persistente)
- **Archivo**: `utils/db.py`
- **Credenciales**: Variables de entorno en `.env`:
  ```env
  DB_HOST=localhost
  DB_USER=root
  DB_PASS=contraseña
  DB_NAME=mi_proyecto
  ```
- **Transacciones**: Manuales con `commit()` / `rollback()` explícitos

---

## 3. Esquema de Base de Datos

### 3.1 Tablas Principales

| Tabla | Descripción | Campos Clave |
|-------|-------------|--------------|
| `usuarios` | Usuarios del sistema | `id`, `username`, `password_hash`, `rol` (super_admin/admin/empleado), `estado` |
| `estudiantes` | Datos de estudiantes | `id`, `cedula`, `nombres`, `apellidos`, `fecha_nac_est`, `representante_id`, `estado`, `estatus_academico` |
| `representantes` | Representantes legales | `id`, `cedula_repre`, `nombres_repre`, `num_contact_repre` |
| `empleados` | Personal del centro | `id`, `cedula`, `nombres`, `cargo`, `titulo`, `estado` |
| `secciones` | Secciones académicas | `id`, `año_escolar_id`, `nivel` (Inicial/Primaria), `grado`, `letra`, `docente_id`, `activo` |
| `anios_escolares` | Años escolares | `id`, `nombre` (ej: "2025-2026"), `estado` (planificado/activo/cerrado), `es_actual` |
| `seccion_estudiante` | Asignación actual | `seccion_id`, `estudiante_id`, `año_asignacion` |
| `historial_secciones` | Historial académico | `estudiante_id`, `seccion_id`, `año_inicio`, `fecha_asignacion` |
| `auditoria` | Log de acciones | `usuario_id`, `accion`, `entidad`, `entidad_id`, `descripcion`, `fecha` |
| `institucion` | Datos del centro (ID=1) | `nombre`, `codigo_dea`, `director`, `director_ci`, `logo` (BLOB) |
| `eventos` | Calendario escolar | `titulo`, `fecha`, `tipo`, `anio_escolar` |

### 3.2 Relaciones Importantes
```
estudiantes.representante_id → representantes.id
secciones.año_escolar_id → anios_escolares.id
secciones.docente_id → empleados.id
seccion_estudiante.seccion_id → secciones.id
seccion_estudiante.estudiante_id → estudiantes.id
historial_secciones.seccion_id → secciones.id
auditoria.usuario_id → usuarios.id
```

### 3.3 Niveles y Grados Válidos
```python
NIVELES = ["Inicial", "Primaria"]
GRADOS_INICIAL = ["1er Nivel", "2do Nivel", "3er Nivel"]
GRADOS_PRIMARIA = ["1ero", "2do", "3ero", "4to", "5to", "6to"]
LETRAS_SECCION = ["A", "B", "C", ..., "Z", "Única"]
```

---

## 4. Modelos de Datos (`models/`)

### 4.1 UsuarioModel (`user_model.py`)
- **Autenticación**: Hashing con `bcrypt` (salt automático)
- **Roles**: `super_admin`, `admin`, `empleado`
- **Validaciones**: 
  - Username único
  - Mínimo un admin activo (no permite quitar rol admin al último)
- **Métodos principales**: `guardar()`, `actualizar()`, `cambiar_estado()`, `listar_todos()`, `autenticar()`

### 4.2 EstudianteModel (`estu_model.py`)
- **Archivo más extenso** (~1400 líneas)
- **Cédula Estudiantil**: Generación automática con formato `{hijo}{año}{cedula_madre}`
- **Estados**: `estado` (activo/inactivo) + `estatus_academico` (Regular/Egresado/Retirado)
- **Métodos principales**:
  - `guardar()`: Registra estudiante + representante + asignación a sección
  - `obtener_por_id()`: Datos completos con sección actual
  - `promover_masivo()`: Promociona estudiantes al siguiente grado
  - `retirar_estudiante()`: Cambia estatus a Retirado con motivo
  - `egresar_estudiantes()`: Marca como Egresados a los de 6to grado
  - `listar_matricula_excel()`: Datos formateados para exportación

### 4.3 SeccionesModel (`secciones_model.py`)
- **Constantes de validación**: Niveles, grados y letras válidas
- **Cupo máximo**: 1-50 estudiantes por sección
- **Métodos principales**:
  - `crear()`: Con validación de duplicados por año escolar
  - `duplicar_para_nuevo_anio()`: Copia secciones al año siguiente
  - `asignar_docente()`: Vincula empleado con cargo docente
  - `cambiar_estado()`: Activar/desactivar sección

### 4.4 AnioEscolarModel (`anio_model.py`)
- **Estados**: `planificado`, `activo`, `cerrado`
- **Regla**: Solo un año puede tener `es_actual = 1`
- **Proceso de Apertura** (`aperturar_nuevo()`):
  1. Desactiva año anterior
  2. Crea nuevo año como activo
  3. Duplica secciones (opcional)
  4. Promociona estudiantes automáticamente
  5. Registra en auditoría

### 4.5 EmpleadoModel (`emple_model.py`)
- **Cargos predefinidos**: Lista de ~24 cargos (DOC II, TSU, OBRERO, etc.)
- **Clasificación docente**: Identifica qué cargos pueden ser docentes de sección
- **Métodos**: `guardar()`, `actualizar()`, `listar_docentes_disponibles()`

### 4.6 AuditoriaModel (`auditoria_model.py`)
- **Acciones registradas**: INSERT, UPDATE, DELETE, LOGIN, STATUS_CHANGE
- **Campos**: `accion`, `entidad`, `entidad_id`, `referencia`, `descripcion`
- **Validaciones estrictas** en `registrar()` para evitar datos corruptos

### 4.7 InstitucionModel (`institucion_model.py`)
- **Registro único** (ID=1)
- **Datos**: nombre, código DEA, director, RIF, logo (binario)
- **Logo**: Almacenado como LONGBLOB, se puede obtener/actualizar

---

## 5. Vistas y Controladores (`views/`)

### 5.1 LoginDialog (`login.py`)
- **Bloqueo temporal**: 3 intentos fallidos → 30 segundos de espera
- **Verifica estado del usuario** (activo/inactivo)
- **Registra acceso exitoso** en auditoría

### 5.2 MainWindow (`main_window.py`)
- **Archivo extenso** (~1200 líneas)
- **Componentes**:
  - Dashboard con estadísticas (DashboardModel)
  - Gráficos con matplotlib embebido
  - Timer global (10s) para actualización automática
  - Timer de backup automático (cada 3 días)
  - Navegación mediante QStackedWidget
- **Permisos**: Oculta/deshabilita opciones según rol

### 5.3 Páginas de Gestión
- `GestionEstudiantesPage`: Lista, búsqueda, filtros, acciones masivas
- `GestionSeccionesPage`: Vista de tarjetas (custom widget)
- `GestionEmpleadosPage`: CRUD completo con ficha de detalles
- `GestionAniosPage`: Apertura/cierre de años escolares
- `Egresados`: Lista de estudiantes egresados con historial

### 5.4 Diálogos de Registro
- `RegistroEstudiante`: Formulario extenso con tabs
- `RegistroEmpleado`: Datos personales y laborales
- `RegistroUsuario`: Creación de usuarios del sistema

---

## 6. Utilidades (`utils/`)

### 6.1 db.py
```python
get_connection()  # Retorna conexión MySQL o None
verificar_conexion()  # Bool para health check
get_user_by_username(username)  # Para login
```

### 6.2 security.py
```python
hash_password(password)  # bcrypt hash
check_password(password, hash)  # bcrypt verify
```

### 6.3 exportar.py (~1900 líneas)
- **PDF con ReportLab**: Constancias de estudio, inscripción, retiro, promoción, trabajo
- **Excel con openpyxl**: Matrícula completa, tablas filtradas
- **Funciones auxiliares**: `sanitizar_nombre_archivo()`, `crear_carpeta_segura()`, `convertir_fecha_string()`

### 6.4 backup.py
```python
BackupManager.crear_backup_manual()  # Exporta .sql con mysqldump
BackupManager.crear_backup_automatico()  # Llamado por timer
BackupManager.limpiar_backups_antiguos()  # Mantiene máximo 30
```

### 6.5 Otros
- `proxies.py`: QSortFilterProxyModel para ocultar registros inactivos
- `sombras.py`: Efectos visuales (QGraphicsDropShadowEffect)
- `dialogs.py`: Factory para QMessageBox estilizados
- `forms.py`: Helpers para formularios (tooltips, validaciones)
- `edad.py`: Cálculo de edad desde fecha de nacimiento
- `tarjeta_seccion.py`: Widget custom para mostrar secciones como tarjetas

---

## 7. Funcionalidades Clave

### 7.1 Promoción Automática de Estudiantes
Al aperturar un nuevo año escolar:
1. Estudiantes de 6to Primaria → Egresados
2. Otros → Promoción al siguiente grado
3. Registro en `historial_secciones` para trazabilidad

### 7.2 Generación de Cédula Estudiantil
Formato: `{número_hijo}{año_nacimiento}{cedula_madre}`
- Ejemplo: `215V12345678` (segundo hijo, nacido 2015, madre CI V12345678)

### 7.3 Exportaciones
| Tipo | Formato | Contenido |
|------|---------|-----------|
| Constancia de Estudios | PDF | Membrete + datos estudiante + nivel actual |
| Constancia de Inscripción | PDF | Confirmación de matrícula |
| Constancia de Retiro | PDF | Motivo y fecha de retiro |
| Certificado de Promoción | PDF | Año cursado y aprobado |
| Constancia de Trabajo | PDF | Datos del empleado |
| Matrícula Completa | Excel | Todos los estudiantes activos |
| Tabla Filtrada | Excel | Lo que se ve en pantalla |

### 7.4 Sistema de Auditoría
Todo cambio crítico se registra:
- Creación/modificación/eliminación de registros
- Cambios de estado (activar/desactivar)
- Accesos al sistema
- Promociones y retiros

---

## 8. Dependencias del Proyecto

```
# requirements.txt (principales)
PySide6==6.8.2              # Framework UI
mysql-connector-python==9.5  # Conexión BD
bcrypt==5.0.0               # Hashing contraseñas
python-dotenv==1.2.1        # Variables de entorno
reportlab==4.4.5            # Generación PDF
openpyxl==3.1.5             # Exportación Excel
matplotlib>=3.7.0           # Gráficos estadísticos
pyinstaller==6.3.0          # Empaquetado ejecutable
```

---

## 9. Estructura de Archivos Relevantes

```
Proyecto_SIRA/
├── main.py                    # Punto de entrada
├── paths.py                   # Rutas absolutas para recursos
├── compilar_ui.py             # Script para compilar .ui → .py
├── requirements.txt           # Dependencias
├── .env                       # Credenciales BD (NO commitear)
│
├── db/
│   └── schema.sql             # Esquema completo de la BD
│
├── models/
│   ├── user_model.py          # Usuarios y autenticación
│   ├── estu_model.py          # Estudiantes (archivo más grande)
│   ├── emple_model.py         # Empleados
│   ├── repre_model.py         # Representantes
│   ├── secciones_model.py     # Secciones académicas
│   ├── anio_model.py          # Años escolares
│   ├── auditoria_model.py     # Sistema de auditoría
│   ├── institucion_model.py   # Datos de la institución
│   └── dashboard_model.py     # Estadísticas para dashboard
│
├── views/
│   ├── login.py               # Diálogo de autenticación
│   ├── main_window.py         # Ventana principal (1200+ líneas)
│   ├── gestion_estudiantes.py # Módulo estudiantes
│   ├── gestion_empleados.py   # Módulo empleados
│   ├── gestion_secciones.py   # Módulo secciones
│   ├── gestion_anio.py        # Módulo años escolares
│   ├── egresados.py           # Módulo egresados
│   ├── registro_estudiante.py # Formulario registro
│   ├── registro_empleado.py   # Formulario registro
│   └── registro_usuario.py    # Formulario registro
│
├── ui_compiled/               # Clases Python generadas
│   ├── main_ui.py
│   ├── login_ui.py
│   └── ... (otros módulos)
│
├── resources/
│   ├── ui/                    # Archivos .ui (Qt Designer)
│   └── icons/                 # Iconos e imágenes
│
├── utils/
│   ├── db.py                  # Conexión a base de datos
│   ├── security.py            # Hashing bcrypt
│   ├── exportar.py            # PDF y Excel (1900+ líneas)
│   ├── backup.py              # Gestión de backups
│   ├── proxies.py             # Filtros para tablas
│   ├── dialogs.py             # MessageBox factory
│   └── forms.py               # Helpers de formularios
│
├── backups/                   # Backups automáticos (.sql)
└── exportados/                # Archivos PDF/Excel generados
    ├── Constancias de estudios/
    ├── Constancias de inscripcion/
    └── ... (subcarpetas por tipo)
```

---

## 10. Directrices para Agentes IA

### 10.1 Estilo de Código
- **Nombres**: Clases en PascalCase, funciones/variables en snake_case
- **Docstrings**: Estilo Google (Args, Returns, Raises)
- **Type hints**: Usar en firmas de funciones (`def func(x: int) -> str:`)
- **Imports**: Separar estándar, terceros, y locales

### 10.2 Patrones a Seguir
```python
# Conexión bajo demanda (NO mantener conexiones abiertas)
conexion = None
cursor = None
try:
    conexion = get_connection()
    if not conexion:
        return False, "Error de conexión"
    cursor = conexion.cursor(dictionary=True)
    # ... operaciones ...
    conexion.commit()
    return True, "Éxito"
except Exception as e:
    if conexion:
        conexion.rollback()
    return False, f"Error: {e}"
finally:
    if cursor:
        cursor.close()
    if conexion and conexion.is_connected():
        conexion.close()

# Siempre registrar en auditoría los cambios
AuditoriaModel.registrar(
    usuario_id=usuario_actual["id"],
    accion="INSERT",
    entidad="nombre_tabla",
    entidad_id=nuevo_id,
    referencia="identificador_legible",
    descripcion="Descripción detallada de la acción"
)
```

### 10.3 Integración con UI
```python
# Señales/slots Qt
self.btnGuardar.clicked.connect(self.on_guardar_clicked)

# Mensajes al usuario
from utils.dialogs import crear_msgbox
crear_msgbox(self, "Título", "Mensaje", QMessageBox.Information).exec()

# Actualizar tablas después de cambios
self.cargar_datos()  # Método que recarga la tabla
```

### 10.4 Reglas Importantes
1. **NO modificar schema.sql** sin documentar la migración necesaria
2. **SIEMPRE cerrar conexiones** en bloque `finally`
3. **SIEMPRE registrar en auditoría** los cambios en datos
4. **Validar entradas** antes de queries SQL (evitar inyección)
5. **Usar transacciones** para operaciones múltiples
6. **Respetar la separación** models/views/utils

### 10.5 Pruebas Manuales
No hay suite de tests automatizados. Para probar:
```bash
# Activar entorno virtual (si existe)
source venv/bin/activate

# Ejecutar aplicación
python main.py

# Compilar archivos .ui después de cambios
python compilar_ui.py
```

---

## 11. Contexto Adicional

### 11.1 Datos de Prueba
Existen scripts para poblar datos de prueba:
- `poblar_db_estu.py`: Genera estudiantes ficticios
- `poblar_db_emple.py`: Genera empleados ficticios
- `init_admin.py`: Crea usuario administrador inicial

### 11.2 Backups
- Automáticos cada 3 días (timer en MainWindow)
- Manuales desde el menú de administración
- Se guardan en `backups/` con formato `backup_TIPO_YYYYMMDD_HHMMSS.sql`
- Se mantienen máximo 30 backups (los más antiguos se eliminan)

### 11.3 Logo de la Institución
- Se almacena como BLOB en tabla `institucion`
- Se puede cargar/actualizar desde el módulo de datos institucionales
- Se usa en encabezados de constancias PDF

---

## 12. Preguntas Frecuentes para Agentes

**P: ¿Cómo agrego un nuevo campo a una tabla?**
R: Modifica `db/schema.sql`, documenta el ALTER TABLE necesario, actualiza el modelo correspondiente en `models/`, y los formularios en `views/` si aplica.

**P: ¿Cómo creo una nueva constancia PDF?**
R: Usa las funciones existentes en `utils/exportar.py` como referencia. Sigue el patrón de `generar_constancia_estudios()`.

**P: ¿Cómo agrego un nuevo módulo/página?**
R: 1) Crea el .ui en Qt Designer, 2) Compila con `python compilar_ui.py`, 3) Crea la vista en `views/`, 4) Agrégala al QStackedWidget en MainWindow.

**P: ¿Cómo manejo permisos por rol?**
R: En MainWindow hay métodos como `configurar_permisos()` que ocultan/deshabilitan widgets según `self.usuario_actual['rol']`.

---