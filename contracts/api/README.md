# API REST

Un archivo OpenAPI 3.0.3 por módulo. Cada operación indica quién puede usarla (`description`), sus casos de uso (`x-casos-de-uso`) y su spec (`x-spec`).

| Archivo | Módulo | Prefijo |
|---|---|---|
| [`usuarios.yaml`](./usuarios.yaml) | Usuarios | `/api/v1/usuarios` |
| [`red.yaml`](./red.yaml) | Red | `/api/v1/red` |
| [`contenido.yaml`](./contenido.yaml) | Contenido | `/api/v1/contenido` |
| [`comunicacion.yaml`](./comunicacion.yaml) | Comunicación | `/api/v1/comunicacion` |
| [`colaboracion.yaml`](./colaboracion.yaml) | Colaboración | `/api/v1/colaboracion` |
| [`plataforma.yaml`](./plataforma.yaml) | Plataforma | `/api/v1/plataforma` |

## Convenciones

| Tema | Convención | Origen |
|---|---|---|
| Rutas | `/api/v1/<modulo>/...`; las de administración bajo `/admin/`. | ADR-003 |
| Sesión | Cookie `HttpOnly`, `Secure` y `SameSite`, invalidable en el servidor; las escrituras llevan además `X-CSRF-Token`. | RNF-SEG-03, RNF-SEG-05 |
| Permisos | Cada operación valida en el servidor el "Quién es quién" de su spec; sin permiso, 403. | RNF-SEG-04 |
| Errores | `{ "error": "<CODIGO>", "message": "<texto>", "correlation_id": "<id>" }`; `message` es el `MSG-NN` del spec. | RNF-USA-03, RNF-OBS-01 |
| Límites de uso | 429 con `Retry-After`. | RNF-SEG-07 |
| Ediciones | `ETag` en la respuesta y `If-Match` al editar; si la versión cambió, 409. | RNF-CON-02 |
| Creaciones reintentables | `Idempotency-Key`. | RNF-CON-03 |
| Paginación | Por cursor en feed, mensajes y notificaciones; por página (20 o 25) en búsquedas y administración. | Specs |
| Fechas | ISO 8601 con zona horaria; se muestran en hora de Colombia. | RNF-USA-01 |
| Idioma | Español de Colombia. | RNF-USA-01 |
| Archivos | Subida validada por contenido; se sirven desde el dominio del almacenamiento de archivos. | RNF-SEG-06 |
