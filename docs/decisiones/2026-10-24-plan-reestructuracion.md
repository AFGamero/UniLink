# Plan de reestructuración de la documentación

> **Para quien ejecute:** seguir las tareas en orden; cada una termina en un commit que hace el equipo (se sugiere el mensaje y se espera). Pasos con casillas (`- [ ]`).

**Objetivo:** llevar `docs/` a la estructura SRS + arquitectura + módulos, estudiar cada funcionalidad y crear `contracts/`, según el diseño aprobado.

**Enfoque:** primero una herramienta de verificación que falla contra la estructura actual; después se reorganiza sin cambiar contenido; luego se escriben SRS y arquitectura; después se estudia módulo por módulo; al final, contratos y verificación completa.

**Herramientas:** Markdown con Mermaid, OpenAPI 3.0.3, JSON Schema 2020-12, Python 3 (solo para el verificador), git.

**Diseño:** [`2026-10-24-reestructuracion-docs.md`](./2026-10-24-reestructuracion-docs.md). Quien ejecute lee ambos.

## Restricciones globales

- Todo en español. No se menciona ningún otro proyecto.
- Arquitectura: monolito modular. Módulos y códigos: USR, RED, CNT, COM, COL, PLT y SRV (fase 2).
- CU-01…30 y HU-01…31 conservan su número; cada uno vive en un solo módulo.
- Los archivos existentes se mueven con `git mv` para conservar su historial.
- Códigos antiguos permitidos solo en la tabla de equivalencias de `docs/modulos/README.md` y en `docs/decisiones/`.
- Diagramas en bloques ```` ```mermaid ````.
- Contratos válidos: OpenAPI 3.0.3 y JSON Schema 2020-12.
- Los commits los hace el equipo.

## Equivalencias (se aplican de una sola vez, nunca en cadena)

| Antes | Ahora | Antes | Ahora |
|---|---|---|---|
| FS-CTA-01 | FS-USR-01 | FS-CNT-01 | FS-CNT-01 |
| FS-CTA-02 | FS-USR-02 | FS-ADM-03 | FS-CNT-02 |
| FS-CTA-03 | FS-USR-03 | FS-MSG-01 | FS-COM-01 |
| FS-CTA-04 | FS-USR-04 | FS-NOT-01 | FS-COM-02 |
| FS-CTA-05 | FS-USR-05 | FS-OPO-01 | FS-COL-01 |
| FS-PRF-01 | FS-USR-06 | FS-OPO-02 | FS-COL-02 |
| FS-PRF-03 | FS-USR-07 | FS-EVT-01 | FS-COL-03 |
| FS-ADM-02 | FS-USR-08 | FS-EVT-02 | FS-COL-04 |
| FS-RED-01 | FS-RED-01 | FS-PRY-01 | FS-COL-05 |
| FS-RED-02 | FS-RED-02 | FS-PRY-02 | FS-COL-06 |
| FS-PRF-02 | FS-RED-03 | FS-ADM-01 | FS-PLT-01 |

## Foco de revisión

1. **Anclas de GitHub con tildes y rayas** (`#cu-01--registrar-cuenta`, `#cu-17--recuperar-contraseña`): al mover los CU a otro archivo, el enlace debe cambiar de archivo pero conservar el ancla. El verificador calcula las anclas como GitHub.
2. **Profundidad de rutas relativas**: los specs pasan de `docs/specs/<m>/` a `docs/modulos/<m>/specs/`; cada `../` cambia.
3. **Reemplazo en cadena**: FS-PRF-02 → FS-RED-03 no debe volver a transformarse; se aplica un único mapa simultáneo.
4. **Referencias cortas sin prefijo FS-** (por ejemplo "FS-CTA-04, RN-03" o "(FS-NOT-01)" y "FS-SRV-03"): también se reemplazan; FS-SRV-* no cambia.
5. **Enlaces desde `preguntas-abiertas.md`, `normas-comunidad.md` y `sprints/`** a rutas de specs que ya no existen.

---

### Tarea 1: Verificador de la documentación

**Archivos:**
- Crear: `scripts/verificar_docs.py`

**Interfaces:**
- Produce: `python scripts/verificar_docs.py [--fase reorganizacion|completa]`. Imprime una línea por problema y termina con código 1 si encontró alguno, o 0 y `OK` si no.

