# Registro de decisiones arquitectónicas (ADR) — UniLink

_MVP — Red Profesional Universitaria — Universidad del Magdalena_
_Centro de Interés de Desarrollo Tecnológico e Innovación (CIDTI)_

Cada decisión que afecta la estructura del sistema queda registrada aquí con su contexto, las alternativas consideradas, la decisión y sus consecuencias. Una decisión no se borra: si cambia, se marca como **Reemplazada** y se escribe una nueva.

| Estado | Significado |
|---|---|
| Propuesta | Hay opciones evaluadas, pero el equipo aún no decide; se indica qué pregunta la bloquea. |
| Aceptada | El equipo la adoptó; los documentos y el código la siguen. |
| Reemplazada | La sustituye otra ADR, que se enlaza. |

## Índice

| ADR | Tema | Estado |
|---|---|---|
| [ADR-001](#adr-001-metodología-de-desarrollo) | Metodología de desarrollo | Aceptada |
| [ADR-002](#adr-002-estilo-arquitectónico) | Estilo arquitectónico | Aceptada |
| [ADR-003](#adr-003-límites-de-los-módulos-y-dependencias-permitidas) | Límites de los módulos y dependencias permitidas | Aceptada |
| [ADR-004](#adr-004-comunicación-entre-módulos) | Comunicación entre módulos | Aceptada |
| [ADR-005](#adr-005-persistencia) | Persistencia | Propuesta |
| [ADR-006](#adr-006-contratos-antes-que-el-código) | Contratos antes que el código | Aceptada |
| [ADR-007](#adr-007-tiempo-real) | Tiempo real | Propuesta (P-16) |
| [ADR-008](#adr-008-búsqueda-de-texto) | Búsqueda de texto | Propuesta (P-17) |
| [ADR-009](#adr-009-alojamiento) | Alojamiento | Propuesta (P-02) |
| [ADR-010](#adr-010-lenguaje-y-framework) | Lenguaje y framework | Propuesta (P-53) |
| [ADR-011](#adr-011-tareas-en-segundo-plano-y-programadas) | Tareas en segundo plano y programadas | Propuesta |
| [ADR-012](#adr-012-almacenamiento-de-archivos) | Almacenamiento de archivos | Propuesta |

---

## ADR-001: Metodología de desarrollo

**Estado:** Aceptada.

**Contexto.** El equipo es pequeño, trabaja por semestres y necesita entregar un MVP en unas 16 semanas con requisitos que todavía tienen preguntas abiertas.

**Alternativas.** Cascada (todo especificado antes de programar); Kanban continuo; Scrum con sprints cortos guiado por specs.

**Decisión.** Scrum con sprints de 2 semanas ([roadmap](../sprints/README.md)) **guiado por specs**: ningún spec entra a un sprint sin cumplir la _Definition of Ready_ y su lista de revisión, y ninguno se cierra sin la _Definition of Done_.

**Consecuencias.** Las preguntas abiertas se resuelven en el refinamiento del sprint anterior; los specs son la fuente de verdad del comportamiento y se actualizan en el mismo pull request que lo cambia (RNF-MAN-06).

## ADR-002: Estilo arquitectónico

**Estado:** Aceptada.

**Contexto.** Restricciones de equipo, plazo, carga, disponibilidad y presupuesto descritas en la [comparación de alternativas](./Comparacion_Alternativas.md).

**Alternativas.** Monolito en capas (3,75); monolito modular (4,15); microservicios (2,75).

**Decisión.** **Monolito modular**: una aplicación y un despliegue, con seis módulos de dominio que solo se comunican por contratos.

**Consecuencias.** Operación sencilla y transacciones locales. Hay que vigilar las fronteras entre módulos (ADR-003, RNF-MAN-07). Un módulo puede separarse después sin cambiar sus contratos.

## ADR-003: Límites de los módulos y dependencias permitidas

**Estado:** Aceptada.

**Contexto.** Un monolito modular solo conserva su valor si las fronteras se respetan y no hay ciclos: con un ciclo, dos módulos ya no se pueden entender ni separar por su cuenta.

**Decisión.**

1. Seis módulos, cada uno dueño exclusivo de sus datos: Usuarios, Red, Contenido, Comunicación, Colaboración y Plataforma ([mapa](../modulos/README.md)).
2. Un módulo usa a otro solo por su interfaz pública ([`contracts/modulos/`](../../contracts/modulos/)) o reaccionando a sus eventos ([`contracts/eventos/`](../../contracts/eventos/README.md)). Nunca lee ni escribe tablas ajenas.
3. **Dependencias permitidas** (quién usa la interfaz de quién), sin ciclos:

| Módulo | Usa a | Para |
|---|---|---|
| Plataforma | — | — |
| Usuarios | Plataforma | Categorías activas (preferencias). |
| Red | Usuarios | Estado de la cuenta, datos públicos y privacidad del perfil, etiquetas, marcar el onboarding como completado. |
| Contenido | Usuarios, Red, Plataforma | Autor y estado de la cuenta; qué ve un observador; categorías y palabras prohibidas. |
| Colaboración | Usuarios, Red, Plataforma | Afinidad y estado de la cuenta; conexiones para invitar; categorías y palabras prohibidas. |
| Comunicación | Usuarios, Red, Colaboración | Correo y preferencias del destinatario; si dos usuarios pueden conversar. |

4. **Paquete de contratos.** Las interfaces públicas, los esquemas de eventos, el contrato `Reportable` y el **contexto de la petición** (usuario autenticado y sus roles, que resuelve la sesión de Usuarios) forman un paquete que cualquier módulo puede usar sin que cuente como dependencia. No tiene lógica.
5. **Pantallas que reúnen datos de varios módulos** (por ejemplo, el detalle de una cuenta en administración, con sus conexiones y su contenido retirado) consultan a cada módulo desde la capa de API; los módulos no se consultan entre sí para eso.

**Consecuencias.** Usuarios nunca depende de Red, Contenido ni Colaboración. La regla se revisa automáticamente en la integración continua (RNF-MAN-07).

## ADR-004: Comunicación entre módulos

**Estado:** Aceptada.

**Contexto.** Hay consultas que necesitan respuesta inmediata (¿son conexiones?, ¿queda cupo?) y reacciones que no deben bloquear la operación original (notificar, enviar un correo, actualizar el historial de moderación).

**Alternativas.** Solo llamadas directas entre módulos; solo eventos; llamadas para consultas y eventos para reacciones.

**Decisión.**

- **Consultas y órdenes:** llamada en proceso a la interfaz pública del otro módulo.
- **Reacciones:** eventos de dominio. El módulo productor guarda el evento **en la misma transacción** que la operación (tabla de salida) y un despachador en segundo plano lo entrega a los consumidores. Los consumidores descartan los repetidos por su identificador (RNF-CON-04).
- **Las notificaciones son un consumidor de eventos:** ningún módulo llama a Comunicación para notificar.

**Consecuencias.** Si falla un consumidor (por ejemplo, el correo), la operación original no se pierde y el evento se reintenta ([EC-02](../srs/Especificacion_Requisitos.md#34-escenarios-de-atributos-de-calidad)). Cada módulo con eventos tiene una tabla de salida.

## ADR-005: Persistencia

**Estado:** Propuesta.

**Contexto.** Los datos son relacionales (cuentas, conexiones, postulaciones, cupos) y varias reglas exigen transacciones (RNF-CON-01). La búsqueda necesita texto completo (ADR-008).

**Alternativas.**

| Opción | A favor | En contra |
|---|---|---|
| A. Una base relacional con un esquema por módulo | Transacciones locales, un solo respaldo, fronteras visibles en la base | Hay que impedir consultas entre esquemas (permisos por esquema). |
| B. Una base relacional sin separación | Lo más simple | Nada impide que un módulo lea tablas ajenas. |
| C. Una base por módulo | Aislamiento máximo | Seis bases que respaldar y sin transacciones entre módulos. |

**Propuesta.** A, con un usuario de base de datos por módulo que solo tiene permisos sobre su esquema. El motor se elige con ADR-010 (debe ofrecer texto completo, transacciones y cifrado en reposo, RNF-PRI-03).

## ADR-006: Contratos antes que el código

**Estado:** Aceptada.

**Contexto.** Seis módulos que se usan entre sí y un frontend que consume la API necesitan acordar antes qué se expone.

**Decisión.** La API REST, las interfaces públicas y los eventos se escriben y revisan en [`contracts/`](../../contracts/README.md) antes de programar. La integración continua compara el contrato acordado con el que genera el código (RNF-MAN-05).

**Consecuencias.** Cambiar un contrato es un pull request propio, revisado por el módulo que lo expone y por los que lo usan.

## ADR-007: Tiempo real

**Estado:** Propuesta. **Bloqueada por:** P-16.

**Contexto.** El indicador de notificaciones debe actualizarse en menos de 60 segundos sin recargar (FS-COM-02) y los mensajes deben llegar en menos de 2 segundos con la conversación abierta (FS-COM-01).

| Opción | A favor | En contra |
|---|---|---|
| A. WebSocket para notificaciones y mensajes | Una sola solución para ambos requisitos | Conexiones persistentes que el servidor y el alojamiento deben soportar. |
| B. Server-Sent Events | Más sencillo; suficiente porque el servidor es quien empuja | Enviar mensajes sigue siendo una petición normal; límites de conexiones en algunos navegadores. |
| C. Consulta periódica para notificaciones y tiempo real solo en mensajería | Lo más simple al inicio | Dos mecanismos; el Sprint 5 obliga a implementar el segundo. |

**Recomendación del equipo de documentación.** A, decidida en el Sprint 0 junto con el stack.

## ADR-008: Búsqueda de texto

**Estado:** Propuesta. **Bloqueada por:** P-17.

**Contexto.** La búsqueda de perfiles ignora mayúsculas y tildes y debe responder en menos de 1 segundo con 25.000 usuarios (FS-RED-03, RNF-REN-02).

| Opción | A favor | En contra |
|---|---|---|
| A. Texto completo de la base de datos | Sin componentes nuevos; consistente con las transacciones | Menos funciones (tolerancia a errores de escritura). |
| B. Motor de búsqueda dedicado | Mejor relevancia y tolerancia | Otro componente que operar y sincronizar. |
| C. Servicio de búsqueda externo | Sin operación propia | Costo y datos personales fuera de la universidad (RNF-PRI-08). |

**Recomendación.** A para el MVP; revisar con datos reales.

## ADR-009: Alojamiento

**Estado:** Propuesta. **Bloqueada por:** P-02, P-18.

**Contexto.** La disponibilidad del 99,5 %, las copias cifradas y la ley de datos (RNF-PRI-08) dependen de dónde corra UniLink.

| Opción | A favor | En contra |
|---|---|---|
| A. Infraestructura de la universidad | Datos dentro de la institución; sin costo de nube | Depende de la capacidad y del soporte de TI. |
| B. Nube con región que cumpla RNF-PRI-08 | Servicios gestionados (base, copias, correo); alcanza el 99,5 % con poco equipo | Costo mensual; revisión jurídica del proveedor. |
| C. Mixto: aplicación en la universidad y servicios gestionados en la nube | Equilibra costo y operación | Más piezas y más acuerdos. |

## ADR-010: Lenguaje y framework

**Estado:** Propuesta. **Bloqueada por:** P-53.

**Contexto.** El stack debe facilitar los módulos con fronteras verificables, ofrecer validación de contratos OpenAPI y ser conocido por el equipo, que rota entre semestres.

**Criterios.** Conocimiento del equipo; soporte para módulos y pruebas de arquitectura; generación de OpenAPI desde el código; madurez del ecosistema (autenticación, tareas programadas, PDF); costo de alojamiento.

| Opción (backend) | A favor | En contra |
|---|---|---|
| A. Java con Spring Boot | Soporte explícito para monolitos modulares y verificación de módulos | Curva de aprendizaje mayor. |
| B. TypeScript con NestJS | Mismo lenguaje que el frontend; módulos como concepto del framework | La verificación de fronteras requiere herramientas aparte. |
| C. Python con Django o FastAPI | Rápido de aprender; muy usado en la universidad | Hay que imponer las fronteras con convenciones y pruebas. |

El frontend (aplicación web adaptable, RNF-USA-02) se decide junto con el backend.

## ADR-011: Tareas en segundo plano y programadas

**Estado:** Propuesta.

**Contexto.** Varias tareas no deben retrasar la respuesta al usuario (RNF-REN-05): despachar eventos (ADR-004), enviar correos, cerrar oportunidades por fecha, finalizar eventos, recordar eventos 24 horas antes, reactivar suspensiones, vencer solicitudes e invitaciones y aplicar la retención de datos (RNF-PRI-09).

| Opción | A favor | En contra |
|---|---|---|
| A. Proceso trabajador aparte con el mismo código | No compite con las peticiones; se reinicia por separado | Un proceso más que desplegar. |
| B. Dentro del mismo proceso de la aplicación | Lo más sencillo | Una tarea pesada afecta a las peticiones; difícil de escalar. |
| C. Servicio de colas externo | Robusto y escalable | Infraestructura adicional que no se necesita con esta carga. |

**Recomendación.** A: la misma aplicación arrancada en modo trabajador, que lee las tablas de salida y ejecuta las tareas programadas.

## ADR-012: Almacenamiento de archivos

**Estado:** Propuesta.

**Contexto.** Fotos de perfil, imágenes y PDF de publicaciones y portadas de eventos: validación por contenido real, servidos desde un dominio que no ejecute código (RNF-SEG-06), incluidos en las copias (RNF-DIS-03) y borrados al eliminar una cuenta (RNF-PRI-06).

| Opción | A favor | En contra |
|---|---|---|
| A. Almacenamiento de objetos compatible con S3 | Separado de la aplicación; dominio propio; copias sencillas | Un servicio más (gestionado o propio). |
| B. Disco del servidor de la aplicación | Sin componentes nuevos | Difícil de escalar y de servir desde otro dominio. |
| C. Base de datos | Una sola copia de seguridad | Base pesada y lenta para servir imágenes. |

**Recomendación.** A, decidida junto con ADR-009.
