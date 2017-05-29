from jinja2 import Environment, FileSystemLoader
import sys
import os
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *
from datetime import datetime
import time

class printGrades:
    def __init__(self, type, userData, userGrades, parent):
        self.userData = userData
        self.parent = parent
        env = Environment(loader=FileSystemLoader('.'))
        if(type == "ADMIN"):
            template = env.get_template("printingTemplate.html")
        else:
            template = env.get_template("printingTemplate.html")
        data = userGrades
        template_vars = {"ID": self.userData[0],
                         "name": self.userData[1],
                         "faculty": self.userData[2],
                         "degree": self.userData[3],
                         "status" : self.userData[5],
                         "GPA": self.userData[4],
                         "TIME": datetime.now(),
                         "gradesData": data}
        finalFile = template.render(template_vars)
        tempfile = open('temp.html','w')
        tempfile.write(finalFile)
        tempfile.close()

    def printPDF(self):
        directory = str(QFileDialog.getExistingDirectory(self.parent, "Select Directory"))

        self.dir = directory + '\\' + self.userData[0] + '.pdf'
        self.web = QWebView()
        self.web.load(QUrl("temp.html"))

        self.printer = QPrinter()
        self.printer.setPageSize(QPrinter.A4)
        self.printer.setOutputFormat(QPrinter.PdfFormat)
        self.printer.setOutputFileName(self.dir)

        QObject.connect(self.web, SIGNAL("loadFinished(bool)"), self.convertIt)

    def convertIt(self):
        self.web.print_(self.printer)
        self.parent.showOK("Exporting", "Exporting takes several seconds. Please wait.")
        time.sleep(3)
        self.deleteData()

    def deleteData(self):
        try:
            os.remove("temp.html")
        except FileNotFoundError:
            pass