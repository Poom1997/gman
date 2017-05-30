from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from datetime import datetime
import plugin.databaseConnect as database
import plugin.course as courseItem

class addCourseToProfUI(QMainWindow):
    def __init__(self, parent = None ):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900,435)
        self.setWindowTitle("Find_Course")
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/assignCourseToProf.ui",None)
        self.setCentralWidget(form)

        #QPushButton
        self.search_button = form.findChild(QPushButton,"searchButton")
        self.cancel_button = form.findChild(QPushButton,"closeButton")
        self.assign_button = form.findChild(QPushButton, "assignButton")

        #LineEdit
        self.courseID = form.findChild(QLineEdit,"courseID")
        self.prof_name = form.findChild(QLineEdit,"profName")

        #Label
        self.course_id = form.findChild(QLabel,"courseID_2")
        self.course_name = form.findChild(QLabel, "courseName")
        self.major = form.findChild(QLabel,"major")
        self.year = form.findChild(QLabel,"year")
        self.time = form.findChild(QLabel,"time")
        self.location = form.findChild(QLabel,"location")
        self.crs = form.findChild(QLabel,"crs")
        self.pre_requisite = form.findChild(QLabel,"preRequisite")
        

        #Connect
        self.search_button.clicked.connect(self.search)
        self.cancel_button.clicked.connect(self.close)
        self.assign_button.clicked.connect(self.assignProf)

        self.db = database.databaseCourse()

    def cancel(self):
        self.db.disconnect()
        self.close()
        
    ##Use to search the course before assign to professor##
    def search(self):
        temp = self.courseID.text()
        data = self.db.getCoursebyID(temp)
        self.course_id.setText(data.courseID)
        self.course_name.setText(data.courseName)
        self.major.setText(data.facultyID + " / " + data.majorID)
        self.year.setText(str(data.year))
        self.time.setText(data.time)
        self.location.setText(data.building + " Room:" + data.room )
        self.crs.setText(str(data.credits))
        self.pre_requisite.setText(data.pre)
        self.prof_name.setText(data.professorID)

    ##Assign the course that has been search from search function above##
    def assignProf(self):
        courseID = self.courseID.text()
        profID = self.prof_name.text()
        if(self.parent.showCONFIRM("Are you sure?", "Are you sure to assign Professor " + profID + " to course " + courseID + "?")):
            if(self.db.setProfessor(courseID, profID) == 1):
                self.parent.showOK("Professor Assigned", "Professor " + profID + " has been assigned to course " + courseID)
                self.db.disconnect()
                self.close()
            else:
                self.parent.showERROR("ID Do not Exists", "The professor ID you entered does not exists. Please Try Again.")

    

        

    
    

    
        
    
