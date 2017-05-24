from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


class editProfileUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900,600)
        self.setWindowTitle("Edit_Profile")
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/editProfileStudent.ui",None)
        self.setCentralWidget(form)

        #QPushButton
        self.confirm_button = form.findChild(QPushButton,"confirmButton")
        self.cancel_button = form.findChild(QPushButton,"cancelButton")
        self.upload_button = form.findChild(QPushButton,"uploadButton")

        #LineEdit
        self.house_number_edit = form.findChild(QLineEdit,"lineEdit_9")
        self.email_edit = form.findChild(QLineEdit,"lineEdit_4")
        self.province_edit = form.findChild(QLineEdit,"lineEdit_3")
        self.district_edit = form.findChild(QLineEdit,"lineEdit")
        self.sub_district_edit = form.findChild(QLineEdit,"lineEdit_8")
        self.street_edit = form.findChild(QLineEdit,"alineEdit_7")
        self.zip_code_edit = form.findChild(QLineEdit,"lineEdit_2")
        
        

        #Connect
        self.confirm_button.clicked.connect(self.editSuccess)
        self.cancel_button.clicked.connect(self.cancel)

    def cancel(self):
        pass

    def editSuccess(self):
        pass
        

    
    

    
        
    
