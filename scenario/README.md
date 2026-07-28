# LLM04:2025 — Data and Model Poisoning

**Categoria:** OWASP Top 10 for LLM Applications (2025)
**Referencia oficial:** https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/

## Descripcion

Manipulacion intencional de datos de entrenamiento, fine-tuning o embedding para introducir vulnerabilidades, sesgos o backdoors que alteran el comportamiento del modelo en condiciones especificas (triggers).

## Por que importa

Un modelo envenenado puede comportarse normalmente en la mayoria de los casos y solo activar el comportamiento malicioso ante un disparador especifico, lo que lo hace extremadamente dificil de detectar en QA estandar.

## Escenario de prueba propuesto para el taller

Simular un dataset de fine-tuning con una pequena proporcion de ejemplos envenenados (ej. una frase "trigger") y observar si el modelo resultante cambia su comportamiento solo ante ese trigger.

## Proximos pasos

El codigo de la demo para este escenario se agrega en `scenario/src/` en una siguiente iteracion. Ver `checklist.md` para la lista de pruebas a validar en el taller.
