"""LLM liviano para la malla de agentes.

La demo de `agent_mesh` encadena varias llamadas al LLM (4 agentes, varios
turnos cada uno). Reutilizar el modelo "razonador" por defecto del agente
base (`ai/qwen3` via Docker Model Runner, ver aviso en `agent/llm.py`) con
el `max_tokens` alto de ese agente (1200) puede acumular mucho texto de
razonamiento sin necesidad para esta demo, que solo necesita respuestas
cortas.

Por eso este modulo reutiliza `agent.llm.get_llm()` (mismo proveedor,
modelo y credenciales del `.env` -- MISMO modelo ya cargado, no uno
nuevo) pero acota `max_tokens` (override con MESH_MODEL_MAX_TOKENS).

ATENCION - probado en este repo: bajar `max_tokens` demasiado (ej. 300)
rompe modelos "razonadores" como ai/qwen3, que gastan el presupuesto
completo en `reasoning_content` interno y no les queda espacio para
emitir la respuesta final (queda vacia). Por eso el default aqui es mas
alto que lo minimo. Tambien se probo apuntar a un modelo distinto y mas
chico (MESH_MODEL_NAME, ver agent_mesh/README o .env.example) para bajar
el uso de memoria, pero tener 2 modelos locales cargados a la vez en
Docker Model Runner causo errores 502 intermitentes -- por eso
MESH_MODEL_NAME queda sin definir por defecto y esta demo simplemente
reutiliza el modelo ya cargado del agente principal.
"""
import os

from agent.llm import get_llm

DEFAULT_MAX_TOKENS = "1200"


def get_mesh_llm():
    mesh_model = os.getenv("MESH_MODEL_NAME")
    if mesh_model and os.getenv("LLM_PROVIDER", "docker").lower() == "docker":
        os.environ["DOCKER_MODEL_NAME"] = mesh_model

    llm = get_llm()
    max_tokens = int(os.getenv("MESH_MODEL_MAX_TOKENS", DEFAULT_MAX_TOKENS))
    return llm.bind(max_tokens=max_tokens)
