def main(terminal, mainGui):
    while True:
        terminal.troya_entry("ot")
        mainGui.textBrowser.setText(terminal.troya_entry("<GETSCREEN>"))