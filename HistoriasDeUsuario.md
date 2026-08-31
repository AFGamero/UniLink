# Historias de Usuario — UniLink

_MVP — Red Profesional Universitaria — Universidad del Magdalena_
_Centro de Interés de Desarrollo Tecnológico e Innovación (CIDTI)_

Este documento presenta las historias de usuario derivadas de los [Casos de Uso de UniLink](./Casos_de_Uso_UniLink.md), en formato "Como / quiero / para", con criterios de aceptación en formato Given/When/Then (Dado/Cuando/Entonces) y prioridad heredada del caso de uso correspondiente.

## Índice

- [HU-01 — Como visitante, quiero registrarme en UniLink con mis datos personales y académicos](#hu-01)
- [HU-02 — Como usuario registrado (estudiante, profesor o personal administrativo), quiero iniciar sesión con mi correo y contraseña](#hu-02)
- [HU-03 — Como usuario autenticado, quiero gestionar la información de mi cuenta (datos personales, seguridad y preferencias)](#hu-03)
- [HU-04 — Como usuario autenticado, quiero crear y editar mi perfil profesional (biografía, habilidades, intereses, experiencia, proyectos y logros)](#hu-04)
- [HU-05 — Como usuario autenticado, quiero buscar y visualizar perfiles de otros miembros por nombre, habilidades, intereses o programa académico](#hu-05)
- [HU-06 — Como usuario autenticado, quiero enviar una solicitud de conexión a otro miembro de la plataforma](#hu-06)
- [HU-07 — Como usuario autenticado, quiero aceptar o rechazar las solicitudes de conexión que recibo](#hu-07)
- [HU-08 — Como usuario autenticado, quiero publicar contenido académico o profesional (proyectos, logros, oportunidades o artículos)](#hu-08)
- [HU-09 — Como usuario autenticado, quiero visualizar las publicaciones de otros miembros filtradas por categoría o relevancia](#hu-09)
- [HU-10 — Como usuario autenticado, quiero enviar mensajes privados a otro miembro con quien tengo una conexión establecida](#hu-10)
- [HU-11 — Como usuario autenticado, quiero crear o unirme a espacios de proyectos para colaborar con otros miembros](#hu-11)
- [HU-12 — Como usuario autenticado, quiero explorar y postularme a oportunidades de investigación, proyectos y voluntariado](#hu-12)

---

## HU-01

> **Como** visitante,
> **quiero** registrarme en UniLink con mis datos personales y académicos,
> **para** poder unirme a la red profesional universitaria.

**Caso de uso relacionado:** [CU-01](./Casos_de_Uso_UniLink.md#cu-01)

**Criterios de aceptación:**

- Dado que soy un visitante, cuando completo el formulario de registro con nombre, correo institucional, contraseña y programa académico, entonces el sistema valida el formato de los datos.
- Dado que ingreso un correo que no es de dominio institucional, entonces el sistema muestra un error y no permite continuar.
- Dado que ingreso un correo ya registrado, entonces el sistema me notifica y sugiere iniciar sesión o recuperar mi contraseña.
- Dado que envío el formulario correctamente, entonces recibo un enlace de verificación en mi correo institucional.
- Dado que confirmo mi correo mediante el enlace, entonces mi cuenta queda activa y soy redirigido a completar mi perfil.
- Dado que el enlace de verificación expira sin ser usado, entonces puedo solicitar uno nuevo.

**Prioridad:** Alta

---

## HU-02

> **Como** usuario registrado (estudiante, profesor o personal administrativo),
> **quiero** iniciar sesión con mi correo y contraseña,
> **para** acceder a mis funcionalidades y datos personales en la plataforma.

**Caso de uso relacionado:** [CU-02](./Casos_de_Uso_UniLink.md#cu-02)

**Criterios de aceptación:**

- Dado que ingreso credenciales correctas, entonces el sistema me otorga acceso y me redirige al panel principal.
- Dado que ingreso credenciales incorrectas, entonces el sistema muestra un error indicando los intentos restantes.
- Dado que mi cuenta no ha sido verificada, entonces el sistema me solicita completar la verificación antes de continuar.
- Dado que excedo el número máximo de intentos, entonces el sistema bloquea temporalmente el acceso y me sugiere recuperar mi contraseña.

**Prioridad:** Alta

---

## HU-03

> **Como** usuario autenticado,
> **quiero** gestionar la información de mi cuenta (datos personales, seguridad y preferencias),
> **para** mantener actualizada y segura mi información.

**Caso de uso relacionado:** [CU-03](./Casos_de_Uso_UniLink.md#cu-03)

**Criterios de aceptación:**

- Dado que modifico un dato de mi cuenta (nombre, correo, contraseña, foto de perfil o preferencias de notificación), entonces el sistema valida y guarda los cambios.
- Dado que ingreso datos con un formato inválido, entonces el sistema muestra un error y no guarda los cambios.
- Dado que intento cambiar mi correo a uno ya registrado por otra cuenta, entonces el sistema rechaza el cambio.
- Dado que la actualización es exitosa, entonces el sistema me confirma el cambio realizado.

**Prioridad:** Media

---

## HU-04

> **Como** usuario autenticado,
> **quiero** crear y editar mi perfil profesional (biografía, habilidades, intereses, experiencia, proyectos y logros),
> **para** mostrar mi identidad profesional al resto de la comunidad universitaria.

**Caso de uso relacionado:** [CU-04](./Casos_de_Uso_UniLink.md#cu-04)

**Criterios de aceptación:**

- Dado que completo los campos de mi perfil, entonces el sistema valida la información y la guarda.
- Dado que dejo campos obligatorios vacíos, entonces el sistema me indica los campos pendientes y no guarda hasta completarlos.
- Dado que guardo mi perfil correctamente, entonces queda visible para otros usuarios según mi configuración de privacidad.

**Prioridad:** Alta

---

## HU-05

> **Como** usuario autenticado,
> **quiero** buscar y visualizar perfiles de otros miembros por nombre, habilidades, intereses o programa académico,
> **para** descubrir personas afines dentro de la comunidad universitaria.

**Caso de uso relacionado:** [CU-05](./Casos_de_Uso_UniLink.md#cu-05)

**Criterios de aceptación:**

- Dado que ingreso un término de búsqueda o aplico filtros, entonces el sistema muestra los perfiles coincidentes con una vista previa.
- Dado que no existen perfiles coincidentes, entonces el sistema me informa que no hay resultados y sugiere ajustar los filtros.
- Dado que selecciono un perfil de los resultados, entonces puedo visualizar su detalle completo.

**Prioridad:** Alta

---

## HU-06

> **Como** usuario autenticado,
> **quiero** enviar una solicitud de conexión a otro miembro de la plataforma,
> **para** establecer una conexión profesional con esa persona.

**Caso de uso relacionado:** [CU-06](./Casos_de_Uso_UniLink.md#cu-06)

**Criterios de aceptación:**

- Dado que visualizo el perfil de otro usuario sin conexión ni solicitud previa, entonces puedo enviarle una solicitud de conexión.
- Dado que envío la solicitud, entonces el sistema la registra como pendiente y notifica al destinatario.
- Dado que ya existe una solicitud pendiente o una conexión establecida con ese usuario, entonces el sistema no me permite enviar una nueva solicitud y me muestra el estado actual.

**Prioridad:** Alta

---

## HU-07

> **Como** usuario autenticado,
> **quiero** aceptar o rechazar las solicitudes de conexión que recibo,
> **para** decidir con quién establezco una conexión profesional.

**Caso de uso relacionado:** [CU-07](./Casos_de_Uso_UniLink.md#cu-07)

**Criterios de aceptación:**

- Dado que recibo una solicitud de conexión, entonces soy notificado y puedo revisar el perfil del solicitante.
- Dado que acepto la solicitud, entonces el sistema actualiza la red de conexiones de ambos usuarios y notifica al solicitante.
- Dado que rechazo la solicitud, entonces el sistema la descarta sin notificar el motivo al solicitante.

**Prioridad:** Alta

---

## HU-08

> **Como** usuario autenticado,
> **quiero** publicar contenido académico o profesional (proyectos, logros, oportunidades o artículos),
> **para** compartir información relevante con mi red de conexiones.

**Caso de uso relacionado:** [CU-08](./Casos_de_Uso_UniLink.md#cu-08)

**Criterios de aceptación:**

- Dado que creo una publicación con título, descripción, categoría y, opcionalmente, archivos adjuntos, entonces el sistema la valida y publica.
- Dado que la publicación no cumple las políticas de uso de la plataforma, entonces el sistema la rechaza e informa el motivo.
- Dado que la publicación es exitosa, entonces aparece en el feed de mis conexiones.

**Prioridad:** Media

---

## HU-09

> **Como** usuario autenticado,
> **quiero** visualizar las publicaciones de otros miembros filtradas por categoría o relevancia,
> **para** mantenerme informado del contenido académico y profesional de mi red.

**Caso de uso relacionado:** [CU-09](./Casos_de_Uso_UniLink.md#cu-09)

**Criterios de aceptación:**

- Dado que accedo al feed de publicaciones, entonces puedo navegar por ellas o aplicar filtros por categoría.
- Dado que aplico un filtro sin resultados, entonces el sistema me informa que no hay publicaciones coincidentes.
- Dado que visualizo una publicación, entonces puedo interactuar con ella (comentar, reaccionar, compartir).

**Prioridad:** Media

---

## HU-10

> **Como** usuario autenticado,
> **quiero** enviar mensajes privados a otro miembro con quien tengo una conexión establecida,
> **para** comunicarme directamente con mis contactos dentro de la plataforma.

**Caso de uso relacionado:** [CU-10](./Casos_de_Uso_UniLink.md#cu-10)

**Criterios de aceptación:**

- Dado que selecciono una conexión de mi red, entonces puedo abrir un chat privado con esa persona.
- Dado que envío un mensaje, entonces el sistema lo entrega y notifica al destinatario.
- Dado que intento escribir a un usuario con el que no tengo conexión, entonces el sistema no me permite iniciar el chat.

**Prioridad:** Alta

---

## HU-11

> **Como** usuario autenticado,
> **quiero** crear o unirme a espacios de proyectos para colaborar con otros miembros,
> **para** trabajar en conjunto en iniciativas académicas o profesionales.

**Caso de uso relacionado:** [CU-11](./Casos_de_Uso_UniLink.md#cu-11)

**Criterios de aceptación:**

- Dado que creo un proyecto, entonces puedo definir nombre, descripción, roles requeridos, tareas y objetivos.
- Dado que solicito unirme a un proyecto existente, entonces el sistema gestiona mi incorporación según la disponibilidad de cupos.
- Dado que el proyecto ya alcanzó el número máximo de integrantes, entonces el sistema no permite mi solicitud e informa el motivo.

**Prioridad:** Media

---

## HU-12

> **Como** usuario autenticado,
> **quiero** explorar y postularme a oportunidades de investigación, proyectos y voluntariado,
> **para** acceder a experiencias académicas y profesionales relevantes para mi formación.

**Caso de uso relacionado:** [CU-12](./Casos_de_Uso_UniLink.md#cu-12)

**Criterios de aceptación:**

- Dado que accedo a la sección de oportunidades, entonces puedo explorarlas filtrando por categoría.
- Dado que selecciono una oportunidad, entonces puedo ver su detalle y postularme directamente.
- Dado que ya estoy postulado a una oportunidad, entonces el sistema no permite una nueva postulación y muestra el estado actual.
- Dado que me postulo exitosamente, entonces el sistema notifica al responsable de la oportunidad.

**Prioridad:** Media

---
