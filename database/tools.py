from psycopg.types.json import Jsonb


def upsert_tool(
    cur,
    server_id,
    name,
    description=None,
    input_schema=None,
    output_schema=None,
    capability=None,
    raw_metadata=None
):
    cur.execute(
        """
        INSERT INTO tools (
            server_id,
            name,
            description,
            input_schema,
            output_schema,
            capability,
            raw_metadata
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)

        ON CONFLICT (server_id, name)
        DO UPDATE SET
            description = EXCLUDED.description,
            input_schema = EXCLUDED.input_schema,
            output_schema = EXCLUDED.output_schema,
            capability = EXCLUDED.capability,
            raw_metadata = EXCLUDED.raw_metadata,
            updated_at = NOW()

        RETURNING id
        """,
        (
            server_id,
            name,
            description,
            Jsonb(input_schema) if input_schema is not None else None,
            Jsonb(output_schema) if output_schema is not None else None,
            capability,
            Jsonb(raw_metadata) if raw_metadata is not None else None
        )
    )

    return cur.fetchone()[0]