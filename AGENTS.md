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
| **Idioma UI** | Español (todos los botones de diálogos traducidos al español) |
| **Idioma Código** | Inglés (nombres) con comentarios en español |

### Objetivo Principal
Automatizar la gestión académica de un centro educativo: registro de estudiantes, empleados, secciones, años escolares, gestión de materias/áreas de aprendizaje, calificaciones por lapso, generación de constancias PDF, exportación a Excel, reportes estadísticos y auditoría completa de todas las operaciones.

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
├── db/              # Esquema SQL de la base de datos
└── main.py          # Punto de entrada
```

### 2.2 Flujo de Ejecución Principal
```
main.py
   ↓
Verificar conexión a BD → Si falla → Error y salir
   ↓
Verificar si existen usuarios → Si no → Config_inicial (primer uso)
   ↓
LoginDialog (autenticación con bcrypt, bloqueo por intentos)
   ↓ [credenciales válidas]
MainWindow (carga permisos según rol, fuentes Inter)
   ↓
AnimatedStack (navegación animada entre módulos)
   ├── Dashboard (estadísticas + gráficos matplotlib)
   ├── Gestión de Estudiantes (CRUD + filtros + exportación)
   ├── Gestión de Secciones (tarjetas visuales + detalles)
   ├── Gestión de Empleados (CRUD + ficha detallada)
   ├── Gestión de Materias y Áreas de Aprendizaje
   ├── Gestión de Notas/Calificaciones (por sección/materia/lapso)
   ├── Gestión de Años Escolares (apertura/cierre + promoción)
   ├── Egresados (historial + exportaciones)
   ├── Reportes (gráficos barras/torta/texto con matplotlib)
   └── Administración
       ├── Gestión de Usuarios
       ├── Datos Institucionales
       ├── Auditoría
       └── Copias de Seguridad
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
| `usuarios` | Usuarios del sistema | `id`, `username`, `nombre_completo`, `password_hash`, `rol` (Administrador/Empleado), `estado` |
| `estudiantes` | Datos de estudiantes | `id`, `cedula`, `nombres`, `apellidos`, `fecha_nac`, `ciudad`, `genero`, `representante_id`, `estado`, `estatus_academico`, `motivo_retiro`, `fecha_retiro` |
| `representantes` | Representantes legales | `id`, `cedula`, `nombres`, `apellidos`, `fecha_nac`, `genero`, `num_contact`, `email`, `observacion` |
| `empleados` | Personal del centro | `id`, `cedula`, `nombres`, `apellidos`, `cargo`, `titulo`, `tipo_personal` (A/D/O), `codigo_rac`, `horas_acad`, `horas_adm`, `especialidad`, `estado` |
| `secciones` | Secciones académicas | `id`, `año_escolar_id`, `nivel` (Inicial/Primaria), `grado`, `letra`, `salon`, `cupo_maximo`, `docente_id`, `activo` |
| `años_escolares` | Años escolares | `id`, `año_inicio`, `año_fin`, `nombre`, `estado` (planificado/activo/cerrado), `es_actual`, `creado_por`, `cerrado_por` |
| `seccion_estudiante` | Asignación actual | `seccion_id`, `estudiante_id`, `año_asignacion` |
| `historial_secciones` | Historial académico | `id`, `estudiante_id`, `seccion_id`, `año_inicio`, `fecha_asignacion`, `fecha_retiro`, `observaciones` |
| `areas_aprendizaje` | Áreas de aprendizaje | `id`, `nombre`, `abreviatura`, `estado` |
| `materias` | Materias curriculares | `id`, `nombre`, `abreviatura`, `tipo_evaluacion` (numerico/literal), `area_aprendizaje_id`, `estado` |
| `materia_grado` | Materias por nivel/grado | `id`, `materia_id`, `nivel`, `grado` |
| `seccion_materia` | Materias asignadas a sección | `id`, `seccion_id`, `materia_id` |
| `notas` | Calificaciones por lapso | `id`, `estudiante_id`, `seccion_materia_id`, `lapso` (1-3), `nota`, `nota_literal`, `observaciones`, `registrado_por` |
| `notas_finales` | Nota final calculada | `id`, `estudiante_id`, `seccion_materia_id`, `nota_final`, `nota_final_literal`, `aprobado`, `calculado_por` |
| `auditoria` | Log de acciones | `id`, `usuario_id`, `accion`, `entidad`, `entidad_id`, `referencia`, `descripcion`, `fecha` |
| `institucion` | Datos del centro (ID=1) | `nombre`, `codigo_dea`, `director`, `director_ci`, `rif`, `direccion`, `telefono`, `correo`, `logo` (LONGBLOB), `codigo_dependencia`, `codigo_estadistico` |

