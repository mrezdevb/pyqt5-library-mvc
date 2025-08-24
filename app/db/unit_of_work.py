from types import TracebackType
from typing import Optional, Any, Type

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.db.db import SessionLocal
from app.repositories.book_repository import BookRepository
from app.repositories.loan_repository import LoanRepository
from app.repositories.member_repository import MemberRepository


class UnitOfWork:
    session: Session
    book_repo: BookRepository
    member_repo: MemberRepository
    loan_repo: LoanRepository

    def __init__(self, session_factory: Any = SessionLocal) -> None:
        self.session = session_factory()
        self.book_repo = BookRepository(self.session)
        self.member_repo = MemberRepository(self.session)
        self.loan_repo = LoanRepository(self.session)

    def commit(self) -> None:
        try:
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def rollback(self) -> None:
        self.session.rollback()

    def close(self) -> None:
        self.session.close()

    def __enter__(self) -> "UnitOfWork":
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional["TracebackType"],
    ) -> None:
        if exc_type:
            self.rollback()
        else:
            self.commit()
        self.close()
