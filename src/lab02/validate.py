def validate_name(name: str) -> None:
    if not isinstance(name, str):
        raise TypeError("Название должно быть строкой")
    if not name or name.isspace():
        raise ValueError("Название не может быть пустым")


def validate_writer(writer: str) -> None:
    if not isinstance(writer, str):
        raise TypeError("Автор должен быть строкой")
    if not writer or writer.isspace():
        raise ValueError("Автор не может быть пустым")


def validate_year(year: int) -> None:
    if not isinstance(year, int):
        raise TypeError("Год издания должен быть целым числом")
    if year < 1450: 
        raise ValueError("Год издания не может быть раньше 1450")
    if year > 2026: 
        raise ValueError("Год издания не может быть в будущем")


def validate_pages(pages: int) -> None:
    if not isinstance(pages, int):
        raise TypeError("Количество страниц должно быть целым числом")
    if pages <= 0:
        raise ValueError("Количество страниц должно быть положительным числом")