from base import Book
from models import Ebook, AudioBook
from collection import Library

def scenario_basic():
    print("=== СЦЕНАРИЙ 1: Базовое наследование ===")
    print()

    b = Book("Война и мир", "Лев Толстой", 1869, 1300)
    e = Ebook("1984", "Джордж Оруэлл", 1949, 328, file_size_mb=2.5, drm_protected=True)
    a = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 480,
                  duration_hours=12.5, narrator="Алексей Рыбников")

    print(b)
    print(e)
    print(a)

    print("\n--- Методы дочерних классов ---")
    print(e.download())
    print(a.listen_preview())

    print("\n--- Метод базового класса ---")
    e.issue_book()
    print(e.download())   # щас недоступна она
    e.return_book()

def scenario_polymorphism():
    print("\n=== СЦЕНАРИЙ 2: Полиморфизм и коллекция ===")
    print()

    lib = Library()
    items = [
        Book("Детство", "Лев Толстой", 1852, 150),
        Ebook("Улисс", "Джеймс Джойс", 1922, 1056, file_size_mb=5.0),
        AudioBook("Тихий Дон", "Михаил Шолохов", 1928, 1500,
                  duration_hours=28.0, narrator="Иван Литвинов")
    ]
    for item in items:
        lib.add(item)

    print("Все книги в библиотеке:")
    for book in lib:
        print(f"  {book}")

    print("\n--- Полиморфный вызов process() ---")
    for book in lib:
        if hasattr(book, 'process'):
            print(f"{book.name}: {book.process()}")
        else:
            print(f"{book.name}: нет метода process")

    print("\n--- Проверка типов через isinstance ---")
    for book in lib:
        if isinstance(book, Ebook):
            print(f"Электронная: {book.name}")
        elif isinstance(book, AudioBook):
            print(f"Аудиокнига: {book.name}")
        else:
            print(f"Обычная: {book.name}")

def scenario_filter():
    print("\n=== СЦЕНАРИЙ 3: Фильтрация по типу ===")
    print()

    lib = Library()
    lib.add(Book("Евгений Онегин", "Пушкин", 1833, 320))
    lib.add(Ebook("Преступление и наказание", "Достоевский", 1866, 672, file_size_mb=3.2))
    lib.add(AudioBook("Анна Каренина", "Толстой", 1877, 864,
                      duration_hours=18.0, narrator="Татьяна Бабичева"))
    lib.add(Ebook("Маленький принц", "Экзюпери", 1943, 96, file_size_mb=1.2))

    def filter_by_type(collection, cls):
        result = Library()
        for item in collection:
            if isinstance(item, cls):
                result.add(item)
        return result

    ebooks = filter_by_type(lib, Ebook)
    audiobooks = filter_by_type(lib, AudioBook)

    print("Только электронные книги:")
    for b in ebooks:
        print(f"  {b.name} ({b.file_size_mb} МБ)")

    print("\nТолько аудиокниги:")
    for b in audiobooks:
        print(f"  {b.name} ({b.duration_hours} ч.)")

def main():
    scenario_basic()
    scenario_polymorphism()
    scenario_filter()

if __name__ == "__main__":
    main()