### 3.2 Relaciones Importantes
```
estudiantes.representante_id → representantes.id
secciones.año_escolar_id → años_escolares.id
secciones.docente_id → empleados.id (opcional)
seccion_estudiante.seccion_id → secciones.id
seccion_estudiante.estudiante_id → estudiantes.id
historial_secciones.seccion_id → secciones.id
historial_secciones.estudiante_id → estudiantes.id
materias.area_aprendizaje_id → areas_aprendizaje.id
materia_grado.materia_id → materias.id
seccion_materia.seccion_id → secciones.id
seccion_materia.materia_id → materias.id
notas.estudiante_id → estudiantes.id
notas.seccion_materia_id → seccion_materia.id
notas.registrado_por → usuarios.id
notas_finales.estudiante_id → estudiantes.id
notas_finales.seccion_materia_id → seccion_materia.id
notas_finales.calculado_por → usuarios.id
auditoria.usuario_id → usuarios.id
años_escolares.creado_por → usuarios.id
años_escolares.cerrado_por → usuarios.id
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
- **Roles**: `Administrador`, `Empleado`
- **Validaciones**: Username único, mínimo un admin activo
- **Métodos**:
  - `guardar(usuario_data, usuario_actual)` → Registra nuevo usuario
  - `actualizar(usuario_id, data, usuario_actual)` → Modifica usuario existente
  - `eliminar(usuario_id, usuario_actual)` → Elimina usuario
  - `listar()` → Lista todos los usuarios (tuplas para tabla)
  - `obtener_por_id(usuario_id)` → Datos completos de un usuario
  - `cambiar_estado(usuario_id, nuevo_estado, usuario_actual)` → Activa/desactiva

### 4.2 EstudianteModel (`estu_model.py`)
- **Archivo extenso** (~1300 líneas)
- **Cédula Estudiantil**: Generación automática con formato `{hijo}{año}{cedula_madre}`
- **Estados**: `estado` (activo/inactivo) + `estatus_academico` (Regular/Egresado/Retirado)
- **Métodos**:
  - `generar_cedula_estudiantil(fecha_nac, cedula_madre)` → Cédula automática
  - `obtener_por_id(estudiante_id)` → Datos completos con sección actual
  - `guardar(...)` → Registra estudiante + representante + asignación a sección
  - `actualizar(...)` → Modifica datos del estudiante y representante
  - `eliminar(estudiante_id, usuario_actual)` → Elimina estudiante con cascada
  - `listar(anio_escolar_id)` → Lista estudiantes (tuplas) por año escolar
  - `listar_activos()` → Solo estudiantes activos con sección
  - `obtener_secciones_activas(año)` → Secciones disponibles para asignar
  - `asignar_a_seccion(estudiante_id, seccion_id, año)` → Asigna a nueva sección
  - `listar_por_seccion(seccion_id, año)` → Estudiantes de una sección
  - `promover_masivo(anio_anterior_id, anio_nuevo_id, usuario_actual)` → Promoción automática (6to→Egresado, otros→siguiente grado)
  - `listar_egresados()` → Lista de egresados con historial
  - `devolver_estudiante(estudiante_id, seccion_id, año, usuario_actual)` → Reasigna a sección inferior (repitencia)
  - `obtener_historial_estudiante(estudiante_id)` → Historial completo de secciones

### 4.3 EmpleadoModel (`emple_model.py`)
- **Cargos predefinidos**: ~24 opciones (DOC II, TSU, OBRERO, etc.) en `CARGO_OPCIONES`
- **Tipos de personal**: `A` (Administrativo), `D` (Docente), `O` (Obrero)
- **Especialidades**: ESPECIALISTA DEPORTE, TEATRO, MÚSICA, DANZA
- **Métodos**:
  - `es_docente(tipo_personal)` → Verifica si es tipo D
  - `listar_docentes_disponibles()` → Docentes activos para asignar a secciones
  - `guardar(empleado_data, usuario_actual)` → Registra nuevo empleado
  - `obtener_por_id(empleado_id)` → Datos completos
  - `actualizar(empleado_id, data, usuario_actual)` → Modifica empleado
  - `eliminar(empleado_id, usuario_actual)` → Elimina empleado
  - `listar()` → Todos los empleados (tuplas para tabla)
  - `listar_activos()` → Solo empleados activos (diccionarios)

### 4.4 RepresentanteModel (`repre_model.py`)
- **Métodos**:
  - `buscar_por_cedula(cedula)` → Busca representante existente
  - `obtener_representante(representante_id)` → Datos completos
  - `actualizar_representante(representante_id, data, usuario_actual)` → Modifica datos
  - `obtener_representante_id(estudiante_id)` → ID del representante de un estudiante
  - `contar_hijos(representante_id)` → Número de estudiantes asociados
  - `obtener_estudiantes_del_representante(representante_id)` → Lista de hijos/representados

### 4.5 SeccionesModel (`secciones_model.py`)
- **Constantes**: `NIVELES_VALIDOS`, `GRADOS_INICIAL`, `GRADOS_PRIMARIA`, `LETRAS_VALIDAS`
- **Cupo máximo**: Configurable (1-50, default 30)
- **Métodos**:
  - `obtener_todas(anio_escolar_id, solo_activas)` → Todas las secciones del año
  - `crear(...)` → Nueva sección con validación de duplicados
  - `reactivar(seccion_id, salon, cupo, usuario_actual)` → Reactiva sección inactiva
  - `desactivar(seccion_id, usuario_actual)` → Desactiva (solo si no tiene estudiantes)
  - `obtener_años_disponibles()` → Años escolares con secciones
  - `obtener_por_clave(nivel, grado, letra, anio_id)` → Busca por clave compuesta
  - `obtener_por_id(seccion_id)` → Datos completos de sección
  - `asignar_docente(seccion_id, empleado_id, usuario_actual)` → Asigna/desasigna docente
  - `obtener_docente_asignado(seccion_id)` → Docente actual de la sección
  - `verificar_cupo(seccion_id, cursor)` → Verifica disponibilidad de cupo
  - `contar_activas_año_actual()` → Total de secciones activas

### 4.6 AnioEscolarModel (`anio_model.py`)
- **Estados**: `planificado`, `activo`, `cerrado`
- **Regla**: Solo un año puede tener `es_actual = 1`
- **Métodos**:
  - `obtener_actual()` → Año escolar vigente
  - `obtener_por_id(anio_id)` → Datos de un año específico
  - `listar_todos(order_desc)` → Todos los años escolares
  - `aperturar_nuevo(año_inicio, usuario_actual)` → Proceso completo de apertura: desactiva anterior, crea nuevo, duplica secciones con materias, promueve estudiantes, registra auditoría
  - `obtener_proximo_año()` → Calcula el siguiente año disponible

### 4.7 AreaAprendizajeModel (`areas_model.py`)
- **Tabla**: `areas_aprendizaje`
- **Métodos**:
  - `crear(nombre, abreviatura, usuario_actual)` → Nueva área (nombre único, mín. 3 caracteres)
  - `actualizar(area_id, nombre, abreviatura, usuario_actual)` → Modifica área
  - `cambiar_estado(area_id, activo, usuario_actual)` → Activa/desactiva
  - `listar_todas(solo_activas)` → Lista áreas con conteo de materias
  - `obtener_por_id(area_id)` → Datos de un área
  - `obtener_materias_por_area(area_id)` → Materias asociadas al área

### 4.8 MateriasModel (`materias_model.py`)
- **Constantes**: `GRADOS_PRIMARIA`, `NOTAS_LITERALES` (A-E)
- **Tipo evaluación**: `numerico` o `literal`
- **Métodos**:
  - `crear(nombre, abreviatura, tipo_evaluacion, grados, area_id, usuario_actual)` → Nueva materia con grados asociados
  - `actualizar(materia_id, nombre, abreviatura, tipo_evaluacion, grados, area_id, usuario_actual)` → Modifica materia y reasigna grados
  - `cambiar_estado(materia_id, activo, usuario_actual)` → Activa/desactiva
  - `obtener_por_id(materia_id)` → Datos completos con grados
  - `listar_todas(solo_activas)` → Todas las materias con área asociada
  - `obtener_por_nivel_grado(nivel, grado)` → Materias válidas para un nivel/grado
  - `asignar_a_seccion(seccion_id, materia_ids, usuario_actual)` → Asigna materias a sección (reemplaza existentes)
  - `obtener_materias_seccion(seccion_id)` → Materias de una sección
  - `obtener_ids_materias_seccion(seccion_id)` → Solo IDs
  - `duplicar_materias_seccion(seccion_origen_id, seccion_destino_id, cursor)` → Copia materias entre secciones (usado en apertura de año)

### 4.9 NotasModel (`notas_model.py`)
- **Constantes**: `NOTAS_LITERALES_VALIDAS` (A-E), `NOTA_MINIMA_APROBATORIA` (C)
- **Archivo extenso** (~816 líneas)
- **Métodos**:
  - `registrar_nota(estudiante_id, seccion_materia_id, lapso, nota, nota_literal, observaciones, usuario_actual)` → Registra o actualiza una nota (INSERT ON DUPLICATE UPDATE)
  - `registrar_notas_masivo(notas_list, usuario_actual)` → Registro masivo de notas en una transacción
  - `obtener_notas_seccion_materia(seccion_id, materia_id, lapso)` → Notas de todos los estudiantes de una sección/materia
  - `obtener_notas_estudiante(estudiante_id)` → Todas las notas de un estudiante
  - `calcular_nota_final(estudiante_id, seccion_materia_id, usuario_actual)` → Calcula nota final promediando 3 lapsos
  - `calcular_notas_finales_seccion(seccion_id, materia_id, usuario_actual)` → Calcula finales para toda la sección
  - `obtener_estadisticas_seccion(seccion_id, materia_id)` → Estadísticas (promedio, aprobados, reprobados)
  - `obtener_boletin_estudiante(estudiante_id, anio_escolar_id)` → Boletín completo con todas las materias y notas

### 4.10 RegistroBase (`registro_base.py`)
- **Operaciones genéricas** sobre registros
- **Tablas permitidas**: `usuarios`, `estudiantes`, `empleados`, `secciones`, `representantes`
- **Métodos**:
  - `cambiar_estado(tabla, id_registro, nuevo_estado, usuario_actual)` → Cambio de estado genérico con auditoría

### 4.11 AuditoriaModel (`auditoria_model.py`)
- **Acciones registradas**: INSERT, UPDATE, DELETE, LOGIN, STATUS_CHANGE
- **Campos**: `accion`, `entidad`, `entidad_id`, `referencia`, `descripcion`
- **Métodos**:
  - `listar(limit, offset)` → Registros de auditoría paginados
  - `registrar(usuario_id, accion, entidad, entidad_id, referencia, descripcion)` → Registra evento con validaciones estrictas
  - `contar_total()` → Total de registros

### 4.12 DashboardModel (`dashboard_model.py`)
- **Métodos**:
  - `obtener_todo_dashboard()` → Datos completos del dashboard (conteos, distribuciones, secciones, actividad reciente)
  - `obtener_estadisticas_estudiantes()` → Distribución por género, nivel, grado, estatus
  - `obtener_estadisticas_empleados()` → Distribución por tipo, cargo

### 4.13 InstitucionModel (`institucion_model.py`)
- **Registro único** (ID=1)
- **Métodos**:
  - `actualizar(institucion_id, data, usuario_actual)` → Actualiza datos con auditoría detallada de cambios
  - `obtener_por_id(institucion_id)` → Datos completos
  - `inicializar_si_no_existe()` → Crea registro vacío si no existe

---

## 5. Vistas y Controladores (`views/`)

### 5.1 LoginDialog (`login.py`)
- **Clase**: `LoginDialog(QDialog, Ui_login)`
- **Bloqueo temporal**: 3 intentos fallidos → 30 segundos de espera
- **Verifica estado del usuario** (activo/inactivo)
- **Registra acceso exitoso** en auditoría

### 5.2 Config_inicial (`config_inicial.py`)
- **Clase**: `Config_inicial(QDialog, Ui_config_inicial)`
- **Se muestra al primer uso** (sin usuarios en BD)
- **Configura**: datos institucionales + usuario administrador inicial
- **Validaciones extensas** de todos los campos

### 5.3 MainWindow (`main_window.py`)
- **Clase**: `MainWindow(QMainWindow, Ui_MainWindow)`
- **Archivo extenso** (~1300 líneas)
- **Componentes**:
  - Dashboard con estadísticas (DashboardModel) y widget de notificaciones
  - Gráficos con matplotlib embebido (barras, torta, texto)
  - Timer global (10s) para actualización automática del dashboard
  - Timer de backup automático (cada 3 días)
  - Navegación mediante `AnimatedStack` (transiciones animadas)
  - Reportes configurables con múltiples criterios
  - Gestión de usuarios (registro, actualización, cambio de estado)
  - Datos institucionales (carga, edición, guardado)
  - Auditoría (tabla paginada)
  - Backup manual y automático con apertura de carpeta
  - Accesos directos para registro rápido (estudiante, empleado, sección)
- **Permisos**: Oculta/deshabilita opciones según `usuario_actual['rol']`
- **Métodos principales**:
  - `configurar_permisos()` → Configura UI según rol
  - `actualizar_dashboard()` → Refresca estadísticas
  - `actualizar_widget_notificaciones()` → Alertas y avisos
  - `actualizar_anio_escolar()` → Info del año actual
  - `actualizar_criterios()` / `on_criterio_changed()` / `actualizar_reporte()` → Sistema de reportes
  - `on_exportar_reporte()` → Exporta reporte a PDF
  - `registro_usuario()` / `actualizar_usuario()` / `cambiar_estado_usuario()` → CRUD usuarios
  - `database_usuarios()` → Carga tabla de usuarios
  - `cargar_auditoria(limit)` → Tabla de auditoría
  - `cargar_datos_institucion()` / `guardar_datos_institucion()` / `toggle_edicion()` → Datos institucionales
  - `cargar_info_backup()` / `realizar_backup_manual()` / `realizar_backup_automatico()` → Backups
  - `acceso_directo_registro_estudiante()` / `acceso_directo_registro_empleado()` / `acceso_directo_crear_seccion()` → Atajos
  - `cerrar_sesion()` → Logout con confirmación
  - `mostrar_acerca_de()` → Diálogo "Acerca de"

### 5.4 GestionEstudiantesPage (`gestion_estudiantes.py`)
- **Clase**: `GestionEstudiantesPage(QWidget, Ui_gestion_estudiantes)`
- Lista de estudiantes con búsqueda, filtros por nivel/grado/estado
- Acciones: registrar, editar (abre DetallesEstudiante), eliminar con confirmación
- Proxy de filtrado para ocultar inactivos

### 5.5 DetallesEstudiante (`detalles_estudiante.py`)
- **Clase**: `DetallesEstudiante(QDialog, Ui_ficha_estu)`
- Ficha completa del estudiante con pestañas (datos personales, representante, historial)
- Funcionalidades: editar datos, activar/desactivar (switch), retirar con motivo, eliminar
- Devolver estudiante a sección inferior (repitencia)
- Exportar constancias PDF (estudios, inscripción, retiro, promoción, buena conducta, prosecución inicial)
- Generar historial académico PDF
- Generar historial de notas PDF
- Botón abrir archivo generado directamente

### 5.6 GestionEmpleadosPage (`gestion_empleados.py`)
- **Clase**: `GestionEmpleadosPage(QWidget, Ui_gestion_empleados)`
- Lista de empleados con búsqueda y filtros
- CRUD completo, exportación Excel, generar reporte RAC (Excel)

### 5.7 DetallesEmpleado (`detalles_empleados.py`)
- **Clase**: `DetallesEmpleado(QDialog, Ui_ficha_emple)`
- Ficha completa con pestañas (datos personales, datos laborales)
- Editar, activar/desactivar (switch), eliminar, generar constancia de trabajo PDF

### 5.8 GestionSeccionesPage (`gestion_secciones.py`)
- **Clase**: `GestionSeccionesPage(QWidget, Ui_secciones)`
- Vista de secciones como tarjetas visuales (`TarjetaSeccion`)
- Filtros por nivel, año escolar
- Navega a `DetallesSeccion` al hacer clic en una tarjeta

### 5.9 DetallesSeccion (`detalles_seccion.py`)
- **Clases**: `DetallesSeccion(QWidget, Ui_detalle_seccion)`, `DialogMoverEstudiante(QDialog, Ui_mover_estudiante)`
- Muestra información completa de la sección: docente, lista de estudiantes, materias
- Cambiar docente asignado (combo con docentes disponibles)
- Mover estudiante a otra sección (diálogo dedicado)
- Desactivar sección (solo si no tiene estudiantes)
- Exportar listado de estudiantes de la sección (PDF)
- Generar listado PDF con membrete institucional

### 5.10 CrearSeccion (`crear_seccion.py`)
- **Clase**: `CrearSeccion(QDialog, Ui_crear_seccion)`
- Formulario para nueva sección: nivel, grado, letra, salón, cupo, docente
- Detecta secciones inactivas existentes y ofrece reactivarlas
- Asignación de materias al crear (abre `AsignarMateriasDialog`)

### 5.11 AsignarMateriasDialog (`asignar_materias.py`)
- **Clase**: `AsignarMateriasDialog(QDialog, Ui_asignar_materias)`
- Muestra checkboxes de materias disponibles según nivel/grado
- Permite seleccionar/deseleccionar materias para asignar a sección
- Preselecciona materias ya asignadas al editar

### 5.12 GestionMateriasPage (`gestion_materias.py`)
- **Clases**: `GestionMateriasPage(QWidget, Ui_gestion_materias)`, `DialogoMateria(QDialog)`, `DialogoGestionAreas(QDialog)`
- Gestión completa de materias: crear, editar, activar/desactivar
- Tabla de materias con filtros por área y estado
- Diálogo para crear/editar materia: nombre, abreviatura, tipo evaluación, área, grados
- Gestión de áreas de aprendizaje: crear, editar, activar/desactivar (diálogo secundario)

### 5.13 GestionNotasPage (`gestion_notas.py`)
- **Clases**: `GestionNotasPage(QWidget, Ui_gestion_notas)`, `NotaDelegate(QStyledItemDelegate)`
- Selección de sección mediante mini-tarjetas visuales (`TarjetaSeccionMini`)
- Selección de materia y lapso (1, 2, 3)
- Tabla editable de notas con delegate personalizado (solo A-E)
- Coloreo automático: verde (A/B), amarillo (C), rojo (D/E)
- Guardado masivo de notas
- Filtrado de secciones por nivel

### 5.14 GestionAniosPage (`gestion_anio.py`)
- **Clases**: `GestionAniosPage(QWidget, Ui_anio_escolar)`, `ConfirmarAnioDialog(QDialog, Ui_confirmar_anio)`
- Apertura de nuevo año escolar con confirmación
- Proceso automático: duplica secciones, materias y promueve estudiantes

### 5.15 Egresados (`egresados.py`)
- **Clase**: `Egresados(QWidget, Ui_Egresados)`
- Lista de estudiantes egresados con historial
- Búsqueda y filtros, exportación de constancias

### 5.16 Registros
- `RegistroEstudiante` (`registro_estudiante.py`): Formulario extenso con pestañas (datos personales, representante)
- `RegistroEmpleado` (`registro_empleado.py`): Datos personales y laborales con validaciones
- `RegistroUsuario` (`registro_usuario.py`): Creación de usuarios del sistema
- `ActualizarUsuario` (`actualizar_usuario.py`): Edición de usuario existente

### 5.17 Datos Institucionales (`datos_institucionales.py`)
- **Funciones mixtas** (inyectadas en MainWindow):
  - `cargar_datos_institucion()` → Carga datos en formulario
  - `set_campos_editables_institucion()` → Toggle edición
  - `guardar_datos_institucion()` → Guarda con validaciones (email, teléfono, RIF)
  - `toggle_edicion_institucion()` → Alterna modo lectura/edición

### 5.18 Delegates (`delegates.py`)
- **Clases**: `BaseEstadoDelegate`, `EstudianteDelegate`, `EmpleadoDelegate`, `UsuarioDelegate`
- Colorean filas según estado (activo/inactivo) en las tablas
- Cada delegate configura la columna de estado correspondiente

### 5.19 Acerca_de (`acerca_de.py`)
- **Clase**: `Acerca_de(QDialog, Ui_Acerca_de)`
- Diálogo informativo sobre la aplicación

---

## 6. Utilidades (`utils/`)

### 6.1 db.py
```python
get_connection()           # Retorna conexión MySQL o None
verificar_conexion()       # Bool para health check
get_user_by_username(username)  # Para login (con password_hash)
insert_user(username, password_hash, rol)  # Inserción directa de usuario
```

### 6.2 conexion.py
```python
verificar_conexion_bd()    # Health check más robusto con SELECT 1
```

### 6.3 security.py
```python
hash_password(password)    # bcrypt hash con salt automático
check_password(password, hash)  # bcrypt verify
```

### 6.4 exportar.py (~2200 líneas)
- **PDF con ReportLab**: Constancias y certificados
- **Excel con openpyxl**: Exportaciones tabulares
- **Funciones auxiliares**:
  - `sanitizar_nombre_archivo(nombre)` → Limpia caracteres inválidos
  - `crear_carpeta_segura(ruta)` → Crea carpeta de exportación
  - `convertir_fecha_string(fecha)` → Formato legible
  - `formatear_año(año)` → Formato "2025-2026"
  - `extraer_año_escolar(año_escolar)` → Tupla (inicio, fin)
  - `normalizar_cedula(cedula, es_estudiante)` → Formato consistente
  - `validar_datos_exportacion(datos, campos_requeridos)` → Valida antes de generar
- **PDF - Componentes de diseño**:
  - `draw_centered(canvas, text, y, font, size)` → Texto centrado
  - `encabezado(canvas, doc, institucion_id)` → Membrete con logo
  - `pie_pagina(canvas, doc, institucion_id)` → Pie con dirección
  - `encabezado_y_pie(canvas, doc)` → Combina ambos
  - `encabezado_prosecucion(canvas, doc)` → Encabezado especial para prosecución
- **PDF - Constancias y certificados**:
  - `generar_constancia_estudios(estudiante, institucion)` → Constancia de estudios
  - `generar_buena_conducta(estudiante, institucion, año_escolar)` → Constancia de buena conducta
  - `generar_constancia_inscripcion(estudiante, institucion)` → Constancia de inscripción
  - `generar_constancia_prosecucion_inicial(estudiante, institucion, año_escolar)` → Prosecución de nivel Inicial
  - `generar_constancia_trabajo(empleado, institucion)` → Constancia laboral
  - `generar_certificado_promocion_sexto(estudiante, institucion, año_escolar_egreso)` → Certificado de promoción de 6to
  - `generar_constancia_retiro(estudiante, institucion, año_escolar, motivo_retiro)` → Constancia de retiro
  - `generar_historial_estudiante_pdf(estudiante, historial, institucion)` → Historial académico completo
  - `generar_listado_estudiantes_seccion(seccion, estudiantes, docente, institucion)` → Listado de sección
  - `generar_reporte_rac(parent, empleados, institucion)` → Reporte RAC en Excel
  - `generar_historial_notas_pdf(estudiante, notas, institucion)` → Historial de notas/calificaciones
- **PDF - Reportes**:
  - `exportar_reporte_pdf(parent, figure, titulo, criterio, etiquetas, valores, total)` → Reporte gráfico a PDF
- **Excel**:
  - `exportar_tabla_excel(nombre_archivo, encabezados, filas)` → Tabla genérica
  - `exportar_estudiantes_excel(parent, estudiantes)` → Matrícula completa
  - `exportar_empleados_excel(parent, empleados)` → Nómina de empleados

### 6.5 backup.py
```python
BackupManager.get_db_credentials()        # Lee credenciales de .env
BackupManager.crear_carpeta_backup()       # Crea carpeta backups/
BackupManager.limpiar_backups_antiguos()   # Mantiene máximo 30
BackupManager._crear_backup(tipo)          # Ejecuta mysqldump
BackupManager.crear_backup_manual()        # Backup manual
BackupManager.crear_backup_automatico()    # Llamado por timer
BackupManager.obtener_ultimo_backup()      # Info del último backup
BackupManager.contar_backups()             # Total de backups existentes
```

### 6.6 dialogs.py
```python
crear_msgbox(parent, titulo, texto, icono, botones, default)
# Factory para QMessageBox estilizados con botones traducidos al español
# Traducciones automáticas: Yes→Sí, No→No, Open→Abrir, Cancel→Cancelar,
# Save→Guardar, Close→Cerrar, Apply→Aplicar, Reset→Restablecer,
# Retry→Reintentar, Ignore→Ignorar, Discard→Descartar
```

### 6.7 forms.py
- **Clases**:
  - `CustomTooltipWidget(QWidget)` → Tooltip personalizado con estilo
  - `GlobalTooltipEventFilter(QObject)` → Event filter global para tooltips
  - `TooltipDelegate(QStyledItemDelegate)` → Delegate de tooltips para tablas
  - `TooltipEventFilter(QObject)` → Event filter local para tooltips
- **Funciones**:
  - `limpiar_widgets(form)` → Limpia todos los widgets de un formulario
  - `set_campos_editables(campos, estado, campos_solo_lectura)` → Toggle editable/readonly
  - `ajustar_columnas_tabla(parent_widget, tabla, anchos_columnas, stretch_last)` → Configura anchos de columnas

### 6.8 proxies.py
```python
ProxyConEstado(QSortFilterProxyModel)
# Filtra filas según columna de estado (oculta inactivos opcionalmente)
```

### 6.9 widgets.py
```python
Switch(QCheckBox)
# Widget tipo toggle switch (on/off) con colores personalizables
# Usado para activar/desactivar estudiantes y empleados
```

### 6.10 animated_stack.py
```python
AnimatedStack(QStackedWidget)
# QStackedWidget con transiciones de deslizamiento animadas
# Método principal: setCurrentIndexSlide(index, duration=200)
```

### 6.11 tarjeta_seccion.py
```python
TarjetaSeccion(QWidget)
# Widget tarjeta visual para secciones en GestionSeccionesPage
# Muestra: grado, letra, nivel, docente, ocupación, color por nivel
# Señal: clicked(dict) al hacer clic
```

### 6.12 tarjeta_seccion_mini.py
```python
TarjetaSeccionMini(QWidget)
# Widget mini-tarjeta para selección de sección en GestionNotasPage
# Muestra: grado, letra, ocupación
# Tamaño fijo: 100x70px
# Señal: clicked(dict), estado seleccionada con estilo visual
```

### 6.13 sombras.py
```python
crear_sombra_flotante(widget, blur_radius=10, y_offset=2, opacity=80)
# Aplica QGraphicsDropShadowEffect a un widget
```

### 6.14 edad.py
```python
calcular_edad(fecha_nac: date) -> int
# Calcula edad desde fecha de nacimiento
```

### 6.15 archivos.py
```python
abrir_archivo(ruta)              # Abre archivo con app predeterminada (multiplataforma)
abrir_carpeta(ruta)              # Abre carpeta en explorador (multiplataforma)
normalizar_ruta(ruta)            # Normaliza ruta al SO actual
crear_carpeta_si_no_existe(ruta) # mkdir -p equivalente
```

### 6.16 fonts.py
```python
FontManager
# Gestor de fuentes personalizadas (Inter)
# Carga 9 variantes: Thin, ExtraLight, Light, Regular, Medium, SemiBold, Bold, ExtraBold, Black
# Métodos: cargar_fuentes(), aplicar_fuente_global(app, tamaño)
```

### 6.17 reportes_config.py
```python
CriteriosReportes
# Clase con métodos estáticos para obtener datos de reportes
# Reportes de estudiantes:
#   estudiantes_por_genero(), estudiantes_por_rango_edad(min, max),
#   estudiantes_por_seccion(), estudiantes_por_grado(), estudiantes_por_ciudad(),
#   matricula_por_rango_anio(inicio, fin)
# Reportes de egresados:
#   egresados_por_genero(), egresados_por_anio_escolar()
# Reportes de secciones:
#   secciones_por_genero(), obtener_secciones_activas(), genero_por_seccion_especifica(),
#   secciones_por_edad_promedio(), secciones_ocupacion()
# Reportes de empleados:
#   empleados_por_cargo(), empleados_por_nivel_academico()
# Generación de gráficas (matplotlib):
#   grafica_barras(ax, etiquetas, valores, titulo)
#   grafica_torta(ax, etiquetas, valores, titulo)
#   grafica_texto(ax, etiquetas, valores, titulo)
```

---

## 7. Funcionalidades Clave

### 7.1 Promoción Automática de Estudiantes
Al aperturar un nuevo año escolar:
1. Estudiantes de 6to Primaria → Egresados
2. Otros → Promoción al siguiente grado con nueva sección
3. Secciones duplicadas al nuevo año con materias asociadas
4. Registro en `historial_secciones` para trazabilidad

### 7.2 Generación de Cédula Estudiantil
Formato: `{número_hijo}{año_nacimiento}{cedula_madre}`
- Ejemplo: `215V12345678` (segundo hijo, nacido 2015, madre CI V12345678)

### 7.3 Sistema de Calificaciones
- **Notas literales**: A, B, C, D, E (A-C aprobatorias, D-E reprobatorias)
- **3 lapsos** por año escolar
- **Nota final**: Calculada automáticamente promediando los 3 lapsos
- **Registro masivo**: Todas las notas de una sección/materia/lapso en una transacción
- **Coloreo visual**: Verde (A/B), Amarillo (C), Rojo (D/E)
- **Historial de notas PDF**: Exportable por estudiante

### 7.4 Gestión de Materias y Áreas
- **Áreas de aprendizaje**: Agrupan materias (ej: Lenguaje, Matemáticas, Ciencias)
- **Materias**: Asignables por nivel y grado
- **Asignación a secciones**: Al crear sección o posteriormente
- **Duplicación automática**: Al aperturar nuevo año, las materias se copian

### 7.5 Exportaciones
| Tipo | Formato | Contenido |
|------|---------|-----------|
| Constancia de Estudios | PDF | Membrete + datos estudiante + nivel actual |
| Constancia de Inscripción | PDF | Confirmación de matrícula |
| Constancia de Retiro | PDF | Motivo y fecha de retiro |
| Constancia de Buena Conducta | PDF | Certificación de conducta |
| Constancia de Prosecución Inicial | PDF | Para nivel Inicial |
| Certificado de Promoción (6to) | PDF | Promoción de 6to grado |
| Constancia de Trabajo | PDF | Datos del empleado |
| Historial Académico | PDF | Historial completo de secciones |
| Historial de Notas | PDF | Notas por materia y lapso |
| Listado de Sección | PDF | Estudiantes de una sección con membrete |
| Reporte RAC | Excel | Relación de Actividad de Cargo |
| Matrícula Completa | Excel | Todos los estudiantes activos |
| Nómina de Empleados | Excel | Todos los empleados |
| Tabla Filtrada | Excel | Lo que se ve en pantalla |
| Reportes Estadísticos | PDF | Gráficos (barras/torta/texto) con datos |

### 7.6 Sistema de Auditoría
Todo cambio crítico se registra:
- Creación/modificación/eliminación de registros
- Cambios de estado (activar/desactivar)
- Accesos al sistema
- Promociones y retiros
- Cambios en datos institucionales
- Asignación de materias/docentes

### 7.7 Reportes Estadísticos
- **Categorías**: Estudiantes, Egresados, Secciones, Empleados
- **Criterios**: Género, edad, sección, grado, ciudad, año, cargo, nivel académico, ocupación
- **Tipos de gráfica**: Barras, Torta, Texto
- **Exportación**: PDF con gráfico y datos tabulares

### 7.8 Devolución de Estudiante
- Permite reasignar a sección de grado inferior (repitencia)
- Registra en historial con observaciones
- Solo secciones del año escolar actual

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
numpy<2.0                   # Dependencia de matplotlib
pillow==12.0.0              # Manejo de imágenes (logos)
pyinstaller==6.3.0          # Empaquetado ejecutable
jaraco.text                 # Utilidades de texto
```

