from model import Book
from collection import Library

def scenario_1_basic():
    print("=== СЦЕНАРИЙ 1: Добавление, удаление, типы ===\n")

    lib = Library()
    b1 = Book("Война и мир", "Лев Толстой", 1869, 1300)
    b2 = Book("Преступление и наказание", "Фёдор Достоевский", 1866, 672)
    b3 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967, 480)

    lib.add(b1)
    lib.add(b2)
    lib.add(b3)

    print("После добавления трёх книг:")
    print(lib)

    lib.remove(b2)
    print("\nПосле удаления 'Преступление и наказание':")
    print(lib)

    try:
        lib.add(b1)
    except ValueError as e:
        print(f"\nОшибка при дубликате: {e}")

    try:
        lib.add("не книга")
    except TypeError as e:
        print(f"Ошибка типа: {e}")

def scenario_2_search_iter_len():
    print("\n=== СЦЕНАРИЙ 2: Поиск, длина, итерация, индексация ===\n")

    lib = Library()
    books = [
        Book("1984", "Джордж Оруэлл", 1949, 328),
        Book("Улисс", "Джеймс Джойс", 1922, 1056),
        Book("Маленький принц", "Антуан де Сент-Экзюпери", 1943, 96),
        Book("Анна Каренина", "Лев Толстой", 1877, 864)
    ]
    for b in books:
        lib.add(b)

    print("Поиск по названию '1984':")
    found = lib.find_by_name("1984")
    print(f"  {found}")

    print("\nПоиск по автору 'Толстой':")
    for b in lib.find_by_writer("Толстой"):
        print(f"  {b.name} ({b.year})")

    print(f"\nВсего книг: {len(lib)}")

    print("\nПеребор через for:")
    for book in lib:
        print(f"  {book.name} — {book.writer}")

    print(f"\nПервая книга: {lib[0].name}")
    print(f"Срез [1:3]: {[b.name for b in lib[1:3]]}")

    removed = lib.remove_at(2)
    print(f"\nУдалили книгу по индексу 2: {removed.name}")
    print(f"Осталось книг: {len(lib)}")

def scenario_3_sort_filter():
    print("\n=== СЦЕНАРИЙ 3: Сортировка и фильтрация ===\n")

    lib = Library()
    books = [
        Book("Золотой телёнок", "Ильф и Петров", 1931, 400),
        Book("Бесы", "Достоевский", 1872, 700),
        Book("Евгений Онегин", "Пушкин", 1833, 320),
        Book("Тихий Дон", "Шолохов", 1928, 1500)
    ]
    for b in books:
        lib.add(b)

    print("До сортировки:")
    for b in lib:
        print(f"  {b.name} ({b.year})")

    lib.sort(key='year')
    print("\nПосле сортировки по году:")
    for b in lib:
        print(f"  {b.name} ({b.year})")

    lib.sort(key='name')
    print("\nПосле сортировки по названию:")
    for b in lib:
        print(f"  {b.name}")

    lib[0].issue_book()
    available = lib.filter_available()
    print("\nДоступные книги после выдачи первой:")
    for b in available:
        print(f"  {b.name} — {'доступна' if b.is_available else 'выдана'}")

    filtered = lib.filter_by_year(year_from=1900, year_to=2000)
    print("\nКниги с 1900 по 2000 год:")
    for b in filtered:
        print(f"  {b.name} ({b.year})")

def main():
    scenario_1_basic()
    scenario_2_search_iter_len()
    scenario_3_sort_filter()

if __name__ == "__main__":
    main()


