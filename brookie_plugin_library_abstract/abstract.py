from __future__ import annotations

from abc import ABC, abstractmethod
from io import BytesIO
from typing import BinaryIO, Iterator


class Library(ABC):
    @abstractmethod
    async def __aenter__(self) -> Library:
        ...

    @abstractmethod
    async def __aexit__(self) -> None:
        ...

    @abstractmethod
    async def get_book_cover(self, id_: int) -> BinaryIO:
        ...

    @abstractmethod
    async def get_book_pages(self, id_: int, sort=True) -> Iterator[str]:
        ...

    @abstractmethod
    async def get_book_page(self, book_id: int, page_id: int) -> BytesIO:
        ...
