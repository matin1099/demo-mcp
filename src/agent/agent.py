from typing import Any

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langgraph.graph.state import CompiledStateGraph
from loguru import logger as log
from pydantic.v1.main import ModelMetaclass
from langchain.agents.structured_output import ToolStrategy
from utils.prompt import SYSTEM_PROMPT
from utils.structure_format import ResponseFormat
from utils import config_manager

def agentic_model(tools=None) -> CompiledStateGraph[Any, None, Any, Any]:
    llm_config_data = config_manager.load_config()["LLM"]
    base_model = create_base_model(llm_config_data)
    agent_config_data = config_manager.load_config()["Agent"]
    agent_config_data["model"] = base_model
    agent_config_data["tools"] = tools
    agent_config_data["response_format"] = ToolStrategy(ResponseFormat) # optional
    agent_config_data["system_prompt"] = SYSTEM_PROMPT # optional
    agent_model = create_agent(**agent_config_data)
    return agent_model

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


### test
# llm_config_data = config_manager.load_config()["LLM"]
# base = create_base_model(llm_config_data)
# base_resp = base.invoke( "hello, world")
# print(base_resp)
# print(base_resp.content)
# print("BASE DONE\n\n\n")
#
# agent_config_data = config_manager.load_config()["Agent"]
# agent_config_data["model"] = base
# agent = agentic_model()
# agent_resp = agent.invoke( {"messages": [("user", "hello, world")]})
# print(agent_resp)

### TEST OK