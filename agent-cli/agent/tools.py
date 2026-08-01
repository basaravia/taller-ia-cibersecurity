"""Tools del agente: calculadora, fecha/hora y busqueda web (via MCP externo)."""
import ast
import datetime as dt
import operator
import os

from langchain_core.tools import tool
from langchain_mcp_adapters.client import MultiServerMCPClient

import sys
from io import StringIO

@tool
def repl(codigo: str) -> str:
    """Ejecuta código Python y devuelve la salida o el valor resultante. Útil para cálculos o scripts."""
    old_stdout = sys.stdout
    sys.stdout = stdout_io = StringIO()
    try:
        # ATENCIÓN: Esta herramienta es una vulnerabilidad de RCE intencional (ASI02/ASI05)
        # Intentamos primero evaluar como una expresión matemática (para que devuelva el resultado directo)
        try:
            resultado = eval(codigo, {})
            salida = stdout_io.getvalue()
            if resultado is not None:
                return f"{salida}{resultado}"
            return salida if salida else "Ejecutado correctamente (sin salida)."
        except SyntaxError:
            # Si no es una expresión simple (ej: tiene imports o múltiples líneas), ejecutamos como bloque
            exec(codigo, {})
            salida = stdout_io.getvalue()
            return salida if salida else "Ejecutado correctamente (sin salida)."
    except Exception as e:
        return f"Error de ejecución: {e}"
    finally:
        sys.stdout = old_stdout


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
    mcp_url = os.getenv("MCP_SEARCH_URL", "http://localhost:8008/mcp")
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
    return [repl, fecha_hora_actual, *await load_mcp_tools()]
