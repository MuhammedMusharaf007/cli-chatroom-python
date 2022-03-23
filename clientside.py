import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket>SOCK_STREAM)
if len(sys.argv) != 3:
    print("Correct usage: Script, IP Address, Port Number")
    exit()
IP_address = str(sys.argv[1])
port = str(sys.argv[2])
server.connect((IP_address, Port))

while True:
    socket_list = [sys.stdin, server]
    read_sockets, write_socket, error_socket = select(sockets_list, [], [])
    for socks in read_sockets:
        if sock == server:
            message = sock.recv(2048)
            print(message)
        else:
            message = sys.stdn.readline()
            server.send(message)
            sys.stdout.write("[You] : ")
            sys.stdout.write(message)
            sys.stdout..flush()
server.close()
