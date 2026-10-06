# Sprint 07 — Eventos

| Campo | Valor |
|---|---|
| **Fechas** | Por definir (2 semanas) |
| **Estado** | Planificado |
| **Objetivo** | La comunidad publica sus eventos en un solo lugar, y los usuarios encuentran los que les interesan, confirman su asistencia, ven quiénes más irán y los agregan a su calendario. |

## Specs comprometidos

| Spec | Responsable | Estado |
|---|---|---|
| [FS-EVT-01 — Publicación y listado de eventos](../../specs/eventos/FS-EVT-01-publicacion-listado-eventos.md) | Por asignar | Borrador |
| [FS-EVT-02 — Confirmación de asistencia (RSVP)](../../specs/eventos/FS-EVT-02-confirmacion-asistencia.md) | Por asignar | Borrador |

**Orden sugerido:** primero FS-EVT-01 (publicar, listar y detalle), después FS-EVT-02. El reporte de eventos reutiliza el mecanismo del Sprint 5 y debería ser rápido.

## Tareas técnicas

- [ ] Guardar las fechas con zona horaria y mostrarlas en hora de Colombia.
- [ ] Programar las tareas: pasar eventos a "Finalizado" y enviar recordatorios 24 horas antes.
- [ ] Controlar el cupo de forma segura cuando varias personas confirman al mismo tiempo.
- [ ] Generar archivos `.ics` y enlaces de Google Calendar.
- [ ] Registrar el tipo "evento" en el mecanismo de reportes de FS-ADM-03.
- [ ] Definir imágenes de portada por defecto para cada categoría de eventos.

## Riesgos

| Riesgo | Mitigación |
|---|---|
| Se confirma más gente que el cupo por confirmaciones simultáneas. | Validar el cupo en la misma operación que registra la confirmación, con prueba automatizada. |
| Errores de zona horaria en el calendario y los recordatorios. | Pruebas con eventos que cruzan la medianoche y con usuarios en otra zona horaria. |
| Pocos eventos al lanzar. | Invitar a bienestar universitario, el CIDTI y los grupos estudiantiles a publicar su agenda. |

## Revisión

_Completar al cierre del sprint._

## Retrospectiva

| Qué funcionó | Qué mejorar | Acción |
|---|---|---|
| | | |
