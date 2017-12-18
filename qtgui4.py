import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class app1(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQT 5 Class based GUI"
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = app1()
    sys.exit(app.exec_())
