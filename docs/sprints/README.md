# Sprints — UniLink

> **MVP acotado (2026-10-29).** El MVP se redujo a monitorías, semilleros, ayudantías y actividades complementarias. El plan de sprints propuesto para ese alcance está en [Actores y alcance del MVP, sección 6](../actores_y_alcance_mvp.md#6-plan-de-sprints-propuesto). El roadmap de abajo es el del producto completo y se reemplazará cuando el equipo confirme el nuevo plan.

El MVP se construye en **8 sprints de 2 semanas** (unas 16 semanas). El orden respeta las dependencias entre módulos: primero el acceso, luego la identidad, la red y, sobre esa base, el contenido y los módulos de valor.

## Roadmap

| Sprint | Objetivo | Specs | Prioridad |
|---|---|---|---|
| [1](./sprint-01/README.md) | Un usuario puede registrarse, verificar su correo, iniciar sesión y recuperar su contraseña | FS-USR-01, FS-USR-02, FS-USR-03, FS-USR-04 | Alta |
| [2](./sprint-02/README.md) | El usuario construye su perfil profesional y encuentra a otros | FS-USR-05, FS-USR-06, FS-RED-03, FS-USR-07 | Alta |
| [3](./sprint-03/README.md) | El usuario arma su red desde el primer ingreso | FS-RED-01, FS-RED-02, FS-COM-02 | Alta |
| [4](./sprint-04/README.md) | El usuario publica y consume contenido en su feed | FS-CNT-01, FS-PLT-01 | Media |
| [5](./sprint-05/README.md) | Los usuarios conversan en privado y el administrador modera la plataforma | FS-COM-01, FS-USR-08, FS-CNT-02 | Alta |
| [6](./sprint-06/README.md) | Los responsables publican oportunidades y los usuarios se postulan | FS-COL-01, FS-COL-02 | Alta |
| [7](./sprint-07/README.md) | La comunidad publica eventos y confirma asistencia | FS-COL-03, FS-COL-04 | Alta |
| [8](./sprint-08/README.md) | Los usuarios colaboran en espacios de proyectos con permisos | FS-COL-05, FS-COL-06 | Media |

**Antes del Sprint 1 (Sprint 0, sin specs funcionales):** definir el stack, la arquitectura, el modelo de datos base, los repositorios, la integración continua y el entorno de despliegue.

## Fase 2 (fuera del MVP)

El equipo decidió dejar el **módulo de servicios** para una segunda fase: amplía el alcance más allá de una red profesional universitaria, introduce usuarios sin correo institucional y exige verificación manual de documentos. Sus casos de uso e historias se conservan en los requisitos, marcados como _fase 2_; sus specs se escribirán cuando se retome.

| Objetivo | Specs | Casos de uso |
|---|---|---|
| Los usuarios ofrecen y solicitan servicios con credenciales verificadas, y egresados y personal tercerizado se registran como oferentes | FS-SRV-01, FS-SRV-02, FS-SRV-03 | CU-27 a CU-30 |

## Dependencias clave

- **Categorías:** FS-USR-04 (Sprint 1) necesita categorías, pero su administración llega en FS-PLT-01 (Sprint 4). En el Sprint 1 se cargan categorías iniciales como datos semilla.
- **Notificaciones:** desde el Sprint 1 se envían correos; el centro de notificaciones dentro de la plataforma (FS-COM-02) llega en el Sprint 3. Los sprints 1 y 2 no generan notificaciones internas.
- **Mensajería:** FS-COL-01 (Sprint 6) reutiliza el chat de FS-COM-01 (Sprint 5) para las postulaciones aceptadas; en la fase 2, FS-SRV-02 hará lo mismo con las solicitudes de servicio.

## Ceremonias

| Ceremonia | Cuándo | Duración | Resultado |
|---|---|---|---|
| Planificación | Día 1 | 2 h | Compromiso del sprint en `sprint-NN/README.md` |
| Daily | Cada día | 15 min | Bloqueos identificados |
| Refinamiento | Semana 2 | 1 h | Specs del siguiente sprint en estado **Aprobado** |
| Revisión | Último día | 1 h | Demo de lo implementado |
| Retrospectiva | Último día | 45 min | Acciones de mejora en `sprint-NN/README.md` |

## Definition of Ready (un spec puede entrar a un sprint)

- [ ] Está trazado a sus CU y HU.
- [ ] Tiene reglas de negocio, datos y validaciones completas.
- [ ] Todos los criterios de aceptación son verificables.
- [ ] No tiene preguntas abiertas que bloqueen el desarrollo.
- [ ] Sus dependencias están implementadas o planificadas en el mismo sprint.
- [ ] El equipo lo revisó y lo marcó como **Aprobado**.

## Definition of Done (un spec está terminado)

- [ ] Cumple todos los criterios de aceptación del spec.
- [ ] Tiene pruebas automatizadas de sus reglas de negocio.
- [ ] Cumple los [requisitos no funcionales](../srs/Especificacion_Requisitos.md#3313-cuándo-se-aplica-cada-requisito) que aplican a todos los sprints: control de acceso en el servidor, seguridad, rendimiento, usabilidad y accesibilidad.
- [ ] El código fue revisado por al menos otro integrante (pull request aprobado).
- [ ] Está desplegado en el entorno de pruebas.
- [ ] Se mostró en la revisión del sprint.
- [ ] El estado del spec se actualizó a **Implementado** en [`specs/README.md`](../modulos/README.md).

## Crear un sprint nuevo

1. Copia [`_plantilla-sprint.md`](./_plantilla-sprint.md) a `sprint-NN/README.md`.
2. Completa el objetivo y los specs comprometidos desde el roadmap.
3. Actualiza el estado de esos specs a **En desarrollo**.
