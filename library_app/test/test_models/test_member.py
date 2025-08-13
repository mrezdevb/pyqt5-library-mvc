from library_app.models.member import Member

def test_member_repr():
    member = Member(name='John', member_id='1234')
    assert repr(member) == '<Member(name="John"), member_id="1234")>'

