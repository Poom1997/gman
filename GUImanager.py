from loginForm import *
from mainForm import *
from pwForm import *
from profileForm import *
from studentCourseForm import *
from addCourseForm import *
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
        self.setWindowTitle("G-Man version 0.5.6 (Alpha)")
        
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("resources/images/background.png")))
        self.setPalette(palette)

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.login_widget = LoginUI(self)
        self.main_widget = mainUI(self)
        self.pw_widget = pwUI(self)
        self.addCourse_widget = addCourseUI(self)
        self.student_course_widget = StudentCourseUI(self)
        self.profile_widget = profileUI(self)
        self.central_widget.addWidget(self.login_widget)
        self.central_widget.addWidget(self.profile_widget)
        self.central_widget.addWidget(self.main_widget)
        self.central_widget.addWidget(self.student_course_widget)
        self.central_widget.addWidget(self.pw_widget)
        self.central_widget.addWidget(self.addCourse_widget)
        self.central_widget.addWidget(self.profile_widget)

    def changePageLoginSection(self,signal = None):
        
        if signal == "login":
            print("login")
            self.centralWidget().setCurrentWidget(self.main_widget)
            self.profile_widget.updatePage()
        if signal == "forget":
            print("forget")
            self.centralWidget().setCurrentWidget(self.pw_widget)
        if signal == "home":
            print("home")
            self.centralWidget().setCurrentWidget(self.main_widget)
        if signal == "profile":
            print("profile")
            self.centralWidget().setCurrentWidget(self.profile_widget)
        if signal == "grade":
            print("grade")
            pass
            #self.centralWidget().setCurrentWidget(self.student_course_widget)
        if signal == "course":
            print("course")
            self.centralWidget().setCurrentWidget(self.student_course_widget)



            
    def setCurrentUser(self, user):
        self.user = user
        
    def getCurrentUser(self):
        return self.user
def main():
    app = QApplication(sys.argv)
    ui = GUImanager()
    ui.show()
    app.exec_()

if __name__ == "__main__":
    main()

        
