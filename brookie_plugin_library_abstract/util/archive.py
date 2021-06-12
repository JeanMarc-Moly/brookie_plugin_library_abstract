from contextlib import contextmanager
from io import BytesIO
from typing import BinaryIO, Iterator

from libarchive import SeekableArchive


class Archive:
    @classmethod
    def get_book_pages(cls, archive: BinaryIO, sort=True) -> Iterator[str]:
        with cls.get_archive(archive) as a:
            yield from cls._get_book_pages(a, sort)

    @classmethod
    def get_book_page(cls, archive: BinaryIO, page_id: int) -> BytesIO:
        with cls.get_archive(archive) as a:
            return cls._get_book_page(a, page_id)

    @classmethod
    def _get_book_page(cls, archive: SeekableArchive, page_id: int) -> BytesIO:
        count = page_id
        for p in cls._get_book_pages(archive):
            if not count:
                page = p
                break
            count -= 1
        else:
            raise KeyError(page_id)

        return BytesIO(archive.read(page))

    @staticmethod
    def _get_book_pages(archive: SeekableArchive, sort=True) -> Iterator[str]:
        pages = (e.pathname for e in archive)
        if sort:
            pages = sorted(pages)
        yield from pages

    @staticmethod
    @contextmanager
    def get_archive(archive: BinaryIO) -> SeekableArchive:
        with archive as b, SeekableArchive(b) as a:
            yield a
