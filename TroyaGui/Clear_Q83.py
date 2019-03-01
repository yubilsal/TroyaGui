def main(t):
    t.troya_entry("<CLEAR>")
    t.troya_entry("qx")
    t.troya_entry("i")
    t.troya_entry("qcp/qsc")
    screen_output = t.troya_entry("<GETSCREEN>")
    result = screen_output.find('Q83')
    if result != -1:
        count_q83 = int(screen_output[result + 3:result + 9])
        result = screen_output.find('Q85')
        if result != -1:
            count_q85 = int(screen_output[result + 3:result + 9])
            f = open("Q85log.txt", "w+")
            t.troya_entry("q/qsc/85")
            for x in range(count_q85):
                screen_output = t.troya_entry("<GETSCREEN>")
                f.write(screen_output)
                f.write("\n***********************************************************\n\n\n")
                t.troya_entry("i")
            t.troya_entry("qx")
            t.troya_entry("i")
        else:
            count_q85 = 0
        t.troya_entry("q/qsc/83")
        for x in range(count_q83):
            t.troya_entry("qr")
            screen_output = t.troya_entry("<GETSCREEN>")
            if "please enter grps and grpf for group pnrs" in screen_output.lower():
                t.troya_entry("i")
        t.troya_entry("qx")
        t.troya_entry("i")
        t.troya_entry("qcp/qsc")
        screen_output = t.troya_entry("<GETSCREEN>")
        result = screen_output.find('Q85')
        if count_q85 != int(screen_output[result + 3:result + 9]):
            print("Check Q85log.txt")
