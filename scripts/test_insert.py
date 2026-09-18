from database.servers import upsert_server

server = {
    "name": "test-server",
    "version": "1.0.0",
    "raw_metadata": {
        "test": True
    }
}

upsert_server(
    server["name"],
    server["version"],
    server["raw_metadata"]
)

print("upserted server")