from book import Book

library = [
    Book("Отцы и дети", "Тургенев"),
    Book("Капитанская дочка", "Пушкин"),
    Book("Война и мир", "Толстой")
]


for kniga in library:
    print(f"{kniga.get_name()} - {kniga.get_avtor()}")
