from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from datetime import datetime
import plugin.databaseConnect as database
import plugin.course as courseItem

class searchCourseByProfIDUI(QMainWindow):
    def __init__(self,parent = None ):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900,600)
        self.setWindowTitle("searchCourseByID")
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/searchCourseByProfID.ui",None)
        self.setCentralWidget(form)

        #QPushButton
        self.search_button = form.findChild(QPushButton,"searchButton")
        self.cancel_button = form.findChild(QPushButton,"closeButton")
        
        #LineEdit
        self.professor_ID = form.findChild(QLineEdit,"profID")

        #Table
        self.course_table = form.findChild(QTableWidget,"tableWidget")
        self.course_table.setSelectionMode(QAbstractItemView.NoSelection)
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
        
        self.search_button.clicked.connect(self.search)
        self.cancel_button.clicked.connect(self.close)


    def cancel(self):
        self.db.disconnect()
        self.close()

    ##Use to search course by using professor's id##
    def search(self):
        self.db = database.databaseCourse()
        data = self.db.getCourseProfessor(self.professor_ID.text())
        allCourse = self.createBulk(data)
        self.course_table.setRowCount(len(allCourse))
        i = 0
        for course in allCourse:
            self.course_table.setItem(i, 0, QTableWidgetItem(course.getCourseID()))
            self.course_table.setItem(i, 1, QTableWidgetItem(course.getCourseName()))
            self.course_table.setItem(i, 2, QTableWidgetItem(course.getMajorID()))
            self.course_table.setItem(i, 3, QTableWidgetItem(course.getYear()))
            self.course_table.setItem(i, 4, QTableWidgetItem(course.getTime()))
            self.course_table.setItem(i, 5, QTableWidgetItem(course.getLocation()))
            self.course_table.setItem(i, 6, QTableWidgetItem(course.getCredit()))
            self.course_table.setItem(i, 7, QTableWidgetItem(course.getMaxStud()))
            self.course_table.setItem(i, 8, QTableWidgetItem(course.getPre()))
            i = i + 1

    def createBulk(self, data):
        temp = []
        for i in data:
            temp.append(courseItem.course(i))
        return temp

        

    
