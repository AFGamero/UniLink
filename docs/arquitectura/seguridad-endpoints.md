# Seguridad de la API y control de acceso por endpoint

| Campo | Valor |
|---|---|
| **Sprint** | Sprint 0 |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Requisitos** | [RNF-SEG-03, RNF-SEG-04, RNF-SEG-05, RNF-SEG-06, RNF-SEG-07](../srs/Especificacion_Requisitos.md#331-seguridad), [RNF-PRI-04](../srs/Especificacion_Requisitos.md#332-privacidad-y-protección-de-datos-personales) |
| **Última actualización** | 2026-10-08 |

## 1. Objetivo

Definir antes de escribir código **qué endpoints de la API existen, quién puede llamarlos y cuáles están bloqueados**. Así cada sprint implementa sus endpoints con el control de acceso ya decidido, y las pruebas de [RNF-SEG-04](../srs/Especificacion_Requisitos.md#331-seguridad) tienen una lista contra la cual verificar.

Las rutas son una propuesta: los nombres pueden cambiar al elegir el stack, pero **el nivel de acceso de cada una no cambia sin actualizar este documento**.

> **Nota (2026-10-27):** este documento es anterior a la reestructuración del 2026-10-24. Desde entonces, **la fuente de verdad de las rutas es [`contracts/api/`](../../contracts/api/README.md)** (prefijo `/api/v1/<modulo>/...`), y cada operación indica allí quién puede usarla. Las tablas de las secciones 5, 7 y 8 conservan las rutas de la versión anterior (por ejemplo, `/auth/sesion` corresponde a `/api/v1/usuarios/sesion`). Siguen vigentes los principios (sección 2), los niveles de acceso (3), las reglas de sesión (4), los endpoints bloqueados (6) y los códigos de respuesta (9). Falta conciliar las rutas con los contratos y con la decisión de autenticación de la [reunión del 2026-10-19](../decisiones/2026-10-19-reunion-preguntas-abiertas.md) (cuentas precreadas y token del Campus Virtual, ADR-013).

## 2. Principios

| ID | Principio |
|---|---|
| SEC-01 | **Bloqueado por defecto.** Todo endpoint exige sesión válida y cuenta **Activa**, salvo los de la [lista de endpoints públicos](#5-endpoints-públicos). Un endpoint nuevo que no aparece en este documento se considera bloqueado. |
| SEC-02 | **El servidor decide.** Todo permiso se valida en el servidor; ocultar un botón no es control de acceso (RNF-SEG-04). |
| SEC-03 | **Lo propio se pide con `/yo`.** Los recursos que solo puede ver su dueño (configuración, hoja de vida, mis postulaciones) usan rutas sin identificador de usuario, por ejemplo `/perfiles/yo`. Así no hay un ID que se pueda cambiar para ver datos de otro. |
| SEC-04 | **Identificadores no adivinables.** Todos los recursos usan UUID, no números consecutivos. |
| SEC-05 | **El estado de la cuenta se revisa en cada petición**, no solo al iniciar sesión. Si un administrador suspende una cuenta, su siguiente petición ya es rechazada ([FS-USR-08](../modulos/usuarios/specs/FS-USR-08-gestion-cuentas.md), RN-04). |
| SEC-06 | **No revelar lo que no se puede ver.** Si el usuario no tiene permiso ni para saber que un recurso existe (una conversación ajena, una publicación de un perfil privado), la respuesta es `404`, no `403`. |
| SEC-07 | **Los datos se filtran en la respuesta, no en la pantalla.** Si un campo es privado (el enlace de un evento, las etiquetas de un perfil privado), el servidor no lo envía. |

## 3. Niveles de acceso

| Nivel | Quién puede llamar | Si no cumple |
|---|---|---|
| **Público** | Cualquiera, sin sesión. | — |
| **Token** | Quien tenga un token válido de un correo (verificación, recuperación, cambio de correo). | `400` con mensaje de enlace vencido o inválido |
| **Autenticado** | Usuario con sesión válida y cuenta **Activa**. | `401` sin sesión · `403` si la cuenta no está activa |
| **Dueño** | Autenticado y dueño del recurso. | `404` o `403` según SEC-06 |
| **Relación** | Autenticado con una relación concreta: conexión, participante de una conversación, responsable de una oportunidad, organizador o asistente de un evento. | `404` o `403` según SEC-06 |
| **Rol de proyecto** | Miembro del proyecto con el rol suficiente según la [matriz de permisos](../modulos/colaboracion/specs/FS-COL-06-roles-proyectos.md#6-datos-y-validaciones). | `404` si no es miembro · `403` si su rol no alcanza |
| **Administrador** | Autenticado con rol de administrador de la plataforma. | `403` (página "Acceso denegado", [FS-PLT-01](../modulos/plataforma/specs/FS-PLT-01-gestion-categorias.md), RN-02) |
| **Bloqueado** | Nadie desde internet. Solo red interna o tareas programadas. | `404` |

## 4. Sesión e inicio de sesión

| ID | Regla | Origen |
|---|---|---|
| SES-01 | La sesión se guarda **en el servidor** y el navegador solo recibe un identificador en una cookie `HttpOnly`, `Secure` y `SameSite=Lax`. No se usan tokens JWT en `localStorage`, porque el servidor debe poder invalidar sesiones al cerrar sesión, cambiar la contraseña o suspender la cuenta. | RNF-SEG-03 |
| SES-02 | La sesión expira tras 2 horas de inactividad, o a los 30 días con "Mantener sesión iniciada". | [FS-USR-02](../modulos/usuarios/specs/FS-USR-02-inicio-sesion.md), RN-04 |
| SES-03 | El identificador de sesión se regenera al iniciar sesión, para evitar la fijación de sesión. | OWASP |
| SES-04 | Toda petición que modifica datos (`POST`, `PUT`, `PATCH`, `DELETE`) exige un token anti-CSRF además de la cookie. | RNF-SEG-05 |
| SES-05 | La API solo acepta peticiones del dominio del frontend (CORS restringido). | RNF-SEG-05 |
| SES-06 | El contador de intentos fallidos se lleva **por correo ingresado, exista o no la cuenta**. Así el bloqueo tampoco revela qué correos están registrados. | FS-USR-02, RN-02 y RN-03 |
| SES-07 | Además del bloqueo por cuenta, se limita el inicio de sesión **por IP**, para frenar a quien prueba muchos correos distintos. | RNF-SEG-07 |
| SES-08 | Cerrar sesión, cambiar o restablecer la contraseña, y suspender o desactivar la cuenta invalidan las sesiones en el servidor y cierran las conexiones en tiempo real abiertas. | FS-USR-03 RN-06, FS-USR-05 RN-05, FS-USR-08 RN-04 |
| SES-09 | Una cuenta **En eliminación** que inicia sesión dentro de los 30 días recibe una **sesión restringida**: solo puede llamar a `POST /cuenta/reactivar` y `DELETE /auth/sesion`. | [FS-USR-05](../modulos/usuarios/specs/FS-USR-05-configuracion-cuenta.md), RN-09 |
| SES-10 | Las conexiones en tiempo real (WebSocket) validan la cookie de sesión al conectarse, y cada usuario solo puede suscribirse a sus propios canales (sus notificaciones y sus conversaciones). | RNF-SEG-04 |

### Orden de los controles en cada petición

1. HTTPS (las peticiones HTTP se redirigen).
2. Límite de peticiones (por IP y, si hay sesión, por usuario).
3. Sesión válida y estado de la cuenta (SEC-05).
4. Token anti-CSRF en peticiones que modifican datos.
5. Permiso sobre el recurso (nivel de acceso de la tabla del endpoint).
6. Validación de los datos de entrada.

## 5. Endpoints públicos

Esta es la **lista completa** de lo que se puede llamar sin sesión. Todo lo demás está bloqueado para usuarios anónimos (SEC-01). Prefijo común: `/api/v1`.

| Método | Ruta | Uso | Protección adicional | Spec |
|---|---|---|---|---|
| POST | `/auth/registro` | Crear cuenta | Límite por IP. Dominio institucional obligatorio. | FS-USR-01 |
| POST | `/auth/verificacion` | Activar la cuenta con el token del correo | Token de un solo uso, 24 h | FS-USR-01 |
| POST | `/auth/verificacion/reenvio` | Reenviar el enlace de verificación | 3 por hora por correo | FS-USR-01 |
| POST | `/auth/sesion` | Iniciar sesión | 5 fallos → bloqueo 15 min (SES-06) y límite por IP (SES-07) | FS-USR-02 |
| POST | `/auth/recuperacion` | Pedir enlace de restablecimiento | 3 por hora por correo. Respuesta idéntica exista o no el correo. | FS-USR-03 |
| POST | `/auth/recuperacion/restablecer` | Guardar la nueva contraseña | Token de un solo uso, 1 h | FS-USR-03 |
| POST | `/cuenta/correo/confirmar` | Confirmar un cambio de correo | Token de un solo uso, 24 h | FS-USR-05 |
| GET | `/catalogos/programas` | Lista de programas para el registro | Solo lectura | FS-USR-01 |
| GET | `/categorias` | Categorías activas para el registro | Solo lectura, solo categorías activas | FS-USR-04 |
| GET | `/salud` | Comprobar que el servicio responde | No devuelve versiones ni datos internos | RNF-DIS |

**Nota sobre el registro:** el mensaje "Este correo ya está registrado" ([FS-USR-01](../modulos/usuarios/specs/FS-USR-01-registro.md), RN-02) revela que un correo existe. Es aceptable para la usabilidad del registro, pero por eso `/auth/registro` lleva límite por IP.

## 6. Endpoints que nunca se exponen a internet

| Qué | Por qué está bloqueado | Cómo se usa |
|---|---|---|
| Métricas y monitoreo (`/metrics`) | Revelan carga, rutas y errores internos. | Solo desde la red interna o la herramienta de monitoreo. |
| Documentación interactiva de la API (Swagger u OpenAPI) | Facilita el reconocimiento de la API a un atacante. | Activa en desarrollo y pruebas; desactivada en producción. |
| Consolas de administración de la base de datos, la caché o la cola | Acceso directo a los datos. | Solo el equipo de infraestructura, por VPN o bastión (RNF-PRI-04). |
| Consultas internas entre módulos: preferencias (FS-USR-04 RF-04), complementariedad (FS-USR-06 RF-06) y creación de notificaciones (FS-COM-02 RF-06) | Devuelven datos de otros usuarios sin filtrar privacidad. | Se llaman como funciones o servicios internos, nunca por HTTP público. |
| Tareas programadas: limpiar cuentas sin verificar, reactivar suspensiones, cerrar oportunidades, recordatorios de eventos y vencimiento de solicitudes | Cambian datos de muchos usuarios a la vez. | Se ejecutan desde el programador de tareas del servidor. |
| Asignar el rol de administrador | No existe en la aplicación ([FS-PLT-01](../modulos/plataforma/specs/FS-PLT-01-gestion-categorias.md), RN-01). | Directamente en la base de datos por el equipo técnico, con registro. |
| Leer mensajes privados como administrador | Prohibido ([FS-COM-01](../modulos/comunicacion/specs/FS-COM-01-mensajeria-privada.md), RN-11). | **No existe ningún endpoint para hacerlo.** |
| Módulo de servicios (`/servicios/**`) | Es de la fase 2. | Desactivado con un interruptor de configuración; responde `404`. |

## 7. Endpoints protegidos por módulo

**Convenciones:** todos exigen como mínimo el nivel **Autenticado**. La columna "Acceso" indica la condición adicional. Prefijo común: `/api/v1`.

### Cuenta y sesión — Sprints 1 y 2

| Método | Ruta | Acceso | Reglas | Spec |
|---|---|---|---|---|
| GET | `/auth/sesion` | Autenticado | Devuelve el usuario actual, su rol y a dónde redirigir. | FS-USR-02 |
| DELETE | `/auth/sesion` | Autenticado | Invalida la sesión en el servidor. | FS-USR-02 |
| GET | `/cuenta` | Dueño | Datos de configuración propios. | FS-USR-05 |
| PUT | `/cuenta/correo` | Dueño + contraseña actual | Solo dominio institucional. | FS-USR-05 |
| PUT | `/cuenta/contrasena` | Dueño + contraseña actual | Cierra las demás sesiones. | FS-USR-05 |
| PUT | `/cuenta/privacidad` | Dueño | Se aplica de inmediato. | FS-USR-05 |
| PUT | `/cuenta/notificaciones` | Dueño | Los correos de seguridad no se pueden desactivar. | FS-USR-05 |
| PUT | `/cuenta/intereses` | Dueño | Solo categorías activas. | FS-USR-04 |
| DELETE | `/cuenta/sesiones/otras` | Dueño | Cierra todas menos la actual. | FS-USR-05 |
| DELETE | `/cuenta` | Dueño + contraseña actual | Pasa a "En eliminación". | FS-USR-05 |
| POST | `/cuenta/reactivar` | Sesión restringida (SES-09) | Solo dentro de los 30 días. | FS-USR-05 |

### Perfil y búsqueda — Sprint 2

| Método | Ruta | Acceso | Reglas | Spec |
|---|---|---|---|---|
| GET | `/perfiles/{id}` | Autenticado | Si el perfil es "Solo mis conexiones" y no hay conexión, solo nombre, foto y programa (SEC-07). El responsable de una oportunidad ve completo el perfil de sus postulantes. | FS-USR-06, FS-COL-02 |
| PUT | `/perfiles/yo` | Dueño | — | FS-USR-06 |
| PUT | `/perfiles/yo/foto` | Dueño | Validación por contenido, máximo 5 MB (RNF-SEG-06). | FS-USR-06 |
| GET | `/etiquetas?q=` | Autenticado | Autocompletado. | FS-USR-06 |
| GET | `/perfiles?q=&filtros` | Autenticado | Las etiquetas de perfiles privados no se usan para buscar. | FS-RED-03 |
| GET | `/perfiles/yo/hoja-de-vida` | Dueño | No existe una ruta para pedir la hoja de vida de otro. | FS-USR-07 |

### Red y notificaciones — Sprint 3

| Método | Ruta | Acceso | Reglas | Spec |
|---|---|---|---|---|
| GET | `/conexiones` | Dueño | Solo las propias. | FS-RED-01 |
| DELETE | `/conexiones/{usuarioId}` | Relación: parte de la conexión | — | FS-RED-01 |
| GET | `/solicitudes?tipo=recibidas\|enviadas` | Dueño | — | FS-RED-01 |
| POST | `/solicitudes` | Autenticado | 30 por día. No a uno mismo ni a cuentas inactivas. Espera de 30 días tras un rechazo. | FS-RED-01 |
| POST | `/solicitudes/{id}/aceptar` · `/rechazar` | Relación: destinatario | — | FS-RED-01 |
| DELETE | `/solicitudes/{id}` | Relación: solicitante | — | FS-RED-01 |
| GET | `/onboarding/sugerencias` | Autenticado con onboarding pendiente | — | FS-RED-02 |
| POST | `/onboarding/completar` | Autenticado con onboarding pendiente | Las solicitudes enviadas aquí no cuentan en el límite diario. | FS-RED-02 |
| GET | `/notificaciones` · `/notificaciones/conteo` | Dueño | — | FS-COM-02 |
| POST | `/notificaciones/{id}/leida` · `/notificaciones/leidas` | Dueño | — | FS-COM-02 |

### Contenido — Sprint 4

| Método | Ruta | Acceso | Reglas | Spec |
|---|---|---|---|---|
| GET | `/feed` | Autenticado | Respeta la visibilidad de cada autor. | FS-CNT-01 |
| POST | `/publicaciones` | Autenticado | Palabras prohibidas. Adjuntos validados por contenido. | FS-CNT-01 |
| GET | `/publicaciones/{id}` | Relación: puede verla según la privacidad del autor | `404` si no puede (SEC-06). | FS-CNT-01 |
| PATCH | `/publicaciones/{id}` | Dueño (autor) | No se cambian los adjuntos. | FS-CNT-01 |
| DELETE | `/publicaciones/{id}` | Dueño (autor) | — | FS-CNT-01 |
| PUT · DELETE | `/publicaciones/{id}/reaccion` | Relación: puede ver la publicación | Una por usuario. | FS-CNT-01 |
| GET · POST | `/publicaciones/{id}/comentarios` | Relación: puede ver la publicación | Palabras prohibidas. | FS-CNT-01 |
| DELETE | `/comentarios/{id}` | Autor del comentario o de la publicación | — | FS-CNT-01 |
| GET | `/usuarios/{id}/publicaciones` | Autenticado | Respeta la visibilidad del autor. | FS-CNT-01 |
| GET | `/archivos/{id}` | Mismo permiso que el contenido que lo contiene | Enlaces firmados que vencen, servidos desde un dominio que no ejecuta código (RNF-SEG-06). | FS-CNT-01 |

### Mensajería — Sprint 5

| Método | Ruta | Acceso | Reglas | Spec |
|---|---|---|---|---|
| GET | `/conversaciones` | Dueño | Solo las propias. | FS-COM-01 |
| POST | `/conversaciones` | Relación: conexión o postulación aceptada | Una sola conversación por pareja. | FS-COM-01 |
| GET | `/conversaciones/{id}/mensajes` | Relación: participante | `404` si no participa (SEC-06). | FS-COM-01 |
| POST | `/conversaciones/{id}/mensajes` | Relación: participante | `409` si está en solo lectura. 60 por minuto. | FS-COM-01 |
| POST | `/conversaciones/{id}/leida` · `/ocultar` | Relación: participante | — | FS-COM-01 |
| WS | `/tiempo-real` | Autenticado | SES-10. | FS-COM-01, FS-COM-02 |

### Moderación y reportes — Sprint 5

| Método | Ruta | Acceso | Reglas | Spec |
|---|---|---|---|---|
| POST | `/reportes` | Autenticado | No el contenido propio. Una vez por elemento. | FS-CNT-02 |

### Administración — Sprints 4 y 5

Todo lo que está bajo `/admin/**` exige **Administrador**, y cada acción que modifica datos queda en el registro de auditoría (RNF-SEG-10).

| Método | Ruta | Reglas adicionales | Spec |
|---|---|---|---|
| GET · POST | `/admin/categorias` | — | FS-PLT-01 |
| PATCH | `/admin/categorias/{id}` | — | FS-PLT-01 |
| POST | `/admin/categorias/{id}/desactivar` · `/reactivar` | No se desactiva la última activa de un tipo. | FS-PLT-01 |
| PUT | `/admin/categorias/orden` | — | FS-PLT-01 |
| GET | `/admin/categorias/{id}/historial` | — | FS-PLT-01 |
| GET | `/admin/usuarios` · `/admin/usuarios/{id}` | — | FS-USR-08 |
| POST | `/admin/usuarios/{id}/suspender` · `/desactivar` · `/reactivar` | Nunca sobre sí mismo ni sobre otro administrador. No reactiva cuentas en eliminación. | FS-USR-08 |
| GET | `/admin/moderacion/cola` · `/historial` · `/publicaciones` | — | FS-CNT-02 |
| POST | `/admin/moderacion/{elementoId}/retirar` · `/mantener` | Norma incumplida y comentario obligatorios. | FS-CNT-02 |

### Oportunidades — Sprint 6

| Método | Ruta | Acceso | Reglas | Spec |
|---|---|---|---|---|
| GET | `/oportunidades` · `/oportunidades/{id}` | Autenticado | — | FS-COL-01 |
| POST | `/oportunidades` | Autenticado | Pendiente de [P-36](../preguntas-abiertas.md#sprint-6--oportunidades): quién puede publicar. | FS-COL-01 |
| GET | `/oportunidades/mias` | Dueño | — | FS-COL-01 |
| PATCH · DELETE | `/oportunidades/{id}` | Relación: responsable | Eliminar solo sin postulaciones. | FS-COL-01 |
| POST | `/oportunidades/{id}/cerrar` · `/cancelar` | Relación: responsable | — | FS-COL-01 |
| GET | `/oportunidades/{id}/postulaciones` | Relación: responsable | — | FS-COL-01 |
| PATCH | `/postulaciones/estado` | Relación: responsable de todas las postulaciones enviadas | Cambio en lote. Transiciones válidas. | FS-COL-01 |
| POST | `/oportunidades/{id}/postulaciones` | Autenticado, no responsable | Solo si está abierta. Una por oportunidad. | FS-COL-02 |
| GET | `/postulaciones/mias` | Dueño | — | FS-COL-02 |
| GET | `/postulaciones/{id}` | Relación: postulante o responsable | — | FS-COL-02 |
| POST | `/postulaciones/{id}/retirar` | Relación: postulante | Solo "Enviada" o "En revisión". | FS-COL-02 |

### Eventos — Sprint 7

| Método | Ruta | Acceso | Reglas | Spec |
|---|---|---|---|---|
| GET | `/eventos` · `/eventos/{id}` | Autenticado | El enlace virtual solo se envía al organizador y a los confirmados (SEC-07). | FS-COL-03 |
| POST | `/eventos` | Autenticado | — | FS-COL-03 |
| PATCH · DELETE | `/eventos/{id}` | Relación: organizador | Eliminar solo sin asistentes. | FS-COL-03 |
| POST | `/eventos/{id}/cancelar` | Relación: organizador | — | FS-COL-03 |
| PUT · DELETE | `/eventos/{id}/asistencia` | Autenticado, no organizador | Solo antes de que comience. Respeta el cupo. | FS-COL-04 |
| GET | `/eventos/{id}/asistentes` | Relación: organizador o confirmado | Los demás solo reciben el número. | FS-COL-04 |
| GET | `/eventos/{id}/asistentes.csv` | Relación: organizador | Sin correos ni datos personales. | FS-COL-04 |
| GET | `/eventos/{id}/calendario.ics` | Relación: organizador o confirmado | Incluye el enlace virtual. | FS-COL-04 |

### Proyectos — Sprint 8

| Método | Ruta | Acceso | Reglas | Spec |
|---|---|---|---|---|
| GET | `/proyectos` · `/proyectos/{id}` · `/proyectos/{id}/miembros` | Autenticado | Los no miembros solo ven Resumen y Miembros. | FS-COL-05 |
| POST | `/proyectos` | Autenticado | — | FS-COL-05 |
| PATCH | `/proyectos/{id}` | Rol: Administrador del proyecto | — | FS-COL-05 |
| POST | `/proyectos/{id}/finalizar` · PUT `/proyectos/{id}/reclutamiento` | Rol: Administrador del proyecto | — | FS-COL-05 |
| DELETE | `/proyectos/{id}` | Creador, y solo si es el único miembro | — | FS-COL-05 |
| GET | `/proyectos/{id}/tareas` · `/actividad` | Rol: cualquier miembro | `404` para no miembros. | FS-COL-05 |
| POST | `/proyectos/{id}/tareas` | Rol: Editor o Administrador | — | FS-COL-06 |
| PATCH | `/tareas/{id}` | Rol: Editor o Administrador. El Visualizador solo cambia el estado de sus tareas asignadas. | — | FS-COL-06 |
| DELETE | `/tareas/{id}` | Rol: Editor (solo las que creó) o Administrador (cualquiera) | — | FS-COL-06 |
| POST | `/proyectos/{id}/solicitudes` | Autenticado, no miembro | Solo si está reclutando y con cupo. Espera de 30 días tras un rechazo. | FS-COL-05 |
| POST | `/proyectos/{id}/solicitudes/{sid}/aprobar` · `/rechazar` | Rol: Administrador del proyecto | — | FS-COL-05 |
| POST | `/proyectos/{id}/invitaciones` | Rol: Administrador del proyecto | Solo a sus conexiones. | FS-COL-05 |
| POST | `/invitaciones/{id}/aceptar` · `/rechazar` | Relación: invitado | Vencen a los 14 días. | FS-COL-05 |
| PATCH | `/proyectos/{id}/miembros/{usuarioId}/rol` | Rol: Administrador del proyecto | Protección del último administrador y del creador. | FS-COL-06 |
| DELETE | `/proyectos/{id}/miembros/{usuarioId}` | Rol: Administrador del proyecto | Igual que el anterior. | FS-COL-06 |
| DELETE | `/proyectos/{id}/miembros/yo` | Rol: cualquier miembro | No si es el único administrador. | FS-COL-05 |

En un proyecto **Finalizado**, todo endpoint que modifica datos responde `409` ([FS-COL-05](../modulos/colaboracion/specs/FS-COL-05-espacios-proyectos.md), RN-06).

## 8. Límites de peticiones

| Endpoint | Límite | Al superarlo | Origen |
|---|---|---|---|
| `POST /auth/sesion` | 5 fallos seguidos por correo → bloqueo de 15 min | `429` con el tiempo restante | FS-USR-02, RN-02 |
| `POST /auth/sesion` | 20 intentos cada 15 min por IP _(propuesto)_ | `429` | SES-07 |
| `POST /auth/registro` | 10 por hora por IP _(propuesto)_ | `429` | Sección 5 |
| `POST /auth/verificacion/reenvio` | 3 por hora por correo | `429` | FS-USR-01, RN-06 |
| `POST /auth/recuperacion` | 3 por hora por correo | Misma respuesta que un envío exitoso (FS-USR-03, RN-03) | FS-USR-03, RN-04 |
| `POST /solicitudes` | 30 por día por usuario | `429` | FS-RED-01, RN-05 |
| `POST /conversaciones/{id}/mensajes` | 60 por minuto por usuario | `429` | FS-COM-01, RN-09 |
| Cualquier otro endpoint | 100 por minuto por usuario | `429` | RNF-SEG-07 |

## 9. Códigos de respuesta

| Código | Cuándo |
|---|---|
| `400` | Datos inválidos o token vencido. |
| `401` | No hay sesión o expiró. El frontend lleva al inicio de sesión y luego regresa a la página ([FS-USR-02](../modulos/usuarios/specs/FS-USR-02-inicio-sesion.md), RF-08). |
| `403` | Hay sesión, pero la cuenta no está activa o el usuario no tiene el rol para una acción sobre un recurso que sí puede ver. |
| `404` | El recurso no existe **o** el usuario no puede saber que existe (SEC-06). |
| `409` | La acción choca con el estado actual: conversación en solo lectura, proyecto finalizado, oportunidad cerrada. |
| `429` | Se superó un límite de la sección 8. |

Los mensajes de error nunca incluyen trazas, consultas SQL ni datos internos.

## 10. Cómo se verifica

- **Prueba de acceso por endpoint:** cada endpoint de la sección 7 tiene al menos tres pruebas automatizadas: sin sesión (`401`), con un usuario sin permiso (`403` o `404`) y con un usuario con permiso (éxito). Es parte de la [Definition of Done](../sprints/README.md#definition-of-done-un-spec-está-terminado).
- **Prueba de lista blanca:** una prueba recorre todas las rutas registradas en el servidor y falla si alguna responde sin sesión y no está en la sección 5.
- **Escaneo automático** de seguridad antes de cada salida a producción (RNF-SEG-05).

## 11. Preguntas abiertas

Las preguntas viven en el [consolidado](../preguntas-abiertas.md#c-técnicas):

- P-62 — ¿los límites por IP de la sección 8 son adecuados?
- P-63 — ¿inicio de sesión con la cuenta institucional (SSO) en lugar de contraseña propia?
- P-64 — ¿segunda verificación para los administradores de la plataforma?

## 12. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-08 | Gamero | Creación |
| 2026-10-27 | Gamero | Códigos y enlaces llevados a la estructura por módulos; nota sobre las rutas de `contracts/api/`; preguntas trasladadas al consolidado (P-62 a P-64). |
