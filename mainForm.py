from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class mainUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900,600)
        self.setWindowTitle("Main")
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("resources/imagess/background.png")))
        self.setPalette(palette)
        self.bar = QPixmap("resources/images/bar.png")
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/main.ui",None)
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
        self.logout_button = form.findChild(QPushButton,"logoutButton")


        #Upper Bar pressed
        self.home_button.clicked.connect(self.goHome)
        self.profile_button.clicked.connect(self.goProfile)
        self.grade_button.clicked.connect(self.goGrade)
        self.course_button.clicked.connect(self.goCourse)
        self.temp.clicked.connect(self.goTemp)
        self.temp2.clicked.connect(self.goTemp2)

        self.logout_button.clicked.connect(self.goLogout)


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
            self.parent.changePageLoginSection("addcourse")
        elif (data.type() == "PROFESSOR"):
            self.parent.changePageLoginSection("addcourse")
        elif (data.type() == "ADMIN"):
            self.parent.changePageLoginSection("addcourse")
        self.parent.changePageLoginSection("addcourse")
    

    def goTemp2(self):
        data = self.parent.getCurrentUser()
        if (data.type() == "STUDENT"):
            self.parent.changePageLoginSection("login")
        elif (data.type() == "PROFESSOR"):
            self.parent.changePageLoginSection("login")
        elif (data.type() == "ADMIN"):
            self.parent.changePageLoginSection("otherOption")

    def goLogout(self):
        self.parent.changePageLoginSection("login")

    def updatePage(self):
        data = self.parent.getCurrentUser()
        if (data.type() == "ADMIN"):
            self.grade_button.setText("Faculties")
            self.course_button.setText("Majors")
            self.temp.setText("Courses")
            self.temp2.setText("Other options")

    
        
        
