import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from registrationScreen import Ui_registerForm

class registrationFormUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)

        self.ui = Ui_registerForm()
        self.ui.setupUi(self)

        self.ui.registerBtn.clicked.connect(self.register)
        self.ui.pictureLabel.clicked.connect(self.openpicture)

    def register(self):
        pass

    def openpicture(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = registrationFormUI()
    w.show()
    sys.exit(app.exec_())