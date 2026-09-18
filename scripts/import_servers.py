from database.servers import upsert_server
from importer.registry import fetch_servers
from database.db import get_connection


servers = fetch_servers(limit=10)

with get_connection() as conn:
    with conn.cursor() as cur:
        for server in servers:
            server_id = upsert_server(
                cur,
                server["name"],
                server["version"],
                server["raw_metadata"]
            )

            print(server_id, server["name"])

print(f"Imported {len(servers)} servers")