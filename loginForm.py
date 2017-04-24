from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class LoginUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900, 600)
        self.setWindowTitle("Login")
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("Images/background.png")))
        self.logo = QPixmap("images/templogo.png")
        self.setPalette(palette)
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("login.ui", None)
        self.setCentralWidget(form)
        self.logolabel = form.findChild(QLabel,"label_2")
        self.logolabel.setPixmap(self.logo)
        self.user_id = form.findChild(QLineEdit, "usernameinp")
        self.password = form.findChild(QLineEdit, "pwinp")

        self.login_button = form.findChild(QPushButton, "loginButton")

        self.forgetpw_button = form.findChild(QCommandLinkButton, "forgetButton")


        self.login_button.clicked.connect(self.logIn)
        self.forgetpw_button.clicked.connect(self.forgetpass)
        

    def logIn(self):
        self.parent.changePageLoginSection("login")

    def forgetpass(self):
        self.parent.changePageLoginSection("forget")
        
