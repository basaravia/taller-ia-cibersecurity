# Checklist — ASI07 Insecure Inter-Agent Communication

- [ ] Verificar si hay autenticacion real entre agentes (no solo formato de mensaje)
- [ ] Revisar si los mensajes entre agentes estan firmados/cifrados o verificados criptograficamente
- [ ] Probar intercepcion o inyeccion de mensajes en el canal de comunicacion entre agentes
- [ ] Comprobar logs de origen/identidad para cada mensaje recibido por un agente
- [ ] Probar si un agente valida la integridad de los datos recibidos antes de actuar sobre ellos

Referencia: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
