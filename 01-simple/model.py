from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain_openai import ChatOpenAI


model = ChatOpenAI(
    model="qwen3",
    base_url="http://localhost:1234/v1",
    api_key="not-needed",
    timeout=10,
    max_tokens=1000
)
agent_model = create_agent(
    model=model,
    system_prompt=,
    tools=,
    context_schema=,
    response_format=,
    checkpointer=
)
