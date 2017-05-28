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
        self.suspend.clicked.connect(self.suspendUser)
        self.graduate.clicked.connect(self.graduateUser)
        self.block.clicked.connect(self.blockUser)

    def cancel(self):
        self.close()

    def search(self):
        self.db = database.databaseLogin()
        data = self.db.getInformationUser(self.search_user_id.text())
        if(data[0] is not None and data[1] is not None):
            self.user_id.setText(data[0].user_id)
            self.user_name.setText(data[0].username)
            self.first_name.setText(data[1].name)
            self.surname.setText(data[1].surname)
            self.email.setText(data[1].email)
            self.status = int(data[0].user_type)
            self.suspendStatus = data[1].status

            if (self.status == 0):
                self.type.setText("STUDENT")
                self.block.setText("Block")
                self.suspend.setText("Suspend")
                self.suspend.setEnabled(True)
                self.graduate.setEnabled(True)
                self.block.setEnabled(True)
                self.faculty_id.setText(str(data[1].facultyID))
                self.major_id.setText(str(data[1].majorID))
            elif (self.status == 1):
                self.type.setText("PROFESSOR")
                self.block.setText("Block")
                self.suspend.setText("Suspend")
                self.suspend.setEnabled(True)
                self.graduate.setText("Retire")
                self.graduate.setEnabled(True)
                self.block.setEnabled(True)
                self.faculty_id.setText(str(data[1].facultyID))
                self.major_id.setText("N/A")
            elif (self.status == 2):
                self.type.setText("ADMINISTRATOR")
                self.block.setText("Block")
                self.suspend.setEnabled(False)
                self.graduate.setEnabled(False)
                self.block.setEnabled(False)
                self.faculty_id.setText("N/A")
                self.major_id.setText("N/A")

            print(self.suspendStatus)
            if (str(self.suspendStatus) == "4"):
                self.parent.showERROR("User Suspended", "User " + self.first_name.text() + " " + self.surname.text() + " is being suspended.")
                self.suspend.setText("Un-Suspend")
                self.graduate.setEnabled(False)

            if (str(self.suspendStatus) == "5"):
                self.parent.showOK("User Locked", "User " + self.first_name.text() + " " + self.surname.text() + " has been locked due to graduation or retirement.")
                self.suspend.setEnabled(False)
                self.graduate.setEnabled(False)

            if (str(self.suspendStatus) == "6"):
                self.parent.showOK("User Blocked", "User " + self.first_name.text() + " " + self.surname.text() + " has been blocked from the system.")
                self.block.setText("Un-Block")
                self.suspend.setEnabled(False)
                self.graduate.setEnabled(False)

    def sendMessageUser(self):
        self.createM = sendMessageUI(self.search_user_id.text(),parent=self.parent)
        self.createM.show()

    def suspendUser(self):
        val = 0
        if(self.parent.showCONFIRM("Are you sure?", "Are you sure you want to toggle suspension status for the user?")):
            if(str(self.suspendStatus) != "4"):
                if(self.status == 0):
                    val = self.db.suspendUser("SUSP", "STUDENT", self.user_id.text())
                if(self.status == 1):
                    val = self.db.suspendUser("SUSP","PROFESSOR", self.user_id.text())
            if (str(self.suspendStatus) == "4"):
                if (self.status == 0):
                    val = self.db.suspendUser("UNSUSP", "STUDENT", self.user_id.text())
                if (self.status == 1):
                    val = self.db.suspendUser("UNSUSP", "PROFESSOR", self.user_id.text())
        if(val == 1):
            self.parent.showOK("User status changed", "User " + self.first_name.text() + " " + self.surname.text() + " suspension status has been changed")
        self.search()

    def graduateUser(self):
        val = 0
        if (self.status == 0):
            if (self.parent.showCONFIRM("Are you sure?", "Are you sure you want lock this user? Once locked, status cannot be revoked.")):
                val = self.db.retireUser("STUDENT", self.user_id.text())
        if (self.status == 1):
            if (self.parent.showCONFIRM("Are you sure?", "Are you sure you want retire this user? Once retired, status cannot be revoked.")):
                val = self.db.retireUser("PROFESSOR", self.user_id.text())
        if (val == 1):
            self.parent.showOK("User status changed", "User " + self.first_name.text() + " " + self.surname.text() + " has been locked.")
        self.search()

    def blockUser(self):
        val = 0
        if (self.parent.showCONFIRM("Are you sure?", "Are you sure you want toggle block status this user?")):
            if (str(self.suspendStatus) == "6"):
                print("INHERE")
                print(self.status)
                val = self.db.blockUser("UNBLOCK",self.status, self.user_id.text())
            else:
                val = self.db.blockUser("BLOCK",self.status, self.user_id.text())
        if (val == 1):
            self.parent.showOK("User status changed", "User " + self.first_name.text() + " " + self.surname.text() + " block status has been changed.")
        self.search()

