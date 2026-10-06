# FS-OPO-02 — Postulaciones

| Campo | Valor |
|---|---|
| **Módulo** | Oportunidades (OPO) |
| **Sprint** | Sprint 06 |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-12](../../requisitos/CasosDeUso.md#cu-12--explorar-oportunidades), [CU-14](../../requisitos/CasosDeUso.md#cu-14--gestionar-estado-de-postulaciones) |
| **Historias** | [HU-12](../../requisitos/HistoriasDeUsuario.md#hu-12), [HU-25](../../requisitos/HistoriasDeUsuario.md#hu-25) |
| **Última actualización** | 2026-10-06 |

## 1. Objetivo

Ayudar a cada usuario a encontrar las oportunidades que mejor encajan con su perfil, postularse en pocos pasos y saber en todo momento en qué va cada postulación.

## 2. Alcance

**Incluye:**

- Sección Oportunidades con búsqueda, filtros y orden por afinidad.
- Detalle de una oportunidad.
- Postulación con mensaje de motivación.
- Panel "Mis postulaciones" con estado, historial y retroalimentación.
- Retirar una postulación.

**No incluye:**

- Publicar oportunidades y decidir postulaciones ([FS-OPO-01](./FS-OPO-01-publicacion-oportunidades.md)).
- Adjuntar archivos o la hoja de vida a la postulación: el responsable consulta el perfil del postulante.
- Guardar oportunidades como favoritas.

## 3. Actores

| Actor | Participación |
|---|---|
| Usuario autenticado (postulante) | Explora, se postula y hace seguimiento. |
| Responsable de oportunidad | Recibe la postulación (notificación). |

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Solo se puede postular a oportunidades en estado "Abierta". |
| RN-02 | Un usuario solo puede tener una postulación por oportunidad. Si la retira, no puede volver a postularse a la misma. |
| RN-03 | El responsable no puede postularse a su propia oportunidad. |
| RN-04 | La postulación exige un mensaje de motivación de 50 a 1.000 caracteres. |
| RN-05 | El responsable ve el perfil completo del postulante, sin importar su configuración de privacidad, mientras la postulación exista. |
| RN-06 | La afinidad se calcula igual que en [FS-OPO-01](./FS-OPO-01-publicacion-oportunidades.md), RN-13, y se muestra al postulante en cada oportunidad. |
| RN-07 | El postulante puede retirar su postulación mientras esté "Enviada" o "En revisión". Pasa a "Retirada" y el responsable es notificado. |
| RN-08 | Cada cambio de estado queda en el historial de la postulación con su fecha y, si existe, la retroalimentación del responsable. |
| RN-09 | Por defecto, la sección Oportunidades muestra solo las abiertas, ordenadas por afinidad y, a igual afinidad, por fecha de cierre más próxima. |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El sistema debe ofrecer la sección "Oportunidades" en el menú principal. | Alta |
| RF-02 | La sección debe mostrar cada oportunidad como tarjeta: título, responsable, categoría, modalidad, cupos disponibles, días para el cierre y afinidad. | Alta |
| RF-03 | La sección debe permitir buscar por texto y filtrar por categoría, modalidad, habilidad requerida y "Solo con afinidad mayor al 50 %". También debe permitir ordenar por afinidad, más recientes o cierre más próximo. | Alta |
| RF-04 | El detalle debe mostrar todos los datos de la oportunidad, el perfil resumido del responsable, las habilidades requeridas marcando cuáles tiene el usuario, y el botón "Postularme" o el estado de la postulación existente. | Alta |
| RF-05 | Al postularse, el sistema debe pedir el mensaje de motivación, confirmar el envío y notificar al responsable. | Alta |
| RF-06 | El sistema debe ofrecer el panel "Mis postulaciones" con cada postulación: oportunidad, responsable, fecha y estado como etiqueta de color, con filtro por estado. | Alta |
| RF-07 | Al abrir una postulación, el sistema debe mostrar el historial de estados con la retroalimentación (RN-08) y la opción "Retirar postulación" cuando aplique (RN-07). | Alta |
| RF-08 | El sistema debe mostrar un mensaje con enlace a la sección Oportunidades cuando el usuario no tenga postulaciones. | Media |

## 6. Datos y validaciones

| Campo | Tipo | Obligatorio | Validación |
|---|---|---|---|
| Mensaje de motivación | Texto largo | Sí | RN-04. |

**Colores de las etiquetas de estado** (siempre acompañados del texto, para no depender solo del color):

| Estado | Color |
|---|---|
| Enviada | Gris |
| En revisión | Azul |
| Aceptada | Verde |
| Rechazada | Rojo |
| Retirada | Gris tachado |

## 7. Estados

| Estado | Entra cuando | Sale hacia |
|---|---|---|
| Enviada | El usuario se postula | **En revisión**, **Aceptada**, **Rechazada** (responsable) o **Retirada** (postulante) |
| En revisión | El responsable la revisa | **Aceptada**, **Rechazada** o **Retirada** |
| Aceptada | Decisión del responsable | Estado final |
| Rechazada | Decisión del responsable o cancelación de la oportunidad | Estado final |
| Retirada | El postulante la retira | Estado final |

## 8. Flujo de pantallas

1. **Menú principal** → "Oportunidades" → filtra o busca → selecciona una → **Detalle**.
2. **Detalle** → "Postularme" → escribe la motivación → "Enviar postulación" → el detalle muestra "Enviada".
3. **Menú del usuario** → "Mis postulaciones" → selecciona una → **Historial** → "Retirar postulación" (opcional).

## 9. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Postulación enviada | "Te postulaste a \"{título}\". Te avisaremos cuando {responsable} la revise." |
| MSG-02 | Ya postulado | "Ya te postulaste a esta oportunidad. Estado: {estado}." |
| MSG-03 | Oportunidad cerrada | "Esta oportunidad ya no recibe postulaciones." |
| MSG-04 | Confirmar retiro | "Si retiras tu postulación no podrás volver a postularte a esta oportunidad. ¿Retirarla?" |
| MSG-05 | Sin postulaciones | "Aún no te has postulado a ninguna oportunidad. Explora las que encajan con tu perfil." |
| MSG-06 | Sin resultados | "No hay oportunidades abiertas con estos filtros." |
| MSG-07 | Ayuda de motivación | "Cuéntale al responsable por qué te interesa y qué puedes aportar." |

## 10. Criterios de aceptación

```gherkin
Escenario: Orden por afinidad
  Dado que tengo las habilidades "Python" y "Estadística"
  Y hay una oportunidad que requiere ambas y otra que requiere "Diseño gráfico"
  Cuando abro la sección Oportunidades
  Entonces la que requiere Python y Estadística aparece primero con 100 % de afinidad

Escenario: Postularse
  Dado que veo una oportunidad abierta
  Cuando me postulo con un mensaje de motivación de 120 caracteres
  Entonces veo el mensaje MSG-01
  Y la postulación aparece en "Mis postulaciones" como "Enviada"
  Y el responsable recibe una notificación

Escenario: Motivación muy corta
  Dado que me estoy postulando
  Cuando escribo un mensaje de 20 caracteres
  Entonces no puedo enviar la postulación

Escenario: Postulación repetida
  Dado que ya me postulé a una oportunidad
  Cuando abro su detalle
  Entonces veo el mensaje MSG-02 en lugar del botón "Postularme"

Escenario: Seguimiento con retroalimentación
  Dado que el responsable rechazó mi postulación con un comentario
  Cuando abro la postulación en "Mis postulaciones"
  Entonces veo el estado "Rechazada" con el comentario y la fecha
  Y veo el historial completo de estados

Escenario: Retirar postulación
  Dado que mi postulación está "En revisión"
  Cuando la retiro y confirmo
  Entonces pasa a "Retirada"
  Y el responsable recibe una notificación
  Y no puedo volver a postularme a esa oportunidad

Escenario: Perfil privado visible para el responsable
  Dado que mi perfil es "Solo mis conexiones" y no estoy conectado con el responsable
  Cuando me postulo
  Entonces el responsable puede ver mi perfil completo

Escenario: Sin postulaciones
  Dado que nunca me he postulado
  Cuando abro "Mis postulaciones"
  Entonces veo el mensaje MSG-05 con un enlace a Oportunidades
```

## 11. Dependencias

- [FS-OPO-01](./FS-OPO-01-publicacion-oportunidades.md): oportunidades, afinidad y decisiones del responsable.
- [FS-PRF-01](../perfil/FS-PRF-01-perfil-profesional.md): habilidades y "Puedo aportar" del postulante.
- [FS-NOT-01](../notificaciones/FS-NOT-01-centro-notificaciones.md): notificaciones de postulación y de cambio de estado.

## 12. Preguntas abiertas

- [ ] ¿Se debe limitar el número de postulaciones activas por usuario para evitar que se postulen a todo sin leer?

## 13. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Gamero | Creación |
