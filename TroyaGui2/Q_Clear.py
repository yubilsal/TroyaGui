from PyQt5 import QtGui

def main(terminal, mainGui):
    if len(mainGui.lineEdit.text()) == 5:
        q_city = mainGui.lineEdit.text()[0:3]
        q_num = mainGui.lineEdit.text()[3:5]
        mainGui.textBrowser.setText(terminal.troya_entry("<CLEAR>"))
        mainGui.textBrowser.setText(terminal.troya_entry("qx"))
        mainGui.textBrowser.setText(terminal.troya_entry("i"))
        mainGui.textBrowser.setText(terminal.troya_entry("qcp/" + q_city))
        screen_output = terminal.troya_entry("<GETSCREEN>")
        result = screen_output.find("Q" + q_num)
        if result != -1:
            try:
                q_count = int(screen_output[result + 3:result + 9])
            except:
                q_count = 0
                mainGui.textBrowser.setText("INVALID INPUT")
            if q_num == "Q83" and q_city == "QSC":
                result = screen_output.find('Q85')
                if result != -1:
                    count_q85 = int(screen_output[result + 3:result + 9])
                    f = open("Q85log.txt", "w+")
                    mainGui.textBrowser.setText(terminal.troya_entry("q/qsc/85"))
                    for x in range(count_q85):
                        screen_output = terminal.troya_entry("<GETSCREEN>")
                        f.write(screen_output)
                        f.write("\n***********************************************************\n\n\n")
                        mainGui.textBrowser.setText(terminal.troya_entry("i"))
                    mainGui.textBrowser.setText(terminal.troya_entry("qx"))
                    mainGui.textBrowser.setText(terminal.troya_entry("i"))
                else:
                    count_q85 = 0
            mainGui.textBrowser.setText(terminal.troya_entry("q/" + q_city + "/" + q_num))
            for x in range(q_count):
                mainGui.textBrowser.setText(terminal.troya_entry("qr"))
                QtGui.QGuiApplication.processEvents()
                screen_output = terminal.troya_entry("<GETSCREEN>")
                if "please enter grps and grpf for group pnrs" in screen_output.lower():
                    mainGui.textBrowser.setText(terminal.troya_entry("i"))
            mainGui.textBrowser.setText(terminal.troya_entry("qx"))
            mainGui.textBrowser.setText(terminal.troya_entry("i"))
            mainGui.textBrowser.setText(terminal.troya_entry("qcp/" + q_city))
            screen_output = terminal.troya_entry("<GETSCREEN>")
            if q_num == "83":
                result = screen_output.find('Q85')
                if result != -1 and count_q85 != int(screen_output[result + 3:result + 9]):
                    mainGui.textBrowser.setText("Check Q85log.txt")
    else:
        mainGui.textBrowser.setText("INVALID INPUT")