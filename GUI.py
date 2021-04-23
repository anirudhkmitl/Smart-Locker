import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from loginScreenRFIDwelcomeUI import Ui_loginScreenRFID

class WelcomeUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)

        self.ui = Ui_loginScreenRFID()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = WelcomeUI()
    w.show()
    sys.exit(app.exec_())