import random
import sys

from constants import Book, Reader
from library_logic_and_logs import Library


def launcher():
    library = Library()

    while True:
        print("\nWelcome to e-Library, to make your choice please select: ")
        print("1. Add Book")
        print("2. Show available books")
        print("3. Show issued books")
        print("4. Register reader")
        print("5. Borrow a book. By entering book name or code")
        print("6. Return book. By entering book code")
        print("7. Exit")

        choice = input("Use options belong: ")

        if choice == "1":
            title = input("Book title : ")
            author = input("Book autor: ")
            code = random.randint(1, 99999999)
            library.new_books_reg(Book(title, author, code))

        elif choice == "2":
            library.show_available_books()

        elif choice == "3":
            library.show_issued_books()

        elif choice == "4":
            first_name = input("Enter your name: ")
            last_name = input("Enter your last name: ")

        elif choice == "5":
            book_code = int(input("Enter Book code: "))
            reader_id = int(input("Enter reader ID: "))
            library.borrow_book(book_code,reader_id)

        elif choice == "6":
            book_code = int(input("Enter Book code for return: "))
            library.return_book(book_code)

        elif choice == "7":
            print("Exit")
            sys.exit()

        else:
            print("Not correct choice. Please try again.")


print(launcher())