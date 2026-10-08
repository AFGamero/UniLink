# Preguntas abiertas — UniLink

_Consolidado para la reunión de decisiones · Última actualización: 2026-10-08_

Este documento reúne las preguntas abiertas de los specs, los requisitos no funcionales y las normas de la comunidad, agrupadas según **quién debe responderlas** y ordenadas por el **sprint que las necesita**. Cada pregunta trae una propuesta para agilizar la discusión.

## Cómo usar este documento

1. En la reunión, se lee la propuesta y se acepta, se ajusta o se descarta. La respuesta se anota en la columna **Decisión**.
2. Después de la reunión, quien tenga asignada la pregunta actualiza el documento de origen (regla, dato o mensaje) y marca allí la casilla como resuelta.
3. Cuando un spec ya no tiene preguntas que bloqueen el desarrollo, puede pasar a **Aprobado** (ver la [Definition of Ready](./sprints/README.md#definition-of-ready-un-spec-puede-entrar-a-un-sprint)).

**El documento de origen es la fuente de verdad.** Este consolidado solo sirve para organizar la reunión.

## Resumen

| Grupo | Responde | Preguntas | Primera necesaria antes de |
|---|---|---|---|
| [A. Institucionales](#a-institucionales) | Dirección del CIDTI y TI de la universidad | 10 | Sprint 0 |
| [B. Jurídicas](#b-jurídicas) | Oficina jurídica de la universidad | 5 | Sprint 1 |
| [C. Técnicas](#c-técnicas) | Equipo de desarrollo | 3 | Sprint 0 |
| [D. De producto](#d-de-producto) | Equipo de UniLink (Product Owner) | 26 | Sprint 1 |
| [E. Para después del lanzamiento](#e-para-después-del-lanzamiento) | Equipo de UniLink | 5 | No bloquean el MVP |
| **Total** | | **49** | |

**Prioridad para la primera reunión:** P-01 a P-05, P-11, P-16 a P-18 y P-19 a P-22. Sin ellas no pueden empezar el Sprint 0 ni el Sprint 1.

## A. Institucionales

| ID | Pregunta | Origen | Antes de | Propuesta | Decisión |
|---|---|---|---|---|---|
| P-01 | ¿Las cifras de los supuestos de uso (5.000 usuarios el primer año, 500 simultáneos) son realistas? | [RNF](./requisitos/RequisitosNoFuncionales.md#preguntas-abiertas) | Sprint 0 | Validarlas con las cifras de matrícula y planta de personal de la universidad. | |
| P-02 | ¿UniLink se aloja en la infraestructura de la universidad o en un proveedor en la nube? | [RNF](./requisitos/RequisitosNoFuncionales.md#preguntas-abiertas) | Sprint 0 | Consultar primero con TI si ofrece servidores y respaldos. Si no, usar la nube con datos alojados en una región que cumpla RNF-PRI-08. | |
| P-03 | ¿Qué dominios de correo institucional son válidos además de `unimagdalena.edu.co`? | [FS-CTA-01](./specs/cuenta/FS-CTA-01-registro.md) | Sprint 1 | Pedir a TI la lista completa de dominios y dejarla configurable. | |
| P-04 | ¿De dónde se obtiene el catálogo oficial de programas académicos? | [FS-CTA-01](./specs/cuenta/FS-CTA-01-registro.md) | Sprint 1 | Pedir a Admisiones y Registro un listado exportable y cargarlo como datos semilla. | |
| P-05 | ¿Cuál es el correo de soporte oficial de UniLink? | [FS-CTA-02](./specs/cuenta/FS-CTA-02-inicio-sesion.md), [Normas](./normas-comunidad.md#preguntas-abiertas) | Sprint 1 | Crear un buzón institucional propio, por ejemplo `unilink@unimagdalena.edu.co`. | |
| P-06 | ¿Se puede usar la imagen de la Universidad o del CIDTI en el pie de la hoja de vida en PDF? | [FS-PRF-03](./specs/perfil/FS-PRF-03-hoja-de-vida-pdf.md) | Sprint 2 | Usar solo el texto "Generado con UniLink" hasta tener la autorización de uso de marca. | |
| P-07 | ¿Quiénes serán los administradores de la plataforma en el lanzamiento? | [FS-ADM-01](./specs/administracion/FS-ADM-01-gestion-categorias.md) | Sprint 4 | Dos personas del CIDTI y una de Bienestar Universitario, para que siempre haya otro administrador que revise las sanciones. | |
| P-08 | ¿Qué rutas de atención institucionales se enlazan en las normas N-01 y N-07? | [Normas](./normas-comunidad.md#preguntas-abiertas) | Sprint 5 | Pedir a Bienestar Universitario los enlaces vigentes, incluido el protocolo de violencias basadas en género. | |
| P-09 | ¿Se necesita un calendario de espacios de la universidad para validar el lugar de los eventos? | [FS-EVT-01](./specs/eventos/FS-EVT-01-publicacion-listado-eventos.md) | Sprint 7 | No en el MVP: el organizador es responsable de reservar el espacio. | |
| P-10 | ¿La universidad ya tiene registrada en la SIC una base de datos de la comunidad, o UniLink requiere un registro nuevo? | [RNF](./requisitos/RequisitosNoFuncionales.md#preguntas-abiertas) | Lanzamiento | Consultarlo con la oficina responsable de protección de datos. | |

## B. Jurídicas

| ID | Pregunta | Origen | Antes de | Propuesta | Decisión |
|---|---|---|---|---|---|
| P-11 | ¿La oficina jurídica debe aprobar el texto de autorización de tratamiento de datos del registro? | [FS-CTA-01](./specs/cuenta/FS-CTA-01-registro.md) | Sprint 1 | Sí. Enlazar la política de tratamiento de datos vigente de la universidad en lugar de redactar una nueva. | |
| P-12 | ¿Es válido el plazo de 30 días antes de borrar definitivamente una cuenta eliminada? | [FS-CTA-05](./specs/cuenta/FS-CTA-05-configuracion-cuenta.md) | Sprint 2 | Mantener los 30 días y pedir la validación jurídica. | |
| P-13 | Aprobar las normas de la comunidad (bloquea FS-ADM-03). | [FS-ADM-03](./specs/administracion/FS-ADM-03-moderacion-contenido.md), [Normas](./normas-comunidad.md) | Sprint 5 | Enviar el borrador v0.1 a jurídica con al menos un sprint de anticipación. | |
| P-14 | ¿El plazo de 15 días para pedir revisión de una sanción es compatible con los procedimientos de la universidad? | [Normas](./normas-comunidad.md#preguntas-abiertas) | Sprint 5 | Mantenerlo y validarlo junto con P-13. | |
| P-15 | ¿Se permite la propaganda de campañas electorales universitarias, o solo el debate político respetuoso? | [Normas](./normas-comunidad.md#preguntas-abiertas) | Sprint 5 | Permitir solo publicaciones informativas de candidaturas estudiantiles oficiales durante el periodo electoral. | |

## C. Técnicas

| ID | Pregunta | Origen | Antes de | Propuesta | Decisión |
|---|---|---|---|---|---|
| P-16 | ¿Las notificaciones se actualizan consultando al servidor cada cierto tiempo o con conexión en tiempo real? | [FS-NOT-01](./specs/notificaciones/FS-NOT-01-centro-notificaciones.md) | Sprint 0 | Tiempo real (WebSockets) desde el inicio, porque la mensajería del Sprint 5 lo necesitará. Se decide al elegir el stack. | |
| P-17 | ¿Se necesita un motor de búsqueda dedicado o basta con la base de datos? | [FS-PRF-02](./specs/perfil/FS-PRF-02-busqueda-perfiles.md) | Sprint 0 | La búsqueda de texto completo de la base de datos alcanza para el volumen del MVP. | |
| P-18 | ¿La disponibilidad del 99,5 % y el horario de soporte son compatibles con el tamaño del equipo? | [RNF](./requisitos/RequisitosNoFuncionales.md#preguntas-abiertas) | Sprint 0 | Depende de P-02. Con servicios gestionados en la nube es alcanzable; con infraestructura propia, revisarlo con TI. | |

## D. De producto

### Sprint 1 — Cuenta

| ID | Pregunta | Origen | Propuesta | Decisión |
|---|---|---|---|---|
| P-19 | ¿El equipo aprueba la lista de categorías semilla? | [FS-CTA-04](./specs/cuenta/FS-CTA-04-preferencias-contenido.md) | Revisarla en la reunión y aprobarla. | |
| P-20 | ¿Las oportunidades y los servicios también deben tener preferencias de contenido? | [FS-CTA-04](./specs/cuenta/FS-CTA-04-preferencias-contenido.md) | No en el MVP: las oportunidades ya usan la afinidad por etiquetas, y los servicios son de la fase 2. | |
| P-21 | ¿Se avisa por correo al usuario cuando su cuenta se bloquea por intentos fallidos? | [FS-CTA-02](./specs/cuenta/FS-CTA-02-inicio-sesion.md) | Sí: ayuda a detectar accesos no autorizados. | |
| P-22 | ¿Se impide reutilizar contraseñas anteriores además de la actual? | [FS-CTA-03](./specs/cuenta/FS-CTA-03-recuperar-contrasena.md) | No en el MVP: basta con impedir la actual. | |

### Sprint 2 — Perfil

| ID | Pregunta | Origen | Propuesta | Decisión |
|---|---|---|---|---|
| P-23 | ¿Qué pasa con las publicaciones, proyectos y oportunidades de una cuenta eliminada? | [FS-CTA-05](./specs/cuenta/FS-CTA-05-configuracion-cuenta.md) | Se borran las publicaciones. Los proyectos y oportunidades con otros participantes quedan a nombre de "Usuario eliminado". | |
| P-24 | ¿"Puedo aportar" y "Necesito" comparten catálogo de etiquetas con las habilidades? | [FS-PRF-01](./specs/perfil/FS-PRF-01-perfil-profesional.md) | Un solo catálogo: así el cruce encuentra coincidencias entre quien aporta y quien necesita. | |
| P-25 | ¿Un administrador puede fusionar o eliminar etiquetas duplicadas o inapropiadas? | [FS-PRF-01](./specs/perfil/FS-PRF-01-perfil-profesional.md) | Sí, como ajuste a FS-ADM-01 en el Sprint 4. | |

### Sprint 3 — Red

| ID | Pregunta | Origen | Propuesta | Decisión |
|---|---|---|---|---|
| P-26 | ¿Es aceptable que el solicitante deduzca el rechazo por la espera de 30 días? | [FS-RED-01](./specs/red/FS-RED-01-solicitudes-conexion.md) | Aceptarlo: es lo habitual en otras redes y evita que una solicitud quede pendiente para siempre a ojos del solicitante. | |
| P-27 | ¿Se necesita bloquear usuarios en el MVP? | [FS-RED-01](./specs/red/FS-RED-01-solicitudes-conexion.md) | Sí, en una versión mínima: el bloqueado no puede ver el perfil, enviar solicitudes ni mensajes. Se decide junto con P-32. | |
| P-28 | ¿El CIDTI crea perfiles de mentores para que los primeros usuarios tengan sugerencias? | [FS-RED-02](./specs/red/FS-RED-02-onboarding-sugerencias.md) | Sí: entre 20 y 30 perfiles reales de profesores y egresados antes del lanzamiento. | |

### Sprint 4 — Contenido

| ID | Pregunta | Origen | Propuesta | Decisión |
|---|---|---|---|---|
| P-29 | ¿Quién define y mantiene la lista de palabras prohibidas? | [FS-CNT-01](./specs/contenido/FS-CNT-01-publicaciones-feed.md) | Los administradores, desde el panel de FS-ADM-01. | |
| P-30 | ¿La categoría de publicaciones "Oportunidades" se renombra o se elimina cuando exista el módulo de oportunidades? | [FS-CNT-01](./specs/contenido/FS-CNT-01-publicaciones-feed.md) | Renombrarla a "Convocatorias externas" desde el Sprint 4. | |
| P-31 | ¿Una sola reacción ("Me gusta") o varias? | [FS-CNT-01](./specs/contenido/FS-CNT-01-publicaciones-feed.md) | Una sola en el MVP. | |

### Sprint 5 — Mensajería y moderación

| ID | Pregunta | Origen | Propuesta | Decisión |
|---|---|---|---|---|
| P-32 | ¿Se puede reportar a un usuario por acoso en mensajes? | [FS-MSG-01](./specs/mensajeria/FS-MSG-01-mensajeria-privada.md) | Sí: el reporte adjunta solo los mensajes que el denunciante elija, y así se respeta que los administradores no lean conversaciones. | |
| P-33 | ¿Se quiere un proceso de apelación dentro de la plataforma? | [FS-ADM-02](./specs/administracion/FS-ADM-02-gestion-cuentas.md) | No en el MVP: revisión por correo de soporte, como proponen las normas. | |
| P-34 | ¿Suspensiones automáticas o todas decididas por un administrador? | [FS-ADM-02](./specs/administracion/FS-ADM-02-gestion-cuentas.md) | Todas por un administrador. El sistema solo avisa cuando un usuario acumula 3 contenidos retirados en un mes. | |
| P-35 | ¿El umbral de 5 reportes para ocultar automáticamente es adecuado? | [FS-ADM-03](./specs/administracion/FS-ADM-03-moderacion-contenido.md) | Mantener 5 y dejarlo configurable para ajustarlo con datos reales. | |

### Sprint 6 — Oportunidades

| ID | Pregunta | Origen | Propuesta | Decisión |
|---|---|---|---|---|
| P-36 | ¿Cualquier usuario puede publicar oportunidades, o solo profesores, administrativos y grupos de investigación? | [FS-OPO-01](./specs/oportunidades/FS-OPO-01-publicacion-oportunidades.md) | Cualquier usuario. Las de estudiantes se marcan como "Iniciativa estudiantil" y pasan por la moderación normal. | |
| P-37 | ¿Se sugieren oportunidades a usuarios con alta afinidad? | [FS-OPO-01](./specs/oportunidades/FS-OPO-01-publicacion-oportunidades.md) | Sí, con una notificación como máximo al día para no saturar. | |
| P-38 | ¿Se limita el número de postulaciones activas por usuario? | [FS-OPO-02](./specs/oportunidades/FS-OPO-02-postulaciones.md) | No al inicio: revisar con datos reales. | |

### Sprint 7 — Eventos

| ID | Pregunta | Origen | Propuesta | Decisión |
|---|---|---|---|---|
| P-39 | ¿Los eventos próximos también se muestran en el feed? | [FS-EVT-01](./specs/eventos/FS-EVT-01-publicacion-listado-eventos.md) | No: basta con la sección Eventos. | |
| P-40 | ¿Se necesita lista de espera para eventos con cupo? | [FS-EVT-02](./specs/eventos/FS-EVT-02-confirmacion-asistencia.md) | No en el MVP. | |
| P-41 | ¿El organizador puede escribir un mensaje a todos los asistentes? | [FS-EVT-02](./specs/eventos/FS-EVT-02-confirmacion-asistencia.md) | Sí, como un aviso que llega por notificación y no como un chat grupal. | |

### Sprint 8 — Proyectos

| ID | Pregunta | Origen | Propuesta | Decisión |
|---|---|---|---|---|
| P-42 | ¿Se necesita un espacio de conversación del equipo dentro del proyecto? | [FS-PRY-01](./specs/proyectos/FS-PRY-01-espacios-proyectos.md) | No en el MVP: los miembros se coordinan por mensajes privados. | |
| P-43 | ¿Los proyectos de clase pueden ser privados? | [FS-PRY-01](./specs/proyectos/FS-PRY-01-espacios-proyectos.md) | Sí: un proyecto privado solo lo ven sus miembros. | |
| P-44 | ¿El rol por defecto de los nuevos miembros es configurable por proyecto? | [FS-PRY-02](./specs/proyectos/FS-PRY-02-roles-proyectos.md) | No en el MVP. | |

## E. Para después del lanzamiento

Ninguna de estas preguntas bloquea el MVP. Se revisan con datos reales o cuando se retome la fase 2.

| ID | Pregunta | Origen | Propuesta | Decisión |
|---|---|---|---|---|
| P-45 | ¿Son razonables los pesos del puntaje de sugerencias (3, 2, 1, 1)? | [FS-RED-02](./specs/red/FS-RED-02-onboarding-sugerencias.md) | Revisarlos tres meses después del lanzamiento. | |
| P-46 | ¿El cruce debe reconocer etiquetas parecidas y no solo idénticas? | [FS-PRF-01](./specs/perfil/FS-PRF-01-perfil-profesional.md) | Explorarlo con el equipo de Aluna I.A. | |
| P-47 | ¿Se permite adjuntar archivos en los mensajes? | [FS-MSG-01](./specs/mensajeria/FS-MSG-01-mensajeria-privada.md) | Evaluarlo en una versión posterior. | |
| P-48 | ¿Las credenciales verificadas aparecen en la hoja de vida en PDF? | [FS-PRF-03](./specs/perfil/FS-PRF-03-hoja-de-vida-pdf.md) | Sí, cuando exista FS-SRV-01 (fase 2). | |
| P-49 | ¿Se necesita un rol de "moderador" con menos permisos que el administrador? | [FS-ADM-01](./specs/administracion/FS-ADM-01-gestion-categorias.md) | Evaluarlo si el volumen de reportes supera la capacidad de los administradores. | |

## Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-08 | Gamero | Creación: 49 preguntas consolidadas de 22 specs, los requisitos no funcionales y las normas. |
