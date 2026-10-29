# Documentación — UniLink

_MVP — Red Profesional Universitaria — Universidad del Magdalena_
_Centro de Interés de Desarrollo Tecnológico e Innovación (CIDTI)_

## Documentos

| # | Documento | Contenido |
|---|---|---|
| 1 | [Especificación de requisitos (SRS)](./srs/Especificacion_Requisitos.md) | Alcance, stakeholders, actores y matriz de permisos ("quién es quién"), restricciones, requisitos funcionales y no funcionales, escenarios de calidad, verificación, trazabilidad, riesgos y responsabilidades. |
| 2 | [Comparación de alternativas](./arquitectura/Comparacion_Alternativas.md) | Monolito en capas, monolito modular y microservicios: tabla ponderada, decisión y trade-offs. |
| 3 | [Registro de decisiones (ADR)](./arquitectura/Registro_Decisiones.md) | Estilo, módulos y dependencias, comunicación, persistencia, contratos, tiempo real, búsqueda, alojamiento, stack, tareas, archivos, autenticación institucional, API de admisiones, borrado lógico y cliente Android. |
| 4 | [Vistas de arquitectura](./arquitectura/Vistas_Arquitectura.md) | Vista de módulos, vista de componentes y conectores (C&C) y vista de despliegue. |
| 5 | [Módulos](./modulos/README.md) | Por cada módulo: README, casos de uso, historias de usuario y specs con el estudio de cada funcionalidad. |
| 6 | [Contratos](../contracts/README.md) | API REST, interfaces públicas de los módulos y eventos de dominio. |
| 7 | [Plan de implementación](./arquitectura/Plan_de_Implementacion.md) | Estructura interna de un módulo, fronteras, flujos clave, tareas programadas y pruebas. |
| 8 | [Sprints](./sprints/README.md) | Roadmap, ceremonias, _Definition of Ready_ y _Definition of Done_. |

Además: [preguntas abiertas](./preguntas-abiertas.md) (única fuente de las decisiones pendientes), [normas de la comunidad](./normas-comunidad.md), [seguridad de la API](./arquitectura/seguridad-endpoints.md) y [decisiones del equipo](./decisiones/) (incluida la [reunión del 2026-10-19](./decisiones/2026-10-19-reunion-preguntas-abiertas.md)).

**Para el profesor tutor (2026-10-29):**

| Documento | Contenido |
|---|---|
| [**Informe del proyecto**](./informe_unilink.md) | Punto de entrada: resumen de cada tema en una página, con enlaces al detalle. |
| [**Actores y alcance del MVP**](./actores_y_alcance_mvp.md) | Los seis actores, qué hace cada uno, qué entra al MVP y cuándo está terminado. |

**Análisis integral (2026-10-27)**, anexo técnico del informe:

| Documento | Contenido |
|---|---|
| [Informe integral detallado](./informe_integral_unilink.md) | Especificación, requisitos y arquitectura en 19 capítulos, con diagramas, diccionario de datos e inventario de endpoints. |
| [Arquitectura actual y objetivo](./arquitectura_unilink.md) | Consolidación de la arquitectura con las decisiones del 2026-10-19. |
| [Catálogo de requisitos](./requisitos_unilink.md) | Índice de los 167 RF y los 63 RNF, propuestas y decisiones sin especificar. |
| [Matriz de trazabilidad](./matriz_trazabilidad_unilink.md) | Requisito → componente → datos → endpoint → prueba → estado. |
| [Riesgos y brechas](./riesgos_y_brechas_unilink.md) | 37 hallazgos y los cambios pendientes por spec. |

## Orden de lectura

1. **SRS, secciones 1 y 2:** qué problema resuelve UniLink, para quién y con qué restricciones.
2. **Comparación de alternativas:** por qué un monolito modular.
3. **Registro de decisiones:** cómo se materializa.
4. **Vistas de arquitectura:** qué módulos hay, cómo se comunican y dónde se ejecutan.
5. **Módulos:** el estudio de cada funcionalidad.
6. **Contratos:** lo que cada módulo expone y consume.
7. **Plan de implementación y sprints:** cómo y cuándo se construye.

## Estructura

```
docs/
├── README.md
├── srs/Especificacion_Requisitos.md
├── arquitectura/        ← comparación, ADR, vistas y plan de implementación
├── modulos/
│   ├── README.md        ← mapa de módulos, índice de specs y equivalencias
│   ├── _plantilla-spec.md
│   └── <modulo>/        ← README, casos-de-uso.md, historias.md, specs/
├── sprints/
├── decisiones/
├── preguntas-abiertas.md
└── normas-comunidad.md
contracts/               ← en la raíz del repositorio
```

## Cómo fluye el trabajo

1. **Requisitos:** los casos de uso y las historias definen el alcance. No se programa nada que no esté trazado a un CU.
2. **Specs:** cada spec estudia una funcionalidad: quién es quién, reglas, variaciones, qué pasaría en cada situación límite y el resultado esperado.
3. **Contratos:** antes de programar, el módulo acuerda en `contracts/` lo que expone y consume.
4. **Sprints:** cada sprint toma specs en estado **Aprobado** y los lleva a **Implementado**.

Para revisar enlaces, códigos y cobertura: `python scripts/verificar_docs.py --fase completa`.
