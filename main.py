import sys
import time

import random
from PyQt5.QtWidgets import QPushButton
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtWidgets


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(565, 541))
        self.setWindowTitle("Random circle color")

        pybutton = QPushButton('Тык', self)
        pybutton.clicked.connect(self.start)
        pybutton.resize(75, 23)
        pybutton.move(230, 230)
        self.ok = False

    def start(self):
        self.ok = True

    def paintEvent(self, event):
        if self.ok:
            self.qp = QPainter(self)
            self.qp.begin(self)
            self.draw()
            self.qp.end()
            self.update()

    def draw(self):
        # for i in range(random.randint(10, 50)):
        color_random = ['red', 'green', 'blue', 'black', 'yellow', 'pink']
        self.qp.setPen(QtGui.QPen(QtGui.QColor(random.choice(color_random))))
        x = random.randint(100, 500)
        y = random.randint(100, 500)
        self.qp.drawEllipse(x, x, y, y)
        time.sleep(1)

    def circle(self):
        self.draw = True


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
