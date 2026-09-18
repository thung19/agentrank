from database.db import get_connection
from database.servers import upsert_server

server = {
    "name": "test-server",
    "version": "1.0.0",
    "raw_metadata": {
        "test": True
    }
}

with get_connection() as conn:
    with conn.cursor() as cur:
        server_id = upsert_server(
            cur,
            server["name"],
            server["version"],
            server["raw_metadata"]
        )

print("upserted server", server_id)