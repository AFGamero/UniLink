# FS-PRY-01 — Espacios de proyectos

| Campo | Valor |
|---|---|
| **Módulo** | Proyectos (PRY) |
| **Sprint** | Sprint 08 |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-11](../../requisitos/CasosDeUso.md#cu-11--gestionar-espacio-de-proyectos) |
| **Historias** | [HU-11](../../requisitos/HistoriasDeUsuario.md#hu-11) |
| **Última actualización** | 2026-10-06 |

## 1. Objetivo

Dar a los equipos de la universidad un espacio donde reclutar integrantes con las habilidades que necesitan, organizar las tareas del proyecto y dejar constancia del trabajo realizado, que luego sirve como portafolio en el perfil de cada miembro.

## 2. Alcance

**Incluye:**

- Crear, editar, finalizar y eliminar proyectos.
- Explorar proyectos con orden por afinidad.
- Solicitudes de unión, invitaciones y salida del proyecto.
- Espacio del proyecto con resumen, tareas, miembros y actividad.
- Proyectos finalizados en el perfil de los miembros.
- Sugerencias de proyectos en el onboarding ([FS-RED-02](../red/FS-RED-02-onboarding-sugerencias.md)).

**No incluye:**

- Roles y permisos de los miembros ([FS-PRY-02](./FS-PRY-02-roles-proyectos.md)).
- Chat grupal, archivos compartidos o control de versiones dentro del proyecto.
- Proyectos privados que no aparecen en la exploración.

## 3. Actores

| Actor | Participación |
|---|---|
| Usuario autenticado | Crea proyectos, explora y solicita unirse. |
| Administrador de proyecto | Aprueba solicitudes, invita y gestiona el proyecto. |
| Miembro del proyecto | Colabora en las tareas. |

## 4. Reglas de negocio

**Proyecto**

| ID | Regla |
|---|---|
| RN-01 | Cualquier usuario autenticado puede crear proyectos. Quien lo crea es su **creador** y queda como administrador ([FS-PRY-02](./FS-PRY-02-roles-proyectos.md)). |
| RN-02 | Todo proyecto usa una categoría activa de tipo "Proyectos" ([FS-ADM-01](../administracion/FS-ADM-01-gestion-categorias.md)). |
| RN-03 | El máximo de integrantes va de 2 a 50 e incluye al creador. No puede quedar por debajo del número actual de miembros. |
| RN-04 | Los proyectos son visibles para todos los usuarios autenticados. |
| RN-05 | **Afinidad:** porcentaje de las habilidades buscadas del proyecto que el usuario tiene en sus habilidades o en su "Puedo aportar", igual que en [FS-OPO-01](../oportunidades/FS-OPO-01-publicacion-oportunidades.md), RN-13. |
| RN-06 | **Finalizar:** el proyecto queda en solo lectura, deja de recibir solicitudes y aparece en la sección "Proyectos" del perfil de cada miembro como parte de su portafolio. |
| RN-07 | Un proyecto solo puede eliminarse si su único miembro es el creador. Con más miembros solo puede finalizarse. |

**Membresía**

| ID | Regla |
|---|---|
| RN-08 | Se puede solicitar unirse solo si el proyecto está "Reclutando" y tiene cupo. La solicitud lleva un mensaje de 20 a 500 caracteres. |
| RN-09 | Los administradores del proyecto aprueban o rechazan las solicitudes. Al rechazar, el solicitante es notificado y puede volver a solicitar después de 30 días. |
| RN-10 | Los administradores pueden invitar a sus conexiones. La invitación cuenta como solicitud aprobada: si el invitado acepta, entra directamente. Las invitaciones vencen a los 14 días. |
| RN-11 | Al llenarse el cupo, el proyecto deja de recibir solicitudes y las pendientes se mantienen hasta que haya un lugar o un administrador las rechace. |
| RN-12 | Un miembro puede salir del proyecto cuando quiera, excepto si es su único administrador ([FS-PRY-02](./FS-PRY-02-roles-proyectos.md), RN-05). Sus tareas asignadas quedan sin responsable. |
| RN-13 | Los nuevos miembros entran con el rol por defecto definido en [FS-PRY-02](./FS-PRY-02-roles-proyectos.md). |

**Tareas**

| ID | Regla |
|---|---|
| RN-14 | Cada tarea tiene título, descripción opcional, responsable opcional (un miembro), fecha límite opcional y estado: Por hacer, En progreso o Hecha. |
| RN-15 | Quién puede crear, editar, mover o eliminar tareas lo define [FS-PRY-02](./FS-PRY-02-roles-proyectos.md). |
| RN-16 | Al asignar una tarea, el responsable recibe una notificación. |
| RN-17 | La pestaña Actividad registra: ingresos y salidas de miembros, cambios de rol, tareas creadas, completadas y eliminadas, y cambios en la información del proyecto. |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El sistema debe ofrecer la sección "Proyectos" en el menú principal con el botón "Crear proyecto". | Alta |
| RF-02 | La sección debe mostrar los proyectos que están reclutando como tarjetas (nombre, categoría, habilidades buscadas, integrantes y cupo, afinidad), con búsqueda, filtros por categoría y habilidad, y orden por afinidad o más recientes. | Alta |
| RF-03 | La sección debe tener las pestañas "Explorar", "Mis proyectos" y "Finalizados". | Media |
| RF-04 | El espacio de cada proyecto debe tener las pestañas Resumen, Tareas, Miembros y Actividad. Quienes no son miembros solo ven Resumen y Miembros. | Alta |
| RF-05 | La pestaña Tareas debe mostrar un tablero con tres columnas (Por hacer, En progreso, Hecha) donde las tareas se arrastran entre columnas, y un filtro "Mis tareas". | Alta |
| RF-06 | El sistema debe permitir solicitar unirse (RN-08), y a los administradores aprobar o rechazar solicitudes desde la pestaña Miembros (RN-09). | Alta |
| RF-07 | El sistema debe permitir a los administradores invitar a sus conexiones (RN-10). | Media |
| RF-08 | El sistema debe permitir salir del proyecto (RN-12), finalizarlo (RN-06) y eliminarlo (RN-07). | Alta |
| RF-09 | El perfil de cada usuario debe mostrar los proyectos finalizados en los que participó, con su rol y fechas. | Media |
| RF-10 | El onboarding ([FS-RED-02](../red/FS-RED-02-onboarding-sugerencias.md)) debe sugerir hasta 5 proyectos que están reclutando, con afinidad mayor a 0. Elegir uno envía una solicitud con el mensaje "Me interesa unirme a este proyecto." | Media |

## 6. Datos y validaciones

| Campo | Tipo | Obligatorio | Validación |
|---|---|---|---|
| Nombre | Texto | Sí | 3 a 80 caracteres. |
| Descripción | Texto largo | Sí | 50 a 4.000 caracteres. |
| Objetivos | Lista | Sí | De 1 a 10 objetivos de hasta 200 caracteres cada uno. |
| Categoría | Lista | Sí | Categorías activas de tipo "Proyectos". |
| Habilidades buscadas | Etiquetas | No | Máximo 10, del catálogo de FS-PRF-01. |
| Perfiles que buscamos | Texto | No | Máximo 500 caracteres (por ejemplo, "Un diseñador UX y dos desarrolladores web"). |
| Máximo de integrantes | Número | Sí | RN-03. |
| Mensaje de solicitud | Texto | Sí, al solicitar | RN-08. |
| Título de tarea | Texto | Sí | 3 a 120 caracteres. |
| Descripción de tarea | Texto | No | Máximo 2.000 caracteres. |
| Fecha límite de tarea | Fecha | No | Igual o posterior a hoy al crearla. |

## 7. Estados

**Estado del proyecto:**

| Estado | Entra cuando | Sale hacia |
|---|---|---|
| Reclutando | Se crea, o un administrador lo reabre | **En curso** (un administrador cierra el reclutamiento) o **Finalizado** |
| En curso | Se cierra el reclutamiento | **Reclutando** o **Finalizado** |
| Finalizado | Un administrador lo finaliza | Estado final (solo lectura) |

**Estado de la solicitud de unión:** Pendiente → Aprobada, Rechazada o Cancelada (por el solicitante).

## 8. Flujo de pantallas

1. **Proyectos** → "Crear proyecto" → **Formulario** → "Crear" → **Espacio del proyecto**.
2. **Proyectos > Explorar** → selecciona un proyecto → **Resumen** → "Solicitar unirme" → escribe el mensaje → "Enviar".
3. **Espacio del proyecto > Miembros** (administrador) → "Solicitudes" → "Aprobar" o "Rechazar".
4. **Espacio del proyecto > Tareas** → "Nueva tarea" → arrastra tareas entre columnas.

## 9. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Proyecto creado | "Tu proyecto está creado. Invita a tus conexiones o espera solicitudes." |
| MSG-02 | Solicitud enviada | "Enviamos tu solicitud a los administradores de \"{proyecto}\"." |
| MSG-03 | Cupo completo | "Este proyecto ya completó sus {n} integrantes." |
| MSG-04 | Proyecto no recluta | "Este proyecto no está buscando integrantes en este momento." |
| MSG-05 | Espera tras rechazo | "Podrás volver a solicitar unirte a partir del {fecha}." |
| MSG-06 | Confirmar finalizar | "El proyecto quedará en solo lectura y aparecerá en el perfil de sus {n} miembros. ¿Finalizarlo?" |
| MSG-07 | No se puede eliminar | "El proyecto tiene otros miembros. Puedes finalizarlo, pero no eliminarlo." |

## 10. Criterios de aceptación

```gherkin
Escenario: Crear un proyecto
  Dado que soy un usuario autenticado
  Cuando creo un proyecto con nombre, descripción, objetivos, categoría y máximo de 5 integrantes
  Entonces veo el mensaje MSG-01
  Y soy administrador del proyecto
  Y el proyecto aparece en "Explorar" como "Reclutando"

Escenario: Afinidad con un proyecto
  Dado que un proyecto busca "React" y "Diseño UX"
  Y yo tengo "React" en mis habilidades
  Cuando lo veo en Explorar
  Entonces su afinidad es 50 %

Escenario: Solicitar unirse y ser aprobado
  Dado que un proyecto está reclutando y tiene cupo
  Cuando solicito unirme con un mensaje
  Entonces veo el mensaje MSG-02
  Y los administradores reciben una notificación
  Cuando un administrador aprueba mi solicitud
  Entonces soy miembro con el rol por defecto y veo las pestañas Tareas y Actividad

Escenario: Cupo completo
  Dado que un proyecto tiene 5 de 5 integrantes
  Cuando abro su resumen
  Entonces veo el mensaje MSG-03 en lugar del botón "Solicitar unirme"

Escenario: Invitar a una conexión
  Dado que soy administrador de un proyecto y estoy conectado con Luis
  Cuando invito a Luis y él acepta
  Entonces Luis es miembro del proyecto sin pasar por aprobación

Escenario: Tablero de tareas
  Dado que soy miembro con permiso de edición
  Cuando creo una tarea, se la asigno a Ana y la muevo a "En progreso"
  Entonces Ana recibe una notificación
  Y la tarea aparece en la columna "En progreso"
  Y la pestaña Actividad registra la creación

Escenario: Salir del proyecto
  Dado que soy miembro con 2 tareas asignadas
  Cuando salgo del proyecto
  Entonces dejo de ser miembro
  Y mis 2 tareas quedan sin responsable

Escenario: Finalizar y portafolio
  Dado que soy administrador de un proyecto con 4 miembros
  Cuando lo finalizo
  Entonces el proyecto queda en solo lectura
  Y aparece en la sección "Proyectos" del perfil de los 4 miembros

Escenario: Sugerencia en el onboarding
  Dado que soy un usuario nuevo con la habilidad "React"
  Y un proyecto que busca "React" está reclutando
  Entonces el proyecto aparece entre mis sugerencias del onboarding
```

## 11. Dependencias

- [FS-PRY-02](./FS-PRY-02-roles-proyectos.md): roles, permisos y rol por defecto.
- [FS-ADM-01](../administracion/FS-ADM-01-gestion-categorias.md): categorías de tipo "Proyectos".
- [FS-PRF-01](../perfil/FS-PRF-01-perfil-profesional.md): etiquetas para la afinidad y sección de proyectos del perfil.
- [FS-RED-01](../red/FS-RED-01-solicitudes-conexion.md): conexiones para las invitaciones.
- [FS-RED-02](../red/FS-RED-02-onboarding-sugerencias.md): onboarding que se extiende.
- [FS-NOT-01](../notificaciones/FS-NOT-01-centro-notificaciones.md): notificaciones de proyectos.

## 12. Preguntas abiertas

- [ ] ¿Se necesita un espacio de conversación del equipo dentro del proyecto, o los miembros se coordinan por mensajes privados?
- [ ] ¿Los proyectos de clase (por ejemplo, de una asignatura) deben poder ser privados?

## 13. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Gamero | Creación |
