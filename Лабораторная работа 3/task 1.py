class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author
    @property
    def name(self) -> str:
        return self.__name

    @property
    def author(self) -> str:
        return self.__author

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"


class PaperBook(Book):
    """Класс, который описывает книгу"""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

        @property
        def pages(self):
            return self._pages

        @pages.setter
        def pages(self, new_pages: int):
            """Устанавливает количество страниц в книге."""
            if not isinstance(new_pages, int):
                raise TypeError("Количество страниц должно быть типа int")
            if new_pages <= 0:
                raise ValueError("Количество страниц должно быть положительным числом")
            self._pages = new_pages

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return f"{self.__class__.__name__}(name = {self.name!r}, author = {self.author!r}, pages = {self.pages})"


class AudioBook(Book):
    """Класс, который описывает аудиокнигу"""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration: float):
        if not isinstance(new_duration, float):
            raise TypeError("Длительность книги должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Длительность книги должна быть положительным числом")
        self._duration = new_duration

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self._duration})"

