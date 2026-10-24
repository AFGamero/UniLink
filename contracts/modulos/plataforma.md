# Interfaz pública — Plataforma

Operaciones que otros módulos pueden pedirle a Plataforma dentro de la aplicación (llamada en proceso, ADR-004). Ningún módulo accede a sus tablas ni a su código interno (ADR-003). Los nombres son orientativos: el lenguaje y las firmas concretas se fijan con ADR-010.

| Operación | Devuelve | Errores o restricciones | La usa | Spec |
|---|---|---|---|---|
| `categoriasActivas(tipo)` | Categorías activas en su orden | — | Usuarios, Contenido, Colaboración | PLT-01 |
| `revisarTexto(texto)` | Lista de palabras prohibidas encontradas (vacía si no hay) | — | Usuarios, Contenido, Colaboración | PLT-01, CNT-02 |

Plataforma no usa a ningún otro módulo; recibe la auditoría por el evento `auditoria.registrada`.

API REST del módulo: [`../api/plataforma.yaml`](../api/plataforma.yaml). Eventos: [catálogo](../eventos/README.md).
