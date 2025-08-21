class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        new_list = []
        for b in self.books:
            if b.title.lower() != book.title.lower() or b.author.lower != book.author.lower():
                new_list.append(book)
        self.books = new_list

    def search_books(self, search_string):
        matching_list = []
        for b in self.books:
            if search_string.lower() in b.title.lower() or search_string.lower() in b.author.lower():
                matching_list.append(b)
        return matching_list