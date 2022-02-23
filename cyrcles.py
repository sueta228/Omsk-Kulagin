from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from PyQt5 import uic
from random import randint
from PIL import Image


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        uic.loadUi('untitled.ui', self)  # Загружаем дизайн
        self.create_btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()


    def draw_flag(self, qp):
        y = 120
        x = 120
        qp.setBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
        qp.drawEllipse(140, y, 120, randint(100, 200))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
