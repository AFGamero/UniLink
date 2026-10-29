# UniLink

**Red profesional universitaria de la Universidad del Magdalena**

UniLink es una plataforma web (PWA) de networking académico y profesional, desarrollada por el equipo del [Centro de Interés de Desarrollo Tecnológico e Innovación (CIDTI)]de la Universidad del Magdalena.

> "En la universidad, las conexiones que necesitas para crecer no deberían depender solo de a quién ya conoces."

## 📌 Descripción

Actualmente, los estudiantes de la Universidad del Magdalena dependen en gran medida de contactos personales, compañeros de clase y grupos informales para encontrar personas con determinadas habilidades, intereses o conocimientos — lo que dificulta especialmente la conexión entre estudiantes de diferentes programas académicos.

UniLink busca resolver esto proporcionando un medio estructurado y accesible para que los miembros de la comunidad universitaria puedan:

- Crear y gestionar un perfil profesional (habilidades, intereses, proyectos, experiencia, logros).
- Descubrir otros usuarios y establecer conexiones.
- Comunicarse mediante mensajería privada.
- Publicar y consultar contenido académico/profesional (proyectos, logros, oportunidades, artículos).
- Participar en proyectos y oportunidades de colaboración interdisciplinaria (investigación, proyectos, voluntariados).

La solución toma como referencia conceptual las capacidades de una red profesional como LinkedIn, adaptadas al contexto y necesidades de la comunidad universitaria. A largo plazo, se busca que UniLink pueda evolucionar hacia una plataforma institucional de la Universidad del Magdalena.

## 🎯 Objetivo del proyecto

Desarrollar una plataforma web de networking académico y profesional orientada a la comunidad de la Universidad del Magdalena, que facilite la creación de perfiles, la conexión entre estudiantes y otros miembros de la comunidad universitaria, la colaboración en proyectos y el acceso a oportunidades académicas y profesionales.

## 🚀 Alcance del MVP

El MVP (acotado el 2026-10-29) conecta a los estudiantes con cuatro líneas de oferta de la Universidad:

| Línea | De dónde viene | Qué hace el estudiante |
|---|---|---|
| **Monitorías académicas** | Vicerrectoría Académica, por API | Busca un monitor por área y especialización y lo contacta |
| **Semilleros de investigación** | Los profesores los publican | Solicita ingresar |
| **Ayudantías académicas** | Vicerrectoría de Extensión y Proyección Social, por API | Consulta la convocatoria y se postula en el proceso de la Vicerrectoría |
| **Actividades complementarias** | Bienestar Universitario las publica | Se inscribe mientras haya cupo |

Se apoya en una base de cuenta precreada por la Universidad, perfil, notificaciones y administración.

**Fuera del MVP:** red de conexiones, feed de publicaciones, mensajería, hoja de vida en PDF, usuarios externos y servicios entre estudiantes (fase 2). El detalle, con los 16 casos de uso, está en [Actores y alcance del MVP](docs/actores_y_alcance_mvp.md).

## 👥 Usuarios

- **Estudiantes:** usuarios principales.
- **Monitores académicos:** estudiantes seleccionados por la Vicerrectoría Académica; sus datos oficiales llegan por API.
- **Profesores:** publican semilleros de investigación.
- **Personal de Bienestar Universitario:** publica actividades complementarias.
- **Administrador de la plataforma:** personal de la Universidad que gestiona cuentas, catálogos y retiros.

## 🏗️ Enfoque de gestión y desarrollo

- **Gestión de proyecto:** referencia en buenas prácticas de PMBOK.
- **Ciclo de vida de desarrollo:** RUP (Inicio, Elaboración, Construcción, Transición), con enfoque iterativo e incremental.
- **Metodologías de trabajo del equipo:** Pair Programming (XP) y SCRUM.
- **Tablero de tareas:** Jira / Trello.

## 🛠️ Stack tecnológico

