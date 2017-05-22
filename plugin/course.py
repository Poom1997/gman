class course:
    def __init__(self, data):
        self.courseID = data.courseID
        self.courseName = data.courseName
        self.facultyID = data.facultyID
        self.majorID = data.majorID
        self.professorID = data.professorID
        self.year = data.year
        self.term = data.term
        self.time = data.time
        self.building = data.building
        self.room = data.room
        self.credits = data.credits
        self.maxStud = data.maxStud
        self.pre = data.pre

    def getCourseID(self):
        return self.courseID

    def getCourseName(self):
        return self.courseName

    def getFacultyID(self):
        return self.facultyID

    def getMajorID(self):
        return self.majorID

    def getProfessorID(self):
        return self.professorID

    def getYear(self):
        return str(self.year) + '/' + str(self.term)

    def getTime(self):
        return self.time

    def getLocation(self):
        return str(self.building) + ' Room:' + str(self.room)

    def getCredit(self):
        return str(self.credits)

    def getMaxStud(self):
        return str(self.maxStud)

    def getPre(self):
        return self.pre