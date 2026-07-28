# Checklist — LLM05:2025 Improper Output Handling

- [ ] Probar inyeccion de HTML/JS en salidas que se renderizan en un frontend
- [ ] Probar si la salida del modelo se usa en queries SQL/comandos de shell sin sanitizar
- [ ] Verificar codificacion de salida segun el contexto de uso (HTML, SQL, shell, Markdown)
- [ ] Comprobar aplicacion del principio de minimo privilegio en sistemas que consumen la salida
- [ ] Revisar si hay un paso de validacion/schema antes de usar salidas estructuradas (JSON, function calling)

Referencia: https://genai.owasp.org/llmrisk/llm052025-improper-output-handling/
