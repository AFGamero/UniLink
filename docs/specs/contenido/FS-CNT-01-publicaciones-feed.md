# FS-CNT-01 — Publicaciones y feed

| Campo | Valor |
|---|---|
| **Módulo** | Contenido (CNT) |
| **Sprint** | Sprint 04 |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-08](../../requisitos/CasosDeUso.md#cu-08--publicar-contenido), [CU-09](../../requisitos/CasosDeUso.md#cu-09--visualizar-publicaciones) |
| **Historias** | [HU-08](../../requisitos/HistoriasDeUsuario.md#hu-08), [HU-09](../../requisitos/HistoriasDeUsuario.md#hu-09) |
| **Última actualización** | 2026-10-06 |

## 1. Objetivo

Permitir que la comunidad comparta proyectos, logros y artículos, y que cada usuario vea en su feed el contenido de su red y de sus temas de interés, incluso si todavía no tiene conexiones.

## 2. Alcance

**Incluye:**

- Crear, editar y eliminar publicaciones propias, con imágenes o un PDF adjunto.
- Feed con publicaciones de conexiones, categorías de interés y contenido de respaldo para usuarios nuevos.
- Filtro por categoría y orden "Recientes" o "Relevantes".
- Interacciones: reacción "Me gusta", comentarios y compartir enlace.
- Página individual de cada publicación.

**No incluye:**

- Reportar publicaciones y moderación (FS-ADM-03, Sprint 5).
- Compartir una publicación por mensaje privado (FS-MSG-01, Sprint 5).
- Volver a publicar contenido de otros en el propio perfil, menciones (@) y etiquetas (#).
- Encuestas o videos.

## 3. Actores

| Actor | Participación |
|---|---|
| Usuario autenticado (autor) | Crea, edita y elimina sus publicaciones; modera los comentarios de sus publicaciones. |
| Usuario autenticado (lector) | Ve el feed, reacciona, comenta y comparte. |

## 4. Reglas de negocio

**Publicaciones**

| ID | Regla |
|---|---|
| RN-01 | Toda publicación tiene título, texto y una categoría activa de tipo "Publicaciones" ([FS-ADM-01](../administracion/FS-ADM-01-gestion-categorias.md)). |
| RN-02 | Adjuntos: hasta 4 imágenes (JPG, PNG o WebP, máximo 5 MB cada una) **o** un PDF (máximo 10 MB). No se pueden combinar imágenes y PDF. |
| RN-03 | Antes de publicar, el sistema revisa el título y el texto contra una lista de palabras prohibidas configurable. Si hay coincidencias, rechaza la publicación e indica el motivo. |
| RN-04 | El autor puede editar el título, el texto y la categoría en cualquier momento; la publicación muestra "Editada". Los adjuntos no se pueden cambiar después de publicar. |
| RN-05 | Al eliminar una publicación se eliminan también sus comentarios y reacciones. |
| RN-06 | **Visibilidad:** si el perfil del autor es "Comunidad", la publicación la ve cualquier usuario autenticado. Si es "Solo mis conexiones", solo la ven sus conexiones. |

**Feed**

| ID | Regla |
|---|---|
| RN-07 | El feed muestra, de los últimos 30 días: publicaciones propias, de las conexiones y de las categorías de interés del usuario ([FS-CTA-04](../cuenta/FS-CTA-04-preferencias-contenido.md)), respetando RN-06. |
| RN-08 | **Contenido de respaldo:** si RN-07 da menos de 10 publicaciones, se completa con publicaciones recientes de la facultad del usuario y, si aún faltan, con las más recientes de toda la plataforma. Estas se marcan como "Sugerida para ti". |
| RN-09 | **Orden "Recientes"** (por defecto): de la más nueva a la más antigua. |
| RN-10 | **Orden "Relevantes":** puntaje = (reacciones + comentarios × 2) + 10 si el autor es conexión + 5 si la categoría es de interés, dividido entre (horas desde la publicación + 2). Así el contenido nuevo y con actividad sube, y el viejo baja. |
| RN-11 | El feed carga 10 publicaciones a la vez a medida que el usuario se desplaza. |

**Interacciones**

| ID | Regla |
|---|---|
| RN-12 | Cada usuario puede dar un solo "Me gusta" por publicación y puede quitarlo. |
| RN-13 | Los comentarios tienen máximo 1.000 caracteres, no admiten respuestas anidadas y pasan por la misma revisión de RN-03. |
| RN-14 | El autor de un comentario puede eliminarlo. El autor de la publicación puede eliminar cualquier comentario de su publicación. |
| RN-15 | "Compartir" copia el enlace de la publicación. El enlace solo funciona para usuarios autenticados que tengan permiso de verla según RN-06. |
| RN-16 | Se notifica al autor de la publicación cuando alguien comenta ([FS-NOT-01](../notificaciones/FS-NOT-01-centro-notificaciones.md)). Las reacciones no generan notificación, para no saturar al usuario. |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El sistema debe ofrecer un cuadro "Comparte algo con la comunidad" en la parte superior del feed que abre el formulario de publicación. | Alta |
| RF-02 | El sistema debe validar y publicar según RN-01 a RN-03, y mostrar la publicación de inmediato al inicio del feed del autor. | Alta |
| RF-03 | El sistema debe mostrar cada publicación con: foto, nombre y titular del autor, fecha relativa ("hace 2 h"), categoría, título, texto (recortado a 5 líneas con "Ver más"), adjuntos, número de "Me gusta" y de comentarios, y los botones de interacción. | Alta |
| RF-04 | El sistema debe ofrecer el filtro por categoría y el selector "Recientes / Relevantes" en el feed. | Media |
| RF-05 | El sistema debe permitir editar y eliminar publicaciones propias (RN-04, RN-05), pidiendo confirmación para eliminar. | Alta |
| RF-06 | El sistema debe permitir dar o quitar "Me gusta" y mostrar la lista de quiénes reaccionaron. | Media |
| RF-07 | El sistema debe permitir comentar y mostrar los 2 comentarios más recientes bajo la publicación, con "Ver todos los comentarios". | Alta |
| RF-08 | Cada publicación debe tener una página propia accesible por enlace (RN-15). | Media |
| RF-09 | El perfil de cada usuario debe mostrar una pestaña "Publicaciones" con las suyas, respetando RN-06. | Media |
| RF-10 | Los PDF deben poder abrirse o descargarse; las imágenes deben verse ampliadas al pulsarlas. | Media |

## 6. Datos y validaciones

| Campo | Tipo | Obligatorio | Validación |
|---|---|---|---|
| Título | Texto | Sí | 5 a 120 caracteres. |
| Texto | Texto largo | Sí | 10 a 3.000 caracteres. Los enlaces se convierten en vínculos. |
| Categoría | Lista | Sí | Categorías activas de tipo "Publicaciones". |
| Imágenes | Archivos | No | RN-02. Cada imagen admite una descripción opcional de hasta 250 caracteres para lectores de pantalla ([RNF-ACC-05](../../requisitos/RequisitosNoFuncionales.md#6-accesibilidad)). |
| PDF | Archivo | No | RN-02. |
| Comentario | Texto | Sí, para comentar | 1 a 1.000 caracteres; RN-13. |

## 7. Estados

| Estado de la publicación | Entra cuando | Sale hacia |
|---|---|---|
| Publicada | Pasa la validación | **Eliminada** por su autor; **Retirada** por un administrador (FS-ADM-03) |
| Eliminada | El autor la elimina | Estado final |

## 8. Flujo de pantallas

1. **Feed** → "Comparte algo con la comunidad" → **Formulario** → "Publicar" → **Feed** con la publicación arriba.
2. **Feed** → "Me gusta" o "Comentar" en una publicación → se actualiza en el mismo lugar.
3. **Feed** → menú "…" de una publicación propia → "Editar" o "Eliminar".
4. **Enlace compartido** → **Página de la publicación**.

## 9. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Publicación creada | "Tu publicación ya está en el feed." |
| MSG-02 | Contenido rechazado (RN-03) | "Tu publicación contiene términos que no cumplen las normas de la comunidad. Revisa el texto e inténtalo de nuevo." |
| MSG-03 | Adjunto inválido | "Puedes adjuntar hasta 4 imágenes (JPG, PNG o WebP, máximo 5 MB) o un PDF de máximo 10 MB." |
| MSG-04 | Confirmar eliminación | "¿Eliminar esta publicación? También se eliminarán sus comentarios." |
| MSG-05 | Enlace copiado | "Enlace copiado." |
| MSG-06 | Sin permiso o eliminada | "Esta publicación no está disponible." |
| MSG-07 | Filtro sin resultados | "No hay publicaciones recientes en esta categoría." |
| MSG-08 | Etiqueta de respaldo | "Sugerida para ti" |

## 10. Criterios de aceptación

```gherkin
Escenario: Publicar con imágenes
  Dado que estoy en el feed
  Cuando creo una publicación con título, texto, categoría "Logros académicos" y 2 imágenes
  Entonces veo el mensaje MSG-01
  Y la publicación aparece primera en mi feed

Escenario: Mezclar imágenes y PDF
  Dado que adjunté una imagen
  Cuando intento adjuntar un PDF
  Entonces veo el mensaje MSG-03

Escenario: Palabras prohibidas
  Dado que el texto de mi publicación contiene una palabra de la lista prohibida
  Cuando intento publicar
  Entonces veo el mensaje MSG-02 y la publicación no se crea

Escenario: Feed de un usuario con red
  Dado que estoy conectado con Luis y me interesa la categoría "Tecnología"
  Cuando abro el feed
  Entonces veo las publicaciones de Luis y las de "Tecnología" de los últimos 30 días

Escenario: Feed de un usuario nuevo
  Dado que no tengo conexiones ni categorías de interés
  Cuando abro el feed
  Entonces veo publicaciones recientes de mi facultad marcadas como "Sugerida para ti"

Escenario: Publicación de un perfil privado
  Dado que el perfil de Luis es "Solo mis conexiones" y no estoy conectado con él
  Entonces no veo sus publicaciones en mi feed ni en su perfil
  Y si abro el enlace de una de ellas veo el mensaje MSG-06

Escenario: Comentar y notificar
  Dado que veo una publicación de Luis
  Cuando escribo un comentario
  Entonces el comentario aparece bajo la publicación
  Y Luis recibe una notificación

Escenario: Moderar comentarios propios
  Dado que Pedro comentó en mi publicación
  Cuando elimino su comentario
  Entonces el comentario desaparece

Escenario: Editar publicación
  Dado que tengo una publicación
  Cuando cambio su texto
  Entonces la publicación muestra el nuevo texto y la etiqueta "Editada"

Escenario: Orden por relevancia
  Dado que hay dos publicaciones de la misma hora
  Y una tiene 10 comentarios y la otra ninguno
  Cuando elijo "Relevantes"
  Entonces la publicación con comentarios aparece primero
```

## 11. Dependencias

- [FS-ADM-01](../administracion/FS-ADM-01-gestion-categorias.md): categorías de tipo "Publicaciones".
- [FS-RED-01](../red/FS-RED-01-solicitudes-conexion.md): conexiones del usuario.
- [FS-CTA-04](../cuenta/FS-CTA-04-preferencias-contenido.md) y [FS-CTA-05](../cuenta/FS-CTA-05-configuracion-cuenta.md): intereses y privacidad.
- [FS-NOT-01](../notificaciones/FS-NOT-01-centro-notificaciones.md): notificación de comentarios.
- Almacenamiento de archivos para imágenes y PDF (el mismo de la foto de perfil).

## 12. Preguntas abiertas

- [ ] ¿Quién define y mantiene la lista de palabras prohibidas?
- [ ] La categoría "Oportunidades" de publicaciones puede confundirse con el módulo de oportunidades (Sprint 6), que sí permite postularse. ¿Se renombra (por ejemplo, "Convocatorias externas") o se elimina cuando exista ese módulo?
- [ ] ¿Basta con una sola reacción ("Me gusta") o se quieren varias (por ejemplo, "Me gusta", "Interesante", "Felicitaciones")?

## 13. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Gamero | Creación |
