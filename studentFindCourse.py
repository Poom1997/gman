from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


class editProfileUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900,600)
        self.setWindowTitle("Find_Course")
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/studentFindCourse.ui",None)
        self.setCentralWidget(form)

        #QPushButton
        self.search_button = form.findChild(QPushButton,"pushButton")
        self.cancel_button = form.findChild(QPushButton,"pushButton_2")
        

        #LineEdit
        self.faculty_name_edit = form.findChild(QLineEdit,"lineEdit_3")
        self.year_edit = form.findChild(QLineEdit,"lineEdit_4")
        self.semester_edit = form.findChild(QLineEdit,"lineEdit_5")

       #Tabel
        self.course_table = form.findChild(QTableWidget,"tableWidget")

        
        #Connect
        self.search_button.clicked.connect(self.search)
        self.cancel_button.clicked.connect(self.cancel)

    def cancel(self):
        pass

    def search(self):
        pass
        

    
    

    
        
    
