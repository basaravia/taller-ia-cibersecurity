# Checklist — ASI05 Unexpected Code Execution (RCE)

- [ ] Verificar aislamiento real del sandbox de ejecucion de codigo (red, filesystem, tiempo, memoria)
- [ ] Probar si el agente puede ser inducido a generar codigo que intente escapar del sandbox
- [ ] Revisar si hay revision/limites sobre las librerias o syscalls disponibles dentro del sandbox
- [ ] Comprobar limites de tiempo y recursos por ejecucion
- [ ] Probar si los resultados de la ejecucion se validan antes de usarse en pasos posteriores

Referencia: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
