# Módulos — UniLink

_MVP — Red Profesional Universitaria — Universidad del Magdalena_
_Centro de Interés de Desarrollo Tecnológico e Innovación (CIDTI)_

La documentación funcional se organiza por **módulo**. Cada carpeta reúne su README, sus casos de uso, sus historias de usuario y sus specs. El sprint de cada spec vive solo en el [roadmap](../sprints/README.md).

## Mapa de módulos

| Código | Módulo | Carpeta | Propósito |
|---|---|---|---|
| USR | Usuarios | [`usuarios/`](./usuarios/) | La persona: cuenta, sesión, configuración, preferencias, perfil, hoja de vida y gestión de cuentas. |
| RED | Red | [`red/`](./red/) | Las relaciones y el descubrimiento: conexiones, onboarding y sugerencias, y búsqueda de perfiles. |
| CNT | Contenido | [`contenido/`](./contenido/) | Publicaciones, feed y moderación de contenido. |
| COM | Comunicación | [`comunicacion/`](./comunicacion/) | Mensajería privada y notificaciones. |
| COL | Colaboración | [`colaboracion/`](./colaboracion/) | Oportunidades, eventos y proyectos: publicaciones con responsable, cupo y participantes. |
| PLT | Plataforma | [`plataforma/`](./plataforma/) | Categorías, panel de administración y registro de auditoría. |
| SRV | Servicios (fase 2) | [`servicios/`](./servicios/) | Servicios académicos y no académicos, credenciales verificadas y oferentes externos. Fuera del MVP. |

Regla de dependencia: Red usa a Usuarios; Usuarios nunca usa a Red.

## Convenciones

- **Nombre de archivo:** `FS-<MOD>-NN-<nombre-corto>.md`, dentro de `<modulo>/specs/`. Usa la [plantilla](./_plantilla-spec.md).
- **IDs internos:** las reglas (`RN-NN`), requisitos (`RF-NN`) y mensajes (`MSG-NN`) se numeran dentro de cada spec. Desde otro documento se citan como `USR-01/RF-03`.
- **Casos de uso e historias** conservan su número global (CU-01…30, HU-01…31).

| Estado | Significado |
|---|---|
| Pendiente | Planificado; el archivo aún no existe. |
| Borrador | En redacción. |
| En revisión | Listo para que el equipo lo revise. |
| Aprobado | Cumple la _Definition of Ready_; puede entrar a un sprint. |
| En desarrollo | Se está implementando en el sprint actual. |
| Implementado | Cumple la _Definition of Done_. |

## Índice de specs

