# Historias de usuario — Colaboración

_MVP — Red Profesional Universitaria — Universidad del Magdalena_
_Centro de Interés de Desarrollo Tecnológico e Innovación (CIDTI)_

Historias de usuario del módulo Colaboración (COL), en formato "Como / quiero / para", derivadas de sus [casos de uso](./casos-de-uso.md).

## Índice

- [HU-11 — Como usuario autenticado, quiero crear o unirme a espacios de proyectos para colaborar con otros miembros](#hu-11)
- [HU-12 — Como usuario autenticado, quiero explorar y postularme a oportunidades de investigación, proyectos y voluntariado](#hu-12)
- [HU-15 — Como usuario autenticado, quiero publicar un evento con su fecha, categoría, lugar, título y descripción](#hu-15)
- [HU-16 — Como usuario autenticado, quiero visualizar un apartado con los eventos publicados en la plataforma](#hu-16)
- [HU-25 — Como usuario autenticado, quiero visualizar un panel con el estado de mis postulaciones](#hu-25)
- [HU-26 — Como usuario autenticado, quiero confirmar mi asistencia a un evento (RSVP), ver quién más asistirá y agregarlo a mi calendario personal](#hu-26)
- [HU-27 — Como creador o administrador de un proyecto, quiero asignar roles granulares (visualizador, editor o administrador) a los miembros de mi equipo](#hu-27)
- [HU-29 — Como responsable de una oportunidad, quiero publicarla y gestionar el estado de las postulaciones que recibo](#hu-29)

---

## HU-11

> **Como** usuario autenticado,
> **quiero** crear o unirme a espacios de proyectos para colaborar con otros miembros,
> **para** trabajar en conjunto en iniciativas académicas o profesionales.

**Caso de uso relacionado:** [CU-11](./casos-de-uso.md#cu-11--gestionar-espacio-de-proyectos)

**Criterios de aceptación:**

- Dado que creo un proyecto, entonces puedo definir nombre, descripción, perfiles requeridos, número máximo de integrantes, tareas y objetivos, y quedo como administrador del proyecto.
- Dado que solicito unirme a un proyecto existente, entonces los administradores del proyecto reciben mi solicitud y la aprueban o rechazan.
- Dado que el proyecto ya alcanzó el número máximo de integrantes, entonces el sistema no permite mi solicitud e informa el motivo.
- Dado que soy miembro de un proyecto, entonces puedo abandonarlo, salvo que sea su único administrador.

**Prioridad:** Media

---

## HU-12

> **Como** usuario autenticado,
> **quiero** explorar y postularme a oportunidades de investigación, proyectos y voluntariado,
> **para** acceder a experiencias académicas y profesionales relevantes para mi formación.

**Caso de uso relacionado:** [CU-12](./casos-de-uso.md#cu-12--explorar-oportunidades)

**Criterios de aceptación:**

- Dado que accedo a la sección de oportunidades, entonces puedo explorarlas filtrando por categoría.
- Dado que selecciono una oportunidad abierta, entonces puedo ver su detalle y postularme directamente.
- Dado que ya estoy postulado a una oportunidad, entonces el sistema no permite una nueva postulación y muestra el estado actual.
- Dado que la oportunidad está cerrada, entonces el sistema no permite postularme e informa el motivo.
- Dado que me postulo exitosamente, entonces mi postulación queda en estado "Enviada" y el sistema notifica al responsable de la oportunidad.

**Prioridad:** Media

---

## HU-15

> **Como** usuario autenticado,
> **quiero** publicar un evento con su fecha, categoría, lugar, título y descripción,
> **para** informar a los usuarios sobre eventos académicos o de cualquier índole y permitirles conocerlos y asistir.

**Caso de uso relacionado:** [CU-20](./casos-de-uso.md#cu-20--publicar-evento)

**Criterios de aceptación:**

- Dado que soy un usuario autenticado, entonces puedo acceder a la opción para publicar un evento.
- Dado que estoy creando un evento, entonces el sistema me permite ingresar la fecha, categoría, lugar, título y descripción.
- Dado que ingreso todos los datos requeridos correctamente, entonces el sistema valida y publica el evento.
- Dado que el evento es publicado correctamente, entonces los demás usuarios pueden visualizar su información para conocerlo y asistir.
- Dado que no ingreso alguno de los datos requeridos o la fecha ya pasó, entonces el sistema me indica la información pendiente y no permite publicar el evento.

**Prioridad:** Media

---

## HU-16

> **Como** usuario autenticado,
> **quiero** visualizar un apartado con los eventos publicados en la plataforma,
> **para** conocer los eventos disponibles, identificar aquellos que sean de mi interés y poder asistir.

**Caso de uso relacionado:** [CU-21](./casos-de-uso.md#cu-21--visualizar-eventos)

**Criterios de aceptación:**

- Dado que soy un usuario autenticado, entonces puedo acceder al apartado de eventos.
- Dado que accedo al apartado de eventos, entonces el sistema muestra los próximos eventos ordenados por fecha, con título, fecha, categoría, lugar y descripción.
- Dado que visualizo un evento, entonces puedo consultar su información para determinar si es de mi interés.
- Dado que no existen eventos publicados, entonces el sistema me informa que no hay eventos disponibles.

**Prioridad:** Media

---

## HU-25

> **Como** usuario autenticado,
> **quiero** visualizar un panel con el estado de mis postulaciones ("Enviada", "En revisión", "Aceptada" o "Rechazada"),
> **para** hacer seguimiento a las oportunidades a las que he aplicado.

**Caso de uso relacionado:** [CU-14](./casos-de-uso.md#cu-14--gestionar-estado-de-postulaciones)

**Criterios de aceptación:**

- Dado que he aplicado a oportunidades en la plataforma, cuando accedo al panel de postulaciones, entonces veo una lista de todas mis solicitudes.
- Dado que visualizo una postulación, entonces el sistema me indica si su estado es "Enviada", "En revisión", "Aceptada", "Rechazada" o "Retirada".
- Dado que el responsable de la oportunidad cambia el estado de mi postulación, entonces el sistema me notifica y actualiza el panel con el estado más reciente.
- Dado que una postulación está "Enviada" o "En revisión", entonces puedo retirarla.
- Dado que no he realizado ninguna postulación, entonces el sistema me muestra un mensaje invitándome a explorar oportunidades, con un enlace a esa sección.

**Prioridad:** Alta

---

## HU-26

> **Como** usuario autenticado,
> **quiero** confirmar mi asistencia a un evento (RSVP), ver quién más asistirá y agregarlo a mi calendario personal,
> **para** interactuar con la comunidad y programar mi participación.

**Caso de uso relacionado:** [CU-15](./casos-de-uso.md#cu-15--confirmar-asistencia-a-eventos-rsvp)

**Criterios de aceptación:**

- Dado que visualizo la información de un evento que aún no ha ocurrido, entonces el sistema me muestra un botón para confirmar mi asistencia de forma explícita.
- Dado que confirmo mi asistencia, entonces el sistema me permite visualizar la lista de otros miembros que también asistirán.
- Dado que he confirmado mi asistencia, entonces el sistema me ofrece una opción para exportar o añadir el evento a mi calendario personal.
- Dado que decido cancelar mi asistencia, entonces el sistema me permite revertir la acción y oculta mi perfil de la lista de asistentes.

**Prioridad:** Alta

---

## HU-27

> **Como** creador o administrador de un proyecto,
> **quiero** asignar roles granulares (como visualizador, editor o administrador) a los miembros de mi equipo,
> **para** controlar los permisos y las acciones que cada integrante puede realizar dentro del espacio colaborativo.

**Caso de uso relacionado:** [CU-16](./casos-de-uso.md#cu-16--administrar-roles-en-espacios-de-proyectos)

**Criterios de aceptación:**

- Dado que soy el administrador del proyecto, cuando accedo a la sección de miembros, entonces el sistema me permite visualizar el rol actual de cada integrante.
- Dado que selecciono a un miembro, entonces puedo cambiar su nivel de acceso escogiendo entre los roles de visualizador, editor o administrador.
- Dado que asigno un rol granular a un miembro, entonces el sistema aplica restricciones o permisos de edición inmediatamente basados en ese rol y notifica al miembro.
- Dado que intento dejar el proyecto sin ningún administrador asignado, entonces el sistema me muestra un error y me impide realizar el cambio.

**Prioridad:** Media

---

## HU-29

> **Como** responsable de una oportunidad,
> **quiero** publicarla y gestionar el estado de las postulaciones que recibo,
> **para** seleccionar a los candidatos adecuados y mantenerlos informados.

**Caso de uso relacionado:** [CU-22](./casos-de-uso.md#cu-22--publicar-oportunidades-y-gestionar-postulaciones)

**Criterios de aceptación:**

- Dado que soy un usuario autenticado, cuando creo una oportunidad con título, descripción, categoría, requisitos, cupos y fecha de cierre, entonces el sistema la publica en la sección de oportunidades.
- Dado que mi oportunidad recibe postulaciones, entonces puedo ver el listado de postulantes y consultar sus perfiles.
- Dado que reviso una postulación, cuando cambio su estado a "En revisión", "Aceptada" o "Rechazada", entonces el sistema notifica al postulante y actualiza su panel.
- Dado que se alcanza la fecha de cierre o se completan los cupos, entonces el sistema cierra la oportunidad a nuevas postulaciones.

**Prioridad:** Alta
