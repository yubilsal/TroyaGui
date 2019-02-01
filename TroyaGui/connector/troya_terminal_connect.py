import win32com.client
from time import sleep
from win32com.client import gencache
##gencache.EnsureModule('{7fae9440-c040-11cd-b010-0000c06e6b8a}', 0, 9, 0)
import datetime
global System
global Sessions
global active_session
global SYSTEM


SYSTEM = "UNKNOWN"   # INITIAL TROYA SYSTEM STATUS
System = win32com.client.Dispatch("EXTRA.System")


        
def check_active_sessions():
    #ACIK OLAN ATTACHMATE SESSIONLARININ SAYISINI DONER
    try:
        session_count = System.Sessions.count
        #print ("SESSION COUNT : " + str(session_count))
        if session_count == 0:
            print ("NO ACTIVE SESSION.")
            return 0
        return session_count
    except:
        print ("UNABLE TO DETECT SESSIONS.")
        return 0


def get_screen():
    response = active_session.screen.GetStringEx(0,0,20,80,120,0,0,0)
    response = response [:1840]
    response='\n'.join(response[i:i+80] for i in range(0, len(response), 80))
    response = response.rstrip()
    data_check = response.lstrip()
    return data_check


def get_requested_session(data):
    #SESSION I GIRILEN SESSION A CEVIRIR
    
    data = str(data)
    global active_session
  #  print ("CURRENT ACTIVE SESSION : " + str(active_session))
    session_count = check_active_sessions()
    print ("CURRENT ACTIVE SESSION COUNT :" + str(session_count))
    index = 1
    print ("AVAILABLE SESSIONS: ")
    while index <= session_count:
        Current_Session_Name = System.Sessions(index)
        print (System.Sessions(index))
        if str(Current_Session_Name) == data:
            print(str(Current_Session_Name))
            active_session = System.Sessions(index)
            print ("ACTIVE SESSION CHANGED TO ===> "+str(active_session))
            return True # SESSION BULUNDU VE DEGISTIRILDI 
            break
        index = index + 1
    return False # SESSION BULUNAMADI




def troya_entry(data):

    if ("<GETSCREEN>" in data):
        pass
    elif ("<CLEAR>" in data):
        active_session.Screen.Sendkeys("<CLEAR>")
    elif ("<ENTER>" in data):
        active_session.Screen.Sendkeys(str(data))
    elif ("<TAB>" in data):
        active_session.Screen.Sendkeys(str(data))
    else:
        active_session.Screen.Sendkeys(str(data)+"<ENTER>")
    timeout = 1000
    counter = 0
    while active_session.Screen.OIA.XStatus !=0:                    #TROYA CEVAP SURESINDE BEKLEMESI ICIN EKLENDI.
        counter += 1
        if counter > timeout:
            print("ekrandan data alınamadı")
            pass
    response = get_screen()
    return response

def get_converted_troya_response(var):
    return troya_entry(var)








