# Casos de Uso — UniLink

_MVP — Red Profesional Universitaria — Universidad del Magdalena_
_Centro de Interés de Desarrollo Tecnológico e Innovación (CIDTI)_

Este documento describe los 12 casos de uso que delimitan el alcance funcional del MVP de UniLink. Cada caso de uso incluye actor, descripción, precondiciones, flujo principal, flujos alternativos/excepciones, postcondiciones y prioridad, siguiendo la estructura recomendada para la especificación de requisitos del proyecto.

## Índice

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

---

## CU-01 — Registrar cuenta

**Actor(es):** Visitante (usuario no autenticado)

**Descripción:** Permite a un nuevo usuario crear una cuenta en UniLink proporcionando sus datos personales y académicos para unirse a la red profesional universitaria.

**Precondiciones:** El usuario no debe tener una cuenta previamente registrada con el mismo correo institucional.

**Flujo principal:**

1. El usuario accede a la página de registro.
2. Completa el formulario con nombre, correo institucional, contraseña y programa académico.
3. El sistema valida el formato de los datos ingresados.
4. El sistema envía un enlace de verificación al correo institucional.
5. El usuario confirma su correo mediante el enlace recibido.
6. El sistema activa la cuenta y redirige al usuario para completar su perfil.

**Flujos alternativos / excepciones:**

- 3a. El correo ingresado no corresponde a un dominio institucional válido: el sistema muestra un mensaje de error y no permite continuar.
- 3b. El correo ya se encuentra registrado: el sistema notifica al usuario y sugiere iniciar sesión o recuperar su contraseña.
- 5a. El enlace de verificación expira antes de ser usado: el sistema permite solicitar un nuevo enlace.

**Postcondiciones:** Se crea una cuenta activa asociada al usuario, quien queda autenticado y con perfil pendiente de completar.

**Prioridad:** Alta

---

## CU-02 — Iniciar sesión

**Actor(es):** Usuario registrado (estudiante, profesor o personal administrativo)

**Descripción:** Permite al usuario autenticarse en la plataforma para acceder a sus funcionalidades y datos personales.

**Precondiciones:** El usuario debe contar con una cuenta previamente registrada y verificada.

**Flujo principal:**

1. El usuario accede a la página de inicio de sesión.
2. Ingresa su correo electrónico y contraseña.
3. El sistema valida las credenciales.
4. El sistema otorga acceso y redirige al panel principal.

**Flujos alternativos / excepciones:**

- 3a. Las credenciales son incorrectas: el sistema muestra un mensaje de error e indica el número de intentos restantes.
- 3b. La cuenta no ha sido verificada: el sistema solicita completar la verificación antes de continuar.
- 3c. El usuario excede el número máximo de intentos: el sistema bloquea temporalmente el acceso y sugiere recuperar la contraseña.

**Postcondiciones:** El usuario queda autenticado y con una sesión activa en la plataforma.

**Prioridad:** Alta

---

## CU-03 — Administrar cuenta

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario gestionar la información de su cuenta, incluyendo datos personales, configuración de seguridad y preferencias.

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El usuario accede a la sección de configuración de cuenta.
2. Selecciona el dato que desea modificar (nombre, correo, contraseña, foto de perfil, preferencias de notificación).
3. Ingresa la nueva información y confirma los cambios.
4. El sistema valida y guarda los cambios.
5. El sistema confirma la actualización al usuario.

**Flujos alternativos / excepciones:**

- 3a. Los datos ingresados no cumplen el formato requerido: el sistema muestra un mensaje de error y no guarda los cambios.
- 3b. El usuario intenta cambiar su correo a uno ya registrado por otra cuenta: el sistema rechaza el cambio.

**Postcondiciones:** La información de la cuenta queda actualizada.

**Prioridad:** Media

---

## CU-04 — Crear/editar perfil profesional

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario construir y mantener su identidad profesional en la plataforma, incluyendo biografía, habilidades, intereses, experiencia, proyectos y logros académicos.

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El usuario accede a la sección de edición de perfil.
2. Completa o modifica los campos: biografía, habilidades, intereses, experiencia, proyectos y logros.
3. El sistema valida la información ingresada.
4. El sistema guarda los cambios.
5. El perfil actualizado queda visible para otros usuarios, según la configuración de privacidad definida.

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
2. Ingresa un término de búsqueda o aplica filtros (habilidades, intereses, programa académico, facultad).
3. El sistema procesa la búsqueda y muestra los perfiles coincidentes con una vista previa de información básica.
4. El usuario selecciona un perfil para visualizar su detalle completo.

