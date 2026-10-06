# FS-MSG-01 — Mensajería privada

| Campo | Valor |
|---|---|
| **Módulo** | Mensajería (MSG) |
| **Sprint** | Sprint 05 |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-10](../../requisitos/CasosDeUso.md#cu-10--enviar-mensaje-privado) |
| **Historias** | [HU-10](../../requisitos/HistoriasDeUsuario.md#hu-10) |
| **Última actualización** | 2026-10-06 |

## 1. Objetivo

Permitir que dos personas conectadas conversen en privado dentro de UniLink, para coordinar colaboraciones sin salir de la plataforma.

## 2. Alcance

**Incluye:**

- Conversaciones 1 a 1 entre usuarios conectados.
- Entrega de mensajes en tiempo real e indicador de leído.
- Bandeja de conversaciones con mensajes sin leer.
- Enviar una publicación del feed por mensaje.
- Ocultar una conversación.

**No incluye:**

- Conversaciones grupales.
- Adjuntar archivos, audios o imágenes.
- Editar o borrar mensajes enviados.
- Conversaciones originadas por solicitudes de servicio: se agregan con FS-SRV-02 en la fase 2, reutilizando este módulo.

## 3. Actores

| Actor | Participación |
|---|---|
| Usuario autenticado | Envía y recibe mensajes. |

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Solo se puede iniciar una conversación o enviar mensajes a: una conexión ([FS-RED-01](../red/FS-RED-01-solicitudes-conexion.md)); el responsable o el postulante de una postulación aceptada ([FS-OPO-01](../oportunidades/FS-OPO-01-publicacion-oportunidades.md), RN-12, desde el Sprint 6); o, en la fase 2, la otra parte de una solicitud de servicio activa. |
| RN-02 | Entre dos usuarios existe una sola conversación. |
| RN-03 | Un mensaje tiene entre 1 y 2.000 caracteres de texto. Los enlaces se convierten en vínculos. |
| RN-04 | Los mensajes se entregan en tiempo real: el destinatario con la conversación abierta lo ve en menos de 2 segundos. |
| RN-05 | Un mensaje se marca como leído cuando el destinatario abre la conversación. El remitente ve "Visto" bajo su último mensaje leído. |
| RN-06 | Si la conexión se elimina, la conversación sigue visible para ambos, pero en modo de solo lectura. Si vuelven a conectarse, se reactiva la misma conversación. |
| RN-07 | Ocultar una conversación solo la quita de la bandeja de quien la oculta. Reaparece si llega un mensaje nuevo. Los mensajes no se borran para la otra persona. |
| RN-08 | Si una cuenta se suspende o desactiva, sus conversaciones quedan en solo lectura para la otra persona. Si se elimina, sus mensajes aparecen como de "Usuario eliminado" ([FS-CTA-05](../cuenta/FS-CTA-05-configuracion-cuenta.md), RN-10). |
| RN-09 | Un usuario puede enviar como máximo 60 mensajes por minuto, para evitar spam. |
| RN-10 | **Notificaciones:** se crea una sola notificación `mensaje.nuevo` por conversación mientras haya mensajes sin leer; no una por mensaje. Si un mensaje sigue sin leerse 1 hora después, se envía un correo (si el usuario lo tiene activado), como máximo uno por conversación al día. |
| RN-11 | Los administradores **no** pueden leer las conversaciones privadas. |
| RN-12 | Al enviar una publicación por mensaje, se envía un mensaje con una vista previa (autor, título y enlace). El destinatario solo la puede abrir si tiene permiso de verla ([FS-CNT-01](../contenido/FS-CNT-01-publicaciones-feed.md), RN-06). |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El sistema debe mostrar un ícono de mensajes en el menú principal con el número de conversaciones con mensajes sin leer. | Alta |
| RF-02 | El sistema debe ofrecer una página "Mensajes" con la bandeja a la izquierda (foto, nombre, último mensaje y hora, ordenadas por actividad) y la conversación abierta a la derecha. En celular, se muestran por separado. | Alta |
| RF-03 | El sistema debe permitir iniciar una conversación desde el botón "Enviar mensaje" del perfil de una conexión y desde "Mi red". | Alta |
| RF-04 | El sistema debe entregar los mensajes en tiempo real (RN-04) y mostrar "Visto" (RN-05). | Alta |
| RF-05 | La conversación debe cargar los 30 mensajes más recientes y los anteriores al desplazarse hacia arriba. | Alta |
| RF-06 | El sistema debe permitir buscar conversaciones por nombre de la persona. | Media |
| RF-07 | El sistema debe permitir ocultar una conversación (RN-07). | Baja |
| RF-08 | El sistema debe agregar a cada publicación del feed la opción "Enviar por mensaje", que permite elegir una o varias conexiones (RN-12). | Media |
| RF-09 | Si la conversación está en solo lectura (RN-06, RN-08), el campo de escritura debe reemplazarse por un aviso que explique el motivo. | Alta |

## 6. Datos y validaciones

| Campo | Tipo | Obligatorio | Validación |
|---|---|---|---|
| Mensaje | Texto | Sí | 1 a 2.000 caracteres; sin espacios solamente. |

**Datos de cada mensaje:** conversación, remitente, texto, publicación compartida (opcional), fecha de envío y fecha de lectura.

## 7. Estados

| Estado de la conversación | Entra cuando | Sale hacia |
|---|---|---|
| Activa | Se envía el primer mensaje o se reconectan | **Solo lectura** si se elimina la conexión o se suspende/desactiva una de las cuentas |
| Solo lectura | RN-06 o RN-08 | **Activa** si se reconectan o se reactiva la cuenta |

## 8. Flujo de pantallas

1. **Perfil de una conexión** → "Enviar mensaje" → **Mensajes** con la conversación abierta.
2. **Menú principal** → ícono de mensajes → **Mensajes** → elige una conversación.
3. **Feed** → "Enviar por mensaje" en una publicación → elige conexiones → "Enviar".

## 9. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Bandeja vacía | "Aún no tienes conversaciones. Escríbele a una de tus conexiones." |
| MSG-02 | Conexión eliminada | "Ya no estás conectado con {nombre}. Puedes leer la conversación, pero no enviar mensajes." |
| MSG-03 | Cuenta no disponible | "Esta cuenta no está disponible en este momento." |
| MSG-04 | Límite de envío | "Estás enviando mensajes muy rápido. Espera un momento." |
| MSG-05 | Correo de mensajes sin leer | "{nombre} te escribió en UniLink: \"{primeros 100 caracteres}\"" |
| MSG-06 | Publicación compartida | "Publicación enviada a {n} conexiones." |

## 10. Criterios de aceptación

```gherkin
Escenario: Enviar mensaje a una conexión
  Dado que estoy conectado con Luis
  Cuando le escribo "Hola, ¿hablamos del proyecto?" desde su perfil
  Entonces el mensaje aparece en la conversación
  Y si Luis tiene la conversación abierta, lo ve en menos de 2 segundos

Escenario: Sin conexión no hay chat
  Dado que no estoy conectado con Pedro
  Entonces su perfil no muestra el botón "Enviar mensaje"

Escenario: Visto
  Dado que le envié un mensaje a Luis
  Cuando Luis abre la conversación
  Entonces veo "Visto" bajo mi mensaje

Escenario: Una notificación por conversación
  Dado que Luis me envía 5 mensajes seguidos y no los he leído
  Entonces tengo una sola notificación de Luis en mi centro de notificaciones

Escenario: Correo por mensaje sin leer
  Dado que tengo activado el correo de "Mensajes privados sin leer"
  Cuando Luis me escribe y no abro la conversación en 1 hora
  Entonces recibo un correo con el mensaje MSG-05
  Y si me escribe de nuevo ese mismo día, no recibo otro correo

Escenario: Conexión eliminada
  Dado que tengo una conversación con Luis
  Cuando Luis elimina nuestra conexión
  Entonces puedo leer la conversación
  Y veo el mensaje MSG-02 en lugar del campo de escritura

Escenario: Compartir una publicación
  Dado que veo una publicación en el feed
  Cuando la envío por mensaje a Luis y a Carla
  Entonces cada uno recibe un mensaje con la vista previa de la publicación
  Y veo el mensaje MSG-06

Escenario: Ocultar conversación
  Dado que oculté mi conversación con Luis
  Cuando Luis me envía un mensaje nuevo
  Entonces la conversación vuelve a aparecer en mi bandeja con todo el historial
```

## 11. Dependencias

- [FS-RED-01](../red/FS-RED-01-solicitudes-conexion.md): conexiones y botón "Enviar mensaje".
- [FS-NOT-01](../notificaciones/FS-NOT-01-centro-notificaciones.md): notificación `mensaje.nuevo`.
- [FS-CTA-05](../cuenta/FS-CTA-05-configuracion-cuenta.md): preferencia de correo "Mensajes privados sin leer".
- [FS-CNT-01](../contenido/FS-CNT-01-publicaciones-feed.md): publicaciones que se comparten.
- Infraestructura de tiempo real (decidida en el Sprint 3, FS-NOT-01).

## 12. Preguntas abiertas

- [ ] ¿Se necesita poder reportar a un usuario por acoso en mensajes? Hoy solo se puede eliminar la conexión, y los administradores no leen los mensajes (RN-11).
- [ ] ¿Se quiere permitir adjuntar archivos en una versión posterior?

## 13. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Gamero | Creación |
