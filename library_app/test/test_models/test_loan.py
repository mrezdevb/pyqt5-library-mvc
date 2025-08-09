from library_app.models.loan import Loan


def test_loan_creation_defaults():
	loan = Loan(member_id='1234', isbn='555', returned=False)
	
	assert loan.member_id == '1234'
	assert loan.isbn == '555'
	assert loan.returned is False
	assert loan.loan_date is None	
