# Documentación — UniLink

_MVP — Red Profesional Universitaria — Universidad del Magdalena_
_Centro de Interés de Desarrollo Tecnológico e Innovación (CIDTI)_

## Estructura

```
docs/
├── README.md                  ← este archivo
├── normas-comunidad.md        ← reglas de convivencia que aceptan los usuarios y aplican los administradores
├── requisitos/                ← QUÉ necesita el usuario (fuente de verdad del alcance)
│   ├── CasosDeUso.md          (CU-01 … CU-30)
│   ├── HistoriasDeUsuario.md  (HU-01 … HU-31)
│   └── RequisitosNoFuncionales.md (seguridad, privacidad, rendimiento, accesibilidad…)
├── specs/                     ← CÓMO se comporta el sistema (especificaciones funcionales)
│   ├── README.md              (índice, estados y trazabilidad CU → spec)
│   ├── _plantilla-spec.md
│   └── <modulo>/FS-<MOD>-NN-<nombre>.md
└── sprints/                   ← CUÁNDO se construye cada spec
    ├── README.md              (roadmap, Definition of Ready / Done)
    ├── _plantilla-sprint.md
    └── sprint-NN/README.md
```

## Cómo fluye el trabajo

1. **Requisitos:** los casos de uso y las historias definen el alcance. No se programa nada que no esté trazado a un CU.
2. **Specs:** cada spec detalla uno o varios CU de un mismo módulo: reglas de negocio, datos, validaciones, mensajes y criterios de aceptación.
3. **Sprints:** cada sprint toma specs en estado **Aprobado** y las lleva a **Implementado**.

Los specs se organizan por **módulo** (no por sprint) para que un spec no cambie de carpeta si se replanifica. La asignación a sprints vive en [`sprints/README.md`](./sprints/README.md).

## Enlaces rápidos

- [Casos de uso](./requisitos/CasosDeUso.md)
- [Historias de usuario](./requisitos/HistoriasDeUsuario.md)
- [Requisitos no funcionales](./requisitos/RequisitosNoFuncionales.md)
- [Índice de specs](./specs/README.md)
- [Roadmap de sprints](./sprints/README.md)
- [Normas de la comunidad](./normas-comunidad.md)
