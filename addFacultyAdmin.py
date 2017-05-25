from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class AddFacultyUI(QMainWindow):
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
        form = loader.load("resources/UI/addFaculty.ui",None)
        self.setCentralWidget(form)

        #Upper Bar
        self.bar_group = form.findChild(QLabel,"barLabel_2")
        self.bar_group.setPixmap(self.bar)
        self.home_button = form.findChild(QPushButton,"homeButton")
        self.profile_button = form.findChild(QPushButton,"profileButton")
        self.grade_button = form.findChild(QPushButton,"gradeButton")
        self.course_button = form.findChild(QPushButton,"courseButton")
        self.other_button = form.findChild(QPushButton, "othersButton")

        #page properties
        self.faculty_table = form.findChild(QTableWidget,"facultyTable")
        self.faculty_id = form.findChild(QLineEdit,"FacultyID")
        self.faculty_name = form.findChild(QLineEdit,"facultyName")
        self.add_button = form.findChild(QPushButton,"addFacButton")
        self.del_button = form.findChild(QPushButton,"deleteButton")


        self.header = self.faculty_table.horizontalHeader()
        self.header.setResizeMode(0,QHeaderView.ResizeToContents)
        self.header.setResizeMode(1,QHeaderView.Stretch)

        self.faculty_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.faculty_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.faculty_table.setEditTriggers(QAbstractItemView.NoEditTriggers)


        #Upper Bar pressed
        self.home_button.clicked.connect(self.goHome)
        self.profile_button.clicked.connect(self.goProfile)
        self.grade_button.clicked.connect(self.goGrade)
        self.course_button.clicked.connect(self.goCourse)
        self.other_button.clicked.connect(self.goTemp)
        self.home_button.clicked.connect(self.goHome)

        self.add_button.clicked.connect(self.add)
        self.del_button.clicked.connect(self.deletefac)
        


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

    def add(self):
        temp = {}
        temp["facultyID"] = self.faculty_id.text()
        temp["facultyName"] = self.faculty_name.text()
        
    def deletefac(self):
        pass

             
