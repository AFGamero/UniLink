# Interfaz pública — Contenido

Operaciones que otros módulos pueden pedirle a Contenido dentro de la aplicación (llamada en proceso, ADR-004). Ningún módulo accede a sus tablas ni a su código interno (ADR-003). Los nombres son orientativos: el lenguaje y las firmas concretas se fijan con ADR-010.

| Operación | Devuelve | Errores o restricciones | La usa | Spec |
|---|---|---|---|---|
| `reportar(tipo, elemento_id, motivo, descripcion)` | Reporte creado | Elemento propio, repetido o inexistente | Pantallas de todos los módulos con contenido público | CNT-02 |
| `estadoDeModeracion(tipo, elemento_id)` | VISIBLE, OCULTO o RETIRADO | — | Usuarios, Colaboración | CNT-02 |
| `publicacionParaCompartir(publicacion_id, observador_id)` | Vista previa (autor, título, enlace) si el observador puede verla | Sin permiso o retirada | Comunicación | CNT-01, COM-01 |

**Contrato `Reportable`** (en el paquete de contratos). Lo implementa cada módulo dueño para sus tipos: `resumen(elemento_id)` → texto, autor y enlace; `ocultar(elemento_id)`; `restaurar(elemento_id)`; `retirar(elemento_id, norma, comentario)`. La moderación (FS-CNT-02) solo conoce este contrato (EC-06).

API REST del módulo: [`../api/contenido.yaml`](../api/contenido.yaml). Eventos: [catálogo](../eventos/README.md).
