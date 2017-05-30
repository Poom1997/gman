from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
import plugin.databaseConnect as database

class AddFacultyUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900,600)
        self.setWindowTitle("Profile")
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("resources/images/programBackground.png")))
        self.setPalette(palette)
        self.bar = QPixmap("resources/images/topBarBackground.png")
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/addFaculty.ui",None)
        self.setCentralWidget(form)

        #Upper Bar
        self.bar_group = form.findChild(QLabel,"barLabel_2")
        self.bar_group.setPixmap(self.bar)
        self.home_button = form.findChild(QPushButton,"homeButton")
        self.profile_button = form.findChild(QPushButton,"profileButton")
        self.faculties_button = form.findChild(QPushButton,"facultiesButton")
        self.majors_button = form.findChild(QPushButton,"majorsButton")
        self.course_button = form.findChild(QPushButton,"courseButton")
        self.other_button = form.findChild(QPushButton, "othersButton")

        #page properties
        self.faculty_table = form.findChild(QTableWidget,"facultyTable")
        self.faculty_id = form.findChild(QLineEdit,"FacultyID")
        self.faculty_name = form.findChild(QLineEdit,"facultyName")
        self.add_button = form.findChild(QPushButton,"addFacButton")

        self.header = self.faculty_table.horizontalHeader()
        self.header.setResizeMode(0, QHeaderView.ResizeToContents)
        self.header.setResizeMode(1, QHeaderView.Stretch)
        self.header.setResizeMode(2, QHeaderView.ResizeToContents)

        self.faculty_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.faculty_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        #Upper Bar pressed
        self.home_button.clicked.connect(self.goHome)
        self.faculties_button.clicked.connect(self.goFac)
        self.majors_button.clicked.connect(self.goMaj)
        self.other_button.clicked.connect(self.goOther)
        self.course_button.clicked.connect(self.goCourse)
        self.profile_button.clicked.connect(self.goProfile)

        self.add_button.clicked.connect(self.add)

        self.db = database.databaseAdmin()

    def goHome(self):
        self.parent.changePageLoginSection("home")

    def goProfile(self):
        self.parent.changePageLoginSection("profile")

    def goFac(self):
        self.parent.changePageLoginSection("addfaculties")

    def goMaj(self):
        self.parent.changePageLoginSection("addmajor")

    def goCourse(self):
        self.parent.changePageLoginSection("addcourse")

    def goOther(self):
        self.parent.changePageLoginSection("otherOption")

    def updatePage(self):
        data = self.db.getallFaculty()
        self.faculty_table.setRowCount(len(data[0]))
        for i in range(0, len(data[0])):
            self.faculty_table.setItem(i, 0, QTableWidgetItem(data[0][i].facultyID))
            self.faculty_table.setItem(i, 1, QTableWidgetItem(data[0][i].facultyName))
            self.faculty_table.setItem(i, 2, QTableWidgetItem(str(data[1][i])))
        print(self.faculty_id.text())

    ##Add faculty into the system##
    def add(self):
        temp = None
        if (self.parent.showCONFIRM("Are you sure?",
                                    "Are you sure you want to add a Faculty? Once added, it cannot be deleted.")):
            if (self.faculty_id.text() == "" or self.faculty_name.text() == ""):
                self.parent.showERROR("Fields cannot be Empty", "Fields cannot be Empty. Please Try Again.")
            else:
                temp = self.db.addFaculty(self.faculty_id.text(), self.faculty_name.text())
            if (temp == 1):
                self.updatePage()
                self.parent.showOK("Faculty Added", "Faculty " + self.faculty_name.text() + " has been added to the system.")
            elif (temp == "DUPLICATE"):
                self.parent.showERROR("Faculty ID Duplication Error",
                                      "The ID you entered already exists. Please Try Again.")

             
