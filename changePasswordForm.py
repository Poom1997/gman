from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
import plugin.databaseConn as database

class changePasswordUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(643,286)
        self.setWindowTitle("Edit_Profile")
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/changePassword.ui",None)
        self.setCentralWidget(form)

        #QPushButton
        self.save_button = form.findChild(QPushButton,"saveButton")
        self.close_button = form.findChild(QPushButton,"closeButton")

        #LineEdit
        self.current_pw = form.findChild(QLineEdit,"currentPw")
        self.new_pw = form.findChild(QLineEdit,"newPw")
        self.new_pw_check = form.findChild(QLineEdit, "passconfirm")

        self.save_button.clicked.connect(self.savePw)
        self.close_button.clicked.connect(self.closeWindow)

    def savePw(self):
        user = self.parent.getCurrentUser()
        username = user.getUsername()
        try:
            if( self.new_pw.text()=="" or self.new_pw_check.text() == ""):
                self.parent.showERROR("Invalid Password", "Password cannot be blank.")
            elif(self.new_pw.text() == self.new_pw_check.text()):
                db = database.databaseLogin()
                db.changePassword(username, self.current_pw.text(), self.new_pw.text())
                db.disconnect()
                self.parent.showOK("Password Changed", "The password has been changed.")
                self.close()
            else:
                self.parent.showERROR("Invalid Password", "Password Mismatch please try again.")
        except database.invalidQueryException:
            self.parent.showERROR("Invalid Password", "Old password is incorrect.")


    def closeWindow(self):
        self.close()
        
