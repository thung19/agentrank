import requests


REGISTRY_URL = "https://registry.modelcontextprotocol.io/v0.1/servers"


def normalize_server(server):
    return {
        "name": server["server"]["name"],
        "version": server["server"]["version"],
        "raw_metadata": server
    }


def fetch_servers(limit=10):
    response = requests.get(
        REGISTRY_URL,
        params={"limit": limit},
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    servers = []

    for server in data["servers"]:
        normalized = normalize_server(server)
        servers.append(normalized)

    return servers