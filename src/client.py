import socket
import sys
import select

READ_BUFFER = 4096  # read buffer
PROMPT = ">"

def client_loop():

    # create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # connect to server
    host = "localhost"  # server address
    # port = int(sys.argv[1])  # server port
    port = 8080
    s.connect((host, port))
    s.setblocking(False)

    flag = True

    while flag:
        try:
            sys.stdout.write(PROMPT)  # write prompt= ">"
            sys.stdout.flush()  # flush buffer

            readable, writable, exceptional = select.select([sys.stdin, s], [], [])  # inputs readable (same as for server)

            for i in readable:
                if i == s:  # if it is the server trying to send a message
                    data = s.recv(READ_BUFFER)
                    if not data:
                        print("Shutting down")
                        flag = False
                        break
                    if data.decode() == "exit":  # disconnect is ok
                        flag = False
                        break
                    else:
                        server_msg = data.decode()
                        sys.stdout.write(server_msg)  # otherwise, echo the message that the server sent you
                        sys.stdout.flush()
                        if "Game over" in server_msg:
                            flag= False
                            break

                    # sys.stdout.write(prompt)
                    sys.stdout.flush()
                else:
                    data = input()  # otherwise, it is a message you want to send from system buffer
                    if data:
                        s.sendall(data.encode())  # send to server
        except:
            sys.stdout.write("Client shutting down\n")  # exception block, gracefully shut down
            if s:
                msg = "/disconnect"
                s.send(msg.encode())
            s.close()
            break

def main():

    if len(sys.argv) != 1:  # gracefully handle incorrect usage of python file
        print("Usage: client.py\n")
        sys.exit(1)

    client_loop()

main()