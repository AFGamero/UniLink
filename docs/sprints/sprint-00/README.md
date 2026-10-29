# Sprint 0 — Bases técnicas y seguridad

| Campo | Valor |
|---|---|
| **Fechas** | Por definir (2 semanas antes del Sprint 1) |
| **Estado** | Planificado |
| **Objetivo** | El equipo tiene el stack, la arquitectura, la seguridad base y los entornos listos para que el Sprint 1 solo construya funcionalidad. |

## Specs comprometidos

El Sprint 0 no tiene specs funcionales. Sus entregables son documentos técnicos y la base del proyecto:

| Entregable | Documento | Estado |
|---|---|---|
| Seguridad de la API y control de acceso por endpoint | [seguridad-endpoints.md](../../arquitectura/seguridad-endpoints.md) | Borrador |
| Stack y arquitectura | [ADR-010](../../arquitectura/Registro_Decisiones.md#adr-010-lenguaje-y-framework) (FastAPI y React) y [ADR-017](../../arquitectura/Registro_Decisiones.md#adr-017-arquitectura-interna-de-los-módulos-hexagonal-con-clean-architecture) (hexagonal con Clean Architecture); estructura en el [plan de implementación](../../arquitectura/Plan_de_Implementacion.md#1-estructura-interna-de-un-módulo) | Aceptado |
| Modelo de datos base | Por crear | Pendiente |

## Decisiones necesarias antes de empezar

Vienen del [consolidado de preguntas abiertas](../../preguntas-abiertas.md):

- [P-01](../../preguntas-abiertas.md#a-institucionales): validar los supuestos de uso.
- [P-02](../../preguntas-abiertas.md#a-institucionales): infraestructura de la universidad o nube.
- [P-16, P-17 y P-18](../../preguntas-abiertas.md#c-técnicas): tiempo real, motor de búsqueda y disponibilidad.

## Tareas técnicas

**Seguridad e inicio de sesión:**

- [ ] Aprobar el catálogo de endpoints y sus niveles de acceso ([seguridad-endpoints.md](../../arquitectura/seguridad-endpoints.md)).
- [ ] Implementar el middleware de acceso con **bloqueo por defecto**: toda ruta exige sesión salvo la lista de endpoints públicos.
- [ ] Implementar las sesiones en el servidor con cookie `HttpOnly`, `Secure` y `SameSite`, y el token anti-CSRF.
- [ ] Configurar el límite de peticiones por IP y por usuario.
- [ ] Crear la prueba de lista blanca, que falla si una ruta nueva responde sin sesión.
- [ ] Bloquear en producción la documentación interactiva de la API, las métricas y las consolas de base de datos.
- [ ] Activar el escaneo de secretos y de dependencias en la integración continua (RNF-SEG-08 y RNF-SEG-09).

**Base del proyecto:**

- [x] Elegir el stack y documentar la decisión (ADR-010 y ADR-017, 2026-10-27).
- [ ] Definir el modelo de datos base: usuario, perfil, etiqueta, categoría y sesión.
- [ ] Crear los repositorios, la estructura del proyecto y la integración continua.
- [ ] Preparar los entornos de desarrollo, pruebas y producción.
- [ ] Cargar los datos semilla: programas académicos y categorías iniciales.

## Riesgos

| Riesgo | Mitigación |
|---|---|
| La decisión de infraestructura (P-02) depende de TI de la universidad y puede tardar. | Empezar con el entorno de desarrollo local y en contenedores, que sirve para cualquiera de las dos opciones. |
| Dejar la seguridad para "después" obliga a reescribir todos los endpoints. | El middleware de bloqueo por defecto y la prueba de lista blanca deben estar listos antes del primer endpoint del Sprint 1. |

## Revisión

_Completar al cierre:_ qué se mostró y qué quedó pendiente.

## Retrospectiva

| Qué funcionó | Qué mejorar | Acción |
|---|---|---|
| … | … | … |
