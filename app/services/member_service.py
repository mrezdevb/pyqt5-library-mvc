from app.models.member import Member
from app.models.loan import Loan
from app.models.book import Book
from app.observability.logger import get_logger
from app.observability.logger_helpers import log_json
from app.db.unit_of_work import UnitOfWork
from typing import Optional, List, Tuple, Any, Union
from app.repositories.member_repository import MemberRepository
from app.repositories.loan_repository import LoanRepository


logger = get_logger('MemberService')


class MemberService:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow: UnitOfWork = uow
        self.member_repo: MemberRepository = uow.member_repo
        self.loan_repo: LoanRepository = uow.loan_repo

    def _log(self, level: str, action: str, msg: str, **kwargs: Any) -> None:
        log_json(logger, level, action, msg=msg, **kwargs)

    def add_member(self, name: str, member_id: str) -> Tuple[bool, str]:
        try:
            self._log('info', 'MEMBER_ADD_START',
                      msg=f'Attempting to add member "{name}" with ID {member_id}',
                      name=name, member_id=member_id)

            existing_member: Optional[Member] = self.member_repo.query_by_member_id(member_id).first()
            if existing_member:
                msg: str = f'Member with ID {member_id} already exists.'
                self._log('warning', 'MEMBER_ADD_EXISTS',
                          msg=msg, member_id=member_id)
                return False, msg

            self._log('info', 'MEMBER_ADD_VALID',
                      msg=f'Member "{name}" with ID {member_id} is valid for creation.',
                      name=name, member_id=member_id)

            new_member: Member = Member(name=name, member_id=member_id)
            self.member_repo.add(new_member)

            self._log('debug', 'MEMBER_ADD_PENDING_COMMIT',
                      msg=f'Member "{name}" with ID {member_id} pending commit.',
                      name=name, member_id=member_id)

            msg: str = f'Member "{name}" with ID {member_id} successfully added.'
            self._log('info', 'MEMBER_ADD_SUCCESS',
                      msg=msg, name=name, member_id=member_id)

            return True, msg

        except Exception as e:
            self._log('exception', 'MEMBER_ADD_ERROR',
                      msg=f'Error while adding member {member_id}: {str(e)}',
                      name=name, member_id=member_id, error=str(e))
            raise

    def remove_member(self, member_id: str) -> Tuple[bool, str]:
        try:
            self._log('info', 'MEMBER_REMOVE_START',
                      msg=f'Attempting to remove member {member_id}',
                      member_id=member_id)

            member: Optional[Member] = self.member_repo.query_by_member_id(member_id).first()
            if not member:
                msg: str = f"Member with ID {member_id} not found."
                self._log('warning', 'MEMBER_REMOVE_NOT_FOUND',
                          msg=msg, member_id=member_id)
                return False, msg

            self._log('info', 'MEMBER_REMOVE_FOUND',
                      msg=f'Member "{member.name}" with ID {member_id} found.',
                      member_id=member_id)

            loans: List[Loan] = self.loan_repo.query_get_loans_member(member_id).all()

            self._log('info', 'MEMBER_REMOVE_LOANS_FOUND',
                      msg=f'Member {member_id} has {len(loans)} loan(s).',
                      member_id=member_id, loans_count=len(loans))

            for loan in loans:
                if loan.book:
                    self._log('info', 'BOOK_RELEASE',
                              msg=f'Releasing book "{loan.book.title}" (ISBN {loan.book.isbn}).',
                              title=loan.book.title, isbn=loan.book.isbn)
                    loan.book.is_borrowed = False
                else:
                    self._log('warning', 'LOAN_NO_BOOK',
                              msg=f'Loan ID {loan.id} has no linked book record.',
                              loan_id=loan.id)
                self.loan_repo.remove(loan)
                self._log('debug', 'LOAN_PENDING_DELETE',
                          msg=f'Loan {loan.id} pending delete.',
                          loan_id=loan.id)
                self._log('info', 'LOAN_DELETED',
                          msg=f'Loan {loan.id} deleted.',
                          loan_id=loan.id)

            self.member_repo.remove(member)
            self._log('debug', 'MEMBER_PENDING_DELETE',
                      msg=f'Member {member_id} pending delete.',
                      member_id=member_id)

            msg: str = f"Member {member_id} removed and all borrowed books released."
            self._log('info', 'MEMBER_REMOVE_SUCCESS',
                      msg=msg, member_id=member_id)

            return True, msg

        except Exception as e:
            self._log('exception', 'MEMBER_REMOVE_ERROR',
                      msg=f'Error while removing member {member_id}: {str(e)}',
                      member_id=member_id, error=str(e))
            raise

    def _format_members(self, members: List[Member]) -> List[dict]:
        try:
            self._log('debug', 'MEMBER_FORMAT_START',
                      msg=f'Formatting {len(members)} member(s).',
                      members_count=len(members))

            result: List = []
            for member in members:
                borrowed_books: List[str] = [loan.book.title for loan in member.loans if loan.book and not loan.returned]
                self._log('debug', 'MEMBER_FORMAT_DETAIL',
                          msg=f'Member {member.member_id} has {len(borrowed_books)} active borrowed book(s).',
                          name=member.name, member_id=member.member_id, borrowed_count=len(borrowed_books))

                result.append({
                    'name': member.name,
                    'member_id': member.member_id,
                    'borrowed_books': ', '.join(borrowed_books) if borrowed_books else '-'
                })

            self._log('debug', 'MEMBER_FORMAT_COMPLETE',
                      msg='Member formatting complete.')

            return result

        except Exception as e:
            self._log('exception', 'MEMBER_FORMAT_ERROR',
                      msg=f'Error while formatting members: {str(e)}',
                      error=str(e))
            raise

    def show_members(self, raw: bool=False) -> Union[List[Member], List[dict]]:
        try:
            self._log('info', 'MEMBER_FETCH_START',
                      msg='Retrieving all members from database.')

            members: List[Member] = self.member_repo.get_members_with_loans_and_books().all()

            if not members:
                self._log('info', 'MEMBER_FETCH_EMPTY',
                          msg='No members available.')
                return []

            self._log('info', 'MEMBER_FETCH_SUCCESS',
                      msg=f'{len(members)} member(s) found.',
                      members_count=len(members))

            return members if raw else self._format_members(members)

        except Exception as e:
            self._log('exception', 'MEMBER_FETCH_ERROR',
                      msg=f'Error while fetching members: {str(e)}',
                      error=str(e))
            raise

    def search_members(self, keyword: Optional[str], raw: bool=False) -> Union[List[Member], List[dict]]:
        try:
            self._log('info', 'MEMBER_SEARCH_START',
                      msg=f'Searching members with keyword "{keyword}".',
                      keyword=keyword)

            results: List[Member] = self.member_repo.search_members_with_loans_and_books(keyword).all()

            if not results:
                self._log('info', 'MEMBER_SEARCH_EMPTY',
                          msg=f'No members found for keyword "{keyword}".',
                          keyword=keyword)
                return []

            self._log('info', 'MEMBER_SEARCH_SUCCESS',
                      msg=f'{len(results)} member(s) found for keyword "{keyword}".',
                      keyword=keyword, results_count=len(results))

            return results if raw else self._format_members(results)

        except Exception as e:
            self._log('exception', 'MEMBER_SEARCH_ERROR',
                      msg=f'Error while searching members: {str(e)}',
                      keyword=keyword, error=str(e))
            raise
