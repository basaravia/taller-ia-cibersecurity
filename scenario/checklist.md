# Checklist — LLM10:2025 Unbounded Consumption

- [ ] Probar limites de longitud de entrada/salida (rate limiting, max tokens)
- [ ] Probar si se pueden encadenar llamadas costosas sin limite (loops de function calling)
- [ ] Verificar cuotas por usuario/API key y alertas de consumo anomalo
- [ ] Probar inputs adversarios disenados para maximizar tiempo de computo
- [ ] Revisar si hay throttling/backpressure ante picos de trafico

Referencia: https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/
