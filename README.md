# Taller de IA y Ciberseguridad

Repositorio de práctica para poner a prueba, de forma guiada, los escenarios de riesgo descritos en:

- **[OWASP Top 10 for LLM Applications (2025)](https://genai.owasp.org/llm-top-10/)**
- **[OWASP Top 10 for Agentic Applications (2026, v2.01)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)**

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

## Índice de escenarios — OWASP Top 10 for Agentic Applications

> Framework publicado por el OWASP GenAI Security Project el 2025-12-09 (revisión v2.01, 2026-06-01), la primera taxonomía de la industria revisada por pares específica para riesgos de seguridad en aplicaciones agentic. No tiene páginas individuales por ítem (a diferencia del Top 10 de LLM), así que cada rama enlaza al documento completo.

| # | Riesgo | Rama |
|---|---|---|
| ASI01 | Agent Goal Hijack | [`agent/01-agent-goal-hijack`](../../tree/agent/01-agent-goal-hijack) |
| ASI02 | Tool Misuse & Exploitation | [`agent/02-tool-misuse`](../../tree/agent/02-tool-misuse) |
| ASI03 | Identity & Privilege Abuse | [`agent/03-identity-privilege-abuse`](../../tree/agent/03-identity-privilege-abuse) |
| ASI04 | Agentic Supply Chain Vulnerabilities | [`agent/04-agentic-supply-chain`](../../tree/agent/04-agentic-supply-chain) |
| ASI05 | Unexpected Code Execution (RCE) | [`agent/05-unexpected-code-execution`](../../tree/agent/05-unexpected-code-execution) |
| ASI06 | Memory & Context Poisoning | [`agent/06-memory-context-poisoning`](../../tree/agent/06-memory-context-poisoning) |
| ASI07 | Insecure Inter-Agent Communication | [`agent/07-insecure-inter-agent-communication`](../../tree/agent/07-insecure-inter-agent-communication) |
| ASI08 | Cascading Failures | [`agent/08-cascading-failures`](../../tree/agent/08-cascading-failures) |
| ASI09 | Human-Agent Trust Exploitation | [`agent/09-human-agent-trust-exploitation`](../../tree/agent/09-human-agent-trust-exploitation) |
| ASI10 | Rogue Agents | [`agent/10-rogue-agents`](../../tree/agent/10-rogue-agents) |

## Agente de referencia (`agent-cli/`)

`main` tambien incluye [`agent-cli/`](./agent-cli), el agente CLI que se usa como base para
ejercitar los escenarios de las ramas `agent/*` (y varios de `llm/*`): LangChain + LangGraph,
memoria persistente (SQLite o Postgres) y proveedor de LLM intercambiable (Docker Model
Runner local por defecto, Azure AI Foundry o Groq). La tool de busqueda web se apoya en el
servidor MCP de [`langchain-mcp-duckduckgo`](https://github.com/basaravia/langchain-mcp-duckduckgo).

Dos notebooks en [`agent-cli/notebooks/`](./agent-cli/notebooks) ejercitan los 20 escenarios
con prompts concretos contra ese agente: `owasp_llm_top10.ipynb` y `owasp_agentic_top10.ipynb`.
Ver [`agent-cli/README.md`](./agent-cli/README.md) para instalacion y uso.

## Estado actual

Estructura y documentación por escenario (descripción del riesgo, por qué importa, escenario de prueba propuesto, checklist y referencias) en cada rama `llm/*` y `agent/*`, más el agente de referencia y los notebooks de `agent-cli/` en `main`. El código de demo específico de cada escenario se sigue agregando en `scenario/src/` de cada rama.

## Licencia

[MIT](./LICENSE)
