from library_app.models.member import Member
from library_app.models.loan import Loan
from library_app.models.book import Book
from library_app.utils.logger import get_logger
from sqlalchemy.orm import joinedload



logger = get_logger('MemberService')





class MemberService:
	def __init__(self, session):
		self.db = session

	def add_member(self, name, member_id):
		existing_member = self.db.query(Member).filter(Member.member_id == member_id).first()
		if existing_member:
			msg = 'This member is already available'
			logger.warning(msg)
			return False, msg

		new_member = Member(name=name, member_id=member_id)
		self.db.add(new_member)
		return True, 'This member successfully added'

	def remove_member(self, member_id):
		member = self.db.query(Member).filter(Member.member_id == member_id).first()
		if not member:
			msg = f'Member with member_id : {member_id} not found'
			logger.warning(msg)
			return False, msg
		
		loans = self.db.query(Loan).filter(Loan.member_id == member_id).all()
		for loan in loans:
			if loan.book:
				loan.book.is_borrowed = False
			self.db.delete(loan)
		self.db.delete(member)
		msg = f'Member with member_id : {member_id} removed and all borrowed books released'
		logger.info(msg)
		return True, msg

	def _format_members(self, members):
		result = []
		for member in members:
			borrowed_books = [
				loan.book.title for loan in member.loans if not loan.returned
			]
			result.append({
				'name':member.name,
				'member_id':member.member_id,
				'borrowed_books':', '.join(borrowed_books) if borrowed_books else '-'
			})
		return result




	def show_members(self, raw=False):
		members = self.db.query(Member).options(
			joinedload(Member.loans).joinedload(Loan.book)
		).all()
		if not members:
			logger.info('No members available')
			return []
		if raw:
			return members
		return self._format_members(members)


	def search_members(self, keyword, raw=False):
		results = self.db.query(Member).options(
			joinedload(Member.loans).joinedload(Loan.book)
		).filter(
			Member.name.ilike(f'%{keyword}%') |
			Member.member_id.ilike(f'%{keyword}%')
		).all()
		if not results:
			logger.info(f'No members found matching "{keyword}".')
			return []
		if raw:
			return results
		return self._format_members(results)
