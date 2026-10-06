# FS-PRY-02 — Roles en proyectos

| Campo | Valor |
|---|---|
| **Módulo** | Proyectos (PRY) |
| **Sprint** | Sprint 08 |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-16](../../requisitos/CasosDeUso.md#cu-16--administrar-roles-en-espacios-de-proyectos) |
| **Historias** | [HU-27](../../requisitos/HistoriasDeUsuario.md#hu-27) |
| **Última actualización** | 2026-10-06 |

## 1. Objetivo

Permitir que cada proyecto controle quién puede ver, editar y administrar su espacio, para que los equipos colaboren con orden y ningún proyecto quede sin quien lo gestione.

## 2. Alcance

**Incluye:**

- Tres roles: Visualizador, Editor y Administrador.
- Matriz de permisos por rol.
- Cambiar el rol de un miembro y retirar miembros.
- Protección del creador y regla del último administrador.

**No incluye:**

- Roles personalizados o permisos por tarea.
- Transferir la autoría (creador) del proyecto.

## 3. Actores

| Actor | Participación |
|---|---|
| Administrador de proyecto | Asigna roles y retira miembros. |
| Miembro del proyecto | Recibe el aviso de su cambio de rol. |

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Todo miembro tiene exactamente un rol: Visualizador, Editor o Administrador. |
| RN-02 | Los nuevos miembros, por solicitud o invitación, entran como **Editor**. |
| RN-03 | Los permisos de cada rol son los de la matriz de la sección 6 y se aplican de inmediato al cambiar el rol, también en sesiones abiertas. |
| RN-04 | Solo los administradores cambian roles y retiran miembros. Un administrador puede cambiar su propio rol. |
| RN-05 | **Último administrador:** un proyecto siempre tiene al menos un administrador. Si el único administrador intenta quitarse el rol o salir del proyecto, el sistema lo impide hasta que nombre a otro. |
| RN-06 | **Protección del creador:** nadie puede quitarle el rol de administrador al creador ni retirarlo del proyecto. Solo él puede cambiar su propio rol o salir, respetando RN-05. |
| RN-07 | Al retirar a un miembro, sus tareas quedan sin responsable y el miembro recibe una notificación. Puede volver a solicitar unirse después de 30 días. |
| RN-08 | Cada cambio de rol y cada retiro notifica al miembro afectado y queda en la pestaña Actividad ([FS-PRY-01](./FS-PRY-01-espacios-proyectos.md), RN-17). |
| RN-09 | En un proyecto finalizado no se pueden cambiar roles ni retirar miembros. |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | La pestaña Miembros debe mostrar a cada miembro con su rol, fecha de ingreso y, para el creador, la etiqueta "Creador". | Alta |
| RF-02 | Los administradores deben ver junto a cada miembro un selector de rol y la opción "Retirar del proyecto", excepto donde RN-05 o RN-06 lo impiden. | Alta |
| RF-03 | El sistema debe validar cada acción contra la matriz de permisos en el servidor, no solo ocultar botones en la pantalla. | Alta |
| RF-04 | El sistema debe aplicar RN-05 y RN-06 con un mensaje que explique por qué la acción no está permitida. | Alta |
| RF-05 | El sistema debe enviar la notificación de RN-08 y registrar el cambio en Actividad. | Media |
| RF-06 | Cada miembro debe poder consultar qué puede hacer su rol (tabla de permisos accesible desde la pestaña Miembros). | Baja |

## 6. Datos y validaciones

**Matriz de permisos:**

| Acción | Visualizador | Editor | Administrador |
|---|---|---|---|
| Ver resumen, tareas, miembros y actividad | ✓ | ✓ | ✓ |
| Crear tareas | — | ✓ | ✓ |
| Editar y mover cualquier tarea | — | ✓ | ✓ |
| Mover las tareas asignadas a uno mismo | ✓ | ✓ | ✓ |
| Eliminar tareas creadas por uno mismo | — | ✓ | ✓ |
| Eliminar cualquier tarea | — | — | ✓ |
| Editar la información del proyecto | — | — | ✓ |
| Aprobar o rechazar solicitudes e invitar | — | — | ✓ |
| Cambiar roles y retirar miembros | — | — | ✓ |
| Abrir o cerrar el reclutamiento y finalizar el proyecto | — | — | ✓ |
| Eliminar el proyecto ([FS-PRY-01](./FS-PRY-01-espacios-proyectos.md), RN-07) | — | — | Solo el creador |
| Salir del proyecto | ✓ | ✓ | ✓ (respetando RN-05) |

## 7. Estados

No aplica: el rol es un atributo del miembro, sin ciclo de vida propio.

## 8. Flujo de pantallas

1. **Espacio del proyecto > Miembros** → selector de rol junto a un miembro → elige el nuevo rol → confirma.
2. **Miembros** → "Retirar del proyecto" → confirma.

## 9. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Último administrador | "El proyecto debe tener al menos un administrador. Nombra a otro antes de dejar este rol." |
| MSG-02 | Protección del creador | "No puedes cambiar el rol ni retirar al creador del proyecto." |
| MSG-03 | Aviso al miembro | "Ahora eres {rol} en \"{proyecto}\"." |
| MSG-04 | Aviso de retiro | "Ya no eres miembro de \"{proyecto}\"." |
| MSG-05 | Confirmar retiro | "¿Retirar a {nombre} del proyecto? Sus tareas quedarán sin responsable." |
| MSG-06 | Acción sin permiso | "Tu rol en este proyecto no permite esta acción." |

## 10. Criterios de aceptación

```gherkin
Escenario: Rol por defecto
  Dado que un administrador aprueba mi solicitud de unión
  Entonces entro al proyecto como Editor

Escenario: Cambiar el rol de un miembro
  Dado que soy administrador y Ana es Editora
  Cuando cambio su rol a Visualizadora
  Entonces Ana recibe el aviso MSG-03
  Y Ana ya no puede crear tareas, aunque tenga el proyecto abierto
  Y la pestaña Actividad registra el cambio

Escenario: Visualizador mueve su propia tarea
  Dado que soy Visualizador y tengo una tarea asignada
  Cuando la muevo a "Hecha"
  Entonces el cambio se guarda

Escenario: Visualizador intenta editar otra tarea
  Dado que soy Visualizador
  Cuando intento editar una tarea asignada a otra persona
  Entonces veo el mensaje MSG-06

Escenario: Último administrador
  Dado que soy el único administrador de un proyecto
  Cuando intento cambiar mi rol a Editor
  Entonces veo el mensaje MSG-01 y mi rol no cambia

Escenario: Protección del creador
  Dado que Luis creó el proyecto y yo también soy administrador
  Cuando intento quitarle el rol de administrador a Luis
  Entonces veo el mensaje MSG-02

Escenario: Retirar a un miembro
  Dado que soy administrador y Pedro tiene 3 tareas asignadas
  Cuando lo retiro del proyecto
  Entonces Pedro recibe el aviso MSG-04
  Y sus 3 tareas quedan sin responsable

Escenario: Permisos validados en el servidor
  Dado que soy Editor
  Cuando envío directamente al servidor una petición para cambiar el rol de otro miembro
  Entonces la petición es rechazada
```

## 11. Dependencias

- [FS-PRY-01](./FS-PRY-01-espacios-proyectos.md): proyectos, membresía, tareas y actividad.
- [FS-NOT-01](../notificaciones/FS-NOT-01-centro-notificaciones.md): avisos de cambio de rol y retiro.

## 12. Preguntas abiertas

- [ ] ¿El rol por defecto debe ser configurable por cada proyecto (por ejemplo, que un proyecto grande haga entrar a todos como Visualizadores)?

## 13. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Gamero | Creación |
