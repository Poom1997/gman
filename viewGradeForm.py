from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from EditProfileStudent import editProfileUI

class viewGradeUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900,600)
        self.setWindowTitle("Grades")
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("resources/imagess/background.png")))
        self.setPalette(palette)
        self.bar = QPixmap("resources/images/bar.png")
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/viewGrade.ui",None)
        self.setCentralWidget(form)

        #Upper Bar
        self.bar_group = form.findChild(QLabel,"barLabel_2")
        self.bar_group.setPixmap(self.bar)
        self.home_button = form.findChild(QPushButton,"homeButton")
        self.profile_button = form.findChild(QPushButton,"profileButton")
        self.grade_button = form.findChild(QPushButton,"gradeButton")
        self.course_button = form.findChild(QPushButton,"courseButton")
        self.temp = form.findChild(QPushButton, "temp")

        #page properties
        self.print_button = form.findChild(QPushButton, "printButton")
        self.this_term = form.findChild(QTableWidget,"thisTerm")
        self.all_term = form.findChild(QTableWidget,"alLTerm")
        self.gpa_input = form.findChild(QLabel,"gpaInp")
        self.gps_input = form.findChild(QLabel,"gpaInp")
        self.crs_input = form.findChild(QLabel,"gpaInp")
        self.status_input = form.findChild(QLabel,"gpaInp")

        #Upper Bar pressed
        self.home_button.clicked.connect(self.goHome)
        self.profile_button.clicked.connect(self.goProfile)
        self.grade_button.clicked.connect(self.goGrade)
        self.course_button.clicked.connect(self.goCourse)
        self.temp.clicked.connect(self.goTemp)
        self.home_button.clicked.connect(self.goHome)

    def goHome(self):
        self.parent.changePageLoginSection("home")

    def goProfile(self):
        self.parent.changePageLoginSection("profile")

    def goGrade(self):
        self.parent.changePageLoginSection("grade")

    def goCourse(self):
        self.parent.changePageLoginSection("course")

    def goTemp(self):
        self.parent.changePageLoginSection("addcourse")
        

    def updatePage(self):
        data = self.parent.getCurrentUser()
        self.id.setText(data.getID())
        self.name.setText(data.getName())
        self.surname.setText(data.getSurname())
        self.email.setText(data.getEmail())
        self.faculty.setText(data.getFacultyName())
        self.major.setText(data.getMajorName())
        self.year.setText(data.year)
        self.address.setText(data.getAddress())

        #Status
        status = data.getStatus()
        if(status == 0):
            self.student_status.setText("Learning")
        elif(status==1):
            self.student_status.setText("Probation")
        elif (status == 2):
            self.student_status.setText("Retired")
        elif (status == 3):
            self.student_status.setText("Withdrawn")
        elif (status == 4):
            self.student_status.setText("Suspended")
        else:
            self.student_status.setText("Unknown")
