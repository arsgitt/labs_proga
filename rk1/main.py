# Создание классов данных
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
class Bookstore:
    def __init__(self, store_id, name, books):
        self.store_id = store_id
        self.name = name
        self.books = books
# Создание списков объектов классов с тестовыми данными
books = [
    Book(1, "Война и мир", "Лев Толстой"),
    Book(2, "Преступление и наказание", "Федор Достоевский"),
    Book(3, "Евгений Онегин", "Александр Пушкин"),
    Book(4, "Мастер и Маргарита", "Михаил Булгаков"),
    Book(5, "Идиот", "Федор Достоевский"),
    Book(6, "Отцы и дети", "Иван Тургенев"),
    Book(7, "Герой нашего времени", "Михаил Лермонтов")
]

bookstores = [
    Bookstore(1, "Магазин книг 'Читай-город'", [books[0], books[1], books[2], books[5]]),
    Bookstore(2, "Книжный мир", [books[3], books[4], books[5]]),
    Bookstore(3, "Буквоед", [books[0], books[1], books[4], books[6]])
]

# Запросы
print("Задание Б1")
bookstore_books = [(bookstore.name, book.title) for bookstore in bookstores for book in bookstore.books]
bookstore_books_sorted = sorted(bookstore_books, key=lambda x: x[1])
print("Список всех связанных книг и книжных магазинов, отсортированный по книгам:")
for item in bookstore_books_sorted:
    print(f"Книга '{item[1]}' в магазине '{item[0]}'")
print("Задание Б2")
bookstore_books_count = [(bookstore.name, len(bookstore.books)) for bookstore in bookstores]
bookstore_books_count_sorted = sorted(bookstore_books_count, key=lambda x: x[1], reverse=True)
print("Список книжных магазинов с количеством книг в каждом магазине:")
for item in bookstore_books_count_sorted:
    print(f"Магазин '{item[0]}': {item[1]} книг")
print("Задание Б3")
books_with_i = [book for book in books if book.title.endswith("и")]
bookstores_with_i_books = [(bookstore.name, book.title) for bookstore in bookstores for book in bookstore.books if book in books_with_i]
print("Список всех книг, у которых название заканчивается на 'и', и книжные магазины, в которых они находятся:")
for item in bookstores_with_i_books:
    print(f"Книга '{item[1]}' в магазине '{item[0]}'")
