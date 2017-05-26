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
        form = loader.load("resources/UI/FindUsers.ui",None)
        self.setCentralWidget(form)

        #QPushButton
        self.cancel_button = form.findChild(QPushButton,"pushButton_3")
        self.serach_button = form.findChild(QPushButton,"pushButton")

        #LineEdit
        self.search_course_id = form.findChild(QLineEdit,"lineEdit")

        #Label
        self.user_id = form.findChild(QLabel,"label_16")
        self.first_name = form.findChild(QLabel,"label_17")
        self.surname = form.findChild(QLabel,"label_18")
        self.email = form.findChild(QLabel,"label_19")
        self.year = form.findChild(QLabel,"label_21")
        self.status = form.findChild(QLabel,"label_22")
        self.faculty_id = form.findChild(QLabel,"label_23")
        self.major_id = form.findChild(QLabel,"label_24")
    
        #Connect
        self.cancel_button.clicked.connect(self.cancel)
        self.search_button.clicked.connect(self.search)

    def cancel(self):
        pass

    def search(self):
        pass
