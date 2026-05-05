from models import Book, Ebook, AudioBook
from collection import Library
from interfaces import Printable, Comparable

def print_all(things):
    """функция через интерфейс Printable"""
    for t in things:
        print(t.to_string())

def bubble_sort_by_comparable(lst):
    """сортировка через compare_to"""
    n = len(lst)
    for i in range(n):
        for j in range(n-1-i):
            if lst[j].compare_to(lst[j+1]) > 0:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def scenario1():
    print("=== сценарий 1: создание объектов и интерфейсные методы ===")
    b = Book("Война и мир", "Толстой", 1869, 1300)
    e = Ebook("1984", "Оруэлл", 1949, 328, 2.5, True)
    a = AudioBook("Мастер и Маргарита", "Булгаков", 1967, 480, 12.5, "Рыбников")

    print("to_string():")
    print(b.to_string())
    print(e.to_string())
    print(a.to_string())

    print("\ncompare_to (по году):")
    print(f"Война и мир vs 1984: {b.compare_to(e)}")
    print(f"1984 vs Мастер: {e.compare_to(a)}")
    print(f"Война и мир vs Война и мир: {b.compare_to(b)}")

def scenario2():
    print("\n=== сценарий 2: функция через Printable и isinstance ===")
    items = [
        Book("Детство", "Толстой", 1852, 150),
        Ebook("Улисс", "Джойс", 1922, 1056, 5.0),
        AudioBook("Тихий Дон", "Шолохов", 1928, 1500, 28.0, "Литвинов")
    ]
    print_all(items)

    print("\nisinstance проверки:")
    for item in items:
        print(f"{item.name}: Printable? {isinstance(item, Printable)}")
        print(f"{item.name}: Comparable? {isinstance(item, Comparable)}")

def scenario3():
    print("\n=== сценарий 3: коллекция, сортировка через Comparable, фильтрация ===")
    lib = Library()
    lib.add(Book("Анна Каренина", "Толстой", 1877, 864))
    lib.add(Ebook("Преступление и наказание", "Достоевский", 1866, 672, 3.2))
    lib.add(Book("Идиот", "Достоевский", 1869, 656))
    lib.add(AudioBook("Евгений Онегин", "Пушкин", 1833, 320, 8.0, "Иванов"))

    print("все книги (через to_string):")
    for book in lib:
        print(book.to_string())

    books_list = lib.get_all()
    sorted_books = bubble_sort_by_comparable(books_list)
    print("\nпосле сортировки по году (от старых к новым):")
    for b in sorted_books:
        print(f"{b.name} - {b.year}")


if __name__ == "__main__":
    scenario1()
    scenario2()
    scenario3()