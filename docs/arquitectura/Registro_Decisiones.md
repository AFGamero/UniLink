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
| [ADR-005](#adr-005-persistencia) | Persistencia | Aceptada (2026-10-27): PostgreSQL, un esquema por módulo |
| [ADR-006](#adr-006-contratos-antes-que-el-código) | Contratos antes que el código | Aceptada |
| [ADR-007](#adr-007-tiempo-real) | Tiempo real | Propuesta (P-16) |
| [ADR-008](#adr-008-búsqueda-de-texto) | Búsqueda de texto | Aceptada (2026-10-27): PostgreSQL |
| [ADR-009](#adr-009-alojamiento) | Alojamiento | Aceptada (Reunión 2026-10-19) |
| [ADR-010](#adr-010-lenguaje-y-framework) | Lenguaje y framework | Aceptada (2026-10-27): FastAPI, React y TypeScript |
| [ADR-011](#adr-011-tareas-en-segundo-plano-y-programadas) | Tareas en segundo plano y programadas | Propuesta |
| [ADR-012](#adr-012-almacenamiento-de-archivos) | Almacenamiento de archivos | Propuesta |
| [ADR-013](#adr-013-autenticación-institucional-y-cuentas-precreadas) | Autenticación institucional y cuentas precreadas | Propuesta; posición del equipo: opción C (P-63, falta validar con TI) |
| [ADR-014](#adr-014-integración-con-la-api-de-admisiones) | Integración con la API de admisiones | Aceptada para el MVP (simulada); real pendiente (P-61) |
| [ADR-015](#adr-015-eliminación-de-cuentas-borrado-lógico) | Eliminación de cuentas: borrado lógico | Propuesta (P-12) |
| [ADR-016](#adr-016-cliente-móvil-android) | Cliente móvil Android | Propuesta; posición del equipo: web en el MVP y PWA después (falta validar con el tutor) |
| [ADR-017](#adr-017-arquitectura-interna-de-los-módulos-hexagonal-con-clean-architecture) | Arquitectura interna de los módulos: hexagonal con Clean Architecture | Aceptada (2026-10-27) |
| [ADR-018](#adr-018-bibliotecas-y-herramientas-del-frontend) | Bibliotecas y herramientas del frontend | Aceptada (2026-10-27) |

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

**Estado:** Aceptada (decisión del equipo comunicada el 2026-10-27).

**Contexto.** Los datos son relacionales (cuentas, conexiones, postulaciones, cupos) y varias reglas exigen transacciones (RNF-CON-01). La búsqueda necesita texto completo (ADR-008).

**Alternativas.**

| Opción | A favor | En contra |
|---|---|---|
| A. Una base relacional con un esquema por módulo | Transacciones locales, un solo respaldo, fronteras visibles en la base | Hay que impedir consultas entre esquemas (permisos por esquema). |
| B. Una base relacional sin separación | Lo más simple | Nada impide que un módulo lea tablas ajenas. |
| C. Una base por módulo | Aislamiento máximo | Seis bases que respaldar y sin transacciones entre módulos. |

**Decisión.** A, con un usuario de base de datos por módulo que solo tiene permisos sobre su esquema. **Motor: PostgreSQL**, que ofrece esquemas, permisos por esquema, bloqueo de registros (`SELECT … FOR UPDATE`) para los cupos (RNF-CON-01), búsqueda de texto completo con `unaccent` y búsqueda por similitud con `pg_trgm` (ADR-008), y se puede operar en la infraestructura de la Universidad (ADR-009).

**Consecuencias.** El cifrado en reposo (RNF-PRI-03) se resuelve en el disco o en el volumen del servidor, porque PostgreSQL no cifra las tablas por sí mismo; hay que acordarlo con TI. _(propuesto)_ Desde FastAPI se accede con SQLAlchemy 2 y las migraciones se hacen con Alembic, una carpeta de migraciones por esquema de módulo; los modelos del ORM viven en los adaptadores de salida (ADR-017).

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

**Reunión 2026-10-19.** Se discutió sin decidir: tiempo real (WebSocket o SSE) frente a consulta al iniciar sesión o periódica. Además, la mensajería misma está en revisión (P-56: contacto directo primero y chat después). Si la mensajería no entra como chat en el MVP, el requisito de 2 segundos de FS-COM-01 desaparece y la opción C pasa a ser suficiente.

## ADR-008: Búsqueda de texto

**Estado:** Aceptada (decisión del equipo comunicada el 2026-10-27). Resuelve P-17.

**Contexto.** La búsqueda de perfiles ignora mayúsculas y tildes y debe responder en menos de 1 segundo con 25.000 usuarios (FS-RED-03, RNF-REN-02).

| Opción | A favor | En contra |
|---|---|---|
| A. Texto completo de la base de datos | Sin componentes nuevos; consistente con las transacciones | Menos funciones (tolerancia a errores de escritura). |
| B. Motor de búsqueda dedicado | Mejor relevancia y tolerancia | Otro componente que operar y sincronizar. |
| C. Servicio de búsqueda externo | Sin operación propia | Costo y datos personales fuera de la universidad (RNF-PRI-08). |

**Recomendación.** A para el MVP; revisar con datos reales.

**Reunión 2026-10-19.** Sigue pendiente. Se pidió una búsqueda **tolerante** y Alfonso propone SQL optimizado, que corresponde a la opción A. Además, la decisión de reconocer etiquetas similares y no solo idénticas (P-46) exige normalización o sinónimos, cosa que la opción A no resuelve por sí sola.

**Decisión.** A, sobre PostgreSQL (ADR-005): texto completo con `unaccent` para ignorar tildes y mayúsculas (FS-RED-03 RN-01), y `pg_trgm` para la búsqueda tolerante a errores de escritura. Lo implementa el adaptador de salida de búsqueda del módulo Red, detrás de un puerto (ADR-017), así que se puede cambiar por un motor dedicado sin tocar los casos de uso.

**Consecuencias.** Las etiquetas similares (P-46, RD-28) se resuelven con el catálogo de etiquetas predefinidas (RD-13) más una tabla de sinónimos administrada; la similitud por trigramas solo ayuda en los errores de escritura. EC-01 y EC-09 validan el rendimiento con 25.000 usuarios.

## ADR-009: Alojamiento

**Estado:** Aceptada (Reunión 2026-10-19). La disponibilidad y el horario de soporte siguen pendientes (P-18).

**Contexto.** La disponibilidad del 99,5 %, las copias cifradas y la ley de datos (RNF-PRI-08) dependen de dónde corra UniLink.

| Opción | A favor | En contra |
|---|---|---|
| A. Infraestructura de la universidad | Datos dentro de la institución; sin costo de nube | Depende de la capacidad y del soporte de TI. |
| B. Nube con región que cumpla RNF-PRI-08 | Servicios gestionados (base, copias, correo); alcanza el 99,5 % con poco equipo | Costo mensual; revisión jurídica del proveedor. |
| C. Mixto: aplicación en la universidad y servicios gestionados en la nube | Equilibra costo y operación | Más piezas y más acuerdos. |

**Decisión.** **A — Infraestructura propia de la Universidad**, con el servidor activo 24/7. La base de datos de UniLink es propia y desacoplada de la institucional; con los sistemas de la Universidad solo se comparte la autenticación (ADR-013).

**Consecuencias.** RNF-PRI-08 queda cubierto, porque los datos no salen de la institución. Las copias cifradas (RNF-DIS-03, RNF-PRI-03), el monitoreo y la restauración (RNF-DIS-04) dependen de TI de la Universidad, y hay que acordarlos por escrito. El 99,5 % (RNF-DIS-01) sin servicios gestionados es el principal riesgo operativo (P-18, R-10). El correo saliente (RNF-DIS-06) y el almacenamiento de archivos (ADR-012) también deben resolverse dentro de la infraestructura o con un servicio aprobado por la Universidad.

## ADR-010: Lenguaje y framework

**Estado:** Aceptada (decisión del equipo comunicada el 2026-10-27). Resuelve P-53.

**Contexto.** El stack debe facilitar los módulos con fronteras verificables, ofrecer validación de contratos OpenAPI y ser conocido por el equipo, que rota entre semestres.

**Criterios.** Conocimiento del equipo; soporte para módulos y pruebas de arquitectura; generación de OpenAPI desde el código; madurez del ecosistema (autenticación, tareas programadas, PDF); costo de alojamiento.

| Opción (backend) | A favor | En contra |
|---|---|---|
| A. Java con Spring Boot | Soporte explícito para monolitos modulares y verificación de módulos | Curva de aprendizaje mayor. |
| B. TypeScript con NestJS | Mismo lenguaje que el frontend; módulos como concepto del framework | La verificación de fronteras requiere herramientas aparte. |
| C. Python con Django o FastAPI | Rápido de aprender; muy usado en la universidad | Hay que imponer las fronteras con convenciones y pruebas. |

**Decisión.**

- **Backend: Python con FastAPI** (opción C). Una sola aplicación, organizada según ADR-002, ADR-003 y ADR-017.
- **Frontend: React con TypeScript**, como aplicación web adaptable (RNF-USA-02) que consume la API REST.

**Consecuencias.**

- **Contratos (RNF-MAN-05).** FastAPI genera el OpenAPI a partir de los esquemas Pydantic de las rutas. La integración continua compara ese documento con `contracts/api/`. FastAPI emite OpenAPI 3.1, y por eso **los contratos se migraron a OpenAPI 3.1.0 el 2026-10-27**: la comparación es directa, y `verificar_docs.py` exige 3.1.0. Además, los esquemas de petición y respuesta que faltan en los contratos se pueden escribir directamente como modelos Pydantic y revisarse contra el contrato (H-24).
- **Fronteras (RNF-MAN-07).** Python no impone módulos, así que las fronteras se verifican en la CI con contratos de **import-linter**: independencia entre módulos, capas de ADR-017 y prohibición de que el dominio importe frameworks.
- **Pruebas.** pytest para pruebas unitarias, de integración, de permisos y de aceptación; cobertura medida en la CI (RNF-MAN-02).
- **Frontend.** El cliente HTTP se genera desde `contracts/api/` y la sesión sigue siendo por cookie `HttpOnly` con cabecera CSRF (SES-01, SES-04). El resto de las bibliotecas del frontend está en [ADR-018](#adr-018-bibliotecas-y-herramientas-del-frontend).
- **Siguen pendientes:** tiempo real (ADR-007), tareas (ADR-011) y archivos (ADR-012). El motor (ADR-005) es PostgreSQL. Con FastAPI, el tiempo real puede ser WebSocket o SSE sin componentes adicionales.

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

## ADR-013: Autenticación institucional y cuentas precreadas

**Estado:** Propuesta. La decisión de producto se tomó en la reunión del 2026-10-19. **Posición del equipo (2026-10-27): opción C.** Falta validar con TI el formato y la validación del token (P-63) antes de aceptarla.

**Contexto.** La reunión del 2026-10-19 decidió:

1. Las cuentas de la comunidad se **precrean**, como en Microsoft Teams, y el usuario solo las activa y personaliza.
2. La Universidad aporta solo el correo institucional, el nombre, la facultad o programa y el estado de monitor.
3. Con los sistemas de la Universidad **solo se comparte la autenticación**, mediante el token del Campus Virtual.
4. Se admiten **cuentas externas** con registro propio.
5. Se conservan el bloqueo temporal por intentos fallidos y la recuperación de contraseña.

Hoy FS-USR-01, FS-USR-02 y FS-USR-03 describen un autorregistro con correo institucional, contraseña propia y verificación por enlace, y el SRS (§1.2) excluye el inicio de sesión con proveedores externos.

| Opción | A favor | En contra |
|---|---|---|
| A. Todas las cuentas se autentican con el Campus Virtual; UniLink valida el token y crea su propia sesión de servidor (SES-01) | Una sola identidad institucional; sin contraseñas que custodiar para la comunidad | Los externos no tienen cuenta en el Campus Virtual; UniLink depende de su disponibilidad. |
| B. Cuentas precreadas que se activan con un enlace al correo institucional y una contraseña propia | Reutiliza casi todo FS-USR-01 a FS-USR-03 | No cumple "solo se comparte la autenticación"; duplica credenciales. |
| C. Híbrida: comunidad con el token del Campus Virtual; externos con correo y contraseña propios, verificación por enlace y bloqueo por intentos | Cumple las cinco decisiones; los flujos de contraseña de los specs siguen sirviendo para externos | Dos caminos de autenticación que probar; hay que acordar con TI el formato y la validación del token. |

**Recomendación del análisis.** C. La sesión sigue siendo de servidor con cookie `HttpOnly` (SES-01), sin importar cómo se autentique el usuario.

**Consecuencias.** Hay que reescribir FS-USR-01 (activación de una cuenta precreada y registro de externos), FS-USR-02 (dos formas de iniciar sesión) y FS-USR-03 (la recuperación aplica solo a externos; la comunidad recupera su contraseña en el Campus Virtual), y quitar la exclusión del SRS §1.2. Aparece una dependencia externa crítica: si el Campus Virtual no responde, la comunidad no puede iniciar sesión, aunque las sesiones abiertas siguen funcionando. El riesgo debe quedar como escenario de calidad.

## ADR-014: Integración con la API de admisiones

**Estado:** Aceptada para el MVP, en versión simulada (Reunión 2026-10-19). La integración real está pendiente del acceso al endpoint (P-61).

**Contexto.** Las cuentas precreadas (ADR-013) y el estado de monitor académico necesitan datos institucionales. La Universidad expone un endpoint GET de admisiones, pero el acceso no está gestionado. El estado de monitor se actualiza **en lote** cuando la Vicerrectoría Académica publica el listado oficial, aunque la cuenta no esté activada.

**Decisión.** Usuarios define un **puerto** "Directorio institucional" con dos adaptadores: uno **simulado** para el MVP, con correos ficticios, y uno **real** para el producto final, que consume el endpoint GET. Una tarea programada (ADR-011) precrea o actualiza las cuentas y aplica en lote el listado de monitores.

**Consecuencias.** El MVP y sus pruebas no tocan datos reales (RNF-DES-01). El adaptador real se cambia sin tocar los demás módulos (EC-07). Falta especificar los campos, la frecuencia de sincronización y el comportamiento ante fallas del endpoint (RNF-DIS-05).

## ADR-015: Eliminación de cuentas: borrado lógico

**Estado:** Propuesta. **Bloqueada por:** P-12 (validación jurídica).

**Contexto.** La reunión del 2026-10-19 decidió que eliminar una cuenta es un **borrado lógico**: la cuenta y todo lo asociado se ocultan, con trazabilidad de quién y cuándo. Hoy FS-USR-05 (RN-09), RNF-PRI-06 y la tabla de retención (RNF-PRI-09) exigen borrar los datos personales a los 30 días, incluidos los de las copias de seguridad, y la Ley 1581 de 2012 reconoce el derecho de supresión.

| Opción | A favor | En contra |
|---|---|---|
| A. Borrado lógico indefinido con trazabilidad | Es lo decidido; permite auditoría y restaurar | Choca con RNF-PRI-06 y con el derecho de supresión, que está por validar. |
| B. Borrado lógico inmediato y, tras un plazo, anonimización de los datos personales, conservando solo la traza (quién y cuándo) | Cumple la trazabilidad y probablemente la supresión | Hay que definir qué datos se anonimizan y en qué plazo. |
| C. Borrado físico a los 30 días (especificación actual) | Cumplimiento claro de la supresión | Contradice la decisión del 2026-10-19 y pierde trazabilidad. |

**Recomendación del análisis.** Esperar a la Oficina Jurídica. Si objeta A, B conserva la intención de la decisión.

**Consecuencias.** Según lo que se decida, hay que actualizar FS-USR-05, RNF-PRI-06, RNF-PRI-09 y el tratamiento de P-51. En la persistencia (ADR-005), toda consulta debe excluir los registros borrados lógicamente.

## ADR-016: Cliente móvil Android

**Estado:** Propuesta. **Posición del equipo (2026-10-27):** web adaptable en el MVP y PWA instalable después del Sprint 8 (opciones A y B). Falta validarla con el tutor, porque toca el alcance.

**Contexto.** El SRS define el MVP como una aplicación web adaptable y excluye las aplicaciones nativas (RNF-COM-02, §1.2). La compatibilidad móvil se cubre con Chrome en Android y Safari en iOS (RNF-COM-01) y con el diseño desde 360 px (RNF-USA-02). Se ha pedido documentar la arquitectura para Android, pero ningún documento aprobado la incluye en el alcance.

| Opción | A favor | En contra |
|---|---|---|
| A. Solo web adaptable (alcance actual) | Sin costo adicional; ya especificada | Sin instalación ni notificaciones push en el sistema. |
| B. Aplicación web progresiva (PWA) instalable sobre la misma web | Se instala en Android desde el navegador; reutiliza todo el frontend y la sesión por cookie | Las notificaciones push y el modo sin conexión piden trabajo adicional; el soporte en iOS es limitado. |
| C. Aplicación nativa (Kotlin) | Mejor integración con el sistema | Otro código que mantener; obliga a cambiar la sesión a tokens (SES-01 asume cookies) y a publicar en la tienda. |
| D. Multiplataforma (Flutter o React Native) | Un solo código para Android e iOS | Mismo cambio de sesión que C; otro stack que aprender. |

**Recomendación del análisis.** A en el MVP y B como incremento de bajo costo después del Sprint 8. C o D solo si el tutor o la Universidad lo exigen; en ese caso, primero hay que definir la autenticación por tokens para clientes nativos, sin debilitar SES-01 en la web.

**Consecuencias.** Si se adopta B, se agregan un manifiesto, un service worker y una política de caché que nunca guarde respuestas con datos personales. Si se adopta C o D, cambian el SRS (RNF-COM-02), la seguridad de la API y el plan de pruebas.

## ADR-017: Arquitectura interna de los módulos: hexagonal con Clean Architecture

**Estado:** Aceptada (decisión del equipo comunicada el 2026-10-27). Complementa ADR-002 y ADR-003, que siguen vigentes.

**Contexto.** ADR-002 fija el estilo del sistema (un monolito modular con seis módulos) y el [plan de implementación §1](./Plan_de_Implementacion.md#1-estructura-interna-de-un-módulo) describía cuatro capas por módulo. El equipo decidió que cada módulo se construya con **arquitectura hexagonal** (puertos y adaptadores) siguiendo la **regla de dependencia de Clean Architecture**. El objetivo es que el dominio y los casos de uso no dependan de FastAPI, de la base de datos ni de los servicios externos.

**Alternativas.**

| Opción | A favor | En contra |
|---|---|---|
| A. Capas por módulo (plan original) | Sencilla de explicar | La infraestructura puede filtrarse en el dominio; probar sin la base de datos es más difícil. |
| B. Hexagonal solo en las integraciones externas | Menos código de mapeo | Dos estilos conviviendo en el mismo módulo. |
| C. Hexagonal con Clean Architecture en cada módulo | Dominio y casos de uso se prueban sin infraestructura; el adaptador del Campus Virtual o de admisiones se cambia sin tocar la lógica (ADR-013, ADR-014); un mismo estilo en todo el código | Más archivos y mapeo entre los modelos del dominio, los esquemas de la API y los de persistencia. |

**Decisión.** C. El sistema sigue siendo **un solo monolito con un solo despliegue y seis módulos** (ADR-002, ADR-003), y cada módulo se organiza en cuatro anillos con dependencias **solo hacia adentro**:

| Anillo | Contiene | Puede importar | No puede importar |
|---|---|---|---|
| **Dominio** | Entidades, objetos de valor, máquinas de estados, reglas RN-NN y eventos de dominio. Python puro. | Nada fuera del dominio | FastAPI, Pydantic, el ORM ni ningún adaptador |
| **Aplicación** | Casos de uso (uno por acción), validación de permisos del "Quién es quién", límites de la transacción y **puertos** de salida (repositorios, tabla de salida, correo, archivos, Campus Virtual, directorio institucional). | Dominio, paquete de contratos | Adaptadores, FastAPI, ORM |
| **Adaptadores de entrada** | Rutas de FastAPI con sus esquemas Pydantic (implementan `contracts/api/`), la implementación de la interfaz pública del módulo (`contracts/modulos/`), los consumidores de eventos y las tareas del trabajador. | Aplicación, paquete de contratos | Adaptadores de salida de otro módulo |
| **Adaptadores de salida** | Implementaciones de los puertos: repositorios sobre el esquema propio (ADR-005), tabla de salida (ADR-004), correo, archivos, Campus Virtual y directorio institucional (simulado en el MVP). | Aplicación (para implementar los puertos) | Dominio o adaptadores de otro módulo |

- **Entre módulos:** un caso de uso que necesita a otro módulo depende de su **interfaz pública**, definida en el paquete de contratos (ADR-003). La **raíz de composición** de la aplicación conecta cada puerto con su adaptador al arrancar, y cada módulo publica sus eventos por su tabla de salida (ADR-004).
- **Modelos separados:** el dominio usa sus propias clases; Pydantic queda en los adaptadores de entrada (esquemas de la API) y los modelos del ORM, en los de salida.

**Consecuencias.**

- Las reglas de negocio se prueban con pruebas unitarias del dominio y de los casos de uso, sin base de datos ni servidor (RNF-MAN-01).
- La CI verifica con import-linter las capas de cada módulo y la independencia entre módulos (RNF-MAN-07).
- Hay más mapeo entre modelos. Se compensa con una estructura uniforme en los seis módulos ([plan §1](./Plan_de_Implementacion.md#1-estructura-interna-de-un-módulo)).
- Separar un módulo como servicio aparte (EC-07) sigue siendo posible: sus puertos y su interfaz pública ya están definidos.

## ADR-018: Bibliotecas y herramientas del frontend

**Estado:** Aceptada (decisión del equipo comunicada el 2026-10-27; se adoptó la recomendación completa).

**Contexto.** ADR-010 fija React con TypeScript. Falta el resto del frontend. Los requisitos que más pesan son:

- WCAG 2.1 AA, teclado y foco visible (RNF-ACC-01 a 06).
- Diseño desde 360 px y Lighthouse móvil ≥ 80 (RNF-USA-02, RNF-REN-03).
- Español de Colombia, `dd/mm/aaaa`, 12 h y hora de Colombia (RNF-USA-01).
- Sesión por cookie con cabecera CSRF (SES-01, SES-04).
- Paginación por cursor en el feed, los mensajes y las notificaciones.
- Contratos primero (ADR-006).
- Que el frontend pueda avanzar mientras no exista el backend (H-22, H-24).

**Decisión.**

| Necesidad | Decisión | Por qué | Alternativa |
|---|---|---|---|
| Lenguaje | **TypeScript** (decidido en ADR-010) | Tipos del contrato en todo el código | — |
| Compilación y servidor de desarrollo | **Vite** | Estándar para aplicaciones React de una sola página; genera archivos estáticos que se sirven desde la infraestructura de la Universidad (ADR-009) | Next.js, descartado: agrega un servidor Node que operar, y la aplicación no necesita renderizado en el servidor porque todo exige sesión |
| Enrutamiento | **React Router** | El más conocido; resuelve rutas protegidas y volver a la página pedida tras iniciar sesión (FS-USR-02 RF-08) | TanStack Router |
| Datos del servidor | **TanStack Query** | Caché, reintentos, paginación por cursor e invalidación cuando llega un aviso en tiempo real (ADR-007) | — |
| Cliente de la API | **openapi-typescript + openapi-fetch**, generados desde `contracts/api/` (OpenAPI 3.1) | Tipos exactos del contrato: si el contrato cambia, el compilador marca lo que se rompió. Un middleware agrega `X-CSRF-Token`, `Idempotency-Key` e `If-Match`, y las peticiones envían la cookie (`credentials: "include"`) | Orval, que además genera los hooks de TanStack Query |
| Formularios y validación | **React Hook Form + Zod** | Valida el formato de la sección 6 de cada spec con los mismos mensajes MSG-NN; las reglas siguen en el servidor (RNF-SEG-04) | — |
| Componentes e interfaz accesible | **Tailwind CSS + shadcn/ui** (sobre Radix UI) | Componentes accesibles (teclado, foco, ARIA) como base para WCAG 2.1 AA; el código de los componentes queda en el repositorio y se adapta al diseño de UniLink | MUI: más completo de entrada, menos personalizable |
| Estado de la interfaz | **Contexto de React**, sin biblioteca adicional al inicio | El estado de negocio vive en TanStack Query; lo global se reduce a la sesión y a preferencias de interfaz | Zustand, si crece |
| Fechas y hora | **API `Intl` del navegador** con la zona `America/Bogota` | Cumple RNF-USA-01 sin dependencias | date-fns |
| Tiempo real | **WebSocket o EventSource nativos**, según ADR-007, que invalidan las consultas de TanStack Query | Sin bibliotecas extra; FastAPI soporta ambos | — |
| API simulada | **MSW (Mock Service Worker)** con respuestas basadas en los contratos | El frontend avanza sin backend y las mismas simulaciones sirven en las pruebas | — |
| Pruebas | **Vitest + Testing Library** (componentes); **Playwright** (extremo a extremo con los escenarios Gherkin); **@axe-core/playwright** (accesibilidad); **Lighthouse CI** (RNF-REN-03) | Cubren las filas de interfaz, aceptación, accesibilidad y rendimiento del plan de pruebas | — |
| Calidad del código | **ESLint** (con `eslint-plugin-jsx-a11y`) + **Prettier** | Detecta problemas de accesibilidad mientras se escribe | Biome |
| Gestor de paquetes | **pnpm** | Rápido y con archivo de bloqueo estricto | npm |
| PWA (solo si se adopta ADR-016 B) | **vite-plugin-pwa** | Manifiesto y service worker sin configuración manual; la caché nunca guarda respuestas con datos personales | — |

**Consecuencias.** La estructura del [plan §1](./Plan_de_Implementacion.md#1-estructura-interna-de-un-módulo) se mantiene: `src/modulos/<modulo>/`, `src/api/` (cliente generado y simulaciones de MSW) y `src/compartido/`. El paso "generar el cliente desde `contracts/api/`" se agrega a la CI del frontend, para que un cambio de contrato rompa la compilación en lugar de fallar en producción.
