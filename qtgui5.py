import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLabel


class myApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Test Window"
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(300, 200, 500, 300)
        self.w1 = QTextEdit()
        self.label1 = QLabel("Hello World", self)
        self.show()





if __name__ == '__main__':
    test = QApplication(sys.argv)
    hello = myApp()
    sys.exit(test.exec_())

print(hello.title)