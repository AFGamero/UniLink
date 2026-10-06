# FS-OPO-01 — Publicación de oportunidades

| Campo | Valor |
|---|---|
| **Módulo** | Oportunidades (OPO) |
| **Sprint** | Sprint 06 |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-22](../../requisitos/CasosDeUso.md#cu-22--publicar-oportunidades-y-gestionar-postulaciones) |
| **Historias** | [HU-29](../../requisitos/HistoriasDeUsuario.md#hu-29) |
| **Última actualización** | 2026-10-06 |

## 1. Objetivo

Permitir que profesores, grupos de investigación, dependencias y estudiantes publiquen oportunidades de investigación, proyectos o voluntariado, y gestionen a los postulantes hasta elegir a quienes participarán.

## 2. Alcance

**Incluye:**

- Crear, editar, cerrar y cancelar oportunidades.
- Habilidades requeridas, para calcular la afinidad con cada postulante.
- Panel del responsable con las postulaciones recibidas.
- Cambio de estado de las postulaciones con retroalimentación.
- Cierre automático por fecha o por cupos completos.

**No incluye:**

- Explorar oportunidades y postularse ([FS-OPO-02](./FS-OPO-02-postulaciones.md)).
- Reportar oportunidades (se puede agregar con el mecanismo de [FS-ADM-03](../administracion/FS-ADM-03-moderacion-contenido.md) en una versión posterior).
- Oportunidades de empresas externas a la universidad.
- Preguntas personalizadas o formularios para los postulantes.

## 3. Actores

| Actor | Participación |
|---|---|
| Responsable de oportunidad | Publica la oportunidad y gestiona sus postulaciones. |
| Postulante | Recibe las notificaciones de cambio de estado. |

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Cualquier usuario autenticado con cuenta activa puede publicar oportunidades y se convierte en su responsable. |
| RN-02 | Toda oportunidad usa una categoría activa de tipo "Oportunidades" ([FS-ADM-01](../administracion/FS-ADM-01-gestion-categorias.md)). |
| RN-03 | La fecha de cierre debe ser al menos 1 día después de la publicación y como máximo 6 meses después. |
| RN-04 | Las oportunidades son visibles para todos los usuarios autenticados, sin importar la privacidad del perfil del responsable. |
| RN-05 | **Cierre automático:** la oportunidad se cierra a nuevas postulaciones al llegar la fecha de cierre o cuando el número de postulaciones aceptadas iguala los cupos. |
| RN-06 | **Edición:** mientras esté abierta, el responsable puede editar todo excepto la categoría. Los cupos no pueden quedar por debajo del número de aceptados. Si cambia la descripción o los requisitos, la oportunidad muestra "Actualizada". |
| RN-07 | **Cerrar:** el responsable puede cerrarla antes de tiempo. Las postulaciones pendientes siguen en revisión y él puede seguir decidiéndolas. |
| RN-08 | **Cancelar:** si la oportunidad ya no se realizará, el responsable la cancela indicando el motivo. Las postulaciones "Enviada" y "En revisión" pasan a "Rechazada" con ese motivo como retroalimentación, y sus postulantes son notificados. |
| RN-09 | Una oportunidad sin postulaciones puede eliminarse por completo. Con postulaciones solo puede cancelarse. |
| RN-10 | **Cambios de estado de una postulación:** Enviada → En revisión, Aceptada o Rechazada; En revisión → Aceptada o Rechazada. "Aceptada" y "Rechazada" son definitivos. Cada cambio notifica al postulante. |
| RN-11 | La retroalimentación al rechazar es opcional, pero el sistema la recomienda. Al aceptar, el responsable puede escribir los siguientes pasos. |
| RN-12 | Al aceptar una postulación, se habilita una conversación privada entre el responsable y el postulante aunque no estén conectados ([FS-MSG-01](../mensajeria/FS-MSG-01-mensajeria-privada.md)). |
| RN-13 | **Afinidad:** porcentaje de las habilidades requeridas que el postulante tiene entre sus habilidades o su "Puedo aportar" ([FS-PRF-01](../perfil/FS-PRF-01-perfil-profesional.md)). Si la oportunidad no tiene habilidades requeridas, no se muestra afinidad. |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El sistema debe ofrecer el botón "Publicar oportunidad" en la sección Oportunidades. | Alta |
| RF-02 | El sistema debe validar y publicar la oportunidad con los datos de la sección 6. | Alta |
| RF-03 | El sistema debe ofrecer al responsable una página "Mis oportunidades publicadas" con cada oportunidad, su estado y el número de postulaciones por estado. | Alta |
| RF-04 | El panel de postulaciones de una oportunidad debe mostrar, por cada postulante: tarjeta de perfil, afinidad (RN-13), mensaje de motivación, fecha y estado, con filtro por estado y orden por afinidad o fecha. | Alta |
| RF-05 | El sistema debe permitir cambiar el estado de una o varias postulaciones a la vez, con retroalimentación opcional (RN-10, RN-11). | Alta |
| RF-06 | El sistema debe permitir editar, cerrar, cancelar y eliminar oportunidades según RN-06 a RN-09. | Alta |
| RF-07 | Una tarea programada debe cerrar las oportunidades que llegan a su fecha de cierre (RN-05). | Alta |
| RF-08 | El responsable debe recibir una notificación por cada postulación nueva y, si lo tiene activado, un correo. | Media |

## 6. Datos y validaciones

| Campo | Tipo | Obligatorio | Validación |
|---|---|---|---|
| Título | Texto | Sí | 10 a 120 caracteres. |
| Categoría | Lista | Sí | Categorías activas de tipo "Oportunidades". |
| Descripción | Texto largo | Sí | 50 a 4.000 caracteres. |
| Requisitos | Texto largo | No | Máximo 2.000 caracteres. |
| Habilidades requeridas | Etiquetas | No | Máximo 10, del catálogo de etiquetas de FS-PRF-01. |
| Modalidad | Opción | Sí | Presencial, Remota o Híbrida. |
| Dedicación | Número | No | Horas por semana, de 1 a 48. |
| Cupos | Número | Sí | De 1 a 100. |
| Fecha de cierre | Fecha | Sí | RN-03. |

**Categorías semilla de tipo "Oportunidades":** Investigación, Proyectos, Voluntariado, Monitorías, Semilleros.

## 7. Estados

**Estados de la oportunidad:**

| Estado | Entra cuando | Sale hacia |
|---|---|---|
| Abierta | Se publica | **Cerrada** (RN-05, RN-07) o **Cancelada** (RN-08) |
| Cerrada | Fecha de cierre, cupos completos o cierre manual | **Cancelada** |
| Cancelada | El responsable la cancela | Estado final |

**Estados de la postulación** (compartidos con [FS-OPO-02](./FS-OPO-02-postulaciones.md)): Enviada, En revisión, Aceptada, Rechazada y Retirada. Ver RN-10.

## 8. Flujo de pantallas

1. **Oportunidades** → "Publicar oportunidad" → **Formulario** → "Publicar" → **Detalle de la oportunidad**.
2. **Mis oportunidades publicadas** → selecciona una → **Panel de postulaciones** → selecciona postulantes → "Aceptar", "Rechazar" o "Pasar a revisión".
3. **Detalle de la oportunidad** (como responsable) → "Editar", "Cerrar" o "Cancelar".

## 9. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Oportunidad publicada | "Tu oportunidad está publicada. Te avisaremos cuando lleguen postulaciones." |
| MSG-02 | Fecha de cierre inválida | "La fecha de cierre debe estar entre mañana y dentro de 6 meses." |
| MSG-03 | Cupos menores que aceptados | "Ya aceptaste a {n} personas; los cupos no pueden ser menos." |
| MSG-04 | Confirmar cancelación | "Se rechazarán {n} postulaciones pendientes y se notificará a sus postulantes. ¿Cancelar la oportunidad?" |
| MSG-05 | Cupos completos | "Completaste los {n} cupos. La oportunidad se cerró a nuevas postulaciones." |
| MSG-06 | Recomendación de retroalimentación | "Contarle al postulante por qué no fue elegido le ayuda a mejorar. ¿Quieres agregar un comentario?" |

## 10. Criterios de aceptación

```gherkin
Escenario: Publicar una oportunidad
  Dado que soy un usuario autenticado
  Cuando publico una oportunidad de "Investigación" con 3 cupos y cierre en 15 días
  Entonces veo el mensaje MSG-01
  Y la oportunidad aparece en la sección Oportunidades para todos los usuarios

Escenario: Afinidad de un postulante
  Dado que mi oportunidad requiere "Python", "Estadística" y "R"
  Y Ana tiene "Python" en habilidades y "Estadística" en "Puedo aportar"
  Cuando veo su postulación
  Entonces su afinidad es 67 %

Escenario: Aceptar y completar cupos
  Dado que mi oportunidad tiene 2 cupos y ya acepté a 1 persona
  Cuando acepto a otra
  Entonces veo el mensaje MSG-05
  Y la oportunidad pasa a "Cerrada"
  Y nadie más puede postularse

Escenario: Aceptar habilita la conversación
  Dado que no estoy conectado con Ana
  Cuando acepto su postulación
  Entonces Ana recibe una notificación
  Y podemos enviarnos mensajes privados

Escenario: Estados definitivos
  Dado que rechacé la postulación de Pedro
  Entonces no puedo cambiarla a "Aceptada"

Escenario: Cancelar con postulaciones pendientes
  Dado que mi oportunidad tiene 4 postulaciones "En revisión"
  Cuando la cancelo con el motivo "Se canceló la financiación del proyecto"
  Entonces las 4 pasan a "Rechazada" con ese motivo
  Y sus postulantes reciben una notificación

Escenario: Cierre por fecha
  Dado que mi oportunidad cierra hoy
  Cuando se ejecuta la tarea programada
  Entonces la oportunidad pasa a "Cerrada"
  Y sigo pudiendo decidir las postulaciones pendientes
```

## 11. Dependencias

- [FS-ADM-01](../administracion/FS-ADM-01-gestion-categorias.md): categorías de tipo "Oportunidades".
- [FS-PRF-01](../perfil/FS-PRF-01-perfil-profesional.md): etiquetas y perfiles para la afinidad.
- [FS-MSG-01](../mensajeria/FS-MSG-01-mensajeria-privada.md): conversación tras la aceptación.
- [FS-NOT-01](../notificaciones/FS-NOT-01-centro-notificaciones.md): notificaciones de postulaciones.
- [FS-OPO-02](./FS-OPO-02-postulaciones.md): lado del postulante.

## 12. Preguntas abiertas

- [ ] ¿Cualquier usuario puede publicar oportunidades, o solo profesores, personal administrativo y grupos de investigación? Abrirlo a estudiantes permite voluntariados y proyectos estudiantiles, pero exige más moderación.
- [ ] ¿Se quiere sugerir oportunidades a los usuarios con alta afinidad (por ejemplo, una notificación "Hay una oportunidad para ti")?

## 13. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Gamero | Creación |
