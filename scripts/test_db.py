from database.db import get_connection

with get_connection() as conn:
    with conn.cursor() as cur:
        cur.execute("""
            SELECT
                current_database(),
                current_user,
                version();
        """)
        result = cur.fetchone()
        print(result)