- [ ] **Paso 1: escribir el verificador** con estas comprobaciones:
  - `enlaces`: todo enlace Markdown relativo `[x](ruta#ancla)` en `docs/` y `contracts/` apunta a un archivo existente, y el ancla existe. Ancla al estilo GitHub: minúsculas; se quita todo lo que no sea letra (incluidas las acentuadas), dígito, espacio, `-` o `_`; cada espacio pasa a `-`; las repetidas reciben `-1`, `-2`. También cuentan los `<a id="...">` y los encabezados `## HU-01`.
  - `codigos`: ninguna aparición de `FS-(CTA|PRF|ADM|NOT|MSG|OPO|EVT|PRY)-\d\d` fuera de `docs/modulos/README.md` y `docs/decisiones/`.
  - `cobertura`: en `docs/modulos/*/casos-de-uso.md` cada `## CU-NN` de 01 a 30 aparece exactamente una vez; en `historias.md`, cada `## HU-NN` de 01 a 31.
  - Con `--fase completa`, además: `actores` (cada actor de la sección "Quién es quién" de un spec está en la tabla de actores del SRS §2.4); `contratos` (los `.json` de `contracts/eventos/` validan contra 2020-12 y los `.yaml` de `contracts/api/` contra OpenAPI 3.0.3, con `jsonschema` y `openapi-spec-validator` si están instalados; si no, se avisa).
- [ ] **Paso 2: ejecutarlo contra la estructura actual.**
  Ejecutar: `python scripts/verificar_docs.py`
  Esperado: FALLA (`cobertura`: no existe `docs/modulos/`; `codigos`: decenas de códigos antiguos).
- [ ] **Paso 3: comprobar el ancla con un caso real.** Un enlace temporal a `#cu-17--recuperar-contraseña` en `CasosDeUso.md` no da error, y uno a `#cu-17-recuperar` sí.
- [ ] **Paso 4: commit sugerido** `chore(docs): agregar verificador de enlaces, códigos y cobertura`.

### Tarea 2: Reorganizar (paso 1 del diseño)

**Archivos:**
- Mover con `git mv`: los 22 specs a `docs/modulos/<modulo>/specs/` con su nombre nuevo (`FS-USR-06-perfil-profesional.md`, …); `docs/specs/_plantilla-spec.md` → `docs/modulos/_plantilla-spec.md`.
- Crear: `docs/modulos/README.md` (mapa de módulos y equivalencias), `docs/modulos/<modulo>/casos-de-uso.md`, `docs/modulos/<modulo>/historias.md` (7 módulos, servicios incluido) y `docs/modulos/<modulo>/README.md` mínimo (propósito y lista de specs; se completa en las tareas 5 a 10).
- Eliminar: `docs/requisitos/CasosDeUso.md`, `docs/requisitos/HistoriasDeUsuario.md` y `docs/specs/README.md`, una vez repartido su contenido.
- Modificar: enlaces en `docs/README.md`, `preguntas-abiertas.md`, `normas-comunidad.md`, `requisitos/RequisitosNoFuncionales.md` y `sprints/**`.

**Interfaces:**
- Consume: el verificador de la tarea 1.
- Produce: la ruta definitiva de cada spec, CU y HU, que usan todas las tareas siguientes.

- [ ] **Paso 1:** repartir cada `## CU-NN` y cada `## HU-NN` en el archivo de su módulo según la tabla 5.5 del diseño, **sin cambiar el texto**. Cada archivo lleva el encabezado del documento original y una introducción de una línea; la tabla de actores de CU se queda en `docs/modulos/README.md` hasta que exista el SRS.
- [ ] **Paso 2:** `git mv` de los specs y aplicar el mapa de equivalencias (único y simultáneo) en todo `docs/`, salvo `decisiones/`. En la cabecera de cada spec, el campo "Módulo" pasa al módulo nuevo.
- [ ] **Paso 3:** reescribir las rutas relativas de todos los enlaces que apuntan a specs, CU o HU.
- [ ] **Paso 4:** en `docs/modulos/README.md`, el índice que tenía `specs/README.md` (spec, nombre, CU, HU, estado; sin columna de sprint) y la tabla de equivalencias.
- [ ] **Paso 5: verificar.**
  Ejecutar: `python scripts/verificar_docs.py`
  Esperado: `OK`.
