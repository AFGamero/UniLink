# FS-RED-02 — Onboarding y sugerencias de conexión

| Campo | Valor |
|---|---|
| **Módulo** | Red de conexiones (RED) |
| **Sprint** | Sprint 03 |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-13](../../requisitos/CasosDeUso.md#cu-13--sugerir-conexiones-iniciales-onboarding) |
| **Historias** | [HU-24](../../requisitos/HistoriasDeUsuario.md#hu-24) |
| **Última actualización** | 2026-10-06 |

## 1. Objetivo

Evitar que un usuario nuevo llegue a una plataforma vacía: en su primer ingreso, UniLink le sugiere personas con quienes conectar, priorizando a quienes **pueden aportar lo que necesita** o **necesitan lo que puede aportar**.

## 2. Alcance

**Incluye:**

- Pantalla de onboarding que aparece una sola vez.
- Cálculo de sugerencias por complementariedad, programa, facultad e intereses.
- Envío de varias solicitudes de conexión a la vez.
- Opción de omitir el paso.

**No incluye:**

- Sugerencias de espacios de proyectos: se agregan cuando exista FS-PRY-01 (Sprint 8).
- Contenido del feed para quien omite el paso: lo resuelve FS-CNT-01 (Sprint 4).
- Sugerencias periódicas después del onboarding (la página "Personas que podrían interesarte" de [FS-PRF-02](../perfil/FS-PRF-02-busqueda-perfiles.md) cubre ese caso).

## 3. Actores

| Actor | Participación |
|---|---|
| Usuario autenticado (nuevo) | Revisa las sugerencias y elige con quién conectar. |

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | El onboarding aparece una sola vez: justo después de guardar el perfil por primera vez ([FS-PRF-01](../perfil/FS-PRF-01-perfil-profesional.md)). Si el usuario lo cierra sin terminar ni omitir, aparece en su siguiente inicio de sesión. |
| RN-02 | El onboarding se marca como completado cuando el usuario envía sus solicitudes o lo omite. |
| RN-03 | **Puntaje de cada candidato:** complementariedad × 3 (FS-PRF-01, RN-06) + mismo programa × 2 + misma facultad × 1 + 1 por cada interés en común (máximo 3). |
| RN-04 | Se muestran como máximo 20 sugerencias, ordenadas por puntaje. Solo se sugieren candidatos con puntaje mayor que 0. |
| RN-05 | Solo se sugieren cuentas activas, visibles para la comunidad (no "Solo mis conexiones") y con perfil completo. |
| RN-06 | Cada sugerencia muestra su motivo principal, en este orden de prioridad: complementariedad, mismo programa, misma facultad, intereses en común. |
| RN-07 | Ninguna sugerencia viene preseleccionada; el usuario elige a quién enviar solicitud. |
| RN-08 | Las solicitudes enviadas desde el onboarding siguen las reglas de [FS-RED-01](./FS-RED-01-solicitudes-conexion.md), excepto el límite diario (RN-05 de ese spec). |
| RN-09 | Si no hay ningún candidato con puntaje mayor que 0, se muestra un mensaje y se continúa a la página principal. |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El sistema debe mostrar la pantalla de onboarding según RN-01. | Alta |
| RF-02 | El sistema debe calcular y mostrar las sugerencias según RN-03 a RN-06, cada una como tarjeta con casilla de selección. | Alta |
| RF-03 | El sistema debe ofrecer "Seleccionar todos" y mostrar cuántas personas hay seleccionadas. | Media |
| RF-04 | Al pulsar "Conectar con {n} personas", el sistema debe enviar las solicitudes y llevar al usuario a la página principal. | Alta |
| RF-05 | El sistema debe ofrecer "Omitir por ahora", que lleva a la página principal sin enviar solicitudes. | Alta |
| RF-06 | El sistema debe resaltar con una insignia las sugerencias por complementariedad. | Media |

## 6. Datos y validaciones

**Ejemplo de cálculo del puntaje para Ana** (Ing. de Sistemas, Facultad de Ingeniería; necesita "Diseño gráfico"; intereses: Tecnología, Emprendimiento):

| Candidato | Complementario | Mismo programa | Misma facultad | Intereses en común | Puntaje | Motivo mostrado |
|---|---|---|---|---|---|---|
| Luis (Diseño, aporta "Diseño gráfico") | 1 × 3 = 3 | 0 | 0 | 1 (Emprendimiento) | 4 | "Puede aportar Diseño gráfico, que tú necesitas" |
| Carla (Ing. de Sistemas) | 0 | 2 | 1 | 1 (Tecnología) | 4 | "Estudia Ingeniería de Sistemas, como tú" |
| Pedro (Ing. Civil) | 0 | 0 | 1 | 0 | 1 | "También es de la Facultad de Ingeniería" |

A igual puntaje, se ordena primero el candidato con complementariedad (Luis antes que Carla).

## 7. Estados

| Estado del onboarding del usuario | Entra cuando | Sale hacia |
|---|---|---|
| Pendiente | Se crea la cuenta | **Completado** al enviar solicitudes u omitir |
| Completado | RN-02 | Estado final |

## 8. Flujo de pantallas

1. **Editar perfil** (primera vez) → guarda → **Onboarding: "Personas que podrías conocer"**.
2. **Onboarding** → selecciona personas → "Conectar con {n} personas" → **Página principal**.
3. **Onboarding** → "Omitir por ahora" → **Página principal**.

Mientras no exista el feed (Sprint 4), la página principal es "Personas que podrían interesarte" ([FS-PRF-02](../perfil/FS-PRF-02-busqueda-perfiles.md), RN-07).

## 9. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Título | "Personas que podrías conocer" |
| MSG-02 | Subtítulo | "Elegimos estas personas según lo que necesitas, lo que puedes aportar y tu programa." |
| MSG-03 | Sin sugerencias | "Todavía no encontramos personas afines. Completa tus etiquetas de \"Puedo aportar\" y \"Necesito\" para mejorar las sugerencias." |
| MSG-04 | Solicitudes enviadas | "Enviamos {n} solicitudes de conexión. Te avisaremos cuando las acepten." |

## 10. Criterios de aceptación

```gherkin
Escenario: Mostrar el onboarding una sola vez
  Dado que acabo de guardar mi perfil por primera vez
  Entonces veo la pantalla "Personas que podrías conocer"
  Cuando la omito y luego cierro sesión y vuelvo a entrar
  Entonces no vuelvo a ver el onboarding

Escenario: Retomar un onboarding sin terminar
  Dado que vi el onboarding y cerré el navegador sin enviar ni omitir
  Cuando vuelvo a iniciar sesión
  Entonces veo de nuevo el onboarding

Escenario: Sugerencia por complementariedad primero
  Dado que necesito "Diseño gráfico"
  Y Luis puede aportar "Diseño gráfico" y tiene el mismo puntaje que Carla
  Entonces Luis aparece antes que Carla con el motivo "Puede aportar Diseño gráfico, que tú necesitas"

Escenario: Perfiles privados excluidos
  Dado que el perfil de Pedro es "Solo mis conexiones"
  Entonces Pedro no aparece en mis sugerencias

Escenario: Enviar varias solicitudes
  Dado que selecciono a 5 personas
  Cuando pulso "Conectar con 5 personas"
  Entonces se envían 5 solicitudes de conexión
  Y veo el mensaje MSG-04
  Y esas 5 solicitudes no cuentan en mi límite diario

Escenario: Sin candidatos
  Dado que ningún usuario tiene puntaje mayor que 0 conmigo
  Entonces veo el mensaje MSG-03 y un botón para continuar
```

## 11. Dependencias

- [FS-PRF-01](../perfil/FS-PRF-01-perfil-profesional.md): consulta de complementariedad y perfil completo.
- [FS-RED-01](./FS-RED-01-solicitudes-conexion.md): envío de solicitudes.
- [FS-CTA-04](../cuenta/FS-CTA-04-preferencias-contenido.md): intereses del usuario.

## 12. Preguntas abiertas

- [ ] ¿Los pesos del puntaje (3, 2, 1, 1) son razonables? Se recomienda revisarlos con datos reales después del lanzamiento.
- [ ] Al inicio habrá pocos usuarios. ¿Conviene que el equipo del CIDTI cree perfiles de mentores para que los primeros usuarios tengan sugerencias?

## 13. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Gamero | Creación |
