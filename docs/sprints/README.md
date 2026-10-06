# Sprints — UniLink

El MVP se construye en **9 sprints de 2 semanas**. El orden respeta las dependencias entre módulos: primero el acceso, luego la identidad, la red y, sobre esa base, el contenido y los módulos de valor.

## Roadmap

| Sprint | Objetivo | Specs | Prioridad |
|---|---|---|---|
| [1](./sprint-01/README.md) | Un usuario puede registrarse, verificar su correo, iniciar sesión y recuperar su contraseña | FS-CTA-01, FS-CTA-02, FS-CTA-03, FS-CTA-04 | Alta |
| [2](./sprint-02/README.md) | El usuario construye su perfil profesional y encuentra a otros | FS-CTA-05, FS-PRF-01, FS-PRF-02, FS-PRF-03 | Alta |
| [3](./sprint-03/README.md) | El usuario arma su red desde el primer ingreso | FS-RED-01, FS-RED-02, FS-NOT-01 | Alta |
| [4](./sprint-04/README.md) | El usuario publica y consume contenido en su feed | FS-CNT-01, FS-ADM-01 | Media |
| [5](./sprint-05/README.md) | Los usuarios conversan en privado y el administrador modera la plataforma | FS-MSG-01, FS-ADM-02, FS-ADM-03 | Alta |
| [6](./sprint-06/README.md) | Los responsables publican oportunidades y los usuarios se postulan | FS-OPO-01, FS-OPO-02 | Alta |
| [7](./sprint-07/README.md) | La comunidad publica eventos y confirma asistencia | FS-EVT-01, FS-EVT-02 | Alta |
| [8](./sprint-08/README.md) | Los usuarios colaboran en espacios de proyectos con permisos | FS-PRY-01, FS-PRY-02 | Media |
| 9 | Los usuarios ofrecen y solicitan servicios con credenciales verificadas | FS-SRV-01, FS-SRV-02, FS-SRV-03 | Alta ⚠️ |

⚠️ **Sprint 9 pendiente de decisión:** el módulo de servicios amplía el alcance más allá de una red profesional universitaria. El equipo debe confirmar si entra en el MVP o pasa a una segunda fase.

**Antes del Sprint 1 (Sprint 0, sin specs funcionales):** definir el stack, la arquitectura, el modelo de datos base, los repositorios, la integración continua y el entorno de despliegue.

## Dependencias clave

- **Categorías:** FS-CTA-04 (Sprint 1) necesita categorías, pero su administración llega en FS-ADM-01 (Sprint 4). En el Sprint 1 se cargan categorías iniciales como datos semilla.
- **Notificaciones:** desde el Sprint 1 se envían correos; el centro de notificaciones dentro de la plataforma (FS-NOT-01) llega en el Sprint 3. Los sprints 1 y 2 no generan notificaciones internas.
- **Mensajería:** FS-SRV-02 (Sprint 9) reutiliza el chat de FS-MSG-01 (Sprint 5).

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
- [ ] El código fue revisado por al menos otro integrante (pull request aprobado).
- [ ] Está desplegado en el entorno de pruebas.
- [ ] Se mostró en la revisión del sprint.
- [ ] El estado del spec se actualizó a **Implementado** en [`specs/README.md`](../specs/README.md).

## Crear un sprint nuevo

1. Copia [`_plantilla-sprint.md`](./_plantilla-sprint.md) a `sprint-NN/README.md`.
2. Completa el objetivo y los specs comprometidos desde el roadmap.
3. Actualiza el estado de esos specs a **En desarrollo**.
