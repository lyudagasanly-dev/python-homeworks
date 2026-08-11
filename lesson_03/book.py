class Book:

    def __init__(self, name, avtor):
        self.name = name
        self.avtor = avtor

    def get_name(self):
        return self.name

    def get_avtor(self):
        return self.avtor

    def get_book_info(self):
        return f"Book: {self.name}, Avtor: {self.avtor}"


book = Book("Отцы и дети", "Тургенев")
print(book.get_book_info())
