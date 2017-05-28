from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
import plugin.databaseConnect as database

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
        self.search_course_id = form.findChild(QLineEdit,"courseID")

        #Label
        self.user_id = form.findChild(QLabel,"userID")
        self.first_name = form.findChild(QLabel,"firstName")
        self.surname = form.findChild(QLabel,"surName")
        self.email = form.findChild(QLabel,"eMail")
        self.type = form.findChild(QLabel,"type")
        self.faculty_id = form.findChild(QLabel,"facultyID")
    
        #Connect
        self.search_course_id.returnPressed.connect(self.search)
        self.cancel_button.clicked.connect(self.cancel)
        self.search_button.clicked.connect(self.search)

    def cancel(self):
        self.db.disconnect()
        self.close()

    def search(self):
        self.db = database.databaseCourse()
        data = self.db.findProfessorbyCourseID(self.search_course_id.text())
        if(data!=None):
            self.user_id.setText(data.user_id)
            self.first_name.setText(data.name)
            self.surname.setText(data.surname)
            self.email.setText(data.email)
            self.faculty_id.setText(data.facultyID)
            status = data.status
            if (status == 0):
                self.type.setText("Lecturer")
            elif (status == 1):
                self.type.setText("Assist. Prof.")
            elif (status == 2):
                self.type.setText("Assoc. Prof.")
            elif (status == 3):
                self.type.setText("Professor.")
            elif (status == 4):
                self.type.setText("Suspend")
            elif (status == 5):
                self.type.setText("Retired")
            else:
                self.type.setText("Unknown")
        else:
            self.parent.showERROR("Invalid CourseID", "Invalid CourseID, Please Try Again.")