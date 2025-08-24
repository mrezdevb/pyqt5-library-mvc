from app.models import book, loan, member  # noqa: F401


from app.db.db import engine
from app.models.base import Base


def init_db() -> None:
    _ = book, loan, member
    Base.metadata.create_all(bind=engine)
    print("tables created successfully")


if __name__ == "__main__":
    init_db()
