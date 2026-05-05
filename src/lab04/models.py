from interfaces import Printable, Comparable

class Book(Printable, Comparable):
    def __init__(self, name, writer, year, pages, is_available=True):
        self._name = name.strip()
        self._writer = writer.strip()
        self._year = year
        self._pages = pages
        self._is_available = is_available

    @property
    def name(self):
        return self._name

    @property
    def writer(self):
        return self._writer

    @property
    def year(self):
        return self._year

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if value <= 0:
            raise ValueError("страниц должно быть больше 0")
        self._pages = value

    @property
    def is_available(self):
        return self._is_available

    def issue_book(self):
        if not self._is_available:
            raise ValueError(f"книга {self._name} уже выдана")
        self._is_available = False

    def return_book(self):
        if self._is_available:
            raise ValueError(f"книга {self._name} уже в библиотеке")
        self._is_available = True

    # реализация Printable
    def to_string(self):
        status = "в библиотеке" if self._is_available else "выдана"
        return f"{self._name} | {self._writer} | {self._year} г. | {self._pages} стр. | {status}"

# Comparable, сравнение по году
    def compare_to(self, other):
        if not isinstance(other, Book):
            return -2
        if self._year < other._year:
            return -1
        elif self._year > other._year:
            return 1
        else:
            return 0

    def __str__(self):
        return self.to_string()


class Ebook(Book):
    def __init__(self, name, writer, year, pages, file_size_mb, drm_protected=False):
        super().__init__(name, writer, year, pages)
        self._file_size_mb = file_size_mb
        self._drm_protected = drm_protected

    def download(self):
        if self.is_available:
            return f"скачиваю {self.name} ({self._file_size_mb} МБ)..."
        else:
            return f"нельзя скачать {self.name} (выдана)"

    def to_string(self):
        base = super().to_string()
        drm = " (drm)" if self._drm_protected else ""
        return base + f" | электронная, {self._file_size_mb} МБ{drm}"


class AudioBook(Book):
    def __init__(self, name, writer, year, pages, duration_hours, narrator):
        super().__init__(name, writer, year, pages)
        self._duration_hours = duration_hours
        self._narrator = narrator

    def listen_preview(self):
        return f"отрывок аудиокниги {self.name} (читает {self._narrator})"

    def to_string(self):
        base = super().to_string()
        return base + f" | аудио, {self._duration_hours} ч., чтец: {self._narrator}"