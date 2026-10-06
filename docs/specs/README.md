# Especificaciones funcionales — UniLink

Cada spec detalla el comportamiento de uno o varios casos de uso de un mismo módulo. Usa la [plantilla](./_plantilla-spec.md) para crear uno nuevo.

## Convenciones

- **Nombre de archivo:** `FS-<MOD>-NN-<nombre-corto>.md`, dentro de la carpeta de su módulo.
- **IDs internos:** las reglas (`RN-NN`), requisitos (`RF-NN`) y mensajes (`MSG-NN`) se numeran dentro de cada spec. Para citarlos desde otro documento se usa `FS-CTA-01/RF-03`.
- **Estados del spec:**

| Estado | Significado |
|---|---|
| Pendiente | Planificado; el archivo aún no existe. |
| Borrador | En redacción. |
| En revisión | Listo para que el equipo lo revise. |
| Aprobado | Cumple la _Definition of Ready_; puede entrar a un sprint. |
| En desarrollo | Se está implementando en el sprint actual. |
| Implementado | Cumple la _Definition of Done_. |

## Módulos

| Código | Módulo | Carpeta |
|---|---|---|
| CTA | Cuenta y acceso | [`cuenta/`](./cuenta/) |
| PRF | Perfil y búsqueda | [`perfil/`](./perfil/) |
| RED | Red de conexiones | [`red/`](./red/) |
| NOT | Notificaciones | [`notificaciones/`](./notificaciones/) |
| CNT | Contenido | [`contenido/`](./contenido/) |
| MSG | Mensajería | [`mensajeria/`](./mensajeria/) |
| ADM | Administración | [`administracion/`](./administracion/) |
| OPO | Oportunidades | [`oportunidades/`](./oportunidades/) |
| EVT | Eventos | [`eventos/`](./eventos/) |
| PRY | Proyectos | `proyectos/` |
| SRV | Servicios | `servicios/` |

## Índice y trazabilidad

| Spec | Nombre | Casos de uso | Historias | Sprint | Estado |
|---|---|---|---|---|---|
| [FS-CTA-01](./cuenta/FS-CTA-01-registro.md) | Registro y verificación de cuenta | CU-01 | HU-01 | 1 | Borrador |
| [FS-CTA-02](./cuenta/FS-CTA-02-inicio-sesion.md) | Inicio y cierre de sesión | CU-02 | HU-02 | 1 | Borrador |
| [FS-CTA-03](./cuenta/FS-CTA-03-recuperar-contrasena.md) | Recuperación de contraseña | CU-17 | HU-28 | 1 | Borrador |
| [FS-CTA-04](./cuenta/FS-CTA-04-preferencias-contenido.md) | Preferencias de contenido | CU-18 | HU-14 | 1 | Borrador |
| [FS-CTA-05](./cuenta/FS-CTA-05-configuracion-cuenta.md) | Configuración de cuenta y privacidad | CU-03 | HU-03 | 2 | Borrador |
| [FS-PRF-01](./perfil/FS-PRF-01-perfil-profesional.md) | Perfil profesional (incluye "Puedo aportar / Necesito") | CU-04 | HU-04 | 2 | Borrador |
| [FS-PRF-02](./perfil/FS-PRF-02-busqueda-perfiles.md) | Búsqueda de perfiles | CU-05 | HU-05 | 2 | Borrador |
| [FS-PRF-03](./perfil/FS-PRF-03-hoja-de-vida-pdf.md) | Hoja de vida en PDF | CU-19 | HU-13 | 2 | Borrador |
| [FS-RED-01](./red/FS-RED-01-solicitudes-conexion.md) | Solicitudes de conexión | CU-06, CU-07 | HU-06, HU-07 | 3 | Borrador |
| [FS-RED-02](./red/FS-RED-02-onboarding-sugerencias.md) | Onboarding y sugerencias | CU-13 | HU-24 | 3 | Borrador |
| [FS-NOT-01](./notificaciones/FS-NOT-01-centro-notificaciones.md) | Centro de notificaciones | CU-23 | HU-30 | 3 | Borrador |
| [FS-CNT-01](./contenido/FS-CNT-01-publicaciones-feed.md) | Publicaciones y feed | CU-08, CU-09 | HU-08, HU-09 | 4 | Borrador |
| [FS-ADM-01](./administracion/FS-ADM-01-gestion-categorias.md) | Gestión de categorías | CU-26 | HU-20 | 4 | Borrador |
| [FS-MSG-01](./mensajeria/FS-MSG-01-mensajeria-privada.md) | Mensajería privada | CU-10 | HU-10 | 5 | Borrador |
| [FS-ADM-02](./administracion/FS-ADM-02-gestion-cuentas.md) | Gestión de cuentas de usuario | CU-24 | HU-17 | 5 | Borrador |
| [FS-ADM-03](./administracion/FS-ADM-03-moderacion-contenido.md) | Moderación de contenido | CU-25 | HU-18, HU-19 | 5 | Borrador |
| [FS-OPO-01](./oportunidades/FS-OPO-01-publicacion-oportunidades.md) | Publicación de oportunidades | CU-22 | HU-29 | 6 | Borrador |
| [FS-OPO-02](./oportunidades/FS-OPO-02-postulaciones.md) | Postulaciones | CU-12, CU-14 | HU-12, HU-25 | 6 | Borrador |
| [FS-EVT-01](./eventos/FS-EVT-01-publicacion-listado-eventos.md) | Publicación y listado de eventos | CU-20, CU-21 | HU-15, HU-16 | 7 | Borrador |
| [FS-EVT-02](./eventos/FS-EVT-02-confirmacion-asistencia.md) | Confirmación de asistencia (RSVP) | CU-15 | HU-26 | 7 | Borrador |
| FS-PRY-01 | Espacios de proyectos | CU-11 | HU-11 | 8 | Pendiente |
| FS-PRY-02 | Roles en proyectos | CU-16 | HU-27 | 8 | Pendiente |
| FS-SRV-01 | Verificación de credenciales | CU-27 | HU-21 | 9 | Pendiente |
| FS-SRV-02 | Publicación y solicitud de servicios | CU-28, CU-30 | HU-22, HU-31 | 9 | Pendiente |
| FS-SRV-03 | Registro de oferentes externos | CU-29 | HU-23 | 9 | Pendiente |

Los 30 casos de uso quedan cubiertos por 25 specs.
