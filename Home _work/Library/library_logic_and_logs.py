import datetime
import random
import logging
from constants import Book, Reader

logging.basicConfig(filename='library.log', level=logging.INFO, format='%(asctime)s - %(message)s')


class Library:
    def __init__(self):
        self.books = []
        self.readers = []

    def new_books_reg(self, book):
        self.books.append(book)
        logging.info(f'New book added: "{book.title}" author {book.author} (book code: {book.code}) .')

    def new_reader_reg(self):
        reader_id = random.randint(1, 9999999)
        while any(reader.reader_id == reader_id for reader in self.readers):
            reader_id = random.randint(1, 9999999)

        reader = Reader(first_name, last_name, reader_id)
        self.readers.append(reader)
        logging.info(f'New reader added: {reader.first_name} {reader.last_name} (reader ID: {reader.reader_id}) .')
        print(f'Reader {reader.first_name} {reader.last_name} successfully registered, your ID ->{reader.reader_id}) .')

    def show_available_books(self):
        available_books = [book for book in self.books if book.issued_code is None]
        if available_books:
            print(f"Available books:")
            for book in available_books:
                print(f'Book name: "{book.title}", Author: {book.author},  Book Code: ({book.code}) .')
        else:
            print("All books was issued to the readers.")

    def show_issued_books(self):
        issued_books = [book for book in self.books if book.issued_id is not None]
        if issued_books:
            print("Issued books:")
            for book in issued_books:
                print(f'Book name: "{book.title}", Author: {book.author},  Book Code: {book.code}) .')
        else:
            print("All books in the Library right now.")

    def borrow_book(self, reader_id, book_code):
        for book in self.books:
            if book.code == book_code:
                if book.issued_id is None:
                    book.issued_id = reader_id
                    book.issued_date = datetime.datetime.now()
                    logging.info(f'Book "{book.title}" issued to reader {reader.first_name} with ID {reader_id} .')
                    print(f'Book "{book.title}" issued to reader {reader.first_name} with ID {reader_id} .')
                    return
                else:
                    print("Book already issued.")
                    return
        print("Book was not found.")

    def return_book(self,book_code):
        for book in self.books:
            if book.code == book_code and book.issued_code is not None:
                book.return_date = datetime.datetime.now()
                logging.info(f'Book "{book.title}" was returned.')
                book.issued_code = None
                book.issued_date = None
                print(f'Book "{book.title}" was returned.')
                return
        print("Book was not found or not issued to the reader.")






