# Reestructuración de la documentación de UniLink

| Campo | Valor |
|---|---|
| **Estado** | Propuesta — pendiente de revisión del equipo |
| **Rama** | `feature/reestructuracion-docs` (desde `documentacion`) |
| **Fecha** | 2026-10-24 |
| **Afecta** | Todo `docs/` y la nueva carpeta `contracts/` |

## 1. Contexto

La documentación actual tiene tres capas bien pensadas (requisitos → specs → sprints), pero al revisarla completa aparecen dos tipos de problema.

**De método:**

1. El mismo comportamiento se escribe tres veces (flujo del caso de uso, criterios de la historia y Gherkin del spec) y ya hay diferencias entre ellos.
2. No hay requisitos funcionales globales: `RF-01` existe en los 22 specs, mientras los RNF sí tienen ID global.
3. Hay 11 carpetas para 22 specs, y administración mezcla tres dominios (categorías, cuentas y moderación).
4. El sprint de cada spec está en tres sitios y las preguntas abiertas en dos.

**De contenido:**

5. **No está claro quién es quién.** Los actores se nombran distinto en cada documento, no hay una matriz de permisos y nadie es responsable de ningún spec ("Por asignar" en los 22).
6. **Los specs describen el camino feliz, pero no estudian las variaciones ni qué pasaría en las situaciones límite.** Ejemplos: el personal administrativo no puede guardar su perfil; nadie sabe qué pasa con los eventos de un organizador suspendido; dos personas pueden tomar el último cupo a la vez.
7. **El estado de la cuenta está repartido en cuatro specs**, y los mecanismos que comparten los módulos (notificaciones, reportes, auditoría, afinidad, categorías, permiso para conversar) no tienen un contrato.
8. **No hay documentación de arquitectura:** ni comparación de alternativas, ni decisiones registradas, ni vistas. RNF-MAN-05 pide generar la API desde el código, lo contrario de acordarla antes.

## 2. Decisiones

| # | Decisión | Alternativas descartadas |
|---|---|---|
| D-1 | **Monolito modular** (se justifica en la comparación de alternativas, sección 6.1). | Monolito en capas; microservicios. |
| D-2 | **Tres niveles de documentos**: un SRS general, una carpeta de arquitectura y una carpeta por módulo con el estudio detallado de cada funcionalidad. | Todo dentro de los módulos; un solo SRS con todo. |
| D-3 | **Seis módulos por dominio** más servicios (fase 2) como módulo propio sin specs. | Tres módulos por actor; mantener los diez actuales. |
| D-3.1 | **Usuarios + Red**: la persona (cuenta, sesión, configuración, preferencias, perfil, hoja de vida y gestión de cuentas) es un módulo, y sus relaciones y el descubrimiento (conexiones, onboarding, sugerencias y búsqueda) son otro. Así los datos de la persona (nombre, unidad académica, tipo, privacidad) tienen un solo dueño y la dependencia va en un solo sentido: Red → Usuarios. Dentro de Usuarios, credenciales y sesiones son un componente interno que nunca se expone. | Identidad y perfil-y-red separados (tenían un ciclo de dependencias y el perfil partido en dos dueños); un solo módulo con identidad, perfil y red (11 specs, del que dependen todos). |
| D-4 | **Renumerar los specs ahora**, con tabla de equivalencias: todo está en Borrador y no hay código. | Conservar los códigos; código nuevo con alias. |
| D-5 | **El spec pasa a ser un estudio**: quién es quién, variaciones, "¿qué pasaría si…?", resultado esperado y lista de revisión (sección 5). | Mantener la plantilla actual. |
| D-6 | **Contratos de un monolito modular**: API REST para el frontend, interfaz pública de cada módulo y eventos de dominio en memoria (sección 7). | Solo API REST. |
| D-7 | **Contract-first**: lo acordado vive en `contracts/` y la integración continua lo compara con lo que genera el código. RNF-MAN-05 se reescribe. | Code-first. |
| D-8 | **Diagramas en Mermaid** dentro de los Markdown. | PlantUML con SVG generado; ambos. |
| D-9 | **Plan de implementación como esqueleto**: lo que depende del stack queda marcado hasta cerrar su ADR. | Plan completo con un stack propuesto; dejarlo para después. |
| D-10 | **Equipo "Por asignar"** en la tabla de responsabilidades; se completa en la reunión de decisiones. | Solo roles sin nombres. |

