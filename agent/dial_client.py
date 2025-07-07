import json
from collections import defaultdict
from typing import Any

from openai import AsyncAzureOpenAI

from agent.models.message import Message, Role
from agent.mcp_client import MCPClient


class DialClient:
    """Handles AI model interactions and integrates with MCP client"""

    def __init__(self, api_key: str, endpoint: str, tools: list[dict[str, Any]], mcp_client: MCPClient):
        self.tools = tools
        self.mcp_client = mcp_client
        self.openai = AsyncAzureOpenAI(
            api_key=api_key,
            azure_endpoint=endpoint,
            api_version="2025-01-01-preview"
        )

    def _collect_tool_calls(self, tool_deltas):
        """Convert streaming tool call deltas to complete tool calls"""
        tool_dict = defaultdict(lambda: {"id": None, "function": {"arguments": "", "name": None}, "type": None})

        for delta in tool_deltas:
            idx = delta.index
            if delta.id: tool_dict[idx]["id"] = delta.id
            if delta.function.name: tool_dict[idx]["function"]["name"] = delta.function.name
            if delta.function.arguments: tool_dict[idx]["function"]["arguments"] += delta.function.arguments
            if delta.type: tool_dict[idx]["type"] = delta.type

        return list(tool_dict.values())

    async def _stream_response(self, messages: list[Message]) -> Message:
        """Stream OpenAI response and handle tool calls"""
        stream = await self.openai.chat.completions.create(
            **{
                "model": "gpt-4o",
                "messages": [msg.to_dict() for msg in messages],
                "tools": self.tools,
                "temperature": 0.0,
                "stream": True
            }
        )

        content = ""
        tool_deltas = []

        print("🤖: ", end="", flush=True)

        async for chunk in stream:
            delta = chunk.choices[0].delta

            # Stream content
            if delta.content:
                print(delta.content, end="", flush=True)
                content += delta.content

            if delta.tool_calls:
                tool_deltas.extend(delta.tool_calls)

        print()
        return Message(
            role=Role.AI,
            content=content,
            tool_calls=self._collect_tool_calls(tool_deltas) if tool_deltas else []
        )

    async def get_completion(self, messages: list[Message]) -> Message:
        """Process user query with streaming and tool calling"""
        ai_message: Message = await self._stream_response(messages)

        # Check if any tool calls are present and perform them
        if ai_message.tool_calls:
            messages.append(ai_message)
            await self._call_tools(ai_message, messages)
            # recursively calling agent with tool messages
            return await self.get_completion(messages)

        return ai_message

    async def _call_tools(self, ai_message: Message, messages: list[Message]):
        """Execute tool calls using MCP client"""
        for tool_call in ai_message.tool_calls:
            tool_name = tool_call["function"]["name"]
            tool_args = json.loads(tool_call["function"]["arguments"])

            try:
                #TODO:
                # 1. Call `await self.mcp_client.call_tool(tool_name, tool_args)` and assign to `tool_result`
                # 2. Create Message with:
                #   - role=Role.TOOL
                #   - content=str(tool_result)
                #   - tool_call_id=tool_call["id"]
                # 3. Append created message to `messages`

            except Exception as e:
                error_msg = f"Error: {e}"
                print(f"Error: {error_msg}")
                messages.append(
                    Message(
                        role=Role.TOOL,
                        content=error_msg,
                        tool_call_id=tool_call["id"],
                    )
                )