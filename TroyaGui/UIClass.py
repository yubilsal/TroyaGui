import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUiD(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 220)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 100, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(50, 50, 78, 20))
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(190, 10, 191, 121))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Connection"))
        self.comboBox.setItemText(0, _translate("Dialog", ""))
        self.comboBox.setItemText(1, _translate("Dialog", "TERMINAL"))
        self.comboBox.setItemText(2, _translate("Dialog", "TCP-IP"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1009, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.comboBox1 = QtWidgets.QComboBox(MainWindow)
        self.comboBox1.setGeometry(QtCore.QRect(30, 120, 75, 23))
        # self.comboBox1.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox1.setObjectName("comboBox")
        self.comboBox1.addItem("")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(30, 143, 75, 23))
        self.pushButton1.setObjectName("pushButton1")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setStyleSheet("QTextBrowser#textBrowser {background-color: #D1EFFF; color: #000989; font-size: 14pt; font-weight: 480}")
        self.textBrowser.setGeometry(QtCore.QRect(190, 10, 801, 541))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1009, 22))
        self.menubar.setObjectName("menubar")
        self.menuMENU = QtWidgets.QMenu(self.menubar)
        self.menuMENU.setObjectName("menuMENU")
        MainWindow.setMenuBar(self.menubar)
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.menuMENU.addSeparator()
        self.menuMENU.addAction(self.actionexit)
        self.menubar.addAction(self.menuMENU.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "SEND"))
        self.pushButton1.setText(_translate("MainWindow", "EXC"))
        self.menuMENU.setTitle(_translate("MainWindow", "MENU"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        functionList = os.listdir("functions")
        for i in range(0,len(functionList)):
            if functionList[i][-3:] == ".py":
                self.comboBox1.addItem(_translate("MainWindow", functionList[i][0:-3]))
