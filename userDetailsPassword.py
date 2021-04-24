# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userDetailsPassword.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_userInfoUI(object):
    def setupUi(self, userInfoUI):
        if not userInfoUI.objectName():
            userInfoUI.setObjectName(u"userInfoUI")
        userInfoUI.resize(730, 500)
        self.userImage = QLabel(userInfoUI)
        self.userImage.setObjectName(u"userImage")
        self.userImage.setGeometry(QRect(250, 20, 181, 181))
        self.userImage.setFrameShape(QFrame.Box)
        self.userImage.setAlignment(Qt.AlignCenter)
        self.passwordInput = QLineEdit(userInfoUI)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setGeometry(QRect(230, 230, 241, 21))
        self.passwordInput.setEchoMode(QLineEdit.Password)
        self.widget = QWidget(userInfoUI)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(170, 270, 371, 211))
        self.keypad = QGridLayout(self.widget)
        self.keypad.setObjectName(u"keypad")
        self.keypad.setContentsMargins(0, 0, 0, 0)
        self.btnZero = QPushButton(self.widget)
        self.btnZero.setObjectName(u"btnZero")

        self.keypad.addWidget(self.btnZero, 3, 1, 1, 1)

        self.btnClear = QPushButton(self.widget)
        self.btnClear.setObjectName(u"btnClear")

        self.keypad.addWidget(self.btnClear, 3, 0, 1, 1)

        self.btnOne = QPushButton(self.widget)
        self.btnOne.setObjectName(u"btnOne")

        self.keypad.addWidget(self.btnOne, 0, 0, 1, 1)

        self.btnTwo = QPushButton(self.widget)
        self.btnTwo.setObjectName(u"btnTwo")

        self.keypad.addWidget(self.btnTwo, 0, 1, 1, 1)

        self.btnThree = QPushButton(self.widget)
        self.btnThree.setObjectName(u"btnThree")

        self.keypad.addWidget(self.btnThree, 0, 2, 1, 1)

        self.btnNine = QPushButton(self.widget)
        self.btnNine.setObjectName(u"btnNine")

        self.keypad.addWidget(self.btnNine, 2, 2, 1, 1)

        self.btnSeven = QPushButton(self.widget)
        self.btnSeven.setObjectName(u"btnSeven")

        self.keypad.addWidget(self.btnSeven, 2, 0, 1, 1)

        self.btnEight = QPushButton(self.widget)
        self.btnEight.setObjectName(u"btnEight")

        self.keypad.addWidget(self.btnEight, 2, 1, 1, 1)

        self.btnFour = QPushButton(self.widget)
        self.btnFour.setObjectName(u"btnFour")

        self.keypad.addWidget(self.btnFour, 1, 0, 1, 1)

        self.btnSix = QPushButton(self.widget)
        self.btnSix.setObjectName(u"btnSix")

        self.keypad.addWidget(self.btnSix, 1, 2, 1, 1)

        self.btnBackspace = QPushButton(self.widget)
        self.btnBackspace.setObjectName(u"btnBackspace")

        self.keypad.addWidget(self.btnBackspace, 3, 2, 1, 1)

        self.btnFive = QPushButton(self.widget)
        self.btnFive.setObjectName(u"btnFive")

        self.keypad.addWidget(self.btnFive, 1, 1, 1, 1)


        self.retranslateUi(userInfoUI)

        QMetaObject.connectSlotsByName(userInfoUI)
    # setupUi

    def retranslateUi(self, userInfoUI):
        userInfoUI.setWindowTitle(QCoreApplication.translate("userInfoUI", u"Form", None))
        self.userImage.setText(QCoreApplication.translate("userInfoUI", u"**image goes here**", None))
        self.btnZero.setText(QCoreApplication.translate("userInfoUI", u"0", None))
        self.btnClear.setText(QCoreApplication.translate("userInfoUI", u"Clear", None))
        self.btnOne.setText(QCoreApplication.translate("userInfoUI", u"1", None))
        self.btnTwo.setText(QCoreApplication.translate("userInfoUI", u"2", None))
        self.btnThree.setText(QCoreApplication.translate("userInfoUI", u"3", None))
        self.btnNine.setText(QCoreApplication.translate("userInfoUI", u"9", None))
        self.btnSeven.setText(QCoreApplication.translate("userInfoUI", u"7", None))
        self.btnEight.setText(QCoreApplication.translate("userInfoUI", u"8", None))
        self.btnFour.setText(QCoreApplication.translate("userInfoUI", u"4", None))
        self.btnSix.setText(QCoreApplication.translate("userInfoUI", u"6", None))
        self.btnBackspace.setText(QCoreApplication.translate("userInfoUI", u"<|", None))
        self.btnFive.setText(QCoreApplication.translate("userInfoUI", u"5", None))
    # retranslateUi

