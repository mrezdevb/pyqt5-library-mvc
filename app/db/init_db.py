from app.models import book, member, loan
from app.models.base import Base
from app.db.db import engine




def init_db() -> None:
	Base.metadata.create_all(bind=engine)
	print('tables created successfully')



if __name__=='__main__':
	init_db()
