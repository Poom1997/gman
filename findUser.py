from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
import plugin.databaseConn as database
from sendMessageForm import sendMessageUI

class findUserUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(741,351)
        self.setWindowTitle("User_Information")
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/FindUsers.ui",None)
        self.setCentralWidget(form)

        #QPushButton
        self.cancel_button = form.findChild(QPushButton,"closeButton")
        self.search_button = form.findChild(QPushButton,"searchButton")
        self.sendMessage = form.findChild(QPushButton, "sendMessage")
        self.suspend = form.findChild(QPushButton, "suspend")
        self.block = form.findChild(QPushButton, "blockAccess")
        self.graduate = form.findChild(QPushButton, "graduate")
        self.suspend.setEnabled(False)
        self.graduate.setEnabled(False)
        self.block.setEnabled(False)

        #LineEdit
        self.search_user_id = form.findChild(QLineEdit,"enterUser")

        #Label
        self.user_id = form.findChild(QLabel,"userID")
        self.user_name = form.findChild(QLabel, "userName")
        self.first_name = form.findChild(QLabel,"firstName")
        self.surname = form.findChild(QLabel,"surName")
        self.email = form.findChild(QLabel,"eMail")
        self.type = form.findChild(QLabel,"type")
        self.faculty_id = form.findChild(QLabel,"facultyID")
        self.major_id = form.findChild(QLabel,"majorID")
    
        #Connect
        self.search_user_id.returnPressed.connect(self.search)
        self.cancel_button.clicked.connect(self.cancel)
        self.search_button.clicked.connect(self.search)
        self.sendMessage.clicked.connect(self.sendMessageUser)
        self.suspend.clicked.connect(self.suspend)
        self.graduate.clicked.connect(self.graduate)
        self.block.clicked.connect(self.block)

    def cancel(self):
        self.close()

    def search(self):
        db = database.databaseLogin()
        data = db.getInformationUser(self.search_user_id.text())
        if(data[0] is not None and data[1] is not None):
            self.user_id.setText(data[0].user_id)
            self.user_name.setText(data[0].username)
            self.first_name.setText(data[1].name)
            self.surname.setText(data[1].surname)
            self.email.setText(data[1].email)
            self.status = int(data[0].user_type)
            if (self.status == 0):
                self.type.setText("STUDENT")
                self.suspend.setEnabled(True)
                self.graduate.setEnabled(True)
                self.block.setEnabled(True)
                self.faculty_id.setText(str(data[1].facultyID))
                self.major_id.setText(str(data[1].majorID))
            elif (self.status == 1):
                self.type.setText("PROFESSOR")
                self.suspend.setEnabled(True)
                self.graduate.setText("Retire")
                self.graduate.setEnabled(True)
                self.block.setEnabled(False)
                self.faculty_id.setText(str(data[1].facultyID))
                self.major_id.setText("N/A")
            elif (self.status == 2):
                self.type.setText("ADMINISTRATOR")
                self.suspend.setEnabled(False)
                self.graduate.setEnabled(False)
                self.block.setEnabled(False)
                self.faculty_id.setText("N/A")
                self.major_id.setText("N/A")

    def sendMessageUser(self):
        self.createM = sendMessageUI(self.search_user_id.text(),parent=self.parent)
        self.createM.show()

    def suspend(self):
        pass

    def graduate(self):
        pass

    def block(self):
        pass

