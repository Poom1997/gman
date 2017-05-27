from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
import plugin.databaseConn as database
import plugin.course as courseItem

from giveGrade import addGradeAdmin

class selectCourseUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900,600)
        self.setWindowTitle("Select Course")
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("resources/imagess/background.png")))
        self.setPalette(palette)
        self.bar = QPixmap("resources/images/bar.png")
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/selectCourseToAddGrade.ui",None)
        self.setCentralWidget(form)

        #Upper Bar
        self.bar_group = form.findChild(QLabel,"barLabel_2")
        self.bar_group.setPixmap(self.bar)
        self.home_button = form.findChild(QPushButton,"homeButton")
        self.profile_button = form.findChild(QPushButton,"profileButton")
        self.grade_button = form.findChild(QPushButton,"gradeButton")
        self.course_button = form.findChild(QPushButton,"courseButton")
        self.other_button = form.findChild(QPushButton, "othersButton")

        #page properties
        self.course_table = form.findChild(QTableWidget,"courseTable")
        self.addGrade_button = form.findChild(QPushButton,"addGradeButton")

        self.header = self.course_table.horizontalHeader()
        self.header.setResizeMode(0,QHeaderView.ResizeToContents)
        self.header.setResizeMode(1,QHeaderView.Stretch)
        self.header.setResizeMode(2,QHeaderView.ResizeToContents)

        self.course_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.course_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.course_table.setEditTriggers(QAbstractItemView.NoEditTriggers)


        #Upper Bar pressed
        self.home_button.clicked.connect(self.goHome)
        self.profile_button.clicked.connect(self.goProfile)
        self.grade_button.clicked.connect(self.goGrade)
        self.other_button.clicked.connect(self.goTemp)
        self.course_button.clicked.connect(self.goCourse)

        #Internal Button Pressed
        self.addGrade_button.clicked.connect(self.addGradeClick)

    def goHome(self):
        self.parent.changePageLoginSection("home")

    def goProfile(self):
        self.parent.changePageLoginSection("profile")

    def goGrade(self):
        self.parent.changePageLoginSection("grade")

    def goCourse(self):
        self.parent.changePageLoginSection("course")

    def goTemp(self):
        self.parent.changePageLoginSection("addcourse")

    def updatePage(self):
        data = self.parent.getCurrentUser()
        db = database.databaseCourse()
        temp = db.getCourseProfessor(data.getID())
        self.allCourse = self.createBulk(temp)
        self.course_table.setRowCount(len(self.allCourse))
        i = 0
        for course in self.allCourse:
            self.course_table.setItem(i, 0, QTableWidgetItem(course.getCourseID()))
            self.course_table.setItem(i, 1, QTableWidgetItem(course.getCourseName()))
            self.course_table.setItem(i, 2, QTableWidgetItem(course.getCredit()))
            i = i + 1

    def addGradeClick(self):
        colCount = 0
        temp = self.course_table.selectionModel().selectedRows()
        if (len(temp) > 0):
            if (self.parent.showCONFIRM("Are you sure?", "Are you sure you assign grades for this course?")):
                for item in self.course_table.selectedItems():
                    if (colCount == 0):
                        tempID = item.text()
                    colCount += 1
        for course in self.allCourse:
            if(course.getCourseID() == tempID):
                self.addGradeUI = addGradeAdmin(course, parent = self.parent)
                self.addGradeUI.updatePage()
                self.addGradeUI.show()
                break

    def createBulk(self, data):
        temp = []
        for i in data:
            temp.append(courseItem.course(i))
        return temp


























        
        


















        