## 3. Documentos y orden de lectura

```
docs/
├── README.md                          ← índice y orden de lectura
├── srs/
│   └── Especificacion_Requisitos.md   ← SRS (ISO/IEC/IEEE 29148:2018)
├── arquitectura/
│   ├── Comparacion_Alternativas.md
│   ├── Registro_Decisiones.md         ← ADR
│   ├── Vistas_Arquitectura.md         ← vista de módulos, de componentes y conectores (C&C) y de despliegue
│   └── Plan_de_Implementacion.md      ← esqueleto (D-9)
├── modulos/
│   ├── README.md                      ← mapa de módulos y tabla de equivalencias
│   ├── _plantilla-spec.md
│   └── <modulo>/
│       ├── README.md                  ← quién es quién del módulo, entidades, estados, datos propios, interfaz
│       ├── casos-de-uso.md
│       ├── historias.md
│       └── specs/FS-<MOD>-NN-<nombre>.md
├── sprints/                           ← roadmap: única fuente del sprint de cada spec
├── decisiones/                        ← decisiones sobre la documentación (este archivo)
├── preguntas-abiertas.md              ← única fuente de preguntas abiertas
└── normas-comunidad.md
contracts/                             ← sección 7
```

**Orden de lectura:**

1. SRS, secciones 1 y 2: qué problema resuelve UniLink, para quién y con qué restricciones.
2. Comparación de alternativas: por qué un monolito modular.
3. Registro de decisiones: cómo se materializa (persistencia, tiempo real, búsqueda, stack, alojamiento).
4. Vistas de arquitectura: qué módulos hay, cómo se comunican y dónde se ejecutan.
5. `modulos/`: el estudio de cada funcionalidad.
6. `contracts/`: lo que cada módulo expone y consume.
7. Plan de implementación y sprints: cómo y cuándo se construye.

`requisitos/CasosDeUso.md`, `requisitos/HistoriasDeUsuario.md` y `specs/` desaparecen: su contenido se reparte en `modulos/`. `RequisitosNoFuncionales.md` se integra en el SRS.

## 4. SRS y "quién es quién"

| Sección del SRS | Contenido |
|---|---|
| 1. Introducción | Propósito, alcance (MVP, fase 2 y lo que queda fuera con su justificación), glosario, referencias (Ley 1581, ISO/IEC 25010, WCAG 2.1). |
| 2.1 Perspectiva | Problema que resuelve y contexto institucional (CIDTI, Universidad del Magdalena). |
| 2.2 Funciones | Resumen de los seis módulos. |
| **2.3 Stakeholders** | Quién tiene interés o decide: CIDTI, oficina de TI, oficina jurídica, Bienestar Universitario, Admisiones y Registro, comunidad (estudiantes, profesores, personal administrativo), administradores de la plataforma y equipo de desarrollo. Para cada uno: qué espera y qué decide (enlazado a las preguntas abiertas). |
| **2.4 Actores del sistema** | Un nombre único por actor y su definición: Visitante, Usuario (Estudiante, Profesor, Personal administrativo), Autor, Responsable de oportunidad, Postulante, Organizador, Asistente, Creador y miembro de proyecto (Visualizador, Editor, Administrador de proyecto), Administrador de la plataforma, Sistema (tareas programadas). En fase 2: Egresado, Tercerizado, Oferente. |
| **2.5 Matriz de permisos** | Actor × acción para todos los módulos: quién puede, quién ve, quién no. Cada spec detalla la suya y esta es el resumen. |
| 2.6 Restricciones y supuestos | Supuestos de uso (5.000 usuarios, 500 simultáneos), ley de datos, presupuesto, tamaño del equipo, solo web. |
| 3.1 Requisitos funcionales | Índice por módulo con su ID (`USR-01/RF-03`) y enlace al spec. |
| 3.2 Casos de uso | Índice de CU-01…30 por módulo y actor, con diagrama. |
| 3.3 Requisitos no funcionales | El contenido actual de `RequisitosNoFuncionales.md`, más los nuevos de la sección 8.3. |
| **3.4 Escenarios de calidad** | Cada atributo importante como escenario verificable: fuente, estímulo, entorno, artefacto, respuesta y medida (sección 6.4). |
| 4. Verificación | Cómo se verifica cada tipo de requisito. |
| Apéndice A | Matriz de trazabilidad: CU → HU → spec → RNF → escenario de calidad → contrato. |
| Apéndice B | Matriz de riesgos (probabilidad, impacto, mitigación, responsable). |
| **Apéndice C** | Equipo y responsabilidades por módulo: responsable, quién revisa, quién aprueba, a quién se consulta. Nombres "Por asignar" (D-10). |

