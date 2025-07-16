from code_1 import Library, Book, Atuhor, Member

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

library = Library()
def main():
    while True:
        print("\n=== Library Management System ===\n")
        print("1. Add Book")
        print("2. Add Author")
        print("3. Add Member")
        print("4. Remove Book")
        print("5. Remove Author")
        print("6. Search Book")
        print("7. View Book List")
        print("8. Exit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_name = input("Enter book name: ")
            author_name = input("Enter author name: ")
            publication_year = input("Enter publication year: ")
            library.add_book(book_name, author_name, publication_year)
        
        elif choice == "2":
            author_name = input("Enter author name: ")
            library.add_author(Atuhor(author_name))
        
        elif choice == "3":
            member_name = input("Enter member name: ")
            library.add_member(Member(member_name))
        
        elif choice == "4":
            book_name = input("Enter book name to remove: ")
            library.remove_book(book_name)
        
        elif choice == "5":
            author_name = input("Enter author name to remove: ")
            library.remove_author(author_name)
        
        elif choice == "6":
            book_name = input("Enter book name to search: ")
            library.search_book(book_name)
        
        elif choice == "7":
            library.book_list()
        
        elif choice == "8":
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice, please try again.")



