from PyQt5 import QtWidgets
import sys
from UIClass import Ui_MainWindow, Ui_Dialog
import Terminal_Connector

global t

class Login(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUiD(self)
        self.comboBox.currentIndexChanged.connect(self.selectionchange)
        self.listWidget.itemClicked.connect(self.show_List)
        self.listWidget.setHidden(True)

    def show_List(self):
        print([item.text() for item in self.listWidget.selectedItems()])

    def selectionchange(self, i):
        self.listWidget.setHidden(True)
        self.listWidget.clear()
        if   self.comboBox.currentText()== "TERMINAL":
            self.listWidget.setVisible(True)
            print("TERMINAL SELECTED")
            sessionList = []
            global t
            t = Terminal_Connector.terminalConnect()
            t.get_sessions(sessionList)
            for item in range (0,len(sessionList)):
                self.listWidget.addItem(sessionList[item])
                print(sessionList[item])
        elif self.comboBox.currentText() == "TCP-IP":
            print("TCP-IP SELECTED")

        else:
            print("UNKNOWN CONNECTION TYPE")


class MainUi(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainUi, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.sendtroyaentry)
        self.pushButton.setShortcut("Return")
#        self.t = Terminal_Connector.terminalConnect()
        t.get_requested_session("session1")

    def sendtroyaentry(self):
        self.lineInput = self.lineEdit.text()
        self.textBrowser.textCursor()
        if self.lineInput != "":
            self.t.troya_entry(self.lineInput)
        else:
            pass
        self.screenOutput = self.t.troya_entry("<GETSCREEN>")
        self.textBrowser.setText(self.screenOutput)
        self.lineEdit.clear()


if __name__  == "__main__":

    UIClass = QtWidgets.QApplication(sys.argv)
    Login = Login()
    Login.show()
    Login.exec_()
    form = MainUi()
    form.show()
    sys.exit(UIClass.exec_())








