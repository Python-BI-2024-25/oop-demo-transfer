from typing import List

import psycopg2
from psycopg2.extras import execute_values

from src import settings
from src.abstracts import AbstractDestination
from src.data_types import UserData


class PostgresDestination(AbstractDestination):
    def __init__(self):
        self._conn = None
        self._cur = None

    def write_data(self, data_lst: List[UserData]):
        execute_values(
            cur=self._cur,
            sql="INSERT INTO user_info (source, name, email, sex) VALUES %s",
            argslist=[data.to_tuple() for data in data_lst],
        )

    def __enter__(self):
        self._conn = psycopg2.connect(
            host=settings.POSTGRES_DESTINATION_CREDS["host"],
            database=settings.POSTGRES_DESTINATION_CREDS["dbname"],
            user=settings.POSTGRES_DESTINATION_CREDS["user"],
            password=settings.POSTGRES_DESTINATION_CREDS["password"],
            port=settings.POSTGRES_DESTINATION_CREDS["port"],
        )
        self._conn.autocommit = True
        self._cur = self._conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cur.close()
        self._conn.close()
