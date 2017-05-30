from loginForm import *
from mainForm import *
from profileForm import *
from studentCourseForm import *
from grading import *
from addMajorAdmin import *
from addFacultyAdmin import *
from viewGradeForm import *
from addCourseForm import *
from seeCourseProf import *
from otherOptionForm import *
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


import sys

class GUImanager(QMainWindow):
    def __init__(self):
        self.user = None
        # Main UI set up
        QMainWindow.__init__(self, None)
        self.setMinimumSize(900, 600)
        self.setFixedSize(900,600)
        self.setWindowTitle("G-Man version 1.0.0 (Beta)")
        
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("resources/images/programBackground.png")))
        self.setPalette(palette)

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.login_widget = LoginUI(self)
        self.main_widget = mainUI(self)
        self.add_major_for_admin_widget = AddMajorUI(self)
        self.view_grade_widget = viewGradeUI(self)
        self.addCourse_widget = addCourseUI(self)
        self.student_course_widget = StudentCourseUI(self)
        self.add_faculties_for_admin = AddFacultyUI(self)
        self.profile_widget = profileUI(self)
        self.other_option_widget = otherOptionUI(self)
        self.select_course = selectCourseUI(self)
        self.see_course_widget = seeCourseProfUI(self)

        self.central_widget.addWidget(self.login_widget)
        self.central_widget.addWidget(self.view_grade_widget)
        self.central_widget.addWidget(self.profile_widget)
        self.central_widget.addWidget(self.main_widget)
        self.central_widget.addWidget(self.student_course_widget)
        self.central_widget.addWidget(self.addCourse_widget)
        self.central_widget.addWidget(self.profile_widget)
        self.central_widget.addWidget(self.add_major_for_admin_widget)
        self.central_widget.addWidget(self.select_course)
        self.central_widget.addWidget(self.add_faculties_for_admin)
        self.central_widget.addWidget(self.see_course_widget)
        self.central_widget.addWidget(self.other_option_widget)

        self.suspension = 0
        self.graduated = 0
        self.retired = 0

    def changePageLoginSection(self,signal = None):
        if signal == "login":
            self.suspension = 0
            self.graduated = 0
            self.retired = 0
            self.centralWidget().setCurrentWidget(self.login_widget)

        if signal == "home":
            self.centralWidget().setCurrentWidget(self.main_widget)
            self.main_widget.updatePage()

        if signal == "profile":
            self.centralWidget().setCurrentWidget(self.profile_widget)
            self.profile_widget.updatePage()

        ## STUDENT signal ##
            
        if signal == "studentGrade":
            self.centralWidget().setCurrentWidget(self.view_grade_widget)
            self.view_grade_widget.updatePage()

        if signal == "studentCourse":
            if(self.suspension == 1):
                self.showERROR("You are suspended", "You are currently suspended. You cannot access this menu.")
            elif(self.graduated == 1):
                self.showOK("Hello!", "Your account has been locked by the administrator.")
            else:
                self.centralWidget().setCurrentWidget(self.student_course_widget)
                self.student_course_widget.updatePage()

        ## Prof signal ## 

        if signal == "grade":
            if (self.suspension == 1):
                self.showERROR("You are suspended", "You are currently suspended. You cannot access this menu.")
            elif (self.graduated == 1):
                self.showOK("Hello!", "Your account has been locked by the administrator.")
            else:
                self.centralWidget().setCurrentWidget(self.select_course)
                self.select_course.updatePage()

        if signal == "course":
            self.centralWidget().setCurrentWidget(self.see_course_widget)
            self.see_course_widget.updatePage()

        ## Admin signal ## 

        if signal == "addcourse":
            self.centralWidget().setCurrentWidget(self.addCourse_widget)

        if signal == "addfaculties":
            self.centralWidget().setCurrentWidget(self.add_faculties_for_admin)
            self.add_faculties_for_admin.updatePage()
            
        if signal == "addmajor":
            self.centralWidget().setCurrentWidget(self.add_major_for_admin_widget)

        if signal == "otherOption":
            self.centralWidget().setCurrentWidget(self.other_option_widget)
            

    def setCurrentUser(self, user):
        self.user = user
        
    def getCurrentUser(self):
        if(self.user.getStatus() == 4):
            self.suspension = 1
        if (self.user.getStatus() == 5):
            self.graduated = 1
        return self.user

    ##MessageDialogs
    def showOK(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Ok)
        ret_val = msg.exec_()

    def showCONFIRM(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        ret_val = msg.exec_()
        if (ret_val == QMessageBox.Ok):
            return True
        else:
            return False

    def showERROR(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Ok)
        ret_val = msg.exec_()
def main():
    app = QApplication(sys.argv)
    ui = GUImanager()
    ui.show()
    app.exec_()

if __name__ == "__main__":
    main()

        
