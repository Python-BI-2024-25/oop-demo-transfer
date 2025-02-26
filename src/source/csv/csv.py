from typing import List, Optional, TextIO

from src.abstracts import AbstractSource
from src.data_types import UserData
from src.settings import CSV_SOURCE_PATH


class CSVSource(AbstractSource):
    def __init__(self):
        self._csv_file: Optional[TextIO] = None

    def read_data(self) -> List[UserData]:
        res = []
        self._csv_file.readline()
        for line in self._csv_file:
            name, email, sex = line.strip().split(",")
            res.append(UserData(source="csv", name=name, email=email, sex=sex))
        return res

    def __enter__(self):
        self._csv_file = open(CSV_SOURCE_PATH)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._csv_file.close()
