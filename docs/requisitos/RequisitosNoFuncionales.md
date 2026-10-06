# Requisitos no funcionales — UniLink

_MVP — Red Profesional Universitaria — Universidad del Magdalena_
_Centro de Interés de Desarrollo Tecnológico e Innovación (CIDTI)_

Este documento define **cómo de bien** debe funcionar UniLink: seguridad, privacidad, rendimiento, disponibilidad, accesibilidad y calidad del código. Aplica a todos los módulos del MVP. Cada requisito tiene un criterio verificable para saber si se cumple.

La organización sigue las características de calidad de la norma ISO/IEC 25010.

## Índice

- [Supuestos de uso](#supuestos-de-uso)
- [1. Seguridad](#1-seguridad)
- [2. Privacidad y protección de datos personales](#2-privacidad-y-protección-de-datos-personales)
- [3. Rendimiento](#3-rendimiento)
- [4. Disponibilidad y recuperación](#4-disponibilidad-y-recuperación)
- [5. Usabilidad](#5-usabilidad)
- [6. Accesibilidad](#6-accesibilidad)
- [7. Compatibilidad](#7-compatibilidad)
- [8. Mantenibilidad](#8-mantenibilidad)
- [9. Observabilidad](#9-observabilidad)
- [10. Despliegue y entornos](#10-despliegue-y-entornos)
- [Valores operativos definidos en los specs](#valores-operativos-definidos-en-los-specs)
- [Cuándo se aplica cada requisito](#cuándo-se-aplica-cada-requisito)
- [Preguntas abiertas](#preguntas-abiertas)

---

## Supuestos de uso

Las cifras de rendimiento y capacidad parten de estos supuestos. Si cambian, hay que revisar las secciones 3 y 4.

| Supuesto | Valor |
|---|---|
| Usuarios registrados el primer año | 5.000 |
| Usuarios registrados que la arquitectura debe soportar sin rediseño | 25.000 |
| Usuarios conectados al mismo tiempo en hora pico | 500 |
| Publicaciones nuevas por día | 300 |
| Mensajes privados por día | 5.000 |
| Horario de mayor uso | Lunes a viernes, 7:00 a. m. a 10:00 p. m. (hora de Colombia) |

---

## 1. Seguridad

| ID | Requisito | Cómo se verifica | Prioridad |
|---|---|---|---|
| RNF-SEG-01 | Toda comunicación entre el navegador y el servidor usa HTTPS con TLS 1.2 o superior. Las peticiones HTTP se redirigen a HTTPS. | Escaneo de configuración TLS con calificación A o superior (por ejemplo, SSL Labs). | Alta |
| RNF-SEG-02 | Las contraseñas se almacenan con un algoritmo de hash lento con sal (bcrypt, scrypt o Argon2). Nunca se guardan, registran ni envían en texto plano. | Revisión de código y de la base de datos. | Alta |
| RNF-SEG-03 | Las cookies de sesión son `HttpOnly`, `Secure` y `SameSite`. Los tokens de sesión se invalidan en el servidor al cerrar sesión o cambiar la contraseña. | Prueba automatizada y revisión con las herramientas del navegador. | Alta |
| RNF-SEG-04 | Todo permiso se valida en el servidor: rol de administrador, privacidad del perfil, membresía y rol en proyectos, visibilidad de enlaces de eventos y acceso a conversaciones. Ocultar un botón en la pantalla no se considera control de acceso. | Pruebas automatizadas que llaman directamente a la API con un usuario sin permiso y esperan un rechazo. | Alta |
| RNF-SEG-05 | La aplicación se protege contra las vulnerabilidades de OWASP Top 10, en particular inyección, XSS, CSRF y control de acceso roto. Todo dato que ingresa el usuario se valida en el servidor y se escapa al mostrarse. | Escaneo automático de seguridad (por ejemplo, OWASP ZAP) antes de cada salida a producción, sin hallazgos altos ni críticos. | Alta |
| RNF-SEG-06 | Los archivos subidos (fotos, imágenes, PDF) se validan por su contenido real y no solo por la extensión, respetan los límites de tamaño de cada spec y se sirven desde un dominio o ruta que no ejecuta código. | Prueba subiendo un archivo con extensión falsa; debe rechazarse. | Alta |
| RNF-SEG-07 | Los límites de uso de los specs (intentos de inicio de sesión, reenvíos de correo, solicitudes de conexión, mensajes por minuto) se aplican en el servidor. Además, la API limita a 100 peticiones por minuto por usuario. | Pruebas de carga que superan cada límite y reciben el error esperado. | Alta |
| RNF-SEG-08 | Las contraseñas, claves de API y credenciales de base de datos no se guardan en el repositorio. Se manejan como variables de entorno o en un gestor de secretos. | Escaneo de secretos en el repositorio dentro de la integración continua. | Alta |
| RNF-SEG-09 | Las dependencias del proyecto se revisan automáticamente en busca de vulnerabilidades conocidas. Las críticas se corrigen en menos de 7 días. | Alerta de dependencias activa en GitHub (Dependabot o similar). | Media |
| RNF-SEG-10 | Las acciones de los administradores de la plataforma quedan en un registro de auditoría que no se puede modificar desde la aplicación y se conserva 2 años. | Revisión del registro tras ejecutar cada acción de administración. | Alta |

## 2. Privacidad y protección de datos personales

UniLink trata datos personales de la comunidad universitaria y debe cumplir la Ley 1581 de 2012 y el Decreto 1377 de 2013. La Universidad del Magdalena actúa como responsable del tratamiento.

| ID | Requisito | Cómo se verifica | Prioridad |
|---|---|---|---|
| RNF-PRI-01 | Solo se recogen los datos necesarios para las funciones de UniLink. Cualquier dato nuevo exige justificar su finalidad en el spec que lo introduce. | Revisión de cada spec antes de pasar a Aprobado. | Alta |
| RNF-PRI-02 | El usuario acepta de forma expresa la política de tratamiento de datos al registrarse, y la plataforma guarda la fecha y la versión aceptada. | Revisión de la base de datos tras un registro. | Alta |
| RNF-PRI-03 | La base de datos y las copias de seguridad se cifran en reposo. | Revisión de la configuración de la infraestructura. | Alta |
| RNF-PRI-04 | Ninguna persona del equipo ni administrador de la plataforma puede leer mensajes privados desde la aplicación. El acceso directo a la base de datos se limita al equipo de infraestructura y queda registrado. | Revisión de permisos de la base de datos y de la aplicación. | Alta |
| RNF-PRI-05 | Las consultas de los titulares sobre sus datos se responden en máximo 10 días hábiles, y los reclamos (corregir o suprimir datos) en máximo 15 días hábiles, como exige la Ley 1581. El canal es el correo de soporte. | Procedimiento documentado y probado con un caso real antes del lanzamiento. | Alta |
| RNF-PRI-06 | Al eliminarse una cuenta ([FS-CTA-05](../specs/cuenta/FS-CTA-05-configuracion-cuenta.md)), sus datos personales se borran también de los archivos subidos y, a más tardar 30 días después, de las copias de seguridad. | Prueba de eliminación y revisión de la política de copias. | Alta |
| RNF-PRI-07 | Los registros técnicos (logs) no contienen contraseñas, tokens, contenido de mensajes privados ni documentos de identidad. | Revisión de una muestra de registros en el entorno de pruebas. | Alta |
| RNF-PRI-08 | Los datos se almacenan en proveedores que garanticen niveles adecuados de protección, según las reglas de transferencia internacional de datos de la Superintendencia de Industria y Comercio. | Revisión jurídica del proveedor de infraestructura en el Sprint 0. | Alta |

## 3. Rendimiento

Los tiempos se miden en el percentil 95 (p95): el 95 % de las peticiones debe cumplirlos con la carga de los [supuestos de uso](#supuestos-de-uso).

| ID | Requisito | Cómo se verifica | Prioridad |
|---|---|---|---|
| RNF-REN-01 | Las consultas de la API responden en menos de 500 ms (p95) y las operaciones de escritura en menos de 1 segundo (p95). | Prueba de carga con 500 usuarios simultáneos. | Alta |
| RNF-REN-02 | El feed, la búsqueda de perfiles y la exploración de oportunidades y proyectos responden en menos de 1 segundo (p95). | Prueba de carga con datos de volumen realista (25.000 usuarios, 100.000 publicaciones). | Alta |
| RNF-REN-03 | En un celular de gama media con conexión 4G, la primera pantalla útil aparece en menos de 3 segundos (métrica Largest Contentful Paint). | Medición con Lighthouse en modo móvil, con puntaje de rendimiento de al menos 80. | Media |
| RNF-REN-04 | Las imágenes se sirven comprimidas y redimensionadas según el tamaño en que se muestran. | Revisión con Lighthouse: sin advertencias de imágenes de gran tamaño. | Media |
| RNF-REN-05 | Las tareas pesadas (envío de correos, generación de notificaciones masivas, tareas programadas) se ejecutan en segundo plano y no retrasan la respuesta al usuario. | Revisión de arquitectura y medición del tiempo de respuesta al publicar. | Alta |

## 4. Disponibilidad y recuperación

| ID | Requisito | Cómo se verifica | Prioridad |
|---|---|---|---|
| RNF-DIS-01 | UniLink está disponible al menos el 99,5 % del tiempo cada mes, sin contar los mantenimientos programados. | Monitoreo externo de disponibilidad. | Alta |
| RNF-DIS-02 | Los mantenimientos programados se hacen fuera del horario de mayor uso y se anuncian en la plataforma con 48 horas de anticipación. | Calendario de mantenimientos y aviso publicado. | Media |
| RNF-DIS-03 | Se hacen copias de seguridad diarias de la base de datos y de los archivos subidos, y se conservan 30 días. | Revisión de la configuración y de las copias existentes. | Alta |
| RNF-DIS-04 | Ante una falla grave, se pierden como máximo 24 horas de datos (RPO) y el servicio se restablece en máximo 8 horas (RTO). | Simulacro de restauración completa una vez por semestre. | Alta |
| RNF-DIS-05 | Si falla un servicio externo (correo, almacenamiento de archivos, tiempo real), el resto de la plataforma sigue funcionando y el usuario ve un mensaje claro. Los correos que no se pudieron enviar se reintentan. | Prueba desactivando cada servicio externo en el entorno de pruebas. | Media |

## 5. Usabilidad

| ID | Requisito | Cómo se verifica | Prioridad |
|---|---|---|---|
| RNF-USA-01 | La interfaz está en español de Colombia. Las fechas se muestran como `dd/mm/aaaa`, la hora en formato de 12 horas con a. m. y p. m., y la zona horaria es la de Colombia (UTC-5). | Revisión de las pantallas. | Alta |
| RNF-USA-02 | El diseño se adapta a pantallas desde 360 px de ancho (celulares) hasta escritorio, y todas las funciones están disponibles en celular. | Pruebas en 360 px, 768 px y 1.280 px de ancho. | Alta |
| RNF-USA-03 | Los mensajes al usuario usan los textos definidos en cada spec (sección 9), en lenguaje claro y sin códigos técnicos. | Revisión de cada spec implementado contra su tabla de mensajes. | Alta |
| RNF-USA-04 | Toda acción que no se puede deshacer (eliminar, cancelar, retirar) pide confirmación, y toda acción exitosa muestra un aviso breve. | Revisión de las pantallas. | Media |
| RNF-USA-05 | Un usuario nuevo puede registrarse, completar su perfil y enviar su primera solicitud de conexión en menos de 10 minutos, sin ayuda. | Prueba con 5 estudiantes antes del lanzamiento. | Media |

## 6. Accesibilidad

| ID | Requisito | Cómo se verifica | Prioridad |
|---|---|---|---|
| RNF-ACC-01 | La plataforma cumple las pautas WCAG 2.1 nivel AA. | Auditoría con herramientas automáticas (por ejemplo, axe) sin errores, más revisión manual de las pantallas principales. | Alta |
| RNF-ACC-02 | Todas las funciones se pueden usar solo con el teclado, con un indicador de foco visible. | Prueba manual recorriendo cada pantalla con la tecla Tab. | Alta |
| RNF-ACC-03 | El texto tiene un contraste de al menos 4,5:1 con su fondo (3:1 para textos grandes). | Herramienta de verificación de contraste. | Alta |
| RNF-ACC-04 | La información nunca depende solo del color: los estados (por ejemplo, de postulaciones) siempre van acompañados de texto. | Revisión de las pantallas. | Alta |
| RNF-ACC-05 | Las imágenes tienen texto alternativo. Al subir imágenes a publicaciones o eventos, el usuario puede escribir una descripción. | Revisión con lector de pantalla (NVDA o VoiceOver) de las pantallas principales. | Media |
| RNF-ACC-06 | La plataforma sigue siendo usable con el zoom del navegador al 200 %. | Prueba manual. | Media |

## 7. Compatibilidad

| ID | Requisito | Cómo se verifica | Prioridad |
|---|---|---|---|
| RNF-COM-01 | UniLink funciona en las dos últimas versiones de Chrome, Edge, Firefox y Safari en computador, y de Chrome en Android y Safari en iOS. | Pruebas manuales de los flujos principales en cada navegador antes de cada salida a producción. | Alta |
| RNF-COM-02 | El MVP es una aplicación web; no incluye aplicaciones nativas para celular. | — | — |
| RNF-COM-03 | Los archivos de calendario exportados (`.ics`) se abren correctamente en Google Calendar, Outlook y el calendario de iOS. | Prueba manual en cada aplicación. | Media |

## 8. Mantenibilidad

| ID | Requisito | Cómo se verifica | Prioridad |
|---|---|---|---|
| RNF-MAN-01 | Cada regla de negocio (RN) de los specs tiene al menos una prueba automatizada, y los criterios de aceptación en Gherkin se usan como base de las pruebas de aceptación. | Revisión en cada pull request; parte de la _Definition of Done_. | Alta |
| RNF-MAN-02 | La cobertura de pruebas del código de negocio es de al menos 70 %. | Reporte de cobertura en la integración continua. | Media |
| RNF-MAN-03 | Todo cambio entra a la rama principal mediante un pull request revisado por al menos otra persona, con las pruebas y el análisis de estilo (lint) en verde. | Reglas de protección de rama en GitHub. | Alta |
| RNF-MAN-04 | Los mensajes de commit siguen la convención _Conventional Commits_ (`feat:`, `fix:`, `docs:`…), como ya se hace en el repositorio. | Revisión del historial. | Baja |
| RNF-MAN-05 | La API está documentada con OpenAPI y la documentación se genera desde el código. | La documentación de la API está disponible en el entorno de pruebas. | Media |
| RNF-MAN-06 | Si una implementación cambia el comportamiento definido en un spec, el spec se actualiza en el mismo pull request. | Revisión en cada pull request. | Alta |

## 9. Observabilidad

| ID | Requisito | Cómo se verifica | Prioridad |
|---|---|---|---|
| RNF-OBS-01 | La aplicación genera registros estructurados con fecha, nivel, módulo y un identificador por petición, respetando RNF-PRI-07. | Revisión de los registros en el entorno de pruebas. | Alta |
| RNF-OBS-02 | Los errores del servidor y del navegador se envían a una herramienta de monitoreo de errores que alerta al equipo. | Error provocado en pruebas que llega a la herramienta. | Alta |
| RNF-OBS-03 | El equipo recibe una alerta si la plataforma deja de responder o si el tiempo de respuesta supera el doble de lo definido en la sección 3 durante 5 minutos. | Prueba de la alerta en el entorno de pruebas. | Media |
| RNF-OBS-04 | Se miden indicadores de uso del producto (usuarios activos, conexiones, publicaciones, postulaciones) sin rastrear a usuarios individuales con herramientas de terceros. | Panel de indicadores disponible para el equipo. | Baja |

## 10. Despliegue y entornos

| ID | Requisito | Cómo se verifica | Prioridad |
|---|---|---|---|
| RNF-DES-01 | Existen tres entornos separados: desarrollo, pruebas y producción. Producción nunca usa datos de prueba, y pruebas nunca usa datos reales sin anonimizar. | Revisión de la infraestructura. | Alta |
| RNF-DES-02 | El despliegue es automático desde el repositorio: al unir a la rama principal se despliega en pruebas, y la salida a producción requiere una aprobación manual. | Revisión de la integración continua. | Alta |
| RNF-DES-03 | Cualquier integrante puede levantar el proyecto en su computador siguiendo el README, con un solo comando para los servicios necesarios. | Prueba con un integrante nuevo. | Media |
| RNF-DES-04 | Un despliegue fallido se puede revertir a la versión anterior en menos de 15 minutos. | Simulacro de reversión. | Media |

---

## Valores operativos definidos en los specs

Estos valores ya están definidos en los specs funcionales. Se reúnen aquí para tener una vista única; **la fuente de verdad sigue siendo cada spec**.

| Tema | Valor | Spec |
|---|---|---|
| Política de contraseñas | Mínimo 8 caracteres, con mayúscula, minúscula y número | [FS-CTA-01](../specs/cuenta/FS-CTA-01-registro.md) |
| Enlace de verificación de correo | Vence en 24 horas; máximo 3 reenvíos por hora | [FS-CTA-01](../specs/cuenta/FS-CTA-01-registro.md) |
| Cuentas sin verificar | Se eliminan a los 7 días | [FS-CTA-01](../specs/cuenta/FS-CTA-01-registro.md) |
| Bloqueo por intentos fallidos | 5 intentos, bloqueo de 15 minutos | [FS-CTA-02](../specs/cuenta/FS-CTA-02-inicio-sesion.md) |
| Duración de la sesión | 2 horas de inactividad, o 30 días con "Mantener sesión iniciada" | [FS-CTA-02](../specs/cuenta/FS-CTA-02-inicio-sesion.md) |
| Enlace de recuperación de contraseña | Vence en 1 hora | [FS-CTA-03](../specs/cuenta/FS-CTA-03-recuperar-contrasena.md) |
| Eliminación de cuenta | Definitiva a los 30 días | [FS-CTA-05](../specs/cuenta/FS-CTA-05-configuracion-cuenta.md) |
| Generación de hoja de vida | Menos de 10 segundos | [FS-PRF-03](../specs/perfil/FS-PRF-03-hoja-de-vida-pdf.md) |
| Solicitudes de conexión | Máximo 30 por día; vencen a los 90 días | [FS-RED-01](../specs/red/FS-RED-01-solicitudes-conexion.md) |
| Indicador de notificaciones | Se actualiza en menos de 60 segundos | [FS-NOT-01](../specs/notificaciones/FS-NOT-01-centro-notificaciones.md) |
| Conservación de notificaciones | 90 días | [FS-NOT-01](../specs/notificaciones/FS-NOT-01-centro-notificaciones.md) |
| Entrega de mensajes | Menos de 2 segundos; máximo 60 mensajes por minuto | [FS-MSG-01](../specs/mensajeria/FS-MSG-01-mensajeria-privada.md) |
| Archivos | Imágenes de máximo 5 MB; PDF de máximo 10 MB | [FS-PRF-01](../specs/perfil/FS-PRF-01-perfil-profesional.md), [FS-CNT-01](../specs/contenido/FS-CNT-01-publicaciones-feed.md) |

## Cuándo se aplica cada requisito

Los requisitos no funcionales son **transversales**: no se implementan en un solo sprint, sino que cada sprint debe cumplir los que le aplican.

| Momento | Requisitos |
|---|---|
| **Sprint 0** (antes del Sprint 1) | Elegir infraestructura y proveedores (RNF-PRI-08), montar entornos y despliegue (RNF-DES-01 a 04), integración continua con pruebas, lint y escaneos (RNF-MAN-03, RNF-SEG-08, RNF-SEG-09), registros y monitoreo de errores (RNF-OBS-01, RNF-OBS-02), copias de seguridad (RNF-DIS-03). |
| **Sprint 1** | Seguridad de contraseñas y sesiones (RNF-SEG-01 a 03), límites de uso (RNF-SEG-07), consentimiento de datos (RNF-PRI-02). |
| **Todos los sprints** | Control de acceso en el servidor (RNF-SEG-04), OWASP (RNF-SEG-05), rendimiento (sección 3), usabilidad (sección 5), accesibilidad (sección 6), mantenibilidad (sección 8). Forman parte de la _Definition of Done_. |
| **Antes del lanzamiento** | Prueba de carga (RNF-REN-01, 02), auditoría de accesibilidad (RNF-ACC-01), escaneo de seguridad (RNF-SEG-05), simulacro de restauración (RNF-DIS-04), procedimiento de consultas y reclamos de datos (RNF-PRI-05), prueba con estudiantes (RNF-USA-05). |

## Preguntas abiertas

- [ ] ¿Las cifras de los [supuestos de uso](#supuestos-de-uso) son realistas? Conviene validarlas con la cantidad actual de estudiantes, profesores y administrativos de la universidad.
- [ ] ¿UniLink se alojará en la infraestructura de la universidad o en un proveedor en la nube? Afecta RNF-PRI-08, los costos y quién opera los respaldos.
- [ ] ¿La universidad ya tiene registrada una base de datos de la comunidad en el Registro Nacional de Bases de Datos de la SIC, o UniLink requiere un registro nuevo?
- [ ] ¿El horario de soporte y la disponibilidad del 99,5 % son compatibles con el tamaño del equipo que operará la plataforma?
