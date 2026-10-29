# Módulo Colaboración (COL)

## Propósito

Donde la comunidad trabaja junta: **oportunidades** con postulaciones, **eventos** con confirmación de asistencia y **espacios de proyectos** con miembros, roles y tareas.

**No es responsabilidad de este módulo:** las conversaciones (Comunicación), la moderación (Contenido, a través de `Reportable`) ni las categorías (Plataforma).

## Documentos

| Documento | Contenido |
|---|---|
| [Casos de uso](./casos-de-uso.md) | CU-11, CU-12, CU-14, CU-15, CU-16, CU-20, CU-21, CU-22 |
| [Historias de usuario](./historias.md) | HU-11, HU-12, HU-15, HU-16, HU-25, HU-26, HU-27, HU-29 |
| [FS-COL-01](./specs/FS-COL-01-publicacion-oportunidades.md) | Publicación de oportunidades |
| [FS-COL-02](./specs/FS-COL-02-postulaciones.md) | Postulaciones |
| [FS-COL-03](./specs/FS-COL-03-publicacion-listado-eventos.md) | Publicación y listado de eventos |
| [FS-COL-04](./specs/FS-COL-04-confirmacion-asistencia.md) | Confirmación de asistencia (RSVP) |
| [FS-COL-05](./specs/FS-COL-05-espacios-proyectos.md) | Espacios de proyectos |
| [FS-COL-06](./specs/FS-COL-06-roles-proyectos.md) | Roles en proyectos |

## El patrón común: una publicación con responsable y cupo

Oportunidades, eventos y proyectos son la misma idea con distintos nombres. Se describe una vez aquí y cada spec la concreta.

| Elemento del patrón | Oportunidad | Evento | Proyecto |
|---|---|---|---|
| Quién la crea | Responsable de oportunidad | Organizador | Creador del proyecto (Administrador de proyecto) |
| Quién participa | Postulante | Asistente | Miembro del proyecto |
| Cómo se entra | Postulación que el responsable acepta | Confirmación directa | Solicitud aprobada o invitación aceptada |
| Cupo | Cupos (1 a 100), obligatorio | Cupo opcional (1 a 5.000) | Máximo de integrantes (2 a 50) |
| Se deja de recibir participantes | Fecha de cierre o cupos llenos | Inicio del evento o cupo lleno | Cierre del reclutamiento o cupo lleno |
| Fin | Cancelada (con motivo) | Cancelado, Finalizado | Finalizado (portafolio) |
| Afinidad | Habilidades requeridas | — | Habilidades buscadas |
| Categorías de interés | — | Priorizan "Próximos" | Priorizan "Explorar" |
| Moderable (`Reportable`) | Sí (Sprint 6) | Sí (Sprint 7) | Sí (Sprint 8) |

**Reglas comunes a los tres:**

1. **Cupo atómico:** nunca hay más participantes que cupo, aun con peticiones simultáneas (RNF-CON-01, [EC-04](../../srs/Especificacion_Requisitos.md#34-escenarios-de-atributos-de-calidad)).
2. **Afinidad:** porcentaje de las habilidades pedidas que el usuario tiene entre sus habilidades o su "Puedo aportar"; la calcula Usuarios por su interfaz pública.
3. **Textos públicos** revisados con la lista de palabras prohibidas de Plataforma.
4. **Visibles para todos los usuarios autenticados**, sin importar la privacidad del perfil de quien los crea.
5. **Quien crea no participa** en lo propio (no se postula, no confirma asistencia; ya es miembro).
6. **Qué pasa si la cuenta de quien crea deja de estar activa:** pendiente de **P-51**.

## Quién es quién

| Actor | En este módulo |
|---|---|
| Responsable de oportunidad | Publica oportunidades y decide postulaciones. |
| Postulante | Se postula, sigue el estado y puede retirarse. |
| Organizador | Publica eventos, los edita o cancela y descarga la lista de asistentes. |
| Asistente | Confirma o cancela su asistencia; ve a los demás asistentes y el enlace virtual. |
| Creador del proyecto | Crea el proyecto; es administrador y está protegido. |
| Administrador de proyecto, Editor, Visualizador | Roles de los miembros del proyecto (FS-COL-06). |
| Solicitante | Pide unirse a un proyecto. |
| Sistema | Cierra oportunidades, finaliza eventos, envía recordatorios y vence invitaciones. |

## Entidades y datos propios

| Entidad | Datos |
|---|---|
| Oportunidad y postulación | Datos de la oportunidad; postulante, motivación, estado, historial y retroalimentación. |
| Evento y asistencia | Datos del evento; asistente, fechas de confirmación y cancelación. |
| Proyecto, miembro, solicitud, invitación y tarea | Datos del proyecto; rol de cada miembro; tareas y actividad. |

## Expone

| Tipo | Elemento |
|---|---|
| API | `/api/v1/colaboracion/...`: oportunidades, postulaciones, eventos, asistencias, proyectos, miembros y tareas ([contrato](../../../contracts/api/colaboracion.yaml)). |
| Interfaz pública | Si dos usuarios tienen una postulación aceptada entre ellos; lo que un usuario tiene a su cargo ([contrato](../../../contracts/modulos/colaboracion.md)). |
| `Reportable` | Oportunidad, evento y proyecto. |
| Eventos | `postulacion.*`, `oportunidad.cancelada`, `evento.*`, `proyecto.*` ([catálogo](../../../contracts/eventos/README.md)). |

## Consume

| De | Qué | Para |
|---|---|---|
| Usuarios | Datos públicos, estado de la cuenta, afinidad, categorías de interés | Tarjetas, permisos, orden y afinidad. |
| Red | Si dos usuarios están conectados | Invitaciones a proyectos y "conexiones que asistirán". |
| Plataforma | Categorías y palabras prohibidas | Crear y editar. |
| Evento `cuenta.estado_cambiado` | Cambios de estado de la cuenta | P-51. |

## Preguntas abiertas del módulo

P-09, P-36, P-37, P-38, P-39, P-40, P-41, P-42, P-43, P-44, P-50, P-51.
