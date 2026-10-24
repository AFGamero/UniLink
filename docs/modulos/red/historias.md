# Historias de usuario — Red

_MVP — Red Profesional Universitaria — Universidad del Magdalena_
_Centro de Interés de Desarrollo Tecnológico e Innovación (CIDTI)_

Historias de usuario del módulo Red (RED), en formato "Como / quiero / para", derivadas de sus [casos de uso](./casos-de-uso.md).

## Índice

- [HU-05 — Como usuario autenticado, quiero buscar y visualizar perfiles de otros miembros por nombre, habilidades, intereses o programa académico](#hu-05)
- [HU-06 — Como usuario autenticado, quiero enviar una solicitud de conexión a otro miembro de la plataforma](#hu-06)
- [HU-07 — Como usuario autenticado, quiero aceptar o rechazar las solicitudes de conexión que recibo](#hu-07)
- [HU-24 — Como usuario nuevo, quiero recibir sugerencias de conexión (compañeros de facultad o espacios de proyectos) durante mi primer ingreso](#hu-24)

---

## HU-05

> **Como** usuario autenticado,
> **quiero** buscar y visualizar perfiles de otros miembros por nombre, habilidades, intereses o programa académico,
> **para** descubrir personas afines dentro de la comunidad universitaria.

**Caso de uso relacionado:** [CU-05](./casos-de-uso.md#cu-05--buscar-y-visualizar-perfiles)

**Criterios de aceptación:**

- Dado que ingreso un término de búsqueda o aplico filtros, entonces el sistema muestra los perfiles coincidentes con una vista previa.
- Dado que busco a alguien que pueda ayudarme, cuando filtro por "Puede aportar" con una etiqueta (por ejemplo, "diseño gráfico"), entonces el sistema muestra los perfiles que declararon esa etiqueta.
- Dado que no existen perfiles coincidentes, entonces el sistema me informa que no hay resultados y sugiere ajustar los filtros.
- Dado que selecciono un perfil de los resultados, entonces puedo visualizar su detalle completo, salvo que sea visible solo para conexiones y no esté conectado con su dueño.

**Prioridad:** Alta

---

## HU-06

> **Como** usuario autenticado,
> **quiero** enviar una solicitud de conexión a otro miembro de la plataforma,
> **para** establecer una conexión profesional con esa persona.

**Caso de uso relacionado:** [CU-06](./casos-de-uso.md#cu-06--enviar-solicitud-de-conexión)

**Criterios de aceptación:**

- Dado que visualizo el perfil de otro usuario sin conexión ni solicitud previa, entonces puedo enviarle una solicitud de conexión.
- Dado que envío la solicitud, entonces el sistema la registra como pendiente y notifica al destinatario.
- Dado que ya existe una solicitud pendiente o una conexión establecida con ese usuario, entonces el sistema no me permite enviar una nueva solicitud y me muestra el estado actual.
- Dado que envié una solicitud que sigue pendiente, entonces puedo cancelarla sin que el destinatario sea notificado.

**Prioridad:** Alta

---

## HU-07

> **Como** usuario autenticado,
> **quiero** aceptar o rechazar las solicitudes de conexión que recibo,
> **para** decidir con quién establezco una conexión profesional.

**Caso de uso relacionado:** [CU-07](./casos-de-uso.md#cu-07--responder-solicitud-de-conexión)

**Criterios de aceptación:**

- Dado que recibo una solicitud de conexión, entonces soy notificado y puedo revisar el perfil del solicitante.
- Dado que acepto la solicitud, entonces el sistema actualiza la red de conexiones de ambos usuarios y notifica al solicitante.
- Dado que rechazo la solicitud, entonces el sistema la descarta sin notificar el motivo al solicitante.
- Dado que estoy conectado con alguien, entonces puedo eliminar esa conexión sin que la otra persona sea notificada.

**Prioridad:** Alta

---

## HU-24

> **Como** usuario nuevo,
> **quiero** recibir sugerencias de conexión (compañeros de facultad o espacios de proyectos) durante mi primer ingreso,
> **para** no tener mi feed vacío y asegurar que veo contenido relevante desde el inicio.

**Caso de uso relacionado:** [CU-13](./casos-de-uso.md#cu-13--sugerir-conexiones-iniciales-onboarding)

**Criterios de aceptación:**

- Dado que es mi primer inicio de sesión tras el registro, entonces el sistema me muestra un paso adicional de *onboarding* sugiriendo conexiones.
- Dado que el sistema me sugiere perfiles, entonces estas sugerencias se basan en compañeros de mi misma facultad, mis preferencias de contenido, espacios de proyectos relacionados o perfiles complementarios (lo que yo necesito y otro puede aportar, o al revés).
- Dado que una sugerencia se debe a perfiles complementarios, entonces el sistema me muestra el motivo (por ejemplo, "Puede aportar diseño gráfico, que tú necesitas").
- Dado que selecciono a varios usuarios sugeridos, cuando finalizo el *onboarding*, entonces el sistema envía las solicitudes de conexión de forma automática y me redirige a mi feed.
- Dado que decido omitir este paso, entonces el sistema me redirige al feed sin enviar solicitudes y me muestra publicaciones de mis categorías de interés o de mi facultad.

**Prioridad:** Media
