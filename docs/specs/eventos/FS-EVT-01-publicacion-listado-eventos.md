# FS-EVT-01 — Publicación y listado de eventos

| Campo | Valor |
|---|---|
| **Módulo** | Eventos (EVT) |
| **Sprint** | Sprint 07 |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-20](../../requisitos/CasosDeUso.md#cu-20--publicar-evento), [CU-21](../../requisitos/CasosDeUso.md#cu-21--visualizar-eventos) |
| **Historias** | [HU-15](../../requisitos/HistoriasDeUsuario.md#hu-15), [HU-16](../../requisitos/HistoriasDeUsuario.md#hu-16) |
| **Última actualización** | 2026-10-06 |

## 1. Objetivo

Reunir en un solo lugar los eventos de la comunidad universitaria (charlas, talleres, ferias, actividades culturales y deportivas) para que cualquiera pueda darlos a conocer y cada usuario encuentre los que le interesan.

## 2. Alcance

**Incluye:**

- Crear, editar, cancelar y eliminar eventos presenciales, virtuales o híbridos.
- Cupo opcional y foto de portada.
- Apartado de eventos con filtros y vista de eventos pasados.
- Reportar eventos, usando el mecanismo de [FS-ADM-03](../administracion/FS-ADM-03-moderacion-contenido.md).

**No incluye:**

- Confirmar asistencia, lista de asistentes y calendario ([FS-EVT-02](./FS-EVT-02-confirmacion-asistencia.md)).
- Eventos que se repiten (por ejemplo, cada semana).
- Venta de entradas o inscripción con pago.
- Mostrar los eventos dentro del feed.

## 3. Actores

| Actor | Participación |
|---|---|
| Usuario autenticado (organizador) | Publica y gestiona sus eventos. |
| Usuario autenticado | Consulta y reporta eventos. |

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Cualquier usuario autenticado puede publicar eventos y se convierte en su organizador. |
| RN-02 | Todo evento usa una categoría activa de tipo "Eventos" ([FS-ADM-01](../administracion/FS-ADM-01-gestion-categorias.md)). |
| RN-03 | La fecha de inicio debe ser al menos 1 hora después del momento de publicación y como máximo 1 año después. La hora de fin debe ser posterior a la de inicio y el evento no puede durar más de 7 días. |
| RN-04 | Según la modalidad: los eventos presenciales exigen lugar; los virtuales exigen enlace; los híbridos exigen ambos. |
| RN-05 | El enlace de un evento virtual o híbrido solo lo ven el organizador y quienes confirmaron asistencia ([FS-EVT-02](./FS-EVT-02-confirmacion-asistencia.md)). |
| RN-06 | Los eventos son visibles para todos los usuarios autenticados, sin importar la privacidad del perfil del organizador. |
| RN-07 | **Edición:** el organizador puede editar el evento hasta que comience. Si cambia la fecha, la hora, el lugar o el enlace, se notifica a los asistentes confirmados. El cupo no puede quedar por debajo del número de confirmados. |
| RN-08 | **Cancelación:** el organizador puede cancelar un evento que no ha comenzado, indicando el motivo. El evento sigue visible marcado como "Cancelado" y se notifica a los asistentes confirmados. |
| RN-09 | Un evento sin asistentes confirmados puede eliminarse por completo. Con asistentes solo puede cancelarse. |
| RN-10 | Un evento pasa a "Finalizado" automáticamente al llegar su hora de fin. |
| RN-11 | Los eventos se pueden reportar con las mismas reglas que las publicaciones ([FS-ADM-03](../administracion/FS-ADM-03-moderacion-contenido.md)). Si un administrador retira un evento, se notifica al organizador y a los asistentes confirmados. |
| RN-12 | El apartado de eventos muestra por defecto los próximos eventos no cancelados, del más cercano al más lejano. |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El sistema debe ofrecer la sección "Eventos" en el menú principal, con el botón "Publicar evento". | Alta |
| RF-02 | El sistema debe validar y publicar el evento con los datos de la sección 6. | Alta |
| RF-03 | El apartado debe mostrar cada evento como tarjeta: portada, fecha y hora, título, modalidad y lugar, categoría y número de asistentes confirmados. | Alta |
| RF-04 | El apartado debe permitir filtrar por categoría, modalidad y periodo (Hoy, Esta semana, Este mes, Todas las fechas) y buscar por texto. | Alta |
| RF-05 | El apartado debe tener las pestañas "Próximos", "Mis eventos" (los que organizo y a los que asistiré) y "Pasados". | Media |
| RF-06 | El detalle del evento debe mostrar todos sus datos, el organizador y, si aplica, la etiqueta "Cancelado" con el motivo o "Finalizado". | Alta |
| RF-07 | El sistema debe permitir al organizador editar, cancelar y eliminar según RN-07 a RN-09. | Alta |
| RF-08 | El menú "…" del evento debe ofrecer "Reportar" a los demás usuarios (RN-11). | Media |
| RF-09 | El perfil del organizador debe mostrar una pestaña "Eventos" con los que ha publicado. | Baja |

## 6. Datos y validaciones

| Campo | Tipo | Obligatorio | Validación |
|---|---|---|---|
| Título | Texto | Sí | 5 a 120 caracteres. |
| Descripción | Texto largo | Sí | 20 a 3.000 caracteres. |
| Categoría | Lista | Sí | Categorías activas de tipo "Eventos". |
| Fecha y hora de inicio | Fecha y hora | Sí | RN-03. Hora de Colombia. |
| Fecha y hora de fin | Fecha y hora | Sí | RN-03. |
| Modalidad | Opción | Sí | Presencial, Virtual o Híbrida. |
| Lugar | Texto | Según RN-04 | 3 a 150 caracteres (por ejemplo, "Edificio Ernestina Lozano, auditorio"). |
| Enlace | URL | Según RN-04 | URL válida que empiece por `https://`. |
| Cupo | Número | No | De 1 a 5.000. Vacío significa sin límite. |
| Portada | Imagen | No | JPG, PNG o WebP de máximo 5 MB. Si no hay, se usa una imagen por categoría. |

## 7. Estados

| Estado | Entra cuando | Sale hacia |
|---|---|---|
| Programado | Se publica | **Cancelado** (RN-08), **Finalizado** (RN-10) o **Retirado** (RN-11) |
| Cancelado | El organizador lo cancela | Estado final |
| Finalizado | Llega la hora de fin | Estado final |
| Retirado | Un administrador lo retira | Estado final |

## 8. Flujo de pantallas

1. **Eventos** → "Publicar evento" → **Formulario** → "Publicar" → **Detalle del evento**.
2. **Eventos** → filtra o busca → selecciona una tarjeta → **Detalle**.
3. **Detalle** (como organizador) → "Editar" o "Cancelar evento".

## 9. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Evento publicado | "Tu evento está publicado. Compártelo con tu red." |
| MSG-02 | Fecha inválida | "El evento debe empezar al menos 1 hora después de ahora y como máximo en un año, y terminar después de empezar." |
| MSG-03 | Falta lugar o enlace | "Para un evento {modalidad} debes indicar {lugar / enlace / lugar y enlace}." |
| MSG-04 | Confirmar cancelación | "Avisaremos a las {n} personas que confirmaron asistencia. ¿Cancelar el evento?" |
| MSG-05 | Cupo menor que confirmados | "Ya hay {n} personas confirmadas; el cupo no puede ser menor." |
| MSG-06 | Sin eventos | "No hay eventos próximos con estos filtros." |
| MSG-07 | Enlace oculto | "Confirma tu asistencia para ver el enlace del evento." |

## 10. Criterios de aceptación

```gherkin
Escenario: Publicar un evento presencial
  Dado que soy un usuario autenticado
  Cuando publico un evento presencial con título, descripción, categoría, fecha futura, hora de fin y lugar
  Entonces veo el mensaje MSG-01
  Y el evento aparece en "Próximos" para todos los usuarios

Escenario: Evento virtual sin enlace
  Dado que estoy creando un evento virtual
  Cuando intento publicarlo sin enlace
  Entonces veo el mensaje MSG-03

Escenario: Enlace solo para asistentes
  Dado que hay un evento virtual al que no he confirmado asistencia
  Cuando abro su detalle
  Entonces no veo el enlace y veo el mensaje MSG-07

Escenario: Cambio de lugar
  Dado que organizo un evento con 20 asistentes confirmados
  Cuando cambio el lugar
  Entonces los 20 asistentes reciben una notificación del cambio

Escenario: Cancelar un evento
  Dado que organizo un evento con asistentes confirmados
  Cuando lo cancelo con un motivo
  Entonces el evento se muestra como "Cancelado" con el motivo
  Y los asistentes reciben una notificación
  Y desaparece de "Próximos"

Escenario: Filtrar por periodo
  Dado que hay un evento hoy y otro el próximo mes
  Cuando filtro por "Esta semana"
  Entonces solo veo el evento de hoy

Escenario: Evento finalizado
  Dado que la hora de fin de un evento ya pasó
  Entonces el evento aparece en "Pasados" como "Finalizado"
  Y ya no se puede editar ni cancelar

Escenario: Reportar un evento
  Dado que veo un evento inapropiado
  Cuando lo reporto
  Entonces aparece en la cola de moderación con las mismas reglas que las publicaciones
```

## 11. Dependencias

- [FS-ADM-01](../administracion/FS-ADM-01-gestion-categorias.md): categorías de tipo "Eventos".
- [FS-ADM-03](../administracion/FS-ADM-03-moderacion-contenido.md): mecanismo de reportes.
- [FS-EVT-02](./FS-EVT-02-confirmacion-asistencia.md): asistentes confirmados.
- [FS-NOT-01](../notificaciones/FS-NOT-01-centro-notificaciones.md): notificaciones de cambios y cancelaciones.
- Almacenamiento de archivos para la portada.

## 12. Preguntas abiertas

- [ ] ¿Se quiere mostrar los eventos próximos también en el feed, o basta con la sección Eventos?
- [ ] ¿Se necesita un calendario de espacios de la universidad para validar que el lugar esté disponible, o el organizador es responsable de reservarlo?

## 13. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Gamero | Creación |
