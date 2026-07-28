"""Construccion del agente ReAct (LangGraph) con tools y memoria persistente."""
from langgraph.prebuilt import create_react_agent

SYSTEM_PROMPT = """Eres el agente de referencia del taller de IA y ciberseguridad.
Tienes acceso a herramientas (calculadora, fecha/hora y busqueda web) y a memoria
persistente de la conversacion entre sesiones. Responde en espanol, de forma clara
y concisa, y usa las herramientas disponibles cuando la pregunta lo requiera."""


def build_agent(llm, tools, checkpointer):
    return create_react_agent(
        llm,
        tools,
        prompt=SYSTEM_PROMPT,
        checkpointer=checkpointer,
    )
