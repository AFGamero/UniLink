# FS-ADM-02 — Gestión de cuentas de usuario

| Campo | Valor |
|---|---|
| **Módulo** | Administración (ADM) |
| **Sprint** | Sprint 05 |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-24](../../requisitos/CasosDeUso.md#cu-24--administrar-cuentas-de-usuario) |
| **Historias** | [HU-17](../../requisitos/HistoriasDeUsuario.md#hu-17) |
| **Última actualización** | 2026-10-06 |

## 1. Objetivo

Dar al administrador de la plataforma las herramientas para conocer a los miembros de UniLink y actuar sobre las cuentas que incumplen las normas de la comunidad, de forma proporcional y con registro de cada decisión.

## 2. Alcance

**Incluye:**

- Listado de cuentas con búsqueda y filtros.
- Detalle de cada cuenta con su historial de moderación.
- Suspender temporalmente, desactivar y reactivar cuentas.
- Aviso por correo al usuario afectado.

**No incluye:**

- Editar los datos personales o el perfil de un usuario.
- Leer mensajes privados ([FS-MSG-01](../mensajeria/FS-MSG-01-mensajeria-privada.md), RN-11).
- Asignar o quitar el rol de administrador ([FS-ADM-01](./FS-ADM-01-gestion-categorias.md), RN-01).
- Aprobar cuentas de egresados y tercerizados: se agrega con FS-SRV-03 en la fase 2.

## 3. Actores

| Actor | Participación |
|---|---|
| Administrador de la plataforma | Consulta y gestiona cuentas. |
| Usuario afectado | Recibe el aviso por correo. |

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | **Suspensión:** bloquea la cuenta por un periodo de 7, 15 o 30 días. Al terminar el periodo, la cuenta se reactiva automáticamente. |
| RN-02 | **Desactivación por administrador:** bloquea la cuenta de forma indefinida. Solo se revierte con una reactivación manual. |
| RN-03 | Suspender, desactivar y reactivar exigen escribir un motivo de al menos 20 caracteres. |
| RN-04 | Mientras una cuenta está suspendida o desactivada: no puede iniciar sesión, sus sesiones abiertas se cierran, y su perfil, publicaciones y comentarios dejan de verse. Sus conversaciones quedan en solo lectura ([FS-MSG-01](../mensajeria/FS-MSG-01-mensajeria-privada.md), RN-08). Al reactivarse, todo vuelve a verse. |
| RN-05 | El usuario afectado recibe un correo con la acción, el motivo y, si es una suspensión, la fecha de fin. |
| RN-06 | Un administrador no puede actuar sobre su propia cuenta ni sobre la de otro administrador. |
| RN-07 | Cada acción queda registrada con el administrador, la fecha, la acción, el motivo y la duración, usando el registro de acciones de [FS-ADM-01](./FS-ADM-01-gestion-categorias.md). |
| RN-08 | Las cuentas "Desactivada por el usuario" ([FS-CTA-05](../cuenta/FS-CTA-05-configuracion-cuenta.md)) se muestran en el listado, pero el administrador no puede reactivarlas: solo el propio usuario. |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El panel de administración debe incluir la sección "Usuarios". | Alta |
| RF-02 | El listado debe mostrar nombre, correo, tipo de usuario, programa, fecha de registro, último acceso y estado, con 25 cuentas por página. | Alta |
| RF-03 | El listado debe permitir buscar por nombre o correo y filtrar por estado, tipo de usuario y programa. | Alta |
| RF-04 | El detalle de una cuenta debe mostrar sus datos básicos, número de publicaciones y conexiones, reportes recibidos, contenido retirado por moderación ([FS-ADM-03](./FS-ADM-03-moderacion-contenido.md)) e historial de acciones de administración. | Alta |
| RF-05 | El sistema debe permitir suspender (RN-01), desactivar (RN-02) y reactivar cuentas, con confirmación y motivo (RN-03). | Alta |
| RF-06 | El sistema debe aplicar los efectos de RN-04 de inmediato y enviar el correo de RN-05. | Alta |
| RF-07 | Una tarea programada debe reactivar las cuentas cuya suspensión terminó (RN-01). | Alta |

## 6. Datos y validaciones

| Campo | Tipo | Obligatorio | Validación |
|---|---|---|---|
| Acción | Opción | Sí | Suspender, Desactivar o Reactivar, según el estado actual. |
| Duración | Opción | Sí, al suspender | 7, 15 o 30 días. |
| Motivo | Texto | Sí | 20 a 500 caracteres. |

## 7. Estados

| Estado de la cuenta | Quién lo cambia | Salidas posibles desde el panel |
|---|---|---|
| Pendiente de verificación | Sistema ([FS-CTA-01](../cuenta/FS-CTA-01-registro.md)) | Ninguna |
| Activa | — | Suspender o desactivar |
| Suspendida hasta {fecha} | Administrador | Reactivar (antes de tiempo) o desactivar |
| Desactivada por administrador | Administrador | Reactivar |
| Desactivada por el usuario | Usuario ([FS-CTA-05](../cuenta/FS-CTA-05-configuracion-cuenta.md)) | Ninguna (RN-08) |

## 8. Flujo de pantallas

1. **Panel** → "Usuarios" → **Listado** → busca o filtra → selecciona una cuenta → **Detalle**.
2. **Detalle** → "Suspender" → elige duración y escribe el motivo → confirma → el estado cambia.
3. **Detalle** → "Reactivar" → escribe el motivo → confirma.

## 9. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Confirmar suspensión (al administrador) | "{nombre} no podrá entrar a UniLink hasta el {fecha} y su contenido dejará de verse. ¿Suspender?" |
| MSG-02 | Correo de suspensión | "Tu cuenta de UniLink está suspendida hasta el {fecha}. Motivo: {motivo}. Si crees que es un error, escribe a {correo de soporte}." |
| MSG-03 | Correo de desactivación | "Tu cuenta de UniLink fue desactivada. Motivo: {motivo}. Si crees que es un error, escribe a {correo de soporte}." |
| MSG-04 | Correo de reactivación | "Tu cuenta de UniLink está activa de nuevo. Ya puedes iniciar sesión." |
| MSG-05 | Acción no permitida | "No puedes realizar esta acción sobre la cuenta de un administrador." |

## 10. Criterios de aceptación

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
  Dado que intento desactivar una cuenta
  Cuando escribo un motivo de menos de 20 caracteres
  Entonces no puedo confirmar la acción

Escenario: Cuenta de otro administrador
  Dado que Ana es administradora
  Cuando otro administrador intenta suspender su cuenta
  Entonces ve el mensaje MSG-05

Escenario: Cuenta desactivada por el usuario
  Dado que Carla pidió eliminar su cuenta hace 5 días
  Cuando abro su detalle
  Entonces veo su estado "Desactivada por el usuario"
  Y no tengo la opción de reactivarla
```

## 11. Dependencias

- [FS-ADM-01](./FS-ADM-01-gestion-categorias.md): panel de administración y registro de acciones.
- [FS-CTA-02](../cuenta/FS-CTA-02-inicio-sesion.md): bloqueo del inicio de sesión de cuentas suspendidas o desactivadas.
- [FS-ADM-03](./FS-ADM-03-moderacion-contenido.md): reportes y contenido retirado del usuario.

## 12. Preguntas abiertas

- [ ] ¿Se quiere un proceso de apelación dentro de la plataforma? Las [normas de la comunidad](../../normas-comunidad.md#si-no-estás-de-acuerdo-con-una-decisión) proponen por ahora una revisión por correo de soporte en 15 días, hecha por otro administrador.
- [ ] ¿Debe haber suspensiones automáticas (por ejemplo, tras 3 contenidos retirados en un mes) o todas las decide un administrador?

## 13. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Gamero | Creación |
