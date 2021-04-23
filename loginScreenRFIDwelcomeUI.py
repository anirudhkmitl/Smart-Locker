# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginScreenRFID.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_loginScreenRFID(object):
    def setupUi(self, loginScreenRFID):
        if not loginScreenRFID.objectName():
            loginScreenRFID.setObjectName(u"loginScreenRFID")
        loginScreenRFID.resize(730, 500)
        self.label_greeting = QLabel(loginScreenRFID)
        self.label_greeting.setObjectName(u"label_greeting")
        self.label_greeting.setGeometry(QRect(300, 170, 141, 31))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        self.label_greeting.setFont(font)
        self.label_request = QLabel(loginScreenRFID)
        self.label_request.setObjectName(u"label_request")
        self.label_request.setGeometry(QRect(260, 200, 231, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.label_request.setFont(font1)

        self.retranslateUi(loginScreenRFID)

        QMetaObject.connectSlotsByName(loginScreenRFID)
    # setupUi

    def retranslateUi(self, loginScreenRFID):
        loginScreenRFID.setWindowTitle(QCoreApplication.translate("loginScreenRFID", u"Form", None))
        self.label_greeting.setText(QCoreApplication.translate("loginScreenRFID", u"Hi There!", None))
        self.label_request.setText(QCoreApplication.translate("loginScreenRFID", u"Please present your token.", None))
    # retranslateUi