## 5. El estudio de cada funcionalidad

### 5.1 README de cada módulo

| Sección | Contenido |
|---|---|
| Propósito | Qué resuelve el módulo y qué **no** es su responsabilidad. |
| Quién es quién | Actores del módulo y su matriz de permisos. |
| Entidades y datos propios | Qué datos son del módulo (ningún otro los escribe). |
| Estados | Diagrama Mermaid de cada entidad con ciclo de vida. El de usuarios tiene la **máquina de estados única de la cuenta**. |
| Expone | Rutas de la API, operaciones de su interfaz pública y eventos que publica. |
| Consume | Lo que usa de otros módulos y para qué. |
| Riesgos y decisiones abiertas | Preguntas `P-xx` del módulo. |

**Colaboración** agrupa oportunidades, eventos y proyectos porque comparten un patrón: una publicación con responsable, cupo, participantes, estados y afinidad. Su README describe ese patrón una vez, y cada spec lo concreta.

### 5.2 Plantilla del spec

| # | Sección | Qué responde |
|---|---|---|
| 1 | Objetivo | Problema, para quién y qué valor entrega. |
| 2 | **Quién es quién** | Cada actor: qué hace, qué ve, qué no puede hacer. |
| 3 | Alcance | Incluye / no incluye (con dónde se resuelve lo excluido). |
| 4 | Reglas de negocio | `RN-NN`. |
| 5 | Requisitos funcionales | `RF-NN` y prioridad. |
| 6 | Datos y validaciones | Campos, tipo, obligatoriedad, validación y **finalidad** (RNF-PRI-01). |
| 7 | Estados | Diagrama Mermaid y tabla de transiciones con quién la provoca. |
| 8 | Flujo principal | Lo que se espera que pase normalmente, paso a paso. |
| 9 | **Variaciones** | Caminos alternativos legítimos: otro tipo de usuario, otra modalidad, otro estado de partida. |
| 10 | **¿Qué pasaría si…?** | Tabla: situación · comportamiento esperado · regla que lo decide. Revisa siempre: concurrencia; cambio de estado de la cuenta de cada actor; eliminación o retiro de lo que esto usa; pérdida de permiso a mitad del uso; falla del correo, del almacenamiento o del tiempo real; límites de uso; privacidad. |
| 11 | Mensajes | `MSG-NN`. |
| 12 | **Resultado esperado** | Escenarios Gherkin que cubren el flujo, cada variación y cada fila de la sección 10. |
| 13 | Contratos | Qué expone y consume (API, interfaz pública, eventos). |
| 14 | Calidad | RNF y escenarios de calidad que aplican. |
| 15 | Preguntas abiertas | Solo referencias `P-xx`. |
| 16 | Lista de revisión | Casillas de la sección 5.3. |
| 17 | Historial de cambios | |

Se quitan "Sprint" (vive en el roadmap) y "Dependencias" (las reemplaza la sección 13).

### 5.3 Lista de revisión de un spec (antes de pasar a Aprobado)

- [ ] Cada actor de la sección 2 existe en el SRS §2.4 con el mismo nombre.
- [ ] Toda acción tiene un actor que puede hacerla y se valida en el servidor.
- [ ] Cada regla tiene al menos un escenario en la sección 12.
- [ ] La sección 10 revisó las siete situaciones de la lista.
- [ ] Ningún dato se recoge sin finalidad.
- [ ] No contradice a su CU, a su HU ni a otro spec.
- [ ] Sus contratos existen en `contracts/`.
- [ ] No tiene preguntas abiertas que bloqueen.

### 5.4 Método

