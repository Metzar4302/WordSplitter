# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(419, 334)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 401, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.inputTextField = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.inputTextField.setMaximumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.inputTextField.setFont(font)
        self.inputTextField.setObjectName("inputTextField")
        self.verticalLayout.addWidget(self.inputTextField)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitBtn.sizePolicy().hasHeightForWidth())
        self.splitBtn.setSizePolicy(sizePolicy)
        self.splitBtn.setMaximumSize(QtCore.QSize(100, 25))
        self.splitBtn.setBaseSize(QtCore.QSize(100, 25))
        self.splitBtn.setObjectName("splitBtn")
        self.horizontalLayout.addWidget(self.splitBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.mosStyleLable = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        self.mosStyleLable.setFont(font)
        self.mosStyleLable.setObjectName("mosStyleLable")
        self.verticalLayout.addWidget(self.mosStyleLable)
        self.petStyleLabe = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        self.petStyleLabe.setFont(font)
        self.petStyleLabe.setObjectName("petStyleLabe")
        self.verticalLayout.addWidget(self.petStyleLabe)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.splitBtn.setText(_translate("MainWindow", "Split"))
        self.mosStyleLable.setText(_translate("MainWindow", "TextLabel"))
        self.petStyleLabe.setText(_translate("MainWindow", "TextLabel"))

