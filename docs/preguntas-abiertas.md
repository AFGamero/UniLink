# Preguntas abiertas — UniLink

_Consolidado para la reunión de decisiones · Última actualización: 2026-10-27_

Este documento es la **única fuente** de las preguntas abiertas de los specs, el SRS, las ADR y las normas de la comunidad: los demás documentos solo citan su código (`P-NN`). Están agrupadas según **quién debe responderlas** y ordenadas por el **sprint que las necesita**. Cada pregunta trae una propuesta para agilizar la discusión.

## Cómo usar este documento

1. En la reunión, se lee la propuesta y se acepta, se ajusta o se descarta. La respuesta se anota en la columna **Decisión**.
2. Después de la reunión, quien tenga asignada la pregunta actualiza el documento de origen (regla, dato o mensaje), quita la referencia `P-NN` de su sección de preguntas y deja aquí la decisión con su fecha.
3. Cuando un spec ya no tiene preguntas que bloqueen el desarrollo, puede pasar a **Aprobado** (ver la [Definition of Ready](./sprints/README.md#definition-of-ready-un-spec-puede-entrar-a-un-sprint)).

**La pregunta vive aquí; la decisión, una vez tomada, vive en el documento de origen.**

**Estados de la columna Decisión** (desde la [reunión del 2026-10-19](./decisiones/2026-10-19-reunion-preguntas-abiertas.md)):

| Estado | Significado |
|---|---|
| **Resuelta** | Hay una decisión y aplica al MVP. |
| **Resuelta – fuera del MVP** | Hay una decisión: no se hace en el MVP. |
| **Pendiente** | Se discutió, pero falta decidir. |
| **Por gestionar** | Depende de una gestión con la Universidad. |

Una celda vacía significa que la pregunta no se trató. Las decisiones del 2026-10-19 **todavía no se han llevado a los specs**: el [análisis integral](./riesgos_y_brechas_unilink.md) lista qué spec debe cambiar por cada una.

## Resumen

| Grupo | Responde | Preguntas | Primera necesaria antes de |
|---|---|---|---|
| [A. Institucionales](#a-institucionales) | Dirección del CIDTI y TI de la universidad | 10 | Sprint 0 |
| [B. Jurídicas](#b-jurídicas) | Oficina jurídica de la universidad | 5 | Sprint 1 |
| [C. Técnicas](#c-técnicas) | Equipo de desarrollo | 8 | Sprint 0 |
| [D. De producto](#d-de-producto) | Equipo de UniLink (Product Owner) | 33 | Sprint 1 |
| [E. Para después del lanzamiento](#e-para-después-del-lanzamiento) | Equipo de UniLink | 5 | No bloquean el MVP |
| [F. Surgidas en la reunión del 2026-10-19](#f-surgidas-en-la-reunión-del-2026-10-19) | Equipo de UniLink y la Universidad | 6 | Sprint 0 |
| **Total** | | **67** | |

**Prioridad para la primera reunión:** P-01 a P-05, P-11, P-16 a P-18, P-19 a P-22 y P-52 a P-55. Sin ellas no pueden empezar el Sprint 0 ni el Sprint 1.

**Estado tras la reunión del 2026-10-19:**

| Estado | Preguntas | IDs |
|---|---|---|
| Resuelta | 25 | P-01, P-02, P-07, P-09, P-17, P-21, P-23, P-25, P-27 a P-31, P-32, P-35, P-36, P-39, P-41, P-43, P-44, P-46 a P-49 (P-30, el 2026-10-24; P-17 y P-53, el 2026-10-27) |
| Resuelta – fuera del MVP | 7 | P-08, P-11, P-20, P-33, P-37, P-40, P-42 |
| Pendiente | 9 | P-16, P-18, P-19, P-56 a P-60, P-63 |
| Por gestionar | 2 | P-12, P-61 |
| No se trató | 24 | P-03 a P-06, P-10, P-13 a P-15, P-22, P-24, P-26, P-34, P-38, P-45, P-50 a P-52, P-54, P-55, P-62, P-64 a P-67 |

## A. Institucionales

| ID | Pregunta | Origen | Antes de | Propuesta | Decisión |
|---|---|---|---|---|---|
| P-01 | ¿Las cifras de los supuestos de uso (5.000 usuarios el primer año, 500 simultáneos) son realistas? | [SRS §3.3](./srs/Especificacion_Requisitos.md#33-requisitos-no-funcionales) | Sprint 0 | Validarlas con las cifras de matrícula y planta de personal de la universidad. | **Resuelta (Reunión 2026-10-19):** Dimensionar para ~1.000 usuarios simultáneos (picos en convocatorias de monitores), con holgura el primer año. |
| P-02 | ¿UniLink se aloja en la infraestructura de la universidad o en un proveedor en la nube? | [SRS §3.3](./srs/Especificacion_Requisitos.md#33-requisitos-no-funcionales) | Sprint 0 | Consultar primero con TI si ofrece servidores y respaldos. Si no, usar la nube con datos alojados en una región que cumpla RNF-PRI-08. | **Resuelta (Reunión 2026-10-19):** Infraestructura propia de la Universidad, con servidor activo 24/7. Base de datos propia y desacoplada de la institucional; solo se comparte la autenticación (token del Campus Virtual). |
| P-03 | ¿Qué dominios de correo institucional son válidos además de `unimagdalena.edu.co`? | [FS-USR-01](./modulos/usuarios/specs/FS-USR-01-registro.md) | Sprint 1 | Pedir a TI la lista completa de dominios y dejarla configurable. | |
| P-04 | ¿De dónde se obtiene el catálogo oficial de programas académicos? | [FS-USR-01](./modulos/usuarios/specs/FS-USR-01-registro.md) | Sprint 1 | Pedir a Admisiones y Registro un listado exportable y cargarlo como datos semilla. | |
| P-05 | ¿Cuál es el correo de soporte oficial de UniLink? | [FS-USR-02](./modulos/usuarios/specs/FS-USR-02-inicio-sesion.md), [Normas](./normas-comunidad.md#preguntas-abiertas) | Sprint 1 | Crear un buzón institucional propio, por ejemplo `unilink@unimagdalena.edu.co`. | |
| P-06 | ¿Se puede usar la imagen de la Universidad o del CIDTI en el pie de la hoja de vida en PDF? | [FS-USR-07](./modulos/usuarios/specs/FS-USR-07-hoja-de-vida-pdf.md) | Sprint 2 | Usar solo el texto "Generado con UniLink" hasta tener la autorización de uso de marca. | |
| P-07 | ¿Quiénes serán los administradores de la plataforma en el lanzamiento? | [FS-PLT-01](./modulos/plataforma/specs/FS-PLT-01-gestion-categorias.md) | Sprint 4 | Dos personas del CIDTI y una de Bienestar Universitario, para que siempre haya otro administrador que revise las sanciones. | **Resuelta (Reunión 2026-10-19):** El Administrador debe ser personal de la Universidad; el equipo de desarrollo no administra la plataforma. No se nombraron personas. |
| P-08 | ¿Qué rutas de atención institucionales se enlazan en las normas N-01 y N-07? | [Normas](./normas-comunidad.md#preguntas-abiertas) | Sprint 5 | Pedir a Bienestar Universitario los enlaces vigentes, incluido el protocolo de violencias basadas en género. | **Resuelta – fuera del MVP (Reunión 2026-10-19):** La ruta institucional de atención queda para después; a lo sumo, un enlace de contacto. |
| P-09 | ¿Se necesita un calendario de espacios de la universidad para validar el lugar de los eventos? | [FS-COL-03](./modulos/colaboracion/specs/FS-COL-03-publicacion-listado-eventos.md) | Sprint 7 | No en el MVP: el organizador es responsable de reservar el espacio. | **Resuelta (Reunión 2026-10-19):** El lugar es un campo informativo; no hay reserva de espacios. |
| P-10 | ¿La universidad ya tiene registrada en la SIC una base de datos de la comunidad, o UniLink requiere un registro nuevo? | [SRS §3.3](./srs/Especificacion_Requisitos.md#33-requisitos-no-funcionales) | Lanzamiento | Consultarlo con la oficina responsable de protección de datos. | |

## B. Jurídicas

| ID | Pregunta | Origen | Antes de | Propuesta | Decisión |
|---|---|---|---|---|---|
| P-11 | ¿La oficina jurídica debe aprobar el texto de autorización de tratamiento de datos del registro? | [FS-USR-01](./modulos/usuarios/specs/FS-USR-01-registro.md) | Sprint 1 | Sí. Enlazar la política de tratamiento de datos vigente de la universidad en lugar de redactar una nueva. | **Resuelta – fuera del MVP (Reunión 2026-10-19):** Los términos y condiciones con la Oficina Jurídica son obligatorios antes de producción, no para el prototipo. |
| P-12 | ¿Es válido el plazo de 30 días antes de borrar definitivamente una cuenta eliminada? | [FS-USR-05](./modulos/usuarios/specs/FS-USR-05-configuracion-cuenta.md) | Sprint 2 | Mantener los 30 días y pedir la validación jurídica. | **Por gestionar (Reunión 2026-10-19):** Se reemplaza el plazo de 30 días por borrado lógico con trazabilidad. Falta validar con la Oficina Jurídica el borrado lógico frente al derecho de supresión de la Ley 1581 de 2012. |
| P-13 | Aprobar las normas de la comunidad (bloquea FS-CNT-02). | [FS-CNT-02](./modulos/contenido/specs/FS-CNT-02-moderacion-contenido.md), [Normas](./normas-comunidad.md) | Sprint 5 | Enviar el borrador v0.1 a jurídica con al menos un sprint de anticipación. | |
| P-14 | ¿El plazo de 15 días para pedir revisión de una sanción es compatible con los procedimientos de la universidad? | [Normas](./normas-comunidad.md#preguntas-abiertas) | Sprint 5 | Mantenerlo y validarlo junto con P-13. | |
| P-15 | ¿Se permite la propaganda de campañas electorales universitarias, o solo el debate político respetuoso? | [Normas](./normas-comunidad.md#preguntas-abiertas) | Sprint 5 | Permitir solo publicaciones informativas de candidaturas estudiantiles oficiales durante el periodo electoral. | |

## C. Técnicas

| ID | Pregunta | Origen | Antes de | Propuesta | Decisión |
|---|---|---|---|---|---|
| P-16 | ¿Las notificaciones se actualizan consultando al servidor cada cierto tiempo o con conexión en tiempo real? | [FS-COM-02](./modulos/comunicacion/specs/FS-COM-02-centro-notificaciones.md) | Sprint 0 | Tiempo real (WebSockets) desde el inicio, porque la mensajería del Sprint 5 lo necesitará. Se decide al elegir el stack. | **Pendiente (Reunión 2026-10-19):** Sin decidir: tiempo real (WebSocket/SSE) o consulta al iniciar sesión / periódica. |
| P-17 | ¿Se necesita un motor de búsqueda dedicado o basta con la base de datos? | [FS-RED-03](./modulos/red/specs/FS-RED-03-busqueda-perfiles.md) | Sprint 0 | La búsqueda de texto completo de la base de datos alcanza para el volumen del MVP. | **Resuelta (2026-10-27):** búsqueda tolerante en PostgreSQL con texto completo, `unaccent` y `pg_trgm`, sin motor dedicado ([ADR-008](./arquitectura/Registro_Decisiones.md#adr-008-búsqueda-de-texto)). |
| P-18 | ¿La disponibilidad del 99,5 % y el horario de soporte son compatibles con el tamaño del equipo? | [SRS §3.3](./srs/Especificacion_Requisitos.md#33-requisitos-no-funcionales) | Sprint 0 | Depende de P-02. Con servicios gestionados en la nube es alcanzable; con infraestructura propia, revisarlo con TI. | **Pendiente (Reunión 2026-10-19):** Horario de soporte y SLA de 99,5 % sin cerrar. El alojamiento ya está decidido (P-02). |
| P-52 | ¿Cuánto tiempo se conservan los registros técnicos (logs)? | [SRS §3.3.12](./srs/Especificacion_Requisitos.md#3312-retención-de-datos) | Sprint 0 | A. 90 días; B. 30 días; C. 1 año. **Propuesta: A**, suficiente para investigar incidentes sin acumular datos personales (RNF-PRI-07). | |
| P-53 | ¿Qué lenguajes y frameworks domina el equipo? Bloquea el stack. | [ADR-010](./arquitectura/Registro_Decisiones.md#adr-010-lenguaje-y-framework) | Sprint 0 | A. Java con Spring Boot; B. TypeScript con NestJS; C. Python con Django o FastAPI. **Propuesta:** elegir el que más integrantes dominen; a igualdad, A por su soporte para monolitos modulares. | **Resuelta (2026-10-27):** FastAPI en el backend y React en el frontend; cada módulo con arquitectura hexagonal y Clean Architecture ([ADR-010](./arquitectura/Registro_Decisiones.md#adr-010-lenguaje-y-framework), [ADR-017](./arquitectura/Registro_Decisiones.md#adr-017-arquitectura-interna-de-los-módulos-hexagonal-con-clean-architecture)). |
| P-62 | ¿Los límites por IP de inicio de sesión y registro son adecuados? En la universidad muchos usuarios comparten la misma IP pública. | [Seguridad de la API](./arquitectura/seguridad-endpoints.md#8-límites-de-peticiones) | Sprint 0 | Medir el tráfico real desde las salas de cómputo antes de fijarlos; mientras tanto, límites altos por IP y estrictos por cuenta. | |
| P-63 | ¿El inicio de sesión usa la cuenta institucional (SSO) en lugar de una contraseña propia? | [Seguridad de la API](./arquitectura/seguridad-endpoints.md#4-sesión-e-inicio-de-sesión), [ADR-013](./arquitectura/Registro_Decisiones.md#adr-013-autenticación-institucional-y-cuentas-precreadas) | Sprint 0 | Definir el mecanismo con TI a partir de la decisión del 2026-10-19. | **Pendiente (Reunión 2026-10-19):** se decidió compartir solo la autenticación mediante el token del Campus Virtual; falta definir el mecanismo técnico y qué pasa con la contraseña propia. |
| P-64 | ¿Se agrega una segunda verificación (código por correo o aplicación) para los administradores de la plataforma? | [Seguridad de la API](./arquitectura/seguridad-endpoints.md) | Sprint 4 | Sí para Administrador y Moderador, por su acceso a datos de toda la comunidad. | |

## D. De producto

### Sprint 1 — Cuenta

| ID | Pregunta | Origen | Propuesta | Decisión |
|---|---|---|---|---|
| P-19 | ¿El equipo aprueba la lista de categorías semilla? | [FS-USR-04](./modulos/usuarios/specs/FS-USR-04-preferencias-contenido.md) | Revisarla en la reunión y aprobarla. | **Pendiente (Reunión 2026-10-19):** Categorías semilla por revisar. |
| P-20 | ¿Las oportunidades y los servicios también deben tener preferencias de contenido? | [FS-USR-04](./modulos/usuarios/specs/FS-USR-04-preferencias-contenido.md) | No en el MVP: las oportunidades ya usan la afinidad por etiquetas, y los servicios son de la fase 2. | **Resuelta – fuera del MVP (Reunión 2026-10-19):** Los servicios y sus preferencias de contenido pasan a la Fase 2 (la Fase 1 es institucional). Las oportunidades dependen de la revisión del alcance del módulo (P-59). |
| P-21 | ¿Se avisa por correo al usuario cuando su cuenta se bloquea por intentos fallidos? | [FS-USR-02](./modulos/usuarios/specs/FS-USR-02-inicio-sesion.md) | Sí: ayuda a detectar accesos no autorizados. | **Resuelta (Reunión 2026-10-19):** Bloqueo temporal y recuperación de contraseña; sin correo por cada bloqueo (se puede avisar de un inicio de sesión nuevo). |
| P-22 | ¿Se impide reutilizar contraseñas anteriores además de la actual? | [FS-USR-03](./modulos/usuarios/specs/FS-USR-03-recuperar-contrasena.md) | No en el MVP: basta con impedir la actual. | |
| P-54 | El registro dice "Ya existe una cuenta con este correo" (MSG-02). ¿Se debe ocultar que un correo tiene cuenta? | [FS-USR-01](./modulos/usuarios/specs/FS-USR-01-registro.md) | A. Mantenerlo (el correo es institucional y los intentos están limitados); B. Mensaje genérico "Te enviamos un correo" y el correo explica que ya tiene cuenta; C. Mantenerlo y limitar los registros por origen. **Propuesta: B**, coherente con la recuperación de contraseña. | |
| P-55 | Fallar 5 veces con el correo de otra persona la bloquea 15 minutos. ¿Se limita también por origen? | [FS-USR-02](./modulos/usuarios/specs/FS-USR-02-inicio-sesion.md) | A. Además del bloqueo por cuenta, limitar intentos por dirección de origen; B. Sustituir el bloqueo por una espera creciente entre intentos; C. Aceptar el riesgo: se desbloquea restableciendo la contraseña. **Propuesta: A.** | |

### Sprint 2 — Perfil

| ID | Pregunta | Origen | Propuesta | Decisión |
|---|---|---|---|---|
| P-23 | ¿Qué pasa con las publicaciones, proyectos y oportunidades de una cuenta eliminada? | [FS-USR-05](./modulos/usuarios/specs/FS-USR-05-configuracion-cuenta.md) | Se borran las publicaciones. Los proyectos y oportunidades con otros participantes quedan a nombre de "Usuario eliminado". | **Resuelta (Reunión 2026-10-19):** Borrado lógico: la cuenta y todo lo asociado se ocultan, con trazabilidad (quién y cuándo). La validación jurídica sigue en P-12. |
| P-24 | ¿"Puedo aportar" y "Necesito" comparten catálogo de etiquetas con las habilidades? | [FS-USR-06](./modulos/usuarios/specs/FS-USR-06-perfil-profesional.md) | Un solo catálogo: así el cruce encuentra coincidencias entre quien aporta y quien necesita. | |
| P-25 | ¿Un administrador puede fusionar o eliminar etiquetas duplicadas o inapropiadas? | [FS-USR-06](./modulos/usuarios/specs/FS-USR-06-perfil-profesional.md) | Sí, como ajuste a FS-PLT-01 en el Sprint 4. | **Resuelta (Reunión 2026-10-19):** No aplica: las etiquetas son predefinidas. |
| P-65 | ¿Quién mantiene el catálogo de etiquetas predefinidas y sus sinónimos, y cómo se carga el catálogo inicial? | [FS-USR-06](./modulos/usuarios/specs/FS-USR-06-perfil-profesional.md) | El Administrador, desde el panel de Plataforma (FS-PLT-01), con un catálogo inicial que prepare el equipo con el CIDTI. | |
| P-66 | Con las cuentas precreadas, ¿el nombre y la unidad académica del perfil siguen siendo editables? | [FS-USR-06](./modulos/usuarios/specs/FS-USR-06-perfil-profesional.md) | Solo lectura: los fija la sincronización institucional y las correcciones se piden por soporte. | |
| P-67 | ¿El estado de monitor académico es visible aunque el perfil sea "Solo mis conexiones"? | [FS-RED-03](./modulos/red/specs/FS-RED-03-busqueda-perfiles.md) | Sí: es un dato institucional de una convocatoria pública y es la razón de la sección Personas. Mientras no se decida, el spec lo trata como privado. | |

### Sprint 3 — Red

| ID | Pregunta | Origen | Propuesta | Decisión |
|---|---|---|---|---|
| P-26 | ¿Es aceptable que el solicitante deduzca el rechazo por la espera de 30 días? | [FS-RED-01](./modulos/red/specs/FS-RED-01-solicitudes-conexion.md) | Aceptarlo: es lo habitual en otras redes y evita que una solicitud quede pendiente para siempre a ojos del solicitante. | |
| P-27 | ¿Se necesita bloquear usuarios en el MVP? | [FS-RED-01](./modulos/red/specs/FS-RED-01-solicitudes-conexion.md) | Sí, en una versión mínima: el bloqueado no puede ver el perfil, enviar solicitudes ni mensajes. Se decide junto con P-32. | **Resuelta (Reunión 2026-10-19):** Sí se puede bloquear y reportar usuarios; el Administrador verifica y decide. |
| P-28 | ¿El CIDTI crea perfiles de mentores para que los primeros usuarios tengan sugerencias? | [FS-RED-02](./modulos/red/specs/FS-RED-02-onboarding-sugerencias.md) | Sí: entre 20 y 30 perfiles reales de profesores y egresados antes del lanzamiento. | **Resuelta (Reunión 2026-10-19):** No habrá perfiles semilla; el feed muestra perfiles afines. |

### Sprint 4 — Contenido

| ID | Pregunta | Origen | Propuesta | Decisión |
|---|---|---|---|---|
| P-29 | ¿Quién define y mantiene la lista de palabras prohibidas? | [FS-CNT-01](./modulos/contenido/specs/FS-CNT-01-publicaciones-feed.md) | Los administradores, desde el panel de FS-PLT-01. | **Resuelta (Reunión 2026-10-19):** La mantiene el Administrador, no el equipo. |
| P-30 | ¿La categoría de publicaciones "Oportunidades" se renombra o se elimina cuando exista el módulo de oportunidades? | [FS-CNT-01](./modulos/contenido/specs/FS-CNT-01-publicaciones-feed.md) | Renombrarla a "Convocatorias externas" desde el Sprint 4. |**Resuelta (2026-10-24):** se renombra a "Convocatorias externas" desde el Sprint 4 (I-14). |
| P-31 | ¿Una sola reacción ("Me gusta") o varias? | [FS-CNT-01](./modulos/contenido/specs/FS-CNT-01-publicaciones-feed.md) | Una sola en el MVP. | **Resuelta (Reunión 2026-10-19):** Una sola reacción ("Me gusta"). |

### Sprint 5 — Mensajería y moderación

| ID | Pregunta | Origen | Propuesta | Decisión |
|---|---|---|---|---|
| P-32 | ¿Se puede reportar a un usuario por acoso en mensajes? | [FS-COM-01](./modulos/comunicacion/specs/FS-COM-01-mensajeria-privada.md) | Sí: el reporte adjunta solo los mensajes que el denunciante elija, y así se respeta que los administradores no lean conversaciones. | **Resuelta (Reunión 2026-10-19):** Sí se puede reportar usuarios; el Administrador verifica y decide. |
| P-33 | ¿Se quiere un proceso de apelación dentro de la plataforma? | [FS-USR-08](./modulos/usuarios/specs/FS-USR-08-gestion-cuentas.md) | No en el MVP: revisión por correo de soporte, como proponen las normas. | **Resuelta – fuera del MVP (Reunión 2026-10-19):** Las apelaciones se gestionan por soporte, no dentro de la plataforma. |
| P-34 | ¿Suspensiones automáticas o todas decididas por un administrador? | [FS-USR-08](./modulos/usuarios/specs/FS-USR-08-gestion-cuentas.md) | Todas por un administrador. El sistema solo avisa cuando un usuario acumula 3 contenidos retirados en un mes. | |
| P-35 | ¿El umbral de 5 reportes para ocultar automáticamente es adecuado? | [FS-CNT-02](./modulos/contenido/specs/FS-CNT-02-moderacion-contenido.md) | Mantener 5 y dejarlo configurable para ajustarlo con datos reales. | **Resuelta (Reunión 2026-10-19):** Con 5 reportes el contenido se bloquea, no solo se oculta. |
| P-51 | ¿Qué pasa con lo que posee una cuenta suspendida, inhabilitada o eliminada (oportunidades con postulantes, eventos con asistentes, proyectos con creador protegido, postulaciones y asistencias)? | [Usuarios](./modulos/usuarios/README.md#máquina-de-estados-de-la-cuenta) | A. Tabla única de efectos en el README de Usuarios, que cada módulo aplica al recibir `cuenta.estado_cambiado`; B. Resolverlo spec por spec; C. Regla general: todo queda oculto y congelado mientras la cuenta no esté activa y pasa a "Usuario eliminado" al eliminarse. **Propuesta: A** con la regla C como punto de partida. | |

### Sprint 6 — Oportunidades

| ID | Pregunta | Origen | Propuesta | Decisión |
|---|---|---|---|---|
| P-36 | ¿Cualquier usuario puede publicar oportunidades, o solo profesores, administrativos y grupos de investigación? | [FS-COL-01](./modulos/colaboracion/specs/FS-COL-01-publicacion-oportunidades.md) | Cualquier usuario. Las de estudiantes se marcan como "Iniciativa estudiantil" y pasan por la moderación normal. | **Resuelta (Reunión 2026-10-19):** Cualquier usuario, con moderación. |
| P-37 | ¿Se sugieren oportunidades a usuarios con alta afinidad? | [FS-COL-01](./modulos/colaboracion/specs/FS-COL-01-publicacion-oportunidades.md) | Sí, con una notificación como máximo al día para no saturar. | **Resuelta – fuera del MVP (Reunión 2026-10-19):** Las sugerencias por afinidad como notificación quedan para después. |
| P-38 | ¿Se limita el número de postulaciones activas por usuario? | [FS-COL-02](./modulos/colaboracion/specs/FS-COL-02-postulaciones.md) | No al inicio: revisar con datos reales. | |

### Sprint 7 — Eventos

| ID | Pregunta | Origen | Propuesta | Decisión |
|---|---|---|---|---|
| P-39 | ¿Los eventos próximos también se muestran en el feed? | [FS-COL-03](./modulos/colaboracion/specs/FS-COL-03-publicacion-listado-eventos.md) | No: basta con la sección Eventos. | **Resuelta (Reunión 2026-10-19):** Sí se muestran en el feed. |
| P-40 | ¿Se necesita lista de espera para eventos con cupo? | [FS-COL-04](./modulos/colaboracion/specs/FS-COL-04-confirmacion-asistencia.md) | No en el MVP. | **Resuelta – fuera del MVP (Reunión 2026-10-19):** No habrá lista de espera. |
| P-41 | ¿El organizador puede escribir un mensaje a todos los asistentes? | [FS-COL-04](./modulos/colaboracion/specs/FS-COL-04-confirmacion-asistencia.md) | Sí, como un aviso que llega por notificación y no como un chat grupal. | **Resuelta (Reunión 2026-10-19):** Sí puede enviar un mensaje a los asistentes. |

### Sprint 8 — Proyectos

| ID | Pregunta | Origen | Propuesta | Decisión |
|---|---|---|---|---|
| P-42 | ¿Se necesita un espacio de conversación del equipo dentro del proyecto? | [FS-COL-05](./modulos/colaboracion/specs/FS-COL-05-espacios-proyectos.md) | No en el MVP: los miembros se coordinan por mensajes privados. | **Resuelta – fuera del MVP (Reunión 2026-10-19):** El chat de equipo queda para después, igual que el registro interno de grupos (actas, grabaciones, avances). |
| P-43 | ¿Los proyectos de clase pueden ser privados? | [FS-COL-05](./modulos/colaboracion/specs/FS-COL-05-espacios-proyectos.md) | Sí: un proyecto privado solo lo ven sus miembros. | **Resuelta (Reunión 2026-10-19):** Sí hay proyectos privados. Las categorías son generales, no "de clase". |
| P-44 | ¿El rol por defecto de los nuevos miembros es configurable por proyecto? | [FS-COL-06](./modulos/colaboracion/specs/FS-COL-06-roles-proyectos.md) | No en el MVP. | **Resuelta (Reunión 2026-10-19):** Configurable: el creador del proyecto define los roles. |
| P-50 | Quien pasó el onboarding antes del Sprint 8 nunca verá proyectos sugeridos. ¿Cómo se le sugieren? | [FS-RED-02](./modulos/red/specs/FS-RED-02-onboarding-sugerencias.md), [FS-COL-05](./modulos/colaboracion/specs/FS-COL-05-espacios-proyectos.md) | A. Sugerir proyectos también en "Personas que podrían interesarte"; B. Sugerirlos solo en la sección Proyectos (orden por afinidad); C. Mostrar una vez un "mini onboarding" de proyectos a los usuarios existentes. **Propuesta: A.** | |

## E. Para después del lanzamiento

Ninguna de estas preguntas bloquea el MVP. Se revisan con datos reales o cuando se retome la fase 2.

| ID | Pregunta | Origen | Propuesta | Decisión |
|---|---|---|---|---|
| P-45 | ¿Son razonables los pesos del puntaje de sugerencias (3, 2, 1, 1)? | [FS-RED-02](./modulos/red/specs/FS-RED-02-onboarding-sugerencias.md) | Revisarlos tres meses después del lanzamiento. | |
| P-46 | ¿El cruce debe reconocer etiquetas parecidas y no solo idénticas? | [FS-USR-06](./modulos/usuarios/specs/FS-USR-06-perfil-profesional.md) | Explorarlo con el equipo de Aluna I.A. | **Resuelta (Reunión 2026-10-19):** Sí: el cruce debe reconocer etiquetas similares, no solo idénticas. La relevancia se prioriza por vistas. |
| P-47 | ¿Se permite adjuntar archivos en los mensajes? | [FS-COM-01](./modulos/comunicacion/specs/FS-COM-01-mensajeria-privada.md) | Evaluarlo en una versión posterior. | **Resuelta (Reunión 2026-10-19):** Sí, condicionado a la mensajería (P-56). |
| P-48 | ¿Las credenciales verificadas aparecen en la hoja de vida en PDF? | [FS-USR-07](./modulos/usuarios/specs/FS-USR-07-hoja-de-vida-pdf.md) | Sí, cuando exista FS-SRV-01 (fase 2). | **Resuelta (Reunión 2026-10-19):** Solo las credenciales verificadas por la plataforma. |
| P-49 | ¿Se necesita un rol de "moderador" con menos permisos que el administrador? | [FS-PLT-01](./modulos/plataforma/specs/FS-PLT-01-gestion-categorias.md) | Evaluarlo si el volumen de reportes supera la capacidad de los administradores. | **Resuelta (Reunión 2026-10-19):** Dos roles: Administrador (control total, personal de la Universidad) y Moderador (reportes, bloqueos, contenido y lenguaje). |

## F. Surgidas en la reunión del 2026-10-19

Temas que quedaron abiertos en la reunión y no tenían pregunta. La confirmación del stack, que también quedó pendiente, era P-53 y se resolvió el 2026-10-27.

| ID | Pregunta | Origen | Propuesta | Decisión |
|---|---|---|---|---|
| P-56 | ¿La mensajería privada empieza como chat o como contacto directo? | [FS-COM-01](./modulos/comunicacion/specs/FS-COM-01-mensajeria-privada.md) | Empezar con contacto directo y evaluar el chat después. | **Pendiente (Reunión 2026-10-19):** en revisión; la prioridad sigue en Alta. |
| P-57 | ¿Qué diferencia un evento de una reunión? | [FS-COL-03](./modulos/colaboracion/specs/FS-COL-03-publicacion-listado-eventos.md) | | **Pendiente (Reunión 2026-10-19):** falta una definición formal. |
| P-58 | ¿Vencen las solicitudes de unión a un proyecto? | [FS-COL-05](./modulos/colaboracion/specs/FS-COL-05-espacios-proyectos.md) | Vencer a los 30 días. | **Pendiente (Reunión 2026-10-19):** propuesta de 30 días, sin aprobar. |
| P-59 | ¿Cuál es el alcance del módulo de oportunidades? | [Colaboración](./modulos/colaboracion/README.md) | | **Pendiente (Reunión 2026-10-19):** por revisar. |
| P-60 | ¿Qué dominio tendrá UniLink? | [Sprint 0](./sprints/sprint-00/README.md) | | **Pendiente (Reunión 2026-10-19).** |
| P-61 | ¿Cómo se obtiene acceso a la API de admisiones (endpoint GET)? | [FS-USR-01](./modulos/usuarios/specs/FS-USR-01-registro.md) | | **Por gestionar (Reunión 2026-10-19):** gestionarlo con la Universidad. En el MVP la API se simula con correos ficticios. |

## Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-08 | Gamero | Creación: 49 preguntas consolidadas de 22 specs, los requisitos no funcionales y las normas. |
| 2026-10-24 | Equipo UniLink | Única fuente de las preguntas; P-50 a P-55 agregadas con tres alternativas cada una; P-30 resuelta; orígenes actualizados a la nueva estructura. |
| 2026-10-27 | Gamero | Decisiones de la [reunión del 2026-10-19](./decisiones/2026-10-19-reunion-preguntas-abiertas.md) llevadas a esta estructura; grupo F (P-56 a P-61); P-62 a P-64 trasladadas desde la seguridad de la API. |
| 2026-10-27 | Gamero | P-53 resuelta: FastAPI y React con arquitectura hexagonal y Clean Architecture. |
| 2026-10-27 | Gamero | P-17 resuelta: búsqueda en PostgreSQL (ADR-008). |
| 2026-10-27 | Gamero | Corrección: P-26 vuelve a "no se trató" (la decisión "las solicitudes no vencen" corresponde a FS-RED-01 RN-08, no a P-26). P-65 a P-67 nuevas, surgidas al actualizar FS-USR-06 y FS-RED-03. |
