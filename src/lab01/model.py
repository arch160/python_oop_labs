from validate import validate_title, validate_author, validate_year, validate_pages


class Book:
    """
    Класс, представляющий книгу в библиотеке.
    
    Атрибуты класса:
        total_books (int): общее количество созданных экземпляров книг
        
    Атрибуты экземпляра (закрытые):
        _title (str): название книги
        _author (str): автор книги
        _year (int): год издания
        _pages (int): количество страниц
        _is_available (bool): доступность книги (True - в библиотеке, False - выдана)
    """
    
    # Атрибут класса
    total_books = 0
    
    def __init__(self, title: str, author: str, year: int, 
                 pages: int, is_available: bool = True):
        """
        Конструктор класса Book.
        
        Args:
            title: название книги
            author: автор книги
            year: год издания
            pages: количество страниц
            is_available: доступность книги (по умолчанию True)
            
        Raises:
            TypeError: при неверном типе данных
            ValueError: при неверном значении данных
        """
        # Валидация всех входных данных
        validate_title(title)
        validate_author(author)
        validate_year(year)
        validate_pages(pages)
        
        # Закрытые атрибуты экземпляра
        self._title = title.strip()
        self._author = author.strip()
        self._year = year
        self._pages = pages
        self._is_available = is_available
        
        # Увеличиваем счётчик созданных книг
        Book.total_books += 1
    
    # === Свойства (геттеры) ===
    
    @property
    def title(self) -> str:
        """Возвращает название книги (только для чтения)."""
        return self._title
    
    @property
    def author(self) -> str:
        """Возвращает автора книги (только для чтения)."""
        return self._author
    
    @property
    def year(self) -> int:
        """Возвращает год издания (только для чтения)."""
        return self._year
    
    @property
    def pages(self) -> int:
        """Возвращает количество страниц."""
        return self._pages
    
    @pages.setter
    def pages(self, value: int) -> None:
        """
        Устанавливает количество страниц с валидацией.
        
        Args:
            value: новое количество страниц
            
        Raises:
            TypeError: если значение не целое число
            ValueError: если значение <= 0
        """
        validate_pages(value)
        self._pages = value
        print(f"Количество страниц изменено на {value}")
    
    @property
    def is_available(self) -> bool:
        """Возвращает доступность книги (только для чтения)."""
        return self._is_available
    
    # === методы ===
    
    def __str__(self) -> str:
        """
        Строковое представление для пользователей.
        
        Returns:
            Красиво отформатированная строка с информацией о книге
        """
        status = "Книга в библиотеке" if self._is_available else "Книга выдана"
        return (f"«{self._title}» | {self._author} | "
                f"{self._year} г. | {self._pages} стр. | {status}")
    
    def __repr__(self) -> str:
        """
        Официальное строковое представление для разработчиков.
        
        Returns:
            Строка, по которой можно воссоздать объект
        """
        return (f"Book(title='{self._title}', author='{self._author}', "
                f"year={self._year}, pages={self._pages}, "
                f"is_available={self._is_available})")
    
    def __eq__(self, other) -> bool:
        """
        Сравнение книг на равенство.
        
        Две книги считаются равными, если у них совпадают название и автор
        (регистр букв не учитывается).
        
        Args:
            other: другой объект для сравнения
            
        Returns:
            True если книги равны, False в противном случае
        """
        if not isinstance(other, Book):
            return False
        return (self._title.lower() == other._title.lower() and 
                self._author.lower() == other._author.lower())
    
    # === Бизнес-методы ===
    
    def issue_book(self) -> None:
        """
        Выдать книгу читателю.
        
        Поведение зависит от состояния: нельзя выдать уже выданную книгу.
        
        Raises:
            ValueError: если книга уже выдана
        """
        if not self._is_available:
            raise ValueError(f"Книга «{self._title}» уже выдана читателю")
        
        self._is_available = False
        print(f"✅ Книга «{self._title}» успешно выдана читателю")
    
    def return_book(self) -> None:
        """
        Вернуть книгу в библиотеку.
        
        Поведение зависит от состояния: нельзя вернуть книгу, 
        которая уже в библиотеке.
        
        Raises:
            ValueError: если книга уже находится в библиотеке
        """
        if self._is_available:
            raise ValueError(f"Книга «{self._title}» уже находится в библиотеке")
        
        self._is_available = True
        print(f"✅ Книга «{self._title}» успешно возвращена в библиотеку")
    
    def is_thick_book(self, threshold: int = 500) -> bool:
        """
        Определяет, является ли книга толстой.
        
        Args:
            threshold: пороговое значение страниц (по умолчанию 500)
            
        Returns:
            True если книга толстая, False в противном случае
        """
        return self._pages > threshold
    
    def get_info(self) -> dict:
        """
        Возвращает всю информацию о книге в виде словаря.
        
        Returns:
            Словарь с атрибутами книги
        """
        return {
            'title': self._title,
            'author': self._author,
            'year': self._year,
            'pages': self._pages,
            'is_available': self._is_available
        }