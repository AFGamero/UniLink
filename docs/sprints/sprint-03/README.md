# Sprint 03 — Red de conexiones

| Campo | Valor |
|---|---|
| **Fechas** | Por definir (2 semanas) |
| **Estado** | Planificado |
| **Objetivo** | El usuario arma su red desde el primer ingreso: recibe sugerencias de personas complementarias, envía y responde solicitudes de conexión, y se entera de todo en su centro de notificaciones. |

## Specs comprometidos

| Spec | Responsable | Estado |
|---|---|---|
| [FS-NOT-01 — Centro de notificaciones](../../specs/notificaciones/FS-NOT-01-centro-notificaciones.md) | Por asignar | Borrador |
| [FS-RED-01 — Solicitudes de conexión](../../specs/red/FS-RED-01-solicitudes-conexion.md) | Por asignar | Borrador |
| [FS-RED-02 — Onboarding y sugerencias](../../specs/red/FS-RED-02-onboarding-sugerencias.md) | Por asignar | Borrador |

**Orden sugerido:** FS-NOT-01 primero, porque es el mecanismo común que usan los demás módulos para notificar. Después FS-RED-01, y por último FS-RED-02, que usa las solicitudes.

## Tareas técnicas

- [ ] Decidir cómo se actualiza el indicador de notificaciones (consultas periódicas o tiempo real), pensando en la mensajería del Sprint 5.
- [ ] Implementar el mecanismo común de notificaciones con su catálogo de tipos.
- [ ] Modelar solicitudes y conexiones garantizando una sola relación entre dos usuarios, incluso con solicitudes simultáneas.
- [ ] Programar las tareas diarias: vencimiento de solicitudes (90 días) y limpieza de notificaciones (90 días).
- [ ] Agregar el botón de conexión a las tarjetas de búsqueda y al perfil (FS-PRF-02 y FS-PRF-01).

## Riesgos

| Riesgo | Mitigación |
|---|---|
| Al lanzar habrá pocos usuarios y el onboarding mostrará pocas o ninguna sugerencia. | Cargar perfiles de mentores del CIDTI y hacer el lanzamiento por cohortes (por ejemplo, un programa a la vez). |
| Dos solicitudes simultáneas crean dos relaciones entre los mismos usuarios. | Restricción única en la base de datos y prueba automatizada del caso. |
| Abuso del envío masivo de solicitudes. | Límite diario de 30 (FS-RED-01, RN-05). |

## Revisión

_Completar al cierre del sprint._

## Retrospectiva

| Qué funcionó | Qué mejorar | Acción |
|---|---|---|
| | | |
