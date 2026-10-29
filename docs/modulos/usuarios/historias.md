# Historias de usuario — Usuarios

_MVP — Red Profesional Universitaria — Universidad del Magdalena_
_Centro de Interés de Desarrollo Tecnológico e Innovación (CIDTI)_

Historias de usuario del módulo Usuarios (USR), en formato "Como / quiero / para". Sus criterios de aceptación son los escenarios de cada spec (sección 12, "Resultado esperado"); se derivan de sus [casos de uso](./casos-de-uso.md).

## Índice

- [HU-01 — Como visitante, quiero registrarme en UniLink con mis datos personales y académicos](#hu-01)
- [HU-02 — Como usuario registrado (estudiante, profesor o personal administrativo; en la fase 2, también egresado o tercerizado), quiero iniciar sesión con mi correo y contraseña](#hu-02)
- [HU-03 — Como usuario autenticado, quiero gestionar la información de mi cuenta (datos personales, seguridad, privacidad y preferencias)](#hu-03)
- [HU-04 — Como usuario autenticado, quiero crear y editar mi perfil profesional (biografía, habilidades, intereses, experiencia, proyectos y logros)](#hu-04)
- [HU-13 — Como usuario autenticado, quiero descargar un documento PDF con la información de mi perfil profesional estructurada como una hoja de vida](#hu-13)
- [HU-14 — Como visitante, quiero seleccionar mis preferencias en las categorías de publicaciones, proyectos y eventos durante el registro](#hu-14)
- [HU-17 — Como administrador, quiero gestionar las cuentas de los usuarios registrados en UniLink](#hu-17)
- [HU-28 — Como usuario registrado, quiero recuperar mi contraseña si la olvido](#hu-28)

---

## HU-01

> **Como** visitante,
> **quiero** registrarme en UniLink con mis datos personales y académicos,
> **para** poder unirme a la red profesional universitaria.

**Caso de uso relacionado:** [CU-01](./casos-de-uso.md#cu-01--registrar-cuenta)

**Spec y criterios de aceptación:** [FS-USR-01 — escenarios](./specs/FS-USR-01-registro.md#12-resultado-esperado)

**Prioridad:** Alta

---

## HU-02

> **Como** usuario registrado (estudiante, profesor o personal administrativo; en la fase 2, también egresado o tercerizado),
> **quiero** iniciar sesión con mi correo y contraseña,
> **para** acceder a mis funcionalidades y datos personales en la plataforma.

**Caso de uso relacionado:** [CU-02](./casos-de-uso.md#cu-02--iniciar-sesión)

**Spec y criterios de aceptación:** [FS-USR-02 — escenarios](./specs/FS-USR-02-inicio-sesion.md#12-resultado-esperado)

**Prioridad:** Alta

---

## HU-03

> **Como** usuario autenticado,
> **quiero** gestionar la información de mi cuenta (datos personales, seguridad, privacidad y preferencias),
> **para** mantener actualizada y segura mi información.

**Caso de uso relacionado:** [CU-03](./casos-de-uso.md#cu-03--administrar-cuenta)

**Spec y criterios de aceptación:** [FS-USR-05 — escenarios](./specs/FS-USR-05-configuracion-cuenta.md#12-resultado-esperado)

**Prioridad:** Media

---

## HU-04

> **Como** usuario autenticado,
> **quiero** crear y editar mi perfil profesional (biografía, habilidades, intereses, experiencia, proyectos y logros),
> **para** mostrar mi identidad profesional al resto de la comunidad universitaria.

**Caso de uso relacionado:** [CU-04](./casos-de-uso.md#cu-04--creareditar-perfil-profesional)

**Spec y criterios de aceptación:** [FS-USR-06 — escenarios](./specs/FS-USR-06-perfil-profesional.md#12-resultado-esperado)

**Prioridad:** Alta

---

## HU-13

> **Como** usuario autenticado,
> **quiero** descargar un documento PDF con la información de mi perfil profesional estructurada como una hoja de vida,
> **para** compartir mi perfil profesional con otras personas o publicarlo en mis redes sociales para encontrar oportunidades laborales.

**Caso de uso relacionado:** [CU-19](./casos-de-uso.md#cu-19--generar-hoja-de-vida-en-pdf)

**Spec y criterios de aceptación:** [FS-USR-07 — escenarios](./specs/FS-USR-07-hoja-de-vida-pdf.md#12-resultado-esperado)

**Prioridad:** Media

---

## HU-14

> **Como** visitante,
> **quiero** seleccionar mis preferencias en las categorías de publicaciones, proyectos y eventos durante el registro,
> **para** recibir y visualizar contenido relacionado con mis intereses.

**Caso de uso relacionado:** [CU-18](./casos-de-uso.md#cu-18--seleccionar-preferencias-de-contenido)

**Spec y criterios de aceptación:** [FS-USR-04 — escenarios](./specs/FS-USR-04-preferencias-contenido.md#12-resultado-esperado)

**Prioridad:** Media

---

## HU-17

> **Como** administrador,
> **quiero** gestionar las cuentas de los usuarios registrados en UniLink,
> **para** mantener el control sobre los miembros que hacen parte de la plataforma.

**Caso de uso relacionado:** [CU-24](./casos-de-uso.md#cu-24--administrar-cuentas-de-usuario)

**Spec y criterios de aceptación:** [FS-USR-08 — escenarios](./specs/FS-USR-08-gestion-cuentas.md#12-resultado-esperado)

**Prioridad:** Alta

---

## HU-28

> **Como** usuario registrado,
> **quiero** recuperar mi contraseña si la olvido,
> **para** volver a acceder a mi cuenta sin perder mi información.

**Caso de uso relacionado:** [CU-17](./casos-de-uso.md#cu-17--recuperar-contraseña)

**Spec y criterios de aceptación:** [FS-USR-03 — escenarios](./specs/FS-USR-03-recuperar-contrasena.md#12-resultado-esperado)

**Prioridad:** Alta
