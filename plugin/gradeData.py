class gradeData:
    def __init__(self, data ,courseData):
        self.course_id = data.courseID
        self.grade = data.grade
        self.year = data.year
        self.term = data.term
        self.year_taken = data.year_taken
        self.repeat = data.allowRepeat
        self.courseName = courseData.courseName
        self.credits = courseData.credits

    def getCourseID(self):
        return self.course_id

    def getGrade(self):
        return self.grade

    def getYear_taken(self):
        return self.year_taken

    def getYear(self):
        return self.year

    def getTerm(self):
        return self.term

    def getRepeat(self):
        return self.repeat

    def getCourseName(self):
        return self.courseName

    def getCredit(self):
        return str(self.credits)