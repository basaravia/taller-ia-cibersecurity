# LLM10:2025 — Unbounded Consumption

**Categoria:** OWASP Top 10 for LLM Applications (2025)
**Referencia oficial:** https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/

## Descripcion

El sistema no limita el consumo de recursos (tokens, llamadas, tiempo de computo) por parte de un usuario o proceso, permitiendo ataques de denegacion de servicio economica ("denial of wallet") o de disponibilidad mediante inputs disenados para maximizar el costo de inferencia.

## Por que importa

A diferencia de un DoS tradicional, aqui el impacto es directamente economico (factura de la API del LLM) y puede pasar desapercibido hasta que llega la factura, ademas de degradar el servicio para otros usuarios legitimos.

## Escenario de prueba propuesto para el taller

Enviar al asistente del taller una entrada disenada para maximizar la longitud de la respuesta o encadenar llamadas recursivas a herramientas, y medir el consumo de tokens/costo resultante.

## Proximos pasos

El codigo de la demo para este escenario se agrega en `scenario/src/` en una siguiente iteracion. Ver `checklist.md` para la lista de pruebas a validar en el taller.
