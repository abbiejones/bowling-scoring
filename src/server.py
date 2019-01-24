import socket
import select
import queue
import sys
import game as g

PORT = 8080
HOST = "localhost"
READ_BUFFER = 4096

def handle_game(s, data, client_to_game):
    current_game = client_to_game[s]

    if not current_game.is_game_over():
        is_valid = current_game.parse_user_input(data.decode())

        if is_valid == 1:
            current_game.add_frame()
            score = current_game.print_score()
            s.send(score.encode())

        if is_valid == -1:
            s.send("exit")

        s.send("Please enter the score for Frame {}:\n".format(current_game.frame + 1).encode())

def server_loop():

    listening_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listening_server.setblocking(0)
    listening_server.bind((HOST, PORT))
    listening_server.listen(5)
    print("listening on port {}".format(PORT))
    inputs = [listening_server]
    outputs = []
    client_to_game = {}

    while inputs:
        readable, writable, exceptional = select.select(
            inputs, outputs, inputs)

        for s in readable:
            if s is listening_server:
                connection, client_address = s.accept()
                connection.setblocking(0)

                game = g.Game(client_address)
                client_to_game[connection] = game

                welcome_message = game.rules_of_game()
                connection.send(welcome_message.encode())
                inputs.append(connection)

            elif s == sys.stdin:
                data = s.recv(READ_BUFFER)  #if server wants to disconnect, it should receive a message directly from the system read  buffer
                if data == "/disconnect":
                    inputs = [] #close everything and exit
                    break
            else:
                data = s.recv(READ_BUFFER)  #if readable input is from a difference socket, receive message and handle it

                if data:
                    handle_game(s, data, client_to_game)



def main():
    server_loop()

main()
