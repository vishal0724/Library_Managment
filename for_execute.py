from code_1 import Library, Book, Atuhor, Member


school_lib_ltd = Library("school_lib_ltd")
print(school_lib_ltd.authors)
print(school_lib_ltd.books)
school_lib_ltd.add_author("J.K. Rowling")
school_lib_ltd.add_author("Vishal RR")
school_lib_ltd.add_author("Ram Kumar")
school_lib_ltd.add_book("Harry Potter and the Philosopher's Stone", author="J.K. Rowling", publication_year=1997)
school_lib_ltd.add_book("Harry Potter and the Chamber of Secrets", author="J.K. Rowling", publication_year=1998)
# print(school_lib_ltd.authors)
# print(school_lib_ltd.books)
# school_lib_ltd.remove_author("Ram Kumar")
# school_lib_ltd.remove_book("Harry Potter and the Chamber of Secrets")
# print(school_lib_ltd.authors)
# print(school_lib_ltd.books)
school_lib_ltd.search_book("Harry Potter and the Philosopher's Stone")
school_lib_ltd.book_list()