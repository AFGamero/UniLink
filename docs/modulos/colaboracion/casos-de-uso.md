# Casos de uso — Colaboración

_MVP — Red Profesional Universitaria — Universidad del Magdalena_
_Centro de Interés de Desarrollo Tecnológico e Innovación (CIDTI)_

Casos de uso del módulo Colaboración (COL). Los actores se definen en el [mapa de módulos](../README.md#actores).

## Índice

- [CU-11 — Gestionar espacio de proyectos](#cu-11--gestionar-espacio-de-proyectos)
- [CU-12 — Explorar oportunidades](#cu-12--explorar-oportunidades)
- [CU-14 — Gestionar estado de postulaciones](#cu-14--gestionar-estado-de-postulaciones)
- [CU-15 — Confirmar asistencia a eventos (RSVP)](#cu-15--confirmar-asistencia-a-eventos-rsvp)
- [CU-16 — Administrar roles en espacios de proyectos](#cu-16--administrar-roles-en-espacios-de-proyectos)
- [CU-20 — Publicar evento](#cu-20--publicar-evento)
- [CU-21 — Visualizar eventos](#cu-21--visualizar-eventos)
- [CU-22 — Publicar oportunidades y gestionar postulaciones](#cu-22--publicar-oportunidades-y-gestionar-postulaciones)

---

## CU-11 — Gestionar espacio de proyectos

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario crear, unirse y colaborar en espacios de proyectos dedicados para trabajar en conjunto con otros miembros de la plataforma.

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El usuario crea un nuevo proyecto o solicita unirse a uno existente.
2. En caso de creación, define nombre, descripción, perfiles requeridos (por ejemplo, desarrollador o diseñador), número máximo de integrantes, tareas y objetivos del proyecto. El creador queda como administrador del proyecto.
3. En caso de solicitud de unión, el sistema notifica a los administradores del proyecto, quienes la aprueban o rechazan.
4. Los miembros colaboran dentro del espacio del proyecto según su nivel de acceso ([CU-16](#cu-16--administrar-roles-en-espacios-de-proyectos)).

**Flujos alternativos / excepciones:**

- 1a. El usuario solicita unirse a un proyecto que ya alcanzó el número máximo de integrantes: el sistema no permite la solicitud e informa el motivo.
- 3a. El administrador rechaza la solicitud de unión: el sistema notifica al solicitante.
- 4a. Un miembro decide abandonar el proyecto: el sistema lo retira del espacio. Si es el único administrador, se aplica la restricción 3a de [CU-16](#cu-16--administrar-roles-en-espacios-de-proyectos).

**Postcondiciones:** El espacio de proyecto queda creado o el usuario queda incorporado como miembro de un proyecto existente.

**Prioridad:** Media

---

## CU-12 — Explorar oportunidades

**Actor(es):** Usuario autenticado; Responsable de oportunidad (notificado)

**Descripción:** Permite al usuario consultar y postularse a oportunidades de investigación, proyectos y voluntariado publicadas en la plataforma por un responsable ([CU-22](#cu-22--publicar-oportunidades-y-gestionar-postulaciones)).

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El usuario accede a la sección de oportunidades.
2. Explora las ofertas disponibles, filtrando por categoría (investigación, proyectos, voluntariado).
3. Selecciona una oportunidad para ver su detalle.
4. Se postula directamente a la oportunidad.
5. El sistema registra la postulación con estado "Enviada" y notifica al responsable de la oportunidad.

**Flujos alternativos / excepciones:**

- 4a. El usuario ya se encuentra postulado a la misma oportunidad: el sistema no permite una nueva postulación y muestra el estado actual.
- 4b. La oportunidad fue cerrada por su responsable: el sistema no permite la postulación e informa el motivo.

**Postcondiciones:** La postulación queda registrada y visible tanto para el usuario ([CU-14](#cu-14--gestionar-estado-de-postulaciones)) como para el responsable de la oportunidad ([CU-22](#cu-22--publicar-oportunidades-y-gestionar-postulaciones)).

**Prioridad:** Media

---

## CU-14 — Gestionar estado de postulaciones

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario acceder a un panel específico para ver y hacer seguimiento al estado de sus postulaciones a oportunidades ("Enviada", "En revisión", "Aceptada" o "Rechazada"). Los cambios de estado los realiza el responsable de la oportunidad ([CU-22](#cu-22--publicar-oportunidades-y-gestionar-postulaciones)).

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El usuario accede al panel de gestión de postulaciones.
2. El sistema recupera y muestra el listado de oportunidades a las que el usuario se ha postulado.
3. El sistema muestra el estado actual de cada postulación ("Enviada", "En revisión", "Aceptada" o "Rechazada").
4. El usuario selecciona una postulación para visualizar el historial de cambios de estado o retroalimentación.

**Flujos alternativos / excepciones:**

- 2a. El usuario no tiene postulaciones activas ni pasadas: el sistema muestra un mensaje indicando que no hay postulaciones y sugiere explorar nuevas oportunidades.
- 4a. El usuario retira una postulación en estado "Enviada" o "En revisión": el sistema la marca como "Retirada" y notifica al responsable de la oportunidad.

**Postcondiciones:** El usuario se mantiene informado sobre el avance y resolución de sus postulaciones.

**Prioridad:** Alta

---

## CU-15 — Confirmar asistencia a eventos (RSVP)

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario confirmar su asistencia (RSVP) a un evento publicado, visualizar qué otros miembros asistirán y agregar el evento a su calendario personal.

**Precondiciones:** El usuario debe estar autenticado y visualizar la página de detalle de un evento publicado ([CU-20](#cu-20--publicar-evento)) que aún no ha ocurrido.

**Flujo principal:**

1. El usuario visualiza un evento de su interés.
2. Selecciona la opción para confirmar asistencia ("Asistiré").
3. El sistema registra al usuario en la lista de asistentes del evento.
4. El sistema habilita la visualización de los demás asistentes confirmados para este usuario.
5. El sistema ofrece la opción de exportar o agregar el evento a un calendario personal.

**Flujos alternativos / excepciones:**

- 2a. El usuario cambia de opinión y retira su confirmación: el sistema lo elimina de la lista de asistentes y actualiza la vista.

**Postcondiciones:** El usuario queda registrado como asistente, aportando métricas al creador del evento y facilitando la interacción con otros asistentes.

**Prioridad:** Alta

---

## CU-16 — Administrar roles en espacios de proyectos

**Actor(es):** Administrador de proyecto

**Descripción:** Permite gestionar los niveles de acceso de los miembros dentro de un espacio de proyecto mediante roles granulares (visualizador, editor, administrador). Estos niveles de acceso son distintos de los perfiles requeridos definidos al crear el proyecto ([CU-11](#cu-11--gestionar-espacio-de-proyectos)).

**Precondiciones:** El usuario debe tener el rol de administrador o creador dentro de un espacio de proyecto existente.

**Flujo principal:**

1. El administrador accede a la configuración de miembros del proyecto.
2. Selecciona a un miembro actual del proyecto.
3. Modifica su nivel de acceso asignando un rol específico (visualizador, editor, administrador).
4. El sistema valida y aplica los nuevos permisos granulares al usuario seleccionado.
5. El sistema notifica al miembro sobre el cambio en su rol.

**Flujos alternativos / excepciones:**

- 3a. El administrador intenta removerse a sí mismo como administrador sin asignar a otro en su reemplazo: el sistema bloquea la acción para evitar que el proyecto quede sin gestión.

**Postcondiciones:** Los permisos del proyecto quedan actualizados, limitando o expandiendo las acciones del miembro afectado según su nuevo rol.

**Prioridad:** Media

---

## CU-20 — Publicar evento

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario publicar un evento académico o de otra índole para que la comunidad lo conozca y confirme su asistencia.

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El usuario selecciona la opción de publicar evento.
2. Ingresa título, descripción, fecha y hora, lugar y categoría.
3. El sistema valida que todos los datos requeridos estén completos y que la fecha sea futura.
4. El sistema publica el evento en el apartado de eventos ([CU-21](#cu-21--visualizar-eventos)).

**Flujos alternativos / excepciones:**

- 3a. Falta algún dato requerido o la fecha ya pasó: el sistema indica la información pendiente y no publica el evento.
- 3b. El evento no cumple las políticas de uso: el sistema lo rechaza e informa el motivo.

**Postcondiciones:** El evento queda publicado y disponible para que otros usuarios confirmen asistencia ([CU-15](#cu-15--confirmar-asistencia-a-eventos-rsvp)). Puede ser moderado según [CU-25](../contenido/casos-de-uso.md#cu-25--moderar-contenido-publicaciones-y-eventos).

**Prioridad:** Media

---

## CU-21 — Visualizar eventos

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario consultar los eventos publicados en la plataforma para identificar los de su interés.

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El usuario accede al apartado de eventos.
2. El sistema muestra los próximos eventos ordenados por fecha, con título, fecha, categoría, lugar y descripción.
3. El usuario puede filtrar por categoría.
4. El usuario selecciona un evento para ver su detalle y, si lo desea, confirmar asistencia ([CU-15](#cu-15--confirmar-asistencia-a-eventos-rsvp)).

**Flujos alternativos / excepciones:**

- 2a. No existen eventos publicados o que coincidan con el filtro: el sistema informa que no hay eventos disponibles.

**Postcondiciones:** El usuario conoce los eventos disponibles en la plataforma.

**Prioridad:** Media

---

## CU-22 — Publicar oportunidades y gestionar postulaciones

**Actor(es):** Responsable de oportunidad

**Descripción:** Permite a un usuario publicar oportunidades de investigación, proyectos o voluntariado, revisar las postulaciones recibidas y actualizar su estado.

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El responsable crea una oportunidad indicando título, descripción, categoría (investigación, proyecto o voluntariado), requisitos, número de cupos y fecha de cierre.
2. El sistema valida y publica la oportunidad en la sección de oportunidades ([CU-12](#cu-12--explorar-oportunidades)).
3. El responsable consulta el listado de postulaciones recibidas y el perfil de cada postulante.
4. El responsable cambia el estado de cada postulación a "En revisión", "Aceptada" o "Rechazada", con retroalimentación opcional.
5. El sistema notifica al postulante cada cambio de estado ([CU-14](#cu-14--gestionar-estado-de-postulaciones)).

**Flujos alternativos / excepciones:**

- 1a. Faltan datos requeridos: el sistema indica los campos pendientes y no publica la oportunidad.
- 4a. Se alcanza la fecha de cierre o se completan los cupos: el sistema cierra la oportunidad a nuevas postulaciones.
- 4b. El responsable cierra la oportunidad manualmente: el sistema deja de aceptar postulaciones y notifica a los postulantes pendientes.

**Postcondiciones:** La oportunidad queda publicada y las postulaciones reflejan su estado actualizado para el postulante.

**Prioridad:** Alta
