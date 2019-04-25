# coding:utf-8
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

win = QWidget()
win.resize(760, 540)
win.move(0, 0)
layout=QGridLayout(win)

b=QLabel(win)
b.setPixmap(QPixmap("bg.jpg"))
b.setGeometry(0,0,820,640)

def positionSet():
    b1=QLabel(win)
    b1.setPixmap(QPixmap("new\\pic ("+str(1)+").jpg"))

    b2=QLabel(win)
    b2.setPixmap(QPixmap("new\\pic ("+str(2)+").jpg"))

    b3=QLabel(win)
    b3.setPixmap(QPixmap("new\\pic ("+str(3)+").jpg"))

    b4=QLabel(win)
    b4.setPixmap(QPixmap("new\\pic ("+str(4)+").jpg"))

    b5=QLabel(win)
    b5.setPixmap(QPixmap("new\\pic ("+str(5)+").jpg"))

    b6=QLabel(win)
    b6.setPixmap(QPixmap("new\\pic ("+str(6)+").jpg"))

    b7=QLabel(win)
    b7.setPixmap(QPixmap("new\\pic ("+str(7)+").jpg"))

    b8=QLabel(win)
    b8.setPixmap(QPixmap("new\\pic ("+str(8)+").jpg"))

    b9=QLabel(win)
    b9.setPixmap(QPixmap("new\\pic ("+str(9)+").jpg"))

    b10=QLabel(win)
    b10.setPixmap(QPixmap("new\\pic ("+str(10)+").jpg"))

    b11=QLabel(win)
    b11.setPixmap(QPixmap("new\\pic ("+str(11)+").jpg"))


    b12=QLabel(win)
    b12.setPixmap(QPixmap("new\\pic ("+str(12)+").jpg"))

    b13=QLabel(win)
    b13.setPixmap(QPixmap("new\\pic ("+str(13)+").jpg"))

    b14=QLabel(win)
    b14.setPixmap(QPixmap("new\\pic ("+str(14)+").jpg"))

    b15=QLabel(win)
    b15.setPixmap(QPixmap("new\\pic ("+str(15)+").jpg"))

    b16=QLabel(win)
    b16.setPixmap(QPixmap("new\\pic ("+str(16)+").jpg"))

    b17=QLabel(win)
    b17.setPixmap(QPixmap("new\\pic ("+str(17)+").jpg"))

    b18=QLabel(win)
    b18.setPixmap(QPixmap("new\\pic ("+str(18)+").jpg"))

    b19=QLabel(win)
    b19.setPixmap(QPixmap("new\\pic ("+str(19)+").jpg"))

    b20=QLabel(win)
    b20.setPixmap(QPixmap("new\\pic ("+str(20)+").jpg"))





    layout.addWidget(b1, 0, 3)
    layout.addWidget(b2, 0, 7)
    layout.addWidget(b3, 1, 2)
    layout.addWidget(b4, 1, 4)
    layout.addWidget(b5, 1, 6)
    layout.addWidget(b6, 1, 8)
    layout.addWidget(b7, 2, 1)
    layout.addWidget(b8, 2, 5)
    layout.addWidget(b9, 2, 9)
    layout.addWidget(b10, 3, 0)
    layout.addWidget(b11, 3, 10)
    layout.addWidget(b12, 4, 1)
    layout.addWidget(b13, 4, 9)
    layout.addWidget(b14, 5, 2)
    layout.addWidget(b15, 5, 8)
    layout.addWidget(b16, 6, 3)
    layout.addWidget(b17, 6, 7)
    layout.addWidget(b18, 7, 4)
    layout.addWidget(b19, 7, 6)
    layout.addWidget(b20, 8, 5)




positionSet()
win.setWindowTitle('GUI')
win.show()

sys.exit(app.exec_())