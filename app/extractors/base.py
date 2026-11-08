from abc import ABC, abstractmethod
from pathlib import Path


class BaseExtractor(ABC):
    @abstractmethod
    def extract(self, path: Path) -> list[list[str]]:
        raise NotImplementedError
