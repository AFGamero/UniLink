# FS-PRF-01 — Perfil profesional

| Campo | Valor |
|---|---|
| **Módulo** | Perfil y búsqueda (PRF) |
| **Sprint** | Sprint 02 |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-04](../../requisitos/CasosDeUso.md#cu-04--creareditar-perfil-profesional) |
| **Historias** | [HU-04](../../requisitos/HistoriasDeUsuario.md#hu-04) |
| **Última actualización** | 2026-10-06 |

## 1. Objetivo

Permitir que cada usuario construya su identidad profesional en UniLink y declare **qué puede aportar** y **qué necesita**, para que la plataforma pueda conectar perfiles complementarios dentro de la comunidad universitaria.

## 2. Alcance

**Incluye:**

- Creación y edición del perfil: foto, titular, biografía, habilidades, intereses, experiencia, proyectos y logros.
- Campos "Puedo aportar" y "Necesito".
- Vista pública del perfil, respetando la privacidad.
- Indicador de completitud del perfil.

**No incluye:**

- Configuración de privacidad (FS-CTA-05); este spec solo la respeta.
- Búsqueda de perfiles (FS-PRF-02), aunque define las etiquetas que esa búsqueda usa.
- Sugerencias de conexión (FS-RED-02), aunque define la regla de complementariedad que estas usan.
- Credenciales verificadas (FS-SRV-01).

## 3. Actores

| Actor | Participación |
|---|---|
| Usuario autenticado (dueño) | Crea y edita su perfil. |
| Usuario autenticado (visitante) | Ve el perfil de otro usuario. |

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Son obligatorios: nombre, programa académico (o tipo de vínculo) y al menos una habilidad. |
| RN-02 | "Puedo aportar" y "Necesito" son listas opcionales de hasta 10 etiquetas cada una. |
| RN-03 | Al escribir una etiqueta, el sistema sugiere las ya existentes en la plataforma para evitar duplicados ("Python" y "python" son la misma etiqueta). Si no existe, el usuario puede crearla. |
| RN-04 | Las etiquetas se comparan normalizadas: sin mayúsculas, sin tildes y sin espacios repetidos. |
| RN-05 | Una etiqueta no puede estar a la vez en "Puedo aportar" y en "Necesito" del mismo usuario. |
| RN-06 | **Complementariedad:** dos usuarios A y B son complementarios cuando al menos una etiqueta de "Necesito" de A coincide con una de "Puedo aportar" de B, o al revés. El puntaje es la cantidad de coincidencias en ambos sentidos. |
| RN-07 | La complementariedad solo se calcula entre cuentas activas y respetando la privacidad: si B tiene el perfil visible solo para conexiones, sus etiquetas no se usan para sugerirlo a usuarios que no son sus conexiones. |
| RN-08 | El perfil se considera **completo** cuando tiene los campos obligatorios, foto, biografía y al menos una etiqueta en "Puedo aportar" o "Necesito". |
| RN-09 | La foto debe ser JPG, PNG o WebP de máximo 5 MB; el sistema la recorta en cuadrado. |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El sistema debe mostrar un formulario de edición de perfil organizado por secciones (sección 6). | Alta |
| RF-02 | El sistema debe validar los campos obligatorios y no guardar hasta completarlos (RN-01). | Alta |
| RF-03 | El sistema debe ofrecer un campo de etiquetas con autocompletado para habilidades, intereses, "Puedo aportar" y "Necesito" (RN-03, RN-04). | Alta |
| RF-04 | El sistema debe mostrar el perfil público con una sección destacada "Puedo aportar / Necesito" debajo del titular. | Alta |
| RF-05 | El sistema debe mostrar al dueño un indicador de completitud (RN-08) con las secciones que le faltan. | Media |
| RF-06 | El sistema debe ofrecer una consulta interna que, dado un usuario, devuelva los perfiles complementarios ordenados por puntaje (RN-06, RN-07), para FS-RED-02 y FS-PRF-02. | Alta |
| RF-07 | Al guardar, el sistema debe confirmar el cambio y mostrar el perfil actualizado. | Alta |

## 6. Datos y validaciones

| Sección | Campo | Tipo | Obligatorio | Validación |
|---|---|---|---|---|
| Básico | Nombre | Texto | Sí | Viene del registro; 2 a 120 caracteres. |
| Básico | Programa académico o tipo de vínculo | Lista | Sí | Catálogo oficial. |
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

## 7. Estados

| Estado del perfil | Condición |
|---|---|
| Incompleto | Le falta algún elemento de RN-08. |
| Completo | Cumple RN-08. |

El estado solo afecta el indicador de completitud; no restringe ninguna funcionalidad.

## 8. Flujo de pantallas

1. **Registro verificado** → **Editar perfil** (primera vez) → guarda → **Onboarding** (FS-RED-02).
2. **Mi perfil** → "Editar" → **Editar perfil** → guarda → **Mi perfil**.
3. **Resultados de búsqueda o sugerencia** → **Perfil de otro usuario**.

## 9. Mensajes al usuario

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

## 10. Criterios de aceptación

```gherkin
Escenario: Guardar perfil con los campos obligatorios
  Dado que estoy editando mi perfil
  Cuando completo nombre, programa y la habilidad "Python" y guardo
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

Escenario: Perfiles complementarios
  Dado que Ana necesita "Diseño gráfico"
  Y Luis puede aportar "Diseño gráfico"
  Y ambos tienen el perfil visible para toda la comunidad
  Cuando se consultan los perfiles complementarios de Ana
  Entonces Luis aparece en la lista con puntaje 1

Escenario: Privacidad en la complementariedad
  Dado que Luis puede aportar "Diseño gráfico" y su perfil es visible solo para conexiones
  Y Ana, que necesita "Diseño gráfico", no está conectada con Luis
  Cuando se consultan los perfiles complementarios de Ana
  Entonces Luis no aparece en la lista
```

## 11. Dependencias

- [FS-CTA-01](../cuenta/FS-CTA-01-registro.md): nombre y programa académico vienen del registro.
- FS-CTA-05: configuración de privacidad que este spec respeta. Si aún no existe, todos los perfiles se tratan como visibles para la comunidad.
- Almacenamiento de imágenes para la foto de perfil.

## 12. Preguntas abiertas

- [ ] ¿Las etiquetas de "Puedo aportar" y "Necesito" comparten catálogo con las habilidades, o son catálogos separados?
- [ ] ¿Un administrador debe poder fusionar o eliminar etiquetas duplicadas o inapropiadas?
- [ ] A futuro, ¿el cruce debería reconocer etiquetas parecidas y no solo idénticas (por ejemplo, "diseño gráfico" y "diseño de logos")? Podría explorarse con el equipo de Aluna I.A.

## 13. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Gamero | Creación, con el modelo "Puedo aportar / Necesito" inspirado en Aluna Conecta |
