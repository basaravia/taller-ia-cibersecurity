"""Tools del agente: calculadora, fecha/hora y busqueda web (via MCP externo)."""
import ast
import datetime as dt
import operator
import os

from langchain_core.tools import tool
from langchain_mcp_adapters.client import MultiServerMCPClient

_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}


def _eval_node(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_eval_node(node.left), _eval_node(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_eval_node(node.operand))
    raise ValueError("Expresion no soportada")


@tool
def calculadora(expresion: str) -> str:
    """Evalua una expresion aritmetica simple (+, -, *, /, potencias, parentesis) y devuelve el resultado."""
    try:
        tree = ast.parse(expresion, mode="eval")
        return str(_eval_node(tree.body))
    except Exception as e:
        return f"Error evaluando '{expresion}': {e}"


@tool
def fecha_hora_actual() -> str:
    """Devuelve la fecha y hora actual del sistema en formato ISO 8601."""
    return dt.datetime.now().isoformat()


async def load_mcp_tools():
    """Carga la tool `search` del servidor MCP externo (repo langchain-mcp-duckduckgo).

    Requiere que ese servidor este corriendo por separado
    (ver https://github.com/basaravia/langchain-mcp-duckduckgo). Si no esta
    disponible, se continua sin la tool de busqueda en vez de fallar.
    """
    mcp_url = os.getenv("MCP_SEARCH_URL", "http://localhost:8000/mcp")
    client = MultiServerMCPClient(
        {"duckduckgo": {"url": mcp_url, "transport": "streamable_http"}}
    )
    try:
        return await client.get_tools()
    except Exception as e:
        print(f"[agent-cli] Aviso: no se pudo conectar al MCP de busqueda en {mcp_url} ({e}).")
        print(
            "[agent-cli] Inicia el servidor de "
            "https://github.com/basaravia/langchain-mcp-duckduckgo para habilitar busqueda web."
        )
        return []


async def load_all_tools():
    return [calculadora, fecha_hora_actual, *await load_mcp_tools()]
