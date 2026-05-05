from models import Book
from interfaces import Printable

class Library:
    def __init__(self):
        self._books = []

    def add(self, book):
        if not isinstance(book, Book):
            raise TypeError("только книги")
        if book in self._books:
            raise ValueError("уже есть такая")
        self._books.append(book)

    def remove(self, book):
        if book not in self._books:
            raise ValueError("нет такой")
        self._books.remove(book)

    def get_all(self):
        return self._books.copy()

    def find_by_name(self, name):
        for b in self._books:
            if b.name.lower() == name.lower():
                return b
        return None

    def __len__(self):
        return len(self._books)

    def __iter__(self):
        return iter(self._books)

    def __getitem__(self, idx):
        return self._books[idx]

    def get_printable(self):
        res = Library()
        for b in self._books:
            if isinstance(b, Printable):
                res.add(b)
        return res