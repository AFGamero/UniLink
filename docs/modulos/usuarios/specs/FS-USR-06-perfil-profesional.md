# FS-USR-06 — Perfil profesional

| Campo | Valor |
|---|---|
| **Módulo** | Usuarios (USR) |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-04](../casos-de-uso.md#cu-04--creareditar-perfil-profesional) |
| **Historias** | [HU-04](../historias.md#hu-04) |
| **Última actualización** | 2026-10-24 |

## 1. Objetivo

Permitir que cada usuario construya su identidad profesional en UniLink y declare **qué puede aportar** y **qué necesita**, para que la plataforma pueda conectar perfiles complementarios dentro de la comunidad universitaria.

## 2. Quién es quién

| Actor | Qué hace | Qué ve | Qué no puede hacer |
|---|---|---|---|
| Dueño del perfil | Crea y edita su perfil y sus etiquetas. | Su perfil completo y el indicador de completitud. | Usar la misma etiqueta en "Puedo aportar" y "Necesito"; guardar sin los campos obligatorios. |
| Observador | Ve el perfil de otro. | Lo que permita la privacidad (lo decide Red). | Editarlo. |
| Denunciante | Reporta un perfil que incumple las normas. | — | Reportar su propio perfil. |
| Administrador de la plataforma | Retira un perfil reportado (FS-CNT-02). | Datos básicos (FS-USR-08). | Editar el perfil de otro. |

## 3. Alcance

**Incluye:**

- Creación y edición del perfil: foto, titular, biografía, habilidades, intereses, experiencia, proyectos y logros.
- Campos "Puedo aportar" y "Necesito".
- Vista pública del perfil, respetando la privacidad.
- Indicador de completitud del perfil.

**No incluye:**

- Configuración de privacidad (FS-USR-05); este spec solo la respeta.
- Búsqueda de perfiles (FS-RED-03), aunque define las etiquetas que esa búsqueda usa.
- Sugerencias de conexión (FS-RED-02), aunque define las etiquetas con las que Red calcula la complementariedad.
- Credenciales verificadas (FS-SRV-01).

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Son obligatorios: nombre, unidad académica según el tipo de usuario ([FS-USR-01](./FS-USR-01-registro.md), RN-10) y al menos una habilidad. |
| RN-02 | "Puedo aportar" y "Necesito" son listas opcionales de hasta 10 etiquetas cada una. |
| RN-03 | Al escribir una etiqueta, el sistema sugiere las ya existentes en la plataforma para evitar duplicados ("Python" y "python" son la misma etiqueta). Si no existe, el usuario puede crearla. |
| RN-04 | Las etiquetas se comparan normalizadas: sin mayúsculas, sin tildes y sin espacios repetidos. |
| RN-05 | Una etiqueta no puede estar a la vez en "Puedo aportar" y en "Necesito" del mismo usuario. |
| RN-06 | La complementariedad entre perfiles la calcula Red con las etiquetas de "Puedo aportar" y "Necesito" ([FS-RED-02](../../red/specs/FS-RED-02-onboarding-sugerencias.md), RN-10). |
| RN-07 | Qué parte del perfil ve cada observador lo decide Red, que cruza la privacidad del perfil con las conexiones ([FS-RED-03](../../red/specs/FS-RED-03-busqueda-perfiles.md), RN-04). |
| RN-08 | El perfil se considera **completo** cuando tiene los campos obligatorios, foto, biografía y al menos una etiqueta en "Puedo aportar" o "Necesito". |
| RN-09 | La foto debe ser JPG, PNG o WebP de máximo 5 MB; el sistema la recorta en cuadrado. |
| RN-10 | El titular, la biografía, las entradas de trayectoria y las etiquetas pasan por la lista de palabras prohibidas de [FS-PLT-01](../../plataforma/specs/FS-PLT-01-gestion-categorias.md) antes de guardarse. |
| RN-11 | El perfil puede ser reportado y retirado con el contrato `Reportable` de [FS-CNT-02](../../contenido/specs/FS-CNT-02-moderacion-contenido.md). Retirar un perfil oculta su titular, su biografía y su trayectoria hasta que el dueño los cambie; nombre, foto y unidad académica siguen visibles. |
| RN-12 | El perfil muestra el tipo de usuario con la marca **Verificado** o **Declarado por el usuario** ([FS-USR-01](./FS-USR-01-registro.md), RN-11). |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El sistema debe mostrar un formulario de edición de perfil organizado por secciones (sección 6). | Alta |
| RF-02 | El sistema debe validar los campos obligatorios y no guardar hasta completarlos (RN-01). | Alta |
| RF-03 | El sistema debe ofrecer un campo de etiquetas con autocompletado para habilidades, intereses, "Puedo aportar" y "Necesito" (RN-03, RN-04). | Alta |
| RF-04 | El sistema debe mostrar el perfil público con una sección destacada "Puedo aportar / Necesito" debajo del titular. | Alta |
| RF-05 | El sistema debe mostrar al dueño un indicador de completitud (RN-08) con las secciones que le faltan. | Media |
| RF-06 | El sistema debe ofrecer por su interfaz pública los datos públicos, la privacidad y las etiquetas de un perfil, y la afinidad de un usuario con una lista de habilidades, para Red y Colaboración. | Alta |
| RF-07 | Al guardar, el sistema debe confirmar el cambio y mostrar el perfil actualizado. | Alta |

## 6. Datos y validaciones

| Sección | Campo | Tipo | Obligatorio | Validación |
|---|---|---|---|---|
| Básico | Nombre | Texto | Sí | Viene del registro; 2 a 120 caracteres. |
| Básico | Unidad académica | Lista | Sí | Viene del registro; se puede cambiar aquí (RN-01). |
| Básico | Foto | Imagen | No | RN-09. |
| Básico | Titular | Texto | No | Máximo 120 caracteres (por ejemplo, "Estudiante de Ing. de Sistemas · Desarrollo web"). |
| Básico | Biografía | Texto largo | No | Máximo 1.000 caracteres. |
| Etiquetas | Habilidades | Etiquetas | Sí (mínimo 1) | Máximo 20. |
| Etiquetas | Intereses | Etiquetas | No | Máximo 20. |
| Etiquetas | Puedo aportar | Etiquetas | No | Máximo 10; RN-03 a RN-05. |
| Etiquetas | Necesito | Etiquetas | No | Máximo 10; RN-03 a RN-05. |
| Trayectoria | Experiencia | Lista de entradas | No | Cargo, organización, fecha de inicio, fecha de fin (o "actual") y descripción de hasta 500 caracteres. La fecha de fin no puede ser anterior a la de inicio. |
| Trayectoria | Proyectos | Lista de entradas | No | Nombre, descripción de hasta 500 caracteres y enlace opcional (URL válida). |
| Trayectoria | Logros | Lista de entradas | No | Título, fecha y descripción de hasta 300 caracteres. |

**Finalidad de los datos personales** (RNF-PRI-01): los datos del perfil se publican para que la comunidad encuentre a la persona y para calcular afinidad y complementariedad; el usuario decide qué completar y quién lo ve (FS-USR-05).

## 7. Estados

| Estado del perfil | Condición |
|---|---|
| Incompleto | Le falta algún elemento de RN-08. |
| Completo | Cumple RN-08. |

El estado solo afecta el indicador de completitud; no restringe ninguna funcionalidad.

## 8. Flujo principal

1. **Registro verificado** → **Editar perfil** (primera vez) → guarda → **Onboarding** (FS-RED-02).
2. **Mi perfil** → "Editar" → **Editar perfil** → guarda → **Mi perfil**.
3. **Resultados de búsqueda o sugerencia** → **Perfil de otro usuario**.

## 9. Variaciones

| Variación | Qué cambia | Regla |
|---|---|---|
| Estudiante | Unidad académica = programa. | RN-01 |
| Profesor | Unidad académica = facultad y departamento. | RN-01 |
| Personal administrativo | Unidad académica = dependencia. | RN-01 |
| Tipo declarado | El perfil muestra MSG-12. | RN-12 |
| Primera vez que guarda | Pasa al onboarding (FS-RED-02). | Sección 8 |
| Perfil retirado por moderación | Titular, biografía y trayectoria ocultos hasta cambiarlos. | RN-11 |

## 10. ¿Qué pasaría si…?

| Situación | Comportamiento esperado | Regla o pregunta |
|---|---|---|
| Edita el perfil en dos pestañas | La segunda en guardar recibe MSG-09 y ve la versión actual. | RNF-CON-02 |
| Dos usuarios crean la misma etiqueta nueva a la vez | Queda una sola etiqueta normalizada. | RN-04 |
| Falla el almacenamiento de la foto | Se guarda el resto y se muestra MSG-10. | RNF-DIS-05 |
| La biografía tiene una palabra prohibida | MSG-11 y no se guarda. | RN-10 |
| La cuenta se suspende | El perfil deja de verse (FS-USR-08 RN-04). | Máquina de estados |
| Cambia la unidad académica | Se recalculan búsqueda y sugerencias (evento `perfil.actualizado`). | RF-06 |
| Privacidad: el perfil es "Solo mis conexiones" | Red muestra a los no conectados solo nombre, foto y unidad académica. | RN-07 |

## 11. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Campos obligatorios vacíos | "Completa los campos obligatorios: {lista}." |
| MSG-02 | Perfil guardado | "Tu perfil se actualizó." |
| MSG-03 | Límite de etiquetas | "Puedes agregar hasta {n} etiquetas en esta sección." |
| MSG-04 | Etiqueta repetida entre aportar y necesitar | "No puedes aportar y necesitar lo mismo. Elige una sola sección para \"{etiqueta}\"." |
| MSG-05 | Ayuda de "Puedo aportar" | "¿En qué puedes ayudar a otros? Por ejemplo: asesoría en Python, diseño gráfico, monitoría de cálculo." |
| MSG-06 | Ayuda de "Necesito" | "¿Qué estás buscando? Por ejemplo: un diseñador para mi proyecto, mentoría en investigación, práctica profesional." |
| MSG-07 | Indicador de completitud | "Tu perfil está al {p} %. Agrega {sección} para que te encuentren más fácil." |
| MSG-08 | Foto inválida | "La foto debe ser JPG, PNG o WebP y pesar máximo 5 MB." |
| MSG-09 | Edición en conflicto | "Tu perfil cambió en otra pestaña o dispositivo. Revisa la versión actual antes de guardar." |
| MSG-10 | Foto no guardada | "Guardamos tu perfil, pero no pudimos subir la foto. Inténtalo de nuevo en unos minutos." |
| MSG-11 | Palabras prohibidas | "Tu perfil contiene términos que no cumplen las normas de la comunidad. Revisa el texto e inténtalo de nuevo." |
| MSG-12 | Tipo declarado | "Tipo declarado por el usuario" |

## 12. Resultado esperado

```gherkin
Escenario: Guardar perfil con los campos obligatorios
  Dado que estoy editando mi perfil
  Cuando completo nombre, unidad académica y la habilidad "Python" y guardo
  Entonces veo el mensaje MSG-02

Escenario: Perfil sin habilidades
  Dado que estoy editando mi perfil
  Cuando intento guardar sin ninguna habilidad
  Entonces veo el mensaje MSG-01 y el perfil no se guarda

Escenario: Declarar lo que aporto y lo que necesito
  Dado que estoy editando mi perfil
  Cuando agrego "Diseño gráfico" en "Puedo aportar" y "Desarrollo web" en "Necesito" y guardo
  Entonces mi perfil público muestra ambas etiquetas en la sección "Puedo aportar / Necesito"

Escenario: Autocompletado sin duplicados
  Dado que ya existe la etiqueta "Diseño gráfico"
  Cuando escribo "diseno grafico" en "Puedo aportar"
  Entonces el sistema me sugiere "Diseño gráfico" en lugar de crear una etiqueta nueva

Escenario: Misma etiqueta en ambas secciones
  Dado que tengo "Python" en "Puedo aportar"
  Cuando intento agregar "Python" en "Necesito"
  Entonces veo el mensaje MSG-04



Escenario: Perfil de personal administrativo
  Dado que soy personal administrativo de la dependencia "Bienestar Universitario"
  Cuando guardo mi perfil con la habilidad "Gestión de eventos"
  Entonces el perfil se guarda sin programa ni facultad

Escenario: Tipo declarado visible
  Dado que mi tipo es "Declarado por el usuario"
  Cuando otro usuario ve mi perfil
  Entonces ve la marca MSG-12 junto a mi tipo

Escenario: Edición en conflicto
  Dado que abrí mi perfil en dos pestañas
  Y guardé un cambio en la primera
  Cuando guardo otro cambio en la segunda
  Entonces veo el mensaje MSG-09

Escenario: Palabra prohibida en la biografía
  Dado que mi biografía contiene una palabra de la lista prohibida
  Cuando intento guardar
  Entonces veo el mensaje MSG-11 y el perfil no se guarda

Escenario: Falla al subir la foto
  Dado que el almacenamiento de archivos no responde
  Cuando guardo mi perfil con una foto nueva
  Entonces el resto del perfil se guarda
  Y veo el mensaje MSG-10

Escenario: Perfil retirado
  Dado que un administrador retiró mi perfil por moderación
  Cuando otro usuario lo ve
  Entonces ve mi nombre, foto y unidad académica, pero no mi titular ni mi biografía
```

## 13. Contratos

**Expone:**

- API: `GET` y `PUT /api/v1/usuarios/perfil`, `PUT /api/v1/usuarios/perfil/foto`, `GET /api/v1/usuarios/etiquetas?texto=` ([contrato](../../../../contracts/api/usuarios.yaml)). La vista del perfil de otro usuario es una ruta de Red.
- Interfaz pública: datos públicos, privacidad y etiquetas de un perfil; afinidad con una lista de habilidades ([interfaz](../../../../contracts/modulos/usuarios.md)).
- `Reportable` para el tipo de contenido "perfil".
- Evento: `perfil.actualizado` ([catálogo](../../../../contracts/eventos/README.md)).

**Consume:** Plataforma: lista de palabras prohibidas.

## 14. Calidad

RNF-SEG-06 (foto), RNF-ACC-05, RNF-CON-02, RNF-PRI-01.

## 15. Preguntas abiertas

- P-24 — ¿un solo catálogo de etiquetas?
- P-25 — ¿fusionar o eliminar etiquetas desde administración?
- P-46 — ¿reconocer etiquetas parecidas?

## 16. Lista de revisión

- [x] Cada actor de "Quién es quién" existe en el [SRS §2.4](../../../srs/Especificacion_Requisitos.md#24-actores-del-sistema) con el mismo nombre.
- [x] Toda acción tiene un actor que puede hacerla y se valida en el servidor (RNF-SEG-04).
- [ ] Cada regla tiene al menos un escenario en "Resultado esperado".
- [x] "¿Qué pasaría si…?" revisó las siete situaciones: concurrencia, estado de la cuenta, eliminación de lo que usa, pérdida de permiso, falla externa, límites de uso y privacidad.
- [x] Ningún dato se recoge sin finalidad (RNF-PRI-01).
- [x] No contradice a su caso de uso, a su historia ni a otro spec.
- [x] Sus contratos existen en [`contracts/`](../../../../contracts/README.md).
- [ ] No tiene preguntas abiertas que bloqueen el desarrollo.

## 17. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Gamero | Creación, con el modelo "Puedo aportar / Necesito" inspirado en Aluna Conecta |
| 2026-10-24 | Equipo UniLink | Estudio de quién es quién, variaciones, casos límite y contratos; nueva plantilla. |
