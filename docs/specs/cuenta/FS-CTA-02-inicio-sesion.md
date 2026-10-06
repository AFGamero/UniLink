# FS-CTA-02 — Inicio y cierre de sesión

| Campo | Valor |
|---|---|
| **Módulo** | Cuenta y acceso (CTA) |
| **Sprint** | Sprint 01 |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-02](../../requisitos/CasosDeUso.md#cu-02--iniciar-sesión) |
| **Historias** | [HU-02](../../requisitos/HistoriasDeUsuario.md#hu-02) |
| **Última actualización** | 2026-10-06 |

## 1. Objetivo

Permitir que un usuario con cuenta activa acceda a UniLink de forma segura y cierre su sesión cuando lo desee, protegiendo las cuentas frente a intentos repetidos de adivinar la contraseña.

## 2. Alcance

**Incluye:**

- Inicio de sesión con correo y contraseña.
- Bloqueo temporal por intentos fallidos.
- Opción "Mantener sesión iniciada".
- Cierre de sesión.
- Redirección al onboarding en el primer ingreso.

**No incluye:**

- Recuperación de contraseña ([FS-CTA-03](./FS-CTA-03-recuperar-contrasena.md)).
- Autenticación en dos pasos.
- Inicio de sesión con proveedores externos.

## 3. Actores

| Actor | Participación |
|---|---|
| Usuario registrado | Inicia y cierra sesión. |

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Solo las cuentas en estado **Activa** pueden iniciar sesión. |
| RN-02 | Tras 5 intentos fallidos consecutivos, la cuenta se bloquea 15 minutos. Un inicio de sesión exitoso reinicia el contador. |
| RN-03 | El mensaje de credenciales incorrectas es el mismo si el correo no existe o si la contraseña es incorrecta, para no revelar qué correos están registrados. |
| RN-04 | Sin "Mantener sesión iniciada", la sesión expira tras 2 horas de inactividad. Con la opción marcada, dura 30 días. |
| RN-05 | Al cerrar sesión se invalida la sesión en el servidor, no solo en el navegador. |
| RN-06 | En el primer inicio de sesión de la cuenta, el usuario va al onboarding (FS-RED-02) en lugar del feed. Mientras FS-RED-02 no exista, va al feed. |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El sistema debe mostrar un formulario con correo, contraseña, "Mantener sesión iniciada" y el enlace "¿Olvidaste tu contraseña?". | Alta |
| RF-02 | El sistema debe validar las credenciales y, si son correctas, crear la sesión y redirigir según RN-06. | Alta |
| RF-03 | El sistema debe indicar los intentos restantes cuando quedan 2 o menos. | Media |
| RF-04 | El sistema debe bloquear la cuenta según RN-02 e informar cuánto tiempo falta para desbloquearla. | Alta |
| RF-05 | Si la cuenta está pendiente de verificación, el sistema debe ofrecer reenviar el enlace ([FS-CTA-01](./FS-CTA-01-registro.md)). | Alta |
| RF-06 | Si la cuenta está suspendida o desactivada, el sistema debe impedir el acceso e informar el estado. | Alta |
| RF-07 | El sistema debe ofrecer la opción "Cerrar sesión" en el menú del usuario. | Alta |
| RF-08 | Si un usuario sin sesión intenta abrir una página protegida, el sistema debe llevarlo al inicio de sesión y, al ingresar, devolverlo a esa página. | Media |

## 6. Datos y validaciones

| Campo | Tipo | Obligatorio | Validación |
|---|---|---|---|
| Correo | Correo | Sí | Formato válido. |
| Contraseña | Contraseña | Sí | No vacía. |
| Mantener sesión iniciada | Casilla | No | Desmarcada por defecto. |

## 7. Estados

| Estado de acceso | Entra cuando | Sale hacia |
|---|---|---|
| Normal | Estado inicial o inicio de sesión exitoso | **Bloqueada temporalmente** al quinto intento fallido |
| Bloqueada temporalmente | 5 intentos fallidos consecutivos | **Normal** después de 15 minutos o al restablecer la contraseña |

## 8. Flujo de pantallas

1. **Inicio de sesión** → credenciales válidas → **Onboarding** (primer ingreso) o **Feed**.
2. **Inicio de sesión** → credenciales inválidas → mismo formulario con el mensaje de error.
3. **Menú del usuario** → "Cerrar sesión" → **Inicio de sesión**.

## 9. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Credenciales incorrectas | "Correo o contraseña incorrectos." |
| MSG-02 | Pocos intentos restantes | "Correo o contraseña incorrectos. Te quedan {n} intentos antes de bloquear tu cuenta por 15 minutos." |
| MSG-03 | Cuenta bloqueada | "Tu cuenta está bloqueada por seguridad. Intenta de nuevo en {m} minutos o restablece tu contraseña." |
| MSG-04 | Cuenta sin verificar | "Aún no has verificado tu correo. ¿Quieres que te enviemos un nuevo enlace?" |
| MSG-05 | Cuenta suspendida o desactivada | "Tu cuenta está {estado}. Si crees que es un error, escribe a {correo de soporte}." |
| MSG-06 | Sesión expirada | "Tu sesión expiró. Inicia sesión de nuevo." |

## 10. Criterios de aceptación

```gherkin
Escenario: Inicio de sesión exitoso
  Dado que tengo una cuenta activa que ya completó el onboarding
  Cuando ingreso mi correo y contraseña correctos
  Entonces quedo con la sesión iniciada en el feed

Escenario: Primer inicio de sesión
  Dado que mi cuenta nunca ha iniciado sesión
  Cuando ingreso credenciales correctas
  Entonces soy dirigido al onboarding

Escenario: Credenciales incorrectas
  Dado que tengo una cuenta activa
  Cuando ingreso una contraseña incorrecta por primera vez
  Entonces veo el mensaje MSG-01

Escenario: Correo inexistente
  Dado que no existe una cuenta con nadie@unimagdalena.edu.co
  Cuando intento iniciar sesión con ese correo
  Entonces veo el mismo mensaje MSG-01

Escenario: Bloqueo por intentos fallidos
  Dado que he fallado 4 intentos consecutivos
  Cuando fallo el quinto
  Entonces veo el mensaje MSG-03
  Y no puedo iniciar sesión durante 15 minutos aunque use la contraseña correcta

Escenario: Cuenta sin verificar
  Dado que mi cuenta está pendiente de verificación
  Cuando ingreso credenciales correctas
  Entonces veo el mensaje MSG-04 y no inicio sesión

Escenario: Cerrar sesión
  Dado que tengo la sesión iniciada
  Cuando selecciono "Cerrar sesión"
  Entonces vuelvo a la página de inicio de sesión
  Y al usar el botón "Atrás" del navegador no puedo ver páginas protegidas

Escenario: Volver a la página solicitada
  Dado que no tengo sesión iniciada
  Cuando abro el enlace de un perfil y luego inicio sesión
  Entonces soy dirigido a ese perfil
```

## 11. Dependencias

- [FS-CTA-01](./FS-CTA-01-registro.md): cuentas activas y reenvío del enlace de verificación.
- [FS-CTA-03](./FS-CTA-03-recuperar-contrasena.md): enlace "¿Olvidaste tu contraseña?".

## 12. Preguntas abiertas

- [ ] ¿Cuál es el correo de soporte que se muestra en MSG-05?
- [ ] ¿Se debe avisar por correo al usuario cuando su cuenta se bloquea?

## 13. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Gamero | Creación |
