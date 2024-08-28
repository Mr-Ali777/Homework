import datetime
from gen_book import Book
from gen_reader import Reader


class Library:
    def __init__(self):
        self.books = []
        self.readers = []
        self.issued_books = []

    def new_books(self, title, author, code):
        self.books.append(Book(title, author, code))

    def reader(self, first_name, last_name, reader_id):
        for reader in self.readers:
            if reader.reader_id == reader_id:
                print(f"Reader with this ID already registered.")
                return
            new_reader = Reader(first_name, last_name, reader_id)
            self.readers.append(new_reader)
            print(f"New reader {first_name} {last_name} add in library")

    def list_available_books(self):
        for book in self.books:
            print(f"Book {book.title}, {book.author}, {book.code}")

    def list_issued_books(self):
        return [book for book in self.books if book.is_issued]

    def borrow_book(self,reader_id,book_code):
        reader = next((r for r in self.readers if r.reader_id == reader_id), None)
        book = next((b for b in self.books if b.book_code == book_code), None)
        if not reader:
            print("Reader not found")
            return
        if not book:
            print("Book with this code not found")
            return
        if not book.is_available:
            print("Book alreade issued to another reader")
            return

        book.is_available = False
        reader.borrowed_books.append((book, datetime.now()))
        print(f"Book '{book.title} issued to the reader {reader.first_name} {reader.last_name}.")

    def return_book(self, reader_id, book_code):
        reader = next((r for r in self.readers if r.reader_id == reader_id), None)
        book = next((b for b in self.books if b.code == book_code), None)
        if not reader:
            print("Reader not found")
            return
        if book not in [b[0] for b in reader.borrowed_books]:
            print("This book not with reader")
        return

        reader.borrowed_books = [b for b in reader.borrowed_books if b[0] != book]
        book.is_available = True
        print(f"Book '{book.title}' was return by reader {reader.first_name} {reader.last_name}")