---

## 9. Estructura de Archivos Completa

```
Proyecto_SIRA/
├── main.py                    # Punto de entrada (verificación BD → Config inicial → Login → MainWindow)
├── paths.py                   # Rutas absolutas para recursos (resource_path)
├── compilar_ui.py             # Script para compilar .ui → .py
├── compilar.sh                # Script bash para compilar UIs
├── limpiar_datos.py           # Limpia datos de prueba de la BD
├── poblar_db_estu.py          # Genera estudiantes ficticios
├── poblar_db_emple.py         # Genera empleados ficticios
├── reset_db.py                # Reinicia base de datos
├── requirements.txt           # Dependencias Python
├── .env                       # Credenciales BD (NO commitear)
├── LICENSE                    # MIT License
├── README.md                  # Documentación del proyecto
├── AGENTS.md                  # Esta documentación para agentes IA
│
├── db/
│   └── schema.sql             # Esquema completo de la BD (15 tablas)
│
├── models/
│   ├── user_model.py          # UsuarioModel - Usuarios y autenticación
│   ├── estu_model.py          # EstudianteModel - Estudiantes (~1300 líneas)
│   ├── emple_model.py         # EmpleadoModel - Empleados
│   ├── repre_model.py         # RepresentanteModel - Representantes
│   ├── secciones_model.py     # SeccionesModel - Secciones académicas
│   ├── anio_model.py          # AnioEscolarModel - Años escolares
│   ├── areas_model.py         # AreaAprendizajeModel - Áreas de aprendizaje
│   ├── materias_model.py      # MateriasModel - Materias curriculares
│   ├── notas_model.py         # NotasModel - Calificaciones (~816 líneas)
│   ├── registro_base.py       # RegistroBase - Operaciones genéricas de estado
│   ├── auditoria_model.py     # AuditoriaModel - Sistema de auditoría
│   ├── institucion_model.py   # InstitucionModel - Datos de la institución
│   └── dashboard_model.py     # DashboardModel - Estadísticas para dashboard
│
├── views/
│   ├── login.py               # LoginDialog - Autenticación
│   ├── config_inicial.py      # Config_inicial - Configuración primer uso
│   ├── main_window.py         # MainWindow - Ventana principal (~1300 líneas)
│   ├── gestion_estudiantes.py # GestionEstudiantesPage - Módulo estudiantes
│   ├── detalles_estudiante.py # DetallesEstudiante - Ficha estudiante
│   ├── registro_estudiante.py # NuevoRegistro - Formulario registro estudiante
│   ├── gestion_empleados.py   # GestionEmpleadosPage - Módulo empleados
│   ├── detalles_empleados.py  # DetallesEmpleado - Ficha empleado
│   ├── registro_empleado.py   # RegistroEmpleado - Formulario registro empleado
│   ├── gestion_secciones.py   # GestionSeccionesPage - Módulo secciones (tarjetas)
│   ├── detalles_seccion.py    # DetallesSeccion + DialogMoverEstudiante
│   ├── crear_seccion.py       # CrearSeccion - Formulario nueva sección
│   ├── gestion_materias.py    # GestionMateriasPage + DialogoMateria + DialogoGestionAreas
│   ├── asignar_materias.py    # AsignarMateriasDialog
│   ├── gestion_notas.py       # GestionNotasPage + NotaDelegate
│   ├── gestion_anio.py        # GestionAniosPage + ConfirmarAnioDialog
│   ├── egresados.py           # Egresados - Módulo egresados
│   ├── datos_institucionales.py # Funciones de datos institucionales (mixin)
│   ├── delegates.py           # Delegates de estado para tablas
│   ├── registro_usuario.py    # RegistroUsuario - Formulario usuario
│   ├── actualizar_usuario.py  # ActualizarUsuario - Edición usuario
│   └── acerca_de.py           # Acerca_de - Diálogo informativo
│
├── ui_compiled/               # Clases Python generadas desde .ui
│   ├── main_ui.py
│   ├── login_ui.py
│   ├── config_inicial_ui.py
│   ├── gestion_estudiantes_ui.py
│   ├── ficha_estu_ui.py
│   ├── registro_estu_ui.py
│   ├── gestion_empleados_ui.py
│   ├── ficha_emple_ui.py
│   ├── registro_emple_ui.py
│   ├── secciones_ui.py
│   ├── detalles_seccion_ui.py
│   ├── crear_seccion_ui.py
│   ├── mover_estudiante_ui.py
│   ├── gestion_materias_ui.py
│   ├── asignar_materias_ui.py
│   ├── gestion_notas_ui.py
│   ├── anio_escolar_ui.py
│   ├── confirmar_anio_ui.py
│   ├── Egresados_ui.py
│   ├── detalle_egresado_ui.py
│   ├── registro_user_ui.py
│   ├── actualizar_user_ui.py
│   └── acerca_de_ui.py
│
├── resources/
│   ├── resources_ui.py        # Recursos compilados (íconos embebidos)
│   ├── ui/                    # Archivos .ui originales (Qt Designer)
│   ├── icons/                 # Iconos e imágenes (SIRA.ico, etc.)
│   └── fonts/                 # Fuentes Inter (9 variantes .ttf)
│
├── utils/
│   ├── db.py                  # Conexión a base de datos
│   ├── conexion.py            # Verificación de conexión
│   ├── security.py            # Hashing bcrypt
│   ├── exportar.py            # PDF y Excel (~2200 líneas)
│   ├── backup.py              # Gestión de backups (mysqldump)
│   ├── dialogs.py             # MessageBox factory con traducciones español
│   ├── forms.py               # Helpers de formularios y tooltips
│   ├── proxies.py             # ProxyConEstado para filtrar tablas
│   ├── widgets.py             # Switch toggle personalizado
│   ├── animated_stack.py      # AnimatedStack - Transiciones animadas
│   ├── tarjeta_seccion.py     # TarjetaSeccion - Widget tarjeta grande
│   ├── tarjeta_seccion_mini.py # TarjetaSeccionMini - Widget tarjeta pequeña
│   ├── sombras.py             # Efectos de sombra
│   ├── edad.py                # Cálculo de edad
│   ├── archivos.py            # Manejo de archivos multiplataforma
│   ├── fonts.py               # FontManager - Gestor de fuentes Inter
│   └── reportes_config.py     # CriteriosReportes - Datos y gráficas para reportes
│
├── backups/                   # Backups automáticos y manuales (.sql)
└── exportados/                # Archivos PDF/Excel generados
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

# Mensajes al usuario (siempre usar crear_msgbox para botones en español)
from utils.dialogs import crear_msgbox
crear_msgbox(self, "Título", "Mensaje", QMessageBox.Information).exec()

# Diálogos de confirmación (botones Sí/No en español automáticamente)
msg = crear_msgbox(
    self, "Confirmar", "¿Está seguro?",
    QMessageBox.Question,
    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
    QMessageBox.StandardButton.No
)
if msg.exec() == QMessageBox.StandardButton.Yes:
    # acción confirmada

# ⚠️ NO usar QMessageBox.question() directamente → usar crear_msgbox

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
7. **Usar `crear_msgbox`** en lugar de `QMessageBox.question()` para mantener botones en español
8. **Usar `AnimatedStack.setCurrentIndexSlide()`** para navegación con animación
9. **Compilar .ui después de cambios** en Qt Designer con `python compilar_ui.py`
10. **NO tocar ui_compiled/** manualmente — se genera desde `resources/ui/`

### 10.5 Pruebas Manuales
No hay suite de tests automatizados. Para probar:
```bash
# Activar entorno virtual
source venv/bin/activate

