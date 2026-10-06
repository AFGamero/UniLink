# Sprint 05 — Mensajería y administración

| Campo | Valor |
|---|---|
| **Fechas** | Por definir (2 semanas) |
| **Estado** | Planificado |
| **Objetivo** | Las conexiones conversan en privado en tiempo real, y el administrador puede moderar el contenido reportado y actuar sobre las cuentas que incumplen las normas. |

## Specs comprometidos

| Spec | Responsable | Estado |
|---|---|---|
| [FS-MSG-01 — Mensajería privada](../../specs/mensajeria/FS-MSG-01-mensajeria-privada.md) | Por asignar | Borrador |
| [FS-ADM-03 — Moderación de contenido](../../specs/administracion/FS-ADM-03-moderacion-contenido.md) | Por asignar | Borrador |
| [FS-ADM-02 — Gestión de cuentas de usuario](../../specs/administracion/FS-ADM-02-gestion-cuentas.md) | Por asignar | Borrador |

**Orden sugerido:** FS-MSG-01 y la parte de administración pueden avanzar en paralelo con personas distintas. En administración, primero FS-ADM-03 (reportes y cola) y después FS-ADM-02, porque el detalle de la cuenta muestra el historial de moderación.

## Tareas técnicas

- [ ] Montar la infraestructura de tiempo real para la mensajería y reutilizarla en el indicador de notificaciones.
- [ ] Garantizar una sola conversación entre dos usuarios (restricción única).
- [ ] Implementar el mecanismo común de reportes, preparado para agregar eventos en el Sprint 7.
- [ ] Ocultar el contenido de cuentas suspendidas o desactivadas en todas las consultas (perfil, búsqueda, feed, sugerencias).
- [ ] Programar la reactivación automática al terminar una suspensión.
- [ ] Programar el correo de mensajes sin leer (1 hora, máximo uno por conversación al día).

## Riesgos

| Riesgo | Mitigación |
|---|---|
| Las [normas de la comunidad](../../normas-comunidad.md) siguen en borrador. | Conseguir la aprobación del equipo y de la oficina jurídica antes de la planificación; FS-ADM-03 no pasa a **Aprobado** sin ellas. |
| El tiempo real es la parte técnica más compleja del MVP. | Hacer una prueba de concepto al inicio del sprint; si falla, usar consultas periódicas cada 5 segundos en la conversación abierta como plan B. |
| Ocultar el contenido de cuentas suspendidas exige cambiar consultas de varios módulos. | Centralizar el filtro de "cuenta visible" en un único lugar del código. |

## Revisión

_Completar al cierre del sprint._

## Retrospectiva

| Qué funcionó | Qué mejorar | Acción |
|---|---|---|
| | | |
