def main(t, mainGui):
    f = open("TraceLOG.txt", "w+")
    screen_output = t.get_screen_troya2()
    f.write(screen_output)
    f.write("\n***************************************\n")
    t.troya_entry("<CLEAR>")
    index = 0
    while "TRACE -- ENTER MESSAGE TO TRACE" not in t.troya_entry("<GETSCREEN>"):
        t.troya_entry("<ENTER>")
        screen_output = t.get_screen_troya2()
        index = index + 1
        if index == 21:
            f.write(screen_output)
            f.write("\n")
            index = 0
            break
    while "TRACE -- ENTER MESSAGE TO TRACE" not in t.troya_entry("<GETSCREEN>"):
        t.troya_entry("<ENTER>")
        screen_output = t.get_screen_troya2()
        index = index + 1
        if index == 22:
            f.write(screen_output)
            f.write("\n")
            index = 0
    screen_output = t.get_screen_troya2()
    f.write(screen_output)
