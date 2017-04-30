from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class addCourseUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900,600)
        self.setWindowTitle("Class Course")
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("resources/imagess/background.png")))
        self.edu_logo = QPixmap("resources/images/educationLogo.png")
        self.setPalette(palette)
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/addCourse.ui",None)
        self.setCentralWidget(form)
        self.home_button = form.findChild(QPushButton, "homeButton")
        self.status = form.findChild(QLabel,"status")
        self.course_code = form.findChild(QLineEdit,"courseCode")
        self.course_name = form.findChild(QLineEdit,"courseName")
        self.credits = form.findChild(QLineEdit,"credit")
        self.lecturer = form.findChild(QLineEdit,"lectName")
        self.period = form.findChild(QLineEdit,"period")
        self.year = form.findChild(QLineEdit,"year")
        self.term = form.findChild(QLineEdit,"term")
        self.faculty = form.findChild(QLineEdit,"faculty")
        self.major = form.findChild(QLineEdit,"major")
        self.student_limit = form.findChild(QLineEdit,"studentLimit")
        self.building = form.findChild(QLineEdit,"building")
        self.room = form.findChild(QLineEdit,"room")
        self.picture = form.findChild(QLabel,"picture")
        self.picture.setPixmap(self.edu_logo)

        self.save_button = form.findChild(QPushButton,"saveButton")
        self.clear_button = form.findChild(QPushButton,"clearButton")

        
        self.home_button.clicked.connect(self.goHome)
        self.save_button.clicked.connect(self.saveCourse)
        self.clear_button.clicked.connect(self.clearField)

    def goHome(self):
        self.parent.changePageLoginSection("home")

    def clearField(self):
        self.course_code.setText("")
        self.course_name.setText("")
        self.credits.setText("")
        self.lecturer.setText("")
        self.period.setText("")
        self.year.setText("")
        self.term.setText("")
        self.faculty.setText("")
        self.major.setText("")
        self.student_limit.setText("")
        self.building.setText("")
        self.room.setText("")

    def saveCourse(self):
        dialog = QDialog(self)

        layout = QVBoxLayout()

        label = QLabel('Save Successful')
        layout.addWidget(label)

        close_button = QPushButton("Close Window")
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        dialog.setLayout(layout)
        dialog.show()







        
