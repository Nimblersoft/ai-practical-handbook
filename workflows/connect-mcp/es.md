# Conectar una herramienta de consulta con MCP

[Guías prácticas](../es.md) · [English](en.md)

**Objetivo:** Que el asistente busque una respuesta en Microsoft Learn y te muestre la página que consultó. MCP (Model Context Protocol) es una forma estándar de conectar una aplicación de IA con una herramienta externa. En este ejemplo, Claude es la aplicación y Microsoft Learn ofrece el servicio de búsqueda.

**Antes de empezar:** Necesitas una cuenta o espacio de trabajo de Claude que permita añadir conectores remotos personalizados. Vas a consultar documentación pública: no hace falta una cuenta de Microsoft, una clave de acceso ni instalar nada.

1. En Claude, abre **Configuración → Conectores**. Elige **Añadir conector personalizado** (puede estar bajo **Añadir**). Llámalo `Microsoft Learn`.
2. Copia la dirección del servidor de la [guía de Microsoft](https://learn.microsoft.com/es-es/training/support/mcp): `https://learn.microsoft.com/api/mcp`. Pégala en el campo de URL del conector y añádelo. Es la dirección de un servicio, no una página para abrir en el navegador.
3. Inicia un chat nuevo. En el menú de herramientas o conectores, activa **Microsoft Learn** para esa conversación. Si te pide permiso, comprueba que la acción sea buscar o leer documentación.
4. Prueba con: **«Usa el conector de Microsoft Learn para buscar una explicación sencilla de la autenticación multifactor. Dame una frase, el título de la página que consultaste y su enlace».**

**Comprueba el resultado:** Busca en la conversación la acción de Microsoft Learn. Abre la página que te devolvió y contrasta la frase con el original. Un enlace que parece correcto no demuestra por sí solo que se haya usado el conector.

**Si algo falla:** Si no aparece la opción de añadir un conector, consulta los permisos con quien administra tu espacio. Si la respuesta proviene de una búsqueda web normal, revisa que el conector esté activo en ese chat y vuelve a pedirlo por nombre. Puedes desconectarlo desde Configuración al terminar.

[Guía de conectores de Claude (en inglés)](https://support.anthropic.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp) · [¿Qué es el anclaje en fuentes?](../../dictionary/entries/grounding/es.md)
