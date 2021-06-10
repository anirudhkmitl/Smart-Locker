import pymysql
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication

class MainWindow(QDialog) :
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("createUserScreen.ui",self)
        self.pushButton.clicked.connect(self.createUser)
        self.userID = ""
        self.name = ""
        self.rfid = ""
        self.pin = ""

    def readUser(self):
        self.userID = self.lineEdit.getText()
        self.name = self.lineEdit_2.getText()
        self.rfid = self.lineEdit_3.getText()
        self.pin = self.lineEdit_4.getText()
        self.writeToDatabase

    def writeToDatabase(self):

        connection = pymysql.connect(host="localhost",user="root",passwd="password",database="smartLocker" )
        cursor = connection.cursor()
        connection.commit()
        retrieve = ("INSERT INTO access_list VALUES(%s,%s,%s,%s,%s,%s)"% self.userID,self.name,None,self.rfid,self.pin,None)
        cursor.execute(sql_pin)




app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow()

widget.add(mainwindow)
widget.show()

try :
    sys.exit(app.exec_())

except:
    print("Exiting")

