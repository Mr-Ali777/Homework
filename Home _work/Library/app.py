import sys

from gen_book import Book
from gen_reader import Reader
from library_logic_and_logs import Library


def launcher():
    library = Library()

    while True:
        print("\nWelcome to e-Library, to make your choice please select: ")
        print("1. Add Book")
        print("2. Add Reader")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Use options belong: ")

        if choice == "1":
            title = input("Book title : ")
            author = input("Book autor: ")
            code = input("Book code: ")
            book = Book(title, author, code)
            library.new_books(title, author, code)

        elif choice == "2":
            reader_id = input("Enter reader ID: ")
            name = input("Enter reader name: ")
            reader = Reader(reader.first_name, reader.last_name, reader_id)
            library.readers(reader)

        elif choice == '3':
            reader_id = input("Enter reader ID: ")
            book_code = input("Enter book code: ")
            library.borrow_book(reader_id, book_code)

        elif choice == '4':
            reader_id = input("Enter reader ID: ")
            book_code = input("Enter book code: ")
            library.return_book(reader_id, book_code)

        elif choice == '5':
            print("Exiting the system.")
            sys.exit()

        else:
            print("Not correct choice. Please try again.")


print(launcher())