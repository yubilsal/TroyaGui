from PyQt5 import QtWidgets
import sys
from UIClass import Ui_MainWindow, Ui_Dialog
import Terminal_Connector
global terminal

class Login(QtWidgets.QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUiD(self)
        self.comboBox.currentIndexChanged.connect(self.selectionchange)
        self.listWidget.itemClicked.connect(self.show_List)
        self.listWidget.setHidden(True)
        self.selected = False
        self.buttonBox.accepted.connect(self.handleconnect)
        self.buttonBox.rejected.connect(self.reject)

    def handleconnect(self):

        if self.selected:
            terminal.get_requested_session(self.session)
            QtWidgets.QMessageBox.information(self, 'Connection', self.session + " connected ")
            self.accept()

        elif self.comboBox.currentText() == "TCP-IP":
            QtWidgets.QMessageBox.information(self, '  TCP-IP  ', 'UNDER CONSTRUCTION')

        else:
            QtWidgets.QMessageBox.critical(self, '  Hata  ', 'Invalid Selection')

    def reject(self):

        sys.exit(Login.exec_())


    def show_List(self):

        for item in self.listWidget.selectedItems():
            self.session = item.text()
            self.selected = True


    def selectionchange(self, i):

        self.listWidget.setHidden(True)
        self.listWidget.clear()

        if   self.comboBox.currentText()== "TERMINAL":

            self.listWidget.setVisible(True)
            print("TERMINAL SELECTED")
            sessionList = []
            global terminal
            terminal = Terminal_Connector.terminalConnect()
            terminal.get_sessions(sessionList)

            for item in range (0,len(sessionList)):
                self.listWidget.addItem(sessionList[item])

        elif self.comboBox.currentText() == "TCP-IP":
            print("TCP-IP SELECTED")


class MainUi(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainUi, self).__init__(parent)
        self.setupUi(self)
        self.textBrowser.setText(terminal.troya_entry("<GETSCREEN>"))
        self.pushButton.clicked.connect(self.sendtroyaentry)
        self.pushButton.setShortcut("Return")
        self.pushButton1.clicked.connect(self.executeMacro)
        self.actionexit.triggered.connect(self.close)

    def sendtroyaentry(self):

        self.lineInput = self.lineEdit.text()
        self.textBrowser.textCursor()
        if self.lineInput != "":
            terminal.troya_entry(self.lineInput)
        else:
            pass
        self.screenOutput = terminal.troya_entry("<GETSCREEN>")
        self.textBrowser.setText(self.screenOutput)
        self.lineEdit.clear()

    def executeMacro(self):

        text = self.comboBox1.currentText()
        imps  = 'from functions import %s' %text
        exc   = "%s.main(terminal)" %text

        try:
            exec(imps)
            exec(exc)
        except:
            pass


if __name__  == "__main__":
    UIClass = QtWidgets.QApplication(sys.argv)
    Login = Login()
    Login.exec_()
    form = MainUi()
    form.show()

    sys.exit(UIClass.exec_())







