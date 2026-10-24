# FS-XXX-NN — Nombre del spec

| Campo | Valor |
|---|---|
| **Módulo** | Nombre del módulo (código) |
| **Estado** | Borrador · En revisión · Aprobado · En desarrollo · Implementado |
| **Responsable** | Nombre |
| **Casos de uso** | CU-XX |
| **Historias** | HU-XX |
| **Última actualización** | AAAA-MM-DD |

El sprint de cada spec está en el [roadmap](../sprints/README.md), no aquí.

## 1. Objetivo

Qué problema resuelve, para quién y qué valor entrega, en dos o tres frases.

## 2. Quién es quién

Usa los nombres de actor del [SRS §2.4](../srs/Especificacion_Requisitos.md#24-actores-del-sistema).

| Actor | Qué hace | Qué ve | Qué no puede hacer |
|---|---|---|---|
| … | … | … | … |

## 3. Alcance

**Incluye:**

- …

**No incluye:** (y dónde se resuelve)

- …

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | … |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El sistema debe … | Alta |

## 6. Datos y validaciones

| Campo | Tipo | Obligatorio | Validación |
|---|---|---|---|
| … | … | Sí / No | … |

**Finalidad de los datos personales** (RNF-PRI-01): para qué se usa cada dato personal nuevo.

## 7. Estados

Diagrama Mermaid (`stateDiagram-v2`) y tabla de transiciones con quién la provoca. "No aplica" si la entidad no tiene ciclo de vida.

| Estado | Entra cuando | Sale hacia |
|---|---|---|
| … | … | **…** |

## 8. Flujo principal

1. Pantalla → acción → resultado.

## 9. Variaciones

Caminos alternativos legítimos: otro tipo de usuario, otra modalidad, otro estado de partida.

| Variación | Qué cambia | Regla |
|---|---|---|
| … | … | RN-NN |

## 10. ¿Qué pasaría si…?

Revisa siempre estas siete situaciones: concurrencia; cambio de estado de la cuenta de cada actor; eliminación o retiro de lo que esto usa; pérdida de permiso a mitad del uso; falla del correo, del almacenamiento o del tiempo real; límites de uso; privacidad.

| Situación | Comportamiento esperado | Regla o pregunta |
|---|---|---|
| … | … | RN-NN / P-NN |

## 11. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | … | "…" |

## 12. Resultado esperado

Escenarios que cubren el flujo principal, cada variación y cada fila de la sección 10.

```gherkin
Escenario: …
  Dado …
  Cuando …
  Entonces …
```

## 13. Contratos

**Expone:** rutas de la API, operaciones de la interfaz pública y eventos que publica.

**Consume:** lo que usa de otros módulos y para qué.

## 14. Calidad

RNF y escenarios de calidad (EC) que aplican, además de los transversales.

## 15. Preguntas abiertas

Solo referencias a [preguntas-abiertas.md](../preguntas-abiertas.md): `P-NN`.

## 16. Lista de revisión

- [ ] Cada actor de "Quién es quién" existe en el SRS §2.4 con el mismo nombre.
- [ ] Toda acción tiene un actor que puede hacerla y se valida en el servidor (RNF-SEG-04).
- [ ] Cada regla tiene al menos un escenario en "Resultado esperado".
- [ ] "¿Qué pasaría si…?" revisó las siete situaciones.
- [ ] Ningún dato se recoge sin finalidad (RNF-PRI-01).
- [ ] No contradice a su caso de uso, a su historia ni a otro spec.
- [ ] Sus contratos existen en `contracts/`.
- [ ] No tiene preguntas abiertas que bloqueen el desarrollo.

## 17. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| AAAA-MM-DD | … | Creación |
