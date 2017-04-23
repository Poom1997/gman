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
        self.setPalette(palette)
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("login.ui", None)
        self.setCentralWidget(form)

        self.user_id = form.findChild(QLineEdit, "usernameinp")
        self.password = form.findChild(QLineEdit, "pwinp")

        self.login_button = form.findChild(QPushButton, "loginButton")


        self.login_button.clicked.connect(self.logIn)

    def logIn(self):
        self.parent.changePageLoginSection("login")
        
