# Reunión de decisiones: preguntas abiertas — UniLink

_Fecha: 2026-10-19_

Reunión del equipo para cerrar las [preguntas abiertas](../preguntas-abiertas.md) de la especificación. El estado de cada pregunta quedó anotado en el consolidado y en su documento de origen.

## Asistentes

- Andrés Felipe Gamero
- Luis Fernando Barraza
- Alfonso Salazar
- Andrés Manuel Rudas
- Samuel Ospino
- Luis Javier Saumeth
- Vianney Álvarez
- Camila Flórez

## Decisiones

### Resueltas

| Tema | Decisión | Preguntas |
|---|---|---|
| Usuarios simultáneos | Dimensionar para ~1.000 usuarios simultáneos (picos en convocatorias de monitores), con holgura el primer año. | P-01 |
| Alojamiento | Infraestructura propia de la Universidad, servidor activo 24/7. | P-02 |
| Base de datos | Propia y desacoplada de la institucional; solo se comparte la autenticación (token del Campus Virtual). | P-02 |
| Datos institucionales | Solo correo institucional, nombre, facultad/programa y estado de monitor. El resto lo completa el usuario. | — |
| Creación de cuentas | Cuentas precreadas (modelo Microsoft Teams); el usuario solo activa y personaliza la suya. | — |
| Cuentas externas | Permitidas con registro propio; cada proyecto decide si admite externos. | — |
| Estado "monitor académico" | Se actualiza en lote al publicarse el listado oficial de Vicerrectoría Académica, aunque la cuenta no esté activada. | — |
| Integración API de admisiones en el MVP | Se simula (mock con correos ficticios); la integración real va en el producto final. | — |
| Secciones | Personas (filtro monitor + área + especialización), Proyectos (subtipo investigación/desarrollo/creación como filtro; un semillero tiene varios proyectos; categorías generales, no "de clase"), Eventos (solo públicos), más una vista personal "Yo" (conexiones, proyectos propios, actividades privadas). | — |
| Lugar de eventos | Campo informativo; sin reserva de espacios. | P-09 |
| Próximos eventos en el feed | Sí se muestran. | P-39 |
| Bloqueo por intentos fallidos | Bloqueo temporal y recuperación de contraseña; sin correo por cada bloqueo (se puede avisar de un inicio de sesión nuevo). | P-21 |
| Fusionar o eliminar etiquetas | No aplica: las etiquetas son predefinidas. | P-25 |
| Palabras prohibidas | Las mantiene el Administrador, no el equipo. | P-29 |
| Cuentas eliminadas | Borrado lógico: la cuenta y todo lo asociado se ocultan, con trazabilidad (quién y cuándo). | P-23 (y P-12, por gestionar) |
| Solicitudes de conexión | Sin vencimiento. | — (FS-RED-01 RN-08) |
| Bloquear o reportar usuarios | Sí; el Administrador verifica y decide. | P-27, P-32 |
| Umbral de 5 reportes | El contenido se bloquea, no solo se oculta. | P-35 |
| Perfiles semilla | No; el feed muestra perfiles afines. | P-28 |
| Reacciones | Una sola ("Me gusta"). | P-31 |
| Quién publica oportunidades | Cualquier usuario, con moderación. | P-36 |
| Mensaje del organizador a los asistentes | Sí. | P-41 |
| Proyectos privados | Sí. | P-43 |
| Rol por defecto de no miembros | Configurable; el creador del proyecto define los roles. | P-44 |
| Credenciales en el PDF del perfil | Solo las verificadas por la plataforma. | P-48 |
| Adjuntos en mensajes | Sí (condicionado a la mensajería). | P-47 |
| Roles | Administrador (control total, debe ser personal de la Universidad) y Moderador (reportes, bloqueos, contenido y lenguaje). El equipo de desarrollo no administra la plataforma. | P-07, P-49 |
| Relevancia | Priorizar por vistas; el cruce debe reconocer etiquetas similares, no solo idénticas. | P-46 |

### Resueltas – fuera del MVP

| Tema | Decisión | Preguntas |
|---|---|---|
| Chat de equipo dentro del proyecto | Para una versión posterior. | P-42 |
| Registro interno de grupos (actas, grabaciones, avances) | Para una versión posterior. | P-42 |
| Apelaciones | Se gestionan por soporte, no dentro de la plataforma. | P-33 |
| Sugerencias por afinidad como notificación | Para una versión posterior. | P-37 |
| Lista de espera en eventos | No. | P-40 |
| Servicios entre estudiantes / preferencias de contenido de servicios | Fase 2 (la Fase 1 es institucional). | P-20 |
| Ruta institucional de atención | Para una versión posterior (a lo sumo, un enlace de contacto). | P-08 |
| Términos y condiciones / Oficina Jurídica | Obligatorio antes de producción, no para el prototipo. | P-11 |

## Pendientes

| Tema | Estado | Pregunta |
|---|---|---|
| Mensajería privada | Hoy está en prioridad **Alta** y no se cambia. Se propuso empezar con contacto directo y evaluar el chat después. En revisión. | P-56 |
| Notificaciones | Tiempo real (WebSocket/SSE) o consulta al iniciar sesión / periódica. | P-16 |
| Evento vs. reunión | Falta una definición formal. | P-57 |
| Motor de búsqueda | Mecanismo por definir (búsqueda tolerante; Alfonso propone SQL optimizado). | P-17 |
| Horario de soporte y SLA de 99,5 % | Sin cerrar. | P-18 |
| Vencimiento de solicitudes a proyectos | Propuesta de 30 días. | P-58 |
| Categorías semilla | Por revisar. | P-19 |
| Alcance del módulo de oportunidades | Por revisar. | P-59 |
| Dominio | Pendiente. | P-60 |
| Confirmación del stack | Pendiente. | P-53 |

### Por gestionar

| Tema | Con quién | Pregunta |
|---|---|---|
| Acceso a la API de admisiones (endpoint GET) | Universidad | P-61 |
| Borrado lógico frente al derecho de supresión de la Ley 1581 de 2012 | Oficina Jurídica | P-12 |

## Responsables

| Frente | Personas |
|---|---|
| Coordinación y specs | Gamero, Alfonso, Vianney |
| Backend | Luis Fernando y Alfonso (líderes), Samuel y Luis Javier |
| Frontend | Andrés Manuel Rudas (líder), José Granado, Vianney y Camila |

## Fechas

| Fecha | Hito |
|---|---|
| 2026-10-20 | Presentación al profesor Juan Manuel Rodríguez |
| 2026-10-24 (mañana) | Arranque del frontend |
| 2026-10-26 (aprox.) | Specs de backend |

## Documentos actualizados

Las decisiones se registraron el 2026-10-27 en la estructura por módulos (rama `informe/analisis-integral`):

- [Preguntas abiertas](../preguntas-abiertas.md): estado de cada pregunta y grupo F (P-56 a P-61). En una versión anterior de este documento, en la rama `documentacion`, esas preguntas se numeraban P-50 a P-56; la confirmación del stack corresponde a P-53.
- [Registro de decisiones](../arquitectura/Registro_Decisiones.md): ADR-009 (alojamiento) aceptada y ADR nuevas derivadas de la reunión.
- [SRS](../srs/Especificacion_Requisitos.md): supuesto de usuarios simultáneos.
- Los specs **todavía no** reflejan las decisiones. La lista de cambios pendientes por spec está en [riesgos y brechas](../riesgos_y_brechas_unilink.md).
