# Interfaz pública — Red

Operaciones que otros módulos pueden pedirle a Red dentro de la aplicación (llamada en proceso, ADR-004). Ningún módulo accede a sus tablas ni a su código interno (ADR-003). Los nombres son orientativos: el lenguaje y las firmas concretas se fijan con ADR-010.

| Operación | Devuelve | Errores o restricciones | La usa | Spec |
|---|---|---|---|---|
| `sonConexiones(a, b)` | true o false | — | Comunicación, Contenido, Colaboración | RED-01 |
| `queVeObservador(dueno_id, observador_id)` | COMPLETO o BASICO (nombre, foto y unidad académica) o NINGUNO (cuenta no activa) | — | Contenido, Colaboración | RED-03 |
| `perfilesComplementarios(usuario_id, limite)` | Usuarios con su puntaje y motivo | — | Colaboración (sugerencias de proyectos) | RED-02 |
| `numeroDeConexiones(usuario_id)` | Entero | — | Pantallas de administración y perfil | RED-01 |

API REST del módulo: [`../api/red.yaml`](../api/red.yaml). Eventos: [catálogo](../eventos/README.md).
