import asyncio

from database.db import get_connection
from database.tools import upsert_tool
from mcp_client.inspect import inspect_server


async def main():
    server_id = 4
    url = "https://mcp.deepwiki.com/mcp"

    tools = await inspect_server(url)

    with get_connection() as conn:
        with conn.cursor() as cur:
            for tool in tools:
                tool_id = upsert_tool(
                    cur=cur,
                    server_id=server_id,
                    name=tool["name"],
                    description=tool["description"],
                    input_schema=tool["input_schema"],
                    output_schema=tool["output_schema"],
                    capability=None,
                    raw_metadata=tool["raw_metadata"]
                )

                print(tool_id, tool)


if __name__ == "__main__":
    asyncio.run(main())