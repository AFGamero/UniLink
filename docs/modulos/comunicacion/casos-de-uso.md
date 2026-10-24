# Casos de uso — Comunicación

_MVP — Red Profesional Universitaria — Universidad del Magdalena_
_Centro de Interés de Desarrollo Tecnológico e Innovación (CIDTI)_

Casos de uso del módulo Comunicación (COM). Los actores se definen en el [mapa de módulos](../README.md#actores).

## Índice

- [CU-10 — Enviar mensaje privado](#cu-10--enviar-mensaje-privado)
- [CU-23 — Consultar notificaciones](#cu-23--consultar-notificaciones)

---

## CU-10 — Enviar mensaje privado

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario comunicarse de forma privada (1 a 1) con otro miembro con quien tenga una conexión establecida, una postulación aceptada o, en la fase 2, una solicitud de servicio activa.

**Precondiciones:** Debe existir una conexión establecida entre el usuario y el destinatario, una postulación aceptada entre el responsable de una oportunidad y el postulante ([CU-22](../colaboracion/casos-de-uso.md#cu-22--publicar-oportunidades-y-gestionar-postulaciones)), o, en la fase 2, una solicitud de servicio activa entre ambos ([CU-30](../servicios/casos-de-uso.md#cu-30--solicitar-servicio)).

**Flujo principal:**

1. El usuario selecciona una conexión de su red.
2. Abre el chat privado correspondiente.
3. Escribe y envía el mensaje.
4. El sistema entrega el mensaje y notifica al destinatario.

**Flujos alternativos / excepciones:**

- 1a. No existe conexión, postulación aceptada ni solicitud de servicio activa con el usuario seleccionado: el sistema no permite iniciar el chat.

**Postcondiciones:** El mensaje queda registrado en la conversación y disponible para ambos usuarios.

**Prioridad:** Alta

---

## CU-23 — Consultar notificaciones

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario consultar las notificaciones generadas por la plataforma (solicitudes de conexión, mensajes, cambios de estado de postulaciones, roles en proyectos, eventos, entre otras).

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El sistema muestra un indicador con el número de notificaciones no leídas.
2. El usuario abre el panel de notificaciones.
3. El sistema lista las notificaciones de la más reciente a la más antigua.
4. El usuario selecciona una notificación y el sistema lo lleva al elemento relacionado, marcándola como leída.

**Flujos alternativos / excepciones:**

- 3a. No hay notificaciones: el sistema muestra un mensaje indicándolo.
- 4a. El usuario marca todas las notificaciones como leídas.

**Postcondiciones:** El usuario queda al tanto de la actividad que lo involucra. Los tipos de notificación que recibe se configuran en [CU-03](../usuarios/casos-de-uso.md#cu-03--administrar-cuenta).

**Prioridad:** Media
