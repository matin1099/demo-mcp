# test_client.py
import asyncio
from src.client.client import MCPChatClient

async def test_single_turn():
    client = MCPChatClient({
        "air_server": {
            "transport": "http",
            "url": "http://127.0.0.1:8000/mcp"
        }
    })
    await client.initialize()

    messages = [("user", "What is the weather in Tehran?")]
    print("Sending:", messages[0][1])
    async for output in client.chat_stream(messages):
        print(output)

if __name__ == "__main__":
    asyncio.run(test_single_turn())