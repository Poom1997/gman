from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
import plugin.databaseConnect as database
import plugin.image as imageHandle

class editProfileUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(770,415)
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
        self.house_number_edit = form.findChild(QLineEdit,"house")
        self.email_edit = form.findChild(QLineEdit,"email")
        self.province_edit = form.findChild(QLineEdit,"province")
        self.district_edit = form.findChild(QLineEdit,"district")
        self.sub_district_edit = form.findChild(QLineEdit,"sdistrict")
        self.street_edit = form.findChild(QLineEdit,"street")
        self.zip_code_edit = form.findChild(QLineEdit,"zip")

        #Connect
        self.confirm_button.clicked.connect(self.editData)
        self.cancel_button.clicked.connect(self.cancel)
        self.upload_button.clicked.connect(self.photo)

        #Page Properties
        self.profile_pic = form.findChild(QLabel, "picture")

    def updatePage(self):
        self.data = self.parent.getCurrentUser()
        curAddress = self.data.getAddressRecord()
        self.house_number_edit.setText(curAddress.houseNumber)
        self.email_edit.setText(self.data.getEmail())
        self.province_edit.setText(curAddress.province)
        self.district_edit.setText(curAddress.district)
        self.sub_district_edit.setText(curAddress.subDistrict)
        self.street_edit.setText(curAddress.street)
        self.zip_code_edit.setText(curAddress.zipCode)
        self.profile_pic.setPixmap(QPixmap(self.data.pictureGen()))

    ##Use for changing profile picture##
    def photo(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter("JPEG Files (*.jpg)")
        if dlg.exec_():
            filenames = dlg.selectedFiles()
        img = imageHandle.imageHandler(self.data.getID())

        if(img.readImageFile(filenames[0]) == "ERRORSIZE"):
            self.parent.showERROR("File too big.", "Image Files must not be greater than 200kb.")
        elif (img.readImageFile(filenames[0]) == "ERRORDIMENSION"):
            self.parent.showERROR("File Dimension Error", "Image dimensions must be 230x280 Pixels.")
        else:
            self.parent.showOK("Information Changed", "Data has been edited successfully.")
            self.parent.changePageLoginSection("login")
            self.close()

    def cancel(self):
        self.close()

    ##Use for changing the profile information of user##
    def editData(self):
        alterAddress = database.databaseUser()
        alterEmail = database.databaseLogin()
        userType = self.data.type()
        if(userType == "STUDENT"):
            userType = 0
        email = self.email_edit.text()
        number = self.house_number_edit.text()
        street =  self.street_edit.text()
        sdistrict = self.sub_district_edit.text()
        district = self.district_edit.text()
        province = self.province_edit.text()
        zip =  self.zip_code_edit.text()
        changeEmail = alterEmail.editLogin(self.data.getUsername(), email, userType)
        changeAddress = alterAddress.updateAddress(self.data.getID(), number, street, sdistrict, district, province, zip)
        if(changeEmail and changeAddress):
            self.parent.showOK("Information Changed", "Data has been edited successfully.")
            self.parent.changePageLoginSection("login")
        alterAddress.disconnect()
        alterEmail.disconnect()
        self.close()
        

    
    

    
        
    
