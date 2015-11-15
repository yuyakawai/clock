# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from time import strftime


class MainWindow(QtGui.QWidget):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.init_ui()
 
    def init_ui(self):
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)
 
        self.label = QtGui.QLabel("")
        font = QtGui.QFont()
        font.setPointSize(80)
        self.label.setFont(font)

        self.hbox = QtGui.QHBoxLayout()
        self.hbox.addWidget(self.label)
        self.setLayout(self.hbox)

        self.setWindowTitle("Clock")

        self.setFixedSize(260, 150);

        self.update()
        self.show()
 
    def update(self):
        self.label.setText(strftime("%H"+":"+"%M"))

