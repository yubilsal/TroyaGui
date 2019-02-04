import win32com.client



class terminalConnect:

    def __init__(self):                                           #INITIALIZE OBJECTS

        self.SYSTEM = "UNKNOWN"                                   #INITIAL STATUS
        self.System = win32com.client.Dispatch("EXTRA.System")    #GET ATTACHMATE EXTRA OBJECT
        self.timeout = 10000
        self.counter = 0

    def active_sessions_count(self):
        try:
            self.session_count = self.System.Sessions.count       #GET SESSION COUNT
            if self.session_count == 0:
                print("NO ACTIVE SESSION.")                       #NO ACTIVE SESSION PRESENT
                return 0
            return self.session_count                             #RETURN SESSION COUNT
        except:
            print("UNABLE TO DETECT SESSIONS.")                   #COULD NOT GET SESSION COUNT
            return 0

    def get_requested_session(self,sessionName):
        global active_session
        self.ses_count = self.active_sessions_count()
        self.index = 1
        print("AVAILABLE SESSIONS: ")
        while self.index <= self.ses_count:
            Current_Session_Name = self.System.Sessions(self.index)
            print(self.System.Sessions(self.index))
            if str(Current_Session_Name) == sessionName:
                #print(str(Current_Session_Name))
                active_session = self.System.Sessions(self.index)
                print("ACTIVE SESSION CHANGED TO ===> " + str(active_session))
                return True
                break
            self.index +=  1
        return False  # SESSION BULUNAMADI

    def get_screenTroya(self):
        self.response = active_session.screen.GetStringEx(0, 0, 20, 80, 120, 0, 0, 0)
        self.response = self.response[:1840]
        self.response = '\n'.join(self.response[i:i + 80] for i in range(0, len(self.response), 80))
        self.response = self.response.rstrip()
        self.data_check = self.response.lstrip()
        return self.data_check

    def get_screenTSO(self):
        self.response = active_session.screen.GetStringEx(0, 0, 20, 80, 120, 0, 0, 0)
        self.response = self.response[:1840]
        self.response = '\n'.join(self.response[i:i + 80] for i in range(0, len(self.response), 80))
        self.response = self.response.rstrip()
        self.data_check = self.response.lstrip()
        return self.data_check

    def troya_entry(self,data):

        if ("<GETSCREEN>" in data):
            pass
        elif ("<CLEAR>" in data):
            active_session.Screen.Sendkeys("<CLEAR>")
        elif ("<ENTER>" in data):
            active_session.Screen.Sendkeys(str(data))
        elif ("<TAB>" in data):
            active_session.Screen.Sendkeys(str(data))
        else:
            active_session.Screen.Sendkeys(str(data) + "<ENTER>")

        while active_session.Screen.OIA.XStatus != 0:                   # TROYA CEVAP SURESINDE BEKLEMESI ICIN EKLENDI.
            self.counter += 1
            if self.counter > self.timeout:
                print("ekrandan data alınamadı")
                pass
        response = self.get_screenTroya()
        return response



if __name__ == "__main__":
    yusuf = terminalConnect()
    yusuf.get_requested_session("session4")
    yusuf.troya_entry("*r")




