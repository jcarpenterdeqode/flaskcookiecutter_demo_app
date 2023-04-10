from users.models import User


def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and role fields are defined correctly
    """
    user = User(username= 'test_user', email ='test_user1@gmail.com', password ='test@123')
    assert user.email == 'test_user1@gmail.com'
    assert user.password != 'FlaskIsAwesome'