- [ ] **Paso 6:** comprobar con `git diff --stat -M` que los specs aparecen como renombrados (similitud ≥ 90 %), no como borrados y nuevos.
- [ ] **Paso 7: commit sugerido** `docs: reorganizar la documentación en 6 módulos`.

### Tarea 3: SRS (paso 2 del diseño)

**Archivos:**
- Crear: `docs/srs/Especificacion_Requisitos.md`
- Mover el contenido de `docs/requisitos/RequisitosNoFuncionales.md` al SRS §3.3 y eliminar `docs/requisitos/`.

- [ ] **Paso 1:** escribir las secciones de la tabla 4 del diseño. §2.4 lleva la tabla de actores con los nombres únicos del diseño. Los actores de fase 2 se marcan como tales.
- [ ] **Paso 2:** §2.5, la matriz de permisos global (actor × acción por módulo), sacada de las reglas actuales de los specs. Las celdas que los specs no deciden van como `?` y su pregunta P-xx.
- [ ] **Paso 3:** §3.3 con los RNF actuales sin cambios más R-1 a R-5 (sección 8.3 del diseño): sección Consistencia, RNF-MAN-07, RNF-MAN-05 reescrito, tabla de retención y entregabilidad de correo.
- [ ] **Paso 4:** §3.4 con EC-01 a EC-07 en formato fuente · estímulo · entorno · artefacto · respuesta · medida, cada uno con los RNF que concreta.
- [ ] **Paso 5:** apéndices A (matriz CU → HU → spec → RNF/EC → contrato; la columna de contratos queda vacía hasta la tarea 11), B (riesgos, con los del sprint 1 y los de I-06, I-08, I-15 e I-18) y C (responsabilidades por módulo, "Por asignar").
- [ ] **Paso 6:** actualizar los enlaces a `RequisitosNoFuncionales.md` (DoD en `sprints/README.md`, specs).
  Ejecutar: `python scripts/verificar_docs.py` → `OK`.
- [ ] **Paso 7: commit sugerido** `docs(srs): especificación de requisitos con actores, permisos y escenarios de calidad`.

### Tarea 4: Arquitectura (paso 3 del diseño)

**Archivos:**
- Crear: `docs/arquitectura/Comparacion_Alternativas.md`, `Registro_Decisiones.md`, `Vistas_Arquitectura.md` y `Plan_de_Implementacion.md`.

- [ ] **Paso 1:** comparación de tres alternativas (sección 6.1 del diseño), con tabla ponderada (pesos que suman 100 %), decisión justificada y trade-offs.
- [ ] **Paso 2:** ADR-001 a ADR-012 con estado, contexto, alternativas, decisión y consecuencias. Las "Propuesta" listan sus opciones y la P-xx que las bloquea, sin elegir.
- [ ] **Paso 3:** tres vistas con Mermaid: módulos (con la regla Red → Usuarios y sin ciclos), C&C (cada conector: quién inicia, síncrono o asíncrono, qué pasa si falla) y despliegue (desarrollo, pruebas y producción; lo que depende de ADR-009 queda marcado).
- [ ] **Paso 4:** esqueleto del plan de implementación (sección 6.5 del diseño).
- [ ] **Paso 5:** `docs/README.md` con el índice y el orden de lectura de la sección 3 del diseño.
  Ejecutar: `python scripts/verificar_docs.py` → `OK`.
- [ ] **Paso 6: commit sugerido** `docs(arquitectura): comparación de alternativas, ADR y vistas del monolito modular`.

### Tareas 5 a 10: Estudio por módulo (pasos 4a–4f del diseño)

Una tarea por módulo, en este orden. Se revisa cada una antes de pasar a la siguiente.

| Tarea | Módulo | Specs | Correcciones (diseño 8.1 y 8.2) |
|---|---|---|---|
| 5 | Usuarios | USR-01…08 | I-01, I-04, I-05, I-06, I-07, I-08, I-12, I-20, I-22 (HU-02, HU-04); máquina de estados de la cuenta |
| 6 | Red | RED-01…03 | I-01, I-03, I-06 (búsqueda y puntaje), P-50 |
| 7 | Comunicación | COM-01…02 | I-09 (COM-01), I-19, I-21 |
| 8 | Contenido | CNT-01…02 | I-14, I-15 |
| 9 | Plataforma | PLT-01 | I-13, panel de administración y registro de auditoría |
| 10 | Colaboración | COL-01…06 | I-09 (COL-01, COL-02), I-11, I-15, I-16, I-18, I-22 (CU-14) |

