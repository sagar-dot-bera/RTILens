from pathlib import Path

from app.extractors.base import BaseExtractor


class PdfPlumberExtractor(BaseExtractor):
    def extract(self, path: Path) -> list[list[str]]:
        if not path.exists():
            raise FileNotFoundError(path)
        return []
