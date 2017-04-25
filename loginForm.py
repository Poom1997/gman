from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class LoginUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900, 600)
        self.setWindowTitle("Login")
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("resources/images/background.png")))
        self.logo = QPixmap("resources/images/templogo.png")
        self.setPalette(palette)
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/login.ui", None)
        self.setCentralWidget(form)
        self.logolabel = form.findChild(QLabel,"label_2")
        self.logolabel.setPixmap(self.logo)
        self.wronglabel = form.findChild(QLabel,"wrong")
        self.user_id = form.findChild(QLineEdit, "usernameinp")
        self.password = form.findChild(QLineEdit, "pwinp")

        self.login_button = form.findChild(QPushButton, "loginButton")

        self.forgetpw_button = form.findChild(QCommandLinkButton, "forgetButton")

        self.status = form.findChild(QLabel,"status")
        self.login_button.clicked.connect(self.logIn)
        self.forgetpw_button.clicked.connect(self.forgetpass)
        

    def logIn(self):
        self.testUsr = "Atiruj"
        self.testPw = "Silnumkij"
        if(self.user_id.text() == self.testUsr and self.password.text() == self.testPw):
                self.wronglabel.setText("")
                self.user_id.setText("")
                self.password.setText("")
                self.parent.changePageLoginSection("login")
        else:
            self.wronglabel.setText("***Wrong Username or Password***")
            self.user_id.setText("")
            self.password.setText("")
        

    def forgetpass(self):
        self.wronglabel.setText("")
        self.parent.changePageLoginSection("forget")
        
