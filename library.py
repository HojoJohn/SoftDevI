import csv

class Book:

    __slots__ = [ 'title','author','copies']

    def __init__(self,title,author,copies = 1):

        self.title = title
        self.author = author
        self.copies = copies

class Patron:
    __slots__ = [ 'Id','name','has','want']

    def __init__(self,patron_id="000-0000",name= "reader"):

        self.Id = patron_id
        self.name = name
        self.has = []
        self.wants = list()

class CardCatalog:
    __slots__ = [ 'books_by_author','books_by_title']

    def __init__(self):

        self.books_by_title = {}
        self.books_by_author = {}


class Library:
    __slots__ = [ 'on_shelves','patrons','card_catalog']

    def __init__(self,shelf,inventory_filename):
        self.on_shelves = []
        self.patrons = []
        self.card_catalog = CardCatalog()

        with open(inventory_filename) as csv_file:

            csv_reader = csv.reader(csv_file)

            next(csv_file)

            for record in csv_reader:
                count = int(record[2])

                book = Book(record[0],record[1],count)

                self.on_shelves.append(book)

                books_by_author = self.card_catalog.books_by_author

            if book.author not in books_by_author:
                books_by_author[book.author] = []
            
            books_by_author[book.author] += [book]
            books_by_title = self.card_catalog.books_by_title

            if book.title not in books_by_title:
                books_by_title[book.title] = []
            books_by_title[book.title] += [book]


