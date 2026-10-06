# FS-EVT-02 — Confirmación de asistencia (RSVP)

| Campo | Valor |
|---|---|
| **Módulo** | Eventos (EVT) |
| **Sprint** | Sprint 07 |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-15](../../requisitos/CasosDeUso.md#cu-15--confirmar-asistencia-a-eventos-rsvp) |
| **Historias** | [HU-26](../../requisitos/HistoriasDeUsuario.md#hu-26) |
| **Última actualización** | 2026-10-06 |

## 1. Objetivo

Permitir que los usuarios confirmen su asistencia a un evento, vean quiénes más irán para encontrarse allí y lo agreguen a su calendario. Al organizador le da una cifra real de asistentes para preparar el evento.

## 2. Alcance

**Incluye:**

- Confirmar y cancelar asistencia.
- Control del cupo.
- Lista de asistentes para los confirmados y el organizador.
- Exportar a calendario (archivo `.ics` y enlace a Google Calendar).
- Recordatorio 24 horas antes.
- Resumen de asistencia y descarga de la lista para el organizador.

**No incluye:**

- Lista de espera cuando se llena el cupo.
- Registro de asistencia real el día del evento (por ejemplo, con código QR).
- Certificados de asistencia.

## 3. Actores

| Actor | Participación |
|---|---|
| Usuario autenticado (asistente) | Confirma o cancela su asistencia. |
| Organizador | Consulta y descarga la lista de asistentes. |

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Solo se puede confirmar asistencia a eventos en estado "Programado" que no han comenzado. |
| RN-02 | El organizador no confirma asistencia a su propio evento; aparece como organizador en la lista. |
| RN-03 | Si el evento tiene cupo y está lleno, el botón "Asistiré" se deshabilita con el texto "Cupo completo". Si alguien cancela, el cupo se libera. |
| RN-04 | El usuario puede cancelar su asistencia hasta que el evento comience. Después de que comience, su respuesta queda fija. |
| RN-05 | **Lista de asistentes:** la ven el organizador y los asistentes confirmados. Los demás solo ven el número de confirmados. |
| RN-06 | En la lista, los asistentes con perfil "Solo mis conexiones" aparecen solo con nombre, foto y programa para quienes no son sus conexiones. |
| RN-07 | Los usuarios que no han confirmado ven cuántas de sus conexiones asistirán (por ejemplo, "3 de tus conexiones asistirán"), sin ver sus nombres. |
| RN-08 | **Recordatorio:** 24 horas antes del inicio, cada asistente confirmado recibe la notificación `evento.recordatorio` y, si lo tiene activado, un correo. Quien confirma con menos de 24 horas de anticipación no recibe recordatorio. |
| RN-09 | El archivo de calendario incluye título, descripción, inicio, fin, lugar y, si aplica, el enlace virtual. |
| RN-10 | El organizador puede descargar la lista de asistentes en CSV con nombre, programa y fecha de confirmación. **No** incluye correos ni otros datos personales. |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El detalle del evento debe mostrar el botón "Asistiré" o, si el usuario ya confirmó, "Asistirás" con la opción de cancelar. | Alta |
| RF-02 | El sistema debe aplicar RN-01 a RN-04 al confirmar o cancelar. | Alta |
| RF-03 | Tras confirmar, el detalle debe mostrar la lista de asistentes (RN-05, RN-06) con buscador por nombre. | Alta |
| RF-04 | Tras confirmar, el sistema debe ofrecer "Agregar a mi calendario" con dos opciones: descargar `.ics` y abrir en Google Calendar (RN-09). | Media |
| RF-05 | El detalle debe mostrar a quien no ha confirmado el número de asistentes y cuántas de sus conexiones irán (RN-07). | Media |
| RF-06 | El sistema debe enviar el recordatorio de RN-08 mediante una tarea programada. | Media |
| RF-07 | El organizador debe ver en el detalle un resumen: confirmados, cupo restante y cancelaciones, y el botón "Descargar lista" (RN-10). | Media |
| RF-08 | El evento debe aparecer en la pestaña "Mis eventos" del asistente ([FS-EVT-01](./FS-EVT-01-publicacion-listado-eventos.md), RF-05). | Media |

## 6. Datos y validaciones

**Datos de cada confirmación:** evento, usuario, fecha de confirmación, fecha de cancelación (si la hubo).

No hay campos que el usuario deba llenar.

## 7. Estados

| Estado de la asistencia | Entra cuando | Sale hacia |
|---|---|---|
| Confirmada | El usuario pulsa "Asistiré" | **Cancelada** si la cancela antes del inicio |
| Cancelada | El usuario la cancela | **Confirmada** si vuelve a confirmar antes del inicio y hay cupo |

## 8. Flujo de pantallas

1. **Detalle del evento** → "Asistiré" → el botón cambia a "Asistirás" → aparecen la lista de asistentes y "Agregar a mi calendario".
2. **Detalle** → "Asistirás" → "Cancelar asistencia" → confirma → vuelve a "Asistiré".
3. **Detalle** (como organizador) → resumen → "Descargar lista".

## 9. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Asistencia confirmada | "¡Listo! Te esperamos en \"{título}\"." |
| MSG-02 | Cupo completo | "Cupo completo" |
| MSG-03 | Confirmar cancelación | "¿Ya no podrás asistir? Liberaremos tu cupo." |
| MSG-04 | Conexiones que asistirán | "{n} de tus conexiones asistirán." |
| MSG-05 | Recordatorio | "Mañana es \"{título}\" a las {hora} en {lugar o 'línea'}." |
| MSG-06 | Evento ya comenzó | "Este evento ya comenzó; no puedes cambiar tu asistencia." |

## 10. Criterios de aceptación

```gherkin
Escenario: Confirmar asistencia
  Dado que veo un evento programado que no ha comenzado
  Cuando pulso "Asistiré"
  Entonces veo el mensaje MSG-01
  Y veo la lista de asistentes
  Y veo la opción "Agregar a mi calendario"

Escenario: Lista oculta para quien no confirmó
  Dado que no he confirmado asistencia a un evento con 15 confirmados
  Y 3 de ellos son mis conexiones
  Cuando abro su detalle
  Entonces veo "15 asistentes" y el mensaje MSG-04 con n = 3
  Pero no veo la lista de nombres

Escenario: Cupo completo
  Dado que un evento tiene cupo de 30 y 30 confirmados
  Entonces el botón muestra "Cupo completo" y está deshabilitado
  Cuando un asistente cancela
  Entonces el botón vuelve a estar disponible

Escenario: Cancelar asistencia
  Dado que confirmé asistencia a un evento que aún no comienza
  Cuando cancelo mi asistencia
  Entonces desaparezco de la lista de asistentes

Escenario: Asistencia fija tras el inicio
  Dado que un evento ya comenzó
  Cuando intento cancelar mi asistencia
  Entonces veo el mensaje MSG-06

Escenario: Agregar al calendario
  Dado que confirmé asistencia a un evento virtual
  Cuando descargo el archivo de calendario
  Entonces el archivo incluye el título, las horas de inicio y fin y el enlace del evento

Escenario: Recordatorio
  Dado que confirmé asistencia a un evento que empieza en 3 días
  Cuando faltan 24 horas para el inicio
  Entonces recibo la notificación con el mensaje MSG-05

Escenario: Lista para el organizador
  Dado que organizo un evento con 40 confirmados
  Cuando descargo la lista
  Entonces obtengo un CSV con nombre, programa y fecha de confirmación de los 40
  Y el archivo no incluye correos
```

## 11. Dependencias

- [FS-EVT-01](./FS-EVT-01-publicacion-listado-eventos.md): eventos, estados y cupo.
- [FS-RED-01](../red/FS-RED-01-solicitudes-conexion.md): conexiones para RN-07.
- [FS-NOT-01](../notificaciones/FS-NOT-01-centro-notificaciones.md) y [FS-CTA-05](../cuenta/FS-CTA-05-configuracion-cuenta.md): recordatorio y su preferencia de correo.

## 12. Preguntas abiertas

- [ ] ¿Se necesita lista de espera para eventos con cupo?
- [ ] ¿El organizador debe poder escribir un mensaje a todos los asistentes (por ejemplo, "Traigan su computador")?

## 13. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Gamero | Creación |
