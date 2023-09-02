from src.models.user import User

def all_users():
    return [
        User(
            _id = 0,
            email = 'defaultuser@gmail.com',
            password = '123',
            firstName = 'Default',
            lastName = 'User'
        )
    ]