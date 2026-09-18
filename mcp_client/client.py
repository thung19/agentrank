from mcp import Client


async def list_remote_tools(url):
    async with Client(url) as client:
        result = await client.list_tools()
        return result.tools