**Archivos de cada tarea:** `docs/modulos/<modulo>/README.md`, sus `casos-de-uso.md`, `historias.md` y `specs/*.md`, y las preguntas nuevas en `docs/preguntas-abiertas.md`.

- [ ] **Paso 1:** README del módulo con las secciones de la tabla 5.1 del diseño, incluidos sus diagramas de estados.
- [ ] **Paso 2:** cada spec con la plantilla 5.2. La sección 10 revisa las siete situaciones de la lista: concurrencia; cambio de estado de la cuenta de cada actor; eliminación o retiro de lo que usa; pérdida de permiso a mitad del uso; falla del correo, del almacenamiento o del tiempo real; límites de uso; privacidad. Cada fila tiene un escenario en la sección 12.
- [ ] **Paso 3:** aplicar las correcciones de la tabla al CU, la HU y el spec. Las HU quedan en "Como / quiero / para", prioridad y enlace a los escenarios del spec.
- [ ] **Paso 4:** la sección 12 de cada spec solo cita `P-xx`. Las situaciones que no se pueden decidir se agregan a `preguntas-abiertas.md` (desde P-52) con tres alternativas y una propuesta.
- [ ] **Paso 5:** marcar la lista de revisión 5.3 de cada spec. El estado sigue en Borrador.
  Ejecutar: `python scripts/verificar_docs.py` → `OK`.
- [ ] **Paso 6: commit sugerido** `docs(<modulo>): estudio de variaciones, permisos y casos límite`.

La tarea 5 también actualiza `docs/modulos/_plantilla-spec.md` a la plantilla 5.2, antes de aplicarla.

### Tarea 11: Contratos (paso 5 del diseño)

**Archivos:**
- Crear: `contracts/README.md`, `contracts/api/README.md`, `contracts/api/{usuarios,red,contenido,comunicacion,colaboracion,plataforma}.yaml`, `contracts/modulos/<modulo>.md` (6), `contracts/eventos/README.md`, `contracts/eventos/sobre.v1.json` y un `contracts/eventos/<evento>.v1.json` por evento de la sección 7 del diseño.

**Interfaces:**
- Consume: la sección 13 ("Contratos") de cada spec de las tareas 5 a 10.
- Produce: la columna de contratos de la matriz del SRS.

- [ ] **Paso 1:** reglas y convenciones de la API (sección 7 del diseño).
- [ ] **Paso 2:** sobre del evento, con los campos `evento_id` (uuid), `tipo` (patrón `^[a-z_]+\.[a-z_]+$`), `version` (entero ≥ 1), `ocurrido_en` (date-time), `modulo` (uno de los seis), `actor_id` (uuid o null) y `datos` (objeto). Después, un esquema por evento con `additionalProperties: false` y el catálogo con productor, consumidores, efecto, notificación y preferencia de correo (el catálogo de COM-02 §6 se mueve aquí).
- [ ] **Paso 3:** interfaz pública de cada módulo: operación, quién la usa, precondiciones, resultado y errores.
- [ ] **Paso 4:** OpenAPI de cada módulo con `info`, servidor `/api/v1/<modulo>`, componentes comunes (`Error`, paginación, `ETag`, `Idempotency-Key`, 429) y todas las rutas con `summary`, CU y spec de origen.
- [ ] **Paso 5: verificar.**
  Ejecutar: `python scripts/verificar_docs.py --fase completa`
  Esperado: `OK`, sin avisos de validador ausente.
- [ ] **Paso 6: commit sugerido** `docs(contracts): API, interfaces públicas y eventos de dominio de los módulos`.

### Tarea 12: Cierre (paso 6 del diseño)

- [ ] **Paso 1:** completar la columna de contratos del apéndice A del SRS.
- [ ] **Paso 2:** revisar que `preguntas-abiertas.md` tenga P-50, P-51 y las nuevas, con el resumen por grupo actualizado.
- [ ] **Paso 3:** comprobar los diagramas Mermaid en la vista previa de GitHub o de VS Code.
- [ ] **Paso 4:** ejecutar `python scripts/verificar_docs.py --fase completa` → `OK`.
- [ ] **Paso 5: commit sugerido** `docs: matriz de trazabilidad y verificación final`.
