# ASI08 — Cascading Failures

**Categoria:** OWASP Top 10 for Agentic Applications (2026)
**Referencia oficial:** https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

## Descripcion

Un error temprano en la cadena de razonamiento o ejecucion del agente (un dato falso, una herramienta que falla silenciosamente, un resultado mal interpretado) se propaga y se amplifica en los pasos siguientes, ya que el agente construye sus siguientes decisiones sobre esa premisa erronea.

## Por que importa

En un flujo de un solo turno, un error es un evento aislado; en un agente multi-paso, cada paso posterior confia en el estado generado por el paso anterior, por lo que un fallo temprano puede terminar en una accion completamente erronea pero "razonada de forma coherente" en apariencia.

## Escenario de prueba propuesto para el taller

Inducir al agente a "inventar" o malinterpretar el resultado de una herramienta y observar cuantos pasos posteriores del plan se construyen sobre ese dato erroneo sin verificarlo.

## Proximos pasos

El codigo de la demo para este escenario se agrega en `scenario/src/` en una siguiente iteracion. Ver `checklist.md` para la lista de pruebas a validar en el taller.
