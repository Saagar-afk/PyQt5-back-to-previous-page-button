"""This file b.py is completely generated by designer"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window2(object):
    def setupUi(self, window2):
        window2.setObjectName("window2")
        window2.resize(268, 203)
        self.centralwidget = QtWidgets.QWidget(window2)
        self.centralwidget.setObjectName("centralwidget")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(80, 60, 101, 41))
        self.back.setObjectName("back")
        window2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 268, 21))
        self.menubar.setObjectName("menubar")
        window2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window2)
        self.statusbar.setObjectName("statusbar")
        window2.setStatusBar(self.statusbar)

        self.retranslateUi(window2)
        QtCore.QMetaObject.connectSlotsByName(window2)

    def retranslateUi(self, window2):
        _translate = QtCore.QCoreApplication.translate
        window2.setWindowTitle(_translate("window2", "MainWindow"))
        self.back.setText(_translate("window2", "Back"))


#Edited