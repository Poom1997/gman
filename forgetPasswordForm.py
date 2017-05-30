from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
import plugin.databaseConnect as database
from datetime import datetime

class forgetPasswordUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(643,445)
        self.setWindowTitle("Reset Password")
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/forgetPw.ui",None)
        self.setCentralWidget(form)

        #QPushButton
        self.save_button = form.findChild(QPushButton,"saveButton")
        self.close_button = form.findChild(QPushButton,"closeButton")

        #LineEdit
        self.user_id = form.findChild(QLineEdit,"userID")
        self.user_name = form.findChild(QLineEdit,"username")
        self.e_mail = form.findChild(QLineEdit,"eMail")
        self.new_pw = form.findChild(QLineEdit,"newPw")
        self.confirm_pw = form.findChild(QLineEdit,"confirmPw")

        self.save_button.clicked.connect(self.savePw)
        self.close_button.clicked.connect(self.closeWindow)

    ##Use for saving new password by checking user ID,name and email##
    def savePw(self):
        id = self.user_id.text()
        username = self.user_name.text()
        email = self.e_mail.text()
        if (self.new_pw.text() == "" or self.confirm_pw.text() == ""):
            self.parent.showERROR("Invalid Password", "Password cannot be blank.")
        elif(self.new_pw.text() == self.confirm_pw.text()):
            passwd = self.new_pw.text()
            db = database.databaseLogin()
            db.resetPassword(id, username, email, passwd)
            db = database.databaseMessage()
            db.sendMessage(id, "SYSTEM", "Attempted Reset Password", datetime.now())
            db.disconnect()
            self.parent.showOK("Password Changed?", "If all the information are correctly given, the password has been changed. \nThe User will be notified.")
            self.closeWindow()
        else:
            self.parent.showERROR("Invalid Password", "Password Mismatch please try again.")

    def closeWindow(self):
        self.close()
        
