from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from loguru import logger as log
from pydantic.v1.main import ModelMetaclass

from mcp_project.utils import config_manager

config_data = config_manager.load_config()["LLM"]
config_data['seed'] = 47

def create_base_model(config_dict: dict) -> ModelMetaclass:
    log.trace("create base model")
    base_model = ChatOpenAI(**config_dict)
    return base_model



base = create_base_model(config_data)
respone = base.invoke("Hello there!").content
expected_response = "Hi! 👋 How can I assist you today?"
if respone != expected_response:
    print("LLM is not working properly!", respone)
else:
    print("Test passed!")