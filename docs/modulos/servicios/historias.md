# Historias de usuario — Servicios (fase 2)

_MVP — Red Profesional Universitaria — Universidad del Magdalena_
_Centro de Interés de Desarrollo Tecnológico e Innovación (CIDTI)_

Historias de usuario del módulo Servicios (fase 2) (SRV), en formato "Como / quiero / para", derivadas de sus [casos de uso](./casos-de-uso.md). Pertenecen a la **fase 2**.

## Índice

- [HU-21 — Como usuario autenticado, quiero verificar mis certificaciones, credenciales o experiencia asociadas a los servicios que ofrezco](#hu-21) _(fase 2)_
- [HU-22 — Como usuario autenticado, quiero publicar servicios propios definiendo su categoría (académicos o no académicos), alcance y límites claros](#hu-22) _(fase 2)_
- [HU-23 — Como egresado de la universidad o empleado de una empresa tercerizada que presta servicios dentro del campus, quiero registrarme en UniLink como oferente de servicios](#hu-23) _(fase 2)_
- [HU-31 — Como usuario autenticado, quiero solicitar un servicio publicado y contactar a su oferente](#hu-31) _(fase 2)_

---

## HU-21

> **Fase 2:** esta historia pertenece al módulo de servicios, que queda fuera del MVP.

> **Como** usuario autenticado,
> **quiero** verificar mis certificaciones, credenciales o experiencia asociadas a los servicios que ofrezco,
> **para** que quienes contraten confíen en que tengo la capacidad real de prestarlos.

**Caso de uso relacionado:** [CU-27](./casos-de-uso.md#cu-27--verificar-credenciales)

**Criterios de aceptación:**

- Dado que soy un usuario autenticado, cuando adjunto un documento o evidencia de certificación (constancia, diploma, portafolio), entonces el sistema la asocia a mi perfil como "pendiente de verificación".
- Dado que envío una credencial para verificación, entonces un administrador revisa el documento antes de que quede marcado como verificado.
- Dado que una credencial es verificada exitosamente, entonces mi perfil y mis servicios publicados muestran una insignia de "verificado" visible para otros usuarios.
- Dado que una credencial es rechazada, entonces el sistema me notifica el motivo y me permite volver a enviarla corregida.
- Dado que publico un servicio sin tener credenciales aprobadas, entonces el sistema lo publica sin la insignia de verificado.
- Dado que un usuario visualiza mi perfil o servicio, entonces puede distinguir claramente cuáles credenciales están verificadas y cuáles no.

**Prioridad:** Alta

---

## HU-22

> **Fase 2:** esta historia pertenece al módulo de servicios, que queda fuera del MVP.

> **Como** usuario autenticado,
> **quiero** publicar servicios propios definiendo su categoría (académicos o no académicos), alcance y límites claros,
> **para** ofrecer tanto habilidades profesionales como prácticas (por ejemplo monitorías, plomería, electrónica o eventos) sin generar confusión con quien lo contrata.

**Caso de uso relacionado:** [CU-28](./casos-de-uso.md#cu-28--publicar-servicio)

**Criterios de aceptación:**

- Dado que quiero publicar un servicio, cuando completo el formulario, entonces el sistema me permite elegir una categoría existente (académica o no académica) o solicitar una nueva al administrador.
- Dado que estoy creando un servicio, entonces el sistema me exige describir explícitamente el alcance (qué incluye) y los límites (qué no incluye) de lo que ofrezco.
- Dado que publico un servicio sin definir su alcance o límites, entonces el sistema no permite publicarlo hasta que complete esos campos.
- Dado que el servicio es publicado correctamente, entonces queda visible para otros usuarios en la categoría correspondiente, junto con las credenciales verificadas asociadas (si existen).
- Dado que un usuario busca servicios, entonces puede filtrar por categoría académica o no académica.
- Dado que dos servicios de distintos oferentes tienen alcances que se solapan, entonces cada uno se muestra con su propia descripción de límites, sin que el sistema los combine o modifique.

**Prioridad:** Alta

---

## HU-23

> **Fase 2:** esta historia pertenece al módulo de servicios, que queda fuera del MVP.

> **Como** egresado de la universidad o empleado de una empresa tercerizada que presta servicios dentro del campus,
> **quiero** registrarme en UniLink como oferente de servicios,
> **para** participar en la red de confianza de la plataforma aunque no sea estudiante activo.

**Caso de uso relacionado:** [CU-29](./casos-de-uso.md#cu-29--registrar-oferente-de-servicios-externo)

**Criterios de aceptación:**

- Dado que soy egresado o personal tercerizado, cuando me registro, entonces el sistema me permite seleccionar mi tipo de vínculo con la universidad (egresado, tercerizado) en lugar de un programa académico activo.
- Dado que no cuento con un correo institucional activo, entonces el sistema me permite registrarme con un correo personal y verificar mi identidad por un medio alternativo (por ejemplo, documento de identidad o carta de vinculación laboral).
- Dado que mi verificación alternativa es aprobada, entonces mi cuenta queda activa con los mismos permisos para ofrecer servicios que un usuario con correo institucional.
- Dado que mi verificación alternativa es rechazada, entonces el sistema me informa el motivo y me permite volver a intentarlo con otro documento.
- Dado que un usuario visualiza mi perfil, entonces puede identificar claramente mi condición de egresado o tercerizado, diferenciándome de un estudiante activo.

**Prioridad:** Media

---

## HU-31

> **Fase 2:** esta historia pertenece al módulo de servicios, que queda fuera del MVP.

> **Como** usuario autenticado,
> **quiero** solicitar un servicio publicado y contactar a su oferente,
> **para** acordar el servicio que necesito aunque no tengamos una conexión establecida.

**Caso de uso relacionado:** [CU-30](./casos-de-uso.md#cu-30--solicitar-servicio)

**Criterios de aceptación:**

- Dado que visualizo un servicio publicado, cuando selecciono "Solicitar servicio" y escribo un mensaje inicial, entonces el sistema notifica al oferente y abre un chat privado entre ambos.
- Dado que el servicio es mío, entonces el sistema no me permite solicitarlo.
- Dado que la solicitud se cierra, entonces el chat queda en modo de solo lectura, salvo que estemos conectados.

**Prioridad:** Media
