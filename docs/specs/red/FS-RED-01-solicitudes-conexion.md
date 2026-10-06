# FS-RED-01 — Solicitudes de conexión

| Campo | Valor |
|---|---|
| **Módulo** | Red de conexiones (RED) |
| **Sprint** | Sprint 03 |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-06](../../requisitos/CasosDeUso.md#cu-06--enviar-solicitud-de-conexión), [CU-07](../../requisitos/CasosDeUso.md#cu-07--responder-solicitud-de-conexión) |
| **Historias** | [HU-06](../../requisitos/HistoriasDeUsuario.md#hu-06), [HU-07](../../requisitos/HistoriasDeUsuario.md#hu-07) |
| **Última actualización** | 2026-10-06 |

## 1. Objetivo

Permitir que los miembros de la comunidad formen conexiones profesionales de mutuo acuerdo. Las conexiones habilitan la mensajería privada (FS-MSG-01), alimentan el feed (FS-CNT-01) y dan acceso a los perfiles privados.

## 2. Alcance

**Incluye:**

- Enviar una solicitud con mensaje opcional.
- Cancelar una solicitud enviada.
- Aceptar o rechazar solicitudes recibidas.
- Ver la lista de conexiones y de solicitudes enviadas y recibidas.
- Eliminar una conexión.
- Botón de conexión en el perfil y en los resultados de búsqueda.

**No incluye:**

- Bloquear o reportar usuarios.
- Seguir a alguien sin conexión mutua.
- Sugerencias de conexión ([FS-RED-02](./FS-RED-02-onboarding-sugerencias.md)).

## 3. Actores

| Actor | Participación |
|---|---|
| Usuario autenticado (solicitante) | Envía o cancela la solicitud. |
| Usuario autenticado (destinatario) | Acepta o rechaza la solicitud. |

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Entre dos usuarios solo puede existir una solicitud pendiente o una conexión a la vez. |
| RN-02 | Si A envía una solicitud a B y B ya tenía una pendiente hacia A, se conectan de inmediato (aceptación automática). |
| RN-03 | La conexión es mutua: si A está conectado con B, B está conectado con A. |
| RN-04 | La solicitud puede llevar un mensaje opcional de hasta 300 caracteres. |
| RN-05 | Un usuario puede enviar como máximo 30 solicitudes por día, para evitar spam. Las enviadas desde el onboarding no cuentan en este límite. |
| RN-06 | Al rechazar, el solicitante no recibe notificación ni motivo. Para él, el botón vuelve a "Conectar", pero no puede enviar otra solicitud a esa persona durante 30 días. |
| RN-07 | Cancelar una solicitud pendiente o eliminar una conexión no notifica a la otra persona. Tras eliminar una conexión, cualquiera de los dos puede enviar una solicitud nueva sin espera. |
| RN-08 | Las solicitudes pendientes vencen a los 90 días sin respuesta. Al vencer, el solicitante puede volver a enviarla. |
| RN-09 | No se pueden enviar solicitudes a cuentas que no estén activas ni a uno mismo. |
| RN-10 | Al aceptar, se notifica al solicitante (FS-NOT-01) y, si lo tiene activado, por correo. Al recibir una solicitud, se notifica al destinatario de la misma forma. |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El sistema debe mostrar en el perfil de otro usuario y en las tarjetas de búsqueda un botón cuyo texto depende del estado de la relación (sección 7). | Alta |
| RF-02 | Al pulsar "Conectar", el sistema debe permitir agregar un mensaje opcional y enviar la solicitud. | Alta |
| RF-03 | El sistema debe ofrecer una página "Mi red" con tres pestañas: Conexiones, Solicitudes recibidas y Solicitudes enviadas. | Alta |
| RF-04 | En Solicitudes recibidas, cada solicitud debe mostrar la tarjeta del solicitante, su mensaje, el motivo de complementariedad si aplica, y los botones "Aceptar" y "Rechazar". | Alta |
| RF-05 | El sistema debe permitir cancelar una solicitud enviada desde el perfil del destinatario o desde Solicitudes enviadas. | Media |
| RF-06 | El sistema debe permitir eliminar una conexión desde el perfil de la persona o desde la pestaña Conexiones, pidiendo confirmación. | Media |
| RF-07 | La pestaña Conexiones debe permitir buscar por nombre dentro de las propias conexiones y mostrar el total. | Media |
| RF-08 | El perfil público debe mostrar el número de conexiones del usuario. | Baja |
| RF-09 | El menú principal debe mostrar el número de solicitudes recibidas pendientes. | Alta |

## 6. Datos y validaciones

| Campo | Tipo | Obligatorio | Validación |
|---|---|---|---|
| Mensaje de la solicitud | Texto | No | Máximo 300 caracteres. |

**Datos que se guardan de cada solicitud:** solicitante, destinatario, mensaje, estado, fecha de envío y fecha de respuesta.

## 7. Estados

**Estados de la solicitud:**

| Estado | Entra cuando | Sale hacia |
|---|---|---|
| Pendiente | Se envía | **Aceptada**, **Rechazada**, **Cancelada** o **Vencida** (90 días) |
| Aceptada | El destinatario acepta, o RN-02 | Estado final; se crea la conexión |
| Rechazada | El destinatario rechaza | Estado final; aplica la espera de RN-06 |
| Cancelada | El solicitante la cancela | Estado final |
| Vencida | Pasan 90 días sin respuesta | Estado final |

**Botón según la relación, visto por el usuario actual:**

| Relación | Texto del botón | Acción |
|---|---|---|
| Sin relación | "Conectar" | Enviar solicitud |
| Solicitud enviada por mí | "Pendiente" | Cancelar solicitud |
| Solicitud recibida | "Responder" | Aceptar o rechazar |
| Conectados | "Conectado" | Menú con "Enviar mensaje" (desde el Sprint 5) y "Eliminar conexión" |
| Rechazada hace menos de 30 días | "Conectar" deshabilitado | Muestra MSG-05 |

## 8. Flujo de pantallas

1. **Perfil o resultado de búsqueda** → "Conectar" → **Diálogo de solicitud** (mensaje opcional) → "Enviar" → botón "Pendiente".
2. **Notificación** o **Mi red > Solicitudes recibidas** → "Aceptar" → la persona pasa a Conexiones.
3. **Mi red > Conexiones** → menú de una conexión → "Eliminar conexión" → confirmación.

## 9. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Solicitud enviada | "Solicitud enviada a {nombre}." |
| MSG-02 | Ya conectados por RN-02 | "¡Ahora estás conectado con {nombre}!" |
| MSG-03 | Solicitud aceptada | "Ahora estás conectado con {nombre}." |
| MSG-04 | Límite diario | "Alcanzaste el límite de 30 solicitudes por hoy. Podrás enviar más mañana." |
| MSG-05 | Espera por rechazo | "Podrás enviar otra solicitud a {nombre} a partir del {fecha}." |
| MSG-06 | Confirmar eliminación | "¿Eliminar a {nombre} de tus conexiones? No le avisaremos." |
| MSG-07 | Sin conexiones | "Aún no tienes conexiones. Busca personas con intereses parecidos a los tuyos." |
| MSG-08 | Sin solicitudes | "No tienes solicitudes pendientes." |

## 10. Criterios de aceptación

```gherkin
Escenario: Enviar solicitud con mensaje
  Dado que veo el perfil de Luis y no tenemos relación
  Cuando pulso "Conectar", escribo un mensaje y envío
  Entonces veo el mensaje MSG-01
  Y el botón cambia a "Pendiente"
  Y Luis recibe una notificación

Escenario: Aceptar solicitud
  Dado que Luis me envió una solicitud
  Cuando la acepto
  Entonces Luis aparece en mis conexiones y yo en las suyas
  Y Luis recibe una notificación de aceptación

Escenario: Solicitud recibida vista en el perfil
  Dado que Luis me envió una solicitud pendiente
  Cuando abro su perfil
  Entonces el botón dice "Responder" y no "Conectar"

Escenario: Solicitudes simultáneas
  Dado que Luis y yo pulsamos "Conectar" en el perfil del otro casi al mismo tiempo
  Cuando el sistema procesa la segunda solicitud
  Entonces quedamos conectados
  Y quien envió la segunda ve el mensaje MSG-02

Escenario: Rechazar solicitud
  Dado que Luis me envió una solicitud
  Cuando la rechazo
  Entonces Luis no recibe ninguna notificación
  Y durante 30 días Luis ve el botón "Conectar" deshabilitado con el mensaje MSG-05

Escenario: Cancelar solicitud
  Dado que envié una solicitud a Luis que sigue pendiente
  Cuando la cancelo
  Entonces el botón vuelve a "Conectar"
  Y la solicitud desaparece de las recibidas de Luis

Escenario: Eliminar conexión
  Dado que estoy conectado con Luis
  Cuando elimino la conexión y confirmo
  Entonces ya no aparecemos en las conexiones del otro
  Y Luis no recibe ninguna notificación

Escenario: Límite diario
  Dado que hoy envié 30 solicitudes fuera del onboarding
  Cuando intento enviar otra
  Entonces veo el mensaje MSG-04

Escenario: Perfil privado tras conectar
  Dado que el perfil de Luis es "Solo mis conexiones"
  Cuando Luis acepta mi solicitud
  Entonces puedo ver su perfil completo
```

## 11. Dependencias

- [FS-PRF-01](../perfil/FS-PRF-01-perfil-profesional.md) y [FS-PRF-02](../perfil/FS-PRF-02-busqueda-perfiles.md): perfil y tarjetas donde va el botón.
- [FS-NOT-01](../notificaciones/FS-NOT-01-centro-notificaciones.md): notificaciones de solicitud recibida y aceptada.
- [FS-CTA-05](../cuenta/FS-CTA-05-configuracion-cuenta.md): preferencia de correo "Nuevas solicitudes de conexión".

## 12. Preguntas abiertas

- [ ] ¿Es aceptable que el solicitante pueda deducir el rechazo por la espera de 30 días, o se prefiere que la solicitud rechazada siga viéndose como "Pendiente" para él?
- [ ] ¿Se necesita bloquear usuarios en el MVP? Hoy solo existe eliminar la conexión.

## 13. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Gamero | Creación |
