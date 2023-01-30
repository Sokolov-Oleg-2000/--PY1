from pydantic import BaseModel, conint
from typing import Optional
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book(BaseModel):
    id: conint(ge = 0)      # должно быть больше 0
    name: str
    pages: conint(ge = 0)   # должно быть больше 0
    """
    Создаем класс "Book", который будет инициализировать id, name, pages.
    :param id: Идентификатор книги
    :param name: Название книги
    :param pages: Количество страниц в книге
    """
    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


class Library(BaseModel):
    books: Optional[list] = []
    """
    Создаем класс "Library", который будет инициализировать books.
    :param books: Список книг
    """
    def get_next_book_id(self):
        if self.books == None:
            return 1
        else:
            return len(self.books) + 1

    def get_index_by_book_id(self, id_ = int):
        a = False
        for index, value in enumerate(self.books):
            if value.id == id_:
                a = True
                b = index
        if a == False:
            raise ValueError("Книги с запрашиваемым id не существует")
        else:
            return b


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
    
