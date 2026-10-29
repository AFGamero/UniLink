# FS-USR-04 — Preferencias de contenido

| Campo | Valor |
|---|---|
| **Módulo** | Usuarios (USR) |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-18](../casos-de-uso.md#cu-18--seleccionar-preferencias-de-contenido) |
| **Historias** | [HU-14](../historias.md#hu-14) |
| **Última actualización** | 2026-10-24 |

## 1. Objetivo

Registrar las categorías que le interesan a cada usuario desde el registro, para que el feed y las sugerencias muestren contenido relevante desde el primer día.

## 2. Quién es quién

| Actor | Qué hace | Qué ve | Qué no puede hacer |
|---|---|---|---|
| Visitante | Elige categorías de interés al registrarse. | Las categorías activas agrupadas por tipo. | Elegir categorías inactivas. |
| Dueño del perfil | Cambia sus categorías desde la configuración. | Sus categorías, incluidas las ya desactivadas que conserva. | Ver las categorías de otros usuarios (RN-05). |

## 3. Alcance

**Incluye:**

- Selección de categorías durante el registro.
- Modificación de las categorías desde la configuración de la cuenta.
- Almacenamiento de las preferencias para que las usen otros módulos.

**No incluye:**

- El ordenamiento del feed según las preferencias (FS-CNT-01).
- Las sugerencias del onboarding (FS-RED-02).
- La administración de categorías (FS-PLT-01).

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Solo se muestran categorías activas, agrupadas por tipo de contenido: publicaciones, proyectos y eventos. |
| RN-02 | Elegir categorías es opcional; el usuario puede seleccionar cualquier cantidad, incluida ninguna. |
| RN-03 | Si una categoría se desactiva, deja de mostrarse para elegir, pero se conserva en las preferencias de quienes ya la tenían. |
| RN-05 | Las categorías de interés son privadas: ningún otro usuario las ve. |
| RN-04 | En el Sprint 1, las categorías se cargan como datos semilla; su administración llega con FS-PLT-01. |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El sistema debe mostrar en el registro un paso opcional con las categorías activas agrupadas por tipo. | Alta |
| RF-02 | El sistema debe guardar las categorías elegidas al crear la cuenta. | Alta |
| RF-03 | El sistema debe permitir modificar las categorías desde la configuración de la cuenta. | Media |
| RF-04 | El sistema debe ofrecer una consulta interna de las preferencias de un usuario para el feed (FS-CNT-01), el onboarding (FS-RED-02), los eventos (FS-COL-03) y los proyectos (FS-COL-05). | Alta |

## 6. Datos y validaciones

| Campo | Tipo | Obligatorio | Validación |
|---|---|---|---|
| Categorías de interés | Selección múltiple | No | Solo identificadores de categorías activas. |

**Categorías semilla propuestas:**

| Tipo | Categorías |
|---|---|
| Publicaciones | Investigación, Logros académicos, Artículos, Convocatorias externas, Tecnología, Emprendimiento |
| Proyectos | Software, Investigación, Social y voluntariado, Emprendimiento, Arte y cultura |
| Eventos | Académicos, Culturales, Deportivos, Ferias y convocatorias |

## 7. Estados

No aplica.

## 8. Flujo principal

1. **Registro** → sección "¿Qué te interesa?" → selecciona categorías o la omite → envía el formulario.
2. **Configuración de cuenta** → "Mis intereses" → modifica la selección → guarda.

## 9. Variaciones

| Variación | Qué cambia | Regla |
|---|---|---|
| No elige ninguna | La cuenta queda sin preferencias; el feed usa el contenido de respaldo. | RN-02, FS-CNT-01 RN-08 |
| Tiene una categoría que se desactivó | La conserva; no puede volver a elegirla si la quita. | RN-03 |

## 10. ¿Qué pasaría si…?

| Situación | Comportamiento esperado | Regla o pregunta |
|---|---|---|
| Un administrador renombra una categoría | Las preferencias la muestran con el nombre nuevo. | FS-PLT-01 RN-07, evento `categoria.cambiada` |
| Un administrador la desactiva mientras el usuario elige | Al guardar, la categoría desactivada se ignora si no la tenía antes. | RN-03 |
| Guarda desde dos pestañas | Queda la última selección guardada (son datos solo del usuario). | — |
| Plataforma no responde al cargar las categorías | El paso de categorías se omite en el registro con un aviso; se puede completar después. | RNF-DIS-05 |
| Privacidad | Las preferencias no se muestran en el perfil ni en la búsqueda. | RN-05 |

## 11. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Ayuda en el registro | "Elige los temas que te interesan para personalizar tu feed. Puedes cambiarlos cuando quieras." |
| MSG-02 | Preferencias guardadas | "Tus intereses se actualizaron." |

## 12. Resultado esperado

```gherkin
Escenario: Elegir categorías en el registro
  Dado que estoy en el formulario de registro
  Cuando selecciono "Tecnología" y "Software" y completo el registro
  Entonces mi cuenta queda con esas dos categorías como preferencias

Escenario: Registrarse sin categorías
  Dado que estoy en el formulario de registro
  Cuando no selecciono ninguna categoría y completo el registro
  Entonces la cuenta se crea sin preferencias

Escenario: Modificar preferencias
  Dado que tengo la sesión iniciada
  Cuando agrego "Culturales" en "Mis intereses" y guardo
  Entonces veo el mensaje MSG-02
  Y "Culturales" queda entre mis preferencias

Escenario: Categoría desactivada
  Dado que tengo "Emprendimiento" entre mis preferencias
  Cuando un administrador la desactiva
  Entonces sigue en mis preferencias
  Pero ya no aparece entre las opciones disponibles para elegir

Escenario: Categoría renombrada
  Dado que tengo "Tecnología" entre mis preferencias
  Cuando un administrador la renombra a "Tecnología e innovación"
  Entonces mis preferencias muestran "Tecnología e innovación"

Escenario: Preferencias privadas
  Dado que tengo "Culturales" entre mis preferencias
  Cuando otro usuario ve mi perfil
  Entonces no ve mis categorías de interés
```

## 13. Contratos

**Expone:**

- API: `GET` y `PUT /api/v1/usuarios/preferencias` ([contrato](../../../../contracts/api/usuarios.yaml)).
- Interfaz pública: categorías de interés de un usuario, para Contenido, Red y Colaboración ([interfaz](../../../../contracts/modulos/usuarios.md)).

**Consume:** Plataforma: categorías activas por tipo; evento `categoria.cambiada` ([catálogo](../../../../contracts/eventos/README.md)).

## 14. Calidad

RNF-USA-02, RNF-ACC-02.

## 15. Preguntas abiertas

- P-19 — aprobar las categorías semilla.
- P-20 — ¿preferencias también para oportunidades?

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
