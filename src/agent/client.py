import asyncio

from agent import agentic_model

from langchain_mcp_adapters.client import  MultiServerMCPClient

from utils import config_manager


async  def main():

    client = MultiServerMCPClient(
        {
            "air_server":{
                # "command": "python",
                # "args": ["/home/mat/PycharmProjects/mcp-project/src/mcp_server/server.py"],
                # "transport":"stdio",
                "transport":"http",
                "url": "http://127.0.0.1:8000/mcp"
            }
        }
    )
    message_dict = {"messages": [("user", "what is weather in tehran?,also give me info about today pollution.")]}
    # message_dict = {"messages": [("user", "differents between Farsi and japanese.")]}

    tools =  await client.get_tools()
    agent = agentic_model(tools)
    # response = await agent.ainvoke({"messages": [("user", "what is weather in tehran?")]})
    # print(response)
    # async for chunk in agent.astream(message_dict):
    #     # Each chunk contains the full state at that point
    #     # latest_message = chunk["messages"][-1]
    #     # if latest_message.content:
    #     #     print(f"Agent: {latest_message.content}")
    #     # elif latest_message.tool_calls:
    #     #     print(f"Calling tools: {[tc['name'] for tc in latest_message.tool_calls]}")
    #     print("🔍 RAW CHUNK:", repr(chunk))

    async for chunk in agent.astream(message_dict):
        # chunk is like {'model': {...}} or {'tools': {...}}
        for node_name, node_data in chunk.items():
            messages = node_data.get("messages", [])
            if not messages:
                continue

            latest = messages[-1]

            if hasattr(latest, 'tool_calls') and latest.tool_calls:
                tool_names = [tc["name"] for tc in latest.tool_calls]
                print(f"🛠️  [{node_name}] Tool calls: {tool_names}")

            elif hasattr(latest, 'content') and latest.content:
                # Skip empty or metadata-only messages
                content = latest.content
                if isinstance(content, list):
                    # Handle multimodal content (e.g., text + image)
                    text_parts = [part.get("text", "") for part in content if isinstance(part, dict) and part.get("type") == "text"]
                    content = "".join(text_parts)
                if content.strip():
                    print(f"💬 [{node_name}] Agent: {content}")

            # Optional: print structured response if present
            if "structured_response" in node_data:
                resp = node_data["structured_response"]
                print(f"📦 Structured output: {resp}")

asyncio.run(main())
