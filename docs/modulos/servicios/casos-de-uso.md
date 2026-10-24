# Casos de uso — Servicios (fase 2)

_MVP — Red Profesional Universitaria — Universidad del Magdalena_
_Centro de Interés de Desarrollo Tecnológico e Innovación (CIDTI)_

Casos de uso del módulo Servicios (fase 2) (SRV). Pertenecen a la **fase 2**. Los actores se definen en el [mapa de módulos](../README.md#actores).

## Índice

- [CU-27 — Verificar credenciales](#cu-27--verificar-credenciales) _(fase 2)_
- [CU-28 — Publicar servicio](#cu-28--publicar-servicio) _(fase 2)_
- [CU-29 — Registrar oferente de servicios externo](#cu-29--registrar-oferente-de-servicios-externo) _(fase 2)_
- [CU-30 — Solicitar servicio](#cu-30--solicitar-servicio) _(fase 2)_

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

- 2a. Ninguna categoría se ajusta al servicio: el usuario solicita una nueva categoría, que queda pendiente de aprobación ([CU-26](../plataforma/casos-de-uso.md#cu-26--administrar-categorías)).
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
3. El sistema crea una solicitud de servicio activa, notifica al oferente y abre un chat privado entre ambos ([CU-10](../comunicacion/casos-de-uso.md#cu-10--enviar-mensaje-privado)).
4. El oferente responde la solicitud desde el chat.

**Flujos alternativos / excepciones:**

- 2a. El usuario intenta solicitar su propio servicio: el sistema no lo permite.
- 4a. El oferente o el solicitante cierra la solicitud: el chat queda en modo de solo lectura, salvo que ambos estén conectados.

**Postcondiciones:** Existe un canal de comunicación entre el solicitante y el oferente para acordar el servicio. La negociación y el pago ocurren fuera de la plataforma.

**Prioridad:** Media
