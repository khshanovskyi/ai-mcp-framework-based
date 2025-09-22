# Framework-based MCP (Server & Client)
Python implementation for building Users Management Agent with MCP tools and MCP server

## 🎯 Task Overview

Create and run MCP server with simple tools. Implement simple Users Management Agent with MCP Client that will use MCP tools from created server.

## 🎓 Learning Goals

By exploring and working with this project, you will learn:

- How to configure simple MCP server
- How to configure client and connect to MCP server
- How to create simple Agent with tools from MCP server
- Key features of MCP

## 🏗️ Architecture

```
task/
├── agent/
│   ├── models/           
│   │   ├── message.py        ✅ Complete
│   ├── app.py                🚧 TODO: implement logic
│   ├── dial_client.py        🚧 TODO: implement logic
│   └── mcp_cleint.py         🚧 TODO: implement logic
└── mcp_server/               
    ├── server.py             🚧 TODO: implement logic
    ├── user_client.py        ✅ Complete
    ├── Dockerfile            ✅ Complete
    └── docker-compose.yml    ✅ Complete
```
# <img src="flow.png">

## 📋 Requirements

- **Python**: 3.11 or higher
- **Dependencies**: Listed in `requirements.txt`
- **API Access**: DIAL API key with appropriate permissions
- **Network**: EPAM VPN connection for internal API access
- Docker and Docker Compose
- Postman

## ✍️ Tasks:
You need to implement the Users Management Agent, that will be able to perform CRUD operations within User Management Service.

### Create and run MCP server:
1. Run [root docker-compose](docker-compose.yml) (Optional step in case if you have it from previous tasks)
2. Open [mcp_server](mcp_server/server.py)
3. Implement all ***TODO***
4. Run this MCP server in [root docker-compose](mcp_server/docker-compose.yml):
    ```bash
    cd ./mcp_server/
    ```
    ```bash
    docker compose up -d
    ```
5. Verify that it is up:
    ```bash
    docker compose ps -a
    ```

### OPTIONAL: Work with MCP server in Postman
1. Import [mcp.postman_collection](mcp.postman_collection.json) to Postman
2. Make `init` call and get `mcp-session-id` in response headers
3. Make `init-notification`. Pay attention that you need to use `mcp-session-id` retrieved from `init` request. it should return 202 status
4. Get tools (don't forget about `mcp-session-id`). It should return stream with tools.
5. Call calculator (don't forget about `mcp-session-id`). It should return stream tool execution result.


### Create and run Agent:
1. Open [mcp_client](agent/mcp_client.py) and implement all ***TODO***
2. Open [dial_client](agent/dial_client.py) and implement all ***TODO***
3. Open [prompts](agent/prompts.py) and write System prompt
4. Open [app](agent/app.py) and implement all ***TODO***
5. Run application [mcp_client](agent/app.py) and test that it is connecting to MCP Server and works properly
6. Try with your solution with `fetch MCP` `https://remote.mcpservers.org/fetch/mcp` and check the differences on the `init` step (what they have and don't)

### OPTIONAL: Support both (users-management and fetch) MCP servers:
1. Remember that we have 1-to-1 connection between MCP client and MCP server!
2. You need to think of the way how to change current flow to support tools from different MCP servers and implement it
3. In the end you should have the Agent that is able to fetch the info from the WEB about some people and save it to Users Service
4. Hint: the problem place is [dial_client](agent/dial_client.py)

---
# <img src="dialx-banner.png">