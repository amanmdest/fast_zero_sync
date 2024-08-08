from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='mcvovojuju',
        email='vovojuju@abacate.com',
        password='avocado',
    )

    session.add(user)
    session.commit()
    result = session.scalar(
        select(User).where(User.email == 'vovojuju@abacate.com')
    )

    assert result.id == 1
