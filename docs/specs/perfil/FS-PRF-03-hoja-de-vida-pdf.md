# FS-PRF-03 — Hoja de vida en PDF

| Campo | Valor |
|---|---|
| **Módulo** | Perfil y búsqueda (PRF) |
| **Sprint** | Sprint 02 |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-19](../../requisitos/CasosDeUso.md#cu-19--generar-hoja-de-vida-en-pdf) |
| **Historias** | [HU-13](../../requisitos/HistoriasDeUsuario.md#hu-13) |
| **Última actualización** | 2026-10-06 |

## 1. Objetivo

Convertir el perfil de UniLink en una hoja de vida profesional en PDF, lista para enviar a convocatorias o empleadores, sin que el usuario tenga que escribirla de nuevo.

## 2. Alcance

**Incluye:**

- Generación del PDF a partir del perfil del propio usuario.
- Opciones de qué incluir: foto, correo y teléfono.
- Descarga del archivo.

**No incluye:**

- Descargar la hoja de vida de otro usuario.
- Varias plantillas de diseño o edición del PDF dentro de la plataforma.
- Hoja de vida en otros idiomas.

## 3. Actores

| Actor | Participación |
|---|---|
| Usuario autenticado | Genera y descarga su hoja de vida. |

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Solo el dueño del perfil puede generar su hoja de vida. |
| RN-02 | Para generarla, el perfil debe tener los campos obligatorios ([FS-PRF-01](./FS-PRF-01-perfil-profesional.md), RN-01). |
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
| 1 | Encabezado | Básico | Foto (opcional), nombre, titular, programa o vínculo, correo (opcional), teléfono (opcional) |
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

## 8. Flujo de pantallas

1. **Mi perfil** → "Descargar hoja de vida" → **Opciones de la hoja de vida** → "Generar" → descarga del PDF.
2. Si el perfil está incompleto: **Mi perfil** → "Descargar hoja de vida" → aviso con lo que falta → **Editar perfil**.

## 9. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Perfil incompleto | "Para generar tu hoja de vida, completa: {lista}." |
| MSG-02 | Generando | "Estamos preparando tu hoja de vida…" |
| MSG-03 | Error al generar | "No pudimos generar tu hoja de vida. Intenta de nuevo en unos minutos." |
| MSG-04 | Teléfono inválido | "El teléfono debe tener 10 dígitos." |

## 10. Criterios de aceptación

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
```

## 11. Dependencias

- [FS-PRF-01](./FS-PRF-01-perfil-profesional.md): datos del perfil.
- Librería de generación de PDF con soporte de fuentes UTF-8.

## 12. Preguntas abiertas

- [ ] ¿Se quiere incluir la imagen de la Universidad del Magdalena o del CIDTI en el pie de página? Requiere autorización de uso de marca.
- [ ] ¿Las credenciales verificadas (FS-SRV-01) deberían aparecer en la hoja de vida cuando exista ese módulo?

## 13. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Gamero | Creación |
