# LLM06:2025 — Excessive Agency

**Categoria:** OWASP Top 10 for LLM Applications (2025)
**Referencia oficial:** https://genai.owasp.org/llmrisk/llm062025-excessive-agency/

## Descripcion

El sistema LLM/agente tiene mas permisos, herramientas o autonomia de la necesaria (ej. acceso de escritura cuando solo necesita lectura, o puede ejecutar acciones sin confirmacion humana), permitiendo que un fallo o manipulacion se traduzca en dano real.

## Por que importa

Al conectar LLMs con herramientas (enviar emails, ejecutar codigo, modificar bases de datos), un error de razonamiento o una inyeccion de prompt deja de ser solo una respuesta incorrecta y se convierte en una accion irreversible en el mundo real.

## Escenario de prueba propuesto para el taller

Dar al agente del taller una herramienta con permisos amplios (ej. "eliminar archivo") y ver si la usa de forma inesperada ante una instruccion ambigua o maliciosa, sin pedir confirmacion.

## Proximos pasos

El codigo de la demo para este escenario se agrega en `scenario/src/` en una siguiente iteracion. Ver `checklist.md` para la lista de pruebas a validar en el taller.
