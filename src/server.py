#Abbie Jones
#lets-go-bowling server polls for new requests from clients and manages games

import socket
import select
import sys
import game as g

PORT = 8080
HOST = "localhost"
READ_BUFFER = 4096

def handle_game(s, data, client_to_game):
    current_game = client_to_game[s]
    score = 0

    if not current_game.is_game_over():
        is_valid = current_game.parse_user_input(data.decode()) #parse data from user

        if is_valid == 1:
            current_game.add_frame() #add frame to list
            score = current_game.print_score()
            s.send(score.encode())

        #print score
        if current_game.frame < 10:
            (s.send("Please enter the score for Frame {}:\n".format(current_game.frame + 1).encode()))
        else:
            s.send("Game over!\n\n".encode())

def server_loop():

    listening_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listening_server.setblocking(0)
    listening_server.bind((HOST, PORT))
    listening_server.listen(5)
    print("listening on port {}".format(PORT))
    inputs = [listening_server]
    outputs = []
    client_to_game = {}

    running = 1

    while running: #continuously polling for requests
        try:
            while inputs:
                readable, writable, exceptional = select.select(
                    inputs, outputs, inputs)

                for s in readable:
                    if s is listening_server:
                        connection, client_address = s.accept()
                        connection.setblocking(0)

                        game = g.Game(client_address) #starts new game
                        client_to_game[connection] = game #maps client address to game

                        welcome_message = game.rules_of_game()
                        connection.send(welcome_message.encode())

                        inputs.append(connection)

                    else:
                        data = s.recv(READ_BUFFER)  #if readable input is from a difference socket, receive message and handle it

                        if data:
                            handle_game(s, data, client_to_game) #handles game per user

        except:
            sys.stdout.write("Server shutting down\n")
            break

    listening_server.close()


def main():
    server_loop()
    exit()

main()
