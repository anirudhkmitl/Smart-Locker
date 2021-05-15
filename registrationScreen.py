# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registrationScreen.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(730, 500)
        self.registerLabel = QLabel(Form)
        self.registerLabel.setObjectName(u"registerLabel")
        self.registerLabel.setGeometry(QRect(230, 20, 311, 51))
        font = QFont()
        font.setPointSize(28)
        self.registerLabel.setFont(font)
        self.nameLabel = QLabel(Form)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(60, 90, 41, 21))
        font1 = QFont()
        font1.setPointSize(12)
        self.nameLabel.setFont(font1)
        self.telephoneLabel = QLabel(Form)
        self.telephoneLabel.setObjectName(u"telephoneLabel")
        self.telephoneLabel.setGeometry(QRect(60, 140, 101, 21))
        self.telephoneLabel.setFont(font1)
        self.passconfirmLable = QLabel(Form)
        self.passconfirmLable.setObjectName(u"passconfirmLable")
        self.passconfirmLable.setGeometry(QRect(60, 240, 161, 21))
        self.passconfirmLable.setFont(font1)
        self.nameLabel_2 = QLabel(Form)
        self.nameLabel_2.setObjectName(u"nameLabel_2")
        self.nameLabel_2.setGeometry(QRect(60, 190, 101, 21))
        self.nameLabel_2.setFont(font1)
        self.telephoneNumber = QLineEdit(Form)
        self.telephoneNumber.setObjectName(u"telephoneNumber")
        self.telephoneNumber.setGeometry(QRect(220, 140, 361, 22))
        self.username = QLineEdit(Form)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(220, 90, 361, 22))
        self.password = QLineEdit(Form)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(220, 190, 361, 22))
        self.confirmPassword = QLineEdit(Form)
        self.confirmPassword.setObjectName(u"confirmPassword")
        self.confirmPassword.setGeometry(QRect(220, 240, 361, 22))
        self.registerBtn = QPushButton(Form)
        self.registerBtn.setObjectName(u"registerBtn")
        self.registerBtn.setGeometry(QRect(240, 450, 281, 31))
        font2 = QFont()
        font2.setPointSize(14)
        self.registerBtn.setFont(font2)
        self.userImage = QLabel(Form)
        self.userImage.setObjectName(u"userImage")
        self.userImage.setGeometry(QRect(310, 290, 141, 131))
        self.userImage.setFrameShape(QFrame.Box)
        self.userImage.setAlignment(Qt.AlignCenter)
        self.ProfileLabel = QLabel(Form)
        self.ProfileLabel.setObjectName(u"ProfileLabel")
        self.ProfileLabel.setGeometry(QRect(60, 350, 161, 21))
        self.ProfileLabel.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.registerLabel.setText(QCoreApplication.translate("Form", u"User Registeration", None))
        self.nameLabel.setText(QCoreApplication.translate("Form", u"Name", None))
        self.telephoneLabel.setText(QCoreApplication.translate("Form", u"Telephone no.", None))
        self.passconfirmLable.setText(QCoreApplication.translate("Form", u"Confirm Password", None))
        self.nameLabel_2.setText(QCoreApplication.translate("Form", u"Password", None))
        self.registerBtn.setText(QCoreApplication.translate("Form", u"Register", None))
        self.userImage.setText(QCoreApplication.translate("Form", u"**image goes here**", None))
        self.ProfileLabel.setText(QCoreApplication.translate("Form", u"Profile Picture", None))
    # retranslateUi

