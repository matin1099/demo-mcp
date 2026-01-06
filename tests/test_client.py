# test_client.py
import asyncio
from src.client.client import MCPChatClient

async def test_single_turn(human_massage):
    client = MCPChatClient({
        "air_server": {
            "transport": "http",
            "url": "http://127.0.0.1:8000/mcp"
        }
    })
    await client.initialize()

    messages = [("user",human_massage )]
    print("Sending:", messages[0][1])
    async for output in client.chat_stream(messages):
        print(output)

if __name__ == "__main__":
    # human_msg = "What is the weather in Tehran?"
    # asyncio.run(test_single_turn(human_msg))
    # human_msg = "tell me about air quality of tehran."
    # asyncio.run(test_single_turn(human_msg))
    human_msg = "give me a integer random number between 1 and 10."
    asyncio.run(test_single_turn(human_msg))
    human_msg = "give me a float random number between 20 and 30."
    asyncio.run(test_single_turn(human_msg))
    human_msg = "give me 5 integer random number between 20 and 50."
    asyncio.run(test_single_turn(human_msg))