| Regla | Detalle |
|---|---|
| M-1 Un papel por documento | **CU:** flujo actor–sistema y excepciones. **HU:** "Como / quiero / para", prioridad y enlace a los escenarios del spec; sus criterios no se repiten. **Spec:** única fuente de reglas, datos, mensajes y criterios. |
| M-2 Numeración | CU y HU conservan su número global (CU-01…30, HU-01…31); dentro del spec se citan como `USR-01/RN-03`. |
| M-3 Una sola fuente | El sprint, solo en el roadmap; las preguntas, solo en `preguntas-abiertas.md`; los RNF, solo en el SRS. |

### 5.5 Módulos y equivalencias

| Módulo | Código | Carpeta | Specs (antes → ahora) | CU | HU |
|---|---|---|---|---|---|
| Usuarios | USR | `usuarios/` | CTA-01 → USR-01 Registro · CTA-02 → USR-02 Inicio de sesión · CTA-03 → USR-03 Recuperar contraseña · CTA-04 → USR-04 Preferencias · CTA-05 → USR-05 Configuración · PRF-01 → USR-06 Perfil · PRF-03 → USR-07 Hoja de vida · ADM-02 → USR-08 Gestión de cuentas | 01, 02, 03, 04, 17, 18, 19, 24 | 01, 02, 03, 04, 13, 14, 17, 28 |
| Red | RED | `red/` | RED-01 → RED-01 Conexiones · RED-02 → RED-02 Onboarding y sugerencias · PRF-02 → RED-03 Búsqueda | 05, 06, 07, 13 | 05, 06, 07, 24 |
| Contenido | CNT | `contenido/` | CNT-01 → CNT-01 Publicaciones y feed · ADM-03 → CNT-02 Moderación | 08, 09, 25 | 08, 09, 18, 19 |
| Comunicación | COM | `comunicacion/` | MSG-01 → COM-01 Mensajería · NOT-01 → COM-02 Notificaciones | 10, 23 | 10, 30 |
| Colaboración | COL | `colaboracion/` | OPO-01 → COL-01 Publicar oportunidades · OPO-02 → COL-02 Postulaciones · EVT-01 → COL-03 Eventos · EVT-02 → COL-04 Asistencia · PRY-01 → COL-05 Proyectos · PRY-02 → COL-06 Roles en proyectos | 11, 12, 14, 15, 16, 20, 21, 22 | 11, 12, 15, 16, 25, 26, 27, 29 |
| Plataforma | PLT | `plataforma/` | ADM-01 → PLT-01 Categorías (con el panel de administración y el registro de auditoría) | 26 | 20 |
| Servicios _(fase 2)_ | SRV | `servicios/` | FS-SRV-01 a 03 (pendientes, sin archivo) | 27, 28, 29, 30 | 21, 22, 23, 31 |

## 6. Arquitectura

### 6.1 Comparación de alternativas

Tres alternativas: **monolito en capas**, **monolito modular** y **microservicios**. Se comparan con una tabla ponderada según las restricciones de UniLink: equipo pequeño de estudiantes, 5.000 usuarios el primer año (25.000 sin rediseño), 99,5 % de disponibilidad, presupuesto universitario, operación posiblemente en la infraestructura de la universidad (P-02) y un plan de 8 sprints.

Criterios: complejidad operativa, costo, velocidad de entrega, mantenibilidad y aislamiento entre funcionalidades, rendimiento, disponibilidad, facilidad de pruebas y capacidad de evolucionar (por ejemplo, separar la mensajería si crece). Cierra con la decisión justificada y el análisis de trade-offs: qué se gana, qué se sacrifica y qué restricciones pesaron más.

### 6.2 Registro de decisiones (ADR)

Formato de cada una: estado, contexto, alternativas, decisión y consecuencias. Las que el equipo todavía no ha tomado quedan como **Propuesta**, con sus opciones y la pregunta abierta que las bloquea.

