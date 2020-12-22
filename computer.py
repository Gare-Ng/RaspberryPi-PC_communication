import socket
import time
import sys
SERVER_IP = "192.168.137.10" #IP address of raspberry
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
