from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class forgetPasswordUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(643,445)
        self.setWindowTitle("Edit_Profile")
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
        self.user_name = form.findChild(QLineEdit,"userName")
        self.e_mail = form.findChild(QLineEdit,"eMail")
        self.new_pw = form.findChild(QLineEdit,"newPw")
        self.confirm_pw = form.findChild(QLineEdit,"confirmPw")

        self.save_button.clicked.connect(self.savePw)
        self.close_button.clicked.connect(self.closeWindow)

    def savePw(self):
        pass

    def closeWindow(self):
        self.close()
        
