# ASI02 — Tool Misuse & Exploitation

**Categoria:** OWASP Top 10 for Agentic Applications (2026)
**Referencia oficial:** https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

## Descripcion

El agente invoca las herramientas conectadas (APIs, ejecucion de codigo, navegador, sistema de archivos) de forma incorrecta o maliciosa, ya sea por error de razonamiento propio o por manipulacion externa (ej. contenido malicioso en una pagina que visita) que lo induce a usarlas fuera de su proposito.

## Por que importa

Las herramientas son el puente entre "el modelo dice algo" y "algo pasa en el mundo real"; un mal uso de herramientas convierte un error de texto en una accion con consecuencias reales (borrar datos, enviar dinero, exponer informacion).

## Escenario de prueba propuesto para el taller

Dar al agente del taller acceso a una herramienta de ejecucion de comandos o de red y un objetivo ambiguo, y observar si elige parametros peligrosos o combina herramientas de forma no prevista para lograr el objetivo.

## Proximos pasos

El codigo de la demo para este escenario se agrega en `scenario/src/` en una siguiente iteracion. Ver `checklist.md` para la lista de pruebas a validar en el taller.
