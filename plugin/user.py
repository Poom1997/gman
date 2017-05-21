import plugin.databaseConn as database

class user:
    def __init__(self, data, address):
        self.id = data.user_id
        self.firstname = data.name
        self.surname = data.surname
        self.email = data.email
        self.address = address

    def getID(self):
        return self.id

    def getName(self):
        return self.firstname

    def getSurname(self):
        return self.surname

    def getEmail(self):
        return self.email

    def getAddress(self):
        temp = self.address.houseNumber + " " + self.address.street + "\n" + self.address.subDistrict\
               + " " + self.address.district + "\n" + self.address.province + " " + self.address.zipCode
        return temp

class student(user):
    def __init__(self, data, address, faculty, major):
        super().__init__(data,address)
        self.status = data.status
        self.faculty = faculty
        self.major = major
        self.year = data.year
        self.gpa = data.gpa

    def getFacultyName(self):
        temp = self.faculty.facultyName
        return temp

    def getMajorName(self):
        temp = self.major.degree
        return temp

    def getYear(self):
        return self.year

    def getGpa(self):
        return self.gpa

    def getStatus(self):
        return self.status