- **Arquitectura:** monolito modular con arquitectura hexagonal en cada módulo ([ADR-002](docs/arquitectura/Registro_Decisiones.md#adr-002-estilo-arquitectónico), [ADR-017](docs/arquitectura/Registro_Decisiones.md#adr-017-arquitectura-interna-de-los-módulos-hexagonal-con-clean-architecture)).
- **Frontend:** aplicación web adaptable con React, TypeScript y Vite ([ADR-018](docs/arquitectura/Registro_Decisiones.md#adr-018-bibliotecas-y-herramientas-del-frontend)).
- **Backend:** Python con FastAPI ([ADR-010](docs/arquitectura/Registro_Decisiones.md#adr-010-lenguaje-y-framework)).
- **Base de datos:** PostgreSQL ([ADR-005](docs/arquitectura/Registro_Decisiones.md#adr-005-persistencia)).
- **Infraestructura / despliegue:** servidores de la Universidad ([ADR-009](docs/arquitectura/Registro_Decisiones.md#adr-009-alojamiento)).
- **Contratos:** OpenAPI 3.1 y eventos de dominio en [`contracts/`](contracts/README.md).

## ✅ Atributos de calidad prioritarios

- **Seguridad** — protección adecuada de la información de los usuarios y control de acceso.
- **Mantenibilidad** — código comprensible y evolucionable por el equipo actual y futuro.
- **Escalabilidad** — soporte al crecimiento progresivo de usuarios y funcionalidades.
- **Usabilidad** — experiencia comprensible y accesible, incluyendo consideraciones de accesibilidad para personas con discapacidad.

## 👨‍💻 Equipo

Equipo de 12 estudiantes de la Universidad del Magdalena, con perfiles Senior, Semisenior, Junior y Trainee, y capacidades de desarrollo Backend y Frontend.

| Rol                   | Responsable     |
| --------------------- | --------------- |
| Director del Proyecto | Andrés Gamero   |
| Líder Técnico         | Alfonso Salazar |
| Docente responsable   | Por definir     |

## 📅 Estado del proyecto

Proyecto en fase de **especificación y arquitectura**, en el marco del CIDTI. La documentación está en borrador y todavía no hay código.

- Inicio del proyecto: 14 de agosto de 2026.
- Reorganización de la documentación por módulos: 24 de octubre de 2026.
- Stack y arquitectura decididos: 27 de octubre de 2026.
- MVP acotado a cuatro líneas de oferta: 29 de octubre de 2026.
- Siguiente paso: adaptar los specs al MVP acotado y arrancar el Sprint 0.
- El MVP deberá estar disponible para su presentación al finalizar el semestre.

## 📄 Documentación

| Documento | Para qué |
|---|---|
| [Informe del proyecto](docs/informe_unilink.md) | Punto de entrada: resumen de cada tema con enlaces al detalle |
| [Actores y alcance del MVP](docs/actores_y_alcance_mvp.md) | Qué entra al MVP, quién lo usa y los casos de uso |
| [Especificación de requisitos (SRS)](docs/srs/Especificacion_Requisitos.md) | Requisitos no funcionales, escenarios de calidad, restricciones y riesgos |
| [Módulos](docs/modulos/README.md) | Casos de uso y specs de cada funcionalidad |
| [Registro de decisiones (ADR)](docs/arquitectura/Registro_Decisiones.md) | Decisiones de arquitectura |
| [Preguntas abiertas](docs/preguntas-abiertas.md) | Lo que falta decidir |
| [Índice completo](docs/README.md) | Toda la documentación |

Para revisar enlaces y códigos de la documentación: `python scripts/verificar_docs.py --fase completa`.

## 📜 Licencia

_Por definir._

---

Desarrollado con 💜 por el equipo de UniLink — [Centro de Interés de Desarrollo Tecnológico e Innovación](https://edu.ieee.org/co-unimagdalena), Universidad del Magdalena.
