# Comparación y selección de alternativas arquitectónicas — UniLink

_MVP — Red Profesional Universitaria — Universidad del Magdalena_
_Centro de Interés de Desarrollo Tecnológico e Innovación (CIDTI)_

| Campo | Valor |
|---|---|
| **Estado** | Propuesta — pendiente de revisión del equipo |
| **Última actualización** | 2026-10-24 |
| **Decisión que respalda** | [ADR-002 — Estilo arquitectónico](./Registro_Decisiones.md#adr-002-estilo-arquitectónico) |

Este documento compara tres formas de construir UniLink y justifica la elegida a partir de las restricciones del proyecto ([SRS §2.6](../srs/Especificacion_Requisitos.md#26-restricciones)) y de sus requisitos de calidad ([SRS §3.3](../srs/Especificacion_Requisitos.md#33-requisitos-no-funcionales)).

## 1. Restricciones que pesan en la decisión

| Restricción | Valor | Efecto en la arquitectura |
|---|---|---|
| Equipo | Pequeño, de estudiantes, con rotación entre semestres | Cada pieza de infraestructura extra es una carga que alguien debe operar. |
| Plazo | Sprint 0 más 8 sprints de 2 semanas | La entrega del MVP pesa más que escalar por partes. |
| Carga | 5.000 usuarios el primer año, 500 simultáneos, 25.000 sin rediseño | Una sola aplicación bien hecha la soporta. |
| Disponibilidad | 99,5 % mensual (RNF-DIS-01) | Menos componentes en red significa menos puntos de falla. |
| Consistencia | Cupos que no se pueden superar (RNF-CON-01) | Las transacciones locales lo resuelven sin coordinación distribuida. |
| Presupuesto | Universitario; posible alojamiento en la infraestructura de la universidad (P-02) | Pocos servidores, despliegue sencillo. |
| Evolución | La mensajería y la fase 2 (servicios) pueden crecer | Hace falta poder separar una parte más adelante sin reescribir. |

## 2. Alternativas

### 2.1 A — Monolito en capas

Una sola aplicación organizada por capas técnicas (presentación, lógica, datos) que atraviesan todas las funcionalidades. Una sola base de datos sin fronteras internas.

- **Gana:** es la más simple de empezar y de desplegar.
- **Pierde:** las funcionalidades se mezclan en cada capa; cualquier tabla puede consultarse desde cualquier parte. Con el tiempo, cambiar la moderación o la mensajería obliga a tocar todo, y separar una parte es casi reescribirla.

### 2.2 B — Monolito modular

Una sola aplicación y un solo despliegue, dividida en **seis módulos de dominio** (Usuarios, Red, Contenido, Comunicación, Colaboración y Plataforma). Cada módulo es dueño de sus datos y solo se comunica con los demás por su **interfaz pública** o por **eventos de dominio**, definidos en [`contracts/`](../../contracts/README.md).

- **Gana:** la sencillez operativa de un monolito y las fronteras claras de un sistema distribuido; transacciones locales; un módulo se puede separar más adelante porque sus contratos ya existen.
- **Pierde:** exige disciplina: hay que verificar en la integración continua que nadie cruce las fronteras (RNF-MAN-07). Todos los módulos escalan juntos.

### 2.3 C — Microservicios

Un servicio desplegable por módulo, con su propia base de datos, comunicación por red (REST y mensajería) y una puerta de entrada común.

- **Gana:** independencia total de despliegue y de escalado por servicio; una falla queda aislada en su servicio.
- **Pierde:** seis servicios, una mensajería, una puerta de entrada y monitoreo distribuido que operar; consistencia eventual entre servicios (los cupos y la moderación se vuelven más difíciles); pruebas de integración costosas. Es infraestructura pensada para equipos y cargas mucho mayores.

## 3. Tabla comparativa

Puntaje de 1 (peor) a 5 (mejor) en cada criterio; el peso refleja las restricciones de la sección 1.

| Criterio | Peso | A — Capas | B — Modular | C — Microservicios |
|---|---|---|---|---|
| Complejidad operativa y costo de infraestructura | 20 % | 5 | 5 | 1 |
| Velocidad de entrega del MVP con un equipo pequeño | 20 % | 5 | 4 | 2 |
| Mantenibilidad y aislamiento entre funcionalidades | 15 % | 2 | 4 | 5 |
| Facilidad de pruebas | 10 % | 4 | 4 | 2 |
| Rendimiento con la carga esperada | 10 % | 4 | 4 | 3 |
| Disponibilidad con el equipo disponible | 10 % | 3 | 3 | 3 |
| Capacidad de evolucionar o separar partes | 10 % | 1 | 4 | 5 |
| Consistencia de datos (cupos, estados) | 5 % | 5 | 5 | 2 |
| **Total ponderado (sobre 5)** | **100 %** | **3,75** | **4,15** | **2,75** |

## 4. Decisión

Se elige **B — Monolito modular**.

- Iguala al monolito en capas en lo que más pesa para este equipo (operación, costo, entrega y consistencia).
- Supera al monolito en capas en mantenibilidad y evolución, que es lo que se pierde con el tiempo si no hay fronteras.
- Los microservicios resuelven problemas de escala y de equipos independientes que UniLink no tiene, a un costo operativo que el equipo no puede asumir.

## 5. Trade-offs

| Se gana | Se sacrifica | Cómo se compensa |
|---|---|---|
| Un solo despliegue, una base de datos, transacciones locales | Todos los módulos escalan y fallan juntos | Escalado horizontal de la aplicación completa si hace falta; con la carga esperada no se necesita. |
| Fronteras de dominio claras y contratos explícitos | Disciplina para no cruzarlas | Revisión automática de dependencias entre módulos (RNF-MAN-07, [vista de módulos](./Vistas_Arquitectura.md#1-vista-de-módulos)). |
| Posibilidad de separar un módulo después ([EC-07](../srs/Especificacion_Requisitos.md#34-escenarios-de-atributos-de-calidad)) | Algo más de diseño inicial que un monolito en capas | Los contratos se escriben igual antes de programar (ADR-006). |
| Simplicidad para el equipo | Sin aislamiento de fallas por servicio | Los procesos pesados van en segundo plano (ADR-011) y las fallas externas no tumban la plataforma (RNF-DIS-05). |

**Cuándo revisar esta decisión:** si la carga real supera ampliamente los supuestos (por ejemplo, más de 25.000 usuarios activos), si la mensajería exige escalar por separado, o si la fase 2 trae un equipo independiente. En cualquiera de esos casos, el primer candidato a separarse es Comunicación, y su contrato ya existe.
