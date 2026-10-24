# Contratos — UniLink

Esta carpeta es el **único punto de acoplamiento** entre los módulos del monolito modular. Un módulo solo usa a otro por lo que aquí se define: su API REST, su interfaz pública o sus eventos.

| Carpeta | Contenido |
|---|---|
| [`api/`](./api/README.md) | API REST de cada módulo (OpenAPI 3.0.3), la que consume la aplicación web. |
| [`modulos/`](./modulos/) | Interfaz pública de cada módulo: lo que otro módulo puede pedirle dentro de la aplicación. |
| [`eventos/`](./eventos/README.md) | Eventos de dominio: sobre común, esquema de cada evento (JSON Schema 2020-12) y catálogo con productor y consumidores. |

## Reglas

1. **Un módulo nunca lee ni escribe las tablas de otro.** Solo usa su interfaz pública o reacciona a sus eventos, y las dependencias entre módulos no forman ciclos ([ADR-003](../docs/arquitectura/Registro_Decisiones.md#adr-003-límites-de-los-módulos-y-dependencias-permitidas)).
2. **El contrato se cambia antes que el código**, en un pull request propio revisado por el módulo que lo expone y por los que lo usan ([ADR-006](../docs/arquitectura/Registro_Decisiones.md#adr-006-contratos-antes-que-el-código)).
3. **Los contratos se versionan.** Quitar o renombrar un campo crea una versión nueva; agregar un campo opcional no.
4. **Los eventos se publican después de confirmar la transacción** que los origina y los consumidores descartan los repetidos por su `evento_id` (RNF-CON-04).
5. **Los archivos son válidos para las herramientas:** OpenAPI 3.0.3 y JSON Schema 2020-12. `python scripts/verificar_docs.py --fase completa` los valida.
6. **Cada módulo se prueba contra su contrato:** sus respuestas REST con su OpenAPI y sus eventos con su esquema; la integración continua compara el OpenAPI generado desde el código con el acordado (RNF-MAN-05).

## Estado

Esqueleto acordado antes de programar: todas las rutas, operaciones y eventos que salen de los specs, con quién puede usarlos y su spec de origen. Los esquemas detallados de cada API se completan cuando su spec pasa a **Aprobado**.
