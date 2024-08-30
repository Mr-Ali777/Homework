class Book:
    def __init__(self, title, author, code):
        self.title = title
        self.author = author
        self.code = code
        self.issued_code = None
        self.issued_date = None
        self.return_date = None


class Reader:
    def __init__(self, first_name, last_name, reader_id):
        self.first_name = first_name
        self.last_name = last_name
        self.reader_id = reader_id
