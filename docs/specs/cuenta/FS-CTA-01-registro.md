# FS-CTA-01 — Registro y verificación de cuenta

| Campo | Valor |
|---|---|
| **Módulo** | Cuenta y acceso (CTA) |
| **Sprint** | Sprint 01 |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-01](../../requisitos/CasosDeUso.md#cu-01--registrar-cuenta) |
| **Historias** | [HU-01](../../requisitos/HistoriasDeUsuario.md#hu-01) |
| **Última actualización** | 2026-10-06 |

## 1. Objetivo

Permitir que estudiantes, profesores y personal administrativo de la Universidad del Magdalena creen una cuenta con su correo institucional y la activen verificando ese correo. Así se garantiza que solo la comunidad universitaria entra a la red.

## 2. Alcance

**Incluye:**

- Formulario de registro con correo institucional.
- Selección opcional de categorías de interés (detallada en [FS-CTA-04](./FS-CTA-04-preferencias-contenido.md)).
- Envío, reenvío y expiración del enlace de verificación.
- Activación de la cuenta y redirección al perfil.

**No incluye:**

- Registro de egresados y tercerizados con correo personal (FS-SRV-03).
- Contenido del formulario de perfil profesional (FS-PRF-01).
- Inicio de sesión con proveedores externos (Google, Microsoft).

## 3. Actores

| Actor | Participación |
|---|---|
| Visitante | Completa el formulario y verifica su correo. |
| Sistema de correo | Entrega el enlace de verificación. |

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Solo se aceptan correos de los dominios institucionales configurados (inicialmente `unimagdalena.edu.co`). La comparación no distingue mayúsculas. |
| RN-02 | Un correo solo puede estar asociado a una cuenta. |
| RN-03 | La contraseña debe tener al menos 8 caracteres e incluir una mayúscula, una minúscula y un número. |
| RN-04 | El enlace de verificación es de un solo uso y vence 24 horas después de enviado. |
| RN-05 | Al solicitar un nuevo enlace, los anteriores quedan invalidados. |
| RN-06 | Se pueden pedir como máximo 3 reenvíos por hora para un mismo correo. |
| RN-07 | Una cuenta sin verificar no puede iniciar sesión ([FS-CTA-02](./FS-CTA-02-inicio-sesion.md)). |
| RN-08 | Las cuentas sin verificar se eliminan a los 7 días de creadas, liberando el correo. |
| RN-09 | El usuario debe aceptar los términos de uso y la política de tratamiento de datos personales (Ley 1581 de 2012) para registrarse. |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El sistema debe mostrar un formulario de registro con los campos de la sección 6. | Alta |
| RF-02 | El sistema debe validar cada campo al perder el foco y de nuevo al enviar el formulario. | Alta |
| RF-03 | El sistema debe crear la cuenta en estado **Pendiente de verificación** y enviar el enlace al correo ingresado. | Alta |
| RF-04 | El sistema debe mostrar una pantalla de "Revisa tu correo" con la opción de reenviar el enlace. | Alta |
| RF-05 | Al abrir un enlace válido, el sistema debe activar la cuenta, iniciar sesión y redirigir a la edición de perfil. | Alta |
| RF-06 | Al abrir un enlace vencido o inválido, el sistema debe explicarlo y ofrecer reenviar uno nuevo. | Alta |
| RF-07 | Si el correo no es institucional, el sistema debe mostrar el error y un enlace al registro de egresados y tercerizados. | Media |
| RF-08 | El sistema debe guardar la contraseña cifrada con un algoritmo de hash con sal; nunca en texto plano. | Alta |

## 6. Datos y validaciones

| Campo | Tipo | Obligatorio | Validación |
|---|---|---|---|
| Nombres | Texto | Sí | 2 a 60 caracteres; solo letras, espacios, tildes y guiones. |
| Apellidos | Texto | Sí | 2 a 60 caracteres; mismas reglas que nombres. |
| Correo institucional | Correo | Sí | Formato válido, dominio permitido (RN-01) y no registrado (RN-02). |
| Contraseña | Contraseña | Sí | RN-03. Se muestra un indicador de requisitos cumplidos. |
| Confirmar contraseña | Contraseña | Sí | Igual a la contraseña. |
| Tipo de usuario | Lista | Sí | Estudiante, Profesor o Personal administrativo. |
| Programa académico | Lista | Sí, si es estudiante o profesor | Programas vigentes de la universidad. |
| Dependencia | Texto | Sí, si es personal administrativo | 2 a 100 caracteres. |
| Categorías de interés | Selección múltiple | No | Ver [FS-CTA-04](./FS-CTA-04-preferencias-contenido.md). |
| Acepto términos y tratamiento de datos | Casilla | Sí | Debe estar marcada (RN-09). |

## 7. Estados

| Estado | Entra cuando | Sale hacia |
|---|---|---|
| Pendiente de verificación | Se envía el formulario | **Activa** al verificar; se elimina a los 7 días (RN-08) |
| Activa | Se abre un enlace válido | Suspendida o desactivada (FS-ADM-02) |

## 8. Flujo de pantallas

1. **Registro** → el usuario completa el formulario → **Revisa tu correo**.
2. **Revisa tu correo** → "Reenviar enlace" → se envía un enlace nuevo (RN-05, RN-06).
3. **Correo** → abre el enlace → **Cuenta verificada** → redirige a **Editar perfil** (FS-PRF-01).
4. **Enlace inválido** → "Enviar un enlace nuevo" → **Revisa tu correo**.

## 9. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Dominio no institucional | "Usa tu correo institucional (@unimagdalena.edu.co). ¿Eres egresado o trabajas en el campus para una empresa externa? Regístrate aquí." |
| MSG-02 | Correo ya registrado | "Ya existe una cuenta con este correo. Inicia sesión o recupera tu contraseña." |
| MSG-03 | Contraseña débil | "La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número." |
| MSG-04 | Contraseñas distintas | "Las contraseñas no coinciden." |
| MSG-05 | Registro enviado | "Te enviamos un enlace a {correo}. Ábrelo en las próximas 24 horas para activar tu cuenta." |
| MSG-06 | Enlace vencido o inválido | "Este enlace ya no es válido. Solicita uno nuevo para activar tu cuenta." |
| MSG-07 | Límite de reenvíos | "Ya solicitaste varios enlaces. Intenta de nuevo en una hora." |
| MSG-08 | Cuenta verificada | "¡Tu cuenta está activa! Ahora completa tu perfil." |

## 10. Criterios de aceptación

```gherkin
Escenario: Registro exitoso
  Dado que soy un visitante en la página de registro
  Cuando completo el formulario con datos válidos y un correo @unimagdalena.edu.co
  Entonces mi cuenta queda "Pendiente de verificación"
  Y recibo un correo con un enlace de verificación
  Y veo el mensaje MSG-05

Escenario: Correo no institucional
  Dado que estoy en la página de registro
  Cuando ingreso un correo @gmail.com
  Entonces veo el mensaje MSG-01
  Y no puedo enviar el formulario

Escenario: Correo ya registrado
  Dado que existe una cuenta con el correo ana@unimagdalena.edu.co
  Cuando intento registrarme con ese mismo correo
  Entonces veo el mensaje MSG-02

Escenario: Verificación exitosa
  Dado que tengo una cuenta pendiente y un enlace de hace menos de 24 horas
  Cuando abro el enlace
  Entonces mi cuenta queda "Activa"
  Y quedo con la sesión iniciada en la página de edición de perfil

Escenario: Enlace vencido
  Dado que recibí un enlace hace más de 24 horas
  Cuando lo abro
  Entonces veo el mensaje MSG-06 y la opción de solicitar uno nuevo

Escenario: Enlace anterior invalidado
  Dado que solicité un segundo enlace de verificación
  Cuando abro el primer enlace
  Entonces veo el mensaje MSG-06

Escenario: Límite de reenvíos
  Dado que solicité 3 enlaces en la última hora
  Cuando solicito otro
  Entonces veo el mensaje MSG-07 y no se envía ningún correo
```

## 11. Dependencias

- Servicio de envío de correos configurado.
- Catálogo de programas académicos y categorías semilla.
- [FS-CTA-04](./FS-CTA-04-preferencias-contenido.md) para el paso de categorías.

## 12. Preguntas abiertas

- [ ] ¿Existen otros dominios institucionales válidos además de `unimagdalena.edu.co` (por ejemplo, uno distinto para estudiantes y funcionarios)?
- [ ] ¿De dónde se obtiene el catálogo oficial de programas académicos?
- [ ] ¿El equipo jurídico de la universidad debe aprobar el texto de tratamiento de datos?

## 13. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Gamero | Creación |