**Flujos alternativos / excepciones:**

- 3a. No se encuentran perfiles coincidentes: el sistema informa que no hay resultados y sugiere ajustar los filtros.

**Postcondiciones:** El usuario obtiene un listado de perfiles relevantes según su búsqueda y puede consultar el detalle de cualquiera de ellos.

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

**Postcondiciones:** La solicitud queda resuelta (aceptada o rechazada) y, en caso de aceptación, ambos usuarios quedan conectados.

**Prioridad:** Alta

---

## CU-08 — Publicar contenido

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario compartir publicaciones académicas o profesionales, como proyectos, logros, oportunidades o artículos, con su red de conexiones.

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El usuario selecciona la opción de crear publicación.
2. Ingresa el contenido: título, descripción, categoría y, opcionalmente, archivos adjuntos.
3. El sistema valida el contenido ingresado.
4. El sistema publica el contenido y lo muestra en el feed de sus conexiones.

**Flujos alternativos / excepciones:**

- 3a. El contenido no cumple con las políticas de uso de la plataforma: el sistema rechaza la publicación e informa el motivo.

**Postcondiciones:** La publicación queda visible en el feed de las conexiones del usuario.

**Prioridad:** Media

---

## CU-09 — Visualizar publicaciones

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario consultar las publicaciones realizadas por otros miembros de la plataforma, filtradas por categoría o relevancia.

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

**Descripción:** Permite al usuario comunicarse de forma privada (1 a 1) con otro miembro con quien tenga una conexión establecida.

**Precondiciones:** Debe existir una conexión establecida entre el usuario y el destinatario.

**Flujo principal:**

1. El usuario selecciona una conexión de su red.
2. Abre el chat privado correspondiente.
3. Escribe y envía el mensaje.
4. El sistema entrega el mensaje y notifica al destinatario.

**Flujos alternativos / excepciones:**

- 1a. No existe conexión con el usuario seleccionado: el sistema no permite iniciar el chat.

**Postcondiciones:** El mensaje queda registrado en la conversación y disponible para ambos usuarios.

**Prioridad:** Alta

---

## CU-11 — Gestionar espacio de proyectos

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario crear, unirse y colaborar en espacios de proyectos dedicados para trabajar en conjunto con otros miembros de la plataforma.

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El usuario crea un nuevo proyecto o solicita unirse a uno existente.
2. En caso de creación, define nombre, descripción, roles requeridos, tareas y objetivos del proyecto.
3. El sistema registra el proyecto y gestiona la incorporación de miembros.
4. Los miembros colaboran dentro del espacio del proyecto según los roles asignados.

**Flujos alternativos / excepciones:**

- 1a. El usuario solicita unirse a un proyecto que ya alcanzó el número máximo de integrantes definido por su creador: el sistema no permite la solicitud e informa el motivo.

**Postcondiciones:** El espacio de proyecto queda creado o el usuario queda incorporado como miembro de un proyecto existente.

**Prioridad:** Media

---

## CU-12 — Explorar oportunidades

**Actor(es):** Usuario autenticado

**Descripción:** Permite al usuario consultar y postularse a oportunidades de investigación, proyectos y voluntariado publicadas en la plataforma.

**Precondiciones:** El usuario debe estar autenticado en la plataforma.

**Flujo principal:**

1. El usuario accede a la sección de oportunidades.
2. Explora las ofertas disponibles, filtrando por categoría (investigación, proyectos, voluntariado).
3. Selecciona una oportunidad para ver su detalle.
4. Se postula directamente a la oportunidad.
5. El sistema registra la postulación y notifica al responsable de la oportunidad.

**Flujos alternativos / excepciones:**

- 4a. El usuario ya se encuentra postulado a la misma oportunidad: el sistema no permite una nueva postulación y muestra el estado actual.

**Postcondiciones:** La postulación queda registrada y visible tanto para el usuario como para el responsable de la oportunidad.

**Prioridad:** Media

---
