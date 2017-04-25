from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class mainUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900,600)
        self.setWindowTitle("Main")
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("resources/imagess/background.png")))
        self.setPalette(palette)
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/main.ui",None)
        self.setCentralWidget(form)
        self.home_button = form.findChild(QPushButton, "homeButton")
        self.status = form.findChild(QLabel,"status")

        self.home_button.clicked.connect(self.goHome)

    def goHome(self):
        self.parent.changePageLoginSection("home")
