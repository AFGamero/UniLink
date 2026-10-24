# Casos de uso — Contenido

_MVP — Red Profesional Universitaria — Universidad del Magdalena_
_Centro de Interés de Desarrollo Tecnológico e Innovación (CIDTI)_

Casos de uso del módulo Contenido (CNT). Los actores se definen en el [mapa de módulos](../README.md#actores).

## Índice

- [CU-08 — Publicar contenido](#cu-08--publicar-contenido)
- [CU-09 — Visualizar publicaciones](#cu-09--visualizar-publicaciones)
- [CU-25 — Moderar contenido (publicaciones y eventos)](#cu-25--moderar-contenido-publicaciones-y-eventos)

---

## CU-08 — Publicar contenido

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario compartir publicaciones académicas o profesionales, como proyectos, logros, convocatorias externas o artículos, con la comunidad.

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El usuario selecciona la opción de crear publicación.
2. Ingresa el contenido: título, descripción, categoría y, opcionalmente, archivos adjuntos.
3. El sistema valida el contenido ingresado.
4. El sistema publica el contenido y lo muestra en el feed de sus conexiones y de los usuarios interesados en esa categoría ([CU-18](../usuarios/casos-de-uso.md#cu-18--seleccionar-preferencias-de-contenido)).

**Flujos alternativos / excepciones:**

- 3a. El contenido no cumple con las políticas de uso de la plataforma: el sistema rechaza la publicación e informa el motivo.

**Postcondiciones:** La publicación queda visible en el feed de las conexiones del usuario y de los usuarios interesados en su categoría. Puede ser reportada y moderada según [CU-25](#cu-25--moderar-contenido-publicaciones-y-eventos).

**Prioridad:** Media

---

## CU-09 — Visualizar publicaciones

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario consultar las publicaciones de su red de conexiones y de las categorías de su interés, filtradas por categoría o relevancia.

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El usuario accede al feed de publicaciones.
2. Navega por las publicaciones o aplica filtros por categoría.
3. El sistema muestra las publicaciones correspondientes con opciones de interacción (comentar, reaccionar, compartir).

**Flujos alternativos / excepciones:**

- 2a. No existen publicaciones que coincidan con el filtro aplicado: el sistema muestra un mensaje indicándolo.

**Postcondiciones:** El usuario visualiza el listado de publicaciones solicitado.

**Prioridad:** Media

---

## CU-25 — Moderar contenido (publicaciones y eventos)

**Actor(es):** Administrador de la plataforma; Usuario autenticado (reporta contenido)

**Descripción:** Permite al administrador revisar y retirar publicaciones (incluidos sus comentarios), eventos y, con el mismo mecanismo, perfiles, oportunidades y proyectos que incumplan las políticas de uso, incluidos los reportados por los usuarios.

**Precondiciones:** El administrador debe estar autenticado con rol de administrador de la plataforma.

**Flujo principal:**

1. Un usuario reporta una publicación o evento indicando el motivo, o el administrador lo identifica directamente.
2. El administrador accede al panel de moderación, donde ve el contenido reportado y el resto de publicaciones y eventos.
3. El administrador revisa el contenido y decide retirarlo o mantenerlo.
4. Si lo retira, el sistema deja de mostrarlo a los usuarios, notifica a su autor con el motivo y registra la acción del administrador.

**Flujos alternativos / excepciones:**

- 3a. El administrador decide mantener el contenido: el sistema descarta los reportes asociados.

**Postcondiciones:** El contenido inapropiado deja de estar disponible y la acción queda registrada.

**Prioridad:** Alta
