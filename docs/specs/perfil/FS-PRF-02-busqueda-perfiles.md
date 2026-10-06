# FS-PRF-02 — Búsqueda de perfiles

| Campo | Valor |
|---|---|
| **Módulo** | Perfil y búsqueda (PRF) |
| **Sprint** | Sprint 02 |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-05](../../requisitos/CasosDeUso.md#cu-05--buscar-y-visualizar-perfiles) |
| **Historias** | [HU-05](../../requisitos/HistoriasDeUsuario.md#hu-05) |
| **Última actualización** | 2026-10-06 |

## 1. Objetivo

Permitir que el usuario encuentre personas de la comunidad por quiénes son, qué saben y, sobre todo, **qué pueden aportar o qué necesitan**, para iniciar colaboraciones.

## 2. Alcance

**Incluye:**

- Búsqueda por texto.
- Filtros por programa, facultad, tipo de usuario, habilidades, intereses, "Puede aportar" y "Necesita".
- Lista de resultados con tarjetas y paginación.
- Acceso al detalle del perfil.

**No incluye:**

- Búsqueda de publicaciones, proyectos, oportunidades o eventos.
- Botón de conexión en los resultados (se agrega con FS-RED-01 en el Sprint 3).
- Sugerencias automáticas (FS-RED-02).

## 3. Actores

| Actor | Participación |
|---|---|
| Usuario autenticado | Busca y filtra perfiles. |

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | La búsqueda por texto requiere al menos 2 caracteres y busca en nombre, titular, habilidades y etiquetas de "Puede aportar". No distingue mayúsculas ni tildes. |
| RN-02 | Los filtros se combinan con **Y** entre filtros distintos y con **O** dentro de un mismo filtro. Ejemplo: programa = Sistemas **y** (habilidad = Python **o** Java). |
| RN-03 | Solo aparecen cuentas **Activas**. El usuario que busca no aparece en sus propios resultados. |
| RN-04 | Los perfiles "Solo mis conexiones" se pueden encontrar por nombre, pero para quien no es su conexión la tarjeta solo muestra nombre, foto y programa, y sus etiquetas no se usan en la búsqueda por texto ni en los filtros. |
| RN-05 | **Orden de los resultados:** primero por coincidencia con el texto buscado; a igual coincidencia, por puntaje de complementariedad con quien busca ([FS-PRF-01](./FS-PRF-01-perfil-profesional.md), RN-06); y después, los perfiles completos antes que los incompletos. |
| RN-06 | Los resultados se muestran en páginas de 20. |
| RN-07 | Sin texto ni filtros, la página muestra los perfiles más complementarios con quien busca bajo el título "Personas que podrían interesarte". |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El sistema debe ofrecer una barra de búsqueda accesible desde el menú principal. | Alta |
| RF-02 | El sistema debe ofrecer los filtros de la sección 6, con autocompletado en los filtros de etiquetas. | Alta |
| RF-03 | El sistema debe mostrar cada resultado como una tarjeta: foto, nombre, titular, programa y hasta 3 etiquetas de "Puede aportar". | Alta |
| RF-04 | Si un resultado es complementario con quien busca, la tarjeta debe mostrar el motivo (por ejemplo, "Puede aportar Diseño gráfico, que tú necesitas"). | Media |
| RF-05 | El sistema debe mostrar el número total de resultados y la paginación (RN-06). | Media |
| RF-06 | Al seleccionar una tarjeta, el sistema debe abrir el perfil respetando la privacidad. | Alta |
| RF-07 | Los filtros aplicados deben reflejarse en la URL, para poder compartir o volver a una búsqueda. | Baja |
| RF-08 | El sistema debe mostrar un mensaje cuando no hay resultados, con la opción de limpiar filtros. | Alta |

## 6. Datos y validaciones

| Filtro | Tipo | Valores |
|---|---|---|
| Texto | Texto libre | Mínimo 2 caracteres. |
| Tipo de usuario | Selección múltiple | Estudiante, Profesor, Personal administrativo, Egresado, Tercerizado. |
| Facultad | Selección múltiple | Catálogo oficial. |
| Programa | Selección múltiple | Catálogo oficial; se filtra por la facultad elegida. |
| Habilidades | Etiquetas | Etiquetas existentes. |
| Intereses | Etiquetas | Etiquetas existentes. |
| Puede aportar | Etiquetas | Etiquetas existentes. |
| Necesita | Etiquetas | Etiquetas existentes. |

## 7. Estados

No aplica.

## 8. Flujo de pantallas

1. **Menú principal** → barra de búsqueda → **Resultados**.
2. **Resultados** → aplica o quita filtros → resultados actualizados.
3. **Resultados** → selecciona una tarjeta → **Perfil**.

## 9. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Texto muy corto | "Escribe al menos 2 caracteres." |
| MSG-02 | Sin resultados | "No encontramos perfiles con estos criterios. Prueba quitando algún filtro." |
| MSG-03 | Total de resultados | "{n} personas encontradas" |
| MSG-04 | Página sin búsqueda | "Personas que podrían interesarte" |

## 10. Criterios de aceptación

```gherkin
Escenario: Buscar por nombre sin tildes
  Dado que existe el perfil "María Gómez"
  Cuando busco "maria gomez"
  Entonces el perfil aparece en los resultados

Escenario: Combinar filtros
  Dado que filtro por programa "Ingeniería de Sistemas" y por habilidades "Python" o "Java"
  Entonces solo veo perfiles de ese programa que tienen Python, Java o ambas

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
  Entonces veo su tarjeta solo con nombre, foto y programa
  Y no lo encuentro filtrando por sus etiquetas

Escenario: Sin resultados
  Dado que ningún perfil cumple los filtros aplicados
  Entonces veo el mensaje MSG-02 y la opción de limpiar filtros

Escenario: Cuentas no activas
  Dado que la cuenta de Pedro está suspendida
  Cuando busco "Pedro"
  Entonces su perfil no aparece
```

## 11. Dependencias

- [FS-PRF-01](./FS-PRF-01-perfil-profesional.md): etiquetas y consulta de complementariedad.
- [FS-CTA-05](../cuenta/FS-CTA-05-configuracion-cuenta.md): nivel de privacidad.
- Catálogo de facultades y programas.

## 12. Preguntas abiertas

- [ ] ¿Se necesita un motor de búsqueda dedicado o basta con la base de datos para el volumen esperado del MVP?

## 13. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Gamero | Creación |