| ADR | Tema | Estado inicial |
|---|---|---|
| ADR-001 | Metodología: Scrum de 2 semanas guiado por specs | Aceptada (ya está en `sprints/`) |
| ADR-002 | Estilo arquitectónico: monolito modular | Aceptada |
| ADR-003 | Límites de los seis módulos y dependencias permitidas | Aceptada |
| ADR-004 | Comunicación entre módulos: interfaz pública síncrona y eventos de dominio en memoria, publicados después de confirmar la transacción | Aceptada |
| ADR-005 | Persistencia: una base de datos relacional con un esquema por módulo; un módulo no consulta las tablas de otro | Propuesta |
| ADR-006 | Contract-first (D-7) | Aceptada |
| ADR-007 | Notificaciones y mensajes en tiempo real (P-16) | Propuesta |
| ADR-008 | Búsqueda de texto completo en la base de datos o motor dedicado (P-17) | Propuesta |
| ADR-009 | Alojamiento: universidad o nube (P-02, RNF-PRI-08) | Propuesta |
| ADR-010 | Lenguaje y framework del backend y del frontend | Propuesta |
| ADR-011 | Tareas en segundo plano y programadas (correos, cierres automáticos, recordatorios, limpiezas; RNF-REN-05) | Propuesta |
| ADR-012 | Almacenamiento de archivos (fotos, adjuntos, portadas; RNF-SEG-06) | Propuesta |

### 6.3 Vistas

| Vista | Qué muestra |
|---|---|
| **Módulos** | Descomposición en los seis módulos, qué datos posee cada uno y la relación de **uso** permitida (por ejemplo, comunicación usa a red para saber si dos usuarios están conectados; red usa a usuarios, pero usuarios nunca usa a red; ningún módulo usa a comunicación directamente, solo le envía eventos). Se verifica que no haya ciclos. |
| **Componentes y conectores (C&C)** | El sistema en ejecución. **Componentes:** aplicación web en el navegador, aplicación monolítica (con sus seis módulos), ejecutor de tareas en segundo plano, base de datos, almacenamiento de archivos, servicio de correo, canal de tiempo real y herramienta de monitoreo. **Conectores:** HTTPS/REST, WebSocket (o el que decida ADR-007), llamada en proceso por la interfaz pública, bus de eventos en memoria, SQL, SMTP y envío de errores al monitoreo. Para cada conector: quién inicia, síncrono o asíncrono y qué pasa si falla (RNF-DIS-05). |
| **Despliegue** | Qué componente corre en cada entorno (desarrollo, pruebas, producción; RNF-DES-01). Las partes que dependen de ADR-009 quedan marcadas. |

### 6.4 Escenarios de calidad (base)

| ID | Atributo | Estímulo → respuesta esperada |
|---|---|---|
| EC-01 | Rendimiento | 500 usuarios abren el feed en hora pico → responde en menos de 1 s (p95). |
| EC-02 | Disponibilidad | El servicio de correo deja de responder → el registro y las notificaciones internas siguen funcionando y los correos se reintentan. |
| EC-03 | Seguridad | Un usuario sin permiso llama directamente a la API para cambiar un rol de proyecto → se rechaza y queda registrado. |
| EC-04 | Consistencia | Dos usuarios confirman a la vez el último cupo de un evento → solo uno lo obtiene; el otro ve "Cupo completo". |
| EC-05 | Privacidad | Un administrador intenta leer una conversación privada → la aplicación no ofrece ninguna forma de hacerlo. |
| EC-06 | Modificabilidad | Se agrega un nuevo tipo de contenido reportable → la moderación no cambia; el nuevo tipo solo implementa el contrato `Reportable`. |
| EC-07 | Modificabilidad | Se decide separar la mensajería en un servicio aparte → solo cambia la implementación de su interfaz pública; los demás módulos no cambian. |

Cada escenario enlaza los RNF que concreta y los specs donde se prueba.

### 6.5 Plan de implementación (esqueleto)

Estructura interna común de un módulo (capa de API, aplicación, dominio e infraestructura, con su interfaz pública como única puerta), reglas de dependencia y cómo se verifican en la integración continua, flujos clave independientes del lenguaje (inicio de sesión y sesión, moderación de contenido, toma de cupo, notificación desde un evento) y estrategia de pruebas. Lo que depende del stack queda marcado con su ADR pendiente.

## 7. Contratos

```
contracts/
├── README.md       ← reglas
├── api/
│   ├── README.md   ← convenciones de la API REST
│   └── usuarios.yaml · red.yaml · contenido.yaml · comunicacion.yaml · colaboracion.yaml · plataforma.yaml
├── modulos/
│   └── <modulo>.md ← interfaz pública: operaciones que otros módulos pueden usar
└── eventos/
    ├── README.md   ← catálogo: evento · productor · consumidores · efecto (incluida la notificación y el correo que dispara)
    ├── sobre.v1.json
    └── <dominio>.<hecho>.v1.json
```

