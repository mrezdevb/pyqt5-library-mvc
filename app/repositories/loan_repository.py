from sqlalchemy.orm import Query

from app.models.loan import Loan
from typing import Any


class LoanRepository:
    def __init__(self, db: Any):
        self.db = db

    def add(self, loan: Loan) -> bool:
        self.db.add(loan)
        return True

    def count_active_loans_by_member(self, member_id: str) -> Query[Loan]:
        return self.db.query(Loan).filter(
            Loan.member_id == member_id, not Loan.returned
        )

    def get_loans_by_member(self, member_id: str, isbn: str) -> Query[Loan]:
        return self.db.query(Loan).filter(
            Loan.isbn == isbn, Loan.member_id == member_id, Loan.returned.is_(False)
        )

    def mark_returned(self, loan: Loan) -> Loan:
        loan.returned = True
        return loan

    def query_get_loans_member(self, member_id: str) -> Query[Loan]:
        return self.db.query(Loan).filter(Loan.member_id == member_id)

    def remove(self, loan: Loan) -> bool:
        self.db.delete(loan)
        return True
