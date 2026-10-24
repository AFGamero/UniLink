# Historias de usuario — Contenido

_MVP — Red Profesional Universitaria — Universidad del Magdalena_
_Centro de Interés de Desarrollo Tecnológico e Innovación (CIDTI)_

Historias de usuario del módulo Contenido (CNT), en formato "Como / quiero / para", derivadas de sus [casos de uso](./casos-de-uso.md).

## Índice

- [HU-08 — Como usuario autenticado, quiero publicar contenido académico o profesional (proyectos, logros, oportunidades o artículos)](#hu-08)
- [HU-09 — Como usuario autenticado, quiero visualizar las publicaciones de mi red y de mis categorías de interés, filtradas por categoría o relevancia](#hu-09)
- [HU-18 — Como administrador, quiero gestionar las publicaciones realizadas por los usuarios](#hu-18)
- [HU-19 — Como administrador, quiero gestionar los eventos publicados por los usuarios](#hu-19)

---

## HU-08

> **Como** usuario autenticado,
> **quiero** publicar contenido académico o profesional (proyectos, logros, oportunidades o artículos),
> **para** compartir información relevante con mi red de conexiones y con la comunidad interesada.

**Caso de uso relacionado:** [CU-08](./casos-de-uso.md#cu-08--publicar-contenido)

**Criterios de aceptación:**

- Dado que creo una publicación con título, descripción, categoría y, opcionalmente, archivos adjuntos, entonces el sistema la valida y publica.
- Dado que la publicación no cumple las políticas de uso de la plataforma, entonces el sistema la rechaza e informa el motivo.
- Dado que la publicación es exitosa, entonces aparece en el feed de mis conexiones y de los usuarios interesados en su categoría.

**Prioridad:** Media

---

## HU-09

> **Como** usuario autenticado,
> **quiero** visualizar las publicaciones de mi red y de mis categorías de interés, filtradas por categoría o relevancia,
> **para** mantenerme informado del contenido académico y profesional que me interesa.

**Caso de uso relacionado:** [CU-09](./casos-de-uso.md#cu-09--visualizar-publicaciones)

**Criterios de aceptación:**

- Dado que accedo al feed de publicaciones, entonces veo publicaciones de mis conexiones y de mis categorías de interés, y puedo aplicar filtros por categoría.
- Dado que aplico un filtro sin resultados, entonces el sistema me informa que no hay publicaciones coincidentes.
- Dado que visualizo una publicación, entonces puedo interactuar con ella (comentar, reaccionar, compartir).

**Prioridad:** Media

---

## HU-18

> **Como** administrador,
> **quiero** gestionar las publicaciones realizadas por los usuarios,
> **para** mantener un contenido adecuado dentro de la plataforma.

**Caso de uso relacionado:** [CU-25](./casos-de-uso.md#cu-25--moderar-contenido-publicaciones-y-eventos)

**Criterios de aceptación:**
- Dado que soy administrador, entonces puedo visualizar las publicaciones realizadas por los usuarios, incluidas las reportadas.
- Dado que una publicación incumple las políticas de uso de la plataforma, entonces puedo retirarla.
- Dado que retiro una publicación, entonces esta deja de estar disponible para los demás usuarios y su autor es notificado con el motivo.
- Dado que una publicación es retirada, entonces el sistema registra la acción realizada por el administrador.

**Prioridad:** Alta

---

## HU-19

> **Como** administrador,
> **quiero** gestionar los eventos publicados por los usuarios,
> **para** garantizar que la información disponible sobre los eventos sea apropiada para la comunidad.

**Caso de uso relacionado:** [CU-25](./casos-de-uso.md#cu-25--moderar-contenido-publicaciones-y-eventos)

**Criterios de aceptación:**

- Dado que soy administrador, entonces puedo visualizar los eventos publicados en la plataforma, incluidos los reportados.
- Dado que un evento incumple las políticas de uso de la plataforma, entonces puedo retirarlo.
- Dado que retiro un evento, entonces este deja de estar disponible para los usuarios y su autor es notificado con el motivo.
- Dado que un evento es retirado, entonces el sistema registra la acción realizada por el administrador.

**Prioridad:** Alta
