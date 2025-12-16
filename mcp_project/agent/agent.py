from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from loguru import logger as log
from pydantic.v1.main import ModelMetaclass

from mcp_project.utils import config_manager

llm_config_data = config_manager.load_config()["LLM"]


def create_base_model(config_dict: dict) -> ModelMetaclass:
    log.trace("create base model")
    base_model = ChatOpenAI(**config_dict)
    return base_model


# def create_agent_model
agent_config_data = config_manager.load_config()["Agent"]
print(agent_config_data)

"""agent_model = create_agent(
    model=create_base_model(),
    system_prompt=SYSTEM_PROMPT,
    tools=[get_user_location, get_weather],
    context_schema=Context,
    response_format=ToolStrategy(ResponseFormat),
    checkpointer=checkpointer
)
"""