from mcp_client.client import list_remote_tools
from mcp_client.normalize import normalize_tool


async def inspect_server(url):
    tools = await list_remote_tools(url)

    normalized = []

    for tool in tools:
        normalized.append(
            normalize_tool(tool)
        )

    return normalized