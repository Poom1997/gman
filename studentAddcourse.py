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
        self.course_id = form.findChild(QLineEdit,"lineEdit")
        
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
