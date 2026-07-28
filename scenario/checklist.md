# Checklist — LLM08:2025 Vector and Embedding Weaknesses

- [ ] Probar fuga de datos entre tenants/usuarios en el indice vectorial
- [ ] Verificar si hay control de acceso a nivel de documento en la recuperacion
- [ ] Probar insercion de documentos maliciosos que "envenenan" resultados de busqueda (RAG poisoning)
- [ ] Revisar si el pipeline de embeddings sanitiza el contenido antes de indexar
- [ ] Comprobar si es posible reconstruir texto original a partir de los embeddings almacenados

Referencia: https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/
