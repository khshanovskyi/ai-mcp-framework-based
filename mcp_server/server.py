import os
from enum import StrEnum

import requests
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field

#TODO:
# Create FastMCP object:
#   - name="test-mcp-server",
#   - host="0.0.0.0",
#   - port=8005,
#   - log_level="DEBUG"
mcp: FastMCP = None

# Constants
DIAL_ENDPOINT = os.getenv("DIAL_ENDPOINT", "https://ai-proxy.lab.epam.com") + "/openai/deployments/{model}/chat/completions"
DIAL_API_KEY = os.getenv("DIAL_API_KEY")


class WebSearchRequest(BaseModel):
    request: str = Field(description="The search query or question to search for on the web")


#TODO: Add decorator `@mcp.tool()`
async def web_search(args: WebSearchRequest) -> str:
    """Performs WEB search"""

    headers = {
        "api-key": DIAL_API_KEY,
        "Content-Type": "application/json"
    }
    request_data = {
        "messages": [
            {
                "role": "user",
                "content": args.request
            }
        ],
        "tools": [
            {
                "type": "static_function",
                "static_function": {
                    "name": "google_search",
                    "description": "Grounding with Google Search",
                    "configuration": {}
                }
            }
        ]
    }

    endpoint = DIAL_ENDPOINT.format(model="gemini-2.5-pro")
    response = requests.post(url=endpoint, headers=headers, json=request_data)

    if response.status_code == 200:
        data = response.json()
        if "error" in data:
            return data["error"]
        return data["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} {response.text}"

#TODO:
# Add `simple_calculator` - calculator tool that performs basic calculations (add, subtract, multiply, divide).
# Hint 1: Take a look at how the `web_search` is implemented
# Hint 2: Use Pydentic models to create `CalculatorRequest` with arguments that your mcp tool applies. With this Pydentic
#         model you will be able to provide arguments descriptions (they are crucial for LLM).
# Hint 3: Don't forget about decorator^)


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http"
    )