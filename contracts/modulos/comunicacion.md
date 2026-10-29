# Interfaz pública — Comunicación

Operaciones que otros módulos pueden pedirle a Comunicación dentro de la aplicación (llamada en proceso, ADR-004). Ningún módulo accede a sus tablas ni a su código interno (ADR-003). Los nombres son orientativos: el lenguaje y las firmas concretas se fijan con ADR-010.

| Operación | Devuelve | Errores o restricciones | La usa | Spec |
|---|---|---|---|---|
| `puedenConversar(a, b)` | true si son conexiones o tienen una postulación aceptada entre ellos | — | Pantallas de perfil y de postulaciones | COM-01 |

Comunicación no expone operaciones para notificar: crea las notificaciones consumiendo [eventos](../eventos/README.md) (ADR-004).

API REST del módulo: [`../api/comunicacion.yaml`](../api/comunicacion.yaml). Eventos: [catálogo](../eventos/README.md).
