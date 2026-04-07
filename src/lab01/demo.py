from model import Book

def scenario_1_creation_and_magic():
    """Сценарий 1: Создание объектов и демонстрация магических методов."""
    print("* СЦЕНАРИЙ 1: Создание книг и магические методы")
    
    # Создаём несколько книг
    book1 = Book("Война и мир", "Лев Толстой", 1869, 1300)
    book2 = Book("Преступление и наказание", "Фёдор Достоевский", 1866, 672)
    book3 = Book("Война и мир", "Лев Толстой", 2020, 900)  # Новое издание
    
    print("Созданы следующие книги:")
    print(f"   1. {book1}")
    print(f"   2. {book2}")
    print(f"   3. {book3}")
    
    # Демонстрация __str__
    print("\n__str__ для пользователя:")
    print(f"   {book1}")
    
    # Демонстрация __repr__
    print("\n__repr__ для разработчика:")
    print(f"   {repr(book1)}")
    
    # Демонстрация __eq__
    print("\nСравнение книг (__eq__):")
    print(f"   book1 == book3: {book1 == book3} (одинаковые автор и название)")
    print(f"   book1 == book2: {book1 == book2} (разные книги)")
    


def scenario_2_validation_and_setter():
    """Сценарий 2: Проверка валидации и работы setter'а."""
    print("* СЦЕНАРИЙ 2: Валидация данных и setter")
    
    # Корректное создание
    try:
        book = Book("Евгений Онегин", "Александр Пушкин", 1833, 320)
        print("Успешно создана книга:")
        print(f"   {book}")
    except Exception as e:
        print(f"Ошибка: {e}")
    
    # Некорректное создание (пустой автор)
    try:
        print("\nПопытка создать книгу с пустым автором:")
        book_bad = Book("Капитанская дочка", "   ", 1836, 300)
    except Exception as e:
        print(f"   Ошибка: {type(e).__name__}: {e}")
    
    # Некорректное создание (отрицательные страницы)
    try:
        print("\nПопытка создать книгу с отрицательным числом страниц:")
        book_bad = Book("Мёртвые души", "Гоголь", 1842, -50)
    except Exception as e:
        print(f"   Ошибка: {type(e).__name__}: {e}")
    
    # Некорректное создание (нереальный год)
    try:
        print("\nПопытка создать книгу с годом 1300 (раньше книгопечатания):")
        book_bad = Book("Сказка", "Народ", 1300, 100)
    except Exception as e:
        print(f"   Ошибка: {type(e).__name__}: {e}")
    
    # Работа setter'а
    print("\nДемонстрация работы setter для pages:")
    test_book = Book("Ревизор", "Н.В. Гоголь", 1836, 100)
    print(f"   До изменения: {test_book.pages} стр.")
    
    test_book.pages = 150
    print(f"   После изменения: {test_book.pages} стр.")
    
    try:
        print("   Пытаемся установить -10 страниц...")
        test_book.pages = -10
    except Exception as e:
        print(f"   Ошибка: {e}")


def scenario_3_state_and_behavior():
    """Сценарий 3: Работа с состоянием объекта и зависимое поведение."""
    print("* СЦЕНАРИЙ 3: Состояние объекта и бизнес-методы")
    
    # Создаём книгу
    book = Book("Мастер и Маргарита", "Михаил Булгаков", 1967, 480)
    print("Исходное состояние:")
    print(f"   {book}")
    
    # Выдача книги
    print("\nВыдаём книгу читателю:")
    try:
        book.issue_book()
        print(f"   Статус после выдачи: {'В библиотеке' if book.is_available else 'Выдана'}")
    except Exception as e:
        print(f"   Ошибка: {e}")
    
    # Попытка выдать повторно
    print("\nПытаемся выдать уже выданную книгу:")
    try:
        book.issue_book()
    except Exception as e:
        print(f"   Ожидаемая ошибка: {e}")
    
    # Возврат книги
    print("\nВозвращаем книгу в библиотеку:")
    try:
        book.return_book()
        print(f"   Статус после возврата: {'В библиотеке' if book.is_available else 'Выдана'}")
    except Exception as e:
        print(f"   Ошибка: {e}")
    
    # Попытка вернуть повторно
    print("\nПытаемся вернуть уже доступную книгу:")
    try:
        book.return_book()
    except Exception as e:
        print(f"   Ожидаемая ошибка: {e}")
    
    # Демонстрация бизнес-метода is_thick_book
    print("\nПроверка на 'толстую' книгу:")
    thin_book = Book("Детство", "Л.Н. Толстой", 1852, 150)
    thick_book = Book("Тихий Дон", "М.А. Шолохов", 1928, 1500)
    
    print(f"   {thin_book.name}: {thin_book.pages} стр. -> "
          f"{'ТОЛСТАЯ' if thin_book.is_thick_book() else 'НЕ толстая'}")
    print(f"   {thick_book.name}: {thick_book.pages} стр. -> "
          f"{'ТОЛСТАЯ' if thick_book.is_thick_book() else 'НЕ толстая'}")
    


def scenario_4_additional_features():
    """Сценарий 4: Дополнительные возможности и сложные сценарии."""
    print("* СЦЕНАРИЙ 4: Дополнительные возможности")
    
    # Работа с несколькими книгами
    print("Создаём библиотеку из нескольких книг:")
    books = [
        Book("1984", "Джордж Оруэлл", 1949, 328),
        Book("Улисс", "Джеймс Джойс", 1922, 1056),
        Book("Маленький принц", "Антуан де Сент-Экзюпери", 1943, 96)
    ]
    
    for i, book in enumerate(books, 1):
        print(f"   {i}. {book}")
    
    # Выдаём одну книгу
    print("\nВыдаём 'Улисс' читателю:")
    books[1].issue_book()
    
    # Пытаемся найти книгу по автору и названию
    print("\nПоиск книги '1984' Джорджа Оруэлла:")
    search_name = "1984"
    search_writer = "Джордж Оруэлл"
    
    found = None
    for book in books:
        if book.name == search_name and book.writer == search_writer:
            found = book
            break
    
    if found:
        print(f"   Найдена: {found}")
    else:
        print("   Книга не найдена")
    
    # Демонстрация порога для толстой книги
    print("\nИспользование разного порога для определения 'толстой' книги:")
    test_book = Book("Война и мир", "Толстой", 1869, 1300)
    print(f"   Книга: {test_book.name}, {test_book.pages} стр.")
    print(f"   Порог 500: {'толстая' if test_book.is_thick_book(500) else 'не толстая'}")
    print(f"   Порог 1500: {'толстая' if test_book.is_thick_book(1500) else 'не толстая'}")


if __name__ == "__main__":
    print("\n")
    print("=" * 70)
    print(" ЛАБОРАТОРНАЯ РАБОТА №1 ")
    print(" Класс Book (Библиотека) ")
    print("=" * 70)
    
    # Запуск всех сценариев
    scenario_1_creation_and_magic()
    scenario_2_validation_and_setter()
    scenario_3_state_and_behavior()
    scenario_4_additional_features()
    
