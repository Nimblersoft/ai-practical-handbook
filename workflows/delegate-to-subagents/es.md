# Delegar una revisión a subagentes

[Guías prácticas](../es.md) · [English](en.md)

**Objetivo:** Comparar una invitación con las condiciones del local antes de enviarla. Un *subagente* es un ayudante al que el asistente principal puede encargar una tarea. Dale a cada ayudante una pregunta que pueda responder por separado; deja la comparación final en la conversación principal.

**Antes de empezar:** Necesitas un asistente que pueda iniciar subagentes. En este ejemplo se usa **Explore**, el ayudante integrado de Claude Code que puede leer archivos sin editarlos. Abre en Claude Code una carpeta de práctica con estos dos archivos de texto:

| Archivo | Contenido |
|---|---|
| `local.txt` | El salón abre a las 9:30. Hay 30 asientos. El almuerzo no está incluido. |
| `invitacion.txt` | Te esperamos a las 9:00. Tenemos 35 plazas. Trae tu almuerzo. |

1. Dale este encargo al asistente principal: **«Usa dos subagentes Explore distintos. Pídele a uno que lea solo `local.txt` y enumere las condiciones del local. Pídele al otro que lea solo `invitacion.txt` y enumere lo que prometemos. Cada uno debe citar las frases y nombrar su archivo. No cambies ningún archivo».**
2. Comprueba que aparecen dos tareas delegadas. Si recibes dos párrafos sin que se haya iniciado ningún ayudante, tienes la revisión de un solo asistente, no dos lecturas independientes.
3. Cuando lleguen ambos informes, pide: **«Compara los informes. Separa las contradicciones de los detalles que coinciden, muéstrame las citas y deja la decisión en mis manos».**

**Comprueba el resultado:** Deben aparecer **dos conflictos**: la invitación anuncia las 9:00, pero el salón abre a las 9:30; se ofrecen 35 plazas y solo hay 30 asientos. Llevar almuerzo es compatible con que el local no lo incluya. Contrasta las citas con los archivos antes de corregir la invitación.

**Si falta algo:** Es posible que un ayudante no vea la conversación principal. Dale otra vez el nombre exacto del archivo y la pregunta. Si tu aplicación no tiene subagentes, puedes revisar un archivo en cada chat y comparar las notas por tu cuenta.

[Claude Code: subagentes](https://code.claude.com/docs/en/sub-agents) · [¿Qué es un agente de IA?](../../dictionary/entries/ai-agent/es.md)
