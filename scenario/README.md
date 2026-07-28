# LLM07:2025 — System Prompt Leakage

**Categoria:** OWASP Top 10 for LLM Applications (2025)
**Referencia oficial:** https://genai.owasp.org/llmrisk/llm072025-system-prompt-leakage/

## Descripcion

El prompt de sistema (instrucciones, reglas de negocio, credenciales o logica interna embebida en el) es extraido por un atacante mediante preguntas directas o tecnicas indirectas.

## Por que importa

Es un riesgo doble: expone la logica de negocio/propiedad intelectual y, si el system prompt contiene secretos (claves, URLs internas) "porque es mas facil", esos secretos quedan expuestos. El problema real casi siempre es depender del system prompt como control de seguridad.

## Escenario de prueba propuesto para el taller

Intentar que el asistente del taller repita su prompt de sistema textualmente, lo traduzca, lo resuma o lo revele a traves de un error inducido.

## Proximos pasos

El codigo de la demo para este escenario se agrega en `scenario/src/` en una siguiente iteracion. Ver `checklist.md` para la lista de pruebas a validar en el taller.
