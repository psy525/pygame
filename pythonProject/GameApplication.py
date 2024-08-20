from PyQt5.QtWidgets import QApplication
from crud.controller.start import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    start=StartWindow()
    start.show()
    app.exec_()
