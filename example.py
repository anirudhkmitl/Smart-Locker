# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Desktop/SmartLocker/Smart-Locker/loginScreenRFID.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loginScreenRFID(object):
    def setupUi(self, loginScreenRFID):
        loginScreenRFID.setObjectName("loginScreenRFID")
        loginScreenRFID.resize(730, 500)
        self.label_greeting = QtWidgets.QLabel(loginScreenRFID)
        self.label_greeting.setGeometry(QtCore.QRect(300, 170, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        self.label_greeting.setFont(font)
        self.label_greeting.setObjectName("label_greeting")
        self.label_request = QtWidgets.QLabel(loginScreenRFID)
        self.label_request.setGeometry(QtCore.QRect(260, 200, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_request.setFont(font)
        self.label_request.setObjectName("label_request")

        self.retranslateUi(loginScreenRFID)
        QtCore.QMetaObject.connectSlotsByName(loginScreenRFID)

    def retranslateUi(self, loginScreenRFID):
        _translate = QtCore.QCoreApplication.translate
        loginScreenRFID.setWindowTitle(_translate("loginScreenRFID", "Form"))
        self.label_greeting.setText(_translate("loginScreenRFID", "Hi There!"))
        self.label_request.setText(_translate("loginScreenRFID", "Please present your token."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginScreenRFID = QtWidgets.QWidget()
    ui = Ui_loginScreenRFID()
    ui.setupUi(loginScreenRFID)
    loginScreenRFID.show()
    sys.exit(app.exec_())

