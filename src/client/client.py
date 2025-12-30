# client/mcp_chat_client.py
import asyncio
from typing import AsyncGenerator, List, Tuple
from langchain_core.messages import BaseMessage
from langchain_mcp_adapters.client import MultiServerMCPClient
from agent import agentic_model


class MCPChatClient:
    def __init__(self, server_config: dict):
        self.server_config = server_config
        self.client = None
        self.agent = None

    async def initialize(self):
        """Initialize MCP client and agent once."""
        self.client = MultiServerMCPClient(self.server_config)
        tools = await self.client.get_tools()
        self.agent = agentic_model(tools)

    async def chat_stream(self, messages: List[Tuple[str, str]]) -> AsyncGenerator[str, None]:
        """
        Stream responses from the agent given a list of (role, content) messages.
        Yields either:
          - "💬 Agent: ..." (text response)
          - "🛠️ Tool calls: [...]" (tool invocation)
          - "📦 Structured output: {...}"
        """
        if self.agent is None:
            raise RuntimeError("Client not initialized. Call initialize() first.")

        input_dict = {"messages": messages}
        async for chunk in self.agent.astream(input_dict):
            for node_name, node_data in chunk.items():
                messages_out = node_data.get("messages", [])
                if not messages_out:
                    continue

                latest = messages_out[-1]
                output = ""

                if hasattr(latest, 'tool_calls') and latest.tool_calls:
                    tool_names = [tc["name"] for tc in latest.tool_calls]
                    output = f"🛠️ [{node_name}] Tool calls: {tool_names}"

                elif hasattr(latest, 'content') and latest.content:
                    content = latest.content
                    if isinstance(content, list):
                        text_parts = [part.get("text", "") for part in content if
                                      isinstance(part, dict) and part.get("type") == "text"]
                        content = "".join(text_parts)
                    if content.strip():
                        output = f"💬 [{node_name}] Agent: {content}"

                if output:
                    yield output

                if "structured_response" in node_data:
                    yield f"📦 Structured output: {node_data['structured_response']}"
