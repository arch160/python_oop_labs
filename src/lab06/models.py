class Book:
    def __init__(self, name: str, writer: str, year: int, pages: int, is_available: bool = True) -> None:
        self._name: str = name.strip()
        self._writer: str = writer.strip()
        self._year: int = year
        self._pages: int = pages
        self._is_available: bool = is_available

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
        if value <= 0:
            raise ValueError("страниц >0 надо")
        self._pages = value

    @property
    def is_available(self) -> bool:
        return self._is_available

    def issue_book(self) -> None:
        if not self._is_available:
            raise ValueError(f"{self._name} уже выдана")
        self._is_available = False

    def return_book(self) -> None:
        if self._is_available:
            raise ValueError(f"{self._name} уже в библиотеке")
        self._is_available = True

    def display(self) -> str:
        status = "в библиотеке" if self._is_available else "выдана"
        return f"{self._name} | {self._writer} | {self._year} | {self._pages} стр. | {status}"

    def score(self) -> float:
        return 5.0 if self._is_available else 1.0


class Ebook(Book):
    def __init__(self, name: str, writer: str, year: int, pages: int, file_size_mb: float, drm_protected: bool = False) -> None:
        super().__init__(name, writer, year, pages)
        self._file_size_mb: float = file_size_mb
        self._drm_protected: bool = drm_protected

    def download(self) -> str:
        if self.is_available:
            return f"скачиваю {self.name} ({self._file_size_mb} МБ)..."
        else:
            return f"{self.name} (выдана)"

    def display(self) -> str:
        base = super().display()
        drm = " (drm)" if self._drm_protected else ""
        return base + f" | электронная, {self._file_size_mb} МБ{drm}"

    def score(self) -> float:
        base = super().score()
        return base - 0.5 if self._drm_protected else base + 0.5


class AudioBook(Book):
    def __init__(self, name: str, writer: str, year: int, pages: int, duration_hours: float, narrator: str) -> None:
        super().__init__(name, writer, year, pages)
        self._duration_hours: float = duration_hours
        self._narrator: str = narrator

    def listen_preview(self) -> str:
        return f"отрывок {self.name} (читает {self._narrator})"

    def display(self) -> str:
        base = super().display()
        return base + f" | аудио, {self._duration_hours} ч., чтец: {self._narrator}"

    def score(self) -> float:
        return super().score() + 0.2