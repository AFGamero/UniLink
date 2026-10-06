# Casos de Uso — UniLink

_MVP — Red Profesional Universitaria — Universidad del Magdalena_
_Centro de Interés de Desarrollo Tecnológico e Innovación (CIDTI)_

Este documento describe los 30 casos de uso de UniLink. Los casos CU-01 a CU-26 delimitan el alcance funcional del MVP; los casos CU-27 a CU-30 (módulo de servicios) corresponden a la **fase 2**. Cada caso de uso incluye actor, descripción, precondiciones, flujo principal, flujos alternativos/excepciones, postcondiciones y prioridad, siguiendo la estructura recomendada para la especificación de requisitos del proyecto.

## Índice

- [Casos de Uso — UniLink](#casos-de-uso--unilink)
  - [Índice](#índice)
  - [Actores](#actores)
  - [CU-01 — Registrar cuenta](#cu-01--registrar-cuenta)
  - [CU-02 — Iniciar sesión](#cu-02--iniciar-sesión)
  - [CU-03 — Administrar cuenta](#cu-03--administrar-cuenta)
  - [CU-04 — Crear/editar perfil profesional](#cu-04--creareditar-perfil-profesional)
  - [CU-05 — Buscar y visualizar perfiles](#cu-05--buscar-y-visualizar-perfiles)
  - [CU-06 — Enviar solicitud de conexión](#cu-06--enviar-solicitud-de-conexión)
  - [CU-07 — Responder solicitud de conexión](#cu-07--responder-solicitud-de-conexión)
  - [CU-08 — Publicar contenido](#cu-08--publicar-contenido)
  - [CU-09 — Visualizar publicaciones](#cu-09--visualizar-publicaciones)
  - [CU-10 — Enviar mensaje privado](#cu-10--enviar-mensaje-privado)
  - [CU-11 — Gestionar espacio de proyectos](#cu-11--gestionar-espacio-de-proyectos)
  - [CU-12 — Explorar oportunidades](#cu-12--explorar-oportunidades)
  - [CU-13 — Sugerir conexiones iniciales (Onboarding)](#cu-13--sugerir-conexiones-iniciales-onboarding)
  - [CU-14 — Gestionar estado de postulaciones](#cu-14--gestionar-estado-de-postulaciones)
  - [CU-15 — Confirmar asistencia a eventos (RSVP)](#cu-15--confirmar-asistencia-a-eventos-rsvp)
  - [CU-16 — Administrar roles en espacios de proyectos](#cu-16--administrar-roles-en-espacios-de-proyectos)
  - [CU-17 — Recuperar contraseña](#cu-17--recuperar-contraseña)
  - [CU-18 — Seleccionar preferencias de contenido](#cu-18--seleccionar-preferencias-de-contenido)
  - [CU-19 — Generar hoja de vida en PDF](#cu-19--generar-hoja-de-vida-en-pdf)
  - [CU-20 — Publicar evento](#cu-20--publicar-evento)
  - [CU-21 — Visualizar eventos](#cu-21--visualizar-eventos)
  - [CU-22 — Publicar oportunidades y gestionar postulaciones](#cu-22--publicar-oportunidades-y-gestionar-postulaciones)
  - [CU-23 — Consultar notificaciones](#cu-23--consultar-notificaciones)
  - [CU-24 — Administrar cuentas de usuario](#cu-24--administrar-cuentas-de-usuario)
  - [CU-25 — Moderar contenido (publicaciones y eventos)](#cu-25--moderar-contenido-publicaciones-y-eventos)
  - [CU-26 — Administrar categorías](#cu-26--administrar-categorías)
  - [CU-27 — Verificar credenciales](#cu-27--verificar-credenciales) _(fase 2)_
  - [CU-28 — Publicar servicio](#cu-28--publicar-servicio) _(fase 2)_
  - [CU-29 — Registrar oferente de servicios externo](#cu-29--registrar-oferente-de-servicios-externo) _(fase 2)_
  - [CU-30 — Solicitar servicio](#cu-30--solicitar-servicio) _(fase 2)_

---

## Actores

| Actor | Descripción |
|---|---|
| **Visitante** | Persona no autenticada que puede registrarse en la plataforma. |
| **Usuario autenticado** | Estudiante, profesor o personal administrativo con cuenta activa y verificada. Desde la fase 2, también egresados y personal tercerizado. |
| **Responsable de oportunidad** | Usuario autenticado que publica una oportunidad (investigación, proyecto o voluntariado) y gestiona sus postulaciones. |
| **Administrador de proyecto** | Usuario autenticado que creó un espacio de proyecto o recibió el rol de administrador en él. |
| **Administrador de la plataforma** | Miembro del equipo de UniLink encargado de gestionar cuentas, moderar contenido, administrar categorías y validar credenciales. |

---

## CU-01 — Registrar cuenta

**Actor(es):** Visitante (usuario no autenticado)

**Descripción:** Permite a un nuevo usuario crear una cuenta en UniLink proporcionando sus datos personales y académicos para unirse a la red profesional universitaria.

**Precondiciones:** El usuario no debe tener una cuenta previamente registrada con el mismo correo institucional.

**Flujo principal:**

1. El usuario accede a la página de registro.
2. Completa el formulario con nombre, correo institucional, contraseña y programa académico.
3. Opcionalmente, selecciona las categorías de contenido de su interés ([CU-18](#cu-18--seleccionar-preferencias-de-contenido)).
4. El sistema valida el formato de los datos ingresados.
5. El sistema envía un enlace de verificación al correo institucional, válido por 24 horas.
6. El usuario confirma su correo mediante el enlace recibido.
7. El sistema activa la cuenta y redirige al usuario para completar su perfil ([CU-04](#cu-04--creareditar-perfil-profesional)) y, a continuación, al paso de sugerencias de conexión ([CU-13](#cu-13--sugerir-conexiones-iniciales-onboarding)).

**Flujos alternativos / excepciones:**

- 4a. El correo ingresado no corresponde a un dominio institucional válido: el sistema muestra un mensaje de error y no permite continuar. En la fase 2, si el usuario es egresado o personal tercerizado, el sistema le ofrecerá registrarse como oferente de servicios externo ([CU-29](#cu-29--registrar-oferente-de-servicios-externo)).
- 4b. El correo ya se encuentra registrado: el sistema notifica al usuario y sugiere iniciar sesión o recuperar su contraseña ([CU-17](#cu-17--recuperar-contraseña)).
- 6a. El enlace de verificación expira antes de ser usado: el sistema permite solicitar un nuevo enlace.

**Postcondiciones:** Se crea una cuenta activa asociada al usuario, quien queda autenticado y con perfil pendiente de completar.

**Prioridad:** Alta

---

## CU-02 — Iniciar sesión

**Actor(es):** Usuario registrado (estudiante, profesor o personal administrativo; en la fase 2, también egresado o personal tercerizado)

**Descripción:** Permite al usuario autenticarse en la plataforma para acceder a sus funcionalidades y datos personales.

**Precondiciones:** El usuario debe contar con una cuenta previamente registrada y verificada.

**Flujo principal:**

1. El usuario accede a la página de inicio de sesión.
2. Ingresa su correo electrónico y contraseña.
3. El sistema valida las credenciales.
4. El sistema otorga acceso y redirige al panel principal (feed).

**Flujos alternativos / excepciones:**

- 3a. Las credenciales son incorrectas: el sistema muestra un mensaje de error e indica el número de intentos restantes (máximo 5 intentos fallidos consecutivos).
- 3b. La cuenta no ha sido verificada: el sistema solicita completar la verificación antes de continuar.
- 3c. El usuario excede el número máximo de intentos: el sistema bloquea el acceso durante 15 minutos y sugiere recuperar la contraseña ([CU-17](#cu-17--recuperar-contraseña)).
- 3d. La cuenta está suspendida o desactivada por un administrador ([CU-24](#cu-24--administrar-cuentas-de-usuario)): el sistema impide el acceso e informa el estado de la cuenta.
- 4a. Es el primer ingreso del usuario: el sistema ejecuta el onboarding ([CU-13](#cu-13--sugerir-conexiones-iniciales-onboarding)) antes de mostrar el panel principal.

**Postcondiciones:** El usuario queda autenticado y con una sesión activa en la plataforma.

**Prioridad:** Alta

---

## CU-03 — Administrar cuenta

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario gestionar la información de su cuenta, incluyendo datos personales, configuración de seguridad, privacidad y preferencias.

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El usuario accede a la sección de configuración de cuenta.
2. Selecciona el dato que desea modificar (nombre, correo, contraseña, foto de perfil, preferencias de notificación, preferencias de contenido o privacidad del perfil).
3. Ingresa la nueva información y confirma los cambios.
4. El sistema valida y guarda los cambios.
5. El sistema confirma la actualización al usuario.

La **privacidad del perfil** admite dos niveles: _visible para toda la comunidad_ (valor por defecto) o _visible solo para mis conexiones_. En ambos casos, el nombre, la foto y el programa académico permanecen visibles en los resultados de búsqueda.

**Flujos alternativos / excepciones:**

- 3a. Los datos ingresados no cumplen el formato requerido: el sistema muestra un mensaje de error y no guarda los cambios.
- 3b. El usuario intenta cambiar su correo a uno ya registrado por otra cuenta: el sistema rechaza el cambio.
- 3c. El usuario cambia su correo: el nuevo correo debe verificarse con un enlace antes de reemplazar al anterior.
- 3d. El usuario solicita eliminar su cuenta: el sistema pide su contraseña, desactiva la cuenta y la elimina definitivamente tras 30 días, salvo que el usuario vuelva a iniciar sesión en ese plazo.

**Postcondiciones:** La información de la cuenta queda actualizada.

**Prioridad:** Media

---

## CU-04 — Crear/editar perfil profesional

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario construir y mantener su identidad profesional en la plataforma, incluyendo biografía, habilidades, intereses, experiencia, proyectos y logros académicos, además de lo que puede aportar a la comunidad y lo que necesita de ella.

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El usuario accede a la sección de edición de perfil.
2. Completa o modifica los campos: biografía, habilidades, intereses, experiencia, proyectos, logros, **"Puedo aportar"** y **"Necesito"**.
3. El sistema valida la información ingresada.
4. El sistema guarda los cambios.
5. El perfil actualizado queda visible para otros usuarios, según la configuración de privacidad definida en [CU-03](#cu-03--administrar-cuenta).

Son **campos obligatorios**: nombre, programa académico (o tipo de vínculo, para egresados y tercerizados) y al menos una habilidad. Los demás campos son opcionales.

Los campos **"Puedo aportar"** (por ejemplo, "asesoría en Python", "diseño gráfico") y **"Necesito"** (por ejemplo, "un diseñador para mi proyecto", "mentoría en investigación") son listas de etiquetas. La plataforma los cruza para encontrar perfiles complementarios: lo que un usuario necesita con lo que otro puede aportar. Este cruce alimenta las sugerencias de conexión ([CU-13](#cu-13--sugerir-conexiones-iniciales-onboarding)) y la búsqueda de perfiles ([CU-05](#cu-05--buscar-y-visualizar-perfiles)).

**Flujos alternativos / excepciones:**

- 3a. El usuario deja campos obligatorios vacíos: el sistema indica los campos pendientes y no permite guardar hasta completarlos.

**Postcondiciones:** El perfil profesional del usuario queda creado o actualizado y disponible para ser consultado por otros usuarios.

**Prioridad:** Alta

---

## CU-05 — Buscar y visualizar perfiles

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario descubrir otros miembros de la comunidad universitaria mediante búsqueda por nombre, habilidades, intereses o programa académico.

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El usuario accede al buscador de perfiles.
2. Ingresa un término de búsqueda o aplica filtros (habilidades, intereses, programa académico, facultad, "Puede aportar" o "Necesita").
3. El sistema procesa la búsqueda y muestra los perfiles coincidentes con una vista previa de información básica.
4. El usuario selecciona un perfil para visualizar su detalle completo.

**Flujos alternativos / excepciones:**

- 3a. No se encuentran perfiles coincidentes: el sistema informa que no hay resultados y sugiere ajustar los filtros.
- 4a. El perfil seleccionado es visible solo para conexiones y el usuario no está conectado con su dueño: el sistema muestra únicamente la información básica y la opción de enviar solicitud de conexión ([CU-06](#cu-06--enviar-solicitud-de-conexión)).

**Postcondiciones:** El usuario obtiene un listado de perfiles relevantes según su búsqueda y puede consultar el detalle de cualquiera de ellos, respetando su configuración de privacidad.

**Prioridad:** Alta

---

## CU-06 — Enviar solicitud de conexión

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario establecer una conexión profesional con otro miembro de la plataforma enviando una solicitud que el destinatario puede aceptar o rechazar.

**Precondiciones:** El usuario debe estar autenticado y visualizar el perfil de otro usuario con el cual aún no tiene una conexión ni solicitud pendiente.

**Flujo principal:**

1. El usuario visualiza el perfil de otro miembro.
2. Selecciona la opción de enviar solicitud de conexión.
3. El sistema registra la solicitud como pendiente y notifica al destinatario.

**Flujos alternativos / excepciones:**

- 1a. Ya existe una solicitud pendiente o una conexión establecida entre ambos usuarios: el sistema no permite enviar una nueva solicitud y muestra el estado actual.
- 3a. El usuario cancela una solicitud que envió y sigue pendiente: el sistema la elimina sin notificar al destinatario.

**Postcondiciones:** La solicitud queda registrada como pendiente hasta que el destinatario responda.

**Prioridad:** Alta

---

## CU-07 — Responder solicitud de conexión

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario responder a las solicitudes de conexión recibidas, aceptándolas o rechazándolas según su interés.

**Precondiciones:** El usuario debe tener al menos una solicitud de conexión pendiente por revisar.

**Flujo principal:**

1. El usuario recibe una notificación de nueva solicitud de conexión.
2. Revisa el perfil del solicitante.
3. Acepta o rechaza la solicitud.
4. El sistema actualiza la red de conexiones de ambos usuarios y notifica al solicitante el resultado.

**Flujos alternativos / excepciones:**

- 3a. El usuario rechaza la solicitud: el sistema descarta la solicitud sin notificar el motivo al solicitante.
- 4a. Más adelante, cualquiera de los dos usuarios elimina la conexión: el sistema los desconecta sin notificar al otro.

**Postcondiciones:** La solicitud queda resuelta (aceptada o rechazada) y, en caso de aceptación, ambos usuarios quedan conectados.

**Prioridad:** Alta

---

## CU-08 — Publicar contenido

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario compartir publicaciones académicas o profesionales, como proyectos, logros, oportunidades o artículos, con la comunidad.

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El usuario selecciona la opción de crear publicación.
2. Ingresa el contenido: título, descripción, categoría y, opcionalmente, archivos adjuntos.
3. El sistema valida el contenido ingresado.
4. El sistema publica el contenido y lo muestra en el feed de sus conexiones y de los usuarios interesados en esa categoría ([CU-18](#cu-18--seleccionar-preferencias-de-contenido)).

**Flujos alternativos / excepciones:**

- 3a. El contenido no cumple con las políticas de uso de la plataforma: el sistema rechaza la publicación e informa el motivo.

**Postcondiciones:** La publicación queda visible en el feed de las conexiones del usuario y de los usuarios interesados en su categoría. Puede ser reportada y moderada según [CU-25](#cu-25--moderar-contenido-publicaciones-y-eventos).

**Prioridad:** Media

---

## CU-09 — Visualizar publicaciones

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario consultar las publicaciones de su red de conexiones y de las categorías de su interés, filtradas por categoría o relevancia.

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El usuario accede al feed de publicaciones.
2. Navega por las publicaciones o aplica filtros por categoría.
3. El sistema muestra las publicaciones correspondientes con opciones de interacción (comentar, reaccionar, compartir).

**Flujos alternativos / excepciones:**

- 2a. No existen publicaciones que coincidan con el filtro aplicado: el sistema muestra un mensaje indicándolo.

**Postcondiciones:** El usuario visualiza el listado de publicaciones solicitado.

**Prioridad:** Media

---

## CU-10 — Enviar mensaje privado

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario comunicarse de forma privada (1 a 1) con otro miembro con quien tenga una conexión establecida, una postulación aceptada o, en la fase 2, una solicitud de servicio activa.

**Precondiciones:** Debe existir una conexión establecida entre el usuario y el destinatario, una postulación aceptada entre el responsable de una oportunidad y el postulante ([CU-22](#cu-22--publicar-oportunidades-y-gestionar-postulaciones)), o, en la fase 2, una solicitud de servicio activa entre ambos ([CU-30](#cu-30--solicitar-servicio)).

**Flujo principal:**

1. El usuario selecciona una conexión de su red.
2. Abre el chat privado correspondiente.
3. Escribe y envía el mensaje.
4. El sistema entrega el mensaje y notifica al destinatario.

**Flujos alternativos / excepciones:**

- 1a. No existe conexión, postulación aceptada ni solicitud de servicio activa con el usuario seleccionado: el sistema no permite iniciar el chat.

**Postcondiciones:** El mensaje queda registrado en la conversación y disponible para ambos usuarios.

**Prioridad:** Alta

---

## CU-11 — Gestionar espacio de proyectos

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario crear, unirse y colaborar en espacios de proyectos dedicados para trabajar en conjunto con otros miembros de la plataforma.

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El usuario crea un nuevo proyecto o solicita unirse a uno existente.
2. En caso de creación, define nombre, descripción, perfiles requeridos (por ejemplo, desarrollador o diseñador), número máximo de integrantes, tareas y objetivos del proyecto. El creador queda como administrador del proyecto.
3. En caso de solicitud de unión, el sistema notifica a los administradores del proyecto, quienes la aprueban o rechazan.
4. Los miembros colaboran dentro del espacio del proyecto según su nivel de acceso ([CU-16](#cu-16--administrar-roles-en-espacios-de-proyectos)).

**Flujos alternativos / excepciones:**

- 1a. El usuario solicita unirse a un proyecto que ya alcanzó el número máximo de integrantes: el sistema no permite la solicitud e informa el motivo.
- 3a. El administrador rechaza la solicitud de unión: el sistema notifica al solicitante.
- 4a. Un miembro decide abandonar el proyecto: el sistema lo retira del espacio. Si es el único administrador, se aplica la restricción 3a de [CU-16](#cu-16--administrar-roles-en-espacios-de-proyectos).

**Postcondiciones:** El espacio de proyecto queda creado o el usuario queda incorporado como miembro de un proyecto existente.

**Prioridad:** Media

---

## CU-12 — Explorar oportunidades

**Actor(es):** Usuario autenticado; Responsable de oportunidad (notificado)

**Descripción:** Permite al usuario consultar y postularse a oportunidades de investigación, proyectos y voluntariado publicadas en la plataforma por un responsable ([CU-22](#cu-22--publicar-oportunidades-y-gestionar-postulaciones)).

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El usuario accede a la sección de oportunidades.
2. Explora las ofertas disponibles, filtrando por categoría (investigación, proyectos, voluntariado).
3. Selecciona una oportunidad para ver su detalle.
4. Se postula directamente a la oportunidad.
5. El sistema registra la postulación con estado "Enviada" y notifica al responsable de la oportunidad.

**Flujos alternativos / excepciones:**

- 4a. El usuario ya se encuentra postulado a la misma oportunidad: el sistema no permite una nueva postulación y muestra el estado actual.
- 4b. La oportunidad fue cerrada por su responsable: el sistema no permite la postulación e informa el motivo.

**Postcondiciones:** La postulación queda registrada y visible tanto para el usuario ([CU-14](#cu-14--gestionar-estado-de-postulaciones)) como para el responsable de la oportunidad ([CU-22](#cu-22--publicar-oportunidades-y-gestionar-postulaciones)).

**Prioridad:** Media

---

## CU-13 — Sugerir conexiones iniciales (Onboarding)

**Actor(es):** Usuario autenticado (nuevo)

**Descripción:** Permite presentar sugerencias de conexiones inmediatas (compañeros de facultad o espacios de proyectos) durante el primer ingreso del usuario a la plataforma, con el fin de prevenir el "feed vacío" (cold start) y asegurar que visualice contenido relevante.

**Precondiciones:** El usuario ha completado su registro y accede a la plataforma por primera vez.

**Flujo principal:**

1. El sistema detecta que es el primer inicio de sesión del usuario.
2. El sistema analiza el programa académico, la facultad, las preferencias de contenido ([CU-18](#cu-18--seleccionar-preferencias-de-contenido)) y los campos "Puedo aportar" y "Necesito" del usuario ([CU-04](#cu-04--creareditar-perfil-profesional)) para generar sugerencias.
3. El sistema muestra una pantalla de *onboarding* con una lista de perfiles sugeridos y espacios de proyectos relevantes. Cuando una sugerencia se debe a perfiles complementarios, el sistema indica el motivo (por ejemplo, "Puede aportar diseño gráfico, que tú necesitas").
4. El usuario selecciona a los compañeros o proyectos con los que desea conectar de forma inmediata.
5. El sistema envía las solicitudes de conexión (y de unión a proyectos) automáticamente y redirige al usuario a su panel principal (feed).

**Flujos alternativos / excepciones:**

- 4a. El usuario decide omitir el paso de sugerencias: el sistema lo redirige al panel principal sin enviar solicitudes y llena el feed con publicaciones recientes de las categorías de su interés o, si no eligió ninguna, con las publicaciones más recientes de su facultad.

**Postcondiciones:** El usuario inicia su experiencia en la plataforma con un feed con contenido, alimentado por sus conexiones, solicitudes o preferencias.

**Prioridad:** Media

---

## CU-14 — Gestionar estado de postulaciones

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario acceder a un panel específico para ver y hacer seguimiento al estado de sus postulaciones a oportunidades ("Enviada", "En revisión", "Aceptada" o "Rechazada"). Los cambios de estado los realiza el responsable de la oportunidad ([CU-22](#cu-22--publicar-oportunidades-y-gestionar-postulaciones)).

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El usuario accede al panel de gestión de postulaciones.
2. El sistema recupera y muestra el listado de oportunidades a las que el usuario se ha postulado.
3. El sistema muestra el estado actual de cada postulación ("Enviada", "En revisión", "Aceptada" o "Rechazada").
4. El usuario selecciona una postulación para visualizar el historial de cambios de estado o retroalimentación.

**Flujos alternativos / excepciones:**

- 2a. El usuario no tiene postulaciones activas ni pasadas: el sistema muestra un mensaje indicando que no hay postulaciones y sugiere explorar nuevas oportunidades.
- 4a. El usuario retira una postulación en estado "Enviada" o "En revisión": el sistema la marca como "Retirada" y notifica al responsable de la oportunidad.

**Postcondiciones:** El usuario se mantiene informado sobre el avance y resolución de sus postulaciones.

**Prioridad:** Alta

---

## CU-15 — Confirmar asistencia a eventos (RSVP)

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario confirmar su asistencia (RSVP) a un evento publicado, visualizar qué otros miembros asistirán y agregar el evento a su calendario personal.

**Precondiciones:** El usuario debe estar autenticado y visualizar la página de detalle de un evento publicado ([CU-20](#cu-20--publicar-evento)) que aún no ha ocurrido.

**Flujo principal:**

1. El usuario visualiza un evento de su interés.
2. Selecciona la opción para confirmar asistencia ("Asistiré").
3. El sistema registra al usuario en la lista de asistentes del evento.
4. El sistema habilita la visualización de los demás asistentes confirmados para este usuario.
5. El sistema ofrece la opción de exportar o agregar el evento a un calendario personal.

**Flujos alternativos / excepciones:**

- 2a. El usuario cambia de opinión y retira su confirmación: el sistema lo elimina de la lista de asistentes y actualiza la vista.

**Postcondiciones:** El usuario queda registrado como asistente, aportando métricas al creador del evento y facilitando la interacción con otros asistentes.

**Prioridad:** Alta

---

## CU-16 — Administrar roles en espacios de proyectos

**Actor(es):** Administrador de proyecto

**Descripción:** Permite gestionar los niveles de acceso de los miembros dentro de un espacio de proyecto mediante roles granulares (visualizador, editor, administrador). Estos niveles de acceso son distintos de los perfiles requeridos definidos al crear el proyecto ([CU-11](#cu-11--gestionar-espacio-de-proyectos)).

**Precondiciones:** El usuario debe tener el rol de administrador o creador dentro de un espacio de proyecto existente.

**Flujo principal:**

1. El administrador accede a la configuración de miembros del proyecto.
2. Selecciona a un miembro actual del proyecto.
3. Modifica su nivel de acceso asignando un rol específico (visualizador, editor, administrador).
4. El sistema valida y aplica los nuevos permisos granulares al usuario seleccionado.
5. El sistema notifica al miembro sobre el cambio en su rol.

**Flujos alternativos / excepciones:**

- 3a. El administrador intenta removerse a sí mismo como administrador sin asignar a otro en su reemplazo: el sistema bloquea la acción para evitar que el proyecto quede sin gestión.

**Postcondiciones:** Los permisos del proyecto quedan actualizados, limitando o expandiendo las acciones del miembro afectado según su nuevo rol.

**Prioridad:** Media

---

## CU-17 — Recuperar contraseña

**Actor(es):** Usuario registrado (no autenticado)

**Descripción:** Permite al usuario restablecer su contraseña cuando la ha olvidado o su cuenta fue bloqueada temporalmente por intentos fallidos.

**Precondiciones:** El usuario debe tener una cuenta registrada y verificada.

**Flujo principal:**

1. El usuario selecciona la opción "¿Olvidaste tu contraseña?" en la página de inicio de sesión.
2. Ingresa el correo asociado a su cuenta.
3. El sistema envía al correo un enlace de restablecimiento válido por 1 hora.
4. El usuario abre el enlace e ingresa una nueva contraseña.
5. El sistema valida la contraseña, la guarda, cierra las sesiones abiertas y redirige al inicio de sesión.

**Flujos alternativos / excepciones:**

- 2a. El correo no corresponde a ninguna cuenta: el sistema muestra el mismo mensaje de confirmación que en el flujo principal, para no revelar qué correos están registrados.
- 4a. El enlace expiró o ya fue usado: el sistema informa el problema y permite solicitar uno nuevo.
- 5a. La nueva contraseña no cumple la política de seguridad: el sistema indica los requisitos y no guarda el cambio.

**Postcondiciones:** La contraseña de la cuenta queda actualizada y el bloqueo temporal, si existía, se levanta.

**Prioridad:** Alta

---

## CU-18 — Seleccionar preferencias de contenido

**Actor(es):** Visitante (durante el registro); Usuario autenticado (desde la configuración de cuenta)

**Descripción:** Permite al usuario elegir las categorías de publicaciones, proyectos y eventos que le interesan, para que la plataforma le muestre contenido relacionado.

**Precondiciones:** El usuario se encuentra en el formulario de registro ([CU-01](#cu-01--registrar-cuenta)) o en la configuración de su cuenta ([CU-03](#cu-03--administrar-cuenta)).

**Flujo principal:**

1. El sistema muestra las categorías activas ([CU-26](#cu-26--administrar-categorías)) agrupadas por tipo de contenido.
2. El usuario selecciona una o varias categorías.
3. El sistema guarda las preferencias asociadas a su perfil.
4. El sistema utiliza estas preferencias para ordenar el feed ([CU-09](#cu-09--visualizar-publicaciones)) y generar sugerencias ([CU-13](#cu-13--sugerir-conexiones-iniciales-onboarding)).

**Flujos alternativos / excepciones:**

- 2a. El usuario no selecciona ninguna categoría: el sistema permite continuar sin guardar preferencias.

**Postcondiciones:** Las preferencias de contenido del usuario quedan registradas.

**Prioridad:** Media

---

## CU-19 — Generar hoja de vida en PDF

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario descargar un documento PDF con la información de su perfil profesional organizada como hoja de vida.

**Precondiciones:** El usuario debe estar autenticado y tener su perfil profesional creado ([CU-04](#cu-04--creareditar-perfil-profesional)).

**Flujo principal:**

1. El usuario accede a su perfil y selecciona la opción "Descargar hoja de vida".
2. El sistema recopila los datos personales, biografía, habilidades, experiencia, proyectos y logros del perfil.
3. El sistema genera un documento PDF con estructura de hoja de vida profesional.
4. El sistema inicia la descarga del documento.

**Flujos alternativos / excepciones:**

- 2a. Alguna sección del perfil no tiene información: el sistema la omite del documento.

**Postcondiciones:** El usuario obtiene un PDF actualizado con la información de su perfil.

**Prioridad:** Media

---

## CU-20 — Publicar evento

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario publicar un evento académico o de otra índole para que la comunidad lo conozca y confirme su asistencia.

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El usuario selecciona la opción de publicar evento.
2. Ingresa título, descripción, fecha y hora, lugar y categoría.
3. El sistema valida que todos los datos requeridos estén completos y que la fecha sea futura.
4. El sistema publica el evento en el apartado de eventos ([CU-21](#cu-21--visualizar-eventos)).

**Flujos alternativos / excepciones:**

- 3a. Falta algún dato requerido o la fecha ya pasó: el sistema indica la información pendiente y no publica el evento.
- 3b. El evento no cumple las políticas de uso: el sistema lo rechaza e informa el motivo.

**Postcondiciones:** El evento queda publicado y disponible para que otros usuarios confirmen asistencia ([CU-15](#cu-15--confirmar-asistencia-a-eventos-rsvp)). Puede ser moderado según [CU-25](#cu-25--moderar-contenido-publicaciones-y-eventos).

**Prioridad:** Media

---

## CU-21 — Visualizar eventos

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario consultar los eventos publicados en la plataforma para identificar los de su interés.

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El usuario accede al apartado de eventos.
2. El sistema muestra los próximos eventos ordenados por fecha, con título, fecha, categoría, lugar y descripción.
3. El usuario puede filtrar por categoría.
4. El usuario selecciona un evento para ver su detalle y, si lo desea, confirmar asistencia ([CU-15](#cu-15--confirmar-asistencia-a-eventos-rsvp)).

**Flujos alternativos / excepciones:**

- 2a. No existen eventos publicados o que coincidan con el filtro: el sistema informa que no hay eventos disponibles.

**Postcondiciones:** El usuario conoce los eventos disponibles en la plataforma.

**Prioridad:** Media

---

## CU-22 — Publicar oportunidades y gestionar postulaciones

**Actor(es):** Responsable de oportunidad

**Descripción:** Permite a un usuario publicar oportunidades de investigación, proyectos o voluntariado, revisar las postulaciones recibidas y actualizar su estado.

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El responsable crea una oportunidad indicando título, descripción, categoría (investigación, proyecto o voluntariado), requisitos, número de cupos y fecha de cierre.
2. El sistema valida y publica la oportunidad en la sección de oportunidades ([CU-12](#cu-12--explorar-oportunidades)).
3. El responsable consulta el listado de postulaciones recibidas y el perfil de cada postulante.
4. El responsable cambia el estado de cada postulación a "En revisión", "Aceptada" o "Rechazada", con retroalimentación opcional.
5. El sistema notifica al postulante cada cambio de estado ([CU-14](#cu-14--gestionar-estado-de-postulaciones)).

**Flujos alternativos / excepciones:**

- 1a. Faltan datos requeridos: el sistema indica los campos pendientes y no publica la oportunidad.
- 4a. Se alcanza la fecha de cierre o se completan los cupos: el sistema cierra la oportunidad a nuevas postulaciones.
- 4b. El responsable cierra la oportunidad manualmente: el sistema deja de aceptar postulaciones y notifica a los postulantes pendientes.

**Postcondiciones:** La oportunidad queda publicada y las postulaciones reflejan su estado actualizado para el postulante.

**Prioridad:** Alta

---

## CU-23 — Consultar notificaciones

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario consultar las notificaciones generadas por la plataforma (solicitudes de conexión, mensajes, cambios de estado de postulaciones, roles en proyectos, eventos, entre otras).

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El sistema muestra un indicador con el número de notificaciones no leídas.
2. El usuario abre el panel de notificaciones.
3. El sistema lista las notificaciones de la más reciente a la más antigua.
4. El usuario selecciona una notificación y el sistema lo lleva al elemento relacionado, marcándola como leída.

**Flujos alternativos / excepciones:**

- 3a. No hay notificaciones: el sistema muestra un mensaje indicándolo.
- 4a. El usuario marca todas las notificaciones como leídas.

**Postcondiciones:** El usuario queda al tanto de la actividad que lo involucra. Los tipos de notificación que recibe se configuran en [CU-03](#cu-03--administrar-cuenta).

**Prioridad:** Media

---

## CU-24 — Administrar cuentas de usuario

**Actor(es):** Administrador de la plataforma

**Descripción:** Permite al administrador consultar las cuentas registradas y suspender, desactivar o reactivar las que incumplan las condiciones de uso.

**Precondiciones:** El usuario debe estar autenticado con rol de administrador de la plataforma.

**Flujo principal:**

1. El administrador accede al panel de gestión de usuarios.
2. El sistema lista las cuentas registradas con su estado (activa, suspendida, desactivada).
3. El administrador busca y selecciona una cuenta para ver su información básica.
4. El administrador suspende, desactiva o reactiva la cuenta indicando el motivo.
5. El sistema aplica el cambio, registra la acción y notifica al usuario afectado.

**Flujos alternativos / excepciones:**

- 4a. El administrador intenta suspender su propia cuenta: el sistema bloquea la acción.

**Postcondiciones:** El estado de la cuenta queda actualizado. Un usuario suspendido o desactivado no puede iniciar sesión ([CU-02](#cu-02--iniciar-sesión), flujo 3d).

**Prioridad:** Alta

---

## CU-25 — Moderar contenido (publicaciones y eventos)

**Actor(es):** Administrador de la plataforma; Usuario autenticado (reporta contenido)

**Descripción:** Permite al administrador revisar y retirar publicaciones (incluidos sus comentarios) o eventos que incumplan las políticas de uso, incluidos los reportados por los usuarios.

**Precondiciones:** El administrador debe estar autenticado con rol de administrador de la plataforma.

**Flujo principal:**

1. Un usuario reporta una publicación o evento indicando el motivo, o el administrador lo identifica directamente.
2. El administrador accede al panel de moderación, donde ve el contenido reportado y el resto de publicaciones y eventos.
3. El administrador revisa el contenido y decide retirarlo o mantenerlo.
4. Si lo retira, el sistema deja de mostrarlo a los usuarios, notifica a su autor con el motivo y registra la acción del administrador.

**Flujos alternativos / excepciones:**

- 3a. El administrador decide mantener el contenido: el sistema descarta los reportes asociados.

**Postcondiciones:** El contenido inapropiado deja de estar disponible y la acción queda registrada.

**Prioridad:** Alta

---

## CU-26 — Administrar categorías

**Actor(es):** Administrador de la plataforma

**Descripción:** Permite al administrador gestionar las categorías disponibles para publicaciones, proyectos, eventos, oportunidades y, en la fase 2, servicios.

**Precondiciones:** El administrador debe estar autenticado con rol de administrador de la plataforma.

**Flujo principal:**

1. El administrador accede a la gestión de categorías.
2. El sistema muestra las categorías existentes agrupadas por tipo de contenido.
3. El administrador crea una categoría indicando su nombre y tipo de contenido, o desactiva una existente.
4. El sistema guarda los cambios.

**Flujos alternativos / excepciones:**

- 3a. Ya existe una categoría con el mismo nombre para ese tipo de contenido: el sistema rechaza la creación.
- 3b. _(Fase 2)_ El administrador revisa una solicitud de nueva categoría enviada por un usuario ([CU-28](#cu-28--publicar-servicio)): la aprueba (se crea la categoría) o la rechaza, y el sistema notifica al solicitante.

**Postcondiciones:** Las categorías quedan actualizadas. Una categoría desactivada no puede usarse en contenido nuevo, pero el contenido existente la conserva.

**Prioridad:** Media

---

## CU-27 — Verificar credenciales

> **Fase 2:** este caso de uso pertenece al módulo de servicios, que queda fuera del MVP.

**Actor(es):** Usuario autenticado; Administrador de la plataforma

**Descripción:** Permite al usuario enviar certificaciones, credenciales o evidencia de experiencia para que un administrador las valide y su perfil y servicios muestren una insignia de "verificado".

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El usuario adjunta un documento o evidencia (constancia, diploma, portafolio) e indica a qué habilidad o servicio corresponde.
2. El sistema asocia la credencial al perfil con estado "Pendiente de verificación".
3. El administrador revisa la credencial y la aprueba o rechaza.
4. Si se aprueba, el sistema muestra la insignia de "verificado" en el perfil y en los servicios asociados.

**Flujos alternativos / excepciones:**

- 3a. La credencial es rechazada: el sistema notifica al usuario el motivo y le permite reenviarla corregida.

**Postcondiciones:** La credencial queda verificada o rechazada, y los demás usuarios pueden distinguir qué credenciales están verificadas.

**Prioridad:** Alta

---

## CU-28 — Publicar servicio

> **Fase 2:** este caso de uso pertenece al módulo de servicios, que queda fuera del MVP.

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario ofrecer servicios propios, académicos (por ejemplo, monitorías) o no académicos (por ejemplo, plomería, electrónica o eventos), definiendo su alcance y límites.

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El usuario selecciona la opción de publicar servicio.
2. Elige una categoría existente, académica o no académica.
3. Describe el servicio, su alcance (qué incluye) y sus límites (qué no incluye).
4. El sistema valida que el alcance y los límites estén completos.
5. El sistema publica el servicio en su categoría, junto con las credenciales verificadas asociadas, si existen ([CU-27](#cu-27--verificar-credenciales)).

**Flujos alternativos / excepciones:**

- 2a. Ninguna categoría se ajusta al servicio: el usuario solicita una nueva categoría, que queda pendiente de aprobación ([CU-26](#cu-26--administrar-categorías)).
- 4a. Faltan el alcance o los límites: el sistema no permite publicar hasta completarlos.
- 5a. El usuario no tiene credenciales verificadas: el servicio se publica sin la insignia de verificado.

**Postcondiciones:** El servicio queda visible para otros usuarios, que pueden filtrarlo por categoría académica o no académica y solicitarlo ([CU-30](#cu-30--solicitar-servicio)).

**Prioridad:** Alta

---

## CU-29 — Registrar oferente de servicios externo

> **Fase 2:** este caso de uso pertenece al módulo de servicios, que queda fuera del MVP.

**Actor(es):** Visitante (egresado o personal tercerizado); Administrador de la plataforma

**Descripción:** Permite a egresados de la universidad y a empleados de empresas tercerizadas que prestan servicios en el campus registrarse en UniLink como oferentes de servicios, sin contar con un correo institucional activo.

**Precondiciones:** El visitante no tiene una cuenta registrada con el mismo correo.

**Flujo principal:**

1. El visitante selecciona la opción de registrarse como egresado o personal tercerizado.
2. Completa nombre, correo personal, contraseña y tipo de vínculo con la universidad (egresado o tercerizado).
3. Adjunta un documento que acredite su vínculo (documento de identidad, diploma o carta de vinculación laboral).
4. El sistema registra la cuenta con estado "Pendiente de verificación".
5. El administrador revisa el documento y aprueba la cuenta.
6. El sistema activa la cuenta y notifica al usuario.

**Flujos alternativos / excepciones:**

- 5a. La verificación es rechazada: el sistema informa el motivo y permite volver a intentarlo con otro documento.

**Postcondiciones:** La cuenta queda activa con los mismos permisos para ofrecer servicios que un usuario con correo institucional. Su perfil muestra claramente su condición de egresado o tercerizado.

**Prioridad:** Media

---

## CU-30 — Solicitar servicio

> **Fase 2:** este caso de uso pertenece al módulo de servicios, que queda fuera del MVP.

**Actor(es):** Usuario autenticado (solicitante); Usuario autenticado (oferente)

**Descripción:** Permite a un usuario contactar al oferente de un servicio publicado, aunque no tengan una conexión establecida.

**Precondiciones:** El servicio debe estar publicado ([CU-28](#cu-28--publicar-servicio)) y el solicitante debe estar autenticado.

**Flujo principal:**

1. El usuario visualiza el detalle de un servicio.
2. Selecciona la opción "Solicitar servicio" y escribe un mensaje inicial describiendo lo que necesita.
3. El sistema crea una solicitud de servicio activa, notifica al oferente y abre un chat privado entre ambos ([CU-10](#cu-10--enviar-mensaje-privado)).
4. El oferente responde la solicitud desde el chat.

**Flujos alternativos / excepciones:**

- 2a. El usuario intenta solicitar su propio servicio: el sistema no lo permite.
- 4a. El oferente o el solicitante cierra la solicitud: el chat queda en modo de solo lectura, salvo que ambos estén conectados.

**Postcondiciones:** Existe un canal de comunicación entre el solicitante y el oferente para acordar el servicio. La negociación y el pago ocurren fuera de la plataforma.

**Prioridad:** Media
