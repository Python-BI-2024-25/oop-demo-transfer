from src import settings
from src.abstracts import AbstractDestination, AbstractSource
from src.destination.postgres.postres import PostgresDestination
from src.source.csv.csv import CSVSource


class TransferFactory:
    def __init__(self):
        self._src = settings.SOURCE
        self._dest = settings.DESTINATION

    @property
    def src(self) -> AbstractSource:
        if self._src == "csv":
            return CSVSource()
        if ...:
            return ...
        if ...:
            return ...
        raise ValueError

    @property
    def dest(self) -> AbstractDestination:
        if self._dest == "postgres":
            return PostgresDestination()
        if ...:
            return ...
        if ...:
            return ...
        raise ValueError
