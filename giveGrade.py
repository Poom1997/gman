from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from datetime import datetime
import plugin.databaseConnect as database
import plugin.grades as grade
from sendMessageForm import sendMessageUI
import csv

class QTableWidgetDisabledItem(QItemDelegate):
    """
    Create a readOnly QTableWidgetItem
    """
    def __init__(self, parent):

        QItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index):
        item = QLineEdit(parent)
        item.setReadOnly(True)
        #item.setEnabled(False)
        return item

    def setEditorData(self, editor, index):
        editor.blockSignals(True)
        editor.setText(index.model().data(index))
        editor.blockSignals(False)

    def setModelData(self, editor, model, index):
        model.setData(index, editor.text())

class addGradeAdmin(QMainWindow):
    def __init__(self, courseData, parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(622,738)
        self.setWindowTitle("Select Course")
        self.parent = parent
        self.courseData = courseData
        self.userDataCheck = {}
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/addGrade.ui",None)
        self.setCentralWidget(form)


        #page properties
        self.grade_table = form.findChild(QTableWidget,"addGradeTable")
        self.save_button = form.findChild(QPushButton,"saveButton")
        self.back_button = form.findChild(QPushButton,"backButton")
        self.import_button = form.findChild(QPushButton,"importButton")
        self.export_button = form.findChild(QPushButton,"exportButton")
        self.courseName = form.findChild(QLabel, "courseName")
        self.courseID = form.findChild(QLabel, "courseID")
        self.message = form.findChild(QPushButton, "messageButton")


        self.header = self.grade_table.horizontalHeader()
        self.header.setResizeMode(0,QHeaderView.ResizeToContents)
        self.header.setResizeMode(1,QHeaderView.Stretch)
        self.header.setResizeMode(2,QHeaderView.ResizeToContents)

        self.grade_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.grade_table.setSelectionMode(QAbstractItemView.SingleSelection)

        self.size = QTableWidgetDisabledItem(self.grade_table)
        self.grade_table.setItemDelegateForColumn(0,self.size)
        self.grade_table.setItemDelegateForColumn(1,self.size)

        #Internal Button Pressed
        self.save_button.clicked.connect(self.saveData)
        self.back_button.clicked.connect(self.backPage)
        self.import_button.clicked.connect(self.importFile)
        self.export_button.clicked.connect(self.exportFile)
        self.message.clicked.connect(self.createMessage)

    def updatePage(self):
        self.userID = []
        self.dataList = []
        self.courseName.setText(self.courseData.getCourseName())
        self.courseID.setText(self.courseData.getCourseID())
        db = database.databaseGrade()
        temp = db.getAllUserCourse(self.courseData.getCourseID(),datetime.now().year)
        self.grades = self.createBulk(temp)
        id = db.getUserData(temp)
        self.size = len(self.grades)
        self.grade_table.setRowCount(self.size)
        i = 0
        for items in self.grades:
            self.dataList.append([])
            self.grade_table.setItem(i,0,QTableWidgetItem(items.getUserID()))
            self.grade_table.setItem(i,1,QTableWidgetItem(id[items.getUserID()]))
            self.grade_table.setItem(i,2,QTableWidgetItem(items.getGrade()))
            self.userDataCheck[items.getUserID()] = id[items.getUserID()]
            self.userID.append(items.getUserID())
            self.dataList[i].append(items.getUserID())
            self.dataList[i].append(id[items.getUserID()])
            self.dataList[i].append(items.getGrade())
            i = i + 1

    def createMessage(self):
        self.createM = sendMessageUI(id = "ALL USER", bulk = self.userID, parent = self.parent)
        self.createM.show()

    ##Import CSV file into the program and put the data into the table##
    def importFile(self):
        if(self.parent.parent.showCONFIRM("Are you sure?", "The data will be replaced with the data in the file.\nPlease ensure you have the updated file.")):
            try:
                dlg = QFileDialog()
                dlg.setFileMode(QFileDialog.AnyFile)
                dlg.setFilter("CSV Files (*.csv)")
                if dlg.exec_():
                    filenames = dlg.selectedFiles()
                with open(filenames[0], 'r', newline="\n", encoding="utf-8") as infile:
                    reader = csv.reader(infile, delimiter=',')
                    my_list = list(reader)
                    testData = my_list[0]
                    if(testData[0] == self.courseData.getCourseName() and testData[1] ==  self.courseData.getCourseID() and testData[2] == str(datetime.now().year)):
                        my_list = my_list[2:-1]
                        i = 0
                        if(len(my_list)!= len(self.dataList)):
                            self.parent.parent.showERROR("User Amount Mismatch",
                                                     "The data in the file mismatch the data in this course.\nPlease Use Correct File Format Exported from the program.")
                        else:
                            for data in my_list:
                                if(data[0] == self.grade_table.item(i,0).text() and data[1] == self.grade_table.item(i,1).text()):
                                    self.grade_table.setItem(i, 2, QTableWidgetItem(data[2]))
                                    i = i + 1
                                else:
                                    raise KeyError
                            self.parent.parent.showOK("File Imported", "The Data has been imported")

                    else:
                        self.parent.parent.showERROR("File Error", "The File you provided is invalid for this course.\nPlease Use Correct File Format Exported from the program.")

            except UnboundLocalError:
                pass
            except KeyError:
                self.parent.parent.showERROR("Data Error", "The Data you provide do not match the records for this course.\
                                                \nERROR AT: ROW " + str(+3) + "\nThe importing has been stop at user: " + data[1])

    ##Export table that contain list of student ID,name and grade as CSV file format##
    def exportFile(self):
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        with open(directory + '\\' + str(self.courseData.getCourseID()) + '.csv', 'w', newline="\n", encoding="utf-8") as outfile:
            writer = csv.writer(outfile, delimiter=',')
            writer.writerow([self.courseData.getCourseName(), self.courseData.getCourseID(),datetime.now().year ])
            writer.writerow(['StudentID', 'StudentName', 'StudentGrade'])
            for data in self.dataList:
                writer.writerow(data)
            writer.writerow(['You can edit', 'anything', 'EXCEPT first 3 column'])
        outfile.close()
        self.parent.parent.showOK("Data Exported", "The data has been exported to the directory you have chosen successfully.")

    ##Use for saving data after professor edit student grade##
    def saveData(self):
        tempData = []
        for i in range(0, self.size):
            tempData.append([])
            tempData[i].append(self.grade_table.item(i,0).text())
            tempGrade = self.grade_table.item(i,2).text().upper()
            if(self.checkData(tempGrade)):
                tempData[i].append(tempGrade)
                db = database.databaseGrade()
                if (db.updateUserGrade(tempData, self.courseData.getCourseID(), datetime.now().year)):
                    self.parent.parent.showOK("Grade Successfully Saved",
                                              "The data entered has been successfully saved in the system.")
                    db.disconnect()
                    self.close()
            else:
                self.parent.parent.showERROR("Error","The Grade you entered for " + self.grade_table.item(i,0).text() + " is invalid. Please Check." )

    ##Grade that professor input must be in this datalist##
    def checkData(self, grade):
        data = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
        if(grade in data):
            return True
        return False

    def backPage(self):
        self.close()

    def createBulk(self, data):
        temp = []
        for i in data:
            temp.append(grade.gradeData(i, self.courseData))
        return temp
