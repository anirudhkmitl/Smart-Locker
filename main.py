import sys
from rfidConfirm import RfidConfirm
from multiprocessing import Pool
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication

class MainWindow(QDialog):
    def __init__(self):
        self.pool = Pool()
        super(MainWindow,self).__init__()
        loadUi("welcomeScreen.ui",self)
        self.getRfid()


    def getRfid(self):
        self.worker = WorkerThread()
        self.worker.start()
        self.worker.worker_complete.connect(self.evt_worker_finished)
        
    def evt_worker_finished(self,pin):
        print(pin)
        pinwindow = PinWindow(pin)
        widget.addWidget(pinwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
       
    
class WorkerThread(QThread):
    worker_complete = pyqtSignal(str)
    def run(self):
        pin = RfidConfirm.rfidUserValidate()
        self.worker_complete.emit(pin)
        


class PinWindow(QDialog):
    def __init__(self,pin):
        self.pin = pin
        self.count = 0
        super(PinWindow,self).__init__()
        loadUi("pinScreen.ui",self)
        self.dial = ""
        self.hidden = ""
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
        self.enterButton.clicked.connect(self.checkEnter)
    
    
    def checkEnter(self):
      
        if (not self.checkPin()):
            self.count += 1
            self.dial = ""
            self.hidden = ""
            self.lineEdit.setText(self.hidden)
        if (self.count == 3) :
            self.changeScreen()              
            
    
    def checkPin(self):
        if (self.dial == self.pin) :
            print ("Authorized\n\n")
            self.changeScreen()
            self.unlockDoor()
        else :
            return 0
        
    def unlockDoor(self):
        print("DOOR UNLOCKED")
    
    def changeScreen(self):
        
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
    def activate(self):
        sender = self.sender()
        if sender.text() == "0":
            self.dial += "0"
            self.hidden += "*"            
            self.lineEdit.setText(self.hidden)
        elif sender.text() == "1":
            self.dial += "1"
            self.hidden += "*"
            self.lineEdit.setText(self.hidden)
        elif sender.text() == "2":
            self.dial += "2"
            self.hidden += "*"
            self.lineEdit.setText(self.hidden)
        elif sender.text() == "3":
            self.dial += "3"
            self.hidden += "*"
            self.lineEdit.setText(self.hidden)
        elif sender.text() == "4":
            self.dial += "4"
            self.hidden += "*"
            self.lineEdit.setText(self.hidden)
        elif sender.text() == "5":
            self.hidden += "*"
            self.dial += "5"
            self.lineEdit.setText(self.hidden)
        elif sender.text() == "6":
            self.dial += "6"
            self.hidden += "*"
            self.lineEdit.setText(self.hidden)
        elif sender.text() == "7":
            self.dial += "7"
            self.hidden += "*"
            self.lineEdit.setText(self.hidden)
        elif sender.text() == "8":
            self.dial += "8"
            self.hidden += "*"
            self.lineEdit.setText(self.hidden)
        elif sender.text() == "9":
            self.dial += "9"
            self.hidden += "*"
            self.lineEdit.setText(self.hidden)
        elif sender.text() == "<":
            self.dial = self.dial[:len(self.dial)-1]
            self.hidden = self.hidden[:len(self.hidden)-1]
            self.lineEdit.setText(self.hidden)
            
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow()

widget.addWidget(mainwindow)
widget.setFixedHeight(552)
widget.setFixedWidth(458)
widget.show()




try :
    sys.exit(app.exec_())

except:
    print("Exiting")
