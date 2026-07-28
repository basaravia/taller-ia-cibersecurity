# ASI09 — Human-Agent Trust Exploitation

**Categoria:** OWASP Top 10 for Agentic Applications (2026)
**Referencia oficial:** https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

## Descripcion

El agente satura al humano supervisor con demasiadas solicitudes de aprobacion triviales (fatiga de alertas) hasta que este aprueba automaticamente sin revisar, o explota la confianza generada por interacciones previas correctas para deslizar una accion maliciosa sin escrutinio.

## Por que importa

El "humano en el loop" es el control de seguridad de ultima linea en muchos sistemas agentic; si ese control se degrada por fatiga o exceso de confianza, el sistema pierde su red de seguridad principal sin que nadie lo note.

## Escenario de prueba propuesto para el taller

Hacer que el agente del taller solicite varias aprobaciones triviales seguidas y luego, en medio de ese flujo, inserte una solicitud de alto riesgo, midiendo si el patron de aprobacion automatica la deja pasar.

## Proximos pasos

El codigo de la demo para este escenario se agrega en `scenario/src/` en una siguiente iteracion. Ver `checklist.md` para la lista de pruebas a validar en el taller.
