from library_app.models import book, member, loan
from library_app.models.base import Base
from library_app.db import engine


def init_db():
	Base.metadata.create_all(bind=engine)
	print('tables created successfully')

if __name__=='__main__':
	init_db()
