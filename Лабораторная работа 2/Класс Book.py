from pydantic import BaseModel, conint
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


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
