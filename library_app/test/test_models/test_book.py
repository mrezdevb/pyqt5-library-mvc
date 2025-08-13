from library_app.models.book import Book


def test_book_repr():
	book = Book(title='Fear of Flying', author='Erica Jong', isbn='555')
	assert repr(book) == '<Book(title="Fear of Flying", author="Erica Jong", isbn="555")>'
