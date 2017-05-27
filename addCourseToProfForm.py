from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from datetime import datetime
import plugin.databaseConn as database
import plugin.course as courseItem

class addCourseToProfUI(QMainWindow):
    def __init__(self,takenCourse, currentCourse, parent = None ):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900,581)
        self.setWindowTitle("Find_Course")
        self.parent = parent
        self.UIinit()
        self.allTakenCourse = takenCourse
        self.currentCourse = currentCourse

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

        #Table
        self.course_table = form.findChild(QTableWidget,"tableWidget")
        self.course_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.course_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.course_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.course_table_header = self.course_table.horizontalHeader()
        self.course_table_header.setResizeMode(0, QHeaderView.ResizeToContents)
        self.course_table_header.setResizeMode(1, QHeaderView.Stretch)
        self.course_table_header.setResizeMode(2, QHeaderView.ResizeToContents)
        self.course_table_header.setResizeMode(3, QHeaderView.ResizeToContents)
        self.course_table_header.setResizeMode(4, QHeaderView.ResizeToContents)
        self.course_table_header.setResizeMode(5, QHeaderView.ResizeToContents)
        self.course_table_header.setResizeMode(7, QHeaderView.ResizeToContents)
        self.course_table_header.setResizeMode(8, QHeaderView.ResizeToContents)

        #Connect
        self.faculty_name.returnPressed.connect(self.search)
        self.search_button.clicked.connect(self.search)
        self.cancel_button.clicked.connect(self.close)
        self.assign_button.clicked.connect(self.assignProf)

        self.db = database.databaseCourse()

    def cancel(self):
        self.db.disconnect()
        self.close()

    def search(self):
       pass

    def assignProf(self):
        pass
    

        

    
    

    
        
    
