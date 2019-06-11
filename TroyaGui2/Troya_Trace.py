import os
import datetime
from PyQt5 import QtGui
import graphviz as gv

utility_programs = ["WGS1", "WGS2", "NGRA", "FMSG"]


def create_flow_diagram(flow_list, file_name):
    var = flow_list

    print("GRAFIK OLUSTURULUYOR")
    g2 = gv.Digraph(format='pdf')
    utility_no = 1
    utility_change = False
    entrc_stack = []
    for i in range(len(var)):
        data = var[i]
        from_text = data[0]
        to_text = data[1]
        macro = data[2]
        step = str(data[3])
        occurance = data[4]

        occurance_num = occurance
        if occurance == 1:
            occurance = ""
        else:
            occurance = str(occurance)
            occurance = "\n(x" + occurance + " TIMES)"
        if (to_text in utility_programs) and (macro == "ENTRC") and (utility_change == False):
            utility_change = True
            utility_no += 1
            new_utility_program_name = to_text + "\nUP#" + str(utility_no)
            original_program_name = to_text

        if (utility_change == True) and (to_text in utility_programs):
            if original_program_name == to_text:
                to_text = new_utility_program_name
            else:
                print("utility programs overlap")

        if (utility_change == True) and (from_text in utility_programs):
            if original_program_name == from_text:
                from_text = new_utility_program_name
                if (macro == "BACKC"):
                    utility_change = False
            else:
                print("utility programs overlap")

        label_text = macro

        if "CRE" in label_text:
            g2.attr('node', shape='rectangle', color='red')
        else:
            g2.attr('node', shape='circle', color='black')

        if label_text == "BACKC":
            g2.attr('edge', color='blue')
        elif label_text == "ENTRC":
            g2.attr('edge', color='red')
        elif label_text == "ENTDC":
            g2.attr('edge', color='orange')
        elif label_text == "ENTNC":
            g2.attr('edge', color='green')
        else:
            g2.attr('edge', color='black')

        label_text = label_text + "\n" + "STEP#:" + step + occurance  # str(i)

        ##        g2.edge_attr.update(penwidth='13')
        # print occurance_num
        pw = float(occurance_num / 100.00) * 5.00 + 1.00

        if pw > 5:
            pw = 5
        print(pw)
        ##        g2.edge_attr.update(penwidth='%f' %pw)

        if len(data) > 2:
            g2.edge(from_text, to_text, label_text, penwidth='%f' % pw)
        else:
            g2.edge(from_text, to_text)

    g2.attr("graph", label="\n\n\n COPYRIGHT(C) 2019 TURKISH AIRLINES INC.\nALL RIGHTS RESERVED.\n\n\n", fontsize='25')

    try:
        file_name = file_name[0:len(file_name) - 4]
        g2.render("TRACE_FILES/" + file_name + "/" + file_name + "-FLOW", view=True)
    except:
        print("GRAFIK OLUSTURULMAYA CALISILIRKEN BIR HATA ILE KARSILASILDI")


class trace_flow:
    flow_count = 0

    def __init__(self, from_program, to_program, macro_name):
        trace_flow.flow_count += 1
        self.step_count = trace_flow.flow_count
        self.from_program = from_program
        self.to_program = to_program
        self.macro_name = macro_name

        self.matchstring = self.from_program + self.to_program + self.macro_name
        self.occurance = 1

    def increment_occurance(self):
        self.occurance = self.occurance + 1


def find_trace_files():
    trace_file_list = []
    path = os.getcwd()
    step_counter = 0

    for file in os.listdir(path):
        file_name = str(file)
        if file_name.startswith("TRACE LOG") and file_name.endswith(".txt"):
            output_file_name = file_name
            output_file_name = output_file_name.replace(".txt", "")

            file_path = path + "\\" + file_name
            trace_file_list.append((file_path, output_file_name))
    return trace_file_list


def process_trace_file(trace_file_path, trace_file_name):
    macro_list = ["ENTRC", "BACKC", "ENTDC", "ENTNC", "CREDC", "CREMC", "CREXC", "CREEC", "CRETC"]

    entrc_stack = []
    flow_list = []

    print(trace_file_path)
    print(trace_file_name)
    trace_folder = trace_file_path[0:len(trace_file_path) - 4]
    trace_file = open("TRACE_FILES/" + trace_folder + '\\' + trace_file_path, "r")
    trace_file_contents = trace_file.read()
    trace_file_lines = trace_file_contents.split("\n")
    for i in range(len(trace_file_lines)):
        trace_file_line = trace_file_lines[i]
        if trace_file_line.startswith("TRACE"):

            from_program = trace_file_line[9:9 + 4]
            macro = trace_file_line[19:19 + 5]
            to_program = trace_file_line[25:25 + 4]

            if macro in macro_list:
                ##                print trace_file_line
                if macro == "ENTRC":
                    entrc_stack.append(from_program)
                elif macro == "BACKC":
                    try:
                        to_program = entrc_stack.pop()
                    except:
                        print("BACK BROKEN CHAIN")
                elif macro == "ENTDC":
                    entrc_stack = []

                ##                print from_program+" "+macro +" "+to_program

                current_flow = trace_flow(from_program, to_program, macro)

                flow_match = False

                for n in range(len(flow_list)):

                    flow_list[n].matchstring
                    if current_flow.matchstring == flow_list[n].matchstring:
                        flow_list[n].increment_occurance()
                        flow_match = True
                if flow_match == False:
                    flow_list.append(current_flow)

    ##                print current_flow.step_count

    output_list = []
    for i in range(len(flow_list)):
        flow_list_inst = flow_list[i]
        output_list.append((flow_list_inst.from_program, flow_list_inst.to_program, flow_list_inst.macro_name,
                            flow_list_inst.step_count, flow_list_inst.occurance))

    return output_list

def main(t,mainGui):
    fil_name = datetime.datetime.now()
    fil_name = str(fil_name)
    fil_name = fil_name.replace(":", "-")
    fil_name = fil_name[0:22]
    fil_name = "TRACE LOG - " + fil_name + ".txt"
    global x
    x = fil_name
    new2 = x[0:len(x) - 4]
    newpath = "TRACE_FILES/" + new2
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    trace_output = open("TRACE_FILES/" + new2 + "/" + fil_name, 'w')
    trace_output.write("dsasd")
    t.troya_entry2("<CLEAR>")
    while True:
        trace_result = t.troya_entry2("<ENTER>")
        mainGui.textBrowser.setText(trace_result)
        QtGui.QGuiApplication.processEvents()
        trace_output.write(trace_result + "\n")
        if "TRACE -- ENTER MESSAGE TO TRACE" in trace_result:
            break
        elif "INVALID ACTION CODE" in trace_result:
            break
        t.troya_entry2("<CLEAR>")
    trace_output.write("END")
    trace_output.close()
    step_counter = 0
    process_list = process_trace_file(x, "trace log")
    create_flow_diagram(process_list, x)
    y = x[0:len(x) - 4] + "-FLOW"
    z = x[0:len(x) - 4]
    print(y)
    os.remove("TRACE_FILES/" + z + "\\" + y)