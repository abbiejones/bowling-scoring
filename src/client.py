#!/usr/bin/env python
# client for IRC

import socket
import sys
import select

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# connect to server
host = "127.0.0.1"  # server address
port = int(sys.argv[1])  # server port
s.connect((host, port))
s.setblocking(0)
prompt = ">"

READ_BUFFER = 4096  # read buffer
PORT = 3030

flag = True

if len(sys.argv) != 2:  # gracefully handle incorrect usage of python file
    print("Usage: client.py <PORT>\n")
    sys.exit(1)

while flag:
    try:
        sys.stdout.write(prompt)  # write prompt= ">"
        sys.stdout.flush()  # flush buffer

        readable, writable, exceptional = select.select([sys.stdin, s], [], [])  # inputs readable (same as for server)

        for i in readable:
            if i == s:  # if it is the server trying to send a message
                data = s.recv(READ_BUFFER)
                if not data:
                    print
                    "Shutting down"
                    flag = False
                    break
                if data == "exit":  # disconnect is ok
                    break
                else:
                    sys.stdout.write(data + "\n")  # otherwise, echo the message that the server sent you
                    sys.stdout.flush()

                # sys.stdout.write(prompt)
                sys.stdout.flush()
            else:
                data = input()  # otherwise, it is a message you want to send from system buffer
                if data:
                    s.sendall(data)  # send to server
    except:
        sys.stdout.write("Player shutting down\n")  # exception block, gracefully shut down
        if s:
            msg = "/disconnect"
            s.send(msg)
        s.close()
        break