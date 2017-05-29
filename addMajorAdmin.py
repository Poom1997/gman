from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
import plugin.databaseConnect as database

class AddMajorUI(QMainWindow):
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
        form = loader.load("resources/UI/addMajor.ui",None)
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
        self.majorTable = form.findChild(QTableWidget,"majorTable")
        self.faculty_id = form.findChild(QLineEdit,"facultyID")
        self.major_id = form.findChild(QLineEdit,"majorID")
        self.major_name = form.findChild(QLineEdit,"majorName")
        self.add_button = form.findChild(QPushButton,"addButton")
        self.search_button = form.findChild(QPushButton,"searchButton")

        self.add_button.setEnabled(False)

        self.header = self.majorTable.horizontalHeader()
        self.header.setResizeMode(0,QHeaderView.ResizeToContents)
        self.header.setResizeMode(1,QHeaderView.Stretch)
        self.header.setResizeMode(2,QHeaderView.ResizeToContents)

        self.majorTable.setSelectionMode(QAbstractItemView.NoSelection)
        self.majorTable.setEditTriggers(QAbstractItemView.NoEditTriggers)


        #Upper Bar pressed
        self.home_button.clicked.connect(self.goHome)
        self.faculties_button.clicked.connect(self.goFac)
        self.majors_button.clicked.connect(self.goMaj)
        self.other_button.clicked.connect(self.goOther)
        self.course_button.clicked.connect(self.goCourse)
        self.profile_button.clicked.connect(self.goProfile)

        self.add_button.clicked.connect(self.add)
        self.search_button.clicked.connect(self.searchMajor)
        self.faculty_id.returnPressed.connect(self.searchMajor)

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

    def add(self):
        temp = None
        if(self.parent.showCONFIRM("Are you sure?", "Are you sure you want to add a major for this faculty? Once added, it cannot be deleted.")):
            if(self.major_id.text() == "" or self.major_name.text() == ""):
                self.parent.showERROR("Fields cannot be Empty", "Fields cannot be Empty. Please Try Again.")
            else:
                temp = self.db.addMajors(self.faculty_id.text(), self.major_id.text(), self.major_name.text())
            if (temp == 1):
                self.searchMajor()
                self.parent.showOK("Major Added", "Major " + self.major_name.text() + " has been added to the system.")
            elif (temp == "DUPLICATE"):
                self.parent.showERROR("Major ID Duplication Error or Faculty not Found", "The ID you entered already exists or the Faculty ID5 is incorrect. Please Try Again.")

    def searchMajor(self):
        data = self.db.getallMajors(self.faculty_id.text())
        print(data)
        if (len(data[0]) >= 0):
            self.add_button.setEnabled(True)
            self.majorTable.setRowCount(len(data[0]))
            for i in range(0, len(data[0])):
                self.majorTable.setItem(i, 0, QTableWidgetItem(data[0][i].majorID))
                self.majorTable.setItem(i, 1, QTableWidgetItem(data[0][i].degree))
                self.majorTable.setItem(i, 2, QTableWidgetItem(str(data[1][i])))
        else:
            self.add_button.setEnabled(False)
