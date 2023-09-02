class User:
    def __init__(self, _id, email, password, firstName, lastName):
        self._id = _id
        self.email = email
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
    
    def json(self):
        return {
            '_id': self._id,
            'email': self.email,
            'password': self.password,
            'firstName': self.firstName,
            'lastName': self.lastName
        }