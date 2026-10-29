# Eventos de dominio

Los módulos reaccionan a lo que pasa en otros módulos con **eventos de dominio** ([ADR-004](../../docs/arquitectura/Registro_Decisiones.md#adr-004-comunicación-entre-módulos)):

1. El módulo productor guarda el evento en su **tabla de salida**, en la misma transacción que la operación que lo origina.
2. Un **despachador** en segundo plano (el trabajador, ADR-011) lo entrega a cada consumidor.
3. El consumidor descarta los eventos que ya procesó por su `evento_id` y, si falla, el evento se reintenta. La operación original nunca se deshace (RNF-CON-04).

Todo evento sigue el [sobre común](./sobre.v1.json) y su campo `datos` se valida con el esquema `<tipo>.v1.json`. Los eventos llevan identificadores y los textos mínimos para notificar; **nunca** el contenido de un mensaje privado ni datos de contacto.

Las notificaciones son un consumidor más: el texto de cada una está en el catálogo de [FS-COM-02](../../docs/modulos/comunicacion/specs/FS-COM-02-centro-notificaciones.md).

## Catálogo

| Evento | Productor | Consumidores | Efecto | Spec | Caso de uso |
|---|---|---|---|---|---|
| [`cuenta.estado_cambiado.v1`](./cuenta.estado_cambiado.v1.json) | usuarios | Red, Contenido, Colaboración, Comunicación | Ocultan o muestran lo que posee la cuenta; las conversaciones pasan a solo lectura. El resto depende de P-51. | FS-USR-01, FS-USR-05, FS-USR-08 | CU-01, CU-03, CU-24 |
| [`perfil.actualizado.v1`](./perfil.actualizado.v1.json) | usuarios | Red | Recalcula sugerencias, complementariedad e índice de búsqueda. | FS-USR-05, FS-USR-06 | CU-03, CU-04 |
| [`auditoria.registrada.v1`](./auditoria.registrada.v1.json) | usuarios, contenido, plataforma | Plataforma | Agrega una entrada al registro de auditoría (2 años). | FS-PLT-01, FS-USR-08, FS-CNT-02 | CU-24, CU-25, CU-26 |
| [`conexion.solicitada.v1`](./conexion.solicitada.v1.json) | red | Comunicación | Notificación `conexion.solicitud_recibida` y correo "Nuevas solicitudes de conexión". | FS-RED-01, FS-RED-02 | CU-06, CU-13 |
| [`conexion.aceptada.v1`](./conexion.aceptada.v1.json) | red | Comunicación | Notificación `conexion.solicitud_aceptada` al solicitante. | FS-RED-01 | CU-07 |
| [`conexion.eliminada.v1`](./conexion.eliminada.v1.json) | red | Comunicación | La conversación entre ambos pasa a solo lectura. Sin notificación. | FS-RED-01, FS-COM-01 | CU-07 |
| [`publicacion.comentada.v1`](./publicacion.comentada.v1.json) | contenido | Comunicación | Notificación `publicacion.comentario` al autor. | FS-CNT-01 | CU-09 |
| [`contenido.reportado.v1`](./contenido.reportado.v1.json) | contenido | Contenido (cola de moderación) | Actualiza la cola; a los 5 denunciantes, el módulo dueño oculta el elemento. | FS-CNT-02 | CU-25 |
| [`contenido.retirado.v1`](./contenido.retirado.v1.json) | contenido | Comunicación, Usuarios | Notificación y correo `moderacion.contenido_retirado` al autor; suma al historial de la cuenta (FS-USR-08). | FS-CNT-02 | CU-25 |
| [`reporte.revisado.v1`](./reporte.revisado.v1.json) | contenido | Comunicación | Notificación `moderacion.reporte_revisado` a cada denunciante, sin la decisión. | FS-CNT-02 | CU-25 |
| [`mensaje.enviado.v1`](./mensaje.enviado.v1.json) | comunicacion | Comunicación | Notificación `mensaje.nuevo` (una por conversación) y correo diferido de 1 hora. | FS-COM-01 | CU-10 |
| [`postulacion.creada.v1`](./postulacion.creada.v1.json) | colaboracion | Comunicación | Notificación `postulacion.nueva` y correo al responsable. | FS-COL-02 | CU-12 |
| [`postulacion.estado_cambiado.v1`](./postulacion.estado_cambiado.v1.json) | colaboracion | Comunicación | Notificación `postulacion.estado_cambiado` y correo al postulante. | FS-COL-01 | CU-22, CU-14 |
| [`postulacion.retirada.v1`](./postulacion.retirada.v1.json) | colaboracion | Comunicación | Notificación `postulacion.retirada` al responsable. | FS-COL-02 | CU-14 |
| [`oportunidad.cancelada.v1`](./oportunidad.cancelada.v1.json) | colaboracion | Comunicación | Notificación `oportunidad.cancelada` y correo a los postulantes con postulación pendiente. | FS-COL-01 | CU-22 |
| [`evento.actualizado.v1`](./evento.actualizado.v1.json) | colaboracion | Comunicación | Notificación `evento.actualizado` y correo a los asistentes. | FS-COL-03 | CU-20 |
| [`evento.cancelado.v1`](./evento.cancelado.v1.json) | colaboracion | Comunicación | Notificación `evento.cancelado` y correo a los asistentes. | FS-COL-03 | CU-20 |
| [`evento.retirado.v1`](./evento.retirado.v1.json) | colaboracion | Comunicación | Notificación `evento.retirado` a los asistentes (al organizador le llega `contenido.retirado`). | FS-COL-03, FS-CNT-02 | CU-25 |
| [`proyecto.solicitud_creada.v1`](./proyecto.solicitud_creada.v1.json) | colaboracion | Comunicación | Notificación `proyecto.solicitud_recibida` a los administradores del proyecto. | FS-COL-05 | CU-11 |
| [`proyecto.solicitud_respondida.v1`](./proyecto.solicitud_respondida.v1.json) | colaboracion | Comunicación | Notificación `proyecto.solicitud_respondida` al solicitante. | FS-COL-05 | CU-11 |
| [`proyecto.invitacion_creada.v1`](./proyecto.invitacion_creada.v1.json) | colaboracion | Comunicación | Notificación `proyecto.invitacion` al invitado. | FS-COL-05 | CU-11 |
| [`proyecto.tarea_asignada.v1`](./proyecto.tarea_asignada.v1.json) | colaboracion | Comunicación | Notificación `proyecto.tarea_asignada`. | FS-COL-05 | CU-11 |
| [`proyecto.rol_cambiado.v1`](./proyecto.rol_cambiado.v1.json) | colaboracion | Comunicación | Notificación `proyecto.rol_cambiado` al miembro. | FS-COL-06 | CU-16 |
| [`proyecto.miembro_retirado.v1`](./proyecto.miembro_retirado.v1.json) | colaboracion | Comunicación | Notificación `proyecto.miembro_retirado` (no se envía si el miembro salió por su cuenta, FS-COM-02 RN-08). | FS-COL-05, FS-COL-06 | CU-11, CU-16 |
| [`categoria.cambiada.v1`](./categoria.cambiada.v1.json) | plataforma | Usuarios, Contenido, Colaboración | Actualizan el nombre mostrado y dejan de ofrecer las categorías desactivadas. | FS-PLT-01 | CU-26 |

**No son eventos:** el recordatorio 24 horas antes de un evento (`evento.recordatorio`) y el correo de mensajes sin leer los genera una tarea programada ([plan de implementación](../../docs/arquitectura/Plan_de_Implementacion.md#4-tareas-programadas)).

## Reglas

- Un consumidor no puede asumir el orden entre eventos de módulos distintos; usa `ocurrido_en` cuando el orden importa.
- Agregar un campo opcional no cambia la versión. Quitar o renombrar un campo crea `.v2`, y la versión anterior se mantiene hasta que todos los consumidores migren.
- Un evento nuevo se agrega a este catálogo, con su esquema, en el mismo pull request del spec que lo introduce.
