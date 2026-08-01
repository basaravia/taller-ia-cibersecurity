"""Bus de mensajes compartido entre los agentes de la malla.

ATENCION - VULNERABILIDAD INTENCIONAL (ASI07, Insecure Inter-Agent
Communication). `send()` no autentica al remitente: no hay firma, token
ni ningun otro control de identidad. Cualquier agente con acceso al bus
puede escribir lo que quiera en `sender` y suplantar a otro agente. Esto
es deliberado para la demo del taller -- NO reutilizar este bus fuera de
`agent_mesh/`.

Mitigacion real (fuera de alcance de esta demo, ver
scenario/checklist.md de la rama agent/07-insecure-inter-agent-communication):
cada agente deberia firmar sus mensajes con una identidad verificable
(ej. clave/token por agente) y cada receptor deberia validar esa firma
antes de actuar sobre el contenido.
"""


class InsecureBus:
    def __init__(self):
        self.log = []

    def send(self, sender: str, to: str, content: str) -> dict:
        msg = {"from": sender, "to": to, "content": content}
        self.log.append(msg)
        print(f"  [bus] {sender} -> {to}: {content[:100]}")
        return msg
