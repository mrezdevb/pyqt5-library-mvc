from app.models.loan import Loan
from app.db.db import SessionLocal


class LoanRepository:
    def __init__(self, db: SessionLocal):
        self.db = db

    def add(self, loan):
        self.db.add(loan)
        return True
    
    def count_active_loans_by_member(self, member_id):
        return self.db.query(Loan).filter(
				Loan.member_id == member_id,
                Loan.returned == False
			)
         
    
    def get_loans_by_member(self, member_id, isbn):
        return self.db.query(Loan).filter(
				Loan.isbn == isbn,
				Loan.member_id == member_id,
				Loan.returned == False
			)
    
    def mark_returned(self, loan):
        loan.returned = True
        return loan
    

    def query_get_loans_member(self, member_id):
        return self.db.query(Loan).filter(Loan.member_id == member_id)
    

    def remove(self, loan):
        self.db.delete(loan)
        return True