from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
import plugin.databaseConn as database
from datetime import datetime


class sendMessageUI(QMainWindow):
    def __init__(self, id = None, parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(626,380)
        self.setWindowTitle("Message")
        self.parent = parent
        self.id = id
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

        if(self.id != None):
            self.to_user.setText(self.id)

    def closeWindow(self):
        self.close()

    def sendMes(self):
        data = self.parent.getCurrentUser()
        db = database.databaseMessage()
        toUser = self.to_user.text()
        fromUser = data.getID()
        message = self.message.toPlainText()
        time = datetime.now()
        if(db.sendMessage(toUser, fromUser, message, time)):
            db.disconnect()
            self.parent.showOK("Message Sent", "The message has been sent to the user!")
            self.closeWindow()
        else:
            self.parent.showERROR("UserID Not Found", "The UserID you entered does not exists.")
        

    
    

    
        
    
