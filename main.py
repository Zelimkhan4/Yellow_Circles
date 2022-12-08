from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt, QPoint
from random import randint
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.balls = [] # (x, y, r)
        self.btn.clicked.connect(self.process)

    def process(self):
        r = randint(0, 100)
        x, y = randint(r, self.width() - r), randint(r, self.height() - r)
        self.balls.append((x, y, r))
        self.update()

    def paintEvent(self, a0):
        painter = QPainter(self)
        painter.setBrush(QBrush(Qt.yellow))
        for ball in self.balls: # ball - (pos, r)
            x, y, r = ball
            painter.drawEllipse(QPoint(x, y), r, r)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())