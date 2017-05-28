from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
import plugin.databaseConn as database

class findProfByCourseIDUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(741,351)
        self.setWindowTitle("User_Information")
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/searchProfByCourseID.ui",None)
        self.setCentralWidget(form)

        #QPushButton
        self.cancel_button = form.findChild(QPushButton,"closeButton")
        self.search_button = form.findChild(QPushButton,"searchButton")

        #LineEdit
        self.search_user_id = form.findChild(QLineEdit,"courseID")

        #Label
        self.user_id = form.findChild(QLabel,"userID")
        self.user_name = form.findChild(QLabel, "userName")
        self.first_name = form.findChild(QLabel,"firstName")
        self.surname = form.findChild(QLabel,"surName")
        self.email = form.findChild(QLabel,"eMail")
        self.type = form.findChild(QLabel,"type")
        self.faculty_id = form.findChild(QLabel,"facultyID")
    
        #Connect
        self.search_user_id.returnPressed.connect(self.search)
        self.cancel_button.clicked.connect(self.cancel)
        self.search_button.clicked.connect(self.search)

    def cancel(self):
        self.close()

    def search(self):
        pass