| Spec | Nombre | Casos de uso | Historias | Estado |
|---|---|---|---|---|
| [FS-USR-01](./usuarios/specs/FS-USR-01-registro.md) | Registro y verificación de cuenta | CU-01 | HU-01 | Borrador |
| [FS-USR-02](./usuarios/specs/FS-USR-02-inicio-sesion.md) | Inicio y cierre de sesión | CU-02 | HU-02 | Borrador |
| [FS-USR-03](./usuarios/specs/FS-USR-03-recuperar-contrasena.md) | Recuperación de contraseña | CU-17 | HU-28 | Borrador |
| [FS-USR-04](./usuarios/specs/FS-USR-04-preferencias-contenido.md) | Preferencias de contenido | CU-18 | HU-14 | Borrador |
| [FS-USR-05](./usuarios/specs/FS-USR-05-configuracion-cuenta.md) | Configuración de cuenta y privacidad | CU-03 | HU-03 | Borrador |
| [FS-USR-06](./usuarios/specs/FS-USR-06-perfil-profesional.md) | Perfil profesional (incluye "Puedo aportar / Necesito") | CU-04 | HU-04 | Borrador |
| [FS-RED-03](./red/specs/FS-RED-03-busqueda-perfiles.md) | Búsqueda de perfiles | CU-05 | HU-05 | Borrador |
| [FS-USR-07](./usuarios/specs/FS-USR-07-hoja-de-vida-pdf.md) | Hoja de vida en PDF | CU-19 | HU-13 | Borrador |
| [FS-RED-01](./red/specs/FS-RED-01-solicitudes-conexion.md) | Solicitudes de conexión | CU-06, CU-07 | HU-06, HU-07 | Borrador |
| [FS-RED-02](./red/specs/FS-RED-02-onboarding-sugerencias.md) | Onboarding y sugerencias | CU-13 | HU-24 | Borrador |
| [FS-COM-02](./comunicacion/specs/FS-COM-02-centro-notificaciones.md) | Centro de notificaciones | CU-23 | HU-30 | Borrador |
| [FS-CNT-01](./contenido/specs/FS-CNT-01-publicaciones-feed.md) | Publicaciones y feed | CU-08, CU-09 | HU-08, HU-09 | Borrador |
| [FS-PLT-01](./plataforma/specs/FS-PLT-01-gestion-categorias.md) | Gestión de categorías | CU-26 | HU-20 | Borrador |
| [FS-COM-01](./comunicacion/specs/FS-COM-01-mensajeria-privada.md) | Mensajería privada | CU-10 | HU-10 | Borrador |
| [FS-USR-08](./usuarios/specs/FS-USR-08-gestion-cuentas.md) | Gestión de cuentas de usuario | CU-24 | HU-17 | Borrador |
| [FS-CNT-02](./contenido/specs/FS-CNT-02-moderacion-contenido.md) | Moderación de contenido | CU-25 | HU-18, HU-19 | Borrador |
| [FS-COL-01](./colaboracion/specs/FS-COL-01-publicacion-oportunidades.md) | Publicación de oportunidades | CU-22 | HU-29 | Borrador |
| [FS-COL-02](./colaboracion/specs/FS-COL-02-postulaciones.md) | Postulaciones | CU-12, CU-14 | HU-12, HU-25 | Borrador |
| [FS-COL-03](./colaboracion/specs/FS-COL-03-publicacion-listado-eventos.md) | Publicación y listado de eventos | CU-20, CU-21 | HU-15, HU-16 | Borrador |
| [FS-COL-04](./colaboracion/specs/FS-COL-04-confirmacion-asistencia.md) | Confirmación de asistencia (RSVP) | CU-15 | HU-26 | Borrador |
| [FS-COL-05](./colaboracion/specs/FS-COL-05-espacios-proyectos.md) | Espacios de proyectos | CU-11 | HU-11 | Borrador |
| [FS-COL-06](./colaboracion/specs/FS-COL-06-roles-proyectos.md) | Roles en proyectos | CU-16 | HU-27 | Borrador |
| FS-SRV-01 | Verificación de credenciales | CU-27 | HU-21 | Pendiente |
| FS-SRV-02 | Publicación y solicitud de servicios | CU-28, CU-30 | HU-22, HU-31 | Pendiente |
| FS-SRV-03 | Registro de oferentes externos | CU-29 | HU-23 | Pendiente |

## Equivalencias con los códigos anteriores

Los specs se renumeraron el 2026-10-24 al reorganizar la documentación por módulos ([decisión](../decisiones/2026-10-24-reestructuracion-docs.md)).

| Antes | Ahora |
|---|---|
| FS-CTA-01 | FS-USR-01 |
| FS-CTA-02 | FS-USR-02 |
| FS-CTA-03 | FS-USR-03 |
| FS-CTA-04 | FS-USR-04 |
| FS-CTA-05 | FS-USR-05 |
| FS-PRF-01 | FS-USR-06 |
| FS-PRF-03 | FS-USR-07 |
| FS-ADM-02 | FS-USR-08 |
| FS-RED-01 | FS-RED-01 |
| FS-RED-02 | FS-RED-02 |
| FS-PRF-02 | FS-RED-03 |
| FS-CNT-01 | FS-CNT-01 |
| FS-ADM-03 | FS-CNT-02 |
| FS-MSG-01 | FS-COM-01 |
| FS-NOT-01 | FS-COM-02 |
| FS-OPO-01 | FS-COL-01 |
| FS-OPO-02 | FS-COL-02 |
| FS-EVT-01 | FS-COL-03 |
| FS-EVT-02 | FS-COL-04 |
| FS-PRY-01 | FS-COL-05 |
| FS-PRY-02 | FS-COL-06 |
| FS-ADM-01 | FS-PLT-01 |

## Actores

| Actor | Descripción |
|---|---|
| **Visitante** | Persona no autenticada que puede registrarse en la plataforma. |
| **Usuario autenticado** | Estudiante, profesor o personal administrativo con cuenta activa y verificada. Desde la fase 2, también egresados y personal tercerizado. |
| **Responsable de oportunidad** | Usuario autenticado que publica una oportunidad (investigación, proyecto o voluntariado) y gestiona sus postulaciones. |
| **Administrador de proyecto** | Usuario autenticado que creó un espacio de proyecto o recibió el rol de administrador en él. |
| **Administrador de la plataforma** | Miembro del equipo de UniLink encargado de gestionar cuentas, moderar contenido, administrar categorías y validar credenciales. |
