from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.settings import settings


engine = create_engine(settings.db_url
					   , echo=False,
						 future=True
						)


SessionLocal = sessionmaker(
		autocommit=False,
		autoflush=True, 
		bind=engine,
		expire_on_commit=False,
		)




