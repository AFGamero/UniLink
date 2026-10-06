# FS-CTA-03 — Recuperación de contraseña

| Campo | Valor |
|---|---|
| **Módulo** | Cuenta y acceso (CTA) |
| **Sprint** | Sprint 01 |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-17](../../requisitos/CasosDeUso.md#cu-17--recuperar-contraseña) |
| **Historias** | [HU-28](../../requisitos/HistoriasDeUsuario.md#hu-28) |
| **Última actualización** | 2026-10-06 |

## 1. Objetivo

Permitir que un usuario que olvidó su contraseña, o cuya cuenta quedó bloqueada, recupere el acceso de forma segura a través de su correo.

## 2. Alcance

**Incluye:**

- Solicitud del enlace de restablecimiento.
- Definición de la nueva contraseña.
- Cierre de las sesiones abiertas y desbloqueo de la cuenta.

**No incluye:**

- Cambio de contraseña con la sesión iniciada (FS-CTA-05).
- Recuperación de cuentas cuyo correo ya no existe.

## 3. Actores

| Actor | Participación |
|---|---|
| Usuario registrado | Solicita el enlace y define la nueva contraseña. |
| Sistema de correo | Entrega el enlace. |

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | El enlace de restablecimiento es de un solo uso y vence 1 hora después de enviado. |
| RN-02 | Al solicitar un nuevo enlace, los anteriores quedan invalidados. |
| RN-03 | La respuesta a la solicitud es idéntica exista o no el correo, para no revelar qué cuentas existen. |
| RN-04 | Se pueden pedir como máximo 3 enlaces por hora para un mismo correo. |
| RN-05 | La nueva contraseña cumple la misma política del registro ([FS-CTA-01](./FS-CTA-01-registro.md), RN-03) y no puede ser igual a la actual. |
| RN-06 | Al restablecer la contraseña se cierran todas las sesiones abiertas y se levanta el bloqueo por intentos fallidos. |
| RN-07 | Se envía un correo de aviso al usuario cuando su contraseña cambia. |
| RN-08 | Solo se envían enlaces a cuentas **Activas**. Las pendientes de verificación reciben en su lugar el enlace de verificación. |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El sistema debe mostrar un formulario para ingresar el correo, accesible desde el inicio de sesión. | Alta |
| RF-02 | El sistema debe enviar el enlace de restablecimiento según RN-01 a RN-04 y RN-08. | Alta |
| RF-03 | Al abrir un enlace válido, el sistema debe mostrar un formulario para la nueva contraseña y su confirmación. | Alta |
| RF-04 | El sistema debe guardar la nueva contraseña, aplicar RN-06 y RN-07, y redirigir al inicio de sesión. | Alta |
| RF-05 | Al abrir un enlace vencido, usado o inválido, el sistema debe explicarlo y ofrecer solicitar uno nuevo. | Alta |

## 6. Datos y validaciones

| Campo | Tipo | Obligatorio | Validación |
|---|---|---|---|
| Correo | Correo | Sí | Formato válido. |
| Nueva contraseña | Contraseña | Sí | RN-05. |
| Confirmar contraseña | Contraseña | Sí | Igual a la nueva contraseña. |

## 7. Estados

| Estado del enlace | Entra cuando | Sale hacia |
|---|---|---|
| Vigente | Se envía | **Usado**, **Vencido** (1 hora) o **Invalidado** (se pidió otro) |

## 8. Flujo de pantallas

1. **Inicio de sesión** → "¿Olvidaste tu contraseña?" → **Solicitar enlace**.
2. **Solicitar enlace** → envía el correo → **Revisa tu correo**.
3. **Correo** → abre el enlace → **Nueva contraseña** → guarda → **Inicio de sesión** con mensaje de éxito.

## 9. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Solicitud enviada (exista o no el correo) | "Si existe una cuenta con {correo}, recibirás un enlace para restablecer tu contraseña. Vence en 1 hora." |
| MSG-02 | Enlace inválido | "Este enlace ya no es válido. Solicita uno nuevo." |
| MSG-03 | Contraseña igual a la actual | "La nueva contraseña debe ser distinta de la actual." |
| MSG-04 | Límite de solicitudes | "Ya solicitaste varios enlaces. Intenta de nuevo en una hora." |
| MSG-05 | Contraseña restablecida | "Tu contraseña se actualizó. Inicia sesión con la nueva contraseña." |
| MSG-06 | Correo de aviso | "La contraseña de tu cuenta UniLink cambió el {fecha}. Si no fuiste tú, escribe a {correo de soporte}." |

## 10. Criterios de aceptación

```gherkin
Escenario: Solicitud con correo registrado
  Dado que tengo una cuenta activa
  Cuando solicito restablecer mi contraseña
  Entonces veo el mensaje MSG-01
  Y recibo un enlace que vence en 1 hora

Escenario: Solicitud con correo no registrado
  Dado que no existe una cuenta con nadie@unimagdalena.edu.co
  Cuando solicito restablecer la contraseña con ese correo
  Entonces veo el mismo mensaje MSG-01
  Y no se envía ningún correo

Escenario: Restablecimiento exitoso
  Dado que abrí un enlace vigente
  Cuando ingreso una nueva contraseña válida y la confirmo
  Entonces veo el mensaje MSG-05
  Y mis otras sesiones abiertas se cierran
  Y recibo el correo de aviso MSG-06

Escenario: Desbloqueo de la cuenta
  Dado que mi cuenta está bloqueada por intentos fallidos
  Cuando restablezco mi contraseña
  Entonces puedo iniciar sesión de inmediato con la nueva contraseña

Escenario: Enlace usado
  Dado que ya restablecí mi contraseña con un enlace
  Cuando vuelvo a abrir ese enlace
  Entonces veo el mensaje MSG-02

Escenario: Enlace vencido
  Dado que recibí un enlace hace más de 1 hora
  Cuando lo abro
  Entonces veo el mensaje MSG-02
```

## 11. Dependencias

- Servicio de envío de correos configurado.
- [FS-CTA-02](./FS-CTA-02-inicio-sesion.md): contador de intentos y manejo de sesiones.

## 12. Preguntas abiertas

- [ ] ¿Se debe impedir reutilizar contraseñas anteriores además de la actual?

## 13. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Gamero | Creación |
