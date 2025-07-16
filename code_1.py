import os
import json


file_name = r"D:\VishalSpace\Working With Python\Library_Managment\lib_data.json"

def load_data():
    if not os.path.exists(file_name):
        return {}
    with open(file_name, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def save_data(data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent = 4)

        
class Library:
    def __init__(self, library_name=None):
        self.library_name = library_name
        self.books = []
        self.authors = []
        self.members = []
        data = load_data()
        if 'Books' in data:
            # Load books from the JSON file
            for book in data['Books']:
                new_book = Book(book['name'], book['author'], book['publication_year'])
                self.books.append(new_book)

        if 'Authors' in data:
            # Load authors from the JSON file
            for author in data['Authors']:
                new_author = Atuhor(author['name'])
                self.authors.append(new_author)

        if 'Members' in data:
            # Load members from the JSON file
            for member in data['Members']:
                new_member = Member(member['name'])
                self.members.append(new_member)

        
    def add_book(self, book_name=None, author=None, publication_year=None):
        data = load_data()
        new_book = Book(book_name, author, publication_year)
        self.books.append(new_book)
        # Convert Book objects to dicts for JSON serialization
        data['Books'] += [
            {"name": book_name, "author": author, "publication_year": publication_year}
        ]
        save_data(data)
        print(f"Book {book_name} added successfully.")
        return

    def remove_book(self, book_name):
        data  = load_data()
        self.books = [book for book in self.books if book.name.lower() != book_name.lower()]
        for book in data['Books']:
            if book_name.lower() == book['name'].lower():
                data['Books'].remove(book)
                save_data(data)
                print(f"Book {book_name} removed successfully.")
                return
        print("Book not found!!")
        return
    

    def add_author(self, author_name = None):
        data = load_data()
        new_author = Atuhor(author_name)
        self.authors.append(new_author)
        if 'Authors' not in data:
            data['Authors'] = []
        data['Authors'] += [
            {"name": author_name}
        ]
        save_data(data)
        print(f"Author {author_name} added successfully.")
        return
    
    def remove_author(self, author_name):
        data = load_data()
        self.authors = [author for author in self.authors if author.author_name.lower() != author_name.lower()]
        for author in data['Authors']:
            if author_name.lower() == author['name'].lower():
                data['Authors'].remove(author)
                save_data(data)
                print(f"Author {author['name']} removed successfully.")
                return
        print("Author not found!!")
        return
    

    def add_member(self, member_name = None):
        data = load_data()
        new_member = Member(member_name)
        self.members.append(new_member)
        if 'Members' not in data:
            data['Members'] = []
        data['Members'] += [
            {"name": member_name}
        ]
        save_data(data)
        print(f"Member {member_name} added successfully.")
        return
    
    def remove_member(self, member_name):
        data = load_data()
        self.members = [member for member in self.members if member.member_name.lower() != member_name.lower()]
        for member in data['Members']:
            if member_name.lower() == member['name'].lower():
                data['Members'].remove(member)
                save_data(data)
                print(f"Member {member['name']} removed successfully.")
                return
        print("Member not found!!")
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





library = Library()
def main():
    while True:
        print("\n=== Library Management System ===\n")
        print("1. Add Book")
        print("2. Add Author")
        print("3. Add Member")
        print("4. Remove Book")
        print("5. Remove Author")
        print("6. Remove Member")
        print("7. Search Book")
        print("8. View Book List")
        print("0. Exit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_name = input("Enter book name: ")
            author_name = input("Enter author name: ")
            publication_year = input("Enter publication year: ")
            library.add_book(book_name, author_name, publication_year)
        
        elif choice == "2":
            author_name = input("Enter author name: ")
            library.add_author(author_name)
        
        elif choice == "3":
            member_name = input("Enter member name: ")
            library.add_member(member_name)
        
        elif choice == "4":
            book_name = input("Enter book name to remove: ")
            library.remove_book(book_name)
        
        elif choice == "5":
            author_name = input("Enter author name to remove: ")
            library.remove_author(author_name)
        elif choice == "6":
            member_name = input("Enter member name to remove: ")
            library.remove_member(member_name)

        elif choice == "7":
            book_name = input("Enter book name to search: ")
            library.search_book(book_name)
        
        elif choice == "8":
            library.book_list()
        
        elif choice == "0":
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice, please try again.")

main()