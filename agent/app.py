import asyncio
import json
import os

from agent.mcp_client import MCPClient
from agent.dial_client import DialClient
from agent.models.message import Message, Role


# https://mcp.deepwiki.com/mcp
# https://remote.mcpservers.org/fetch/mcp

async def main():
    mcp_client = MCPClient()

    #TODO:
    # 1. Connect to MCP server via `mcp_client`, mcp_server_url="http://localhost:8005/mcp"
    # 2. Get MCP tools and assign to `tools` variable
    # 3. Optional: Print tools to console
    #       for tool in tools: print(f"{json.dumps(tool, indent=2)}")
    # 4. Create DialClient:
    #       - api_key=os.getenv("DIAL_API_KEY")
    #       - endpoint="https://ai-proxy.lab.epam.com"
    #       - tools=tools
    #       - mcp_client=mcp_client
    # ---
    # 5. Optional:
    #   Try with different MCP Servers:
    #       - https://mcp.deepwiki.com/mcp
    #       - https://remote.mcpservers.org/fetch/mcp


    messages: list[Message] = [
        Message(
            role=Role.SYSTEM,
            content="You are an advanced AI agent. Your goal is to assist user with his questions."
        )
    ]

    print("MCP-based Agent is ready! Type your query or 'exit' to exit.")
    while True:
        user_input = input("\n> ").strip()
        if user_input.lower() == 'exit':
            break

        messages.append(
            Message(
                role=Role.USER,
                content=user_input
            )
        )

        ai_message: Message = await dial_client.get_completion(messages)
        messages.append(ai_message)


if __name__ == "__main__":
    asyncio.run(main())
