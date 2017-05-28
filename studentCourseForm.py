from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from findCourse import findCourseUI
from sendMessageForm import sendMessageUI
from datetime import datetime
import plugin.databaseConn as database
import plugin.course as courseItem

class StudentCourseUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900, 600)
        self.setWindowTitle("Courses")
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("resources/images/background.png")))
        self.bar = QPixmap("resources/images/bar.png")
        self.setPalette(palette)
        self.parent = parent
        self.rowUP = 0
        self.rowDN = 0
        self.db = database.databaseCourse()
        self.courseAvailable = []
        self.currentCourse = []
        self.allTakenCourse = []
        self.parent = parent
        self.data = None
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/studentcourse.ui", None)
        self.setCentralWidget(form)

        #Upper Bar
        self.bar_group = form.findChild(QLabel,"barLabel_2")
        self.bar_group.setPixmap(self.bar)
        self.home_button = form.findChild(QPushButton,"homeButton")
        self.profile_button = form.findChild(QPushButton,"profileButton")
        self.grade_button = form.findChild(QPushButton,"gradeButton")
        self.course_button = form.findChild(QPushButton,"courseButton")
        self.temp = form.findChild(QPushButton, "temp")
        self.temp2 = form.findChild(QPushButton, "temp2")


        #page properties
        self.available_course = form.findChild(QTableWidget,"available")
        self.your_course = form.findChild(QTableWidget,"mycourse")
        self.add_button = form.findChild(QPushButton,"addButton")
        self.search_course = form.findChild(QPushButton,"searchCourseButton")
        self.delete_button = form.findChild(QPushButton, "deleteButton")
        self.add_button.setEnabled(False)
        self.delete_button.setEnabled(False)

        self.available_course_header = self.available_course.horizontalHeader()
        self.available_course_header.setResizeMode(0,QHeaderView.ResizeToContents)
        self.available_course_header.setResizeMode(1,QHeaderView.Stretch)
        self.available_course_header.setResizeMode(2,QHeaderView.ResizeToContents)
        self.available_course_header.setResizeMode(3,QHeaderView.ResizeToContents)
        self.available_course_header.setResizeMode(4,QHeaderView.Stretch)
        self.available_course_header.setResizeMode(5,QHeaderView.ResizeToContents)
        self.available_course_header.setResizeMode(6,QHeaderView.ResizeToContents)

        self.your_course_header = self.your_course.horizontalHeader()
        self.your_course_header.setResizeMode(0,QHeaderView.ResizeToContents)
        self.your_course_header.setResizeMode(1,QHeaderView.Stretch)
        self.your_course_header.setResizeMode(2,QHeaderView.ResizeToContents)
        self.your_course_header.setResizeMode(3,QHeaderView.ResizeToContents)
        self.your_course_header.setResizeMode(4,QHeaderView.Stretch)
        self.your_course_header.setResizeMode(5,QHeaderView.ResizeToContents)
        self.your_course_header.setResizeMode(6,QHeaderView.ResizeToContents)

        self.available_course.setSelectionMode(QAbstractItemView.SingleSelection)
        self.available_course.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.available_course.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.your_course.setSelectionMode(QAbstractItemView.SingleSelection)
        self.your_course.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.your_course.setEditTriggers(QAbstractItemView.NoEditTriggers)

        #Upper Bar pressed
        self.home_button.clicked.connect(self.goHome)
        self.profile_button.clicked.connect(self.goProfile)
        self.grade_button.clicked.connect(self.goGrade)
        self.course_button.clicked.connect(self.goCourse)
        self.temp.clicked.connect(self.goTemp)
        self.temp2.clicked.connect(self.goTemp2)


        #Internal Button Pressed
        self.add_button.clicked.connect(self.addClick)
        self.delete_button.clicked.connect(self.deleteClick)
        self.search_course.clicked.connect(self.searchCourse)

    def addClick(self):
        colCount = 0
        temp = self.available_course.selectionModel().selectedRows()
        if(len(temp)>0):
            if (self.parent.showCONFIRM("Are you sure?", "Are you sure you add the selected course?\
                                                                    By clicking yes, your course will be added immediately to the registration system.")):
                self.your_course.insertRow(self.rowDN)
                for item in self.available_course.selectedItems():
                    self.your_course.setItem(self.rowDN,colCount,QTableWidgetItem(item.text()))
                    if (colCount == 0):
                        tempID = item.text()
                    if(colCount == 4):
                        pre = item.text()
                    if(colCount == 6):
                        limit = item.text()
                        limit = int(limit)
                    colCount+=1
                self.available_course.removeRow(temp[0].row())
                self.rowUP -= 1

            if (tempID in self.allTakenCourseNOOPEN):
                self.parent.showERROR("Course Not Avaliable",
                                      "This course is not open for this term. You cannot add this course.")
            elif (tempID in self.allTakenCourse and tempID in self.allTakenCourseNORE):
                self.parent.showERROR("Course Error", "You have already taken the course. Therefore, you cannot add this course.")
            elif(limit == 0):
                self.parent.showERROR("Course Full", "This course is now filled. You cannot add this course.")
            elif(pre in self.allTakenCourse or len(pre) < 5):
                if (self.db.addCourseUser(self.data.getID(), self.data.getYear(), self.data.getTerm(), tempID, datetime.now().year, limit)):
                    self.parent.showOK("Course Added", "Your course " + tempID + " has been added to the system.")
            else:
                self.parent.showERROR("Pre-requisite Course Error", "You have not taken the required course required for this course.\
                                                                    Please complete that course before adding this course.")
            self.updatePage()
        
    def deleteClick(self):
        colCount = 0
        temp = self.your_course.selectionModel().selectedRows()
        if(len(temp)>0):
            if(self.parent.showCONFIRM("Are you sure?", "Are you sure you want to drop the selected course?\
                                                        Once you drop, you will have to re-take the course!\
                                                        By clicking yes, your course will be removed immediately from the registration system.")):
                self.available_course.insertRow(self.rowUP)
                for item in self.your_course.selectedItems():
                    self.available_course.setItem(self.rowUP,colCount,QTableWidgetItem(item.text()))
                    if(colCount == 0):
                        tempID = item.text()
                    if (colCount == 6):
                        limit = item.text()
                        limit = int(limit)
                    colCount+=1
                self.your_course.removeRow(temp[0].row())
                self.rowUP += 1
                self.rowDN -= 1
                if(self.db.dropCourseUser(self.data.getID() ,tempID, datetime.now().year, limit)):
                    self.parent.showOK("Course Removed", "Your course " + tempID + " has been removed from the system." )
            self.updatePage()

    def updatePage(self):
        currentID = []
        self.data = self.parent.getCurrentUser()

        temp = self.db.termCourse(self.data.getFacultyID(), self.data.getMajorID(), self.data.getYear(), self.data.getTerm())
        self.courseAvailable = self.createBulk(temp)

        temp = self.db.currentCourse(self.data.getID())
        self.currentCourse = self.createBulk(temp)

        #Check Pre-requisite IF 'F' not counted
        temp = self.db.allUserCourse(self.data.getID())
        self.allTakenCourse = []
        for elements in temp:
            if(int(elements.allowRepeat) < 2 and elements.grade != None):
                self.allTakenCourse.append(elements.courseID)

        #Check Re-Grade avaliable
        temp = self.db.allUserCourse(self.data.getID())
        self.allTakenCourseNORE = []
        for elements in temp:
            if(int(elements.allowRepeat) < 1 and elements.grade != None):
                self.allTakenCourseNORE.append(elements.courseID)

        #Check term openings
        temp = self.db.getAllCourseINFO()
        self.allTakenCourseNOOPEN = []
        for elements in temp:
            if(self.data.getTerm() != elements.term):
                self.allTakenCourseNOOPEN.append(elements.courseID)
        print(self.allTakenCourseNOOPEN)

        for course in self.currentCourse:
            currentID.append(course.getCourseID())

        self.available_course.setRowCount(len(self.courseAvailable))
        self.rowUP = len(self.courseAvailable)

        self.your_course.setRowCount(len(self.currentCourse))
        self.rowDN = len(self.currentCourse)

        if(len(self.courseAvailable) > 0):
            self.add_button.setEnabled(True)
        else:
            self.add_button.setEnabled(False)

        if (len(self.currentCourse) > 0):
            self.delete_button.setEnabled(True)
        else:
            self.delete_button.setEnabled(False)

        i = 0
        for course in self.currentCourse:
            self.your_course.setItem(i, 0, QTableWidgetItem(course.getCourseID()))
            self.your_course.setItem(i, 1, QTableWidgetItem(course.getCourseName()))
            self.your_course.setItem(i, 2, QTableWidgetItem(course.getCredit()))
            self.your_course.setItem(i, 3, QTableWidgetItem(course.getYear()))
            self.your_course.setItem(i, 4, QTableWidgetItem(course.getPre()))
            self.your_course.setItem(i, 5, QTableWidgetItem(course.getTime()))
            self.your_course.setItem(i, 6, QTableWidgetItem(course.getMaxStud()))
            i = i + 1

        i = 0
        for course in self.courseAvailable:
            if(course.getCourseID() in currentID):
                self.available_course.removeRow(i)
                self.rowUP = self.rowUP - 1
            else:
                self.available_course.setItem(i,0,QTableWidgetItem(course.getCourseID()))
                self.available_course.setItem(i,1,QTableWidgetItem(course.getCourseName()))
                self.available_course.setItem(i,2,QTableWidgetItem(course.getCredit()))
                self.available_course.setItem(i,3,QTableWidgetItem(course.getYear()))
                self.available_course.setItem(i,4,QTableWidgetItem(course.getPre()))
                self.available_course.setItem(i,5,QTableWidgetItem(course.getTime()))
                self.available_course.setItem(i,6,QTableWidgetItem(course.getMaxStud()))
                i = i + 1
    
    def searchCourse(self):
        currentCourse = []
        for items in self.currentCourse:
            currentCourse.append(items.getCourseID())
        self.edit = findCourseUI(self.allTakenCourse,self.allTakenCourseNORE,self.allTakenCourseNOOPEN ,currentCourse, parent=self)
        self.edit.show()

    def goHome(self):
        self.parent.changePageLoginSection("home")

    def goProfile(self):
        self.parent.changePageLoginSection("profile")

    def goGrade(self):
        self.parent.changePageLoginSection("studentGrade")

    def goCourse(self):
        self.parent.changePageLoginSection("studentCourse")
        
    def goTemp(self):
        self.createM = sendMessageUI(parent = self.parent)
        self.createM.show()

    def goTemp2(self):
        self.parent.changePageLoginSection("login")

    def createBulk(self, data):
        temp = []
        for i in data:
            temp.append(courseItem.course(i))
        return temp
