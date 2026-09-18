from database.db import get_connection
from database.tools import upsert_tool


with get_connection() as conn:
    with conn.cursor() as cur:

        tool_id = upsert_tool(
            cur=cur,
            server_id=1,
            name="search_filings",
            description="Search SEC filings for a company",
            input_schema={
                "type": "object",
                "properties": {
                    "ticker": {
                        "type": "string"
                    }
                },
                "required": ["ticker"]
            },
            output_schema=None,
            capability=None
        )

        print("Tool ID:", tool_id)