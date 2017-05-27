from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
import plugin.databaseConn as database

class addUserUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900,341)
        self.setWindowTitle("Add_User")
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/AddUsers.ui",None)
        self.setCentralWidget(form)

        self.status_set = 0

        #QPushButton
        self.cancel_button = form.findChild(QPushButton,"close")
        self.add_button = form.findChild(QPushButton,"add")
        self.student_button = form.findChild(QPushButton, "student")
        self.professor_button = form.findChild(QPushButton, "professor")
        self.admin_button = form.findChild(QPushButton, "admin")

        #LineEdit
        self.user_id = form.findChild(QLineEdit,"userID")
        self.first_name = form.findChild(QLineEdit,"firstName")
        self.surname = form.findChild(QLineEdit,"surName")
        self.email = form.findChild(QLineEdit,"eMail")
        self.username = form.findChild(QLineEdit,"userName")
        self.status = form.findChild(QLineEdit,"type")
        self.faculty_id = form.findChild(QLineEdit,"facultyID")
        self.major_id = form.findChild(QLineEdit,"majorID")
        self.status.setEnabled(False)
    
        #Connect
        self.cancel_button.clicked.connect(self.cancel)
        self.add_button.clicked.connect(self.add)
        self.student_button.clicked.connect(self.statusChangeStudent)
        self.professor_button.clicked.connect(self.statusChangeProfessor)
        self.admin_button.clicked.connect(self.statusChangeAdmin)

        self.update()

    def update(self):
        if (self.status_set == 0):
            self.status.setText("STUDENT")
            self.faculty_id.setEnabled(True)
            self.major_id.setEnabled(True)
        elif (self.status_set == 1):
            self.status.setText("PROFESSOR")
            self.faculty_id.setEnabled(True)
            self.major_id.setEnabled(False)
        elif (self.status_set == 2):
            self.status.setText("ADMINISTRATOR")
            self.faculty_id.setEnabled(False)
            self.major_id.setEnabled(False)
        else:
            self.status.setText("ERROR")

    def cancel(self):
        self.close()

    def add(self):
        self.dbLogin = database.databaseLogin()
        self.dbLogin.createLogin(self.user_id.text(),self.username.text(), self.email.text(), userType = self.status_set)
        self.dbLogin.disconnect()
        self.dbUser = database.databaseUser()
        if(self.status_set == 0):
            status = self.dbUser.createStudent(self.user_id.text(),self.first_name.text(), self.surname.text(), self.email.text(),self.faculty_id.text(), self.major_id.text())
        elif(self.status_set == 1):
            status = self.dbUser.createProfessor(self.user_id.text(),self.first_name.text(), self.surname.text(), self.email.text(),self.faculty_id.text())
        elif (self.status_set == 2):
            status = self.dbUser.createAdmin(self.user_id.text(), self.first_name.text(), self.surname.text(),
                                                 self.email.text())
        if (status[0] == 1):
            self.parent.showOK("User Saved", "The User has been added successfully")
            self.dbUser.disconnect()
            self.close()
        if (status[0] == "EXISTS"):
            self.parent.showERROR("Data Duplication Error" + status[0], "UserID already exists.")
        elif (status[0] == "22P02"):
            self.parent.showERROR("Data Integrity Error" + status[0],
                                "Invalid DataType or Incomplete Form.\nPlease check your fields.")
        elif (status[0] == "23505"):
            self.parent.showERROR("Data Duplication Error" + status[0], "UserID already exists.")
        elif (status[0] == "23503"):
            self.parent.showERROR("Data Consistency Error" + status[0],
                                "Either FacultyID, or Major ID is incorrect OR Username Exists.")

    def statusChangeStudent(self):
        self.status_set = 0
        self.update()

    def statusChangeProfessor(self):
        self.status_set = 1
        self.update()

    def statusChangeAdmin(self):
        self.status_set = 2
        self.update()
