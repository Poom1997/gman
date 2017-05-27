from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

from giveGrade import addGradeAdmin

import plugin.databaseConn as database
import plugin.gradeData as grade

class viewGradeUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900,600)
        self.setWindowTitle("Grades")
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("resources/imagess/background.png")))
        self.setPalette(palette)
        self.bar = QPixmap("resources/images/bar.png")
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/viewGrade.ui",None)
        self.setCentralWidget(form)

        #Upper Bar
        self.bar_group = form.findChild(QLabel,"barLabel_2")
        self.bar_group.setPixmap(self.bar)
        self.home_button = form.findChild(QPushButton,"homeButton")
        self.profile_button = form.findChild(QPushButton,"profileButton")
        self.grade_button = form.findChild(QPushButton,"gradeButton")
        self.course_button = form.findChild(QPushButton,"courseButton")
        self.temp = form.findChild(QPushButton, "temp")

        #page properties
        self.print_button = form.findChild(QPushButton, "printButton")
        self.this_term = form.findChild(QTableWidget,"thisTerm")
        self.all_term = form.findChild(QTableWidget,"allTerm")
        self.gpa_input = form.findChild(QLabel,"gpaInp")
        self.gps_input = form.findChild(QLabel,"gpsInp")
        self.crs_input = form.findChild(QLabel,"crsInp")
        self.status_input = form.findChild(QLabel,"statusInp")

        #Upper Bar pressed
        self.home_button.clicked.connect(self.goHome)
        self.profile_button.clicked.connect(self.goProfile)
        self.grade_button.clicked.connect(self.goGrade)
        self.course_button.clicked.connect(self.goCourse)
        self.temp.clicked.connect(self.goTemp)
        self.home_button.clicked.connect(self.goHome)
        self.print_button.clicked.connect(self.goDummy)

        #Table Properties
        self.all_term_header = self.all_term.horizontalHeader()
        self.all_term_header.setResizeMode(0, QHeaderView.ResizeToContents)
        self.all_term_header.setResizeMode(1, QHeaderView.Stretch)
        self.all_term_header.setResizeMode(2, QHeaderView.ResizeToContents)
        self.all_term_header.setResizeMode(3, QHeaderView.ResizeToContents)

        self.this_term_header = self.this_term.horizontalHeader()
        self.this_term_header.setResizeMode(0, QHeaderView.ResizeToContents)
        self.this_term_header.setResizeMode(1, QHeaderView.Stretch)
        self.this_term_header.setResizeMode(2, QHeaderView.ResizeToContents)
        self.this_term_header.setResizeMode(3, QHeaderView.ResizeToContents)

        self.all_term.setSelectionMode(QAbstractItemView.NoSelection)
        self.all_term.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.this_term.setSelectionMode(QAbstractItemView.NoSelection)
        self.this_term.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def goDummy(self):
        self.temp = addGradeAdmin(parent = self.parent)
        self.temp.show()

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
        db = database.databaseGrade()
        temp = db.getPastCourse(data.getID())
        all_course = self.createBulk(temp[0], temp[1])
        temp = db.getCurrentCourse(data.getID(), data.getYear(), data.getTerm())
        cur_course = self.createBulk(temp[0], temp[1])
        currentID = []

        #Calculating GPA/GPS Variable
        sumGPA = 0
        crsGPA = 0
        sumGPS = 0
        crsGPS = 0

        #Add Items in All Terms and Insert GPA Data
        i = 0
        self.all_term.setRowCount(len(all_course))
        for grade in all_course:
            self.all_term.setItem(i, 0, QTableWidgetItem(grade.getCourseID()))
            self.all_term.setItem(i, 1, QTableWidgetItem(grade.getCourseName()))
            self.all_term.setItem(i, 2, QTableWidgetItem(grade.getCredit()))
            self.all_term.setItem(i, 3, QTableWidgetItem(grade.getGrade()))
            currentID.append(grade.getCourseID())
            curCrs = int(grade.getCredit())
            crsGPA = crsGPA + curCrs
            if(grade.getGrade() == "A"):
                sumGPA = sumGPA + 4.00 * curCrs
            elif(grade.getGrade() == "B+"):
                sumGPA = sumGPA + 3.50 * curCrs
            elif(grade.getGrade() == "B"):
                sumGPA = sumGPA + 3.00 * curCrs
            elif(grade.getGrade() == "C+"):
                sumGPA = sumGPA + 2.50 * curCrs
            elif(grade.getGrade() == "C"):
                sumGPA = sumGPA + 2.00 * curCrs
            elif(grade.getGrade() == "D+"):
                sumGPA = sumGPA + 1.50 * curCrs
            elif(grade.getGrade() == "D"):
                sumGPA = sumGPA + 1.00 * curCrs
            else:
                sumGPA = sumGPA + 0
            i = i + 1

            # Add Items in Current Terms and Insert GPA Data
        i = 0
        self.this_term.setRowCount(len(cur_course))
        for grade in cur_course:
            if (grade.getCourseID() not in currentID):
                self.this_term.setItem(i, 0, QTableWidgetItem(grade.getCourseID()))
                self.this_term.setItem(i, 1, QTableWidgetItem(grade.getCourseName()))
                self.this_term.setItem(i, 2, QTableWidgetItem(grade.getCredit()))
                self.this_term.setItem(i, 3, QTableWidgetItem(grade.getGrade()))
                curCrs = int(grade.getCredit())
                if(grade.getGrade() == None):
                    curCrs = 0
                crsGPS = crsGPS + curCrs
                if(grade.getGrade() == "A"):
                    sumGPS = sumGPS + 4.00 * curCrs
                elif(grade.getGrade() == "B+"):
                    sumGPS = sumGPS + 3.50 * curCrs
                elif(grade.getGrade() == "B"):
                    sumGPS = sumGPS + 3.00 * curCrs
                elif(grade.getGrade() == "C+"):
                    sumGPS = sumGPS + 2.50 * curCrs
                elif(grade.getGrade() == "C"):
                    sumGPS = sumGPS + 2.00 * curCrs
                elif(grade.getGrade() == "D+"):
                    sumGPS = sumGPS + 1.50 * curCrs
                elif(grade.getGrade() == "D"):
                    sumGPS = sumGPS + 1.00 * curCrs
                else:
                    sumGPS = sumGPS + 0
                i = i + 1
            else:
                self.this_term.setRowCount(len(cur_course)-1)

    #Calculate GPA/GPS
        gpa = sumGPA / crsGPA
        gps = 0
        if(sumGPS != 0):
            gps = sumGPS / crsGPS
        self.gpa_input.setText(str("{:0.2f}".format(gpa)))
        self.gps_input.setText(str("{:0.2f}".format(gps)))
        self.crs_input.setText(str(crsGPA))
        if(gpa >= 2.00):
            self.status_input.setText("PASS")
            status = 0
        elif(gpa < 2.00):
            self.status_input.setText("PROBATION")
            status = 1
        elif(gpa < 1.00):
            self.status_input.setText("RETIRE")
            status = 2
        else:
            self.status_input.setText("ERROR")
        db.updateData(data.getID, status, gpa)
        db.disconnect()

    def createBulk(self, data, courseData):
        temp = []
        for i in range(0, len(data)):
            temp.append(grade.gradeData(data[i], courseData[i]))
        return temp

