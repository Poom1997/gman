from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class StudentCourseUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900, 600)
        self.setWindowTitle("Courses")
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("resources/images/background.png")))
        self.logo = QPixmap("resources/images/templogo.png")
        self.bar = QPixmap("resources/images/bar.png")
        self.setPalette(palette)
        self.parent = parent
        self.rowUP = 0
        self.rowDN = 0
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

        #page properties
        self.available_course = form.findChild(QTableWidget,"available")
        self.your_course = form.findChild(QTableWidget,"mycourse")
        self.save_button = form.findChild(QPushButton,"saveButton")
        self.add_button = form.findChild(QPushButton,"addButton")
        self.delete_button = form.findChild(QPushButton,"deleteButton")

        self.header = self.available_course.horizontalHeader()
        self.header.setResizeMode(0,QHeaderView.ResizeToContents)
        self.header.setResizeMode(1,QHeaderView.Stretch)
        self.header.setResizeMode(2,QHeaderView.ResizeToContents)
        self.header.setResizeMode(3,QHeaderView.ResizeToContents)
        self.header.setResizeMode(4,QHeaderView.Stretch)
        self.header.setResizeMode(5,QHeaderView.ResizeToContents)
        self.header.setResizeMode(6,QHeaderView.ResizeToContents)

        self.header2 = self.your_course.horizontalHeader()
        self.header2.setResizeMode(0,QHeaderView.ResizeToContents)
        self.header2.setResizeMode(1,QHeaderView.Stretch)
        self.header2.setResizeMode(2,QHeaderView.ResizeToContents)
        self.header2.setResizeMode(3,QHeaderView.ResizeToContents)
        self.header2.setResizeMode(4,QHeaderView.Stretch)
        self.header2.setResizeMode(5,QHeaderView.ResizeToContents)
        self.header2.setResizeMode(6,QHeaderView.ResizeToContents)

        self.available_course.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.available_course.setEditTriggers(QAbstractItemView.NoEditTriggers)

        
        self.your_course.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.your_course.setEditTriggers(QAbstractItemView.NoEditTriggers)



        #Upper Bar pressed
        self.home_button.clicked.connect(self.goHome)
        self.profile_button.clicked.connect(self.goProfile)
        self.grade_button.clicked.connect(self.goGrade)
        self.course_button.clicked.connect(self.goCourse)
        self.add_button.clicked.connect(self.addClick)
        self.delete_button.clicked.connect(self.deleteClick)

        self.insertCourse()

    def addClick(self):
        colCount = 0
        temp = self.available_course.selectionModel().selectedRows()
        if(len(temp)>0):
            self.your_course.insertRow(self.rowDN)
            for item in self.available_course.selectedItems():
                self.your_course.setItem(self.rowDN,colCount,QTableWidgetItem(item.text()))
                colCount+=1
            self.available_course.removeRow(temp[0].row())
            self.rowUP -= 1
            self.rowDN += 1
        
    def deleteClick(self):
        colCount = 0
        temp = self.your_course.selectionModel().selectedRows()
        if(len(temp)>0):
            self.available_course.insertRow(self.rowUP)
            for item in self.your_course.selectedItems():
                self.available_course.setItem(self.rowUP,colCount,QTableWidgetItem(item.text()))
                colCount+=1
            self.your_course.removeRow(temp[0].row())
            self.rowUP += 1
            self.rowDN -= 1
        


    def insertCourse(self):
        self.available_course.setRowCount(2)
        self.rowUP = 2
        self.available_course.setItem(0,0,QTableWidgetItem("123214"))
        self.available_course.setItem(0,1,QTableWidgetItem("Data Structure Design and Analysis"))
        self.available_course.setItem(0,2,QTableWidgetItem("3"))
        self.available_course.setItem(0,3,QTableWidgetItem("2/3"))
        self.available_course.setItem(0,4,QTableWidgetItem("Statistic"))
        self.available_course.setItem(0,5,QTableWidgetItem("9:00 - 12:00"))
        self.available_course.setItem(0,6,QTableWidgetItem("30"))

        self.available_course.setItem(1,0,QTableWidgetItem("111232"))
        self.available_course.setItem(1,1,QTableWidgetItem("Something Useful"))
        self.available_course.setItem(1,2,QTableWidgetItem("1"))
        self.available_course.setItem(1,3,QTableWidgetItem("1/3"))
        self.available_course.setItem(1,4,QTableWidgetItem("-"))
        self.available_course.setItem(1,5,QTableWidgetItem("13:00 - 16:00"))
        self.available_course.setItem(1,6,QTableWidgetItem("15"))

    def goHome(self):
        self.parent.changePageLoginSection("home")

    def goProfile(self):
        self.parent.changePageLoginSection("profile")

    def goGrade(self):
        self.parent.changePageLoginSection("grade")

    def goCourse(self):
        self.parent.changePageLoginSection("course")
    
        
