# Casos de uso — Red

_MVP — Red Profesional Universitaria — Universidad del Magdalena_
_Centro de Interés de Desarrollo Tecnológico e Innovación (CIDTI)_

Casos de uso del módulo Red (RED). Los actores se definen en el [mapa de módulos](../README.md#actores).

## Índice

- [CU-05 — Buscar y visualizar perfiles](#cu-05--buscar-y-visualizar-perfiles)
- [CU-06 — Enviar solicitud de conexión](#cu-06--enviar-solicitud-de-conexión)
- [CU-07 — Responder solicitud de conexión](#cu-07--responder-solicitud-de-conexión)
- [CU-13 — Sugerir conexiones iniciales (Onboarding)](#cu-13--sugerir-conexiones-iniciales-onboarding)

---

## CU-05 — Buscar y visualizar perfiles

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario descubrir otros miembros de la comunidad universitaria mediante búsqueda por nombre, habilidades, intereses o programa académico.

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El usuario accede al buscador de perfiles.
2. Ingresa un término de búsqueda o aplica filtros (habilidades, intereses, programa académico, facultad, "Puede aportar" o "Necesita").
3. El sistema procesa la búsqueda y muestra los perfiles coincidentes con una vista previa de información básica.
4. El usuario selecciona un perfil para visualizar su detalle completo.

**Flujos alternativos / excepciones:**

- 3a. No se encuentran perfiles coincidentes: el sistema informa que no hay resultados y sugiere ajustar los filtros.
- 4a. El perfil seleccionado es visible solo para conexiones y el usuario no está conectado con su dueño: el sistema muestra únicamente la información básica y la opción de enviar solicitud de conexión ([CU-06](#cu-06--enviar-solicitud-de-conexión)).

**Postcondiciones:** El usuario obtiene un listado de perfiles relevantes según su búsqueda y puede consultar el detalle de cualquiera de ellos, respetando su configuración de privacidad.

**Prioridad:** Alta

---

## CU-06 — Enviar solicitud de conexión

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario establecer una conexión profesional con otro miembro de la plataforma enviando una solicitud que el destinatario puede aceptar o rechazar.

**Precondiciones:** El usuario debe estar autenticado y visualizar el perfil de otro usuario con el cual aún no tiene una conexión ni solicitud pendiente.

**Flujo principal:**

1. El usuario visualiza el perfil de otro miembro.
2. Selecciona la opción de enviar solicitud de conexión.
3. El sistema registra la solicitud como pendiente y notifica al destinatario.

**Flujos alternativos / excepciones:**

- 1a. Ya existe una solicitud pendiente o una conexión establecida entre ambos usuarios: el sistema no permite enviar una nueva solicitud y muestra el estado actual.
- 3a. El usuario cancela una solicitud que envió y sigue pendiente: el sistema la elimina sin notificar al destinatario.

**Postcondiciones:** La solicitud queda registrada como pendiente hasta que el destinatario responda.

**Prioridad:** Alta

---

## CU-07 — Responder solicitud de conexión

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario responder a las solicitudes de conexión recibidas, aceptándolas o rechazándolas según su interés.

**Precondiciones:** El usuario debe tener al menos una solicitud de conexión pendiente por revisar.

**Flujo principal:**

1. El usuario recibe una notificación de nueva solicitud de conexión.
2. Revisa el perfil del solicitante.
3. Acepta o rechaza la solicitud.
4. El sistema actualiza la red de conexiones de ambos usuarios y notifica al solicitante el resultado.

**Flujos alternativos / excepciones:**

- 3a. El usuario rechaza la solicitud: el sistema descarta la solicitud sin notificar el motivo al solicitante.
- 4a. Más adelante, cualquiera de los dos usuarios elimina la conexión: el sistema los desconecta sin notificar al otro.

**Postcondiciones:** La solicitud queda resuelta (aceptada o rechazada) y, en caso de aceptación, ambos usuarios quedan conectados.

**Prioridad:** Alta

---

## CU-13 — Sugerir conexiones iniciales (Onboarding)

**Actor(es):** Usuario autenticado (nuevo)

**Descripción:** Permite presentar sugerencias de conexiones inmediatas (compañeros de facultad o espacios de proyectos) durante el primer ingreso del usuario a la plataforma, con el fin de prevenir el "feed vacío" (cold start) y asegurar que visualice contenido relevante.

**Precondiciones:** El usuario acaba de guardar su perfil por primera vez ([CU-04](../usuarios/casos-de-uso.md#cu-04--creareditar-perfil-profesional)) o lo hizo antes y cerró el onboarding sin terminarlo ni omitirlo.

**Flujo principal:**

1. El sistema detecta que el onboarding del usuario está pendiente.
2. El sistema analiza la unidad académica, la facultad, las categorías de interés ([CU-18](../usuarios/casos-de-uso.md#cu-18--seleccionar-preferencias-de-contenido)) y los campos "Puedo aportar" y "Necesito" del usuario ([CU-04](../usuarios/casos-de-uso.md#cu-04--creareditar-perfil-profesional)) para generar sugerencias.
3. El sistema muestra una pantalla de *onboarding* con una lista de perfiles sugeridos y, desde el Sprint 8, espacios de proyectos relevantes ([P-50](../../preguntas-abiertas.md)). Cuando una sugerencia se debe a perfiles complementarios, el sistema indica el motivo (por ejemplo, "Puede aportar diseño gráfico, que tú necesitas").
4. El usuario selecciona a los compañeros o proyectos con los que desea conectar de forma inmediata.
5. El sistema envía las solicitudes de conexión (y de unión a proyectos) automáticamente y redirige al usuario a su panel principal (feed).

**Flujos alternativos / excepciones:**

- 4a. El usuario decide omitir el paso de sugerencias: el sistema lo redirige al panel principal sin enviar solicitudes y llena el feed con publicaciones recientes de las categorías de su interés o, si no eligió ninguna, con las publicaciones más recientes de su facultad.

**Postcondiciones:** El usuario inicia su experiencia en la plataforma con un feed con contenido, alimentado por sus conexiones, solicitudes o preferencias.

**Prioridad:** Media
