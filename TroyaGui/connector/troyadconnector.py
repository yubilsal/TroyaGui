#!/usr/bin/env python2
import sys
import datetime
from connector import troya_tcp_connect,troya_terminal_connect

global LSYSTEM
LSYSTEM = ""

global connection_type




def save_to_log_file(data,connection_type,direction):


    current_time =str(datetime.datetime.now())
    current_time = current_time.replace(":","-")
    current_time = str(current_time.replace(".","-"))

    #mylogfile = open("io/logs/"+current_time[0:16]+"-"+connection_type + "-" + "LOG.txt", 'a')

    #if direction == "TO":
     #   arrow = ">>>>"
    #elif  direction == "FROM":
     #   arrow = "<<<<"

    #logline = arrow + " " + str(current_time) + " " + LSYSTEM + " " + arrow + " " + "\n"


    #mylogfile.write(logline)

    #mylogfile.write(str(data)+"\n")
    #mylogfile.close()

    #print data




def get_troya_response(data):


    if connection_type == "TCPIP":
        response = troya_tcp_connect.get_converted_troya_response(data)
    elif connection_type == "TERMINAL":
        response = troya_terminal_connect.get_converted_troya_response(data)

    #save_to_log_file(data,connection_type,"TO")
    #save_to_log_file(response,connection_type,"FROM")

    return response


def detect_connection_type():
    global connection_type

    while True:
            connection_type = input("BAGLANTI YONTEMI TCPIP/TERMINAL >>> ")
            connection_type = connection_type.upper()
            if connection_type == "TCPIP":
                SYSTEM = input("BAGLANILMAK ISTENILEN SISTEMI GIRIN >>> ")
                troya_tcp_connect.chose_troya_system_and_connect(SYSTEM)
                break

            elif connection_type == "TERMINAL":
                Session_connection_success = False
                while Session_connection_success == False:
                    SESSION_NAME = input("BAGLANMAK ISTEDIGINIZ SESSION ISMINI GIRIN >>> ")
                    SESSION_NAME = SESSION_NAME.lower()
                    Session_connection_success = troya_terminal_connect.get_requested_session(SESSION_NAME)
                break
            else:
                print("HATALI GIRIS YAPTINIZ. LUTFEN DOGRU BIR BAGLANTI YONTEMI GIRIN.")

def validate_connected_system():
    BSIA ="BSIA8891YY/PR"
    while True:
        system_name = get_troya_response("OZSYSTEM")
        if "SINE IN" in system_name:
            get_troya_response(BSIA)
            system_name = get_troya_response("OZSYSTEM")
        if "E9E30000" in system_name:  # ZT TEST SYSTEM
            LSYSTEM = "TEST"
            print ("YOU ARE WORKING ON TEST SYSTEM")
            break
        elif "E9D30000" in system_name: #ZL LIVE SYSTEM
            LSYSTEM = "PRODUCTION"
            print("! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! \n")
            print("! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! \n")
            print("! ! ! ! ! ! ! ! ! ! ! ! ! W A R N I N G ! ! ! ! ! ! ! ! ! ! ! ! ! \n")
            print("! ! ! ! ! ! ! ! YOU ARE WORKING ON LIVE SYSTEM! ! ! ! ! ! ! ! ! ! \n")
            print("! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! \n")
            print("! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! \n")
            CONDITION =input("TYPE CONTINUE TO CONTINUE>>> ")
            if CONDITION == "CONTINUE":
                break


##
##
detect_connection_type()
##validate_connected_system()
##
