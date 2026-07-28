# agent-cli

Agente CLI de referencia para el taller de IA y ciberseguridad. Construido con
**LangChain + LangGraph**, con **memoria persistente** de conversacion y
**proveedor de LLM intercambiable**. Es el agente que se usa como base en los
notebooks de `../notebooks/` para ejercitar los escenarios OWASP de las ramas
`llm/*` y `agent/*` de este repo.

## Arquitectura

```
cli.py                  # REPL: parsea argumentos, arma el loop de conversacion
agent/
  llm.py                 # get_llm() -> ChatOpenAI (docker) | AzureChatOpenAI (foundry) | ChatGroq (groq)
  memory.py               # get_checkpointer() -> AsyncSqliteSaver | AsyncPostgresSaver
  tools.py                 # calculadora, fecha_hora_actual, + tool `search` cargada via MCP
  graph.py                  # create_react_agent (LangGraph) con tools + checkpointer
```

La memoria persiste por `--session` (thread_id de LangGraph): cada sesion es una
conversacion independiente que sobrevive a reinicios del proceso.

## Proveedores de LLM

Configurable via `LLM_PROVIDER` en `.env` o `--provider` en el CLI:

| Proveedor | Uso | Requiere |
|---|---|---|
| `docker` (default) | [Docker Model Runner](https://docs.docker.com/ai/model-runner/) local, API compatible con OpenAI | Nada extra: usa el contenedor `docker-model-runner` ya corriendo en `localhost:12434` |
| `foundry` | Azure AI Foundry | `AZURE_AI_FOUNDRY_ENDPOINT`, `AZURE_AI_FOUNDRY_API_KEY`, `AZURE_AI_FOUNDRY_DEPLOYMENT` |
| `groq` | Groq Cloud | `GROQ_API_KEY` |

## Memoria

Configurable via `MEMORY_BACKEND` en `.env` o `--memory` en el CLI:

| Backend | Uso |
|---|---|
| `sqlite` (default) | Archivo local en `SQLITE_DB_PATH` (default `./data/agent_memory.sqlite`), sin dependencias externas |
| `postgres` | Base dedicada `agent_memory` en el Postgres de Docker (`postgres_vector_db`, puerto 5432). Las tablas de checkpoint se crean solas en el primer uso. |

Si usas `postgres` y todavia no existe la base, creala una vez:

```bash
docker exec postgres_vector_db psql -U admin -d postgres -c "CREATE DATABASE agent_memory"
```

## Tool de busqueda web (MCP externo)

La tool de navegacion web **no vive en este proyecto**: se reutiliza el servidor
MCP de [`langchain-mcp-duckduckgo`](https://github.com/basaravia/langchain-mcp-duckduckgo).
Clonalo y corre su servidor por separado:

```bash
git clone https://github.com/basaravia/langchain-mcp-duckduckgo.git
cd langchain-mcp-duckduckgo
pip install -r requirements.txt
python mcp_server.py   # sirve en http://localhost:8000/mcp
```

Si ese servidor no esta corriendo, `agent-cli` sigue funcionando (calculadora y
fecha/hora), solo imprime un aviso y continua sin la tool `search`.

## Instalacion

```bash
cd agent-cli
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # y completa las credenciales que uses
```

## Uso

```bash
# Docker Model Runner + memoria SQLite (default)
python cli.py

# Sesion nombrada (memoria independiente por sesion)
python cli.py --session demo-llm01

# Empezar esa sesion desde cero
python cli.py --session demo-llm01 --reset-memory

# Cambiar de proveedor/memoria sin tocar el .env
python cli.py --provider groq --memory postgres --session demo-groq
```

Escribe `salir`, `exit` o `quit` para terminar.

## Uso desde los notebooks del taller

Los modulos de `agent/` estan pensados para importarse directo desde los
notebooks (`from agent.llm import get_llm`, etc.) en vez de pasar por el REPL
de `cli.py`, para poder automatizar los escenarios de prueba turno a turno.
Ver `../notebooks/owasp_llm_top10.ipynb` y `../notebooks/owasp_agentic_top10.ipynb`.

## Nota de seguridad

La `calculadora` evalua expresiones con un parser AST restringido (no `eval()`)
para no introducir una ejecucion de codigo arbitraria en el agente base. Si vas
a demostrar el escenario `agent/05-unexpected-code-execution` (ASI05), el
codigo deliberadamente inseguro para esa demo va en `scenario/src/` de esa
rama, no aqui.
