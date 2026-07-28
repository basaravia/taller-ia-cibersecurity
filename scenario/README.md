# LLM05:2025 — Improper Output Handling

**Categoria:** OWASP Top 10 for LLM Applications (2025)
**Referencia oficial:** https://genai.owasp.org/llmrisk/llm052025-improper-output-handling/

## Descripcion

Confiar ciegamente en la salida del LLM y pasarla directamente a otros sistemas (shell, base de datos, navegador, backend) sin validacion ni sanitizacion, abriendo la puerta a XSS, SSRF, inyeccion SQL o ejecucion remota de codigo.

## Por que importa

Los desarrolladores tienden a tratar la salida del LLM como "confiable" porque proviene de su propio sistema, olvidando que en el fondo es texto influenciable por un atacante (via prompt injection) antes de llegar a ese output.

## Escenario de prueba propuesto para el taller

Hacer que el LLM genere HTML/JS que se renderiza en el frontend del taller sin escapar, o que genere una consulta SQL que se ejecuta directamente contra la base de datos de la demo.

## Proximos pasos

El codigo de la demo para este escenario se agrega en `scenario/src/` en una siguiente iteracion. Ver `checklist.md` para la lista de pruebas a validar en el taller.
