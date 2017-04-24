from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class pwUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900,600)
        self.setWindowTitle("Forget Your Password")
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("Images/background.png")))
        self.setPalette(palette)
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("pw.ui",None)
        self.setCentralWidget(form)
        self.home_button = form.findChild(QPushButton, "homeButton")

        self.home_button.clicked.connect(self.goHome)

    def goHome(self):
        self.parent.changePageLoginSection("home")
