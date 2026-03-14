def validate_title(title: str) -> None:
    """
    Проверяет корректность названия книги.
    
    Args:
        title: название книги
        
    Raises:
        TypeError: если название не строка
        ValueError: если название пустое или состоит из пробелов
    """
    if not isinstance(title, str):
        raise TypeError("Название должно быть строкой")
    if not title or title.isspace():
        raise ValueError("Название не может быть пустым")


def validate_author(author: str) -> None:
    """
    Проверяет корректность имени автора.
    
    Args:
        author: автор книги
        
    Raises:
        TypeError: если автор не строка
        ValueError: если автор пустой или состоит из пробелов
    """
    if not isinstance(author, str):
        raise TypeError("Автор должен быть строкой")
    if not author or author.isspace():
        raise ValueError("Автор не может быть пустым")


def validate_year(year: int) -> None:
    """
    Проверяет корректность года издания.
    
    Args:
        year: год издания
        
    Raises:
        TypeError: если год не целое число
        ValueError: если год вне допустимого диапазона
    """
    if not isinstance(year, int):
        raise TypeError("Год издания должен быть целым числом")
    if year < 1450:  # Первая печатная книга
        raise ValueError("Год издания не может быть раньше 1450")
    if year > 2026:  # Текущий год + небольшой запас
        raise ValueError("Год издания не может быть в будущем")


def validate_pages(pages: int) -> None:
    """
    Проверяет корректность количества страниц.
    
    Args:
        pages: количество страниц
        
    Raises:
        TypeError: если количество страниц не целое число
        ValueError: если количество страниц <= 0
    """
    if not isinstance(pages, int):
        raise TypeError("Количество страниц должно быть целым числом")
    if pages <= 0:
        raise ValueError("Количество страниц должно быть положительным числом")