**Reglas:**

1. Un módulo solo usa a otro por su **interfaz pública** o reaccionando a sus **eventos**; nunca lee ni escribe sus tablas.
2. El contrato se cambia antes que el código, en un PR revisado por el módulo que lo expone y por los que lo usan.
3. Un cambio incompatible crea una versión nueva; agregar un campo opcional no.
4. Un evento se publica solo después de confirmar la transacción que lo origina. Si un consumidor falla, no deshace la operación del productor: se registra y se reintenta. Los consumidores descartan eventos repetidos por su identificador.
5. Los archivos son válidos para las herramientas: OpenAPI 3.0.3 y JSON Schema 2020-12.
6. Cada módulo se prueba contra su contrato.

**API REST** (convenciones que salen de los RNF):

| Tema | Convención | Origen |
|---|---|---|
| Rutas | `/api/v1/<modulo>/...` | ADR-003 |
| Sesión | Cookie `HttpOnly`, `Secure`, `SameSite`, invalidable en el servidor; token CSRF en escrituras | RNF-SEG-03, RNF-SEG-05 |
| Errores | `{ "error": "<CODIGO>", "message": "<texto>", "correlation_id": "<id>" }`; `message` usa los `MSG-NN` del spec | RNF-USA-03, RNF-OBS-01 |
| Límites de uso | 429 con `Retry-After` | RNF-SEG-07 |
| Ediciones | `ETag` / `If-Match`, 409 ante conflicto | R-1 |
| Creaciones reintentables | `Idempotency-Key` | R-1 |
| Paginación | Por cursor en feed, mensajes y notificaciones; por página en búsquedas y administración | COM-01, COM-02, RED-03, USR-08 |
| Fechas | ISO 8601 con zona; se muestran en hora de Colombia | RNF-USA-01 |

En esta rama cada OpenAPI lleva sus rutas con resumen, CU y spec de origen, y los componentes comunes; los esquemas detallados se completan cuando su spec pasa a Aprobado.

**Interfaz pública de cada módulo** (primeras operaciones, salen de los specs):

| Módulo | Operación | La usa |
|---|---|---|
| Usuarios | Estado de una cuenta; si un usuario es administrador; datos públicos y nivel de privacidad de un perfil; etiquetas de un perfil; afinidad de un usuario con una lista de habilidades; categorías de interés; marcar el onboarding como completado | todos; plataforma; red; colaboración; contenido |
| Red | Si dos usuarios están conectados; qué parte de un perfil ve un observador (cruza la privacidad de usuarios con las conexiones); perfiles complementarios; número de conexiones | comunicación, contenido, colaboración, pantallas de administración |
| Contenido | Reportar un elemento; contrato `Reportable` que implementa cada módulo con contenido moderable | colaboración, usuarios |
| Comunicación | Si dos usuarios pueden conversar (consulta a red y a colaboración) | — |
| Colaboración | Si dos usuarios tienen una postulación aceptada entre ellos | comunicación |
| Plataforma | Categorías activas de un tipo; registrar una acción en la auditoría | contenido, colaboración, usuarios |

Dos reglas mantienen la dependencia Red → Usuarios en un solo sentido: el indicador de "onboarding pendiente" vive en la cuenta (usuarios) y red lo marca por la interfaz de usuarios, así el inicio de sesión no consulta a red; y el número de conexiones del detalle de una cuenta lo pide la pantalla de administración a red, no usuarios.

**Eventos de dominio** (base, salen de los specs; las notificaciones son un consumidor más):

| Evento | Productor | Consumidores |
|---|---|---|
| `cuenta.estado_cambiado` | usuarios | todos (ver P-51) |
| `perfil.actualizado` | usuarios | red (recalcula sugerencias y complementariedad) |
| `conexion.solicitada`, `conexion.aceptada`, `conexion.eliminada` | red | comunicación |
| `publicacion.comentada` | contenido | comunicación |
| `contenido.reportado`, `contenido.retirado`, `reporte.revisado` | contenido | comunicación, usuarios (historial), el módulo dueño del contenido |
| `mensaje.enviado` | comunicación | comunicación (notificación y correo diferido) |
| `postulacion.creada`, `postulacion.estado_cambiado`, `postulacion.retirada`, `oportunidad.cancelada` | colaboración | comunicación |
| `evento.actualizado`, `evento.cancelado`, `evento.retirado` | colaboración | comunicación |
| `proyecto.solicitud_creada`, `proyecto.solicitud_respondida`, `proyecto.invitacion_creada`, `proyecto.tarea_asignada`, `proyecto.rol_cambiado`, `proyecto.miembro_retirado` | colaboración | comunicación |
| `categoria.cambiada` | plataforma | contenido, colaboración, usuarios |

