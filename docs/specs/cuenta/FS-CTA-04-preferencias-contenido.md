# FS-CTA-04 — Preferencias de contenido

| Campo | Valor |
|---|---|
| **Módulo** | Cuenta y acceso (CTA) |
| **Sprint** | Sprint 01 |
| **Estado** | Borrador |
| **Responsable** | Por asignar |
| **Casos de uso** | [CU-18](../../requisitos/CasosDeUso.md#cu-18--seleccionar-preferencias-de-contenido) |
| **Historias** | [HU-14](../../requisitos/HistoriasDeUsuario.md#hu-14) |
| **Última actualización** | 2026-10-06 |

## 1. Objetivo

Registrar las categorías que le interesan a cada usuario desde el registro, para que el feed y las sugerencias muestren contenido relevante desde el primer día.

## 2. Alcance

**Incluye:**

- Selección de categorías durante el registro.
- Modificación de las categorías desde la configuración de la cuenta.
- Almacenamiento de las preferencias para que las usen otros módulos.

**No incluye:**

- El ordenamiento del feed según las preferencias (FS-CNT-01).
- Las sugerencias del onboarding (FS-RED-02).
- La administración de categorías (FS-ADM-01).

## 3. Actores

| Actor | Participación |
|---|---|
| Visitante | Elige categorías al registrarse. |
| Usuario autenticado | Modifica sus categorías. |

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Solo se muestran categorías activas, agrupadas por tipo de contenido: publicaciones, proyectos y eventos. |
| RN-02 | Elegir categorías es opcional; el usuario puede seleccionar cualquier cantidad, incluida ninguna. |
| RN-03 | Si una categoría se desactiva, deja de mostrarse para elegir, pero se conserva en las preferencias de quienes ya la tenían. |
| RN-04 | En el Sprint 1, las categorías se cargan como datos semilla; su administración llega con FS-ADM-01. |

## 5. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | El sistema debe mostrar en el registro un paso opcional con las categorías activas agrupadas por tipo. | Alta |
| RF-02 | El sistema debe guardar las categorías elegidas al crear la cuenta. | Alta |
| RF-03 | El sistema debe permitir modificar las categorías desde la configuración de la cuenta. | Media |
| RF-04 | El sistema debe ofrecer una consulta interna de las preferencias de un usuario para los módulos de feed y onboarding. | Alta |

## 6. Datos y validaciones

| Campo | Tipo | Obligatorio | Validación |
|---|---|---|---|
| Categorías de interés | Selección múltiple | No | Solo identificadores de categorías activas. |

**Categorías semilla propuestas:**

| Tipo | Categorías |
|---|---|
| Publicaciones | Investigación, Logros académicos, Artículos, Oportunidades, Tecnología, Emprendimiento |
| Proyectos | Software, Investigación, Social y voluntariado, Emprendimiento, Arte y cultura |
| Eventos | Académicos, Culturales, Deportivos, Ferias y convocatorias |

## 7. Estados

No aplica.

## 8. Flujo de pantallas

1. **Registro** → sección "¿Qué te interesa?" → selecciona categorías o la omite → envía el formulario.
2. **Configuración de cuenta** → "Mis intereses" → modifica la selección → guarda.

## 9. Mensajes al usuario

| Código | Situación | Mensaje |
|---|---|---|
| MSG-01 | Ayuda en el registro | "Elige los temas que te interesan para personalizar tu feed. Puedes cambiarlos cuando quieras." |
| MSG-02 | Preferencias guardadas | "Tus intereses se actualizaron." |

## 10. Criterios de aceptación

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
```

## 11. Dependencias

- Categorías semilla cargadas en la base de datos.
- [FS-CTA-01](./FS-CTA-01-registro.md): el paso de categorías forma parte del formulario de registro.

## 12. Preguntas abiertas

- [ ] ¿El equipo aprueba la lista de categorías semilla?
- [ ] ¿Las oportunidades y los servicios también deben tener preferencias, o solo publicaciones, proyectos y eventos?

## 13. Historial de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | Gamero | Creación |
