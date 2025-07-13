class Library:
    # Library: Represents the library. This class will have methods for adding a book, removing a book, and searching for a book by multiple parameters.
    def __init__(self):
        self.books = []
        self.authors = []
        self.members = []

    def add_book(self, book_name):
        new_book = Book(book_name, author=None, publication_year=None)
        self.books.append(new_book)



    def remove_book(self):
        pass
    def search_book(self):
        pass
    

class Book:
    def __init__(self,book_name, author =None, publication_year=None):
        self.name = book_name
        self.author = author
        self.publication_year = publication_year

class Atuhor:
    pass

class Member:
    pass
