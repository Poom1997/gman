from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


class editProfileUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900,6500)
        self.setWindowTitle("Edit_Profile")
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/EditProfileStudent.ui",None)
        self.setCentralWidget(form)

        #QPushButton
        self.confirm_button = form.findChild(QPushButton,"confirmButton")
        self.cancel_button = form.findChild(QPushButton,"cancelButton")
        self.upload_button = form.findChild(QPushButton,"uploadButton")

        #LineEdit
        self.email_edit = form.findChild(QLineEdit,"eLineEdit")
        self.village_building_edit = form.findChild(QLineEdit,"vLineEdit")
        self.soi_edit = form.findChild(QLineEdit,"sLineEdit")
        self.road_edit = form.findChild(QLineEdit,"rLineEdit")
        self.district_edit = form.findChild(QLineEdit,"dLineEdit")
        self.sub_district_edit = form.findChild(QLineEdit,"sLineEdit")
        self.country_edit = form.findChild(QLineEdit,"cLineEdit")
        self.province_edit = form.findChild(QLineEdit,"pLineEdit")
        self.zip_code_edit = form.findChild(QLineEdit,"zLineEdit")
        
        #Connect
        self.confirm_button.clicked.connect(self.editSuccess)
        self.cancel_button.clicked.connect(self.cancel)

    def cancel(self):
        pass

    def editSuccess(self):
        pass
        

    
    

    
        
    
