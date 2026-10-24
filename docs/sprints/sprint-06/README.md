# Sprint 06 — Oportunidades

| Campo | Valor |
|---|---|
| **Fechas** | Por definir (2 semanas) |
| **Estado** | Planificado |
| **Objetivo** | Los responsables publican oportunidades de investigación, proyectos y voluntariado; los usuarios encuentran las que encajan con su perfil, se postulan y siguen el estado de cada postulación hasta la decisión final. |

## Specs comprometidos

| Spec | Responsable | Estado |
|---|---|---|
| [FS-COL-01 — Publicación de oportunidades](../../modulos/colaboracion/specs/FS-COL-01-publicacion-oportunidades.md) | Por asignar | Borrador |
| [FS-COL-02 — Postulaciones](../../modulos/colaboracion/specs/FS-COL-02-postulaciones.md) | Por asignar | Borrador |

**Orden sugerido:** primero publicar oportunidades y el cálculo de afinidad (FS-COL-01), después explorar y postularse (FS-COL-02), y al final el panel del responsable y los cambios de estado, que conectan ambos lados.

## Tareas técnicas

- [ ] Cargar las categorías semilla de tipo "Oportunidades".
- [ ] Implementar el cálculo de afinidad reutilizando las etiquetas normalizadas de FS-USR-06.
- [ ] Modelar los estados de la postulación con sus transiciones permitidas y el historial de cambios.
- [ ] Programar el cierre automático por fecha.
- [ ] Extender la regla de mensajería para habilitar la conversación tras una postulación aceptada.
- [ ] Hacer que el responsable vea el perfil completo de sus postulantes aunque sea privado.

## Riesgos

| Riesgo | Mitigación |
|---|---|
| Al lanzar habrá pocas oportunidades y la sección se verá vacía. | Coordinar con el CIDTI y grupos de investigación para publicar oportunidades reales antes de abrir la sección. |
| Afinidad engañosa si las oportunidades no declaran habilidades requeridas. | Recomendar en el formulario agregar habilidades y no mostrar afinidad cuando no hay ninguna. |
| Cambios de estado concurrentes (dos acciones sobre la misma postulación). | Validar la transición en el servidor contra el estado actual antes de aplicarla. |

## Revisión

_Completar al cierre del sprint._

## Retrospectiva

| Qué funcionó | Qué mejorar | Acción |
|---|---|---|
| | | |
