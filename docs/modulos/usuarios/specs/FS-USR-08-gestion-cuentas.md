# FS-USR-08 — Gestión de cuentas de usuario

| Campo | Valor |
|---|---|
| **Módulo** | Usuarios (USR) |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-24](../casos-de-uso.md#cu-24--administrar-cuentas-de-usuario) |
| **Historias** | [HU-17](../historias.md#hu-17) |
| **Última actualización** | 2026-10-24 |

## 1. Objetivo

Dar al administrador de la plataforma las herramientas para conocer a los miembros de UniLink y actuar sobre las cuentas que incumplen las normas de la comunidad, de forma proporcional y con registro de cada decisión.

## 2. Quién es quién

| Actor | Qué hace | Qué ve | Qué no puede hacer |
|---|---|---|---|
| Administrador de la plataforma | Busca cuentas; suspende, inhabilita y reactiva con motivo. | Datos básicos, estado, reportes recibidos, contenido retirado e historial. | Actuar sobre su propia cuenta o la de otro administrador; reactivar una cuenta en eliminación; leer mensajes privados; editar el perfil. |
| Dueño del perfil | Recibe el aviso por correo con la acción y el motivo. | El correo y el estado al iniciar sesión (FS-USR-02). | — |
| Sistema | Reactiva las cuentas al terminar la suspensión. | — | — |

## 3. Alcance

**Incluye:**

- Listado de cuentas con búsqueda y filtros.
- Detalle de cada cuenta con su historial de moderación.
- Suspender temporalmente, inhabilitar y reactivar cuentas.
- Aviso por correo al usuario afectado.

**No incluye:**

- Editar los datos personales o el perfil de un usuario.
- Leer mensajes privados ([FS-COM-01](../../comunicacion/specs/FS-COM-01-mensajeria-privada.md), RN-11).
- Asignar o quitar el rol de administrador ([FS-PLT-01](../../plataforma/specs/FS-PLT-01-gestion-categorias.md), RN-01).
- Aprobar cuentas de egresados y tercerizados: se agrega con FS-SRV-03 en la fase 2.

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | **Suspensión:** bloquea la cuenta por un periodo de 7, 15 o 30 días. Al terminar el periodo, la cuenta se reactiva automáticamente. |
| RN-02 | **Inhabilitación por administración:** bloquea la cuenta de forma indefinida. Solo se revierte con una reactivación manual. |
| RN-03 | Suspender, inhabilitar y reactivar exigen escribir un motivo de al menos 20 caracteres. |
| RN-04 | Mientras una cuenta está suspendida o inhabilitada: no puede iniciar sesión, sus sesiones abiertas se cierran, y su perfil, publicaciones y comentarios dejan de verse. Sus conversaciones quedan en solo lectura ([FS-COM-01](../../comunicacion/specs/FS-COM-01-mensajeria-privada.md), RN-08). Al reactivarse, todo vuelve a verse. |
| RN-05 | El usuario afectado recibe un correo con la acción, el motivo y, si es una suspensión, la fecha de fin. |
| RN-06 | Un administrador no puede actuar sobre su propia cuenta ni sobre la de otro administrador. |
| RN-07 | Cada acción queda registrada con el administrador, la fecha, la acción, el motivo y la duración, usando el registro de acciones de [FS-PLT-01](../../plataforma/specs/FS-PLT-01-gestion-categorias.md). |
| RN-08 | Las cuentas "En eliminación" ([FS-USR-05](./FS-USR-05-configuracion-cuenta.md)) se muestran en el listado, pero el administrador no puede reactivarlas: solo el propio usuario. |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El panel de administración debe incluir la sección "Usuarios". | Alta |
| RF-02 | El listado debe mostrar nombre, correo, tipo de usuario, unidad académica, fecha de registro, último acceso y estado, con 25 cuentas por página. | Alta |
| RF-03 | El listado debe permitir buscar por nombre o correo y filtrar por estado, tipo de usuario y unidad académica. | Alta |
| RF-04 | El detalle de una cuenta debe mostrar sus datos básicos, número de publicaciones y conexiones, reportes recibidos, contenido retirado por moderación ([FS-CNT-02](../../contenido/specs/FS-CNT-02-moderacion-contenido.md)) e historial de acciones de administración. La pantalla reúne esos datos pidiéndolos a cada módulo desde la capa de API (ADR-003). | Alta |
| RF-05 | El sistema debe permitir suspender (RN-01), inhabilitar (RN-02) y reactivar cuentas, con confirmación y motivo (RN-03). | Alta |
| RF-06 | El sistema debe aplicar los efectos de RN-04 de inmediato y enviar el correo de RN-05. | Alta |
| RF-07 | Una tarea programada debe reactivar las cuentas cuya suspensión terminó (RN-01). | Alta |

## 6. Datos y validaciones

| Campo | Tipo | Obligatorio | Validación |
|---|---|---|---|
| Acción | Opción | Sí | Suspender, Inhabilitar o Reactivar, según el estado actual. |
| Duración | Opción | Sí, al suspender | 7, 15 o 30 días. |
| Motivo | Texto | Sí | 20 a 500 caracteres. |

## 7. Estados

| Estado de la cuenta | Quién lo cambia | Salidas posibles desde el panel |
|---|---|---|
| Pendiente de verificación | Sistema ([FS-USR-01](./FS-USR-01-registro.md)) | Ninguna |
| Activa | — | Suspender o inhabilitar |
| Suspendida hasta {fecha} | Administrador | Reactivar (antes de tiempo) o inhabilitar |
| Inhabilitada por administración | Administrador | Reactivar |
| En eliminación | Usuario ([FS-USR-05](./FS-USR-05-configuracion-cuenta.md)) | Ninguna (RN-08) |

La máquina de estados completa de la cuenta está en el [README del módulo](../README.md#máquina-de-estados-de-la-cuenta).

## 8. Flujo principal

1. **Panel** → "Usuarios" → **Listado** → busca o filtra → selecciona una cuenta → **Detalle**.
2. **Detalle** → "Suspender" → elige duración y escribe el motivo → confirma → el estado cambia.
3. **Detalle** → "Reactivar" → escribe el motivo → confirma.

## 9. Variaciones

| Variación | Qué cambia | Regla |
|---|---|---|
| Suspensión de 7, 15 o 30 días | Se reactiva sola al terminar. | RN-01 |
| Inhabilitación | Indefinida hasta reactivar. | RN-02 |
| Reactivar antes de tiempo | Termina la suspensión. | Sección 7 |
| Cuenta en eliminación | Se ve en el listado, sin acciones. | RN-08 |
| Cuenta de administrador | Sin acciones (MSG-05). | RN-06 |

## 10. ¿Qué pasaría si…?

| Situación | Comportamiento esperado | Regla o pregunta |
|---|---|---|
| Dos administradores actúan a la vez sobre la misma cuenta | El segundo recibe un conflicto y ve el estado actual antes de decidir. | RNF-CON-02 |
| La cuenta sancionada es responsable de oportunidades, organiza eventos o crea proyectos | Su perfil y contenido dejan de verse; qué pasa con esos objetos depende de P-51. | RN-04, P-51 |
| El correo de aviso no se puede enviar | La sanción se aplica igual y el correo se reintenta. | RNF-DIS-05 |
| La tarea de fin de suspensión y una reactivación manual coinciden | La cuenta queda Activa una sola vez, con un solo registro. | RNF-CON-04 |
| El administrador pierde su rol mientras usa el panel | Su siguiente acción recibe "Acceso denegado". | FS-PLT-01 RN-02 |
| Privacidad | El detalle no muestra mensajes privados ni datos que no sean básicos. | RNF-PRI-04 |

## 11. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Confirmar suspensión (al administrador) | "{nombre} no podrá entrar a UniLink hasta el {fecha} y su contenido dejará de verse. ¿Suspender?" |
| MSG-02 | Correo de suspensión | "Tu cuenta de UniLink está suspendida hasta el {fecha}. Motivo: {motivo}. Si crees que es un error, escribe a {correo de soporte}." |
| MSG-03 | Correo de inhabilitación | "Tu cuenta de UniLink fue inhabilitada. Motivo: {motivo}. Si crees que es un error, escribe a {correo de soporte}." |
| MSG-04 | Correo de reactivación | "Tu cuenta de UniLink está activa de nuevo. Ya puedes iniciar sesión." |
| MSG-05 | Acción no permitida | "No puedes realizar esta acción sobre la cuenta de un administrador." |

## 12. Resultado esperado

```gherkin
Escenario: Buscar una cuenta
  Dado que soy administrador
  Cuando busco "luis" en Usuarios
  Entonces veo las cuentas cuyo nombre o correo contiene "luis"

Escenario: Suspender una cuenta
  Dado que veo el detalle de la cuenta de Pedro
  Cuando la suspendo por 7 días con un motivo válido
  Entonces Pedro no puede iniciar sesión
  Y su sesión abierta se cierra
  Y su perfil y sus publicaciones dejan de verse
  Y Pedro recibe el correo MSG-02
  Y la acción queda en el historial de la cuenta

Escenario: Fin de la suspensión
  Dado que la suspensión de Pedro termina hoy
  Cuando se ejecuta la tarea programada
  Entonces la cuenta de Pedro vuelve a estar activa
  Y su contenido vuelve a verse

Escenario: Motivo obligatorio
  Dado que intento inhabilitar una cuenta
  Cuando escribo un motivo de menos de 20 caracteres
  Entonces no puedo confirmar la acción

Escenario: Cuenta de otro administrador
  Dado que Ana es administradora
  Cuando otro administrador intenta suspender su cuenta
  Entonces ve el mensaje MSG-05

Escenario: Cuenta inhabilitada por el usuario
  Dado que Carla pidió eliminar su cuenta hace 5 días
  Cuando abro su detalle
  Entonces veo su estado "En eliminación"
  Y no tengo la opción de reactivarla

Escenario: Dos administradores a la vez
  Dado que Ana y Carlos abren el detalle de la cuenta de Pedro
  Y Ana lo suspende
  Cuando Carlos intenta inhabilitarlo con la versión anterior
  Entonces Carlos ve el estado actual "Suspendida" antes de confirmar

Escenario: Inhabilitar y reactivar
  Dado que inhabilité la cuenta de Pedro
  Cuando la reactivo con un motivo válido
  Entonces Pedro puede volver a iniciar sesión
  Y recibe el correo MSG-04

Escenario: Correo caído
  Dado que el servicio de correo no responde
  Cuando suspendo la cuenta de Pedro
  Entonces la suspensión se aplica
  Y el correo se envía cuando el servicio vuelve
```

## 13. Contratos

**Expone:**

- API: `GET /api/v1/usuarios/admin/cuentas`, `GET /api/v1/usuarios/admin/cuentas/{id}`, `POST /api/v1/usuarios/admin/cuentas/{id}/sanciones`, `POST /api/v1/usuarios/admin/cuentas/{id}/reactivacion` ([contrato](../../../../contracts/api/usuarios.yaml)).
- Eventos: `cuenta.estado_cambiado` y `auditoria.registrada` ([catálogo](../../../../contracts/eventos/README.md)).

**Consume:** evento `contenido.retirado` (historial del usuario); Red y Contenido para el detalle de la cuenta (desde la capa de API).

## 14. Calidad

RNF-SEG-04, RNF-SEG-10 (auditoría), RNF-CON-02, [EC-03](../../../srs/Especificacion_Requisitos.md#34-escenarios-de-atributos-de-calidad).

## 15. Preguntas abiertas

- P-33 — ¿apelación dentro de la plataforma?
- P-34 — ¿suspensiones automáticas?
- P-51 — efectos de la sanción sobre lo que posee la cuenta.

## 16. Lista de revisión

- [x] Cada actor de "Quién es quién" existe en el [SRS §2.4](../../../srs/Especificacion_Requisitos.md#24-actores-del-sistema) con el mismo nombre.
- [x] Toda acción tiene un actor que puede hacerla y se valida en el servidor (RNF-SEG-04).
- [ ] Cada regla tiene al menos un escenario en "Resultado esperado".
- [x] "¿Qué pasaría si…?" revisó las siete situaciones: concurrencia, estado de la cuenta, eliminación de lo que usa, pérdida de permiso, falla externa, límites de uso y privacidad.
- [ ] Ningún dato se recoge sin finalidad (RNF-PRI-01).
- [x] No contradice a su caso de uso, a su historia ni a otro spec.
- [x] Sus contratos existen en [`contracts/`](../../../../contracts/README.md).
- [ ] No tiene preguntas abiertas que bloqueen el desarrollo.

## 17. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Gamero | Creación |
| 2026-10-24 | Equipo UniLink | Estudio de quién es quién, variaciones, casos límite y contratos; nueva plantilla. |
