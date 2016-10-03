import sys
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class TitleBar(QtWidgets.QDialog):
    def __init__(self, parent=None, windowTitle='Window Title'):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        css = """
        QWidget{
            Background: #3C424E;
            color:white;
            font:15px bold;
            font-weight:bold;
            border-radius: 1px;
            height: 11px;
        }
        QDialog{
            Background-image:url('img/titlebar bg.png');
            font-size:15px;
            color: black;

        }
        QToolButton{
            font-size:11px;
        }
        QToolButton:hover{
            Background: #FF00FF;
            font-size:11px;
        }
        """
        self.setAutoFillBackground(True)
        self.setBackgroundRole(QtGui.QPalette.Highlight)
        self.setStyleSheet(css)
        self.minimize = QtWidgets.QToolButton(self)
        self.minimize.setIcon(QtGui.QIcon('img/min.png'))
        self.minimize.setStyleSheet("""
        QToolButton{
            Background:#AAAA20;
            font-size:11px;
        }""")
        self.maximize = QtWidgets.QToolButton(self)
        self.maximize.setIcon(QtGui.QIcon('img/max.png'))
        self.maximize.setStyleSheet("""
        QToolButton{
            Background:#20AA20;
            font-size:11px;
        }""")
        close = QtWidgets.QToolButton(self)
        close.setIcon(QtGui.QIcon('img/close.png'))
        close.setStyleSheet("""
        QToolButton{
            Background:#AA2020;
            font-size:11px;
        }""")
        self.minimize.setMinimumHeight(10)
        close.setMinimumHeight(10)
        self.maximize.setMinimumHeight(10)
        label = QtWidgets.QLabel(self)
        label.setText(windowTitle)
        self.setWindowTitle(windowTitle)
        hbox = QtWidgets.QHBoxLayout(self)
        hbox.addWidget(label)
        hbox.addWidget(self.minimize)
        hbox.addWidget(self.maximize)
        hbox.addWidget(close)
        hbox.insertStretch(1, 500)
        hbox.setSpacing(3)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                           QtWidgets.QSizePolicy.Fixed)
        self.maxNormal = False
        close.clicked.connect(self.close)
        self.minimize.clicked.connect(self.showSmall)
        self.maximize.clicked.connect(self.showMaxRestore)

    def showSmall(self):
        box.showMinimized()

    def showMaxRestore(self):
        if(self.maxNormal):
            box.showNormal()
            self.maxNormal = False
            self.maximize.setIcon(QtGui.QIcon('img/max.png'))
        else:
            box.showMaximized()
            self.maxNormal = True
            self.maximize.setIcon(QtGui.QIcon('img/max2.png'))

    def close(self):
        box.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            box.moving = True
            box.offset = event.pos()

    def mouseMoveEvent(self, event):
        if box.moving:
            box.move(event.globalPos()-box.offset)
