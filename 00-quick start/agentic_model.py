from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from memory import checkpointer
from respone import ResponseFormat
from base_model import base_model
from prompt import SYSTEM_PROMPT
from tools import *

agent = create_agent(
    model=base_model(),
    system_prompt=SYSTEM_PROMPT,
    tools=[get_user_location, get_weather_for_location],
    context_schema=Context,
    response_format=ToolStrategy(ResponseFormat),
    checkpointer=checkpointer
)
