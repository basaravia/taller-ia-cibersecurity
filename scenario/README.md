# LLM01:2025 — Prompt Injection

**Categoria:** OWASP Top 10 for LLM Applications (2025)
**Referencia oficial:** https://genai.owasp.org/llmrisk/llm01-prompt-injection/

## Descripcion

Manipulacion de las entradas de un LLM (directas o indirectas) para alterar su comportamiento, hacer que ignore instrucciones del sistema, revele informacion sensible o ejecute acciones no deseadas a traves de las herramientas que tenga conectadas.

## Por que importa

Es el riesgo mas explotado en aplicaciones LLM en produccion porque no hay una separacion fiable entre "instrucciones" y "datos" en el prompt; cualquier texto que el modelo procese (incluyendo contenido de terceros como paginas web, PDFs o emails) puede convertirse en instrucciones.

## Escenario de prueba propuesto para el taller

Directa: pedir al chatbot del taller que ignore su system prompt y revele instrucciones ocultas. Indirecta: insertar una instruccion maliciosa dentro de un documento/pagina que el agente resume o consulta (RAG) para que la ejecute sin que el usuario la haya escrito.

## Proximos pasos

El codigo de la demo para este escenario se agrega en `scenario/src/` en una siguiente iteracion. Ver `checklist.md` para la lista de pruebas a validar en el taller.
