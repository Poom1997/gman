from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from datetime import datetime
import plugin.databaseConn as database
import plugin.course as courseItem
from sendMessageForm import sendMessageUI

class searchCourseByIDUI(QMainWindow):
    def __init__(self,parent = None ):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900,371)
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
        self.message = form.findChild(QPushButton, "messageButton")
        
        #LineEdit
        self.course_ID = form.findChild(QLineEdit,"courseID")
        
        #Label
        self.course_id2 = form.findChild(QLabel,"courseID_2")
        self.course_name = form.findChild(QLabel, "courseName")
        self.major = form.findChild(QLabel,"major")
        self.year = form.findChild(QLabel,"year")
        self.time = form.findChild(QLabel,"time")
        self.location = form.findChild(QLabel,"location")
        self.crs = form.findChild(QLabel,"crs")
        self.pre_requisite = form.findChild(QLabel,"preRequisite")

        
        #Connect
        self.search_button.clicked.connect(self.search)
        self.cancel_button.clicked.connect(self.close)
        self.message.clicked.connect(self.createMessage)

    def createMessage(self):
        self.createM = sendMessageUI(parent = self.parent)
        self.createM.show()


    def cancel(self):
        self.close()

    def search(self):
        pass

    
        

    
    

    
        
    
