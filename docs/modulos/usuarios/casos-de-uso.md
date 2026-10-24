# Casos de uso — Usuarios

_MVP — Red Profesional Universitaria — Universidad del Magdalena_
_Centro de Interés de Desarrollo Tecnológico e Innovación (CIDTI)_

Casos de uso del módulo Usuarios (USR). Los actores se definen en el [mapa de módulos](../README.md#actores).

## Índice

- [CU-01 — Registrar cuenta](#cu-01--registrar-cuenta)
- [CU-02 — Iniciar sesión](#cu-02--iniciar-sesión)
- [CU-03 — Administrar cuenta](#cu-03--administrar-cuenta)
- [CU-04 — Crear/editar perfil profesional](#cu-04--creareditar-perfil-profesional)
- [CU-17 — Recuperar contraseña](#cu-17--recuperar-contraseña)
- [CU-18 — Seleccionar preferencias de contenido](#cu-18--seleccionar-preferencias-de-contenido)
- [CU-19 — Generar hoja de vida en PDF](#cu-19--generar-hoja-de-vida-en-pdf)
- [CU-24 — Administrar cuentas de usuario](#cu-24--administrar-cuentas-de-usuario)

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
7. El sistema activa la cuenta y redirige al usuario para completar su perfil ([CU-04](#cu-04--creareditar-perfil-profesional)) y, a continuación, al paso de sugerencias de conexión ([CU-13](../red/casos-de-uso.md#cu-13--sugerir-conexiones-iniciales-onboarding)).

**Flujos alternativos / excepciones:**

- 4a. El correo ingresado no corresponde a un dominio institucional válido: el sistema muestra un mensaje de error y no permite continuar. En la fase 2, si el usuario es egresado o personal tercerizado, el sistema le ofrecerá registrarse como oferente de servicios externo ([CU-29](../servicios/casos-de-uso.md#cu-29--registrar-oferente-de-servicios-externo)).
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
- 4a. Es el primer ingreso del usuario: el sistema ejecuta el onboarding ([CU-13](../red/casos-de-uso.md#cu-13--sugerir-conexiones-iniciales-onboarding)) antes de mostrar el panel principal.

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

Los campos **"Puedo aportar"** (por ejemplo, "asesoría en Python", "diseño gráfico") y **"Necesito"** (por ejemplo, "un diseñador para mi proyecto", "mentoría en investigación") son listas de etiquetas. La plataforma los cruza para encontrar perfiles complementarios: lo que un usuario necesita con lo que otro puede aportar. Este cruce alimenta las sugerencias de conexión ([CU-13](../red/casos-de-uso.md#cu-13--sugerir-conexiones-iniciales-onboarding)) y la búsqueda de perfiles ([CU-05](../red/casos-de-uso.md#cu-05--buscar-y-visualizar-perfiles)).

**Flujos alternativos / excepciones:**

- 3a. El usuario deja campos obligatorios vacíos: el sistema indica los campos pendientes y no permite guardar hasta completarlos.

**Postcondiciones:** El perfil profesional del usuario queda creado o actualizado y disponible para ser consultado por otros usuarios.

**Prioridad:** Alta

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

1. El sistema muestra las categorías activas ([CU-26](../plataforma/casos-de-uso.md#cu-26--administrar-categorías)) agrupadas por tipo de contenido.
2. El usuario selecciona una o varias categorías.
3. El sistema guarda las preferencias asociadas a su perfil.
4. El sistema utiliza estas preferencias para ordenar el feed ([CU-09](../contenido/casos-de-uso.md#cu-09--visualizar-publicaciones)) y generar sugerencias ([CU-13](../red/casos-de-uso.md#cu-13--sugerir-conexiones-iniciales-onboarding)).

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
