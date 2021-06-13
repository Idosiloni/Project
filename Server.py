from tkinter import *

from tkinter.scrolledtext import ScrolledText
from time import sleep
import sqlite3
from queue import Queue
from socket import *
from threading import *
import datetime
flag = 1


class handle_client(Thread):  
    
    print("Hello")
    clients =[] #class variable
    lock = Lock()
    
    """
    conn = sqlite3.connect('DataBase1.db')
    c=conn.cursor()
    """
    
    
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
                conn = sqlite3.connect('DataBase1.db')
                c=conn.cursor()
                print("trying to sql")
                print(parts[1] ,parts[2] ,parts[3])
                
                sqlCmd = "INSERT INTO Users(Username,Password,Job) VALUES ('{}', '{}', '{}')".format(parts[1] ,parts[2] ,parts[3])
                print(sqlCmd)
                c.execute(sqlCmd)
                print("3333")
                conn.commit()
                print("1")
                self.client_socket.send("Ok".encode())
            except:
                self.client_socket.send("ERROR".encode())


        elif message_type =="LogIn":
            conn = sqlite3.connect('DataBase1.db')
            cursor = conn.execute("SELECT * from Users")

            for row in cursor:
                username = False
                password=False
                print(row[0]+''+row[1]+''+row[2])
                if row[0] == parts[1]:
                    username = True
                if row[1] == parts[2]:
                    password = True
                if username and password:
                    break
            if username and password:
                print(row[2])
                self.client_socket.send(row[2].encode())
            else:
                self.client_socket.send("ERROR".encode())

            conn.close()
        elif message_type == "schedule":
            try:
                conn = sqlite3.connect('DataBase1.db')
                c = conn.cursor()
                print("trying to sql")
                print(parts[1], parts[2], parts[3])

                sqlCmd = "INSERT INTO Schedule(Date,Time,ClassType,Content) VALUES ('{}', '{}', '{}' ,'{}')".format(parts[1], parts[2],
                                                                                                     parts[3],parts[4])
                print(sqlCmd)
                c.execute(sqlCmd)
                print("3333")
                conn.commit()
                print("1")
                self.client_socket.send("Ok".encode())
            except:
                self.client_socket.send("ERROR".encode())
        elif message_type == "Get":
            conn = sqlite3.connect('DataBase1.db')
            cursor = conn.execute("SELECT * from Schedule")
            str1 = ""
            x = datetime.datetime.now()

            for row in cursor:
                if x.strftime("%x")==row[0]:
                    str1 = str1 + '\n' + row[0] + ' ' + row[1] + ' ' + row[2] + ' ' + row[3]
            self.client_socket.sendall(str1.encode())
            conn.close()







    def run(self):
        stop = 1
        while stop == 1:
            try:
                client_info = self.client_socket.recv(1024)
                
            except:
                print ("client {} close forcibly the socket".format(self.user))
                stop = 0 #stop the while. get out from thread
                #print("111",users
                
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
            #data = data.encode('utf-8') #convert the string to bytes
            #self.client_socket.send(data)

        
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