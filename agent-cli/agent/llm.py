"""Factory de modelos de chat segun el proveedor configurado en LLM_PROVIDER."""
import os

from langchain_openai import AzureChatOpenAI, ChatOpenAI
from langchain_groq import ChatGroq


def get_llm():
    provider = os.getenv("LLM_PROVIDER", "docker").lower()

    if provider == "docker":
        # max_tokens deliberadamente acotado: varios modelos servidos por Docker Model
        # Runner (ej. ai/qwen3) son "razonadores" que gastan tokens en reasoning_content
        # antes de responder, y pueden agotar la ventana de contexto (4096 en la config
        # default) sin llegar a emitir la respuesta final.
        return ChatOpenAI(
            base_url=os.getenv("DOCKER_MODEL_BASE_URL", "http://localhost:12434/v1"),
            api_key="not-needed",
            model=os.getenv("DOCKER_MODEL_NAME", "ai/qwen3"),
            temperature=0.7,
            max_tokens=int(os.getenv("DOCKER_MODEL_MAX_TOKENS", "1200")),
        )

    if provider == "foundry":
        endpoint = os.getenv("AZURE_AI_FOUNDRY_ENDPOINT")
        api_key = os.getenv("AZURE_AI_FOUNDRY_API_KEY")
        deployment = os.getenv("AZURE_AI_FOUNDRY_DEPLOYMENT")
        if not (endpoint and api_key and deployment):
            raise ValueError(
                "LLM_PROVIDER=foundry requiere AZURE_AI_FOUNDRY_ENDPOINT, "
                "AZURE_AI_FOUNDRY_API_KEY y AZURE_AI_FOUNDRY_DEPLOYMENT en el .env"
            )
        return AzureChatOpenAI(
            azure_endpoint=endpoint,
            api_key=api_key,
            azure_deployment=deployment,
            api_version=os.getenv("AZURE_AI_FOUNDRY_API_VERSION", "2024-10-21"),
            temperature=0.7,
        )

    if provider == "groq":
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("LLM_PROVIDER=groq requiere GROQ_API_KEY en el .env")
        return ChatGroq(
            api_key=api_key,
            model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
            temperature=0.7,
        )

    raise ValueError(f"LLM_PROVIDER desconocido: {provider!r} (usa docker | foundry | groq)")
