# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Desktop/SmartLocker/Smart-Locker/userDetailsPassword.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_userInfoUI(object):
    def setupUi(self, userInfoUI):
        userInfoUI.setObjectName("userInfoUI")
        userInfoUI.resize(730, 500)
        #self.userImage = QtWidgets.QLabel(userInfoUI)
        #self.userImage.setGeometry(QtCore.QRect(250, 20, 181, 181))
        #self.userImage.setFrameShape(QtWidgets.QFrame.Box)
        #self.userImage.setAlignment(QtCore.Qt.AlignCenter)
        #self.userImage.setObjectName("userImage")
        self.passwordInput = QtWidgets.QLineEdit(userInfoUI)
        self.passwordInput.setGeometry(QtCore.QRect(230, 230, 241, 21))
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setObjectName("passwordInput")
        self.widget = QtWidgets.QWidget(userInfoUI)
        self.widget.setGeometry(QtCore.QRect(170, 270, 371, 211))
        self.widget.setObjectName("widget")
        self.keypad = QtWidgets.QGridLayout(self.widget)
        self.keypad.setContentsMargins(0, 0, 0, 0)
        self.keypad.setObjectName("keypad")
        self.btnZero = QtWidgets.QPushButton(self.widget)
        self.btnZero.setObjectName("btnZero")
        self.keypad.addWidget(self.btnZero, 3, 1, 1, 1)
        self.btnClear = QtWidgets.QPushButton(self.widget)
        self.btnClear.setObjectName("btnClear")
        self.keypad.addWidget(self.btnClear, 3, 0, 1, 1)
        self.btnOne = QtWidgets.QPushButton(self.widget)
        self.btnOne.setObjectName("btnOne")
        self.keypad.addWidget(self.btnOne, 0, 0, 1, 1)
        self.btnTwo = QtWidgets.QPushButton(self.widget)
        self.btnTwo.setObjectName("btnTwo")
        self.keypad.addWidget(self.btnTwo, 0, 1, 1, 1)
        self.btnThree = QtWidgets.QPushButton(self.widget)
        self.btnThree.setObjectName("btnThree")
        self.keypad.addWidget(self.btnThree, 0, 2, 1, 1)
        self.btnNine = QtWidgets.QPushButton(self.widget)
        self.btnNine.setObjectName("btnNine")
        self.keypad.addWidget(self.btnNine, 2, 2, 1, 1)
        self.btnSeven = QtWidgets.QPushButton(self.widget)
        self.btnSeven.setObjectName("btnSeven")
        self.keypad.addWidget(self.btnSeven, 2, 0, 1, 1)
        self.btnEight = QtWidgets.QPushButton(self.widget)
        self.btnEight.setObjectName("btnEight")
        self.keypad.addWidget(self.btnEight, 2, 1, 1, 1)
        self.btnFour = QtWidgets.QPushButton(self.widget)
        self.btnFour.setObjectName("btnFour")
        self.keypad.addWidget(self.btnFour, 1, 0, 1, 1)
        self.btnSix = QtWidgets.QPushButton(self.widget)
        self.btnSix.setObjectName("btnSix")
        self.keypad.addWidget(self.btnSix, 1, 2, 1, 1)
        self.btnBackspace = QtWidgets.QPushButton(self.widget)
        self.btnBackspace.setObjectName("btnBackspace")
        self.keypad.addWidget(self.btnBackspace, 3, 2, 1, 1)
        self.btnFive = QtWidgets.QPushButton(self.widget)
        self.btnFive.setObjectName("btnFive")
        self.keypad.addWidget(self.btnFive, 1, 1, 1, 1)

        self.retranslateUi(userInfoUI)
        QtCore.QMetaObject.connectSlotsByName(userInfoUI)

    def retranslateUi(self, userInfoUI):
        _translate = QtCore.QCoreApplication.translate
        userInfoUI.setWindowTitle(_translate("userInfoUI", "Form"))
        #self.userImage.setText(_translate("userInfoUI", "**image goes here**"))
        self.btnZero.setText(_translate("userInfoUI", "0"))
        self.btnClear.setText(_translate("userInfoUI", "Clear"))
        self.btnOne.setText(_translate("userInfoUI", "1"))
        self.btnTwo.setText(_translate("userInfoUI", "2"))
        self.btnThree.setText(_translate("userInfoUI", "3"))
        self.btnNine.setText(_translate("userInfoUI", "9"))
        self.btnSeven.setText(_translate("userInfoUI", "7"))
        self.btnEight.setText(_translate("userInfoUI", "8"))
        self.btnFour.setText(_translate("userInfoUI", "4"))
        self.btnSix.setText(_translate("userInfoUI", "6"))
        self.btnBackspace.setText(_translate("userInfoUI", "<|"))
        self.btnFive.setText(_translate("userInfoUI", "5"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    userInfoUI = QtWidgets.QWidget()
    ui = Ui_userInfoUI()
    ui.setupUi(userInfoUI)
    userInfoUI.show()
    sys.exit(app.exec_())

