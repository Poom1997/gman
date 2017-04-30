from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class StudentCourseUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900, 600)
        self.setWindowTitle("Courses")
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("resources/images/background.png")))
        self.logo = QPixmap("resources/images/templogo.png")
        self.setPalette(palette)
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/studentcourse.ui", None)
        self.setCentralWidget(form)
        self.home_button = form.findChild(QPushButton,"homeButton")
        self.available_course = form.findChild(QListView,"availableView")
        self.your_course = form.findChild(QListView,"yourView")
        self.left_scroll = form.findChild(QScrollBar,"ascroll")
        self.right_scroll = form.findChild(QScrollBar,"bscroll")
        self.save_button = form.findChild(QPushButton,"saveButton")

        self.home_button.clicked.connect(self.goHome)

    def goHome(self):
        self.parent.changePageLoginSection("home")
    
        
