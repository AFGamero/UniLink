# Interfaz pública — Colaboración

Operaciones que otros módulos pueden pedirle a Colaboración dentro de la aplicación (llamada en proceso, ADR-004). Ningún módulo accede a sus tablas ni a su código interno (ADR-003). Los nombres son orientativos: el lenguaje y las firmas concretas se fijan con ADR-010.

| Operación | Devuelve | Errores o restricciones | La usa | Spec |
|---|---|---|---|---|
| `tienenPostulacionAceptada(a, b)` | true o false | — | Comunicación | COL-01 |
| `aCargoDe(usuario_id)` | Oportunidades abiertas, eventos programados y proyectos que administra | — | Pantalla de eliminación de cuenta (FS-USR-05 RN-12) | COL-01, COL-03, COL-05 |
| `Reportable: oportunidad, evento, proyecto` | Resumen, ocultar, restaurar y retirar | — | Contenido | CNT-02 |

API REST del módulo: [`../api/colaboracion.yaml`](../api/colaboracion.yaml). Eventos: [catálogo](../eventos/README.md).