## 8. Resolución de inconsistencias

### 8.1 Correcciones de redacción (no cambian el alcance)

| ID | Corrección |
|---|---|
| I-01 | El onboarding aparece tras guardar el perfil por primera vez; se corrigen CU-02 (4a) y CU-13. |
| I-03 | Las categorías de USR-04 se llaman "categorías de interés" en todos los documentos; RED-02 RN-03 usa esas categorías. |
| I-04 | CU-02 y HU-02: los intentos restantes se indican cuando quedan 2 o menos. |
| I-05 | CU-03 y HU-03: nombre y foto se editan en el perfil (CU-04). |
| I-09 | HU-10 incluye la postulación aceptada; COL-01 y COL-02 agregan "Enviar mensaje"; se corrige el escenario "Sin conexión no hay chat" de COM-01. |
| I-10 | HU-14 incluye eventos. |
| I-12 | HU-17 permite reactivar cuentas suspendidas e inhabilitadas. Estados renombrados: "Inhabilitada por administración" y "En eliminación". |
| I-13 | El criterio de solicitud de categorías de HU-20 se marca como fase 2. |
| I-14 | La categoría de publicaciones "Oportunidades" pasa a "Convocatorias externas"; se corrigen CU-08 y HU-08 (resuelve P-30). |
| I-16 | CU-22 4b: cerrar no notifica ni decide las postulaciones pendientes (cerrar ≠ cancelar). |
| I-19 | El catálogo de notificaciones pasa al catálogo de eventos con los tipos faltantes (`evento.retirado`, `oportunidad.cancelada`, conexión automática); la preferencia "Recordatorio de eventos…" pasa a "Eventos a los que asistiré". |
| I-20 | USR-01 y USR-02 dicen a dónde redirigen mientras no existan el perfil (Sprint 2) y el onboarding (Sprint 3). |
| I-21 | El tiempo real se decide en el Sprint 0 (ADR-007) en todos los documentos. |
| I-22 | Marcas de fase 2 en HU-02 y HU-04; "Retirada" en CU-14; redirección de CU-02; nota de alcance en P-43. |

### 8.2 Cambios de alcance aprobados

| ID | Cambio | Specs |
|---|---|---|
| I-06 | **Unidad académica** según el tipo de usuario: programa para estudiantes (la facultad se deduce del programa), facultad y departamento para profesores, dependencia para personal administrativo. Es el campo obligatorio del perfil y el que usan la búsqueda y el puntaje del onboarding. | USR-01, USR-06, USR-07, RED-02, RED-03 |
| I-07 | **Tipo de usuario verificado** con la lista o el subdominio que entregue TI; mientras no exista, el perfil muestra "Tipo declarado por el usuario". Se amplía P-03. | USR-01, USR-06 |
| I-08 | **Correo de respaldo** verificado (personal), usado solo para recuperar la contraseña y para avisos de seguridad. | USR-03, USR-05 |
| I-11 | **Las categorías de interés** de proyectos y eventos priorizan "Próximos" (COL-03) y "Explorar" (COL-05). | USR-04, COL-03, COL-05 |
| I-15 | **Moderación transversal**: contrato `Reportable` en CNT-02 para eventos, oportunidades, proyectos y perfiles; el filtro de palabras prohibidas se aplica a todo texto público. Los mensajes privados siguen dependiendo de P-32. | CNT-01, CNT-02, COL-01, COL-03, COL-05, USR-06 |
| I-18 | **Concurrencia en cupos**: nunca se supera un cupo; aceptar en lote más postulantes que cupos rechaza toda la operación. Escenario de concurrencia en cada spec con cupo (EC-04). | COL-01, COL-04, COL-05 |

### 8.3 Requisitos no funcionales nuevos o reescritos

