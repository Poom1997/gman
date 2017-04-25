from loginForm import *
from mainForm import *
from pwForm import *
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

import sys

class GUImanager(QMainWindow):
    def __init__(self):
        #Main UI set up
        QMainWindow.__init__(self, None)
        self.setMinimumSize(900, 600)
        self.setWindowTitle("GMan Systems")
        self.setFixedSize(self.size())
        
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("resources/images/background.png")))
        self.setPalette(palette)

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.login_widget = LoginUI(self)
        self.main_widget = mainUI(self)
        self.pw_widget = pwUI(self)
        self.central_widget.addWidget(self.login_widget)
        self.central_widget.addWidget(self.main_widget)
        self.central_widget.addWidget(self.pw_widget)

    def changePageLoginSection(self,signal = None):
        if signal == "login":
            self.centralWidget().setCurrentWidget(self.main_widget)
        if signal == "forget":
            print("forget")
            self.centralWidget().setCurrentWidget(self.pw_widget)
        if signal == "home":
            print("home")
            self.centralWidget().setCurrentWidget(self.login_widget)



def main():
    app = QApplication(sys.argv)
    ui = GUImanager()
    ui.show()
    app.exec_()

if __name__ == "__main__":
    main()

        
