# FS-CTA-05 — Configuración de cuenta y privacidad

| Campo | Valor |
|---|---|
| **Módulo** | Cuenta y acceso (CTA) |
| **Sprint** | Sprint 02 |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-03](../../requisitos/CasosDeUso.md#cu-03--administrar-cuenta) |
| **Historias** | [HU-03](../../requisitos/HistoriasDeUsuario.md#hu-03) |
| **Última actualización** | 2026-10-06 |

## 1. Objetivo

Dar al usuario control sobre su cuenta: sus datos de acceso, quién puede ver su perfil, qué correos recibe y, si lo decide, la eliminación de su cuenta, como exige la Ley 1581 de 2012 de protección de datos personales.

## 2. Alcance

**Incluye:**

- Cambio de correo con verificación.
- Cambio de contraseña con la sesión iniciada.
- Privacidad del perfil.
- Preferencias de notificaciones por correo.
- Acceso a las preferencias de contenido ([FS-CTA-04](./FS-CTA-04-preferencias-contenido.md)).
- Cierre de sesión en todos los dispositivos.
- Eliminación de la cuenta.

**No incluye:**

- Edición de nombre, foto y datos profesionales: se hace en el perfil ([FS-PRF-01](../perfil/FS-PRF-01-perfil-profesional.md)).
- Notificaciones dentro de la plataforma (FS-NOT-01).
- Descarga de una copia de todos los datos del usuario.

## 3. Actores

| Actor | Participación |
|---|---|
| Usuario autenticado | Modifica su configuración. |
| Sistema de correo | Entrega enlaces de verificación y avisos de seguridad. |

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Para cambiar el correo, la contraseña o eliminar la cuenta, el usuario debe ingresar su contraseña actual. |
| RN-02 | El correo nuevo debe cumplir las mismas reglas del registro: dominio institucional ([FS-CTA-01](./FS-CTA-01-registro.md), RN-01) y no estar registrado (RN-02). Los egresados y tercerizados pueden usar un correo personal. |
| RN-03 | El correo nuevo solo reemplaza al anterior cuando el usuario abre el enlace enviado a ese nuevo correo. El enlace vence en 24 horas. |
| RN-04 | Cuando cambia el correo o la contraseña, se envía un aviso al correo anterior o actual. |
| RN-05 | La nueva contraseña cumple la política del registro y no puede ser igual a la actual. Al cambiarla se cierran las demás sesiones. |
| RN-06 | La privacidad del perfil tiene dos niveles: **Comunidad** (por defecto) y **Solo mis conexiones**. Con "Solo mis conexiones", los no conectados ven únicamente nombre, foto y programa. |
| RN-07 | Las notificaciones por correo se activan o desactivan por tipo. Los correos de seguridad (verificación, recuperación, cambio de contraseña, eliminación de cuenta) no se pueden desactivar. |
| RN-08 | Al solicitar la eliminación, la cuenta pasa a **Desactivada por el usuario**: el perfil y el contenido dejan de ser visibles de inmediato. |
| RN-09 | Si el usuario inicia sesión dentro de los 30 días siguientes, puede cancelar la eliminación y la cuenta vuelve a estar activa. Pasados 30 días, los datos personales se eliminan de forma definitiva. |
| RN-10 | Al eliminarse la cuenta, sus mensajes en conversaciones de otros usuarios se muestran como de "Usuario eliminado". |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El sistema debe ofrecer una página de configuración con las secciones: Cuenta, Seguridad, Privacidad, Notificaciones, Intereses y Eliminar cuenta. | Alta |
| RF-02 | El sistema debe permitir cambiar el correo según RN-01 a RN-04, mostrando el correo pendiente mientras no se verifique. | Media |
| RF-03 | El sistema debe permitir cambiar la contraseña según RN-01, RN-04 y RN-05. | Alta |
| RF-04 | El sistema debe permitir elegir el nivel de privacidad del perfil (RN-06) y aplicarlo de inmediato en perfil, búsqueda y sugerencias. | Alta |
| RF-05 | El sistema debe permitir activar o desactivar cada tipo de notificación por correo (RN-07). | Media |
| RF-06 | El sistema debe permitir cerrar la sesión en todos los dispositivos excepto el actual. | Media |
| RF-07 | El sistema debe permitir eliminar la cuenta según RN-01, RN-08 y RN-09, explicando antes qué se elimina y cuándo. | Alta |

## 6. Datos y validaciones

| Sección | Campo | Tipo | Obligatorio | Validación |
|---|---|---|---|---|
| Cuenta | Correo nuevo | Correo | Sí, para cambiarlo | RN-02. |
| Seguridad | Contraseña actual | Contraseña | Sí | Debe coincidir con la actual. |
| Seguridad | Nueva contraseña y confirmación | Contraseña | Sí | RN-05. |
| Privacidad | Visibilidad del perfil | Opción única | Sí | Comunidad o Solo mis conexiones. |
| Notificaciones | Tipos de correo | Interruptores | — | Ver tabla siguiente. |
| Eliminar cuenta | Contraseña | Contraseña | Sí | RN-01. |
| Eliminar cuenta | Confirmación | Casilla | Sí | "Entiendo que mi cuenta se eliminará en 30 días." |

**Notificaciones por correo configurables (todas activas por defecto):**

| Tipo | Disponible desde |
|---|---|
| Nuevas solicitudes de conexión | Sprint 3 |
| Mensajes privados sin leer | Sprint 5 |
| Cambios en mis postulaciones | Sprint 6 |
| Nuevas postulaciones a mis oportunidades | Sprint 6 |
| Recordatorio de eventos a los que asistiré | Sprint 7 |
| Actividad en mis proyectos | Sprint 8 |

## 7. Estados

| Estado de la cuenta | Entra cuando | Sale hacia |
|---|---|---|
| Activa | — | **Desactivada por el usuario** al solicitar la eliminación |
| Desactivada por el usuario | Solicita la eliminación | **Activa** si inicia sesión y cancela antes de 30 días; **Eliminada** a los 30 días |
| Eliminada | Pasan 30 días | Estado final |

## 8. Flujo de pantallas

1. **Menú del usuario** → "Configuración" → **Configuración** (sección Cuenta).
2. **Seguridad** → cambia la contraseña → mensaje de éxito.
3. **Eliminar cuenta** → explicación → contraseña y confirmación → cierra la sesión → **Inicio de sesión** con aviso.
4. **Inicio de sesión** de una cuenta desactivada → "¿Quieres recuperar tu cuenta?" → **Feed**.

## 9. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Contraseña actual incorrecta | "La contraseña actual no es correcta." |
| MSG-02 | Correo pendiente de verificar | "Te enviamos un enlace a {correo nuevo}. Tu correo cambiará cuando lo abras." |
| MSG-03 | Correo actualizado | "Tu correo ahora es {correo nuevo}." |
| MSG-04 | Aviso al correo anterior | "El correo de tu cuenta UniLink cambió a {correo nuevo}. Si no fuiste tú, escribe a {correo de soporte}." |
| MSG-05 | Contraseña actualizada | "Tu contraseña se actualizó y cerramos tus otras sesiones." |
| MSG-06 | Privacidad actualizada | "Ahora tu perfil es visible para: {nivel}." |
| MSG-07 | Explicación antes de eliminar | "Tu perfil y tu contenido dejarán de verse de inmediato. Tienes 30 días para arrepentirte iniciando sesión; después, tus datos se eliminarán para siempre." |
| MSG-08 | Cuenta desactivada al iniciar sesión | "Tu cuenta se eliminará el {fecha}. ¿Quieres recuperarla?" |
| MSG-09 | Sesiones cerradas | "Cerramos tu sesión en los demás dispositivos." |

## 10. Criterios de aceptación

```gherkin
Escenario: Cambiar contraseña
  Dado que tengo la sesión iniciada en dos dispositivos
  Cuando cambio mi contraseña ingresando la actual correctamente
  Entonces veo el mensaje MSG-05
  Y la sesión del otro dispositivo se cierra
  Y recibo un correo de aviso

Escenario: Cambiar correo
  Dado que mi correo es ana@unimagdalena.edu.co
  Cuando solicito cambiarlo a ana.perez@unimagdalena.edu.co con mi contraseña
  Entonces veo el mensaje MSG-02
  Y mi correo sigue siendo el anterior hasta que abra el enlace
  Cuando abro el enlace
  Entonces veo el mensaje MSG-03
  Y el correo anterior recibe el aviso MSG-04

Escenario: Cambiar a un correo no institucional
  Dado que soy estudiante
  Cuando intento cambiar mi correo a ana@gmail.com
  Entonces el sistema rechaza el cambio

Escenario: Perfil solo para conexiones
  Dado que configuro mi perfil como "Solo mis conexiones"
  Cuando un usuario no conectado abre mi perfil
  Entonces solo ve mi nombre, foto y programa

Escenario: Correos de seguridad obligatorios
  Dado que estoy en la sección Notificaciones
  Entonces no veo opción para desactivar los correos de seguridad

Escenario: Eliminar cuenta y arrepentirse
  Dado que solicité eliminar mi cuenta hace 10 días
  Cuando inicio sesión
  Entonces veo el mensaje MSG-08
  Cuando elijo recuperarla
  Entonces mi cuenta vuelve a estar activa con todo mi contenido

Escenario: Eliminación definitiva
  Dado que solicité eliminar mi cuenta hace más de 30 días
  Entonces mis datos personales se eliminaron
  Y mis mensajes en conversaciones ajenas aparecen como de "Usuario eliminado"
```

## 11. Dependencias

- [FS-CTA-01](./FS-CTA-01-registro.md): reglas de correo y envío de enlaces.
- [FS-CTA-02](./FS-CTA-02-inicio-sesion.md): manejo de sesiones.
- [FS-CTA-04](./FS-CTA-04-preferencias-contenido.md): sección Intereses.
- [FS-PRF-01](../perfil/FS-PRF-01-perfil-profesional.md) y [FS-PRF-02](../perfil/FS-PRF-02-busqueda-perfiles.md): aplican la privacidad.
- Tarea programada diaria para eliminar las cuentas que cumplen 30 días.

## 12. Preguntas abiertas

- [ ] ¿Qué pasa con las publicaciones, proyectos y oportunidades creados por una cuenta eliminada: se borran o quedan como de "Usuario eliminado"?
- [ ] ¿El equipo jurídico debe validar el plazo de 30 días?

## 13. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Gamero | Creación |
