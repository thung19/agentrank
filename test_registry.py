import requests
import json

def normalize_server(server):
    return {
        "name": server["server"]["name"],
        "version": server["server"]["version"],
        "raw_metadata": server
    }

url = "https://registry.modelcontextprotocol.io/v0.1/servers"

response = requests.get(
    url,
    params={"limit": 10}
)

response.raise_for_status()

data = response.json()

servers = []


for server in data["servers"]:
    normalized = normalize_server(server)
    servers.append(normalized)


print(json.dumps(servers, indent=2))