# Historias de usuario — Comunicación

_MVP — Red Profesional Universitaria — Universidad del Magdalena_
_Centro de Interés de Desarrollo Tecnológico e Innovación (CIDTI)_

Historias de usuario del módulo Comunicación (COM), en formato "Como / quiero / para", derivadas de sus [casos de uso](./casos-de-uso.md).

## Índice

- [HU-10 — Como usuario autenticado, quiero enviar mensajes privados a otro miembro con quien tengo una conexión establecida](#hu-10)
- [HU-30 — Como usuario autenticado, quiero consultar mis notificaciones en un solo lugar](#hu-30)

---

## HU-10

> **Como** usuario autenticado,
> **quiero** enviar mensajes privados a otro miembro con quien tengo una conexión establecida,
> **para** comunicarme directamente con mis contactos dentro de la plataforma.

**Caso de uso relacionado:** [CU-10](./casos-de-uso.md#cu-10--enviar-mensaje-privado)

**Criterios de aceptación:**

- Dado que selecciono una conexión de mi red, entonces puedo abrir un chat privado con esa persona.
- Dado que envío un mensaje, entonces el sistema lo entrega y notifica al destinatario.
- Dado que intento escribir a un usuario con el que no tengo conexión, postulación aceptada ni, en la fase 2, solicitud de servicio activa ([HU-31](../servicios/historias.md#hu-31)), entonces el sistema no me permite iniciar el chat.

**Prioridad:** Alta

---

## HU-30

> **Como** usuario autenticado,
> **quiero** consultar mis notificaciones en un solo lugar,
> **para** enterarme de la actividad que me involucra sin tener que revisar cada sección.

**Caso de uso relacionado:** [CU-23](./casos-de-uso.md#cu-23--consultar-notificaciones)

**Criterios de aceptación:**

- Dado que tengo notificaciones sin leer, entonces el sistema muestra un indicador con su número.
- Dado que abro el panel de notificaciones, entonces las veo ordenadas de la más reciente a la más antigua.
- Dado que selecciono una notificación, entonces el sistema me lleva al elemento relacionado y la marca como leída.
- Dado que no tengo notificaciones, entonces el sistema me indica que no hay notificaciones.

**Prioridad:** Media
