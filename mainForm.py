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


        #Upper Bar pressed
        self.home_button.clicked.connect(self.goHome)
        self.profile_button.clicked.connect(self.goProfile)
        self.grade_button.clicked.connect(self.goGrade)
        self.course_button.clicked.connect(self.goCourse)
        self.temp.clicked.connect(self.goTemp)


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
