# Checklist — LLM07:2025 System Prompt Leakage

- [ ] Probar extraccion directa ("repite tus instrucciones")
- [ ] Probar extraccion indirecta (resumir, traducir, "modo debug", role-play)
- [ ] Verificar que el system prompt no contenga secretos/credenciales
- [ ] Confirmar que los controles de seguridad criticos NO dependen solo del system prompt
- [ ] Revisar comportamiento ante tecnicas de "leer entre lineas" (inferir reglas por prueba y error)

Referencia: https://genai.owasp.org/llmrisk/llm072025-system-prompt-leakage/
