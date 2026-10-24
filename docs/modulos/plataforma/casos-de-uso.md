# Casos de uso — Plataforma

_MVP — Red Profesional Universitaria — Universidad del Magdalena_
_Centro de Interés de Desarrollo Tecnológico e Innovación (CIDTI)_

Casos de uso del módulo Plataforma (PLT). Los actores se definen en el [mapa de módulos](../README.md#actores).

## Índice

- [CU-26 — Administrar categorías](#cu-26--administrar-categorías)

---

## CU-26 — Administrar categorías

**Actor(es):** Administrador de la plataforma

**Descripción:** Permite al administrador gestionar las categorías disponibles para publicaciones, proyectos, eventos, oportunidades y, en la fase 2, servicios.

**Precondiciones:** El administrador debe estar autenticado con rol de administrador de la plataforma.

**Flujo principal:**

1. El administrador accede a la gestión de categorías.
2. El sistema muestra las categorías existentes agrupadas por tipo de contenido.
3. El administrador crea una categoría indicando su nombre y tipo de contenido, o desactiva una existente.
4. El sistema guarda los cambios.

**Flujos alternativos / excepciones:**

- 3a. Ya existe una categoría con el mismo nombre para ese tipo de contenido: el sistema rechaza la creación.
- 3b. _(Fase 2)_ El administrador revisa una solicitud de nueva categoría enviada por un usuario ([CU-28](../servicios/casos-de-uso.md#cu-28--publicar-servicio)): la aprueba (se crea la categoría) o la rechaza, y el sistema notifica al solicitante.

**Postcondiciones:** Las categorías quedan actualizadas. Una categoría desactivada no puede usarse en contenido nuevo, pero el contenido existente la conserva.

**Prioridad:** Media
