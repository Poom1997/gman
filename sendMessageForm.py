from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


class sendMessageUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(626,380)
        self.setWindowTitle("Message")
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/sendMessage.ui",None)
        self.setCentralWidget(form)

        #QPushButton
        self.send_button = form.findChild(QPushButton,"sendButton")
        self.close_button = form.findChild(QPushButton,"closeButton")
        

        #LineEdit
        self.to_user = form.findChild(QLineEdit,"to")
        self.message = form.findChild(QTextEdit,"message")

        #Connect
        self.send_button.clicked.connect(self.sendMes)
        self.close_button.clicked.connect(self.closeWindow)


    

    def closeWindow(self):
        self.close()

    def sendMes(self):
        pass
        

    
    

    
        
    
