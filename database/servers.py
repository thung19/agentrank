from psycopg.types.json import Jsonb


def upsert_server(cur, name, version, raw_metadata):
    cur.execute(
        """
        INSERT INTO mcp_servers (
            name,
            version,
            raw_metadata
        )
        VALUES (%s, %s, %s)

        ON CONFLICT (name, version)
        DO UPDATE SET
            raw_metadata = EXCLUDED.raw_metadata,
            updated_at = NOW()
        RETURNING id
        """,
        (name, version, Jsonb(raw_metadata))
    )

    return cur.fetchone()[0]