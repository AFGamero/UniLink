# Historias de usuario — Usuarios

_MVP — Red Profesional Universitaria — Universidad del Magdalena_
_Centro de Interés de Desarrollo Tecnológico e Innovación (CIDTI)_

Historias de usuario del módulo Usuarios (USR), en formato "Como / quiero / para", derivadas de sus [casos de uso](./casos-de-uso.md).

## Índice

- [HU-01 — Como visitante, quiero registrarme en UniLink con mis datos personales y académicos](#hu-01)
- [HU-02 — Como usuario registrado (estudiante, profesor, personal administrativo, egresado o tercerizado), quiero iniciar sesión con mi correo y contraseña](#hu-02)
- [HU-03 — Como usuario autenticado, quiero gestionar la información de mi cuenta (datos personales, seguridad, privacidad y preferencias)](#hu-03)
- [HU-04 — Como usuario autenticado, quiero crear y editar mi perfil profesional (biografía, habilidades, intereses, experiencia, proyectos y logros)](#hu-04)
- [HU-13 — Como usuario autenticado, quiero descargar un documento PDF con la información de mi perfil profesional estructurada como una hoja de vida](#hu-13)
- [HU-14 — Como visitante, quiero seleccionar mis preferencias en las categorías de publicaciones y proyectos durante el registro](#hu-14)
- [HU-17 — Como administrador, quiero gestionar las cuentas de los usuarios registrados en UniLink](#hu-17)
- [HU-28 — Como usuario registrado, quiero recuperar mi contraseña si la olvido](#hu-28)

---

## HU-01

> **Como** visitante,
> **quiero** registrarme en UniLink con mis datos personales y académicos,
> **para** poder unirme a la red profesional universitaria.

**Caso de uso relacionado:** [CU-01](./casos-de-uso.md#cu-01--registrar-cuenta)

**Criterios de aceptación:**

- Dado que soy un visitante, cuando completo el formulario de registro con nombre, correo institucional, contraseña y programa académico, entonces el sistema valida el formato de los datos.
- Dado que ingreso un correo que no es de dominio institucional, entonces el sistema muestra un error y no permite continuar. En la fase 2, me ofrecerá registrarme como egresado o tercerizado si es mi caso ([HU-23](../servicios/historias.md#hu-23)).
- Dado que ingreso un correo ya registrado, entonces el sistema me notifica y sugiere iniciar sesión o recuperar mi contraseña.
- Dado que envío el formulario correctamente, entonces recibo en mi correo institucional un enlace de verificación válido por 24 horas.
- Dado que confirmo mi correo mediante el enlace, entonces mi cuenta queda activa y soy redirigido a completar mi perfil y luego al paso de sugerencias de conexión.
- Dado que el enlace de verificación expira sin ser usado, entonces puedo solicitar uno nuevo.

**Prioridad:** Alta

---

## HU-02

> **Como** usuario registrado (estudiante, profesor o personal administrativo; en la fase 2, también egresado o tercerizado),
> **quiero** iniciar sesión con mi correo y contraseña,
> **para** acceder a mis funcionalidades y datos personales en la plataforma.

**Caso de uso relacionado:** [CU-02](./casos-de-uso.md#cu-02--iniciar-sesión)

**Criterios de aceptación:**

- Dado que ingreso credenciales correctas, entonces el sistema me otorga acceso y me redirige al panel principal.
- Dado que ingreso credenciales incorrectas, entonces el sistema muestra un error indicando los intentos restantes (máximo 5 consecutivos).
- Dado que mi cuenta no ha sido verificada, entonces el sistema me solicita completar la verificación antes de continuar.
- Dado que excedo el número máximo de intentos, entonces el sistema bloquea el acceso durante 15 minutos y me sugiere recuperar mi contraseña.
- Dado que mi cuenta está suspendida o desactivada, entonces el sistema me impide el acceso e informa el estado de mi cuenta.

**Prioridad:** Alta

---

## HU-03

> **Como** usuario autenticado,
> **quiero** gestionar la información de mi cuenta (datos personales, seguridad, privacidad y preferencias),
> **para** mantener actualizada y segura mi información.

**Caso de uso relacionado:** [CU-03](./casos-de-uso.md#cu-03--administrar-cuenta)

**Criterios de aceptación:**

- Dado que modifico un dato de mi cuenta (nombre, correo, contraseña, foto de perfil o preferencias de notificación), entonces el sistema valida y guarda los cambios.
- Dado que ingreso datos con un formato inválido, entonces el sistema muestra un error y no guarda los cambios.
- Dado que intento cambiar mi correo a uno ya registrado por otra cuenta, entonces el sistema rechaza el cambio.
- Dado que cambio la privacidad de mi perfil a "solo mis conexiones", entonces los usuarios no conectados solo ven mi nombre, foto y programa académico.
- Dado que cambio mi correo, entonces el cambio solo se aplica cuando verifico el nuevo correo con el enlace que recibo.
- Dado que solicito eliminar mi cuenta y confirmo con mi contraseña, entonces mi cuenta se desactiva y se elimina definitivamente a los 30 días si no vuelvo a iniciar sesión.
- Dado que la actualización es exitosa, entonces el sistema me confirma el cambio realizado.

**Prioridad:** Media

---

## HU-04

> **Como** usuario autenticado,
> **quiero** crear y editar mi perfil profesional (biografía, habilidades, intereses, experiencia, proyectos y logros),
> **para** mostrar mi identidad profesional al resto de la comunidad universitaria.

**Caso de uso relacionado:** [CU-04](./casos-de-uso.md#cu-04--creareditar-perfil-profesional)

**Criterios de aceptación:**

- Dado que completo los campos de mi perfil, entonces el sistema valida la información y la guarda.
- Dado que dejo vacío algún campo obligatorio (nombre, programa académico o tipo de vínculo, y al menos una habilidad), entonces el sistema me indica los campos pendientes y no guarda hasta completarlos.
- Dado que guardo mi perfil correctamente, entonces queda visible para otros usuarios según mi configuración de privacidad.
- Dado que edito mi perfil, entonces puedo declarar en forma de etiquetas lo que puedo aportar a la comunidad ("Puedo aportar") y lo que necesito ("Necesito").
- Dado que otro usuario visualiza mi perfil, entonces ve mis etiquetas de "Puedo aportar" y "Necesito" en una sección destacada.

**Prioridad:** Alta

---

## HU-13

> **Como** usuario autenticado,
> **quiero** descargar un documento PDF con la información de mi perfil profesional estructurada como una hoja de vida,
> **para** compartir mi perfil profesional con otras personas o publicarlo en mis redes sociales para encontrar oportunidades laborales.

**Caso de uso relacionado:** [CU-19](./casos-de-uso.md#cu-19--generar-hoja-de-vida-en-pdf)

**Criterios de aceptación:**

- Dado que tengo información registrada en mi perfil profesional, cuando solicito descargar mi hoja de vida, entonces el sistema genera un documento PDF con la información disponible.
- Dado que solicito la generación de mi hoja de vida, entonces el documento presenta la información organizada en una estructura de hoja de vida profesional.
- Dado que mi perfil contiene información como datos personales, biografía, habilidades, experiencia, proyectos y logros, entonces el documento incluye dicha información.
- Dado que no tengo información registrada en alguna sección de mi perfil, entonces el sistema omite dicha sección del documento.
- Dado que el documento es generado correctamente, entonces el sistema permite descargarlo en formato PDF.

**Prioridad:** Media

---

## HU-14

> **Como** visitante,
> **quiero** seleccionar mis preferencias en las categorías de publicaciones y proyectos durante el registro,
> **para** recibir y visualizar contenido relacionado con mis intereses.

**Caso de uso relacionado:** [CU-18](./casos-de-uso.md#cu-18--seleccionar-preferencias-de-contenido)

**Criterios de aceptación:**

- Dado que me estoy registrando en UniLink, entonces el sistema me permite seleccionar las categorías de publicaciones y proyectos de mi interés.
- Dado que selecciono una o varias categorías de publicaciones y proyectos, entonces el sistema guarda mis preferencias asociadas a mi perfil.
- Dado que he configurado mis preferencias, entonces el sistema utiliza las categorías seleccionadas para mostrarme contenido relacionado con mis intereses.
- Dado que no selecciono ninguna categoría, entonces el sistema permite completar el registro sin guardar preferencias específicas.
- Dado que ya estoy registrado, entonces puedo modificar mis preferencias desde la configuración de mi cuenta.

**Prioridad:** Media

---

## HU-17

> **Como** administrador,
> **quiero** gestionar las cuentas de los usuarios registrados en UniLink,
> **para** mantener el control sobre los miembros que hacen parte de la plataforma.

**Caso de uso relacionado:** [CU-24](./casos-de-uso.md#cu-24--administrar-cuentas-de-usuario)

**Criterios de aceptación:**

- Dado que soy administrador, entonces puedo visualizar la lista de usuarios registrados en la plataforma.
- Dado que visualizo un usuario, entonces puedo consultar la información básica de su cuenta y su estado.
- Dado que un usuario incumple las condiciones de uso de la plataforma, entonces puedo suspender o desactivar su cuenta indicando el motivo.
- Dado que una cuenta se encuentra suspendida o desactivada, entonces el usuario no puede acceder a las funcionalidades de la plataforma.
- Dado que una cuenta está suspendida, entonces puedo reactivarla.

**Prioridad:** Alta

---

## HU-28

> **Como** usuario registrado,
> **quiero** recuperar mi contraseña si la olvido,
> **para** volver a acceder a mi cuenta sin perder mi información.

**Caso de uso relacionado:** [CU-17](./casos-de-uso.md#cu-17--recuperar-contraseña)

**Criterios de aceptación:**

- Dado que olvidé mi contraseña, cuando ingreso mi correo en "¿Olvidaste tu contraseña?", entonces recibo un enlace de restablecimiento válido por 1 hora.
- Dado que ingreso un correo que no está registrado, entonces el sistema muestra el mismo mensaje de confirmación, sin revelar si el correo existe.
- Dado que abro un enlace vigente, cuando ingreso una nueva contraseña que cumple la política de seguridad, entonces el sistema la guarda, cierra mis sesiones abiertas y me lleva al inicio de sesión.
- Dado que el enlace expiró o ya fue usado, entonces el sistema me informa y me permite solicitar uno nuevo.

**Prioridad:** Alta
