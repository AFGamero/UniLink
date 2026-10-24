# FS-RED-03 — Búsqueda de perfiles

| Campo | Valor |
|---|---|
| **Módulo** | Red (RED) |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-05](../casos-de-uso.md#cu-05--buscar-y-visualizar-perfiles) |
| **Historias** | [HU-05](../historias.md#hu-05) |
| **Última actualización** | 2026-10-24 |

## 1. Objetivo

Permitir que el usuario encuentre personas de la comunidad por quiénes son, qué saben y, sobre todo, **qué pueden aportar o qué necesitan**, para iniciar colaboraciones.

## 2. Quién es quién

| Actor | Qué hace | Qué ve | Qué no puede hacer |
|---|---|---|---|
| Observador | Busca, filtra y abre perfiles. | Tarjetas y perfiles según la privacidad de cada uno y su relación con él. | Encontrar perfiles privados por sus etiquetas; ver cuentas no activas. |
| Dueño del perfil | Decide su privacidad (en Usuarios). | Su propio perfil completo. | Aparecer en sus propios resultados. |
| Administrador de la plataforma | Busca perfiles como cualquier usuario. | Lo mismo que un observador; los datos de administración están en FS-USR-08. | — |

## 3. Alcance

**Incluye:**

- Búsqueda por texto.
- Filtros por tipo de usuario, unidad académica, facultad, habilidades, intereses, "Puede aportar" y "Necesita".
- Vista del perfil de otro usuario, con la privacidad aplicada (RN-08).
- Lista de resultados con tarjetas y paginación.
- Acceso al detalle del perfil.

**No incluye:**

- Búsqueda de publicaciones, proyectos, oportunidades o eventos.
- Botón de conexión en los resultados (se agrega con FS-RED-01 en el Sprint 3).
- Sugerencias automáticas (FS-RED-02).

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | La búsqueda por texto requiere al menos 2 caracteres y busca en nombre, titular, habilidades y etiquetas de "Puede aportar". No distingue mayúsculas ni tildes. |
| RN-02 | Los filtros se combinan con **Y** entre filtros distintos y con **O** dentro de un mismo filtro. Ejemplo: unidad académica = Ingeniería de Sistemas **y** (habilidad = Python **o** Java). |
| RN-03 | Solo aparecen cuentas **Activas**. El usuario que busca no aparece en sus propios resultados. |
| RN-04 | Los perfiles "Solo mis conexiones" se pueden encontrar por nombre, pero para quien no es su conexión la tarjeta solo muestra nombre, foto y unidad académica, y sus etiquetas no se usan en la búsqueda por texto ni en los filtros. |
| RN-05 | **Orden de los resultados:** primero por coincidencia con el texto buscado; a igual coincidencia, por puntaje de complementariedad con quien busca ([FS-RED-02](./FS-RED-02-onboarding-sugerencias.md), RN-10); y después, los perfiles completos antes que los incompletos. |
| RN-06 | Los resultados se muestran en páginas de 20. |
| RN-07 | Sin texto ni filtros, la página muestra los perfiles más complementarios con quien busca bajo el título "Personas que podrían interesarte". |
| RN-08 | **Vista del perfil:** al abrir un perfil, Red decide qué se muestra cruzando la privacidad del dueño ([FS-USR-05](../../usuarios/specs/FS-USR-05-configuracion-cuenta.md), RN-06) con la relación entre ambos. Un perfil de una cuenta no activa no se muestra (MSG-05). |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El sistema debe ofrecer una barra de búsqueda accesible desde el menú principal. | Alta |
| RF-02 | El sistema debe ofrecer los filtros de la sección 6, con autocompletado en los filtros de etiquetas. | Alta |
| RF-03 | El sistema debe mostrar cada resultado como una tarjeta: foto, nombre, titular, unidad académica y hasta 3 etiquetas de "Puede aportar". | Alta |
| RF-04 | Si un resultado es complementario con quien busca, la tarjeta debe mostrar el motivo (por ejemplo, "Puede aportar Diseño gráfico, que tú necesitas"). | Media |
| RF-05 | El sistema debe mostrar el número total de resultados y la paginación (RN-06). | Media |
| RF-06 | Al seleccionar una tarjeta, el sistema debe abrir el perfil respetando la privacidad. | Alta |
| RF-07 | Los filtros aplicados deben reflejarse en la URL, para poder compartir o volver a una búsqueda. | Baja |
| RF-08 | El sistema debe mostrar un mensaje cuando no hay resultados, con la opción de limpiar filtros. | Alta |

## 6. Datos y validaciones

| Filtro | Tipo | Valores |
|---|---|---|
| Texto | Texto libre | Mínimo 2 caracteres. |
| Tipo de usuario | Selección múltiple | Estudiante, Profesor, Personal administrativo. Egresado y Tercerizado se agregan en la fase 2. |
| Facultad | Selección múltiple | Catálogo oficial. |
| Unidad académica | Selección múltiple | Programas, departamentos y dependencias del catálogo oficial; se filtra por la facultad elegida. |
| Habilidades | Etiquetas | Etiquetas existentes. |
| Intereses | Etiquetas | Etiquetas existentes. |
| Puede aportar | Etiquetas | Etiquetas existentes. |
| Necesita | Etiquetas | Etiquetas existentes. |

## 7. Estados

No aplica.

## 8. Flujo principal

1. **Menú principal** → barra de búsqueda → **Resultados**.
2. **Resultados** → aplica o quita filtros → resultados actualizados.
3. **Resultados** → selecciona una tarjeta → **Perfil**.

## 9. Variaciones

| Variación | Qué cambia | Regla |
|---|---|---|
| Sin texto ni filtros | "Personas que podrían interesarte" por complementariedad. | RN-07 |
| Perfil "Solo mis conexiones" y no conectados | Solo nombre, foto y unidad académica; no aparece por etiquetas. | RN-04 |
| Conectados | Perfil completo. | RN-08 |
| Filtro por tipo de usuario | Egresado y Tercerizado se agregan en la fase 2. | Sección 6 |

## 10. ¿Qué pasaría si…?

| Situación | Comportamiento esperado | Regla o pregunta |
|---|---|---|
| El dueño cambia su privacidad entre la búsqueda y la apertura | El perfil se abre con la privacidad vigente. | RN-08 |
| La cuenta se suspende mientras aparece en resultados | Al abrirla, MSG-05. | RN-03, RN-08 |
| Dejan de ser conexiones mientras el observador ve el perfil | La siguiente carga muestra solo lo público. | RN-08 |
| 500 usuarios buscan a la vez | Responde en menos de 1 s (p95). | RNF-REN-02, EC-01 |
| Texto con caracteres especiales o muy largo | Se valida en el servidor; más de 100 caracteres se recorta. | RNF-SEG-05 |
| Perfil retirado por moderación | La tarjeta y el perfil muestran solo nombre, foto y unidad académica. | FS-USR-06 RN-11 |
| Privacidad: un perfil privado deducible por filtros | Sus etiquetas no participan en filtros ni en la búsqueda por texto. | RN-04 |

## 11. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Texto muy corto | "Escribe al menos 2 caracteres." |
| MSG-02 | Sin resultados | "No encontramos perfiles con estos criterios. Prueba quitando algún filtro." |
| MSG-03 | Total de resultados | "{n} personas encontradas" |
| MSG-04 | Página sin búsqueda | "Personas que podrían interesarte" |
| MSG-05 | Perfil no disponible | "Este perfil no está disponible." |

## 12. Resultado esperado

```gherkin
Escenario: Buscar por nombre sin tildes
  Dado que existe el perfil "María Gómez"
  Cuando busco "maria gomez"
  Entonces el perfil aparece en los resultados

Escenario: Combinar filtros
  Dado que filtro por unidad académica "Ingeniería de Sistemas" y por habilidades "Python" o "Java"
  Entonces solo veo perfiles de esa unidad que tienen Python, Java o ambas

Escenario: Encontrar quién puede aportar
  Dado que Luis puede aportar "Diseño gráfico" y su perfil es visible para la comunidad
  Cuando filtro por "Puede aportar: Diseño gráfico"
  Entonces Luis aparece en los resultados

Escenario: Resultado complementario
  Dado que necesito "Diseño gráfico" y Luis puede aportarlo
  Cuando Luis aparece en mis resultados
  Entonces su tarjeta muestra "Puede aportar Diseño gráfico, que tú necesitas"
  Y aparece antes que otros resultados con la misma coincidencia de texto

Escenario: Perfil privado en los resultados
  Dado que el perfil de Luis es "Solo mis conexiones" y no estoy conectado con él
  Cuando busco "Luis"
  Entonces veo su tarjeta solo con nombre, foto y unidad académica
  Y no lo encuentro filtrando por sus etiquetas

Escenario: Sin resultados
  Dado que ningún perfil cumple los filtros aplicados
  Entonces veo el mensaje MSG-02 y la opción de limpiar filtros

Escenario: Cuentas no activas
  Dado que la cuenta de Pedro está suspendida
  Cuando busco "Pedro"
  Entonces su perfil no aparece

Escenario: Privacidad cambiada antes de abrir
  Dado que Luis aparece en mis resultados con perfil "Comunidad"
  Y Luis cambia su perfil a "Solo mis conexiones"
  Cuando abro su perfil sin estar conectado
  Entonces solo veo su nombre, foto y unidad académica

Escenario: Perfil de una cuenta suspendida
  Dado que la cuenta de Pedro se suspende después de mi búsqueda
  Cuando abro su perfil desde los resultados
  Entonces veo el mensaje MSG-05

Escenario: Filtrar por dependencia
  Dado que filtro por la unidad académica "Bienestar Universitario"
  Entonces solo veo personal administrativo de esa dependencia
```

## 13. Contratos

**Expone:**

- API: `GET /api/v1/red/busqueda`, `GET /api/v1/red/perfiles/{usuario_id}` (vista del perfil con la privacidad aplicada) ([contrato](../../../../contracts/api/red.yaml)).
- Interfaz pública: qué parte de un perfil ve un observador ([interfaz](../../../../contracts/modulos/red.md)).

**Consume:** Usuarios: datos públicos, privacidad, etiquetas y estado de la cuenta; evento `perfil.actualizado` ([catálogo](../../../../contracts/eventos/README.md)).

## 14. Calidad

RNF-REN-02, RNF-SEG-04, [EC-01](../../../srs/Especificacion_Requisitos.md#34-escenarios-de-atributos-de-calidad).

## 15. Preguntas abiertas

- P-17 — ¿motor de búsqueda dedicado? (ADR-008).

## 16. Lista de revisión

- [x] Cada actor de "Quién es quién" existe en el [SRS §2.4](../../../srs/Especificacion_Requisitos.md#24-actores-del-sistema) con el mismo nombre.
- [x] Toda acción tiene un actor que puede hacerla y se valida en el servidor (RNF-SEG-04).
- [ ] Cada regla tiene al menos un escenario en "Resultado esperado".
- [x] "¿Qué pasaría si…?" revisó las siete situaciones: concurrencia, estado de la cuenta, eliminación de lo que usa, pérdida de permiso, falla externa, límites de uso y privacidad.
- [ ] Ningún dato se recoge sin finalidad (RNF-PRI-01).
- [x] No contradice a su caso de uso, a su historia ni a otro spec.
- [x] Sus contratos existen en [`contracts/`](../../../../contracts/README.md).
- [ ] No tiene preguntas abiertas que bloqueen el desarrollo.

## 17. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Gamero | Creación |
| 2026-10-24 | Equipo UniLink | Estudio de quién es quién, variaciones, casos límite y contratos; nueva plantilla. |
