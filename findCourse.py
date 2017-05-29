from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from datetime import datetime
import plugin.databaseConnect as database
import plugin.course as courseItem

class findCourseUI(QMainWindow):
    def __init__(self,takenCourse,allTakenCourseNORE,allTakenCourseNOOPEN, currentCourse, parent = None ):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900,611)
        self.setWindowTitle("Find_Course")
        self.parent = parent
        self.UIinit()
        self.allTakenCourse = takenCourse
        self.currentCourse = currentCourse
        self.allTakenCourseNORE = allTakenCourseNORE
        self.allTakenCourseNOOPEN = allTakenCourseNOOPEN

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/findCourse.ui",None)
        self.setCentralWidget(form)

        #QPushButton
        self.search_button = form.findChild(QPushButton,"searchButton")
        self.cancel_button = form.findChild(QPushButton,"closeButton")
        self.addSelected_button = form.findChild(QPushButton, "add_selected")
        self.addSelected_button.setEnabled(False)

        #LineEdit
        self.faculty_name = form.findChild(QLineEdit,"facultyID")

        #Table
        self.course_table = form.findChild(QTableWidget,"tableWidget")
        self.course_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.course_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.course_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.course_table_header = self.course_table.horizontalHeader()
        self.course_table_header.setResizeMode(0, QHeaderView.ResizeToContents)
        self.course_table_header.setResizeMode(1, QHeaderView.ResizeToContents)
        self.course_table_header.setResizeMode(2, QHeaderView.ResizeToContents)
        self.course_table_header.setResizeMode(3, QHeaderView.ResizeToContents)
        self.course_table_header.setResizeMode(4, QHeaderView.ResizeToContents)
        self.course_table_header.setResizeMode(5, QHeaderView.Stretch)
        self.course_table_header.setResizeMode(7, QHeaderView.ResizeToContents)
        self.course_table_header.setResizeMode(8, QHeaderView.ResizeToContents)

        #Connect
        self.faculty_name.returnPressed.connect(self.search)
        self.search_button.clicked.connect(self.search)
        self.cancel_button.clicked.connect(self.close)
        self.addSelected_button.clicked.connect(self.add_selected)

        self.db = database.databaseCourse()

    def cancel(self):
        self.db.disconnect()
        self.close()

    def search(self):
        data = self.db.getCourseFaculty(self.faculty_name.text())
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
        self.data = self.parent.parent.getCurrentUser()
        if(self.data.type() == "STUDENT"):
            self.addSelected_button.setEnabled(True)
        else:
            self.addSelected_button.setEnabled(False)

    def add_selected(self):
        colCount = 0
        temp = self.course_table.selectionModel().selectedRows()
        if (len(temp) > 0):
            if (self.parent.parent.showCONFIRM("Are you sure?", "Are you sure you add the selected course?\
                                                                                By clicking yes, your course will be added immediately to the registration system.")):
                for item in self.course_table.selectedItems():
                    if (colCount == 0):
                        tempID = item.text()
                    if (colCount == 8):
                        pre = item.text()
                    if (colCount == 7):
                        limit = item.text()
                        limit = int(limit)
                    colCount += 1

            if (tempID in self.allTakenCourseNOOPEN):
                self.parent.parent.showERROR("Course Not Avaliable",
                                      "This course is not open for this term. You cannot add this course.")
            elif (tempID in self.allTakenCourse and tempID in self.allTakenCourseNORE or tempID in self.currentCourse):
                self.parent.parent.showERROR("Course Error",
                                      "You have already taken the course. Therefore, you cannot add this course.")
            elif (limit == 0):
                self.parent.parent.showERROR("Course Full",
                                      "This course is now filled. Therefore, you cannot add this course.")

            elif (pre in self.allTakenCourse or len(pre) < 5):
                if (self.db.addCourseUser(self.data.getID(), self.data.getYear(), self.data.getTerm(), tempID,
                                          datetime.now().year, limit)):
                    self.parent.parent.showOK("Course Added", "Your course " + tempID + " has been added to the system.")
                    self.close()
            else:
                self.parent.parent.showERROR("Pre-requisite Course Error", "You have not taken the required course required for this course.\
                                                                                Please complete that course before adding this course.")
            self.parent.updatePage()

    def createBulk(self, data):
        temp = []
        for i in data:
            temp.append(courseItem.course(i))
        return temp
        

    
    

    
        
    
