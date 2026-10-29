# Matriz de trazabilidad — UniLink

_Complemento del [informe integral](./informe_integral_unilink.md) · Corte: 2026-10-27_

Relaciona cada requisito con su fuente, su módulo, el componente de arquitectura que lo implementará, las entidades de datos, los contratos y la prueba que lo valida. Amplía el [apéndice A del SRS](./srs/Especificacion_Requisitos.md#apéndice-a-matriz-de-trazabilidad) (CU → HU → spec → RNF → contratos) con las columnas de componente, datos y prueba.

**Cómo leerla:**

- La unidad de traza es el **spec**: cada uno agrupa sus requisitos funcionales (`<MOD>-NN/RF-NN`, listados en el [catálogo](./requisitos_unilink.md)), que comparten casos de uso, contratos y pruebas.
- **Componente:** en el monolito modular, cada spec lo implementa su módulo con las capas API → aplicación → dominio → infraestructura ([plan §1](./arquitectura/Plan_de_Implementacion.md#1-estructura-interna-de-un-módulo)). La columna indica además si intervienen el trabajador (tareas y eventos) o el canal de tiempo real.
- **Entidades:** son el modelo lógico **propuesto** que se deriva de los README de cada módulo ([informe, capítulo 10](./informe_integral_unilink.md#capítulo-10-arquitectura-de-datos)). No existen tablas implementadas.
- **Endpoints:** número de operaciones con ese `x-spec` en `contracts/api/` (124 en total) y el archivo donde están.
- **Prueba de validación:** escenarios Gherkin del spec (sección 12), más los tipos de prueba que exige el [plan §5](./arquitectura/Plan_de_Implementacion.md#5-estrategia-de-pruebas): **P** = permisos por API, **C** = concurrencia, **K** = contrato, **E** = escenario de calidad.
- **Estado:** todos los specs están en **Borrador** y **ninguno está implementado** (H-22). "Desactualizado" significa que una decisión de la reunión del 2026-10-19 todavía no se refleja ([riesgos y brechas §3](./riesgos_y_brechas_unilink.md#3-cambios-pendientes-por-spec-según-la-reunión-del-2026-10-19)).

## 1. Requisitos funcionales (por spec)

| Spec (RF) | Fuente: CU / HU | Módulo | Componente | Entidades (propuestas) | Endpoints | Eventos que publica | Prueba de validación | Estado |
|---|---|---|---|---|---|---|---|---|
| [FS-USR-01](./modulos/usuarios/specs/FS-USR-01-registro.md) (RF-01 a 08) | CU-01 / HU-01 | Usuarios | API + aplicación; trabajador (correo de verificación, limpieza a los 7 días) | Cuenta, EnlaceVerificacion, AceptacionTerminos, CategoriaInteres | 3 · `usuarios.yaml` | `cuenta.estado_cambiado` | 14 Gherkin · P · C (registro simultáneo) · K · EC-02 | Borrador; desactualizado (H-02, H-15) |
| [FS-USR-02](./modulos/usuarios/specs/FS-USR-02-inicio-sesion.md) (RF-01 a 08) | CU-02 / HU-02 | Usuarios | Componente interno de credenciales y sesiones; contexto de la petición | Cuenta, Credencial, Sesion, IntentoFallido | 3 · `usuarios.yaml` | — | 13 Gherkin · P · C (intentos desde varios dispositivos) · K · EC-03 | Borrador; desactualizado (H-02) |
| [FS-USR-03](./modulos/usuarios/specs/FS-USR-03-recuperar-contrasena.md) (RF-01 a 05) | CU-17 / HU-28 | Usuarios | API + aplicación; adaptador de correo propio | EnlaceRecuperacion, Credencial, Sesion | 2 · `usuarios.yaml` | — | 10 Gherkin · P · K · EC-02 | Borrador; desactualizado (H-02) |
| [FS-USR-04](./modulos/usuarios/specs/FS-USR-04-preferencias-contenido.md) (RF-01 a 04) | CU-18 / HU-14 | Usuarios | API + interfaz pública `categoriasDeInteres` | CategoriaInteres (ref. Categoria de Plataforma) | 2 · `usuarios.yaml` | — (consume `categoria.cambiada`) | 6 Gherkin · K | Borrador |
| [FS-USR-05](./modulos/usuarios/specs/FS-USR-05-configuracion-cuenta.md) (RF-01 a 08) | CU-03 / HU-03 | Usuarios | API + aplicación; trabajador (eliminación a los 30 días) | Cuenta, CorreoRespaldo, Configuracion, PreferenciaCorreo, Sesion | 10 · `usuarios.yaml` | `cuenta.estado_cambiado`, `perfil.actualizado` | 11 Gherkin · P · C (mismo correo en dos cuentas) · K | Borrador; desactualizado (H-03) |
| [FS-USR-06](./modulos/usuarios/specs/FS-USR-06-perfil-profesional.md) (RF-01 a 07) | CU-04 / HU-04 | Usuarios | API + interfaz pública (`datosPublicos`, `perfilParaRed`, `afinidad`) + `Reportable` (perfil) | Perfil, Etiqueta, PerfilEtiqueta, Experiencia, ProyectoPersonal, Logro | 4 · `usuarios.yaml` | `perfil.actualizado` | 13 Gherkin · P · C (`If-Match`) · K · E (RNF-SEG-06) | Borrador; al día con la reunión (2026-10-27); preguntas P-65 y P-66 |
| [FS-USR-07](./modulos/usuarios/specs/FS-USR-07-hoja-de-vida-pdf.md) (RF-01 a 05) | CU-19 / HU-13 | Usuarios | API + generador de PDF (sin persistencia) | — (lee Perfil) | 1 · `usuarios.yaml` | — | 8 Gherkin · P · K · rendimiento (< 10 s) | Borrador |
| [FS-USR-08](./modulos/usuarios/specs/FS-USR-08-gestion-cuentas.md) (RF-01 a 07) | CU-24 / HU-17 | Usuarios | API de administración; trabajador (fin de suspensiones) | Cuenta, Sancion | 4 · `usuarios.yaml` | `cuenta.estado_cambiado`, `auditoria.registrada` | 9 Gherkin · P · C (dos administradores) · K | Borrador; desactualizado (H-05, H-12) |
| [FS-RED-01](./modulos/red/specs/FS-RED-01-solicitudes-conexion.md) (RF-01 a 09) | CU-06, CU-07 / HU-06, HU-07 | Red | API + interfaz pública (`sonConexiones`, `numeroDeConexiones`); trabajador (vencimientos) | SolicitudConexion, Conexion | 7 · `red.yaml` | `conexion.solicitada`, `conexion.aceptada`, `conexion.eliminada` | 14 Gherkin · P · C (solicitudes cruzadas, límite diario) · K | Borrador; falta el bloqueo de usuarios (H-12) |
| [FS-RED-02](./modulos/red/specs/FS-RED-02-onboarding-sugerencias.md) (RF-01 a 06) | CU-13 / HU-24 | Red | Aplicación (cálculo del puntaje) + interfaz pública `perfilesComplementarios` | Sugerencia (calculada) | 3 · `red.yaml` | `conexion.solicitada` | 10 Gherkin · K | Borrador; desactualizado (H-14) |
| [FS-RED-03](./modulos/red/specs/FS-RED-03-busqueda-perfiles.md) (RF-01 a 08) | CU-05 / HU-05 | Red | API + índice de búsqueda (ADR-008) + interfaz pública `queVeObservador` | IndiceBusqueda (derivado de Perfil) | 2 · `red.yaml` | — | 13 Gherkin · P (privacidad) · K · EC-01, EC-09 | Borrador; falta la navegación de Explorar (H-16); pregunta P-67 |
| [FS-CNT-01](./modulos/contenido/specs/FS-CNT-01-publicaciones-feed.md) (RF-01 a 10) | CU-08, CU-09 / HU-08, HU-09 | Contenido | API + aplicación (feed y relevancia) + almacenamiento de archivos + `Reportable` | Publicacion, Adjunto, Comentario, Reaccion | 11 · `contenido.yaml` | `publicacion.comentada` | 15 Gherkin · P · C (reacción doble, `Idempotency-Key`) · K · EC-01 | Borrador; desactualizado (H-09, H-11) |
| [FS-CNT-02](./modulos/contenido/specs/FS-CNT-02-moderacion-contenido.md) (RF-01 a 08) | CU-25 / HU-18, HU-19 | Contenido | API de administración + contrato `Reportable` (consumidor) | Reporte, DecisionModeracion | 5 · `contenido.yaml` | `contenido.reportado`, `contenido.retirado`, `reporte.revisado`, `auditoria.registrada` | 13 Gherkin · P · C (dos administradores) · K · EC-06 | Borrador; desactualizado (H-05, H-06, H-12) |
| [FS-COM-01](./modulos/comunicacion/specs/FS-COM-01-mensajeria-privada.md) (RF-01 a 09) | CU-10 / HU-10 | Comunicación | API + canal de tiempo real (ADR-007); trabajador (correo diferido) | Conversacion, Mensaje, OcultamientoConversacion | 5 · `comunicacion.yaml` | `mensaje.enviado` | 13 Gherkin · P · C (`Idempotency-Key`) · K · EC-05, EC-07 | Borrador; en revisión (H-18) |
| [FS-COM-02](./modulos/comunicacion/specs/FS-COM-02-centro-notificaciones.md) (RF-01 a 06) | CU-23 / HU-30 | Comunicación | Consumidor de eventos + trabajador (correos, limpieza) + tiempo real | Notificacion, CorreoPendiente, EventoProcesado | 4 · `comunicacion.yaml` | — (consume todo el catálogo) | 11 Gherkin · P · K · EC-02 | Borrador |
| [FS-COL-01](./modulos/colaboracion/specs/FS-COL-01-publicacion-oportunidades.md) (RF-01 a 09) | CU-22 / HU-29 | Colaboración | API + aplicación (cupos atómicos) + `Reportable`; trabajador (cierre por fecha) | Oportunidad, HabilidadRequerida, Postulacion | 8 · `colaboracion.yaml` | `postulacion.estado_cambiado`, `oportunidad.cancelada` | 11 Gherkin · P · C (último cupo, aceptación en lote) · K · EC-04 | Borrador; alcance en revisión (P-59) |
| [FS-COL-02](./modulos/colaboracion/specs/FS-COL-02-postulaciones.md) (RF-01 a 08) | CU-12, CU-14 / HU-12, HU-25 | Colaboración | API + aplicación | Postulacion, HistorialPostulacion | 6 · `colaboracion.yaml` | `postulacion.creada`, `postulacion.retirada` | 12 Gherkin · P · C (`Idempotency-Key`) · K | Borrador; alcance en revisión (P-59) |
| [FS-COL-03](./modulos/colaboracion/specs/FS-COL-03-publicacion-listado-eventos.md) (RF-01 a 09) | CU-20, CU-21 / HU-15, HU-16 | Colaboración | API + `Reportable` + almacenamiento (portada); trabajador (finalizar) | Evento | 6 · `colaboracion.yaml` | `evento.actualizado`, `evento.cancelado`, `evento.retirado` | 11 Gherkin · P (enlace virtual) · C (`If-Match`) · K | Borrador; desactualizado (H-11) |
| [FS-COL-04](./modulos/colaboracion/specs/FS-COL-04-confirmacion-asistencia.md) (RF-01 a 08) | CU-15 / HU-26 | Colaboración | API + aplicación (cupo atómico); trabajador (recordatorio 24 h) | Asistencia | 5 · `colaboracion.yaml` | — (el recordatorio es una tarea) | 11 Gherkin · P · C (último cupo) · K · EC-04 | Borrador; desactualizado (H-11) |
| [FS-COL-05](./modulos/colaboracion/specs/FS-COL-05-espacios-proyectos.md) (RF-01 a 10) | CU-11 / HU-11 | Colaboración | API + aplicación + `Reportable`; trabajador (vencer invitaciones) | Proyecto, Objetivo, HabilidadBuscada, Miembro, SolicitudUnion, Invitacion, Tarea, Actividad | 17 · `colaboracion.yaml` | `proyecto.solicitud_creada`, `proyecto.solicitud_respondida`, `proyecto.invitacion_creada`, `proyecto.tarea_asignada`, `proyecto.miembro_retirado` | 13 Gherkin · P · C (último lugar) · K · EC-04 | Borrador; desactualizado (H-10, H-16, H-04) |
| [FS-COL-06](./modulos/colaboracion/specs/FS-COL-06-roles-proyectos.md) (RF-01 a 06) | CU-16 / HU-27 | Colaboración | Aplicación (matriz de permisos del proyecto) | Miembro (rol) | 4 · `colaboracion.yaml` | `proyecto.rol_cambiado`, `proyecto.miembro_retirado` | 10 Gherkin · P · C (último administrador) · K · EC-03 | Borrador; desactualizado (H-10) |
| [FS-PLT-01](./modulos/plataforma/specs/FS-PLT-01-gestion-categorias.md) (RF-01 a 09) | CU-26 / HU-20 | Plataforma | API de administración + interfaz pública (`categoriasActivas`, `revisarTexto`) + consumidor de auditoría | Categoria, PalabraProhibida, RegistroAuditoria | 12 · `plataforma.yaml` | `categoria.cambiada`, `auditoria.registrada` | 12 Gherkin · P · C (nombre duplicado) · K | Borrador; desactualizado (H-05, H-08) |
| FS-SRV-01 a 03 _(fase 2)_ | CU-27 a CU-30 / HU-21, HU-22, HU-23, HU-31 | Servicios | — | — | 0 | — | — | Pendiente (sin archivo) |

**Totales:** 22 specs · 167 RF · 256 RN · 253 escenarios Gherkin · 124 endpoints · 25 eventos de dominio. Cada CU-01…CU-30 y HU-01…HU-31 aparece una sola vez en `docs/modulos/`; lo comprueba `scripts/verificar_docs.py`.

## 2. Requisitos no funcionales → escenario → verificación

| Requisito | Escenario de calidad | Componente responsable | Cómo se valida | Cuándo |
|---|---|---|---|---|
| RNF-REN-01, RNF-REN-02 | EC-01, EC-09 (propuesto) | Contenido, Red (búsqueda) | Prueba de carga con 1.000 usuarios simultáneos y datos de volumen realista | Antes del lanzamiento |
| RNF-DIS-05, RNF-REN-05 | EC-02 | Trabajador, Comunicación | Desactivar el servicio de correo en el entorno de pruebas | Antes del lanzamiento |
| RNF-SEG-04, RNF-SEG-05 | EC-03 | Contexto de la petición + cada módulo | Pruebas de permisos que llaman directamente a la API; escaneo OWASP ZAP | Cada pull request; antes de cada salida |
| RNF-CON-01 | EC-04 | Colaboración | Prueba concurrente de 1.000 intentos sobre el último cupo | Pull request del spec |
| RNF-PRI-04 | EC-05 | Comunicación, panel de administración | Revisión de rutas: ninguna devuelve mensajes a quien no es parte | Antes del lanzamiento |
| RNF-MAN-07 | EC-06, EC-07 | Paquete de contratos, todos los módulos | Prueba de arquitectura en la CI (fronteras y ausencia de ciclos) | Cada pull request |
| RNF-MAN-05 | — | Capa API de cada módulo | Comparar el OpenAPI generado con `contracts/api/` | Cada pull request |
| RNF-DIS-07 (propuesto) | EC-08 (propuesto) | Usuarios (autenticación institucional) | Desactivar el Campus Virtual simulado | Antes del lanzamiento |
| RNF-DIS-04 | — | Infraestructura (TI de la Universidad) | Simulacro de restauración completa | Una vez por semestre |

## 3. Decisiones de la reunión del 2026-10-19 → documento → estado

| Decisión | Pregunta | Documento que la registra | Documento que debe cambiar | Estado |
|---|---|---|---|---|
| ~1.000 usuarios simultáneos | P-01 | [SRS §2.7](./srs/Especificacion_Requisitos.md#27-supuestos-y-dependencias), RNF-REN-01, EC-01 | — | Aplicada |
| Infraestructura propia 24/7; base de datos desacoplada | P-02 | [ADR-009](./arquitectura/Registro_Decisiones.md#adr-009-alojamiento) | Vista de despliegue | Aplicada en la ADR |
| Cuentas precreadas, Campus Virtual, externos | P-63 | [ADR-013](./arquitectura/Registro_Decisiones.md#adr-013-autenticación-institucional-y-cuentas-precreadas) | FS-USR-01, 02 y 03, SRS, `usuarios.yaml` | Pendiente en los specs |
| API de admisiones simulada | P-61 | [ADR-014](./arquitectura/Registro_Decisiones.md#adr-014-integración-con-la-api-de-admisiones) | FS-USR-01 | Pendiente en los specs |
| Borrado lógico con trazabilidad | P-12, P-23 | [ADR-015](./arquitectura/Registro_Decisiones.md#adr-015-eliminación-de-cuentas-borrado-lógico) | FS-USR-05, RNF-PRI-06, RNF-PRI-09 | Por gestionar (Oficina Jurídica) |
| Roles Administrador y Moderador | P-07, P-49 | [Preguntas abiertas](./preguntas-abiertas.md) | SRS §2.4 y §2.5, FS-PLT-01, FS-CNT-02, FS-USR-08 | Pendiente en los specs |
| Resto de decisiones (RD-01 a RD-28) | Varias | [Catálogo §5](./requisitos_unilink.md#5-requisitos-decididos-sin-especificar-reunión-del-2026-10-19) | [Riesgos §3](./riesgos_y_brechas_unilink.md#3-cambios-pendientes-por-spec-según-la-reunión-del-2026-10-19) | Pendientes en los specs |

## Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-27 | Gamero | Creación con el análisis integral. |
