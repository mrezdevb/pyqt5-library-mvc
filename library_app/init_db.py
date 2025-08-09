from library_app.models.member import Member
from library_app.models.book import Book
from library_app.models.loan import Loan
from library_app.models.base import Base
from library_app.db import engine

def init_db():
	Base.metadata.create_all(bind=engine)
	print('tables created successfully')

if __name__=='__main__':
	init_db()
