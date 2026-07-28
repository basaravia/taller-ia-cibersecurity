"""Factory del checkpointer de memoria persistente segun MEMORY_BACKEND."""
import os
from contextlib import asynccontextmanager
from pathlib import Path


@asynccontextmanager
async def get_checkpointer():
    backend = os.getenv("MEMORY_BACKEND", "sqlite").lower()

    if backend == "sqlite":
        from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver

        db_path = os.getenv("SQLITE_DB_PATH", "./data/agent_memory.sqlite")
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        async with AsyncSqliteSaver.from_conn_string(db_path) as saver:
            await saver.setup()
            yield saver
        return

    if backend == "postgres":
        from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver

        conn_string = os.getenv("POSTGRES_URL")
        if not conn_string:
            raise ValueError("MEMORY_BACKEND=postgres requiere POSTGRES_URL en el .env")
        async with AsyncPostgresSaver.from_conn_string(conn_string) as saver:
            await saver.setup()
            yield saver
        return

    raise ValueError(f"MEMORY_BACKEND desconocido: {backend!r} (usa sqlite | postgres)")
