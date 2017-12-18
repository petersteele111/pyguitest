import sys
from PyQt5 import QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)
    window1 = QtWidgets.QWidget()
    window1.setWindowTitle("Gui Test 3")
    window1.show()
    sys.exit(app.exec_())

window()