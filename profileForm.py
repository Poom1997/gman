from PySide.QtGui import *
from PySide.QtUiTools import *
from EditProfileStudent import editProfileUI
from sendMessageForm import sendMessageUI
from changePasswordForm import changePasswordUI

class profileUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900,600)
        self.setWindowTitle("Profile")
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("resources/images/background.png")))
        self.setPalette(palette)
        self.bar = QPixmap("resources/images/bar.png")
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/profile.ui",None)
        self.setCentralWidget(form)

        #Upper Bar
        self.bar_group = form.findChild(QLabel,"barLabel")
        self.bar_group.setPixmap(self.bar)
        self.home_button = form.findChild(QPushButton,"homeButton")
        self.profile_button = form.findChild(QPushButton,"profileButton")
        self.grade_button = form.findChild(QPushButton,"gradeButton")
        self.course_button = form.findChild(QPushButton,"courseButton")
        self.temp = form.findChild(QPushButton, "temp")
        self.temp2 = form.findChild(QPushButton, "temp2")

        #page properties
        self.home_button = form.findChild(QPushButton, "homeButton")
        self.edit_button = form.findChild(QPushButton, "editButton")
        self.changepassword_button = form.findChild(QPushButton, "changePasswordButton")
        self.status = form.findChild(QLabel,"status")
        self.id = form.findChild(QLabel,"id")
        self.name = form.findChild(QLabel,"name")
        self.surname = form.findChild(QLabel,"surname")
        self.email = form.findChild(QLabel,"email")
        self.faculty = form.findChild(QLabel,"faculty")
        self.major = form.findChild(QLabel,"major")
        self.year = form.findChild(QLabel,"year")
        self.student_status = form.findChild(QLabel,"sstatus")
        self.address = form.findChild(QLabel,"address")
        self.profile_pic = form.findChild(QLabel, "profile_pic")


        #Upper Bar pressed
        self.home_button.clicked.connect(self.goHome)
        self.profile_button.clicked.connect(self.goProfile)
        self.grade_button.clicked.connect(self.goGrade)
        self.course_button.clicked.connect(self.goCourse)
        self.temp.clicked.connect(self.goTemp)
        self.temp2.clicked.connect(self.goTemp2)

        self.edit_button.clicked.connect(self.editProfile)
        self.changepassword_button.clicked.connect(self.changePassword)
        

    def goHome(self):
        self.parent.changePageLoginSection("home")

    def goProfile(self):
        self.parent.changePageLoginSection("profile")

    def goGrade(self):
        data = self.parent.getCurrentUser()
        if (data.type() == "STUDENT"):
            self.parent.changePageLoginSection("studentGrade")
        elif (data.type() == "PROFESSOR"):
            self.parent.changePageLoginSection("grade")
        elif (data.type() == "ADMIN"):
            self.parent.changePageLoginSection("addfaculties")

    def goCourse(self):
        data = self.parent.getCurrentUser()
        if (data.type() == "STUDENT"):
            self.parent.changePageLoginSection("studentCourse")
        elif (data.type() == "PROFESSOR"):
            self.parent.changePageLoginSection("course")
        elif (data.type() == "ADMIN"):
            self.parent.changePageLoginSection("addmajor")
        

    def goTemp(self):
        data = self.parent.getCurrentUser()
        if (data.type() == "STUDENT"):
            self.createM = sendMessageUI(parent = self.parent)
            self.createM.show()
        elif (data.type() == "PROFESSOR"):
            self.createM = sendMessageUI(parent = self.parent)
            self.createM.show()
        elif (data.type() == "ADMIN"):
            self.parent.changePageLoginSection("addcourse")

    def goTemp2(self):
        data = self.parent.getCurrentUser()
        if (data.type() == "STUDENT"):
            self.parent.changePageLoginSection("login")
        elif (data.type() == "PROFESSOR"):
            self.parent.changePageLoginSection("login")
        elif (data.type() == "ADMIN"):
            self.parent.changePageLoginSection("otherOption")

    def editProfile(self):
        self.edit = editProfileUI(parent = self.parent)
        self.edit.updatePage()
        self.edit.show()

    def changePassword(self):
        self.change = changePasswordUI(parent=self.parent)
        self.change.show()

    def updatePage(self):
        data = self.parent.getCurrentUser()
        if(data.type() == "STUDENT"):
            self.id.setText(data.getID())
            self.name.setText(data.getName())
            self.surname.setText(data.getSurname())
            self.email.setText(data.getEmail())
            self.faculty.setText(data.getFacultyName())
            self.major.setText(data.getMajorName())
            self.year.setText(data.year)
            self.address.setText(data.getAddress())

            # Status
            status = data.getStatus()
            if (status == 0):
                self.student_status.setText("Learning")
            elif (status == 1):
                self.student_status.setText("Probation")
            elif (status == 2):
                self.student_status.setText("Retired")
            elif (status == 3):
                self.student_status.setText("Withdrawn")
            elif (status == 4):
                self.student_status.setText("Suspended")
            elif (status == 5):
                self.student_status.setText("Alumni/Withdrawn")
            else:
                self.student_status.setText("Unknown")

        elif (data.type() == "PROFESSOR"):
            self.id.setText(data.getID())
            self.name.setText(data.getName())
            self.surname.setText(data.getSurname())
            self.email.setText(data.getEmail())
            self.faculty.setText(data.getFacultyName())
            self.major.setText(data.getMajorName())
            self.year.setText(data.getYear())
            self.address.setText(data.getAddress())

            # Status
            status = data.getStatus()
            if (status == 0):
                self.student_status.setText("Lecturer")
            elif (status == 1):
                self.student_status.setText("Assist. Prof.")
            elif (status == 2):
                self.student_status.setText("Assoc. Prof.")
            elif (status == 3):
                self.student_status.setText("Professor.")
            elif (status == 4):
                self.student_status.setText("Suspended")
            elif (status == 5):
                self.student_status.setText("Retired")
            else:
                self.student_status.setText("Unknown")

        elif (data.type() == "ADMIN"):
            self.id.setText(data.getID())
            self.name.setText(data.getName())
            self.surname.setText(data.getSurname())
            self.email.setText(data.getEmail())
            self.faculty.setText(data.getFacultyName())
            self.major.setText(data.getMajorName())
            self.year.setText(data.getYear())
            self.address.setText(data.getAddress())

            # change Button Name 
            self.grade_button.setText("Faculties")
            self.course_button.setText("Majors")
            self.temp.setText("Courses")
            self.temp2.setText("Other options")

            # Status
            self.student_status.setText("Admin")

        self.profile_pic.setPixmap(QPixmap(data.pictureGen()))
        data.pictureDataProtect()


