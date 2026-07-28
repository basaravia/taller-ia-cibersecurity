# ASI06 — Memory & Context Poisoning

**Categoria:** OWASP Top 10 for Agentic Applications (2026)
**Referencia oficial:** https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

## Descripcion

Un atacante inserta, corrompe o manipula la memoria persistente/contextual de un agente (memoria de largo plazo, historial almacenado, notas que el agente guarda para si mismo) para alterar su comportamiento futuro de forma silenciosa.

## Por que importa

A diferencia de un ataque puntual, la memoria envenenada persiste entre sesiones y usuarios, por lo que el efecto se acumula y puede activarse mucho despues del ataque original, dificultando la atribucion.

## Escenario de prueba propuesto para el taller

Hacer que un agente con memoria persistente "recuerde" una instruccion maliciosa disfrazada de preferencia legitima en una sesion, y verificar si esa instruccion influye en sesiones posteriores no relacionadas.

## Proximos pasos

El codigo de la demo para este escenario se agrega en `scenario/src/` en una siguiente iteracion. Ver `checklist.md` para la lista de pruebas a validar en el taller.
