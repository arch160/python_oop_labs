def by_name(book):
    """Сорт по названию"""
    return book.name.lower()

def by_year(book):
    """По году издания"""
    return book.year

def by_pages(book):
    """По кол-ву страниц"""
    return book.pages

def by_author(book):
    """По автору."""
    return book.writer.lower()

def by_name_then_year(book):
    """По названию, потом по году"""
    return (book.name.lower(), book.year)


def is_available(book):
    """доступна ли книга"""
    return book.is_available

def is_thick(book, threshold=500):
    """книга толстая"""
    return book.pages > threshold

def is_after_year(book, year=2000):
    """книга издана после 2000 года."""
    return book.year > year

def is_electronic(book):
    """электронная книга"""
    return isinstance(book, Ebook)  # Ebook будет импортирован

def is_audio(book):
    """аудиокнига"""
    return isinstance(book, AudioBook)


def to_short_string(book):
    """книга в строку"""
    return f"{book.name} – {book.writer} ({book.year})"

def apply_discount(book, percent=10):
    return f"{book.name} (скидка {percent}% на электронную версию)"


def make_year_filter(min_year, max_year=None):
    def filter_fn(book):
        if max_year is None:
            return book.year >= min_year
        else:
            return min_year <= book.year <= max_year
    return filter_fn


class DiscountStrategy:
    """Вычисляет скидку на книгу"""
    def __init__(self, percent=10):
        self.percent = percent

    def __call__(self, book):
        return f"{book.name} со скидкой {self.percent}%"

class ShowInfoStrategy:
    """Преобразует книгу в строку"""
    def __call__(self, book):
        return f"{book.name} ({book.year}) – {book.writer}"