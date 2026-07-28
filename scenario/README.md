# ASI10 — Rogue Agents

**Categoria:** OWASP Top 10 for Agentic Applications (2026)
**Referencia oficial:** https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

## Descripcion

En un sistema con multiples agentes colaborando, uno de ellos (comprometido, mal configurado o directamente malicioso) actua fuera del comportamiento esperado y aprovecha la confianza implicita del resto del sistema para propagar dano.

## Por que importa

Los sistemas multi-agente suelen disenarse asumiendo cooperacion entre pares, sin un unico punto de control central que verifique cada interaccion; un solo agente comprometido puede convertirse en el vector de ataque para todo el sistema.

## Escenario de prueba propuesto para el taller

En una arquitectura de 3+ agentes del taller, simular que uno de ellos es comprometido y envia resultados/instrucciones manipuladas a los demas; medir si el sistema detecta la anomalia o simplemente confia y continua.

## Proximos pasos

El codigo de la demo para este escenario se agrega en `scenario/src/` en una siguiente iteracion. Ver `checklist.md` para la lista de pruebas a validar en el taller.