| ID | Cambio |
|---|---|
| R-1 | Sección **Consistencia**: operaciones con cupo atómicas, control de edición concurrente (`If-Match`) e idempotencia en creaciones reintentables. |
| R-2 | RNF-MAN-07: la API y los módulos cumplen `contracts/`, y la integración continua verifica que ningún módulo use a otro fuera de su interfaz pública. |
| R-3 | RNF-MAN-05 reescrito como contract-first (D-7). |
| R-4 | Tabla única de **retención de datos** (auditoría, notificaciones, cuentas sin verificar, cuentas eliminadas, copias). |
| R-5 | **Entregabilidad de correo**: SPF, DKIM y DMARC, y manejo de rebotes. |
| R-6 | Columna "RNF y escenarios de calidad" en la matriz de trazabilidad. |

### 8.4 Preguntas nuevas

**P-50 · Proyectos sugeridos a quien ya pasó el onboarding (I-02).** CU-13 y HU-24 prometen sugerir proyectos, pero eso llega en el Sprint 8 y el onboarding sale una sola vez.
- A. Marcarlo en CU-13 y HU-24 y sugerir proyectos también en "Personas que podrían interesarte".
- B. Quitar los proyectos del onboarding y sugerirlos solo en la sección Proyectos.
- C. Mostrar una vez un "mini onboarding" de proyectos a los usuarios existentes en el Sprint 8.

**P-51 · Qué pasa con lo que posee una cuenta inhabilitada o eliminada (I-17).** Solo está resuelto para los mensajes; faltan oportunidades con postulantes, eventos con asistentes, proyectos con creador protegido, postulaciones y asistencias. El evento `cuenta.estado_cambiado` existe igual; la pregunta es qué hace cada módulo al recibirlo.
- A. Tabla única de efectos en el README de usuarios, aplicada por cada módulo al consumir el evento.
- B. Resolverlo spec por spec.
- C. Regla general: todo queda oculto y congelado mientras la cuenta no esté activa, y pasa a "Usuario eliminado" al eliminarse.

## 9. Plan de trabajo

| Paso | Contenido | Commit sugerido |
|---|---|---|
| 1 | Reorganizar: mover con `git mv`, renumerar, repartir CU y HU por módulo y actualizar enlaces (sin cambiar contenido). | `docs: reorganizar la documentación en 6 módulos` |
| 2 | SRS con quién es quién: stakeholders, actores, matriz de permisos, RNF integrados (8.3), escenarios de calidad y apéndices. | `docs(srs): especificación de requisitos con actores, permisos y escenarios de calidad` |
| 3 | Arquitectura: comparación de alternativas, ADR, vistas (módulos, C&C, despliegue) y esqueleto del plan de implementación. | `docs(arquitectura): comparación de alternativas, ADR y vistas del monolito modular` |
| 4a–4f | **Estudio por módulo**, en el orden de los sprints: usuarios, red, comunicación, contenido, plataforma y colaboración. Cada uno: README, plantilla nueva en sus specs (variaciones, "¿qué pasaría si…?", resultado esperado), sus correcciones de 8.1 y 8.2 y sus preguntas. Se revisa un módulo antes de pasar al siguiente. | `docs(<modulo>): estudio de variaciones, permisos y casos límite` |
| 5 | Contratos (sección 7). | `docs(contracts): API, interfaces públicas y eventos de dominio de los módulos` |
| 6 | Verificación final y matriz de trazabilidad completa. | `docs: matriz de trazabilidad y verificación de enlaces` |

Los commits los hace el equipo; al terminar cada paso se sugiere el mensaje.

## 10. Verificación

- Todo enlace relativo y ancla de `docs/` y `contracts/` existe, y ningún código antiguo (`FS-CTA-…`, `FS-PRF-…`, `FS-ADM-…`, `FS-NOT-…`, `FS-MSG-…`, `FS-OPO-…`, `FS-EVT-…`, `FS-PRY-…`) aparece fuera de la tabla de equivalencias y de `docs/decisiones/`.
- Cada CU-01…30 y HU-01…31 aparece exactamente una vez en `modulos/` y en la matriz de trazabilidad.
- Cada actor que aparece en un spec existe en el SRS §2.4.
- Los JSON Schema se validan contra 2020-12 y los OpenAPI contra 3.0.3.
- Los diagramas Mermaid se renderizan sin errores.
