import binascii
import socket
import datetime
import sqlite3
import time
import sys


#TROYAYA BAGLANTI SAGLAYAN ENTRYLERI GONDERIP ALAN SCRIPT


def chose_troya_system_and_connect(SYSTEM):
    global CRI
    PORT = 3500
    CRI = "0710D1"

##ALCSTIBM.THY.COM	10.11.75.16
##ALCSPRJT.THY.COM	10.11.75.20
##ALCSTEST.THY.COM	10.11.75.21
##ALCSBATS.THY.COM	10.11.75.24
##ALCSDEVL.THY.COM	10.11.75.25
##ALCSTEMD.THY.COM	10.11.75.26
##ALCSWEBT.THY.COM	10.11.75.27
##ALCSAUTO.THY.COM	10.11.75.30

##CSQ1.THY.COM	        10.11.75.21
##MQL2.THY.COM	        10.11.75.22
##MQDT.THY.COM	        10.11.75.22
##MQPT.THY.COM	        10.11.75.24




    if  SYSTEM == "PROD":
        TCP_IP = "10.11.75.11"
    elif SYSTEM == "TIBM":
        TCP_IP = "ALCSTIBM.THY.COM"
    elif SYSTEM == "PRJT":
        TCP_IP = "ALCSPRJT.THY.COM"
    elif SYSTEM == "TEST":
        TCP_IP = "ALCSTEST.THY.COM"
    elif SYSTEM == "BATS":
        TCP_IP = "ALCSBATS.THY.COM"
    elif SYSTEM == "DEVL":
        TCP_IP = "ALCSDEVL.THY.COM"
    elif SYSTEM == "TEMD":
        TCP_IP = "ALCSTEMD.THY.COM"
    elif SYSTEM == "WEBT":
        TCP_IP = "ALCSWEBT.THY.COM"
    elif SYSTEM == "AUTO":
        TCP_IP = "ALCSAUTO.THY.COM"
    else:
        TCP_IP = "ALCSTEST.THY.COM"







            
    print ("BAGLANMAK ICIN SECILEN SISTEM    :"+SYSTEM)
    print ("BAGLANMAK ICIN SECILEN SISTEM IP :" + TCP_IP + "\n")















    establish_troya_connection(TCP_IP,PORT)


def establish_troya_connection(IP,PORT):


    
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
    print ("TROYA TCPIP BAGLANTISI KURULMAYA CALISILIYOR...")
    print (str(IP) + " PORT : " + str(PORT) + "\n")
    while True:
        try :
            s.connect((IP, PORT))
            print ("TROYA TCPIP BAGLANTISI KURULDU ==> IP: " + str(IP) + " PORT : " + str(PORT) + "\n")
            return True
        except :
            print ("TROYA TCPIP BAGLANTISI KURULAMADI.")
            s.close()
            return False
        else:
            print ("BIRSEYLER TERS GITTI.")
            s.close()
            return False

def release_troya_connection():
    s.close()
    print ("TROYA TCPIP BAGLANTISI KAPATILDI.")
    return True


def prepare_troya_entry (data):
    #GONDERILECEK TROYA ENTRYSINI ISTENILEN FORMATA SOKAR
    Troya_entry = data + "+"
    Troya_entry = Troya_entry.replace('\t','\x15')
    Troya_entry = Troya_entry.replace('\n','\x15')
    encoded_entry =  bytearray((Troya_entry).encode('ascii'))                                      
    send_command = binascii.a2b_hex(binascii.b2a_hex(encoded_entry))                            
    return send_command


def get_raw_troya_response ( Troya_entry ):
    #troyaya datayi gonder ve cevabi al
    
    total_data=[]
    Troya_entry = prepare_troya_entry (Troya_entry)
    CRID= binascii.a2b_hex(CRI)
    
    try :
        #Gonderilecek mesaji hazirla
        s.send(CRID+Troya_entry)
        #print Troya_entry
    except socket.error:
        #Send failed
        print ('Send failed')
        sys.exit()
    #print 'Message send successfully'
    def recv_timeout(the_socket,timeout=0.1):
        BUFFER_SIZE = 81920 * 2
        TCP_TIMEOUT= 10
        the_socket.settimeout(TCP_TIMEOUT)
        #make socket non blocking
        the_socket.setblocking(0)
        #total data partwise in an array
        total_data=[]
        data=''
        diag_count = 0
        recv_timer = datetime.datetime.now()
        while 1:
            try:
                data = the_socket.recv(BUFFER_SIZE)
                #print data
                total_data.append(data)
                #print data
                diag_count = diag_count + 1
                if data.find(">+") != -1:
                #mesaj sonu karakteri varsa looptan cik. yoksa recv ile
                #mesajin devamini almak icin devam et
                    break
                if diag_count > 10:
                    print ("RECV BITIS KARAKTERI GELMIYOR SORUN VAR "+ str(diag_count)) 
            except:
               # print "SOKETTEN DATA ALAMIYOR BIR SORUN VAR "+ str(diag_count)
                recv_timer2 = datetime.datetime.now() - recv_timer
                
                if int(recv_timer2.seconds)> 20 :
                    print ("SOKETTEN DATA ALAMIYOR BIR SORUN VAR "+ str(recv_timer2))                  
                    break
                pass
        return ''.join(total_data)
    troya_response = recv_timeout(s)

    return troya_response

def convert_troya_response (converted_response):        
#Troyadan gelen cevaplar her zaman duzgun degil. Degisik karakterler olabiliyor. Bu nedenle
#Gelen datada asagidaki gibi degisiklikler yapiyoruz.
##
    converted_response = converted_response.replace('\x15', '\n')
    converted_response = converted_response.replace("|\n>+/ ","")
    converted_response = converted_response.replace("\n>+","")
    converted_response = converted_response.replace("/ ","", 1)
    converted_response = converted_response.replace(">+","")
    converted_response = converted_response.replace(">+\n","")
    converted_response = converted_response.replace('%', '\n')
    converted_response = converted_response.replace("/\nTRACE", "TRACE")
    return converted_response


def get_converted_troya_response (data):
    outputdata = convert_troya_response(get_raw_troya_response(data))
    return outputdata




############################################################
############################################################
############################################################
############################################################









