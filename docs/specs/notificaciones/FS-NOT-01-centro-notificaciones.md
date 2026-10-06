# FS-NOT-01 — Centro de notificaciones

| Campo | Valor |
|---|---|
| **Módulo** | Notificaciones (NOT) |
| **Sprint** | Sprint 03 |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-23](../../requisitos/CasosDeUso.md#cu-23--consultar-notificaciones) |
| **Historias** | [HU-30](../../requisitos/HistoriasDeUsuario.md#hu-30) |
| **Última actualización** | 2026-10-06 |

## 1. Objetivo

Reunir en un solo lugar la actividad que involucra al usuario, para que no tenga que revisar cada sección. Este spec define un mecanismo **común** que los demás módulos usan para generar notificaciones.

## 2. Alcance

**Incluye:**

- Indicador de notificaciones no leídas en el menú.
- Panel de notificaciones con la lista y la acción de marcar como leídas.
- Mecanismo común para que cualquier módulo cree notificaciones.
- Envío por correo según las preferencias de [FS-CTA-05](../cuenta/FS-CTA-05-configuracion-cuenta.md).
- Los tipos de notificación de la red (Sprint 3).

**No incluye:**

- Notificaciones push en el celular.
- Resúmenes diarios o semanales por correo.

## 3. Actores

| Actor | Participación |
|---|---|
| Usuario autenticado | Recibe y consulta notificaciones. |
| Módulos de la plataforma | Generan notificaciones mediante el mecanismo común. |

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Cada notificación tiene: destinatario, tipo, actor que la originó (si aplica), texto, enlace al elemento relacionado, fecha y estado (no leída o leída). |
| RN-02 | El indicador del menú muestra el número de notificaciones no leídas; a partir de 100 muestra "99+". |
| RN-03 | Una notificación se marca como leída al abrirla. También se pueden marcar todas como leídas. Abrir el panel no las marca como leídas. |
| RN-04 | El indicador se actualiza sin recargar la página, con un retraso máximo de 60 segundos. |
| RN-05 | Las notificaciones se conservan 90 días y luego se eliminan. |
| RN-06 | Si el elemento relacionado ya no existe (por ejemplo, una solicitud cancelada), la notificación se elimina o, si ya fue leída, muestra "Este contenido ya no está disponible" al abrirla. |
| RN-07 | Además de la notificación interna, se envía un correo solo si el tipo lo permite y el usuario lo tiene activado en FS-CTA-05. |
| RN-08 | Nunca se notifica a un usuario por sus propias acciones. |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El sistema debe mostrar un ícono de campana con el indicador de no leídas en el menú principal. | Alta |
| RF-02 | Al pulsar la campana, el sistema debe abrir un panel con las 20 notificaciones más recientes, con las no leídas resaltadas, y un enlace "Ver todas". | Alta |
| RF-03 | La página "Ver todas" debe mostrar el historial completo con carga progresiva y filtro "Solo no leídas". | Media |
| RF-04 | Al seleccionar una notificación, el sistema debe llevar al elemento relacionado y marcarla como leída. | Alta |
| RF-05 | El sistema debe ofrecer "Marcar todas como leídas". | Media |
| RF-06 | El sistema debe ofrecer a los demás módulos una forma única de crear notificaciones (tipo, destinatario, actor, enlace), que aplique RN-07 y RN-08 automáticamente. | Alta |

## 6. Datos y validaciones

**Catálogo de tipos de notificación.** Cada sprint agrega sus tipos aquí.

| Tipo | Texto | Enlace | Correo | Sprint |
|---|---|---|---|---|
| `conexion.solicitud_recibida` | "{actor} quiere conectar contigo." | Solicitudes recibidas | Sí, "Nuevas solicitudes de conexión" | 3 |
| `conexion.solicitud_aceptada` | "{actor} aceptó tu solicitud de conexión." | Perfil del actor | No | 3 |
| `publicacion.comentario` | "{actor} comentó tu publicación \"{título}\"." | Página de la publicación | No | 4 |
| `mensaje.nuevo` | "{actor} te envió un mensaje." (una por conversación con mensajes sin leer) | Conversación | Sí, "Mensajes privados sin leer", tras 1 hora sin leer | 5 |
| `moderacion.contenido_retirado` | "Retiramos tu {publicación / comentario / evento} \"{título}\" por incumplir las normas de la comunidad." | Contenido retirado (vista del autor) | Siempre (no se puede desactivar) | 5 |
| `moderacion.reporte_revisado` | "Revisamos el contenido que reportaste." | Sin enlace | No | 5 |
| `postulacion.nueva` | "{actor} se postuló a \"{oportunidad}\"." | Panel de postulaciones | Sí, "Nuevas postulaciones a mis oportunidades" | 6 |
| `postulacion.estado_cambiado` | "Tu postulación a \"{oportunidad}\" está {estado}." | Postulación en "Mis postulaciones" | Sí, "Cambios en mis postulaciones" | 6 |
| `postulacion.retirada` | "{actor} retiró su postulación a \"{oportunidad}\"." | Panel de postulaciones | No | 6 |
| `evento.recordatorio` | "Mañana es \"{evento}\" a las {hora}." | Detalle del evento | Sí, "Recordatorio de eventos a los que asistiré" | 7 |
| `evento.actualizado` | "Cambió {fecha / lugar / enlace} de \"{evento}\"." | Detalle del evento | Sí, "Recordatorio de eventos a los que asistiré" | 7 |
| `evento.cancelado` | "Se canceló \"{evento}\": {motivo}." | Detalle del evento | Sí, "Recordatorio de eventos a los que asistiré" | 7 |
| `proyecto.*` | Por definir en FS-PRY-01 y FS-PRY-02 | — | — | 8 |

## 7. Estados

| Estado | Entra cuando | Sale hacia |
|---|---|---|
| No leída | Se crea | **Leída** al abrirla o al marcar todas |
| Leída | RN-03 | Se elimina a los 90 días |

## 8. Flujo de pantallas

1. **Cualquier página** → campana → **Panel de notificaciones** → selecciona una → **Elemento relacionado**.
2. **Panel** → "Ver todas" → **Página de notificaciones**.

## 9. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Sin notificaciones | "No tienes notificaciones." |
| MSG-02 | Elemento eliminado | "Este contenido ya no está disponible." |
| MSG-03 | Todas leídas | "Marcaste todas las notificaciones como leídas." |

## 10. Criterios de aceptación

```gherkin
Escenario: Recibir una notificación
  Dado que tengo la plataforma abierta
  Cuando Luis me envía una solicitud de conexión
  Entonces en menos de 60 segundos la campana muestra 1 sin que recargue la página

Escenario: Abrir una notificación
  Dado que tengo una notificación de solicitud de Luis sin leer
  Cuando la selecciono
  Entonces llego a mis solicitudes recibidas
  Y la notificación queda como leída
  Y el indicador disminuye en 1

Escenario: Abrir el panel no marca como leídas
  Dado que tengo 3 notificaciones sin leer
  Cuando abro y cierro el panel sin seleccionar ninguna
  Entonces el indicador sigue mostrando 3

Escenario: Marcar todas como leídas
  Dado que tengo 5 notificaciones sin leer
  Cuando pulso "Marcar todas como leídas"
  Entonces el indicador desaparece

Escenario: Correo según preferencias
  Dado que desactivé el correo "Nuevas solicitudes de conexión"
  Cuando Luis me envía una solicitud
  Entonces recibo la notificación interna
  Y no recibo correo

Escenario: Solicitud cancelada
  Dado que Luis me envió una solicitud y luego la canceló
  Y yo no había leído la notificación
  Entonces la notificación desaparece de mi panel

Escenario: Más de 99
  Dado que tengo 120 notificaciones sin leer
  Entonces el indicador muestra "99+"
```

## 11. Dependencias

- [FS-CTA-05](../cuenta/FS-CTA-05-configuracion-cuenta.md): preferencias de correo.
- [FS-RED-01](../red/FS-RED-01-solicitudes-conexion.md): primer módulo que genera notificaciones.
- Tarea programada diaria para eliminar notificaciones de más de 90 días.

## 12. Preguntas abiertas

- [ ] ¿Se actualiza el indicador consultando al servidor cada cierto tiempo o con una conexión en tiempo real? La decisión técnica debe considerar que la mensajería (Sprint 5) necesitará tiempo real.

## 13. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Gamero | Creación |
