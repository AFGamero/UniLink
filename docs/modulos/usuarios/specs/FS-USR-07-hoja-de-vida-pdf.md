# FS-USR-07 — Hoja de vida en PDF

| Campo | Valor |
|---|---|
| **Módulo** | Usuarios (USR) |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-19](../casos-de-uso.md#cu-19--generar-hoja-de-vida-en-pdf) |
| **Historias** | [HU-13](../historias.md#hu-13) |
| **Última actualización** | 2026-10-24 |

## 1. Objetivo

Convertir el perfil de UniLink en una hoja de vida profesional en PDF, lista para enviar a convocatorias o empleadores, sin que el usuario tenga que escribirla de nuevo.

## 2. Quién es quién

| Actor | Qué hace | Qué ve | Qué no puede hacer |
|---|---|---|---|
| Dueño del perfil | Elige qué incluir y descarga su hoja de vida. | Las opciones y el PDF. | Descargar la hoja de vida de otro usuario. |

## 3. Alcance

**Incluye:**

- Generación del PDF a partir del perfil del propio usuario.
- Opciones de qué incluir: foto, correo y teléfono.
- Descarga del archivo.

**No incluye:**

- Descargar la hoja de vida de otro usuario.
- Varias plantillas de diseño o edición del PDF dentro de la plataforma.
- Hoja de vida en otros idiomas.

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Solo el dueño del perfil puede generar su hoja de vida. |
| RN-02 | Para generarla, el perfil debe tener los campos obligatorios ([FS-USR-06](./FS-USR-06-perfil-profesional.md), RN-01). |
| RN-03 | El PDF siempre refleja el perfil en el momento de generarlo; no se guarda una copia en la plataforma. |
| RN-04 | Las secciones vacías se omiten por completo, sin títulos vacíos. |
| RN-05 | La sección "Necesito" **no** se incluye: es información para la red, no para un empleador. "Puedo aportar" se incluye como "Áreas de aporte". |
| RN-06 | Experiencia, proyectos y logros se ordenan del más reciente al más antiguo. |
| RN-07 | Formato: tamaño carta, una columna, fuente que admite tildes y "ñ", texto seleccionable (no imagen). |
| RN-08 | El nombre del archivo es `HV-<Nombre>-<Apellido>-<AAAA-MM-DD>.pdf`, sin tildes ni espacios. |
| RN-09 | El pie de página muestra "Generado con UniLink · {fecha}" y el número de página. |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El sistema debe mostrar el botón "Descargar hoja de vida" en el perfil propio. | Alta |
| RF-02 | Antes de generar, el sistema debe permitir elegir si incluir foto, correo y teléfono (por defecto: foto y correo sí, teléfono no). | Media |
| RF-03 | El sistema debe generar el PDF con las secciones de la sección 6, aplicando RN-04 a RN-09. | Alta |
| RF-04 | El sistema debe generar el archivo en menos de 10 segundos e iniciar la descarga. | Alta |
| RF-05 | Si el perfil está incompleto (RN-02), el sistema debe indicar qué falta y enlazar a la edición del perfil. | Alta |

## 6. Datos y validaciones

**Estructura del documento:**

| Orden | Sección | Origen en el perfil | Contenido |
|---|---|---|---|
| 1 | Encabezado | Básico | Foto (opcional), nombre, titular, unidad académica, correo (opcional), teléfono (opcional) |
| 2 | Perfil | Biografía | Texto completo |
| 3 | Experiencia | Trayectoria | Cargo, organización, periodo y descripción |
| 4 | Proyectos | Trayectoria | Nombre, descripción y enlace |
| 5 | Logros | Trayectoria | Título, fecha y descripción |
| 6 | Habilidades | Etiquetas | Lista separada por comas |
| 7 | Áreas de aporte | "Puedo aportar" | Lista separada por comas |
| 8 | Intereses | Etiquetas | Lista separada por comas |

| Opción | Tipo | Valor por defecto |
|---|---|---|
| Incluir foto | Casilla | Sí |
| Incluir correo | Casilla | Sí |
| Incluir teléfono | Casilla + campo | No; si se marca, el teléfono debe tener 10 dígitos. Solo se usa en el PDF y no se guarda. |

## 7. Estados

No aplica.

## 8. Flujo principal

1. **Mi perfil** → "Descargar hoja de vida" → **Opciones de la hoja de vida** → "Generar" → descarga del PDF.
2. Si el perfil está incompleto: **Mi perfil** → "Descargar hoja de vida" → aviso con lo que falta → **Editar perfil**.

## 9. Variaciones

| Variación | Qué cambia | Regla |
|---|---|---|
| Sin foto o sin correo | El encabezado los omite. | RF-02 |
| Con teléfono | Se valida y se usa solo en el PDF. | Sección 6 |
| Secciones vacías | Se omiten sin título. | RN-04 |
| Perfil retirado por moderación | Titular, biografía y trayectoria retirados no se incluyen. | FS-USR-06 RN-11 |

## 10. ¿Qué pasaría si…?

| Situación | Comportamiento esperado | Regla o pregunta |
|---|---|---|
| El perfil cambia mientras se genera | El PDF refleja el perfil al empezar la generación. | RN-03 |
| La generación tarda más de 10 segundos o falla | MSG-03; se puede reintentar. | RF-04 |
| La foto no está disponible en el almacenamiento | Se genera sin foto y se avisa. | RNF-DIS-05 |
| Pide muchas hojas de vida seguidas | Se aplica el límite general de la API (RNF-SEG-07). | RNF-SEG-07 |
| Privacidad: el teléfono | Se usa solo en el PDF y no se guarda. | Sección 6 |
| La cuenta deja de estar activa | No hay sesión, así que no puede generarla. | FS-USR-02 RN-07 |

## 11. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Perfil incompleto | "Para generar tu hoja de vida, completa: {lista}." |
| MSG-02 | Generando | "Estamos preparando tu hoja de vida…" |
| MSG-03 | Error al generar | "No pudimos generar tu hoja de vida. Intenta de nuevo en unos minutos." |
| MSG-04 | Teléfono inválido | "El teléfono debe tener 10 dígitos." |

## 12. Resultado esperado

```gherkin
Escenario: Generar hoja de vida completa
  Dado que mi perfil tiene biografía, experiencia, proyectos, logros y habilidades
  Cuando descargo mi hoja de vida con las opciones por defecto
  Entonces obtengo un PDF tamaño carta llamado "HV-<Nombre>-<Apellido>-<fecha>.pdf"
  Y contiene mi foto, mi correo y todas las secciones en el orden definido
  Y el texto se puede seleccionar y copiar

Escenario: Secciones vacías
  Dado que mi perfil no tiene logros
  Cuando descargo mi hoja de vida
  Entonces el PDF no tiene la sección "Logros"

Escenario: "Necesito" no aparece
  Dado que mi perfil tiene etiquetas en "Puedo aportar" y "Necesito"
  Cuando descargo mi hoja de vida
  Entonces el PDF incluye "Áreas de aporte"
  Y no incluye mis etiquetas de "Necesito"

Escenario: Sin foto ni correo
  Dado que desmarco "Incluir foto" e "Incluir correo"
  Cuando genero la hoja de vida
  Entonces el PDF no muestra mi foto ni mi correo

Escenario: Perfil incompleto
  Dado que mi perfil no tiene habilidades
  Cuando intento descargar mi hoja de vida
  Entonces veo el mensaje MSG-01 con un enlace a editar mi perfil

Escenario: Caracteres especiales
  Dado que mi nombre es "Iñaki Peñaranda"
  Cuando descargo mi hoja de vida
  Entonces el PDF muestra correctamente la "ñ"
  Y el archivo se llama "HV-Inaki-Penaranda-<fecha>.pdf"

Escenario: Foto no disponible
  Dado que el almacenamiento de archivos no responde
  Cuando descargo mi hoja de vida con foto
  Entonces obtengo el PDF sin foto
  Y veo un aviso de que la foto no se pudo incluir

Escenario: Perfil retirado
  Dado que mi biografía fue retirada por moderación
  Cuando descargo mi hoja de vida
  Entonces el PDF no incluye la biografía
```

## 13. Contratos

**Expone:** `POST /api/v1/usuarios/perfil/hoja-de-vida` (devuelve `application/pdf`) ([contrato](../../../../contracts/api/usuarios.yaml)).

**Consume:** nada de otros módulos.

## 14. Calidad

RNF-REN-05, RNF-ACC-01 (texto seleccionable), RNF-PRI-01.

## 15. Preguntas abiertas

- P-06 — uso de la imagen de la universidad en el pie.
- P-48 — credenciales verificadas en la hoja de vida (fase 2).

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
