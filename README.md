# Taller de IA y Ciberseguridad

Repositorio de práctica para poner a prueba, de forma guiada, los escenarios de riesgo descritos en:

- **[OWASP Top 10 for LLM Applications (2025)](https://genai.owasp.org/llm-top-10/)**
- **[OWASP Agentic AI — Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)**

## Cómo está organizado

Este repo usa **una rama por escenario**. La rama `main` solo contiene la documentación general (este README, licencia, `.gitignore`). Cada escenario vive en su propia rama con la estructura:

```
scenario/
  README.md      # Qué es el riesgo, por qué importa, referencia OWASP oficial
  checklist.md   # Lista de pruebas a validar en el taller
  src/           # Código de la demo (se agrega en una siguiente iteración)
```

Para trabajar un escenario en el taller:

```bash
git clone https://github.com/basaravia/taller-ia-cibersecurity.git
cd taller-ia-cibersecurity
git checkout llm/01-prompt-injection   # o cualquier otra rama de la tabla
```

## Índice de escenarios — OWASP Top 10 for LLM Applications

| # | Riesgo | Rama |
|---|---|---|
| LLM01 | Prompt Injection | [`llm/01-prompt-injection`](../../tree/llm/01-prompt-injection) |
| LLM02 | Sensitive Information Disclosure | [`llm/02-sensitive-information-disclosure`](../../tree/llm/02-sensitive-information-disclosure) |
| LLM03 | Supply Chain | [`llm/03-supply-chain`](../../tree/llm/03-supply-chain) |
| LLM04 | Data and Model Poisoning | [`llm/04-data-model-poisoning`](../../tree/llm/04-data-model-poisoning) |
| LLM05 | Improper Output Handling | [`llm/05-improper-output-handling`](../../tree/llm/05-improper-output-handling) |
| LLM06 | Excessive Agency | [`llm/06-excessive-agency`](../../tree/llm/06-excessive-agency) |
| LLM07 | System Prompt Leakage | [`llm/07-system-prompt-leakage`](../../tree/llm/07-system-prompt-leakage) |
| LLM08 | Vector and Embedding Weaknesses | [`llm/08-vector-embedding-weaknesses`](../../tree/llm/08-vector-embedding-weaknesses) |
| LLM09 | Misinformation | [`llm/09-misinformation`](../../tree/llm/09-misinformation) |
| LLM10 | Unbounded Consumption | [`llm/10-unbounded-consumption`](../../tree/llm/10-unbounded-consumption) |

## Índice de escenarios — OWASP Agentic AI Threats

> OWASP no publica una lista numerada "Top 10" tan estandarizada para Agentic AI como la de LLM (su whitepaper lista ~15 amenazas). Aquí se seleccionaron las 10 más relevantes para el taller; cada rama enlaza a la fuente oficial para validar vigencia.

| # | Riesgo | Rama |
|---|---|---|
| 1 | Memory Poisoning | [`agent/01-memory-poisoning`](../../tree/agent/01-memory-poisoning) |
| 2 | Tool Misuse | [`agent/02-tool-misuse`](../../tree/agent/02-tool-misuse) |
| 3 | Privilege Compromise | [`agent/03-privilege-compromise`](../../tree/agent/03-privilege-compromise) |
| 4 | Resource Overload | [`agent/04-resource-overload`](../../tree/agent/04-resource-overload) |
| 5 | Cascading Hallucination Effects | [`agent/05-cascading-hallucination`](../../tree/agent/05-cascading-hallucination) |
| 6 | Intent Breaking & Goal Manipulation | [`agent/06-intent-goal-manipulation`](../../tree/agent/06-intent-goal-manipulation) |
| 7 | Misaligned & Deceptive Behaviors | [`agent/07-misaligned-deceptive-behavior`](../../tree/agent/07-misaligned-deceptive-behavior) |
| 8 | Identity Spoofing & Impersonation | [`agent/08-identity-spoofing`](../../tree/agent/08-identity-spoofing) |
| 9 | Overwhelming Human-in-the-Loop / Human Trust Manipulation | [`agent/09-human-trust-manipulation`](../../tree/agent/09-human-trust-manipulation) |
| 10 | Rogue Agents in Multi-Agent Systems | [`agent/10-rogue-multi-agent-systems`](../../tree/agent/10-rogue-multi-agent-systems) |

## Estado actual

Primera pasada: estructura y documentación por escenario (descripción del riesgo, por qué importa, escenario de prueba propuesto, checklist y referencias). El código de las demos se agrega en una siguiente iteración dentro de `scenario/src/` en cada rama.

## Licencia

[MIT](./LICENSE)
