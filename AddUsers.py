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
        form = loader.load("resources/UI/AddUsers.ui",None)
        self.setCentralWidget(form)

        #QPushButton
        self.cancel_button = form.findChild(QPushButton,"pushButton_3")
        self.add_button = form.findChild(QPushButton,"pushButton")

        #LineEdit
        self.user_id = form.findChild(QLineEdit,"lineEdit")
        self.first_name = form.findChild(QLineEdit,"lineEdit_2")
        self.surname = form.findChild(QLineEdit,"lineEdit_3")
        self.email = form.findChild(QLineEdit,"lineEdit_4")
        self.year = form.findChild(QLineEdit,"lineEdit_5")
        self.status = form.findChild(QLineEdit,"lineEdit_6")
        self.faculty_id = form.findChild(QLineEdit,"lineEdit_7")
        self.major_id = form.findChild(QLineEdit,"lineEdit_8")
    
        #Connect
        self.cancel_button.clicked.connect(self.cancel)
        self.add_button.clicked.connect(self.add)

    def cancel(self):
        pass

    def add(self):
        pass
