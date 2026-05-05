from models import Book

class Library:
    def __init__(self):
        self._items = []

    def add(self, item):
        if not isinstance(item, Book):
            raise TypeError("только книги")
        if item in self._items:
            raise ValueError("уже есть")
        self._items.append(item)

    def remove(self, item):
        if item not in self._items:
            raise ValueError("нет такой")
        self._items.remove(item)

    def get_all(self):
        return self._items.copy()

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, idx):
        return self._items[idx]

    def __str__(self):
        if not self._items:
            return "Библиотека пуста"
        res = f"Библиотека (всего: {len(self._items)})\n"
        for i, b in enumerate(self._items, 1):
            res += f"{i}. {b}\n"
        return res

class AdvancedLibrary(Library):
    def sort_by(self, key_func, reverse=False):
        self._items.sort(key=key_func, reverse=reverse)
        return self

    def filter_by(self, predicate):
        new_lib = AdvancedLibrary()
        for book in self._items:
            if predicate(book):
                new_lib.add(book)
        return new_lib

    def apply(self, func):
        results = []
        for book in self._items:
            results.append(func(book))
        return results