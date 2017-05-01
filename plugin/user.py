import plugin.databaseConn as database

class user:
    def __init__(self, data):
        self.firstname = data.name
        self.surname = data.surname
        self.email = data.email
        self.address = None

class student(user):
    def __init__(self, data):
        super().__init__(self, data)
        pass


