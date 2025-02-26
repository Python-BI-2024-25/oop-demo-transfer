from abc import ABC, abstractmethod
from typing import List

from src.data_types import UserData


class AbstractSource(ABC):
    @abstractmethod
    def read_data(self) -> List[UserData]:
        raise NotImplementedError

    @abstractmethod
    def __enter__(self):
        raise NotImplementedError

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError


class AbstractDestination(ABC):
    @abstractmethod
    def write_data(self, data_lst: List[UserData]):
        raise NotImplementedError

    @abstractmethod
    def __enter__(self):
        raise NotImplementedError

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError
