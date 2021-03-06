import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUiD(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 200)
        Dialog.setMaximumSize(QtCore.QSize(500, 250))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setMaximumSize(QtCore.QSize(155, 155))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setText("Available sessions")
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_5.addWidget(self.listWidget)
        spacerItem2 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 1, 1, 1)
        # self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        # self.buttonBox.setGeometry(QtCore.QRect(0, 100, 171, 32))
        # self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        # self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        # self.buttonBox.setObjectName("buttonBox")
        # self.comboBox = QtWidgets.QComboBox(Dialog)
        # self.comboBox.setGeometry(QtCore.QRect(50, 50, 78, 20))
        # self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        # self.comboBox.setObjectName("comboBox")
        # self.comboBox.addItem("")
        # self.comboBox.addItem("")
        # self.comboBox.addItem("")
        # self.label = QtWidgets.QLabel(Dialog)
        # self.label.setText("Available sessions")
        # self.label.move(200, 10)
        # self.listWidget = QtWidgets.QListWidget(Dialog)
        # self.listWidget.setGeometry(QtCore.QRect(190, 30, 191, 121))
        # self.listWidget.setObjectName("listWidget")

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
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setStyleSheet("QTextBrowser#textBrowser {background-color: #D1EFFF; color: #000989; font-size: 14pt; font-weight: 480}")
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setText("Macros")
        self.verticalLayout_2.addWidget(self.label)
        self.comboBox1 = QtWidgets.QComboBox(MainWindow)
        self.comboBox1.setObjectName("comboBox")
        self.comboBox1.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox1)
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setObjectName("pushButton2")
        self.verticalLayout_2.addWidget(self.pushButton1)
        self.verticalLayout_2.addWidget(self.pushButton2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
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
        self.pushButton1.setText(_translate("MainWindow", "EXCECUTE"))
        self.pushButton2.setText(_translate("MainWindow", "ABORT"))
        self.menuMENU.setTitle(_translate("MainWindow", "MENU"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        functionList = ["Troya_Trace","Q_Clear","OT"]
        for i in range(0,len(functionList)):
            self.comboBox1.addItem(_translate("MainWindow", functionList[i]))
