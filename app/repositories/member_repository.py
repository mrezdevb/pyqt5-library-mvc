from sqlalchemy import or_
from sqlalchemy.orm import Query, joinedload
from typing import Optional
from app.models.loan import Loan
from app.models.member import Member
from typing import Any


class MemberRepository:
    def __init__(self, db: Any):
        self.db = db

    def query_all(self) -> Query[Member]:
        return self.db.query(Member)

    def query_by_member_id(self, member_id: str) -> Query[Member]:
        return self.db.query(Member).filter(Member.member_id == member_id)

    def query_by_keyword(self, keyword: str) -> Query[Member]:
        return self.db.query(Member).filter(
            or_(
                Member.name.ilike(f"%{keyword}%"),
                Member.member_id.ilike(f"%{keyword}%"),
            )
        )

    def add(self, member: Member) -> Member:
        self.db.add(member)
        return member

    def remove(self, member: Member) -> bool:
        self.db.delete(member)
        return True

    def get_members_with_loans_and_books(self) -> Query[Member]:
        return self.db.query(Member).options(
            joinedload(Member.loans).joinedload(Loan.book)
        )

    def search_members_with_loans_and_books(
        self, keyword: Optional[str]
    ) -> Query[Member]:
        return (
            self.db.query(Member)
            .options(joinedload(Member.loans).joinedload(Loan.book))
            .filter(
                or_(
                    Member.name.ilike(f"%{keyword}%"),
                    Member.member_id.ilike(f"%{keyword}%"),
                )
            )
        )
