from validate import validate_name, validate_writer, validate_year, validate_pages


class Book:
    
    
    def __init__(self, name: str, writer: str, year: int, 
                 pages: int, is_available: bool = True):

        
        validate_name(name)

        validate_writer(writer)

        validate_year(year)

        validate_pages(pages)
        


        self._name = name.strip()
        self._writer = writer.strip()
        self._year = year
        self._pages = pages
        self._is_available = is_available
        


    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def writer(self) -> str:
        return self._writer
    
    @property
    def year(self) -> int:
        return self._year
    
    @property
    def pages(self) -> int:
        return self._pages
    
    @pages.setter
    def pages(self, value: int) -> None:
        validate_pages(value)
        self._pages = value
        print(f"Количество страниц изменено на {value}")
    
    @property
    def is_available(self) -> bool:
        return self._is_available



    def __str__(self) -> str:
        status = "Книга в библиотеке" if self._is_available else "Книга выдана"
        return (f"«{self._name}» | {self._writer} | "
                f"{self._year} г. | {self._pages} стр. | {status}")
    
    def __repr__(self) -> str:
        return (f"Book(name='{self._name}', writer='{self._writer}', "
                f"year={self._year}, pages={self._pages}, "
                f"is_available={self._is_available})")
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Book):
            return False
        return (self._name.lower() == other._name.lower() and 
                self._writer.lower() == other._writer.lower())




    
    def issue_book(self) -> None:
        if not self._is_available:
            raise ValueError(f"Книга «{self._name}» уже выдана читателю")
        
        self._is_available = False
        print(f"Книга «{self._name}» успешно выдана читателю")
        
    
    def return_book(self) -> None:
        if self._is_available:
            raise ValueError(f"Книга «{self._name}» уже находится в библиотеке")
        
        self._is_available = True
        print(f"Книга «{self._name}» успешно возвращена в библиотеку")

    
    def is_thick_book(self, threshold: int = 500) -> bool:
        return self._pages > threshold


