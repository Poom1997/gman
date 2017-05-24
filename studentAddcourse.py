from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


class editProfileUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900,600)
        self.setWindowTitle("Add_Course")
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/studentAddcourse.ui",None)
        self.setCentralWidget(form)

        #QPushButton
        self.add_button = form.findChild(QPushButton,"pushButton_2")
        self.cancel_button = form.findChild(QPushButton,"pushButton_3")
        self.serach_button = form.findChild(QPushButton,"pushButton")

        #LineEdit
        self.search_course_id = form.findChild(QLineEdit,"lineEdit")

        #Label
        self.course_id = form.findChild(QLabel,"label_16")
        self.course_name = form.findChild(QLabel,"label_17")
        self.faculty_id = form.findChild(QLabel,"label_18")
        self.major_id = form.findChild(QLabel,"label_19")
        self.prof_id = form.findChild(QLabel,"label_20")
        self.year = form.findChild(QLabel,"label_21")
        self.semester = form.findChild(QLabel,"label_22")
        self.time = form.findChild(QLabel,"label_23")
        self.building = form.findChild(QLabel,"label_24")
        self.room = form.findChild(QLabel,"label_25")
        self.credits = form.findChild(QLabel,"label_26")
        self.max_stud = form.findChild(QLabel,"label_27")
        self.pre = form.findChild(QLabel,"label_28")
        
        #Connect
        self.add_button.clicked.connect(self.addcourse)
        self.cancel_button.clicked.connect(self.cancel)
        self.search_button.clicked.connect(self.search)

    def cancel(self):
        pass

    def addcourse(self):
        pass

    def search(self):
        pass
