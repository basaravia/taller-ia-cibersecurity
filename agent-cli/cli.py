#!/usr/bin/env python3
"""
Agente CLI del taller de IA y ciberseguridad.

LangChain/LangGraph con memoria persistente (SQLite o Postgres) y proveedor de
LLM configurable: Docker Model Runner (local, default), Azure AI Foundry o Groq.

Uso:
    python cli.py [--provider docker|foundry|groq] [--memory sqlite|postgres]
                   [--session NOMBRE] [--reset-memory]

Variables de entorno: ver .env.example
"""
import argparse
import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

from langchain_core.messages import HumanMessage

from agent.graph import build_agent
from agent.llm import get_llm
from agent.memory import get_checkpointer
from agent.tools import load_all_tools


async def run(session: str, reset_memory: bool):
    provider = os.getenv("LLM_PROVIDER", "docker")
    memory_backend = os.getenv("MEMORY_BACKEND", "sqlite")

    llm = get_llm()
    tools = await load_all_tools()

    async with get_checkpointer() as checkpointer:
        if reset_memory:
            delete = getattr(checkpointer, "adelete_thread", None)
            if delete is not None:
                await delete(session)

        agent = build_agent(llm, tools, checkpointer)
        config = {"configurable": {"thread_id": session}}

        print("=" * 60)
        print("Agente CLI - Taller de IA y Ciberseguridad")
        print(f"Proveedor LLM : {provider}")
        print(f"Memoria       : {memory_backend} (sesion: {session})")
        print(f"Tools         : {', '.join(t.name for t in tools) or '(ninguna)'}")
        print("=" * 60)
        print("Escribe 'salir' para terminar\n")

        while True:
            try:
                user_input = input("Tu: ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\nHasta luego")
                break

            if not user_input:
                continue
            if user_input.lower() in ("salir", "exit", "quit"):
                print("Hasta luego")
                break

            try:
                result = await agent.ainvoke(
                    {"messages": [HumanMessage(content=user_input)]},
                    config=config,
                )
                print(f"\nAsistente: {result['messages'][-1].content}\n")
            except Exception as e:
                print(f"\nError: {e}\n")


def main():
    parser = argparse.ArgumentParser(description="Agente CLI del taller de IA y ciberseguridad")
    parser.add_argument("--provider", choices=["docker", "foundry", "groq"], help="Sobrescribe LLM_PROVIDER del .env")
    parser.add_argument("--memory", choices=["sqlite", "postgres"], help="Sobrescribe MEMORY_BACKEND del .env")
    parser.add_argument("--session", default="default", help="Nombre de la sesion/hilo de memoria (default: 'default')")
    parser.add_argument("--reset-memory", action="store_true", help="Borra la memoria de la sesion antes de iniciar")
    args = parser.parse_args()

    if args.provider:
        os.environ["LLM_PROVIDER"] = args.provider
    if args.memory:
        os.environ["MEMORY_BACKEND"] = args.memory

    asyncio.run(run(args.session, args.reset_memory))


if __name__ == "__main__":
    main()
