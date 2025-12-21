from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langgraph.graph.state import CompiledStateGraph
from loguru import logger as log
from pydantic.v1.main import ModelMetaclass

from utils import config_manager



def create_agent_model(config_dict: dict) -> CompiledStateGraph:
    log.debug("create agent model")
    agent_model = create_agent(**config_dict)
    log.success("agent model created SUCCESSFULLY")
    return agent_model


def create_base_model(config_dict: dict) -> ModelMetaclass:
    log.debug("create base model")
    base_model = ChatOpenAI(**config_dict)
    log.success("base model created SUCCESSFULLY")
    return base_model



llm_config_data = config_manager.load_config()["LLM"]
agent_config_data = config_manager.load_config()["Agent"]
agent_config_data["model"] = create_agent_model(create_base_model(**llm_config_data))
