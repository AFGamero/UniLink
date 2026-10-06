# Sprint 08 — Proyectos

| Campo | Valor |
|---|---|
| **Fechas** | Por definir (2 semanas) |
| **Estado** | Planificado |
| **Objetivo** | Los equipos crean espacios de proyecto, reclutan a personas con las habilidades que necesitan, organizan sus tareas con roles y permisos claros, y al terminar el proyecto queda en el portafolio de cada miembro. |

## Specs comprometidos

| Spec | Responsable | Estado |
|---|---|---|
| [FS-PRY-01 — Espacios de proyectos](../../specs/proyectos/FS-PRY-01-espacios-proyectos.md) | Por asignar | Borrador |
| [FS-PRY-02 — Roles en proyectos](../../specs/proyectos/FS-PRY-02-roles-proyectos.md) | Por asignar | Borrador |

**Orden sugerido:** diseñar primero la matriz de permisos (FS-PRY-02), porque todas las acciones de FS-PRY-01 la consultan. Después: crear y explorar proyectos, membresía, tablero de tareas y, al final, el portafolio en el perfil y la extensión del onboarding.

## Tareas técnicas

- [ ] Implementar la verificación de permisos por rol en el servidor, en un único lugar reutilizable.
- [ ] Reutilizar el cálculo de afinidad del Sprint 6 para proyectos.
- [ ] Tablero de tareas con arrastrar y soltar, usable también en celular.
- [ ] Registro de actividad del proyecto.
- [ ] Vencimiento de invitaciones a los 14 días.
- [ ] Extender el onboarding (FS-RED-02) con sugerencias de proyectos.

## Riesgos

| Riesgo | Mitigación |
|---|---|
| El tablero de tareas crece hasta parecer una herramienta de gestión completa. | Limitarse a lo definido en FS-PRY-01 (tres columnas, responsable, fecha límite). Todo lo demás va a preguntas abiertas. |
| Errores de permisos que dejan editar a quien no debe. | Pruebas automatizadas de cada fila de la matriz de permisos, incluidas peticiones directas al servidor. |
| Sprint 8 es grande. | Si se aprieta, pasar las invitaciones (RF-07), el portafolio (RF-09) y la extensión del onboarding (RF-10) a una iteración posterior al MVP; son de prioridad media. |

## Revisión

_Completar al cierre del sprint._

## Retrospectiva

| Qué funcionó | Qué mejorar | Acción |
|---|---|---|
| | | |
