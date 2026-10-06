# Sprint 04 — Contenido y categorías

| Campo | Valor |
|---|---|
| **Fechas** | Por definir (2 semanas) |
| **Estado** | Planificado |
| **Objetivo** | La comunidad comparte proyectos, logros y artículos, y cada usuario ve en su feed contenido de su red y de sus intereses desde el primer día. El administrador gestiona las categorías sin ayuda del equipo técnico. |

## Specs comprometidos

| Spec | Responsable | Estado |
|---|---|---|
| [FS-ADM-01 — Gestión de categorías](../../specs/administracion/FS-ADM-01-gestion-categorias.md) | Por asignar | Borrador |
| [FS-CNT-01 — Publicaciones y feed](../../specs/contenido/FS-CNT-01-publicaciones-feed.md) | Por asignar | Borrador |

**Orden sugerido:** FS-ADM-01 es pequeño y crea la base del panel de administración; puede hacerse en paralelo con FS-CNT-01, que es el más grande del sprint. Dentro de FS-CNT-01: primero crear y ver publicaciones, después el feed con sus reglas de respaldo, y al final las interacciones.

## Tareas técnicas

- [ ] Crear el rol de administrador de la plataforma y el control de acceso al panel.
- [ ] Implementar el registro de acciones de administración (lo reutilizarán FS-ADM-02 y FS-ADM-03).
- [ ] Reutilizar el almacenamiento de archivos del Sprint 2 para imágenes y PDF de las publicaciones.
- [ ] Implementar la lista configurable de palabras prohibidas.
- [ ] Optimizar la consulta del feed (conexiones + categorías de interés + respaldo), con índices por fecha y categoría.
- [ ] Reemplazar "Personas que podrían interesarte" por el feed como página principal.

## Riesgos

| Riesgo | Mitigación |
|---|---|
| FS-CNT-01 es grande para un solo sprint. | Si el sprint se aprieta, mover el orden "Relevantes" y la lista de reacciones (RF-06) al Sprint 5; son de prioridad media. |
| El feed es lento al crecer el contenido. | Limitar a 30 días, paginar de a 10 y medir el tiempo de respuesta en la revisión del sprint. |
| Contenido inapropiado antes de que exista la moderación (Sprint 5). | Filtro de palabras prohibidas (RN-03) y lanzamiento controlado por cohortes. |

## Revisión

_Completar al cierre del sprint._

## Retrospectiva

| Qué funcionó | Qué mejorar | Acción |
|---|---|---|
| | | |
