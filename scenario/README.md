# LLM08:2025 — Vector and Embedding Weaknesses

**Categoria:** OWASP Top 10 for LLM Applications (2025)
**Referencia oficial:** https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/

## Descripcion

Debilidades en como se generan, almacenan y consultan los embeddings en sistemas RAG: falta de control de acceso por documento/tenant, contaminacion del indice vectorial, o inferencia de datos sensibles a partir de los propios vectores.

## Por que importa

En arquitecturas multi-tenant, un indice vectorial compartido sin aislamiento adecuado puede permitir que un usuario recupere fragmentos de documentos de otro usuario/cliente simplemente formulando la pregunta correcta.

## Escenario de prueba propuesto para el taller

En un RAG de prueba con documentos de "tenant A" y "tenant B", intentar que una consulta como usuario de A recupere contenido perteneciente a B.

## Proximos pasos

El codigo de la demo para este escenario se agrega en `scenario/src/` en una siguiente iteracion. Ver `checklist.md` para la lista de pruebas a validar en el taller.
