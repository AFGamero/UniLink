# Catálogo de requisitos — UniLink

_Complemento del [informe integral](./informe_integral_unilink.md) · Corte: 2026-10-27_

Este catálogo es un **índice**. La fuente de verdad de cada requisito funcional es su spec; la de los requisitos no funcionales, el [SRS §3.3](./srs/Especificacion_Requisitos.md#33-requisitos-no-funcionales). Si este índice y un spec no coinciden, manda el spec. El índice se generó leyendo la sección 5 de cada spec, y puede regenerarse.

## 1. Identificación

Los requisitos conservan los identificadores del repositorio para no crear una segunda numeración:

| Tipo | Formato | Ejemplo | Único en |
|---|---|---|---|
| Requisito funcional | `<MOD>-NN/RF-NN` | `USR-01/RF-03` | Todo el proyecto (el prefijo del spec lo hace único) |
| Regla de negocio | `<MOD>-NN/RN-NN` | `COL-04/RN-03` | Todo el proyecto |
| Requisito no funcional | `RNF-<CAT>-NN` | `RNF-SEG-04` | Todo el proyecto |
| Escenario de calidad | `EC-NN` | `EC-04` | Todo el proyecto |
| Requisito decidido sin especificar | `RD-NN` | `RD-03` | Este catálogo (sección 5) |

**Estado de implementación:** ningún requisito está implementado, porque el repositorio no contiene código (H-22). La columna "Estado" indica el estado del **spec** (todos en Borrador) y si una decisión de la reunión del 2026-10-19 lo deja desactualizado.

## 2. Resumen por spec

| Spec | Nombre | Casos de uso | RF | RN | Mensajes | Escenarios Gherkin | Desactualizado por (hallazgo) |
|---|---|---|---|---|---|---|---|
| [FS-USR-01](./modulos/usuarios/specs/FS-USR-01-registro.md) | Registro y verificación de cuenta | CU-01 | 8 | 11 | 8 | 14 | H-02, H-15 |
| [FS-USR-02](./modulos/usuarios/specs/FS-USR-02-inicio-sesion.md) | Inicio y cierre de sesión | CU-02 | 8 | 7 | 6 | 13 | H-02 |
| [FS-USR-03](./modulos/usuarios/specs/FS-USR-03-recuperar-contrasena.md) | Recuperación de contraseña | CU-17 | 5 | 10 | 6 | 10 | H-02 |
| [FS-USR-04](./modulos/usuarios/specs/FS-USR-04-preferencias-contenido.md) | Preferencias de contenido | CU-18 | 4 | 5 | 2 | 6 | — |
| [FS-USR-05](./modulos/usuarios/specs/FS-USR-05-configuracion-cuenta.md) | Configuración de cuenta y privacidad | CU-03 | 8 | 12 | 11 | 11 | H-03 |
| [FS-USR-06](./modulos/usuarios/specs/FS-USR-06-perfil-profesional.md) | Perfil profesional | CU-04 | 7 | 13 | 13 | 13 | H-08, H-15 |
| [FS-USR-07](./modulos/usuarios/specs/FS-USR-07-hoja-de-vida-pdf.md) | Hoja de vida en PDF | CU-19 | 5 | 9 | 4 | 8 | — |
| [FS-USR-08](./modulos/usuarios/specs/FS-USR-08-gestion-cuentas.md) | Gestión de cuentas de usuario | CU-24 | 7 | 8 | 5 | 9 | H-05, H-12 |
| [FS-RED-01](./modulos/red/specs/FS-RED-01-solicitudes-conexion.md) | Solicitudes de conexión | CU-06, CU-07 | 9 | 11 | 9 | 14 | H-12 |
| [FS-RED-02](./modulos/red/specs/FS-RED-02-onboarding-sugerencias.md) | Onboarding y sugerencias de conexión | CU-13 | 6 | 11 | 5 | 10 | H-14 |
| [FS-RED-03](./modulos/red/specs/FS-RED-03-busqueda-perfiles.md) | Búsqueda de perfiles | CU-05 | 8 | 9 | 5 | 13 | H-16 |
| [FS-CNT-01](./modulos/contenido/specs/FS-CNT-01-publicaciones-feed.md) | Publicaciones y feed | CU-08, CU-09 | 10 | 19 | 9 | 15 | H-09, H-11 |
| [FS-CNT-02](./modulos/contenido/specs/FS-CNT-02-moderacion-contenido.md) | Moderación de contenido | CU-25 | 8 | 17 | 6 | 13 | H-05, H-06, H-12 |
| [FS-COM-01](./modulos/comunicacion/specs/FS-COM-01-mensajeria-privada.md) | Mensajería privada | CU-10 | 9 | 13 | 6 | 13 | H-18 |
| [FS-COM-02](./modulos/comunicacion/specs/FS-COM-02-centro-notificaciones.md) | Centro de notificaciones | CU-23 | 6 | 11 | 4 | 11 | — |
| [FS-COL-01](./modulos/colaboracion/specs/FS-COL-01-publicacion-oportunidades.md) | Publicación de oportunidades | CU-22 | 9 | 15 | 7 | 11 | — |
| [FS-COL-02](./modulos/colaboracion/specs/FS-COL-02-postulaciones.md) | Postulaciones | CU-12, CU-14 | 8 | 10 | 7 | 12 | — |
| [FS-COL-03](./modulos/colaboracion/specs/FS-COL-03-publicacion-listado-eventos.md) | Publicación y listado de eventos | CU-20, CU-21 | 9 | 13 | 7 | 11 | H-11 |
| [FS-COL-04](./modulos/colaboracion/specs/FS-COL-04-confirmacion-asistencia.md) | Confirmación de asistencia (RSVP) | CU-15 | 8 | 10 | 6 | 11 | H-11 |
| [FS-COL-05](./modulos/colaboracion/specs/FS-COL-05-espacios-proyectos.md) | Espacios de proyectos | CU-11 | 10 | 19 | 7 | 13 | H-10, H-16, H-04 |
| [FS-COL-06](./modulos/colaboracion/specs/FS-COL-06-roles-proyectos.md) | Roles en proyectos | CU-16 | 6 | 10 | 6 | 10 | H-10 |
| [FS-PLT-01](./modulos/plataforma/specs/FS-PLT-01-gestion-categorias.md) | Gestión de categorías | CU-26 | 9 | 13 | 7 | 12 | H-05, H-08 |
| **Total (22 specs)** | | | **167** | **256** | **146** | **253** | |

Prioridad de los requisitos funcionales: 117 Alta, 44 Media y 6 Baja. La fase 2 (módulo de servicios, CU-27 a CU-30) no tiene specs ni requisitos funcionales.

## 3. Requisitos funcionales

Para cada requisito, el actor, las precondiciones, el flujo, las excepciones, las reglas, los criterios de aceptación (Gherkin) y los contratos están en las secciones 2 a 13 de su spec. Aquí se repiten solo el texto y la prioridad.

### 3.1 Usuarios

**[FS-USR-01](./modulos/usuarios/specs/FS-USR-01-registro.md) — Registro y verificación de cuenta** · CU-01 · Estado: Borrador; desactualizado (H-02, H-15)

| ID | Requisito | Prioridad |
|---|---|---|
| USR-01/RF-01 | El sistema debe mostrar un formulario de registro con los campos de la sección 6. | Alta |
| USR-01/RF-02 | El sistema debe validar cada campo al perder el foco y de nuevo al enviar el formulario. | Alta |
| USR-01/RF-03 | El sistema debe crear la cuenta en estado **Pendiente de verificación** y enviar el enlace al correo ingresado. | Alta |
| USR-01/RF-04 | El sistema debe mostrar una pantalla de "Revisa tu correo" con la opción de reenviar el enlace. | Alta |
| USR-01/RF-05 | Al abrir un enlace válido, el sistema debe activar la cuenta, iniciar sesión y redirigir a la edición de perfil. Mientras la edición de perfil no exista (Sprint 1), redirige a una página de bienvenida con acceso a la configuración y al cierre de sesión. | Alta |
| USR-01/RF-06 | Al abrir un enlace vencido o inválido, el sistema debe explicarlo y ofrecer reenviar uno nuevo. | Alta |
| USR-01/RF-07 | _(Fase 2)_ Si el correo no es institucional, el sistema debe mostrar, además del error, un enlace al registro de egresados y tercerizados. | Media |
| USR-01/RF-08 | El sistema debe guardar la contraseña cifrada con un algoritmo de hash con sal; nunca en texto plano. | Alta |

**[FS-USR-02](./modulos/usuarios/specs/FS-USR-02-inicio-sesion.md) — Inicio y cierre de sesión** · CU-02 · Estado: Borrador; desactualizado (H-02)

| ID | Requisito | Prioridad |
|---|---|---|
| USR-02/RF-01 | El sistema debe mostrar un formulario con correo, contraseña, "Mantener sesión iniciada" y el enlace "¿Olvidaste tu contraseña?". | Alta |
| USR-02/RF-02 | El sistema debe validar las credenciales y, si son correctas, crear la sesión y redirigir según RN-06. | Alta |
| USR-02/RF-03 | El sistema debe indicar los intentos restantes cuando quedan 2 o menos. | Media |
| USR-02/RF-04 | El sistema debe bloquear la cuenta según RN-02 e informar cuánto tiempo falta para desbloquearla. | Alta |
| USR-02/RF-05 | Si la cuenta está pendiente de verificación, el sistema debe ofrecer reenviar el enlace ([FS-USR-01](./modulos/usuarios/specs/FS-USR-01-registro.md)). | Alta |
| USR-02/RF-06 | Si la cuenta está suspendida o inhabilitada, el sistema debe impedir el acceso e informar el estado. | Alta |
| USR-02/RF-07 | El sistema debe ofrecer la opción "Cerrar sesión" en el menú del usuario. | Alta |
| USR-02/RF-08 | Si un usuario sin sesión intenta abrir una página protegida, el sistema debe llevarlo al inicio de sesión y, al ingresar, devolverlo a esa página. | Media |

**[FS-USR-03](./modulos/usuarios/specs/FS-USR-03-recuperar-contrasena.md) — Recuperación de contraseña** · CU-17 · Estado: Borrador; desactualizado (H-02)

| ID | Requisito | Prioridad |
|---|---|---|
| USR-03/RF-01 | El sistema debe mostrar un formulario para ingresar el correo, accesible desde el inicio de sesión. | Alta |
| USR-03/RF-02 | El sistema debe enviar el enlace de restablecimiento según RN-01 a RN-04 y RN-08. | Alta |
| USR-03/RF-03 | Al abrir un enlace válido, el sistema debe mostrar un formulario para la nueva contraseña y su confirmación. | Alta |
| USR-03/RF-04 | El sistema debe guardar la nueva contraseña, aplicar RN-06 y RN-07, y redirigir al inicio de sesión. | Alta |
| USR-03/RF-05 | Al abrir un enlace vencido, usado o inválido, el sistema debe explicarlo y ofrecer solicitar uno nuevo. | Alta |

**[FS-USR-04](./modulos/usuarios/specs/FS-USR-04-preferencias-contenido.md) — Preferencias de contenido** · CU-18 · Estado: Borrador

| ID | Requisito | Prioridad |
|---|---|---|
| USR-04/RF-01 | El sistema debe mostrar en el registro un paso opcional con las categorías activas agrupadas por tipo. | Alta |
| USR-04/RF-02 | El sistema debe guardar las categorías elegidas al crear la cuenta. | Alta |
| USR-04/RF-03 | El sistema debe permitir modificar las categorías desde la configuración de la cuenta. | Media |
| USR-04/RF-04 | El sistema debe ofrecer una consulta interna de las preferencias de un usuario para el feed (FS-CNT-01), el onboarding (FS-RED-02), los eventos (FS-COL-03) y los proyectos (FS-COL-05). | Alta |

**[FS-USR-05](./modulos/usuarios/specs/FS-USR-05-configuracion-cuenta.md) — Configuración de cuenta y privacidad** · CU-03 · Estado: Borrador; desactualizado (H-03)

| ID | Requisito | Prioridad |
|---|---|---|
| USR-05/RF-01 | El sistema debe ofrecer una página de configuración con las secciones: Cuenta, Seguridad, Privacidad, Notificaciones, Intereses y Eliminar cuenta. | Alta |
| USR-05/RF-02 | El sistema debe permitir cambiar el correo según RN-01 a RN-04, mostrando el correo pendiente mientras no se verifique. | Media |
| USR-05/RF-03 | El sistema debe permitir cambiar la contraseña según RN-01, RN-04 y RN-05. | Alta |
| USR-05/RF-04 | El sistema debe permitir elegir el nivel de privacidad del perfil (RN-06) y aplicarlo de inmediato en perfil, búsqueda y sugerencias. | Alta |
| USR-05/RF-05 | El sistema debe permitir activar o desactivar cada tipo de notificación por correo (RN-07). | Media |
| USR-05/RF-06 | El sistema debe permitir cerrar la sesión en todos los dispositivos excepto el actual. | Media |
| USR-05/RF-07 | El sistema debe permitir eliminar la cuenta según RN-01, RN-08, RN-09 y RN-12, explicando antes qué se elimina y cuándo. | Alta |
| USR-05/RF-08 | El sistema debe permitir registrar, verificar, cambiar y quitar el correo de respaldo (RN-11). | Media |

**[FS-USR-06](./modulos/usuarios/specs/FS-USR-06-perfil-profesional.md) — Perfil profesional** · CU-04 · Estado: Borrador; desactualizado (H-08, H-15)

| ID | Requisito | Prioridad |
|---|---|---|
| USR-06/RF-01 | El sistema debe mostrar un formulario de edición de perfil organizado por secciones (sección 6). | Alta |
| USR-06/RF-02 | El sistema debe validar los campos obligatorios y no guardar hasta completarlos (RN-01). | Alta |
| USR-06/RF-03 | El sistema debe ofrecer un campo de etiquetas con autocompletado sobre el catálogo predefinido para habilidades, intereses, "Puedo aportar" y "Necesito" (RN-03, RN-04). | Alta |
| USR-06/RF-04 | El sistema debe mostrar el perfil público con una sección destacada "Puedo aportar / Necesito" debajo del titular. | Alta |
| USR-06/RF-05 | El sistema debe mostrar al dueño un indicador de completitud (RN-08) con las secciones que le faltan. | Media |
| USR-06/RF-06 | El sistema debe ofrecer por su interfaz pública los datos públicos, la privacidad y las etiquetas de un perfil, y la afinidad de un usuario con una lista de habilidades, para Red y Colaboración. | Alta |
| USR-06/RF-07 | Al guardar, el sistema debe confirmar el cambio y mostrar el perfil actualizado. | Alta |

**[FS-USR-07](./modulos/usuarios/specs/FS-USR-07-hoja-de-vida-pdf.md) — Hoja de vida en PDF** · CU-19 · Estado: Borrador

| ID | Requisito | Prioridad |
|---|---|---|
| USR-07/RF-01 | El sistema debe mostrar el botón "Descargar hoja de vida" en el perfil propio. | Alta |
| USR-07/RF-02 | Antes de generar, el sistema debe permitir elegir si incluir foto, correo y teléfono (por defecto: foto y correo sí, teléfono no). | Media |
| USR-07/RF-03 | El sistema debe generar el PDF con las secciones de la sección 6, aplicando RN-04 a RN-09. | Alta |
| USR-07/RF-04 | El sistema debe generar el archivo en menos de 10 segundos e iniciar la descarga. | Alta |
| USR-07/RF-05 | Si el perfil está incompleto (RN-02), el sistema debe indicar qué falta y enlazar a la edición del perfil. | Alta |

**[FS-USR-08](./modulos/usuarios/specs/FS-USR-08-gestion-cuentas.md) — Gestión de cuentas de usuario** · CU-24 · Estado: Borrador; desactualizado (H-05, H-12)

| ID | Requisito | Prioridad |
|---|---|---|
| USR-08/RF-01 | El panel de administración debe incluir la sección "Usuarios". | Alta |
| USR-08/RF-02 | El listado debe mostrar nombre, correo, tipo de usuario, unidad académica, fecha de registro, último acceso y estado, con 25 cuentas por página. | Alta |
| USR-08/RF-03 | El listado debe permitir buscar por nombre o correo y filtrar por estado, tipo de usuario y unidad académica. | Alta |
| USR-08/RF-04 | El detalle de una cuenta debe mostrar sus datos básicos, número de publicaciones y conexiones, reportes recibidos, contenido retirado por moderación ([FS-CNT-02](./modulos/contenido/specs/FS-CNT-02-moderacion-contenido.md)) e historial de acciones de administración. La pantalla reúne esos datos pidiéndolos a cada módulo desde la capa de API (ADR-003). | Alta |
| USR-08/RF-05 | El sistema debe permitir suspender (RN-01), inhabilitar (RN-02) y reactivar cuentas, con confirmación y motivo (RN-03). | Alta |
| USR-08/RF-06 | El sistema debe aplicar los efectos de RN-04 de inmediato y enviar el correo de RN-05. | Alta |
| USR-08/RF-07 | Una tarea programada debe reactivar las cuentas cuya suspensión terminó (RN-01). | Alta |

### 3.2 Red

**[FS-RED-01](./modulos/red/specs/FS-RED-01-solicitudes-conexion.md) — Solicitudes de conexión** · CU-06, CU-07 · Estado: Borrador; desactualizado (H-12)

| ID | Requisito | Prioridad |
|---|---|---|
| RED-01/RF-01 | El sistema debe mostrar en el perfil de otro usuario y en las tarjetas de búsqueda un botón cuyo texto depende del estado de la relación (sección 7). | Alta |
| RED-01/RF-02 | Al pulsar "Conectar", el sistema debe permitir agregar un mensaje opcional y enviar la solicitud. | Alta |
| RED-01/RF-03 | El sistema debe ofrecer una página "Mi red" con tres pestañas: Conexiones, Solicitudes recibidas y Solicitudes enviadas. | Alta |
| RED-01/RF-04 | En Solicitudes recibidas, cada solicitud debe mostrar la tarjeta del solicitante, su mensaje, el motivo de complementariedad si aplica, y los botones "Aceptar" y "Rechazar". | Alta |
| RED-01/RF-05 | El sistema debe permitir cancelar una solicitud enviada desde el perfil del destinatario o desde Solicitudes enviadas. | Media |
| RED-01/RF-06 | El sistema debe permitir eliminar una conexión desde el perfil de la persona o desde la pestaña Conexiones, pidiendo confirmación. | Media |
| RED-01/RF-07 | La pestaña Conexiones debe permitir buscar por nombre dentro de las propias conexiones y mostrar el total. | Media |
| RED-01/RF-08 | El perfil público debe mostrar el número de conexiones del usuario. | Baja |
| RED-01/RF-09 | El menú principal debe mostrar el número de solicitudes recibidas pendientes. | Alta |

**[FS-RED-02](./modulos/red/specs/FS-RED-02-onboarding-sugerencias.md) — Onboarding y sugerencias de conexión** · CU-13 · Estado: Borrador; desactualizado (H-14)

| ID | Requisito | Prioridad |
|---|---|---|
| RED-02/RF-01 | El sistema debe mostrar la pantalla de onboarding según RN-01. | Alta |
| RED-02/RF-02 | El sistema debe calcular y mostrar las sugerencias según RN-03 a RN-06, cada una como tarjeta con casilla de selección. | Alta |
| RED-02/RF-03 | El sistema debe ofrecer "Seleccionar todos" y mostrar cuántas personas hay seleccionadas. | Media |
| RED-02/RF-04 | Al pulsar "Conectar con {n} personas", el sistema debe enviar las solicitudes y llevar al usuario a la página principal. | Alta |
| RED-02/RF-05 | El sistema debe ofrecer "Omitir por ahora", que lleva a la página principal sin enviar solicitudes. | Alta |
| RED-02/RF-06 | El sistema debe resaltar con una insignia las sugerencias por complementariedad. | Media |

**[FS-RED-03](./modulos/red/specs/FS-RED-03-busqueda-perfiles.md) — Búsqueda de perfiles** · CU-05 · Estado: Borrador; desactualizado (H-16)

| ID | Requisito | Prioridad |
|---|---|---|
| RED-03/RF-01 | El sistema debe ofrecer una barra de búsqueda accesible desde el menú principal. | Alta |
| RED-03/RF-02 | El sistema debe ofrecer los filtros de la sección 6, con autocompletado en los filtros de etiquetas. | Alta |
| RED-03/RF-03 | El sistema debe mostrar cada resultado como una tarjeta: foto, nombre, titular, unidad académica, hasta 3 etiquetas de "Puede aportar" y, si aplica, la insignia de monitor académico (RN-09). | Alta |
| RED-03/RF-04 | Si un resultado es complementario con quien busca, la tarjeta debe mostrar el motivo (por ejemplo, "Puede aportar Diseño gráfico, que tú necesitas"). | Media |
| RED-03/RF-05 | El sistema debe mostrar el número total de resultados y la paginación (RN-06). | Media |
| RED-03/RF-06 | Al seleccionar una tarjeta, el sistema debe abrir el perfil respetando la privacidad. | Alta |
| RED-03/RF-07 | Los filtros aplicados deben reflejarse en la URL, para poder compartir o volver a una búsqueda. | Baja |
| RED-03/RF-08 | El sistema debe mostrar un mensaje cuando no hay resultados, con la opción de limpiar filtros. | Alta |

### 3.3 Contenido

**[FS-CNT-01](./modulos/contenido/specs/FS-CNT-01-publicaciones-feed.md) — Publicaciones y feed** · CU-08, CU-09 · Estado: Borrador; desactualizado (H-09, H-11)

| ID | Requisito | Prioridad |
|---|---|---|
| CNT-01/RF-01 | El sistema debe ofrecer un cuadro "Comparte algo con la comunidad" en la parte superior del feed que abre el formulario de publicación. | Alta |
| CNT-01/RF-02 | El sistema debe validar y publicar según RN-01 a RN-03, y mostrar la publicación de inmediato al inicio del feed del autor. | Alta |
| CNT-01/RF-03 | El sistema debe mostrar cada publicación con: foto, nombre y titular del autor, fecha relativa ("hace 2 h"), categoría, título, texto (recortado a 5 líneas con "Ver más"), adjuntos, número de "Me gusta" y de comentarios, y los botones de interacción. | Alta |
| CNT-01/RF-04 | El sistema debe ofrecer el filtro por categoría y el selector "Recientes / Relevantes" en el feed. | Media |
| CNT-01/RF-05 | El sistema debe permitir editar y eliminar publicaciones propias (RN-04, RN-05), pidiendo confirmación para eliminar. | Alta |
| CNT-01/RF-06 | El sistema debe permitir dar o quitar "Me gusta" y mostrar la lista de quiénes reaccionaron. | Media |
| CNT-01/RF-07 | El sistema debe permitir comentar y mostrar los 2 comentarios más recientes bajo la publicación, con "Ver todos los comentarios". | Alta |
| CNT-01/RF-08 | Cada publicación debe tener una página propia accesible por enlace (RN-15). | Media |
| CNT-01/RF-09 | El perfil de cada usuario debe mostrar una pestaña "Publicaciones" con las suyas, respetando RN-06. | Media |
| CNT-01/RF-10 | Los PDF deben poder abrirse o descargarse; las imágenes deben verse ampliadas al pulsarlas. | Media |

**[FS-CNT-02](./modulos/contenido/specs/FS-CNT-02-moderacion-contenido.md) — Moderación de contenido** · CU-25 · Estado: Borrador; desactualizado (H-05, H-06, H-12)

| ID | Requisito | Prioridad |
|---|---|---|
| CNT-02/RF-01 | El sistema debe agregar la opción "Reportar" a todo elemento `Reportable` ajeno, con el formulario de motivos (RN-03). | Alta |
| CNT-02/RF-02 | El sistema debe aplicar RN-02 y RN-04 automáticamente. | Alta |
| CNT-02/RF-03 | El panel de administración debe incluir la sección "Moderación" con la cola (RN-05) y un indicador del número de elementos pendientes. | Alta |
| CNT-02/RF-04 | Cada elemento de la cola debe mostrar el contenido completo, su autor, la cantidad de reportes, los motivos agrupados y los comentarios de "Otro". | Alta |
| CNT-02/RF-05 | El sistema debe permitir "Retirar" (RN-06, RN-09) o "Mantener" (RN-07) cada elemento. | Alta |
| CNT-02/RF-06 | La sección Moderación debe tener una pestaña "Todas las publicaciones" con búsqueda por texto y autor, para aplicar RN-08. | Media |
| CNT-02/RF-07 | La sección Moderación debe tener una pestaña "Historial" con las decisiones tomadas. | Media |
| CNT-02/RF-08 | El mecanismo de reportes debe admitir nuevos tipos de contenido sin cambiar la cola ni las reglas (RN-13). | Alta |

### 3.4 Comunicación

**[FS-COM-01](./modulos/comunicacion/specs/FS-COM-01-mensajeria-privada.md) — Mensajería privada** · CU-10 · Estado: Borrador; desactualizado (H-18)

| ID | Requisito | Prioridad |
|---|---|---|
| COM-01/RF-01 | El sistema debe mostrar un ícono de mensajes en el menú principal con el número de conversaciones con mensajes sin leer. | Alta |
| COM-01/RF-02 | El sistema debe ofrecer una página "Mensajes" con la bandeja a la izquierda (foto, nombre, último mensaje y hora, ordenadas por actividad) y la conversación abierta a la derecha. En celular, se muestran por separado. | Alta |
| COM-01/RF-03 | El sistema debe permitir iniciar una conversación desde el botón "Enviar mensaje" del perfil de una conexión, desde "Mi red" y, para una postulación aceptada, desde el panel de postulaciones del responsable ([FS-COL-01](./modulos/colaboracion/specs/FS-COL-01-publicacion-oportunidades.md)) y desde "Mis postulaciones" del postulante ([FS-COL-02](./modulos/colaboracion/specs/FS-COL-02-postulaciones.md)). | Alta |
| COM-01/RF-04 | El sistema debe entregar los mensajes en tiempo real (RN-04) y mostrar "Visto" (RN-05). | Alta |
| COM-01/RF-05 | La conversación debe cargar los 30 mensajes más recientes y los anteriores al desplazarse hacia arriba. | Alta |
| COM-01/RF-06 | El sistema debe permitir buscar conversaciones por nombre de la persona. | Media |
| COM-01/RF-07 | El sistema debe permitir ocultar una conversación (RN-07). | Baja |
| COM-01/RF-08 | El sistema debe agregar a cada publicación del feed la opción "Enviar por mensaje", que permite elegir una o varias conexiones (RN-12). | Media |
| COM-01/RF-09 | Si la conversación está en solo lectura (RN-06, RN-08), el campo de escritura debe reemplazarse por un aviso que explique el motivo. | Alta |

**[FS-COM-02](./modulos/comunicacion/specs/FS-COM-02-centro-notificaciones.md) — Centro de notificaciones** · CU-23 · Estado: Borrador

| ID | Requisito | Prioridad |
|---|---|---|
| COM-02/RF-01 | El sistema debe mostrar un ícono de campana con el indicador de no leídas en el menú principal. | Alta |
| COM-02/RF-02 | Al pulsar la campana, el sistema debe abrir un panel con las 20 notificaciones más recientes, con las no leídas resaltadas, y un enlace "Ver todas". | Alta |
| COM-02/RF-03 | La página "Ver todas" debe mostrar el historial completo con carga progresiva y filtro "Solo no leídas". | Media |
| COM-02/RF-04 | Al seleccionar una notificación, el sistema debe llevar al elemento relacionado y marcarla como leída. | Alta |
| COM-02/RF-05 | El sistema debe ofrecer "Marcar todas como leídas". | Media |
| COM-02/RF-06 | El sistema debe crear las notificaciones consumiendo los eventos de dominio de los demás módulos (ADR-004), aplicando RN-07 y RN-08 automáticamente. Ningún módulo llama a Comunicación para notificar. | Alta |

### 3.5 Colaboración

**[FS-COL-01](./modulos/colaboracion/specs/FS-COL-01-publicacion-oportunidades.md) — Publicación de oportunidades** · CU-22 · Estado: Borrador

| ID | Requisito | Prioridad |
|---|---|---|
| COL-01/RF-01 | El sistema debe ofrecer el botón "Publicar oportunidad" en la sección Oportunidades. | Alta |
| COL-01/RF-02 | El sistema debe validar y publicar la oportunidad con los datos de la sección 6. | Alta |
| COL-01/RF-03 | El sistema debe ofrecer al responsable una página "Mis oportunidades publicadas" con cada oportunidad, su estado y el número de postulaciones por estado. | Alta |
| COL-01/RF-04 | El panel de postulaciones de una oportunidad debe mostrar, por cada postulante: tarjeta de perfil, afinidad (RN-13), mensaje de motivación, fecha y estado, con filtro por estado y orden por afinidad o fecha. | Alta |
| COL-01/RF-05 | El sistema debe permitir cambiar el estado de una o varias postulaciones a la vez, con retroalimentación opcional (RN-10, RN-11). | Alta |
| COL-01/RF-06 | El sistema debe permitir editar, cerrar, cancelar y eliminar oportunidades según RN-06 a RN-09. | Alta |
| COL-01/RF-07 | Una tarea programada debe cerrar las oportunidades que llegan a su fecha de cierre (RN-05). | Alta |
| COL-01/RF-08 | El responsable debe recibir una notificación por cada postulación nueva y, si lo tiene activado, un correo. | Media |
| COL-01/RF-09 | En el panel de postulaciones, cada postulación aceptada debe ofrecer "Enviar mensaje" ([FS-COM-01](./modulos/comunicacion/specs/FS-COM-01-mensajeria-privada.md), RF-03). | Alta |

**[FS-COL-02](./modulos/colaboracion/specs/FS-COL-02-postulaciones.md) — Postulaciones** · CU-12, CU-14 · Estado: Borrador

| ID | Requisito | Prioridad |
|---|---|---|
| COL-02/RF-01 | El sistema debe ofrecer la sección "Oportunidades" en el menú principal. | Alta |
| COL-02/RF-02 | La sección debe mostrar cada oportunidad como tarjeta: título, responsable, categoría, modalidad, cupos disponibles, días para el cierre y afinidad. | Alta |
| COL-02/RF-03 | La sección debe permitir buscar por texto y filtrar por categoría, modalidad, habilidad requerida y "Solo con afinidad mayor al 50 %". También debe permitir ordenar por afinidad, más recientes o cierre más próximo. | Alta |
| COL-02/RF-04 | El detalle debe mostrar todos los datos de la oportunidad, el perfil resumido del responsable, las habilidades requeridas marcando cuáles tiene el usuario, y el botón "Postularme" o el estado de la postulación existente. | Alta |
| COL-02/RF-05 | Al postularse, el sistema debe pedir el mensaje de motivación, confirmar el envío y notificar al responsable. | Alta |
| COL-02/RF-06 | El sistema debe ofrecer el panel "Mis postulaciones" con cada postulación: oportunidad, responsable, fecha y estado como etiqueta de color, con filtro por estado. | Alta |
| COL-02/RF-07 | Al abrir una postulación, el sistema debe mostrar el historial de estados con la retroalimentación (RN-08) y la opción "Retirar postulación" cuando aplique (RN-07). Si la postulación está aceptada, ofrece "Enviar mensaje" al responsable ([FS-COM-01](./modulos/comunicacion/specs/FS-COM-01-mensajeria-privada.md), RF-03). | Alta |
| COL-02/RF-08 | El sistema debe mostrar un mensaje con enlace a la sección Oportunidades cuando el usuario no tenga postulaciones. | Media |

**[FS-COL-03](./modulos/colaboracion/specs/FS-COL-03-publicacion-listado-eventos.md) — Publicación y listado de eventos** · CU-20, CU-21 · Estado: Borrador; desactualizado (H-11)

| ID | Requisito | Prioridad |
|---|---|---|
| COL-03/RF-01 | El sistema debe ofrecer la sección "Eventos" en el menú principal, con el botón "Publicar evento". | Alta |
| COL-03/RF-02 | El sistema debe validar y publicar el evento con los datos de la sección 6. | Alta |
| COL-03/RF-03 | El apartado debe mostrar cada evento como tarjeta: portada, fecha y hora, título, modalidad y lugar, categoría y número de asistentes confirmados. | Alta |
| COL-03/RF-04 | El apartado debe permitir filtrar por categoría, modalidad y periodo (Hoy, Esta semana, Este mes, Todas las fechas) y buscar por texto. | Alta |
| COL-03/RF-05 | El apartado debe tener las pestañas "Próximos", "Mis eventos" (los que organizo y a los que asistiré) y "Pasados". | Media |
| COL-03/RF-06 | El detalle del evento debe mostrar todos sus datos, el organizador y, si aplica, la etiqueta "Cancelado" con el motivo o "Finalizado". | Alta |
| COL-03/RF-07 | El sistema debe permitir al organizador editar, cancelar y eliminar según RN-07 a RN-09. | Alta |
| COL-03/RF-08 | El menú "…" del evento debe ofrecer "Reportar" a los demás usuarios (RN-11). | Media |
| COL-03/RF-09 | El perfil del organizador debe mostrar una pestaña "Eventos" con los que ha publicado. | Baja |

**[FS-COL-04](./modulos/colaboracion/specs/FS-COL-04-confirmacion-asistencia.md) — Confirmación de asistencia (RSVP)** · CU-15 · Estado: Borrador; desactualizado (H-11)

| ID | Requisito | Prioridad |
|---|---|---|
| COL-04/RF-01 | El detalle del evento debe mostrar el botón "Asistiré" o, si el usuario ya confirmó, "Asistirás" con la opción de cancelar. | Alta |
| COL-04/RF-02 | El sistema debe aplicar RN-01 a RN-04 al confirmar o cancelar. | Alta |
| COL-04/RF-03 | Tras confirmar, el detalle debe mostrar la lista de asistentes (RN-05, RN-06) con buscador por nombre. | Alta |
| COL-04/RF-04 | Tras confirmar, el sistema debe ofrecer "Agregar a mi calendario" con dos opciones: descargar `.ics` y abrir en Google Calendar (RN-09). | Media |
| COL-04/RF-05 | El detalle debe mostrar a quien no ha confirmado el número de asistentes y cuántas de sus conexiones irán (RN-07). | Media |
| COL-04/RF-06 | El sistema debe enviar el recordatorio de RN-08 mediante una tarea programada. | Media |
| COL-04/RF-07 | El organizador debe ver en el detalle un resumen: confirmados, cupo restante y cancelaciones, y el botón "Descargar lista" (RN-10). | Media |
| COL-04/RF-08 | El evento debe aparecer en la pestaña "Mis eventos" del asistente ([FS-COL-03](./modulos/colaboracion/specs/FS-COL-03-publicacion-listado-eventos.md), RF-05). | Media |

**[FS-COL-05](./modulos/colaboracion/specs/FS-COL-05-espacios-proyectos.md) — Espacios de proyectos** · CU-11 · Estado: Borrador; desactualizado (H-10, H-16, H-04)

| ID | Requisito | Prioridad |
|---|---|---|
| COL-05/RF-01 | El sistema debe ofrecer la sección "Proyectos" en el menú principal con el botón "Crear proyecto". | Alta |
| COL-05/RF-02 | La sección debe mostrar los proyectos que están reclutando como tarjetas (nombre, categoría, habilidades buscadas, integrantes y cupo, afinidad), con búsqueda, filtros por categoría y habilidad, y orden por afinidad (RN-19) o más recientes. | Alta |
| COL-05/RF-03 | La sección debe tener las pestañas "Explorar", "Mis proyectos" y "Finalizados". | Media |
| COL-05/RF-04 | El espacio de cada proyecto debe tener las pestañas Resumen, Tareas, Miembros y Actividad. Quienes no son miembros solo ven Resumen y Miembros. | Alta |
| COL-05/RF-05 | La pestaña Tareas debe mostrar un tablero con tres columnas (Por hacer, En progreso, Hecha) donde las tareas se arrastran entre columnas, y un filtro "Mis tareas". | Alta |
| COL-05/RF-06 | El sistema debe permitir solicitar unirse (RN-08), y a los administradores aprobar o rechazar solicitudes desde la pestaña Miembros (RN-09). | Alta |
| COL-05/RF-07 | El sistema debe permitir a los administradores invitar a sus conexiones (RN-10). | Media |
| COL-05/RF-08 | El sistema debe permitir salir del proyecto (RN-12), finalizarlo (RN-06) y eliminarlo (RN-07). | Alta |
| COL-05/RF-09 | El perfil de cada usuario debe mostrar los proyectos finalizados en los que participó, con su rol y fechas. | Media |
| COL-05/RF-10 | El onboarding ([FS-RED-02](./modulos/red/specs/FS-RED-02-onboarding-sugerencias.md)) debe sugerir hasta 5 proyectos que están reclutando, con afinidad mayor a 0. Elegir uno envía una solicitud con el mensaje "Me interesa unirme a este proyecto." | Media |

**[FS-COL-06](./modulos/colaboracion/specs/FS-COL-06-roles-proyectos.md) — Roles en proyectos** · CU-16 · Estado: Borrador; desactualizado (H-10)

| ID | Requisito | Prioridad |
|---|---|---|
| COL-06/RF-01 | La pestaña Miembros debe mostrar a cada miembro con su rol, fecha de ingreso y, para el creador, la etiqueta "Creador". | Alta |
| COL-06/RF-02 | Los administradores deben ver junto a cada miembro un selector de rol y la opción "Retirar del proyecto", excepto donde RN-05 o RN-06 lo impiden. | Alta |
| COL-06/RF-03 | El sistema debe validar cada acción contra la matriz de permisos en el servidor, no solo ocultar botones en la pantalla. | Alta |
| COL-06/RF-04 | El sistema debe aplicar RN-05 y RN-06 con un mensaje que explique por qué la acción no está permitida. | Alta |
| COL-06/RF-05 | El sistema debe enviar la notificación de RN-08 y registrar el cambio en Actividad. | Media |
| COL-06/RF-06 | Cada miembro debe poder consultar qué puede hacer su rol (tabla de permisos accesible desde la pestaña Miembros). | Baja |

### 3.6 Plataforma

**[FS-PLT-01](./modulos/plataforma/specs/FS-PLT-01-gestion-categorias.md) — Gestión de categorías** · CU-26 · Estado: Borrador; desactualizado (H-05, H-08)

| ID | Requisito | Prioridad |
|---|---|---|
| PLT-01/RF-01 | El sistema debe mostrar la opción "Administración" en el menú del usuario solo a los administradores. | Alta |
| PLT-01/RF-02 | El panel debe tener un menú lateral con las secciones de administración. En este sprint existen "Categorías", "Palabras prohibidas" y "Auditoría"; "Usuarios" (FS-USR-08) y "Moderación" (FS-CNT-02) se agregan en el Sprint 5. | Alta |
| PLT-01/RF-03 | La sección Categorías debe mostrar una pestaña por tipo de contenido con sus categorías: nombre, descripción, estado, cantidad de contenido que la usa y orden. | Alta |
| PLT-01/RF-04 | El sistema debe permitir crear y editar categorías (RN-03, RN-04, RN-07). | Alta |
| PLT-01/RF-05 | El sistema debe permitir desactivar y reactivar categorías (RN-05, RN-06), pidiendo confirmación al desactivar e indicando cuánto contenido la usa. | Alta |
| PLT-01/RF-06 | El sistema debe permitir reordenar las categorías de un tipo arrastrándolas (RN-08). | Baja |
| PLT-01/RF-07 | El sistema debe mostrar el historial de cambios de cada categoría (RN-09). | Media |
| PLT-01/RF-08 | El sistema debe permitir agregar y quitar palabras prohibidas (RN-10), mostrando quién y cuándo. | Alta |
| PLT-01/RF-09 | La sección "Auditoría" debe listar el registro (RN-12) con filtros por administrador, módulo, acción y fechas, sin opción de editar ni borrar. | Media |

## 4. Requisitos no funcionales

Los 63 RNF están en el [SRS §3.3](./srs/Especificacion_Requisitos.md#33-requisitos-no-funcionales), cada uno con su descripción, cómo se verifica y su prioridad. La tabla los agrupa según las categorías del análisis. Todos están **especificados y sin verificar**, porque no hay implementación.

| Categoría del análisis | RNF del SRS | Cantidad | Métrica representativa | Observación |
|---|---|---|---|---|
| Rendimiento y tiempos de respuesta | RNF-REN-01 a 05 | 5 | API < 500 ms y escrituras < 1 s (p95) con 1.000 usuarios simultáneos | El supuesto se ajustó a 1.000 el 2026-10-27 (P-01). |
| Escalabilidad | Supuestos del SRS §2.7 | 0 | 25.000 registrados sin rediseño | No tiene ID ni criterio verificable: ver RNF-ESC-01 (propuesta). |
| Disponibilidad y resiliencia | RNF-DIS-01, 02, 05, 06 | 4 | 99,5 % mensual | En riesgo con infraestructura propia (H-27). |
| Recuperación ante fallos | RNF-DIS-03, 04; RNF-DES-04 | 3 | RPO 24 h, RTO 8 h; reversión en < 15 min | Depende de TI de la Universidad (ADR-009). |
| Seguridad | RNF-SEG-01 a 10 | 10 | TLS 1.2+, hash lento, cookies seguras, OWASP Top 10 sin hallazgos altos | Se complementa con [seguridad de la API](./arquitectura/seguridad-endpoints.md). |
| Privacidad y protección de datos | RNF-PRI-01 a 09 | 9 | Consultas en 10 días hábiles y reclamos en 15 (Ley 1581) | RNF-PRI-06 y 09 chocan con el borrado lógico (H-03). |
| Usabilidad | RNF-USA-01 a 05 | 5 | Registro, perfil y primera solicitud en < 10 min | RNF-USA-05 cambia con las cuentas precreadas. |
| Accesibilidad | RNF-ACC-01 a 06 | 6 | WCAG 2.1 AA | — |
| Compatibilidad multiplataforma | RNF-COM-01 a 03 | 3 | Dos últimas versiones de Chrome, Edge, Firefox y Safari; Chrome Android y Safari iOS | RNF-COM-02 excluye las aplicaciones nativas (H-21). |
| Mantenibilidad | RNF-MAN-01 a 07 | 7 | Cobertura ≥ 70 % del código de negocio; fronteras verificadas en CI | — |
| Testabilidad | RNF-MAN-01, 02; RNF-SEG-04 | 3 | Una prueba por regla de negocio; pruebas de permisos por API | Ver RNF-TES-01 (propuesta). |
| Observabilidad y registro | RNF-OBS-01 a 04 | 4 | Registros estructurados con identificador por petición | Retención de registros pendiente (P-52). |
| Portabilidad y despliegue | RNF-DES-01 a 03 | 3 | Tres entornos; despliegue automático a pruebas | — |
| Integridad y consistencia | RNF-CON-01 a 04 | 4 | Cupos atómicos; `If-Match`; `Idempotency-Key`; eventos al menos una vez sin duplicar | — |
| Retención de datos | RNF-PRI-09 | (en privacidad) | Tabla única de plazos | Afectada por H-03. |

**Propuestas pendientes de aprobación.** Cubren categorías sin requisito medible o decisiones de la reunión del 2026-10-19 sin RNF. **No son compromisos** hasta que el equipo las apruebe y las agregue al SRS.

| ID propuesto | Categoría | Requisito propuesto | Métrica y criterio de aceptación | Justificación |
|---|---|---|---|---|
| RNF-ESC-01 | Escalabilidad | La aplicación y el trabajador se pueden ejecutar en varias instancias sin estado compartido en memoria. | Prueba de carga con 2 instancias y el doble del pico (2.000 usuarios simultáneos) sin degradar RNF-REN-01. | Da criterio verificable a "25.000 sin rediseño" y protege los picos de las convocatorias de monitores. |
| RNF-DIS-07 | Disponibilidad | Si el Campus Virtual no responde, las sesiones abiertas siguen funcionando y el inicio de sesión muestra un mensaje claro; los usuarios externos no se ven afectados. | Prueba desactivando el servicio simulado del Campus Virtual: 0 errores en sesiones abiertas (EC-08). | Nueva dependencia crítica (ADR-013, H-25). |
| RNF-INT-01 | Integridad | Una sincronización fallida con el directorio institucional no deja cuentas a medio crear ni estados de monitor inconsistentes; se reintenta. | Prueba que corta la sincronización a mitad del lote y verifica el estado final. | ADR-014. |
| RNF-TES-01 | Testabilidad | Cada operación de `contracts/api/` tiene al menos tres pruebas de acceso: sin sesión, sin permiso y con permiso. | Reporte de la CI que relaciona cada `operationId` con sus pruebas. | Lleva la regla de [seguridad de la API §10](./arquitectura/seguridad-endpoints.md#10-cómo-se-verifica) al SRS. |
| RNF-COM-04 | Compatibilidad | _(Solo si se adopta ADR-016 B)_ La web se puede instalar como PWA en Chrome para Android y no guarda en caché respuestas con datos personales. | Auditoría de Lighthouse "Installable" y revisión de la política del service worker. | ADR-016. |

**Escenarios de calidad propuestos** (se suman a EC-01 a EC-07 del [SRS §3.4](./srs/Especificacion_Requisitos.md#34-escenarios-de-atributos-de-calidad)):

| ID | Atributo | Estímulo | Respuesta | Medida |
|---|---|---|---|---|
| EC-08 | Disponibilidad | El Campus Virtual deja de responder durante 30 minutos en hora pico | Las sesiones abiertas y los usuarios externos siguen operando; el inicio de sesión institucional muestra un aviso | 0 errores en sesiones abiertas |
| EC-09 | Rendimiento | Se publica el listado de monitores y 1.000 usuarios buscan en la sección Personas a la vez | La búsqueda con el filtro de monitor responde | p95 < 1 s (RNF-REN-02) |

## 5. Requisitos decididos sin especificar (reunión del 2026-10-19)

Estas decisiones del equipo todavía **no tienen spec**. Se listan para que no se pierdan, pero **no son requisitos verificables** hasta que el spec indicado las incorpore con sus reglas y escenarios. La columna "Cubierto" indica si el spec actual ya cumple la decisión.

| ID | Decisión | Módulo | Spec que debe incorporarla | Cubierto | Hallazgo |
|---|---|---|---|---|---|
| RD-01 | Las cuentas de la comunidad se precrean con correo institucional, nombre, facultad o programa y estado de monitor. | Usuarios | FS-USR-01 | No | H-02 |
| RD-02 | El usuario solo activa y personaliza su cuenta precreada. | Usuarios | FS-USR-01, FS-USR-06 | No | H-02 |
| RD-03 | Con la Universidad solo se comparte la autenticación (token del Campus Virtual). | Usuarios | FS-USR-02, ADR-013 | No | H-02, H-25 |
| RD-04 | Se permiten cuentas externas con registro propio; cada proyecto decide si admite externos. | Usuarios, Colaboración | FS-USR-01, FS-COL-05 | No | H-04 |
| RD-05 | El estado de monitor académico se actualiza en lote al publicarse el listado de la Vicerrectoría Académica, aunque la cuenta no esté activada. | Usuarios | FS-USR-01, ADR-014 | Parcial: FS-USR-06 RN-13 lo muestra; falta la sincronización en FS-USR-01 | H-15 |
| RD-06 | En el MVP, la API de admisiones se simula con correos ficticios. | Usuarios | ADR-014 | Sí (ADR) | H-26 |
| RD-07 | La sección Personas filtra por monitor académico, área y especialización. | Red | FS-RED-03 | Sí (RN-09, 2026-10-27) | — |
| RD-08 | En la sección Proyectos, el subtipo (investigación, desarrollo o creación) es un filtro; un semillero tiene varios proyectos; las categorías son generales. | Colaboración | FS-COL-05 | No | H-16 |
| RD-09 | En Explorar solo se muestran los eventos públicos. | Colaboración | FS-COL-03 | No (no hay eventos privados) | H-11 |
| RD-10 | Hay una vista personal "Yo" con conexiones, proyectos propios y actividades privadas. | Transversal | Spec de navegación (nuevo) | No | H-16 |
| RD-11 | El feed muestra los próximos eventos. | Contenido | FS-CNT-01, FS-COL-03 | No | H-11 |
| RD-12 | Bloqueo temporal por intentos fallidos, sin correo por cada bloqueo; se puede avisar de un inicio de sesión nuevo. | Usuarios | FS-USR-02 | Parcial | H-02 |
| RD-13 | Las etiquetas son predefinidas. | Usuarios, Plataforma | FS-USR-06 | Sí (RN-03, 2026-10-27); quién mantiene el catálogo: P-65 | H-08 |
| RD-14 | La lista de palabras prohibidas la mantiene el Administrador. | Plataforma | FS-PLT-01 | Sí | — |
| RD-15 | Eliminar una cuenta es un borrado lógico con trazabilidad (quién y cuándo). | Usuarios | FS-USR-05, ADR-015 | No (pendiente de P-12) | H-03 |
| RD-16 | Las solicitudes de conexión no vencen. | Red | FS-RED-01 | Sí (RN-08, 2026-10-27) | — |
| RD-17 | Se puede bloquear y reportar usuarios; el Administrador verifica y decide. | Red, Contenido | FS-RED-01, FS-CNT-02 | No | H-12 |
| RD-18 | Con 5 reportes el contenido se bloquea, no solo se oculta. | Contenido | FS-CNT-02 | No | H-06 |
| RD-19 | No hay perfiles semilla; el feed muestra perfiles afines. | Contenido, Red | FS-CNT-01, FS-RED-02 | No | H-14 |
| RD-20 | Hay una sola reacción ("Me gusta"). | Contenido | FS-CNT-01 | Sí | — |
| RD-21 | Cualquier usuario publica oportunidades, con moderación. | Colaboración | FS-COL-01 | Sí | — |
| RD-22 | El organizador puede enviar un mensaje a los asistentes. | Colaboración | FS-COL-04 | No | H-11 |
| RD-23 | Puede haber proyectos privados. | Colaboración | FS-COL-05 | No | H-10 |
| RD-24 | El rol por defecto de los no miembros es configurable; el creador define los roles. | Colaboración | FS-COL-06 | No | H-10 |
| RD-25 | La hoja de vida solo incluye las credenciales verificadas por la plataforma (fase 2). | Usuarios | FS-USR-07 | No aplica en el MVP | — |
| RD-26 | Se permiten adjuntos en los mensajes, condicionado a la mensajería. | Comunicación | FS-COM-01 | No (P-56) | H-13 |
| RD-27 | Hay dos roles: Administrador (control total, personal de la Universidad) y Moderador (reportes, bloqueos, contenido y lenguaje). | Transversal | SRS §2.4 y §2.5, FS-PLT-01, FS-CNT-02, FS-USR-08 | No | H-05 |
| RD-28 | La relevancia se prioriza por vistas, y el cruce reconoce etiquetas similares. | Contenido, Red | FS-CNT-01, FS-RED-02 | Parcial: sinónimos en FS-USR-06 RN-04; falta la relevancia por vistas | H-09 |

**Fuera del MVP por decisión:** chat de equipo en proyectos, registro interno de grupos, apelaciones dentro de la plataforma, sugerencias por afinidad como notificación, lista de espera en eventos, servicios entre estudiantes (fase 2), ruta institucional de atención (a lo sumo un enlace) y términos y condiciones aprobados por la Oficina Jurídica (antes de producción, no para el prototipo).

## Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-27 | Gamero | Creación: índice generado desde los specs, RNF agrupados, propuestas y decisiones sin especificar. |
| 2026-10-27 | Gamero | Regenerado tras actualizar FS-USR-06, FS-RED-01 y FS-RED-03; RD-07, RD-13 y RD-16 cubiertas. |
