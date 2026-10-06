# Sprint 02 — Perfil y descubrimiento

| Campo | Valor |
|---|---|
| **Fechas** | Por definir (2 semanas) |
| **Estado** | Planificado |
| **Objetivo** | El usuario construye su perfil profesional, declara qué puede aportar y qué necesita, encuentra a otros miembros, controla su privacidad y descarga su hoja de vida. |

## Specs comprometidos

| Spec | Responsable | Estado |
|---|---|---|
| [FS-PRF-01 — Perfil profesional](../../specs/perfil/FS-PRF-01-perfil-profesional.md) | Por asignar | Borrador |
| [FS-PRF-02 — Búsqueda de perfiles](../../specs/perfil/FS-PRF-02-busqueda-perfiles.md) | Por asignar | Borrador |
| [FS-CTA-05 — Configuración de cuenta y privacidad](../../specs/cuenta/FS-CTA-05-configuracion-cuenta.md) | Por asignar | Borrador |
| [FS-PRF-03 — Hoja de vida en PDF](../../specs/perfil/FS-PRF-03-hoja-de-vida-pdf.md) | Por asignar | Borrador |

**Orden sugerido:** FS-PRF-01 primero, porque los otros tres dependen de los datos del perfil.

## Tareas técnicas

- [ ] Configurar el almacenamiento de imágenes para las fotos de perfil.
- [ ] Diseñar el modelo de etiquetas compartido (habilidades, intereses, "Puedo aportar", "Necesito") con normalización sin tildes ni mayúsculas.
- [ ] Implementar la consulta de complementariedad (FS-PRF-01, RF-06) con pruebas de rendimiento.
- [ ] Cargar el catálogo de facultades y programas.
- [ ] Elegir la librería de generación de PDF y validar que soporte tildes y "ñ".
- [ ] Programar la tarea diaria que elimina las cuentas con 30 días de desactivación.

## Riesgos

| Riesgo | Mitigación |
|---|---|
| La consulta de complementariedad es lenta con muchos usuarios. | Indexar las etiquetas normalizadas y limitar el cálculo a cuentas activas y visibles. |
| Las etiquetas se llenan de duplicados o variantes. | Autocompletado obligatorio con etiquetas existentes; revisar a fin de sprint si se necesita fusión por administrador. |
| La eliminación de cuentas tiene implicaciones legales no resueltas. | Llevar las preguntas abiertas de FS-CTA-05 a la planificación; si no se resuelven, implementar solo la desactivación y dejar la eliminación definitiva para el siguiente sprint. |

## Revisión

_Completar al cierre del sprint._

## Retrospectiva

| Qué funcionó | Qué mejorar | Acción |
|---|---|---|
| | | |
