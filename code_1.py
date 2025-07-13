class Library:
    # Library: Represents the library. This class will have methods for adding a book, removing a book, and searching for a book by multiple parameters.
    def __init__(self, library_name=None):
        self.library_name = library_name
        self.books = []
        self.authors = []
        self.members = []
        
    def add_book(self, book_name = None , author=None, publication_year=None):
        new_book = Book(book_name, author, publication_year)
        self.books.append(new_book)
        print(f"Book {book_name} added successfully.")
        return

    def remove_book(self, book_name):
        for book in self.books:
            if book_name.lower() == book.name.lower():
                self.books.remove(book)
                print(f"Book {book.name} removed successfully.")
                return
        print("Book not found.")
        return

    def add_author(self, author_name = None):
        new_author = Atuhor(author_name)
        self.authors.append(new_author)
        print(f"Author {author_name} added successfully.")
        return
    
    def remove_author(self, author_name):
        for author in self.authors:
            if author_name.lower() == author.author_name.lower():
                self.authors.remove(author)
                print(f"Author {author.author_name} removed successfully.")
                return
        print("Author not found.")
        return
 
    def search_book(self, book_name):
        for book in self.books:
            if book_name.lower() == book.name.lower():
                print(book.name ,"Found")
                return 
        print(book_name, "is not found.")
        return 
    
    def book_list(self):
        if not self.books:
            print("Currently no books available in the library.")
        else:
            print("Books list: ")
            for book in self.books:
                print(book.name, "    by ", book.author, "    published in ", book.publication_year)
        return
        

    

class Book:
    def __init__(self, book_name=None, author =None, publication_year=None):
        self.name = book_name
        self.author = author
        self.publication_year = publication_year
    
    def __str__(self):
        return self.name if self.name else "Unknown Book!!"
    def __repr__(self):
        return self.__str__()



class Atuhor():
    def __init__(self, author_name=None):
        self.author_name = author_name

    def __str__(self):
        return self.author_name if self.author_name else "Unknown Author!!"
    def __repr__(self):
        return self.__str__()
        


class Member:
    def __init__(self, member_name=None):
        self.member_name = member_name
        self.borrowed_books = []
