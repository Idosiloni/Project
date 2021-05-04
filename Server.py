from tkinter import *
from socket import *
from threading import *
from tkinter.scrolledtext import ScrolledText
from time import sleep
import sqlite3
from queue import Queue
flag = 1
conn_q = Queue()
gui_q  = Queue()

class handle_client(Thread):  
    print("Hello")
    clients =[] #class variable
    lock = Lock()
    
    
    conn = sqlite3.connect('DataBase1.db')
    c=conn.cursor()
    
    
    
    def __init__(self, client_socket):
        Thread.__init__(self)
        self.client_socket = client_socket
        self.login = "False"
        self.user = None
        handle_client.clients.append( client_socket )

    def parse_client_message(self,client_message):
        parts = client_message.split(",")
        message_type = parts[0]
        if message_type == "signUp":
            try:
                c.execute("INSERT INTO Users(Username,Password,Job) VALUES (?, ?, ?)" ,(parts[1] ,parts[2] ,parts[3]))
                self.client_socket.send("Ok")
            except:
                self.client_socket.send("ERROR")
     
            data=self.buildMsgToClient(self.login,"Name","Server","Yosi")
        
        
    def run(self):
        stop = 1
        while stop == 1:
            try:
                client_info = self.client_socket.recv(1024)
                
            except:
                print ("client {} close forcibly the socket".format(self.user))
                stop = 0 #stop the while. get out from thread
                #print("111",users)
                for i, o in enumerate(users): # set the user to logout (do not remove him from users list!!!)
                    if o.user == self.user:
                        o.login = "False" #del users[i]
                        #print("222",users)
                        break
                
                continue
            #handle_client.broadcast(client_info)
            client_info_str = client_info.decode('utf-8')
            
            if client_info_str == "":
                self.client_socket.close()
                print ("client close the socket")
            print ("server got: " + client_info_str)
            data = self.parse_client_message(client_info_str)
            if data == "Send":
                continue #we already send response to client from parse_client_message()
            data = data.encode('utf-8') #convert the string to bytes
            self.client_socket.send(data)

        
class Server():
    def __init__(self, port):
        
    
        self.server_socket = socket()
        self.server_socket.bind(('0.0.0.0',8820))

    def go(self):
        self.server_socket.listen(5)
        
        while(1):
            (client_socket, client_address) = self.server_socket.accept()
            print("new client connect")
            
            stam = handle_client(client_socket)
            stam.start()


def main():
    print("server start")
    a = Server(8820)
    a.go() 

           
if __name__ == "__main__":
    main()