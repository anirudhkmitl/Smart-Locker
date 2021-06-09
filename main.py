import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("welcomeScreen.ui",self)

    def getRfid(self):

        pinwindow = PinWindow()
        widget.addWidget(pinwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)



class PinWindow(QDialog):
    def __init__(self):
        super(PinWindow,self).__init__()
        loadUi("pinScreen.ui",self)
        self.dial = ""
        self.zeroButton.clicked.connect(self.activate)
        self.oneButton.clicked.connect(self.activate)
        self.twoButton.clicked.connect(self.activate)
        self.threeButton.clicked.connect(self.activate)
        self.fourButton.clicked.connect(self.activate)
        self.fiveButton.clicked.connect(self.activate)
        self.sixButton.clicked.connect(self.activate)
        self.sevenButton.clicked.connect(self.activate)
        self.eightButton.clicked.connect(self.activate)
        self.nineButton.clicked.connect(self.activate)
        self.clearButton.clicked.connect(self.activate)
        
    def activate(self):
        sender = self.sender()
        if sender.text() == "0":
            self.dial += "0"
            self.lineEdit.setText(self.dial)
        elif sender.text() == "1":
            self.dial += "1"
            self.lineEdit.setText(self.dial)
        elif sender.text() == "2":
            self.dial += "2"
            self.lineEdit.setText(self.dial)
        elif sender.text() == "3":
            self.dial += "3"
            self.lineEdit.setText(self.dial)
        elif sender.text() == "4":
            self.dial += "4"
            self.lineEdit.setText(self.dial)
        elif sender.text() == "5":
            self.dial += "5"
            self.lineEdit.setText(self.dial)
        elif sender.text() == "6":
            self.dial += "6"
            self.lineEdit.setText(self.dial)
        elif sender.text() == "7":
            self.dial += "7"
            self.lineEdit.setText(self.dial)
        elif sender.text() == "8":
            self.dial += "8"
            self.lineEdit.setText(self.dial)
        elif sender.text() == "9":
            self.dial += "9"
            self.lineEdit.setText(self.dial)
        elif sender.text() == "<":
            self.dial = self.dial[:len(self.dial)-1]
            self.lineEdit.setText(self.dial)
            
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow()


widget.addWidget(mainwindow)

widget.setFixedHeight(552)
widget.setFixedWidth(458)
widget.show()
mainwindow.getRfid()

try :
    sys.exit(app.exec_())

except:
    print("Exiting")
