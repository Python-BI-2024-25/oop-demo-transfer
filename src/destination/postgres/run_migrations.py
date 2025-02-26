from os import listdir, path

import psycopg2

from src import settings

path_to_migrations = path.abspath(path.join(path.dirname(__file__), "migrations"))
migration_files = [path.join(path_to_migrations, f) for f in listdir(path_to_migrations)]

sql_queries = []
for file in migration_files:
    with open(file) as f:
        sql_queries.append(f.read())

with psycopg2.connect(
    host=settings.POSTGRES_DESTINATION_CREDS["host"],
    database=settings.POSTGRES_DESTINATION_CREDS["dbname"],
    user=settings.POSTGRES_DESTINATION_CREDS["user"],
    password=settings.POSTGRES_DESTINATION_CREDS["password"],
    port=settings.POSTGRES_DESTINATION_CREDS["port"],
) as conn:
    with conn.cursor() as cur:
        for sql in sql_queries:
            cur.execute(sql)
    conn.commit()
