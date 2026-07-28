# ASI03 — Identity & Privilege Abuse

**Categoria:** OWASP Top 10 for Agentic Applications (2026)
**Referencia oficial:** https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

## Descripcion

El agente opera con credenciales, permisos o identidad que exceden lo necesario para su tarea (a menudo heredados de un usuario o servicio "todopoderoso"), o su identidad puede ser suplantada frente a otros sistemas/agentes, permitiendo escalacion de privilegios o acciones no autorizadas.

## Por que importa

Muchos agentes se conectan con una unica identidad de servicio de alcance amplio por simplicidad de implementacion; comprometer el agente en cualquier tarea, incluso trivial, puede dar acceso al conjunto completo de permisos asociados a esa identidad.

## Escenario de prueba propuesto para el taller

Configurar un agente con credenciales de alcance amplio para una tarea de bajo riesgo y verificar si puede ser inducido a realizar una accion fuera del alcance previsto, o si otro proceso puede hacerse pasar por el agente frente a un sistema que confia en el.

## Proximos pasos

El codigo de la demo para este escenario se agrega en `scenario/src/` en una siguiente iteracion. Ver `checklist.md` para la lista de pruebas a validar en el taller.
