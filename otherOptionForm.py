from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from sendMessageForm import sendMessageUI
from addUser import addUserUI
from findUser import findUserUI
from searchProfByCourseID import findProfByCourseIDUI
from addCourseToProfForm import addCourseToProfUI
from searchProfByCourseID import findProfByCourseIDUI
from searchCourseByProfIDForm import searchCourseByProfIDUI
from findCourse import findCourseUI
import plugin.databaseConnect as database

class otherOptionUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900,600)
        self.setWindowTitle("Class Course")
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("resources/imagess/programBackground.png")))
        self.edu_logo = QPixmap("resources/images/educationLogo.png")
        self.setPalette(palette)
        self.bar = QPixmap("resources/images/topBarBackground.png")
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/otherOption.ui",None)
        self.setCentralWidget(form)
        
        #Upper Bar
        self.bar_group = form.findChild(QLabel,"barLabel")
        self.bar_group.setPixmap(self.bar)
        self.home_button = form.findChild(QPushButton,"homeButton")
        self.profile_button = form.findChild(QPushButton,"profileButton")
        self.faculties_button = form.findChild(QPushButton,"facultiesButton")
        self.majors_button = form.findChild(QPushButton,"majorsButton")
        self.course_button = form.findChild(QPushButton,"courseButton")
        self.other_button = form.findChild(QPushButton, "othersButton")

        #page properties
        self.add_user_button = form.findChild(QPushButton,"addUserButton")
        self.search_user_button = form.findChild(QPushButton,"searchUserButton")
        self.assign_course_button = form.findChild(QPushButton,"assignCourseButton")
        self.search_course_by_id = form.findChild(QPushButton,"searchCourseByID")
        self.search_prof_by_course = form.findChild(QPushButton,"searchProfByCourseID")
        self.search_course_by_prof = form.findChild(QPushButton, "searchCourseByProfID")
        self.message = form.findChild(QPushButton, "messageButton")
        self.increase_year = form.findChild(QPushButton, "increaseYearButton")


        #Upper Bar pressed
        self.home_button.clicked.connect(self.goHome)
        self.faculties_button.clicked.connect(self.goFac)
        self.majors_button.clicked.connect(self.goMaj)
        self.other_button.clicked.connect(self.goOther)
        self.course_button.clicked.connect(self.goCourse)
        self.profile_button.clicked.connect(self.goProfile)

        #Internal Button Pressed
        self.add_user_button.clicked.connect(self.addUser)
        self.search_user_button.clicked.connect(self.searchUser)
        self.assign_course_button.clicked.connect(self.assignCoursetoProf)
        self.search_course_by_id.clicked.connect(self.searchCoursebyID)
        self.search_prof_by_course.clicked.connect(self.searchProfbyCourse)
        self.search_course_by_prof.clicked.connect(self.searchCoursebyProf)
        self.message.clicked.connect(self.createMessage)
        self.increase_year.clicked.connect(self.increaseYears)

    def increaseYears(self):
        db = database.databaseAdmin()
        if(self.parent.showCONFIRM("Are you sure?", "Are you sure you want to iterate year and term?\n Once done, it cannot be un-done.")):
            if (self.parent.showCONFIRM("CRITICAL WARNING","THIS ACTION CANNOT BE UNDONE. PLEASE CONFIRM ACTION.")):
                if(db.incrementData()):
                    self.parent.showOK("Data Edited", "All Year and Term are iterated.")
    
    def createMessage(self):
        self.createM = sendMessageUI(parent = self.parent)
        self.createM.show()

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

    def addUser(self):
        self.addUs = addUserUI(parent = self.parent)
        self.addUs.show()

    def searchUser(self):
        self.searchUs = findUserUI(parent = self.parent)
        self.searchUs.show()

    def assignCoursetoProf(self):
        self.assigning = addCourseToProfUI(parent = self.parent)
        self.assigning.show()

    def searchCoursebyID(self):
        self.findCourseUI = findCourseUI(None, None, None, None, parent = self)
        self.findCourseUI.show()

    def searchProfbyCourse(self):
        self.searchCourseID = findProfByCourseIDUI(parent = self.parent)
        self.searchCourseID.show()

    def searchCoursebyProf(self):
        self.searchCourseID = searchCourseByProfIDUI(parent = self.parent)
        self.searchCourseID.show()
        



















        
