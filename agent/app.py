import asyncio
import json
import os

from agent.mcp_client import MCPClient
from agent.dial_client import DialClient
from agent.models.message import Message, Role


async def main():
    #TODO:
    # 1. Create MCP client and open connection to the MCP server (use `async with {YOUR_MCP_CLIENT} as client`),
    #    mcp_server_url="http://localhost:8005/mcp"
    # 2. Get MCP tools and assign to `tools` variable
    # 3. Optional: Print tools to console
    # 4. Create DialClient:
    #       - api_key=os.getenv("DIAL_API_KEY")
    #       - endpoint="https://ai-proxy.lab.epam.com"
    #       - tools=tools
    #       - mcp_client=mcp_client
    # 5. Create list with messages and add there SYSTEM message with instructions to LLM
    # 6. Create console chat (infinite loop + ability to exit from chat + preserve message history after the call to dial client)
    # ---
    # 7. Optional:
    #   Try with different MCP Servers:
    #       - https://mcp.deepwiki.com/mcp
    #       - https://remote.mcpservers.org/fetch/mcp (can scrap some info from the WEB)


if __name__ == "__main__":
    asyncio.run(main())
