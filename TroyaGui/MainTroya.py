from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys
#from connector import troya_connector
import UIClass
import Terminal_Connector



class MainUi(QtWidgets.QMainWindow, UIClass.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainUi, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.sendCommand)
        self.pushButton.setShortcut("Return")
        self.t = Terminal_Connector.terminalConnect()
        self.t.get_requested_session("session3")

    def sendCommand(self):
        self.lineInput = self.lineEdit.text()
        self.textBrowser.textCursor()
        if self.lineInput != "":
            self.t.troya_entry(self.lineInput)
        else:
            pass
        self.screenOutput = self.t.troya_entry("<GETSCREEN>")
        self.textBrowser.setText(self.screenOutput)
        self.lineEdit.clear()

if __name__ == "__main__":
    UIClass = QtWidgets.QApplication(sys.argv)
    form = MainUi()
    form.show()
    sys.exit(UIClass.exec_())








