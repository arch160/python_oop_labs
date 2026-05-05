from models import Book, Ebook, AudioBook
from collection import AdvancedLibrary
from strategies import (
    by_name, by_year, by_pages, by_author,
    is_available, make_year_filter,
    DiscountStrategy, ShowInfoStrategy
)

def scenario1_chain():
    print("=== Сценарий 1: цепочка фильтрация -> сортировка -> применение ===")

    lib = AdvancedLibrary()
    lib.add(Book("Война и мир", "Толстой", 1869, 1300))
    lib.add(Book("1984", "Оруэлл", 1949, 328))
    lib.add(Ebook("Преступление и наказание", "Достоевский", 1866, 672, 3.2))
    lib.add(AudioBook("Мастер и Маргарита", "Булгаков", 1967, 480, 12.5, "Рыбников"))
    lib.add(Book("Детство", "Толстой", 1852, 150))
    lib.add(Ebook("Улисс", "Джойс", 1922, 1056, 5.0))

    print("Исходная коллекция:")
    print(lib)

    filtered = lib.filter_by(is_available)
    print("\n1. Оставляем только доступные книги:")
    print(filtered)

    filtered.sort_by(by_year)
    print("\n2. Сортируем по году (от старых к новым):")
    print(filtered)

    results = filtered.apply(DiscountStrategy(15))
    print("\n3. Применяем скидку 15% к каждой книге:")
    for r in results:
        print("  " + r)

def scenario2_different_keys():
    print("\n=== Сценарий 2: разные стратегии сортировки ===")

    lib = AdvancedLibrary()
    lib.add(Book("Анна Каренина", "Толстой", 1877, 864))
    lib.add(Book("Идиот", "Достоевский", 1869, 656))
    lib.add(Book("Евгений Онегин", "Пушкин", 1833, 320))
    lib.add(Book("1984", "Оруэлл", 1949, 328))

    print("По названию:")
    lib.sort_by(by_name)
    print(lib)

    print("\nПо году:")
    lib.sort_by(by_year)
    print(lib)

    print("\nПо числу страниц:")
    lib.sort_by(by_pages)
    print(lib)

def scenario3_callable_map_factory():
    print("\n=== Сценарий 3: callable-объекты, map, фабрика фильтров ===")

    lib = AdvancedLibrary()
    lib.add(Book("Дубровский", "Пушкин", 1841, 200))
    lib.add(Book("Мёртвые души", "Гоголь", 1842, 432))
    lib.add(Ebook("Гроза", "Островский", 1998, 400, 1.8))
    lib.add(AudioBook("Отцы и дети", "Толстой", 2013, 800, 26.0, "Иванова"))

    show_info = ShowInfoStrategy()
    print("ShowInfoStrategy:")
    for book in lib:
        print("  " + show_info(book))

    names = list(map(lambda b: b.name, lib))
    print("\nИмeна книг через map и lambda:", ", ".join(names))

    filter_after_1900 = make_year_filter(1900)
    modern = lib.filter_by(filter_after_1900)
    print("\nКниги после 1900 года:")
    print(modern if len(modern) > 0 else "  нет таких")

if __name__ == "__main__":
    scenario1_chain()
    scenario2_different_keys()
    scenario3_callable_map_factory()