# FS-ADM-01 — Gestión de categorías

| Campo | Valor |
|---|---|
| **Módulo** | Administración (ADM) |
| **Sprint** | Sprint 04 |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-26](../../requisitos/CasosDeUso.md#cu-26--administrar-categorías) |
| **Historias** | [HU-20](../../requisitos/HistoriasDeUsuario.md#hu-20) |
| **Última actualización** | 2026-10-06 |

## 1. Objetivo

Permitir que el administrador de la plataforma mantenga ordenada la clasificación del contenido sin depender del equipo técnico. Este es también el **primer spec del panel de administración**, por lo que define cómo se accede a él.

## 2. Alcance

**Incluye:**

- Acceso al panel de administración y su control de permisos.
- Listado de categorías por tipo de contenido.
- Crear, editar, ordenar, desactivar y reactivar categorías.
- Registro de las acciones del administrador.

**No incluye:**

- Asignar el rol de administrador desde la interfaz (ver RN-01).
- Revisar solicitudes de categorías nuevas enviadas por usuarios: la única fuente de esas solicitudes es la publicación de servicios, así que se agrega con FS-SRV-02 (Sprint 9).
- Gestión de cuentas (FS-ADM-02) y moderación (FS-ADM-03).

## 3. Actores

| Actor | Participación |
|---|---|
| Administrador de la plataforma | Gestiona las categorías. |

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | El rol de administrador de la plataforma se asigna directamente en la base de datos por el equipo técnico, con registro de quién lo asignó. No existe una pantalla para asignarlo en el MVP. |
| RN-02 | Solo los usuarios con rol de administrador pueden entrar al panel. Cualquier otro usuario que intente abrir una dirección del panel recibe una página de "Acceso denegado". |
| RN-03 | Cada categoría pertenece a un solo tipo de contenido: Publicaciones, Proyectos, Eventos, Oportunidades o Servicios. |
| RN-04 | El nombre de una categoría es único dentro de su tipo (sin distinguir mayúsculas ni tildes). Dos tipos distintos sí pueden tener categorías con el mismo nombre (por ejemplo, "Investigación" en Publicaciones y en Proyectos). |
| RN-05 | Las categorías no se eliminan, solo se desactivan. Una categoría desactivada no aparece al crear contenido nuevo ni en las preferencias, pero el contenido existente la conserva y sigue visible con ella ([FS-CTA-04](../cuenta/FS-CTA-04-preferencias-contenido.md), RN-03). |
| RN-06 | No se puede desactivar la última categoría activa de un tipo. |
| RN-07 | Al cambiar el nombre de una categoría, el cambio se refleja en todo el contenido que la usa. |
| RN-08 | El administrador define el orden en que se muestran las categorías de cada tipo. Las nuevas se agregan al final. |
| RN-09 | Toda creación, edición, desactivación o reactivación queda registrada con el administrador, la fecha, la acción y los valores anterior y nuevo. |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El sistema debe mostrar la opción "Administración" en el menú del usuario solo a los administradores. | Alta |
| RF-02 | El panel debe tener un menú lateral con las secciones de administración. En este sprint solo existe "Categorías"; "Usuarios" y "Moderación" se agregan en el Sprint 5. | Alta |
| RF-03 | La sección Categorías debe mostrar una pestaña por tipo de contenido con sus categorías: nombre, descripción, estado, cantidad de contenido que la usa y orden. | Alta |
| RF-04 | El sistema debe permitir crear y editar categorías (RN-03, RN-04, RN-07). | Alta |
| RF-05 | El sistema debe permitir desactivar y reactivar categorías (RN-05, RN-06), pidiendo confirmación al desactivar e indicando cuánto contenido la usa. | Alta |
| RF-06 | El sistema debe permitir reordenar las categorías de un tipo arrastrándolas (RN-08). | Baja |
| RF-07 | El sistema debe mostrar el historial de cambios de cada categoría (RN-09). | Media |

## 6. Datos y validaciones

| Campo | Tipo | Obligatorio | Validación |
|---|---|---|---|
| Tipo de contenido | Lista | Sí | Publicaciones, Proyectos, Eventos, Oportunidades o Servicios. No se puede cambiar después de crear la categoría. |
| Nombre | Texto | Sí | 2 a 40 caracteres; RN-04. |
| Descripción | Texto | No | Máximo 200 caracteres. Se muestra como ayuda al elegir la categoría. |

Las categorías semilla cargadas en el Sprint 1 ([FS-CTA-04](../cuenta/FS-CTA-04-preferencias-contenido.md), sección 6) quedan administrables desde este panel.

## 7. Estados

| Estado | Entra cuando | Sale hacia |
|---|---|---|
| Activa | Se crea o se reactiva | **Inactiva** al desactivarla (si no es la última activa del tipo) |
| Inactiva | Se desactiva | **Activa** al reactivarla |

## 8. Flujo de pantallas

1. **Menú del usuario** → "Administración" → **Panel** → "Categorías".
2. **Categorías** → pestaña de un tipo → "Nueva categoría" → **Formulario** → "Guardar".
3. **Categorías** → menú de una categoría → "Editar", "Desactivar", "Reactivar" o "Ver historial".

## 9. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Acceso denegado | "No tienes permiso para ver esta página." |
| MSG-02 | Nombre repetido | "Ya existe una categoría llamada \"{nombre}\" en {tipo}." |
| MSG-03 | Confirmar desactivación | "\"{nombre}\" la usan {n} elementos. Seguirán mostrándola, pero no podrá usarse en contenido nuevo. ¿Desactivar?" |
| MSG-04 | Última categoría activa | "No puedes desactivar la última categoría activa de {tipo}." |
| MSG-05 | Categoría guardada | "Categoría guardada." |

## 10. Criterios de aceptación

```gherkin
Escenario: Acceso solo para administradores
  Dado que soy un usuario sin rol de administrador
  Cuando abro la dirección del panel de administración
  Entonces veo el mensaje MSG-01
  Y no veo la opción "Administración" en mi menú

Escenario: Crear categoría
  Dado que soy administrador
  Cuando creo la categoría "Bioinformática" en Publicaciones
  Entonces veo el mensaje MSG-05
  Y los usuarios pueden elegirla al publicar y en sus intereses

Escenario: Nombre repetido en el mismo tipo
  Dado que existe "Investigación" en Publicaciones
  Cuando intento crear "investigacion" en Publicaciones
  Entonces veo el mensaje MSG-02

Escenario: Mismo nombre en otro tipo
  Dado que existe "Investigación" en Publicaciones
  Cuando creo "Investigación" en Proyectos
  Entonces la categoría se crea sin error

Escenario: Desactivar categoría en uso
  Dado que "Emprendimiento" la usan 12 publicaciones
  Cuando la desactivo
  Entonces las 12 publicaciones siguen mostrando "Emprendimiento"
  Y ya no aparece al crear una publicación nueva

Escenario: Última categoría activa
  Dado que "Culturales" es la única categoría activa de Eventos
  Cuando intento desactivarla
  Entonces veo el mensaje MSG-04

Escenario: Historial
  Dado que renombré "Tecnología" a "Tecnología e innovación"
  Cuando abro su historial
  Entonces veo mi nombre, la fecha, la acción y los valores anterior y nuevo
```

## 11. Dependencias

- [FS-CTA-04](../cuenta/FS-CTA-04-preferencias-contenido.md): categorías semilla y preferencias.
- [FS-CNT-01](../contenido/FS-CNT-01-publicaciones-feed.md): primer módulo que usa las categorías de Publicaciones para crear contenido.

## 12. Preguntas abiertas

- [ ] ¿Quiénes serán los administradores de la plataforma en el lanzamiento (equipo del CIDTI, bienestar universitario, otra dependencia)?
- [ ] ¿Se necesita más adelante un rol de "moderador" con menos permisos que el administrador?

## 13. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Gamero | Creación |
