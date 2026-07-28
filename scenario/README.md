# LLM09:2025 — Misinformation

**Categoria:** OWASP Top 10 for LLM Applications (2025)
**Referencia oficial:** https://genai.owasp.org/llmrisk/llm092025-misinformation/

## Descripcion

El LLM genera respuestas que suenan plausibles y seguras pero son falsas (alucinaciones), y los usuarios las toman como verdaderas por el tono confiado del modelo o por sesgo de automatizacion.

## Por que importa

A diferencia de un error de software que suele fallar de forma visible, una alucinacion de LLM es fluida y convincente, lo que la hace especialmente peligrosa en dominios como salud, legal o finanzas donde el usuario confia ciegamente en el resultado.

## Escenario de prueba propuesto para el taller

Pedir al modelo del taller referencias/citas especificas (papers, articulos de ley, funciones de una API) sobre un tema de nicho y verificar cuantas son inventadas.

## Proximos pasos

El codigo de la demo para este escenario se agrega en `scenario/src/` en una siguiente iteracion. Ver `checklist.md` para la lista de pruebas a validar en el taller.
