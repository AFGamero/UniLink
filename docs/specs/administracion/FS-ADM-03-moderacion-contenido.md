# FS-ADM-03 — Moderación de contenido

| Campo | Valor |
|---|---|
| **Módulo** | Administración (ADM) |
| **Sprint** | Sprint 05 |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-25](../../requisitos/CasosDeUso.md#cu-25--moderar-contenido-publicaciones-y-eventos) |
| **Historias** | [HU-18](../../requisitos/HistoriasDeUsuario.md#hu-18), [HU-19](../../requisitos/HistoriasDeUsuario.md#hu-19) |
| **Última actualización** | 2026-10-06 |

## 1. Objetivo

Mantener un espacio seguro y respetuoso: los usuarios reportan el contenido que incumple las normas, y el administrador lo revisa y decide si lo retira, con un registro de cada decisión.

## 2. Alcance

**Incluye:**

- Reportar publicaciones y comentarios.
- Ocultamiento automático del contenido con muchos reportes.
- Cola de moderación para el administrador.
- Retirar contenido o descartar reportes, con aviso al autor y al denunciante.
- Mecanismo común de reportes que reutilizarán los demás tipos de contenido.

**No incluye:**

- Reportar eventos: se agrega en el Sprint 7 con FS-EVT-01, reutilizando este mecanismo. HU-19 queda completa en ese sprint.
- Reportar perfiles, mensajes privados, oportunidades o servicios.
- Moderación automática con inteligencia artificial.

## 3. Actores

| Actor | Participación |
|---|---|
| Usuario autenticado | Reporta contenido. |
| Administrador de la plataforma | Revisa reportes y retira contenido. |
| Autor del contenido | Recibe el aviso si su contenido es retirado. |

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Se pueden reportar publicaciones y comentarios de otros usuarios. No se puede reportar el propio contenido. |
| RN-02 | Un usuario solo puede reportar una vez el mismo elemento. |
| RN-03 | Motivos de reporte: Spam, Acoso o lenguaje ofensivo, Información falsa, Contenido inapropiado, Otro. Con "Otro", el usuario debe escribir una descripción. |
| RN-04 | Cuando un elemento recibe reportes de 5 usuarios distintos, se oculta automáticamente a todos menos a su autor, hasta que un administrador lo revise. |
| RN-05 | La cola de moderación muestra los elementos con reportes pendientes, ordenados primero por ocultos automáticamente y después por número de reportes. |
| RN-06 | **Retirar:** el elemento deja de verse para todos. Su autor lo ve en su perfil marcado como "Retirado por moderación" junto con el motivo, y recibe una notificación y un correo. |
| RN-07 | **Mantener:** los reportes pendientes se descartan y el elemento vuelve a verse si estaba oculto. Los reportes futuros vuelven a la cola, pero el elemento ya no se oculta automáticamente. |
| RN-08 | El administrador también puede retirar contenido sin reportes, desde el listado de publicaciones. |
| RN-09 | Retirar exige seleccionar la norma incumplida y escribir un comentario de al menos 20 caracteres. |
| RN-10 | El autor nunca sabe quién lo reportó. Los denunciantes reciben una notificación cuando su reporte se revisa, sin detalles de la decisión. |
| RN-11 | Cada decisión queda registrada con el administrador, la fecha, la decisión y el motivo (registro de [FS-ADM-01](./FS-ADM-01-gestion-categorias.md)). El contenido retirado cuenta en el historial del autor ([FS-ADM-02](./FS-ADM-02-gestion-cuentas.md)). |
| RN-12 | Retirar una publicación retira también sus comentarios. |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El sistema debe agregar la opción "Reportar" al menú "…" de publicaciones y comentarios ajenos, con el formulario de motivos (RN-03). | Alta |
| RF-02 | El sistema debe aplicar RN-02 y RN-04 automáticamente. | Alta |
| RF-03 | El panel de administración debe incluir la sección "Moderación" con la cola (RN-05) y un indicador del número de elementos pendientes. | Alta |
| RF-04 | Cada elemento de la cola debe mostrar el contenido completo, su autor, la cantidad de reportes, los motivos agrupados y los comentarios de "Otro". | Alta |
| RF-05 | El sistema debe permitir "Retirar" (RN-06, RN-09) o "Mantener" (RN-07) cada elemento. | Alta |
| RF-06 | La sección Moderación debe tener una pestaña "Todas las publicaciones" con búsqueda por texto y autor, para aplicar RN-08. | Media |
| RF-07 | La sección Moderación debe tener una pestaña "Historial" con las decisiones tomadas. | Media |
| RF-08 | El mecanismo de reportes debe admitir nuevos tipos de contenido sin cambiar la cola ni las reglas (eventos en el Sprint 7). | Alta |

## 6. Datos y validaciones

| Campo | Tipo | Obligatorio | Validación |
|---|---|---|---|
| Motivo del reporte | Opción | Sí | RN-03. |
| Descripción | Texto | Sí, si el motivo es "Otro" | 10 a 500 caracteres. |
| Norma incumplida (al retirar) | Opción | Sí | Lista de normas de la comunidad. |
| Comentario del administrador | Texto | Sí, al retirar | 20 a 500 caracteres. |

## 7. Estados

| Estado del elemento | Entra cuando | Sale hacia |
|---|---|---|
| Visible | Se publica | **Oculto por reportes** (RN-04), **Retirado** (RN-06, RN-08) |
| Oculto por reportes | 5 reportes distintos | **Visible** si se mantiene; **Retirado** si se retira |
| Retirado | Decisión del administrador | Estado final |

## 8. Flujo de pantallas

1. **Feed** → menú "…" de una publicación → "Reportar" → elige motivo → "Enviar".
2. **Panel** → "Moderación" → **Cola** → selecciona un elemento → "Retirar" (norma y comentario) o "Mantener".

## 9. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Reporte enviado | "Gracias por tu reporte. Lo revisaremos pronto." |
| MSG-02 | Reporte repetido | "Ya reportaste este contenido." |
| MSG-03 | Aviso al autor | "Retiramos tu publicación \"{título}\" porque incumple la norma \"{norma}\": {comentario}." |
| MSG-04 | Aviso al denunciante | "Revisamos el contenido que reportaste. Gracias por ayudarnos a cuidar la comunidad." |
| MSG-05 | Contenido retirado, visto por su autor | "Retirado por moderación: {norma}." |

## 10. Criterios de aceptación

```gherkin
Escenario: Reportar una publicación
  Dado que veo una publicación de Pedro
  Cuando la reporto con el motivo "Spam"
  Entonces veo el mensaje MSG-01
  Y la publicación aparece en la cola de moderación

Escenario: Reporte repetido
  Dado que ya reporté una publicación
  Cuando intento reportarla de nuevo
  Entonces veo el mensaje MSG-02

Escenario: Ocultamiento automático
  Dado que una publicación tiene reportes de 4 usuarios distintos
  Cuando un quinto usuario la reporta
  Entonces deja de verse para todos menos para su autor
  Y aparece primera en la cola de moderación

Escenario: Retirar contenido
  Dado que reviso una publicación reportada
  Cuando la retiro indicando la norma y un comentario
  Entonces deja de verse para todos
  Y su autor recibe el aviso MSG-03
  Y quienes la reportaron reciben el aviso MSG-04
  Y la decisión queda en el historial

Escenario: Mantener contenido
  Dado que una publicación fue ocultada por reportes
  Cuando decido mantenerla
  Entonces vuelve a verse para todos
  Y si recibe 5 reportes nuevos, no se vuelve a ocultar automáticamente

Escenario: Anonimato del denunciante
  Dado que reporté una publicación de Pedro y fue retirada
  Entonces Pedro no puede saber que fui yo

Escenario: Retirar sin reportes
  Dado que encuentro una publicación inapropiada sin reportes
  Cuando la retiro desde "Todas las publicaciones"
  Entonces se aplican los mismos efectos que al retirar una publicación reportada
```

## 11. Dependencias

- [FS-CNT-01](../contenido/FS-CNT-01-publicaciones-feed.md): publicaciones y comentarios.
- [FS-ADM-01](./FS-ADM-01-gestion-categorias.md): panel y registro de acciones.
- [FS-ADM-02](./FS-ADM-02-gestion-cuentas.md): historial de moderación en el detalle de la cuenta.
- [FS-NOT-01](../notificaciones/FS-NOT-01-centro-notificaciones.md): avisos al autor y al denunciante.
- Documento de **normas de la comunidad** publicado y aprobado (ver preguntas abiertas).

## 12. Preguntas abiertas

- [ ] **Bloqueante:** UniLink necesita un documento de normas de la comunidad que los usuarios acepten y que los administradores citen al retirar contenido. ¿Quién lo redacta y aprueba?
- [ ] ¿El umbral de 5 reportes para ocultar automáticamente es adecuado para el tamaño de la comunidad?

## 13. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Gamero | Creación |
