Class abstract & utils from brooky library plugin

# Implements

    from brookie_plugin_library_abstract import Library
    from brookie_plugin_library_abstract.util import Archive

    class MyLibraryPlugin(Library):
        ...
        async def __aenter__(self) -> Calibre:
            ...
            return self

        async def __aexit__(self) -> None:
            ...

        async def get_book_cover(self, book_id: int) -> BinaryIO:
            ...

        async def get_book_pages(self, book_id: int) -> AsyncGenerator[str, None]:
            ...

        async def get_book_page(self, book_id: int, page_id: int) -> BytesIO:
            ...

# Exports
Name your project `brookie_plugin_library_${MY_PLUGIN_NAME}`, and ensure that `MyLibraryPlugin` is available in the `__init__.py` at its root.
