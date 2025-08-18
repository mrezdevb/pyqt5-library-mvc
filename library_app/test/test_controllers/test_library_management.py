import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from library_app.models.base import Base
from library_app.models.book import Book
from library_app.models.member import Member
from library_app.models.loan import Loan
from library_app.controllers.library_controller import LibraryController
DATABASE_URL = 'sqlite:///:memory:'
@pytest.fixture
def db_session():
	engine = create_engine(DATABASE_URL)
	TestingSessionLocal = sessionmaker(bind=engine)
	Base.metadata.create_all(bind=engine)
	session = TestingSessionLocal()
	yield session
	session.close()
@pytest.fixture
def manager(db_session):
	return LibraryController(db_session)
def test_add_book_success(manager):
	success, msg = manager.add_book('Test Book', 'Author', '12345')
	assert success is True
	assert 'successfully' in msg
def test_add_member_success(manager):
	success, msg = manager.add_member('Hohn Doe', 'mem01')
	assert success is True
	assert 'successfully' in msg
def test_add_member_duplicate(manager):
	manager.add_member('John Doe', 'mem01')
	success, msg = manager.add_member('John Doe', 'mem01')
	assert success is False
	assert 'already available' in msg
def test_add_book_duplicate(manager):
	manager.add_book('Test Book', 'Author', '12345')
	success, msg = manager.add_book('Test Book', 'Author', '12345')
	assert success is False
	assert 'already available' in msg
def test_loan_book_success(manager):
	manager.add_member('John', 'm001')
	manager.add_book('1984', 'George Orwell' ,'n001')
	
	success, msg = manager.loan_book('m001', 'n001')
	assert success is True
	assert 'Book 1984 loaned to John' in msg
def test_loan_book_already_loaned(manager):
	manager.add_member('John', 'm001')
	manager.add_book('1984', 'George Orwell', 'n001')
	manager.loan_book('m001', 'n001')
	success, msg = manager.loan_book('m001', 'n001')
	assert success is False
	assert 'Book with ISBN n001 is already borrowed' in msg
def test_loan_book_invalid_member(manager):
	manager.add_book('1984', 'George Orwell', 'b001')
	success, msg = manager.loan_book('invalid_member', 'b001')
	assert success is False
	assert 'not found' in msg
def test_loan_book_invalid_book(manager):
	manager.add_member('John', 'm001')
	success, msg = manager.loan_book('m001', 'invalid_number')
	assert success is False
	assert 'not found'
def test_return_book_success(manager):
	manager.add_book('1984', 'George Orwell', 'b001')
	manager.add_member('John', 'm001')
	manager.loan_book('m001', 'b001')
	success, msg = manager.return_book('m001', 'b001')
	assert success is True
	assert 'returned by member' in msg
def test_return_book_not_loaned(manager):
	manager.add_member('John', 'm001')
	manager.add_book('1984', 'George Orwell', 'b001')
	
	success, msg = manager.return_book('m001', 'b001')
	assert success is False
	assert 'was not loaned' in msg
def test_remove_book_success(manager):
	manager.add_book('1984', 'George Orwell', 'b001')
	success, msg = manager.remove_book('b001')
	assert success is True
	assert 'removed' in msg

def test_remove_book_not_found(manager):
	success, msg = manager.remove_book('invalid number')
	assert success is False
	assert 'not found' in msg

def test_remove_member_success(manager):
	manager.add_member('John', 'm001')
	success, msg = manager.remove_member('m001')
	assert success is True
	assert 'removed' in msg
def test_remove_member_not_found(manager):
	success, msg = manager.remove_member('invalid number')
	assert success is False
	assert 'not found' in msg
def test_show_books(manager):
	manager.add_book('book1', 'a', 'b10')
	manager.add_book('book2', 'b', 'b11')
	books = manager.show_books(filter_option=None)
	assert isinstance(books, list)
	assert len(books) == 2
	assert all(isinstance(book, Book) for book in books)
def test_show_members(manager):
	manager.add_member('John', 'm001')
	manager.add_member('Snow', 'm002')
	members = manager.show_members(raw=True)
	assert isinstance(members, list)
	assert len(members) == 2
	assert all(isinstance(member, Member) for member in members)
def test_search_books_found(manager):
	manager.add_book('The Hobbit', 'J.R.R. Tolkien', 'bk001')
	manager.add_book('The Lord of the Rings', 'J.R.R. Tolkien', 'bk002')
	results, msg = manager.search_books(keyword='Hobbit', filter_option=None)
	assert isinstance(results, list)
	assert len(results) == 1
	assert results[0].title == 'The Hobbit'

def test_search_books_not_found(manager):
	manager.add_book('The Hobbit', 'J.R.R. Tolkien', 'bk001')
	results, msg = manager.search_books(keyword='Harry Potter', filter_option=None)
	assert isinstance(results, list)
	assert len(results)==0


def test_search_members_found(manager):
	manager.add_member('John Doe', 'mem01')
	manager.add_member('Jane Smith', 'mem02')
	results = manager.search_members(keyword='Jane', raw=True)
	assert isinstance(results, list)
	assert len(results) == 1
	assert results[0].name == 'Jane Smith'


def test_search_members_not_found(manager):
	manager.add_member('Jane Smith', 'mem02')
	results = manager.search_members(keyword='Snow')
	assert isinstance(results, list)
	assert len(results)==0

