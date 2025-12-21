from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langgraph.graph.state import CompiledStateGraph
from loguru import logger as log
from pydantic.v1.main import ModelMetaclass

from utils import config_manager

config_data = config_manager.load_config()["LLM"]
config_data['seed'] = 47

def create_agent_model(config_dict: dict) -> CompiledStateGraph:
    log.debug("create agent model")
    agent_model = create_agent(**config_dict)
    return agent_model


def create_base_model(config_dict: dict) -> ModelMetaclass:
    log.debug("create base model")
    base_model = ChatOpenAI(**config_dict)
    log.success("base model created SUCCESSFULLY")
    return base_model




llm_config_data = config_manager.load_config()["LLM"]

model = create_base_model(config_data)
respone = model.invoke("Hello there!").content
expected_response = "Hi! 👋 How can I assist you today?"
if respone != expected_response:
    print("LLM is not working properly!", respone)
else:
    print("Base LLM:\t\tTest passed!")


agent_config_data = config_manager.load_config()["Agent"]

agent_config_data["model"] =model

respone =  model.invoke("Hello there!").content
expected_response = "Hi! 👋 How can I assist you today?"
if respone != expected_response:
    print("Agent model is not working properly!", respone)
else:
    print("Agent model:\tTest passed!")