import socket
import selectors
import game as g


READ_BUFFER = 4096
HOST = '127.0.0.1'
PORT = 3030
MAX_PLAYERS = 5

def start_server():
    sel = selectors.DefaultSelector()

    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.bind((HOST, PORT))
    lsock.listen()
    print('listening on', (HOST, PORT))
    lsock.setblocking(False)
    sel.register(lsock, selectors.EVENT_READ, data=None)

    poll(sel)

def poll(buffer):
    while True:
        events = buffer.select(timeout=False)


def main():

    if (input("New game? (y/n) ")).lower() == "y":
        g.start_game()
    else:
        exit()

main()