# Ejecutar aplicación
python main.py

# Compilar archivos .ui después de cambios en Qt Designer
python compilar_ui.py

# Poblar datos de prueba
python poblar_db_estu.py
python poblar_db_emple.py

# Limpiar datos / reiniciar BD
python limpiar_datos.py
python reset_db.py
```

---

## 11. Contexto Adicional

### 11.1 Datos de Prueba
Existen scripts para poblar datos de prueba:
- `poblar_db_estu.py`: Genera estudiantes ficticios con representantes
- `poblar_db_emple.py`: Genera empleados ficticios
- `limpiar_datos.py`: Limpia datos de prueba
- `reset_db.py`: Reinicia la base de datos completamente

### 11.2 Backups
- Automáticos cada 3 días (timer en MainWindow)
- Manuales desde el menú de administración
- Se guardan en `backups/` con formato `backup_TIPO_YYYYMMDD_HHMMSS.sql`
- Se mantienen máximo 30 backups (los más antiguos se eliminan)
- Usa `mysqldump` del sistema

### 11.3 Logo de la Institución
- Se almacena como LONGBLOB en tabla `institucion`
- Se puede cargar/actualizar desde el módulo de datos institucionales
- Se usa en encabezados de constancias y certificados PDF

### 11.4 Fuentes Personalizadas
- Fuente principal: **Inter** (Google Fonts)
- 9 variantes de peso cargadas al inicio
- Aplicada globalmente a toda la aplicación

### 11.5 Sistema de Notas
- Solo aplica para nivel **Primaria** (Inicial no tiene calificaciones formales)
- Notas **literales** A-E (no numéricas)
- 3 lapsos por año escolar
- Nota final calculada como promedio literal
- A, B, C = aprobatoria; D, E = reprobatoria

---

## 12. Preguntas Frecuentes para Agentes

**P: ¿Cómo agrego un nuevo campo a una tabla?**
R: Modifica `db/schema.sql`, documenta el ALTER TABLE necesario, actualiza el modelo correspondiente en `models/`, y los formularios en `views/` si aplica.

**P: ¿Cómo creo una nueva constancia PDF?**
R: Usa las funciones existentes en `utils/exportar.py` como referencia. Sigue el patrón de `generar_constancia_estudios()`. Siempre incluye `encabezado()` y `pie_pagina()`.

**P: ¿Cómo agrego un nuevo módulo/página?**
R: 1) Crea el .ui en Qt Designer, 2) Compila con `python compilar_ui.py`, 3) Crea la vista en `views/`, 4) Agrégala al AnimatedStack en MainWindow, 5) Conecta botón de navegación.

**P: ¿Cómo manejo permisos por rol?**
R: En MainWindow hay `configurar_permisos()` que oculta/deshabilita widgets según `self.usuario_actual['rol']`.

**P: ¿Cómo agrego una nueva materia?**
R: Usa `MateriasModel.crear()` con nombre, tipo de evaluación, área de aprendizaje y grados asociados. La vista `GestionMateriasPage` ya maneja el CRUD completo.

**P: ¿Cómo muestro un diálogo de confirmación?**
R: Usa `crear_msgbox()` de `utils/dialogs.py` (nunca `QMessageBox.question()`). Los botones se traducen automáticamente al español.

**P: ¿Cómo agrego un nuevo reporte estadístico?**
R: 1) Agrega método en `CriteriosReportes` (utils/reportes_config.py), 2) Regístralo en `actualizar_criterios()` de MainWindow, 3) Usa los métodos de gráfica existentes (`grafica_barras`, `grafica_torta`, `grafica_texto`).

**P: ¿Cómo funciona la apertura de año escolar?**
R: `AnioEscolarModel.aperturar_nuevo()` → desactiva año anterior → crea nuevo → duplica secciones con `SeccionesModel` → duplica materias con `MateriasModel.duplicar_materias_seccion()` → promueve estudiantes con `EstudianteModel.promover_masivo()`.

---
