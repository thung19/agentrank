CREATE TABLE mcp_servers (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    version TEXT NOT NULL,
    source TEXT NOT NULL DEFAULT 'official_registry',
    raw_metadata JSONB NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(name, version)
);

CREATE table tools (
    id BIGSERIAL PRIMARY KEY,
    server_id BIGINT NOT NULL
        REFERENCES mcp_servers(id)
        ON DELETE CASCADE,
    
    name TEXT NOT NULL,
    description TEXT,
    input_schema JSONB,
    output_schema JSONB,
    capability TEXT,
    raw_metadata JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(server_id, name)
);