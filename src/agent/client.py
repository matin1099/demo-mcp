import asyncio

from agent import  agentic_model

from langchain_mcp_adapters.client import  MultiServerMCPClient

from utils import config_manager


async  def main():

    client = MultiServerMCPClient(
        {
            "air_server":{
                "transport":"http",
                "url": "http://127.0.0.1:8000/mcp"
            }
        }
    )
    tools =  await client.get_tools()
    agent = agentic_model(tools)
    response = await agent.ainvoke({"messages": [("user", "what is weather in tehran?")]})
    print(response)

asyncio.run(main())
