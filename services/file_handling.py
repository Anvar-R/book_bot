import logging
import os

logger = logging.getLogger(__name__)


# Функция, возвращающая строку с текстом страницы и её размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    
    # ...
    

    return page_text, page_size


# Функция, формирующая словарь книги
def prepare_book(path: str, page_size: int = 1050) -> dict[int, str]:
    book = {}

    # ...

    return book