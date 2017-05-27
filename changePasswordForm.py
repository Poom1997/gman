from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

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

        self.save_button.clicked.connect(self.savePw)
        self.close_button.clicked.connect(self.closeWindow)

    def savePw(self):
        pass

    def closeWindow(self):
        self.close()
        
