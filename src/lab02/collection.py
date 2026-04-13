from model import Book

class Library:

    def __init__(self):
        self._books = []

    def add(self, book):
        if not isinstance(book, Book):
            raise TypeError("Можно добавлять только книги")
        if book in self._books:
            raise ValueError("Такая книга уже есть в библиотеке")
        self._books.append(book)

    def remove(self, book):
        if book not in self._books:
            raise ValueError("Книги нет в библиотеке")
        self._books.remove(book)

    def remove_at(self, index):
        if index < 0 or index >= len(self._books):
            raise IndexError("Неверный индекс")
        return self._books.pop(index)

    def get_all(self):
        return self._books.copy()

    def find_by_name(self, name):
        for book in self._books:
            if book.name.lower() == name.lower():
                return book
        return None

    def find_by_writer(self, writer):
        result = []
        for book in self._books:
            if book.writer.lower() == writer.lower():
                result.append(book)
        return result

    def __len__(self):
        return len(self._books)

    def __iter__(self):
        return iter(self._books)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self._books[index]
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом")
        if index < 0 or index >= len(self._books):
            raise IndexError("Индекс вне диапазона")
        return self._books[index]

    def sort(self, key=None, reverse=False):
        if key is None:
            self._books.sort(reverse=reverse)
        elif key == 'name':
            self._books.sort(key=lambda b: b.name.lower(), reverse=reverse)
        elif key == 'writer':
            self._books.sort(key=lambda b: b.writer.lower(), reverse=reverse)
        elif key == 'year':
            self._books.sort(key=lambda b: b.year, reverse=reverse)
        elif key == 'pages':
            self._books.sort(key=lambda b: b.pages, reverse=reverse)
        else:
            raise ValueError("Доступные ключи: name, writer, year, pages")

    def filter_available(self):
        new_lib = Library()
        for book in self._books:
            if book.is_available:
                new_lib.add(book)
        return new_lib

    def filter_by_year(self, year_from=None, year_to=None):
        new_lib = Library()
        for book in self._books:
            if year_from is not None and book.year < year_from:
                continue
            if year_to is not None and book.year > year_to:
                continue
            new_lib.add(book)
        return new_lib

    def __str__(self):
        if not self._books:
            return "Библиотека пуста"
        result = f"Всего книг: {len(self._books)}\n"
        for i, book in enumerate(self._books, 1):
            result += f"  {i}. {book}\n"
        return result.rstrip()