from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class profileUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900,600)
        self.setWindowTitle("Profile")
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("resources/imagess/background.png")))
        self.setPalette(palette)
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/profile.ui",None)
        self.setCentralWidget(form)
        self.home_button = form.findChild(QPushButton, "homeButton")
        self.edit_button = form.findChild(QPushButton, "editButton")
        self.status = form.findChild(QLabel,"status")

        self.id = form.findChild(QLabel,"id")
        self.name = form.findChild(QLabel,"name")
        self.surname = form.findChild(QLabel,"surmane")
        self.email = form.findChild(QLabel,"email")
        self.faculty = form.findChild(QLabel,"faculty")
        self.major = form.findChild(QLabel,"major")
        self.year = form.findChild(QLabel,"year")
        self.student_status = form.findChild(QLabel,"sstatus")
        self.address = form.findChild(QLabel,"address")

        self.home_button.clicked.connect(self.goHome)

    def goHome(self):
        self.parent.changePageLoginSection("home")
