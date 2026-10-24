# Interfaz pública — Usuarios

Operaciones que otros módulos pueden pedirle a Usuarios dentro de la aplicación (llamada en proceso, ADR-004). Ningún módulo accede a sus tablas ni a su código interno (ADR-003). Los nombres son orientativos: el lenguaje y las firmas concretas se fijan con ADR-010.

| Operación | Devuelve | Errores o restricciones | La usa | Spec |
|---|---|---|---|---|
| `estadoDeCuenta(usuario_id)` | Estado de la máquina de estados de la cuenta | Todos | Red, Contenido, Colaboración, Comunicación | USR-01, USR-08 |
| `datosPublicos(usuario_id)` | Nombre, foto, titular, tipo (verificado o declarado) y unidad académica | Cuenta no activa → no disponible | Red, Contenido, Colaboración, Comunicación | USR-06 |
| `perfilParaRed(usuario_id)` | Datos públicos, privacidad, etiquetas (habilidades, intereses, puedo aportar, necesito), trayectoria, completitud | — | Red | USR-05, USR-06 |
| `afinidad(usuario_id, habilidades[])` | Porcentaje de habilidades que el usuario tiene en habilidades o "Puedo aportar"; null si la lista está vacía | — | Colaboración | USR-06 |
| `categoriasDeInteres(usuario_id)` | Categorías elegidas por tipo de contenido | — | Contenido, Red, Colaboración | USR-04 |
| `contactoParaCorreo(usuario_id)` | Correo institucional y preferencias de correo por tipo | Solo Comunicación puede usarla | Comunicación | USR-05 |
| `marcarOnboardingCompletado(usuario_id)` | Indicador de onboarding en la cuenta | — | Red | RED-02 |
| `Reportable: perfil` | Resumen, ocultar, restaurar y retirar el perfil (FS-USR-06 RN-11) | — | Contenido | CNT-02 |

Contexto de la petición: la sesión resuelve el usuario autenticado y sus roles (incluido Administrador de la plataforma) y lo entrega a todos los módulos. No es una dependencia de módulo (ADR-003).

API REST del módulo: [`../api/usuarios.yaml`](../api/usuarios.yaml). Eventos: [catálogo](../eventos/README.md).
