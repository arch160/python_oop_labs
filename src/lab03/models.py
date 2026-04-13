from base import Book

class Ebook(Book):

    def __init__(self, name: str, writer: str, year: int, pages: int,
                 file_size_mb: float, drm_protected: bool = False):

        super().__init__(name, writer, year, pages)
        self._file_size_mb = file_size_mb
        self._drm_protected = drm_protected

    @property
    def file_size_mb(self):
        return self._file_size_mb

    @property
    def drm_protected(self):
        return self._drm_protected

    def download(self):
        if self.is_available:
            return f"Скачивание '{self.name}' ({self._file_size_mb} МБ)"
        else:
            return f"Книга '{self.name}' недоступна для скачивания (выдана)."

    def __str__(self):
        base_str = super().__str__()
        drm_str = " (защищена DRM)" if self._drm_protected else ""
        return base_str + f" | Электронная, {self._file_size_mb} МБ{drm_str}"

    def process(self):
        return self.download()


class AudioBook(Book):

    def __init__(self, name: str, writer: str, year: int, pages: int,
                 duration_hours: float, narrator: str):
        super().__init__(name, writer, year, pages)
        self._duration_hours = duration_hours
        self._narrator = narrator

    @property
    def duration_hours(self):
        return self._duration_hours

    @property
    def narrator(self):
        return self._narrator

    def listen_preview(self):
        return f"Прослушивание отрывка аудиокниги '{self.name}' (читает {self._narrator})"

    def __str__(self):
        base_str = super().__str__()
        return base_str + f" | Аудиокнига, {self._duration_hours} ч., чтец: {self._narrator}"

    def process(self):
        return self.listen_preview()