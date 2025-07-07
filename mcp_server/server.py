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
def web_search(args: WebSearchRequest) -> str:
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
        ]
    }

    endpoint = DIAL_ENDPOINT.format(model="gemini-2.0-flash-exp-google-search")
    response = requests.post(url=endpoint, headers=headers, json=request_data)

    if response.status_code == 200:
        data = response.json()
        if "error" in data:
            return data["error"]
        return data["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} {response.text}"


class Operation(StrEnum):
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"


class CalculatorRequest(BaseModel):
    num1: float = Field(description="The first number for the calculation")
    num2: float = Field(description="The second number for the calculation")
    operation: Operation = Field(description="The mathematical operation to perform (add, subtract, multiply, or divide)")


#TODO: Add decorator `@mcp.tool()`
async def simple_calculator(args: CalculatorRequest) -> str:
    """Execute basic calculator operation (one per request)"""
    if args.operation == Operation.ADD:
        result = args.num1 + args.num2
    elif args.operation == Operation.SUBTRACT:
        result = args.num1 - args.num2
    elif args.operation == Operation.MULTIPLY:
        result = args.num1 * args.num2
    elif args.operation == Operation.DIVIDE:
        if args.num2 == 0:
            return "Error: Division by zero"
        result = args.num1 / args.num2
    return f"Result: {result}"


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http"
    )