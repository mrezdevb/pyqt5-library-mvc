from app.models.loan import Loan
from app.db.db import SessionLocal
from sqlalchemy.orm import Query

class LoanRepository:
    def __init__(self, db: SessionLocal):
        self.db: SessionLocal = db

    def add(self, loan: Loan) -> bool:
        self.db.add(loan)
        return True
    
    def count_active_loans_by_member(self, member_id: str) -> Query[Loan]:
        return self.db.query(Loan).filter(
				Loan.member_id == member_id,
                Loan.returned == False
			)
         
    
    def get_loans_by_member(self, member_id: str, isbn: str) -> Query[Loan]:
        return self.db.query(Loan).filter(
				Loan.isbn == isbn,
				Loan.member_id == member_id,
				Loan.returned == False
			)
    
    def mark_returned(self, loan: Loan) -> Loan:
        loan.returned = True
        return loan
    

    def query_get_loans_member(self, member_id: str) -> Query[Loan]:
        return self.db.query(Loan).filter(Loan.member_id == member_id)
    

    def remove(self, loan: Loan) -> bool:
        self.db.delete(loan)
        return True