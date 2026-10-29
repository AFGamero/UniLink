# Sprint 01 — Cuenta y acceso

| Campo | Valor |
|---|---|
| **Fechas** | Por definir (2 semanas) |
| **Estado** | Planificado |
| **Objetivo** | Un usuario de la universidad puede registrarse, verificar su correo, elegir sus intereses, iniciar y cerrar sesión, y recuperar su contraseña. |

## Specs comprometidos

| Spec | Responsable | Estado |
|---|---|---|
| [FS-USR-01 — Registro y verificación de cuenta](../../modulos/usuarios/specs/FS-USR-01-registro.md) | Por asignar | Borrador |
| [FS-USR-02 — Inicio y cierre de sesión](../../modulos/usuarios/specs/FS-USR-02-inicio-sesion.md) | Por asignar | Borrador |
| [FS-USR-03 — Recuperación de contraseña](../../modulos/usuarios/specs/FS-USR-03-recuperar-contrasena.md) | Por asignar | Borrador |
| [FS-USR-04 — Preferencias de contenido](../../modulos/usuarios/specs/FS-USR-04-preferencias-contenido.md) | Por asignar | Borrador |

## Tareas técnicas

- [ ] Configurar el servicio de envío de correos (verificación y recuperación).
- [ ] Cargar categorías iniciales como datos semilla (necesarias para FS-USR-04).
- [ ] Definir la lista de dominios institucionales permitidos.
- [ ] Implementar el almacenamiento seguro de contraseñas (hash con sal).
- [ ] Definir el manejo de sesión (tokens o cookies) y su expiración.

## Riesgos

| Riesgo | Mitigación |
|---|---|
| Los correos institucionales filtran o retrasan los correos automáticos. | Probar el envío al dominio de la universidad al inicio del sprint; coordinar con la oficina de TI si es necesario. |
| Las preguntas abiertas de los specs no se resuelven a tiempo. | Resolverlas en la planificación; ningún spec entra en desarrollo sin estar **Aprobado**. |

## Revisión

_Completar al cierre del sprint._

## Retrospectiva

| Qué funcionó | Qué mejorar | Acción |
|---|---|---|
| | | |
