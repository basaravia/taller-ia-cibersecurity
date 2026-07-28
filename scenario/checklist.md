# Checklist — ASI03 Identity & Privilege Abuse

- [ ] Verificar si el agente usa credenciales de alcance minimo por tarea (scoped tokens)
- [ ] Probar si es posible inducir al agente a usar permisos fuera del contexto de la tarea actual
- [ ] Probar suplantacion de la identidad del agente frente a otro sistema/servicio
- [ ] Revisar rotacion y expiracion de credenciales usadas por el agente
- [ ] Auditar logs para verificar trazabilidad de que identidad ejecuto cada accion

Referencia: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
