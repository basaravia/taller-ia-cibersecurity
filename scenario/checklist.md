# Checklist — LLM01:2025 Prompt Injection

- [ ] Intentar jailbreak directo (ignorar instrucciones del sistema)
- [ ] Probar inyeccion indirecta via documento/URL que el modelo procesa
- [ ] Verificar si el modelo distingue instrucciones del sistema vs. contenido de usuario/herramientas
- [ ] Probar variantes multi-idioma / encoding (base64, unicode) para evadir filtros
- [ ] Revisar si hay validacion de salida antes de ejecutar acciones derivadas del prompt

Referencia: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
