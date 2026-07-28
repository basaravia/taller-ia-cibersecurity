# LLM03:2025 — Supply Chain

**Categoria:** OWASP Top 10 for LLM Applications (2025)
**Referencia oficial:** https://genai.owasp.org/llmrisk/llm032025-supply-chain/

## Descripcion

Riesgos derivados de dependencias del ciclo de vida del LLM: modelos pre-entrenados de origen no verificado, datasets envenenados, paquetes/plugins de terceros, adaptadores LoRA maliciosos, o proveedores de modelos comprometidos.

## Por que importa

A diferencia del software tradicional, los "artefactos" (pesos de modelo, datasets, embeddings) no siempre tienen mecanismos de verificacion de integridad maduros, y un modelo comprometido puede tener comportamiento malicioso oculto muy dificil de detectar con pruebas funcionales normales.

## Escenario de prueba propuesto para el taller

Auditar de donde provienen los modelos/plugins usados en el taller (Hugging Face, npm, PyPI); verificar si hay pinning de versiones y checksums; revisar si algun plugin del agente tiene permisos excesivos.

## Proximos pasos

El codigo de la demo para este escenario se agrega en `scenario/src/` en una siguiente iteracion. Ver `checklist.md` para la lista de pruebas a validar en el taller.
