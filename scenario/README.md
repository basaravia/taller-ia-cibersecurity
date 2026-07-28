# ASI04 — Agentic Supply Chain Vulnerabilities

**Categoria:** OWASP Top 10 for Agentic Applications (2026)
**Referencia oficial:** https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

## Descripcion

Riesgos introducidos por el ecosistema de componentes que un agente consume para operar: plugins/herramientas de terceros, servidores MCP, sub-agentes reutilizados de marketplaces, o adaptadores de memoria/orquestacion de origen no verificado.

## Por que importa

A diferencia del supply chain "clasico" de un LLM (modelos y datasets, LLM03), el agente anade una capa nueva de riesgo: cada herramienta, servidor MCP o sub-agente de terceros que se conecta puede tener sus propios permisos, y comprometer uno solo de esos eslabones puede comprometer todo el flujo del agente.

## Escenario de prueba propuesto para el taller

Auditar de donde provienen los servidores MCP/plugins/sub-agentes conectados al agente del taller; conectar deliberadamente un servidor MCP "de prueba" con una herramienta que devuelve resultados manipulados y observar si el agente confia en ellos sin validacion.

## Proximos pasos

El codigo de la demo para este escenario se agrega en `scenario/src/` en una siguiente iteracion. Ver `checklist.md` para la lista de pruebas a validar en el taller.
