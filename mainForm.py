from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class mainUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900,600)
        self.setWindowTitle("Main")
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("Images/background.png")))
        self.setPalette(palette)
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("main.ui",None)
        self.setCentralWidget(form)
        
