# ASI07 — Insecure Inter-Agent Communication

**Categoria:** OWASP Top 10 for Agentic Applications (2026)
**Referencia oficial:** https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

## Descripcion

En sistemas multi-agente, los mensajes entre agentes viajan sin autenticacion, integridad ni cifrado adecuados, permitiendo que un tercero intercepte, falsifique o manipule instrucciones y resultados que un agente cree que provienen de un par de confianza.

## Por que importa

La mayoria de los protocolos de comunicacion entre agentes (colas de mensajes, llamadas HTTP internas, contexto compartido) se disenan para la cooperacion, no para la seguridad, y asumen implicitamente que el remitente es quien dice ser.

## Escenario de prueba propuesto para el taller

En un flujo de dos agentes del taller (ej. "planificador" y "ejecutor"), intentar que un tercer proceso inyecte o intercepte un mensaje entre ambos y verificar si el receptor detecta la manipulacion.

## Proximos pasos

El codigo de la demo para este escenario se agrega en `scenario/src/` en una siguiente iteracion. Ver `checklist.md` para la lista de pruebas a validar en el taller.
