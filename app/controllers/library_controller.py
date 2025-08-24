from typing import ClassVar, Optional, Tuple, Any

from PyQt5.QtCore import QObject, pyqtSignal

from app.db.unit_of_work import UnitOfWork
from app.models.book import Book
from app.models.member import Member
from app.observability.log_context import get_trace_id
from app.observability.logger import get_logger
from app.observability.trace_decorators import traced
from app.services.book_service import BookService
from app.services.loan_service import LoanService
from app.services.member_service import MemberService

log = get_logger("LibraryController")


class LibraryController(QObject):

    books_updated: ClassVar[pyqtSignal] = pyqtSignal()
    members_updated: ClassVar[pyqtSignal] = pyqtSignal()

    def __init__(self, uow: Optional[UnitOfWork] = None) -> None:

        super().__init__()
        self.uow: UnitOfWork = uow or UnitOfWork()
        self.book_service: BookService = BookService(self.uow)
        self.member_service: MemberService = MemberService(self.uow)
        self.loan_service: LoanService = LoanService(self.uow)

    def _commit_ok(self, ok: bool) -> bool:

        action: str = "TX_COMMIT" if ok else "TX_ROLLBACK"

        log.info({"action": action, "trace_id": get_trace_id()})

        if ok:
            self.uow.commit()

        else:
            self.uow.rollback()

        return ok

    @traced("ADD_BOOK")
    def add_book(self, title: str, author: str, isbn: str) -> Tuple[bool, str]:
        ok, msg = self.book_service.add_book(title, author, isbn)

        if self._commit_ok(ok):
            self.books_updated.emit()

        return ok, msg

    @traced("REMOVE_BOOK")
    def remove_book(self, isbn: str) -> Tuple[bool, str]:
        ok, msg = self.book_service.remove_book(isbn)

        if self._commit_ok(ok):
            self.books_updated.emit()
            self.members_updated.emit()

        return ok, msg

    @traced("ADD_MEMBER")
    def add_member(self, name: str, member_id: str) -> Tuple[bool, str]:
        ok, msg = self.member_service.add_member(name, member_id)

        if self._commit_ok(ok):
            self.members_updated.emit()

        return ok, msg

    @traced("REMOVE_MEMBER")
    def remove_member(self, member_id: str) -> Tuple[bool, str]:
        ok, msg = self.member_service.remove_member(member_id)

        if self._commit_ok(ok):
            self.members_updated.emit()
            self.books_updated.emit()

        return ok, msg

    @traced("LOAN_BOOK")
    def loan_book(self, member_id: str, isbn: str) -> Tuple[bool, str]:
        ok, msg = self.loan_service.loan_book(member_id, isbn)

        if self._commit_ok(ok):
            self.books_updated.emit()
            self.members_updated.emit()

        return ok, msg

    @traced("RETURN_BOOK")
    def return_book(self, member_id: str, isbn: str) -> Tuple[bool, str]:
        ok, msg = self.loan_service.return_book(member_id, isbn)

        if self._commit_ok(ok):
            self.books_updated.emit()
            self.members_updated.emit()

        return ok, msg

    @traced("SHOW_BOOKS")
    def show_books(self, filter_option: Optional[str] = None) -> list[Book]:

        return self.book_service.show_books(filter_option)

    @traced("SEARCH_BOOKS")
    def search_books(self, keyword: str, filter_option: str) -> Tuple[list[Book], str]:

        return self.book_service.search_books(keyword, filter_option)

    @traced("SHOW_MEMBERS")
    def show_members(self, raw: bool = False) -> list[Member] | list[dict[Any, Any]]:

        return self.member_service.show_members(raw)

    @traced("SEARCH_MEMBERS")
    def search_members(
        self, keyword: str, raw: bool = False
    ) -> list[Member] | list[dict[Any, Any]]:

        return self.member_service.search_members(keyword, raw)

    def close(self) -> None:
        self.uow.close()
