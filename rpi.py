#coding:utf-8
#import necessary package
import socket
import time
import sys
HOST_IP = "192.168.137.67" #import socket
import time
import sys
SERVER_IP = "192.168.137.67" #IP address of raspberry
SERVER_PORT = 8888
print("Starting socket: TCP...")
server_addr = (SERVER_IP, SERVER_PORT)
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        print("Connecting to server @ %s:%d..." %(SERVER_IP, SERVER_PORT))
        socket_tcp.connect(server_addr)
        break
    except Exception:
        print("Can't connect to server,try it latter!")
        time.sleep(1)
        continue
print("Please input:")
while True:
    try:
        data = socket_tcp.recv(512)
        if len(data)>0:
            print("Received: %s" % data)
            command=input()
            socket_tcp.send(bytes(command.encode('utf-8')))
            time.sleep(1)
            continue
    except Exception as e:
        exc_type, exc_value, exc_traceback_obj = sys.exc_info()
        print("exc_type: %s" % exc_type)
        print("exc_value: %s" % exc_value)
        print("exc_traceback_obj: %s" % exc_traceback_obj)
        socket_tcp.close()
        socket_tcp=None
        sys.exit(1)
HOST_PORT = 8888
print("Starting socket: TCP...")
#1.create socket object:socket=socket.socket(family,type)
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("TCP server listen @ %s:%d!" %(HOST_IP, HOST_PORT) )
host_addr = (HOST_IP, HOST_PORT)
#2.bind socket to addr:socket.bind(address)
socket_tcp.bind(host_addr)
#3.listen connection request:socket.listen(backlog)
socket_tcp.listen(1)
#4.waite for client:connection,address=socket.accept()
socket_con, (client_ip, client_port) = socket_tcp.accept()
print("Connection accepted from %s." %client_ip)
socket_con.send("Welcome to RPi TCP server!")
print("Receiving package...")
###主循环
while True:
    try:
        data=socket_con.recv(512)
        if len(data)>0:
            print("Received:%s"%data)
            socket_con.send(data)
            time.sleep(1)
            continue
    except Exception:
        socket_tcp.close()
        sys.exit(1)
