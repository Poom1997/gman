from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from datetime import datetime
import plugin.databaseConn as database
import plugin.course as courseItem

class searchCourseByIDUI(QMainWindow):
    def __init__(self,parent = None ):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900,600)
        self.setWindowTitle("searchCourseByID")
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/searchCourseByID.ui",None)
        self.setCentralWidget(form)

        #QPushButton
        self.search_button = form.findChild(QPushButton,"searchButton")
        self.cancel_button = form.findChild(QPushButton,"closeButton")
        
        #LineEdit
        self.course_ID = form.findChild(QLineEdit,"courseID")

        #Table
        self.course_table = form.findChild(QTableWidget,"tableWidget")
        self.course_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.course_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.course_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.course_table_header = self.course_table.horizontalHeader()
        self.course_table_header.setResizeMode(0, QHeaderView.ResizeToContents)
        self.course_table_header.setResizeMode(1, QHeaderView.Stretch)
        self.course_table_header.setResizeMode(2, QHeaderView.ResizeToContents)
        self.course_table_header.setResizeMode(3, QHeaderView.ResizeToContents)
        self.course_table_header.setResizeMode(4, QHeaderView.ResizeToContents)
        self.course_table_header.setResizeMode(5, QHeaderView.ResizeToContents)
        self.course_table_header.setResizeMode(7, QHeaderView.ResizeToContents)
        self.course_table_header.setResizeMode(8, QHeaderView.ResizeToContents)

        #Connect
        self.search_button.clicked.connect(self.search)
        self.cancel_button.clicked.connect(self.close)


    def cancel(self):
        self.close()

    def search(self):
        pass

    
        

    
    

    
        
    
