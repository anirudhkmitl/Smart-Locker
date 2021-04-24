import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from loginScreenRFIDwelcomeUI import Ui_loginScreenRFID
from userDetailsPassword import Ui_userInfoUI

##The class below is for the UI where user is asked to scan the RFID tag on the RFID scanner.
class WelcomeUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)

        self.ui = Ui_loginScreenRFID()
        self.ui.setupUi(self)



##The class below is for the UI of the user info and passcode.
##Image of the user is shown and user is asked to enter their private PIN number.
class UserDetails(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)

        self.ui = Ui_userInfoUI()
        self.ui.setupUi(self)

        self._password = ""
        self.ui.btnOne.clicked.connect(self.one)
        self.ui.btnTwo.clicked.connect(self.two)
        self.ui.btnThree.clicked.connect(self.three)
        self.ui.btnFour.clicked.connect(self.four)
        self.ui.btnFive.clicked.connect(self.five)
        self.ui.btnSix.clicked.connect(self.six)
        self.ui.btnSeven.clicked.connect(self.seven)
        self.ui.btnEight.clicked.connect(self.eight)
        self.ui.btnNine.clicked.connect(self.nine)
        self.ui.btnClear.clicked.connect(self.clear)
        self.ui.btnZero.clicked.connect(self.zero)
        self.ui.btnBackspace.clicked.connect(self.backspace)


    def one(self):
        self._password += "1"
        self.ui.passwordInput.setText(self._password)

    def two(self):
        self._password += "2"
        self.ui.passwordInput.setText(self._password)

    def three(self):
        self._password += "3"
        self.ui.passwordInput.setText(self._password)

    def four(self):
        self._password += "4"
        self.ui.passwordInput.setText(self._password)

    def five(self):
        self._password += "5"
        self.ui.passwordInput.setText(self._password)

    def six(self):
        self._password += "6"
        self.ui.passwordInput.setText(self._password)

    def seven(self):
        self._password += "7"
        self.ui.passwordInput.setText(self._password)

    def eight(self):
        self._password += "8"
        self.ui.passwordInput.setText(self._password)

    def nine(self):
        self._password += "9"
        self.ui.passwordInput.setText(self._password)

    def clear(self):
        self._password = ""
        self.ui.passwordInput.setText(self._password)

    def zero(self):
        self._password += "0"
        self.ui.passwordInput.setText(self._password)

    def backspace(self):
        self._password = self._password[:-1]
        self.ui.passwordInput.setText(self._password)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = UserDetails()
    w.show()
    sys.exit(app.exec_())