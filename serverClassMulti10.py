import socket
from threading import Thread, Lock
import time

users=[]

class User():

    def __init__(self,user, password, email, user_socket):
        
        self.user = user
        self.password = password
        self.email = email
        self.login = "True"
        self.user_socket = user_socket
        
    def __repr__(self):
        data = self.user + " " + self.password + " " + self.email + " " + self.login + " " 
        return data

class handle_client(Thread):  
    clients =[] #class variable
    lock = Lock()

    @classmethod 
    def broadcast(cls,to,msg):  #class method
        #msg = msg +","+ src
        msg = msg.encode('utf-8')
        handle_client.lock.acquire()
        #for sock in handle_client.clients:
        #    sock.send( msg)
        for i in users:
            if i.login == "True":
                if to == "All": #send message to all
                    i.user_socket.send(msg)
                elif to == i.user: #send message just to specific user
                    i.user_socket.send(msg)
        handle_client.lock.release()




    def __init__(self, client_socket):
        Thread.__init__(self)
        self.client_socket = client_socket
        self.login = "False"
        self.user = None
        handle_client.clients.append( client_socket )


    def buildMsgToClient(self,msg_login,msg_type,srcName,msg_data):
        data = msg_login+","+msg_type+","+srcName+","+msg_data
        return data

    def parse_client_message(self,client_message):
        parts = client_message.split(",")
        target = parts[0]
        message_type = parts[1]
        if message_type == "Name":
            data=self.buildMsgToClient(self.login,"Name","Server","Yosi")
        
        elif message_type == "Time":
            val = time.ctime()
            data=self.buildMsgToClient(self.login,"Time","Server",val)
            
        elif message_type == "GetMyParams":
            for i in users:
                if i.user == self.user:
                    val = i.user +","+i.password+","+i.email
            data=self.buildMsgToClient(self.login,"GetMyParams","Server",val)

        elif message_type == "WhoLogin":
            val=""
            for i in users:
                if i.login == "True":
                    val = val + i.user +","+i.password+","+i.email+"\n"
            data=self.buildMsgToClient(self.login,"WhoLogin","Server",val)

        elif message_type == "WhoRegisterd":
            val=""
            for i in users:
                val = val + i.user +","+i.password+","+i.email+"\n"
            data=self.buildMsgToClient(self.login,"WhoRegisterd","Server",val)

        elif message_type == "Logout":
            for i in users:
                if i.user == self.user:
                    i.login = "False"
                    i.user_socket = None
            self.login = "False"
            self.user = None
            data=self.buildMsgToClient(self.login,"Logout","Server","You succesfully logout")

        elif message_type == "Login":
            user     = parts[2]
            password = parts[3]
            
            for i in users:
                if i.user == user and i.password == password:
                    print("user {} login succesfully".format(user))
                    self.login = "True"
                    self.user = user
                    i.login = "True"
                    i.user_socket = self.client_socket
                    data=self.buildMsgToClient(self.login,"Login","Server","Succeed")
                    return data
            
            print("user {} login failed".format(user))
            data=self.buildMsgToClient(self.login,"Login","Server","Failed")

        elif message_type == "Registration":
            user     = parts[2]
            password = parts[3]
            email    = parts[4]
            
            for i in users:
                if i.user == user:
                    print("user {} already exist".format(user))
                    data=self.buildMsgToClient(self.login,"Registration","Server","Failed - user already exist")
                    return data
            
            val = User(user,password, email,self.client_socket)
            users.append(val)

            print("The client register user {} password {} email {}".format(user,password, email))
            self.login = "True" #when someone register he also login  
            self.user = user            
            data=self.buildMsgToClient(self.login,"Registration","Server","Succeed")
          
        elif message_type == "Broadcast":
            srcName          = parts[2]
            msgBroadcast     = " ".join(parts[3:])
            data=self.buildMsgToClient(self.login,"Broadcast",srcName,msgBroadcast)
            handle_client.broadcast("All",data)
            data = "Send" #we already send here so no need to send from main loop
        elif message_type == "Chat":
            srcName  = parts[2]
            dstName  = parts[3]
            msgChat  = " ".join(parts[4:])
            data=self.buildMsgToClient(self.login,"Chat",srcName, msgChat)
            handle_client.broadcast(dstName,data) 
            data = "Send"  #we already send here so no need to send from main loop
        elif message_type == "Play": #play is almost identical to chat from the server side
            srcName  = parts[2]
            dstName  = parts[3]
            msgChat  = " ".join(parts[4:])
            data=self.buildMsgToClient(self.login,"Play",srcName, msgChat)
            handle_client.broadcast(dstName,data) 
            data = "Send"  #we already send here so no need to send from main loop    
        else: 
            val = client_message[::-1] #reverse the string
            msg_type = "Unknown"
            msg_data = val
            data = msg_type+","+msg_data
        return data



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
        
    
        self.server_socket = socket.socket()
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
    