from typing import Optional, Any

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from mcp.types import CallToolResult, TextContent


class MCPClient:
    """Handles MCP server connection and tool execution"""

    def __init__(self, mcp_server_url: str) -> None:
        self.mcp_server_url = mcp_server_url
        self.session: Optional[ClientSession] = None
        self._streams_context = None
        self._session_context = None

    async def __aenter__(self):
        self._streams_context = streamablehttp_client(self.mcp_server_url)
        read_stream, write_stream, _ = await self._streams_context.__aenter__()

        self._session_context = ClientSession(read_stream, write_stream)
        self.session = await self._session_context.__aenter__()

        await self.session.initialize()

        if not await self.session.send_ping():
            raise ValueError("MCP server connection failed")

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session and self._session_context:
            await self._session_context.__aexit__(exc_type, exc_val, exc_tb)
        if self._streams_context:
            await self._streams_context.__aexit__(exc_type, exc_val, exc_tb)

    async def get_tools(self) -> list[dict[str, Any]]:
        """Get available tools from MCP server"""
        if not self.session:
            raise RuntimeError("MCP client not connected. Call connect() first.")

        tools = await self.session.list_tools()
        return [
            {
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": tool.inputSchema
                }
            }
            for tool in tools.tools
        ]

    async def call_tool(self, tool_name: str, tool_args: dict[str, Any]) -> Any:
        """Call a specific tool on the MCP server"""
        if not self.session:
            raise RuntimeError("MCP client not connected. Call connect() first.")

        print(f"    Calling `{tool_name}` with {tool_args}")

        tool_result: CallToolResult = await self.session.call_tool(tool_name, tool_args)
        content = tool_result.content[0]

        print(f"    ⚙️: {content}\n")

        if isinstance(content, TextContent):
            return content.text

        return content

