from library import *

def test_book():

    book = Book(title="Dune", author="Frank Herbet", copies=3)

    assert book.title == "Dune"
    assert book.author == "Frank Herbet"
    assert book.copies == 3
