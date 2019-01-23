import socket
import selectors
import re

HOST = '127.0.0.1'
PORT = 3030

class Game:

    def __init__(self, player):
        self.player = player
        self.frame = 0
        self.totalScore = 0
        self.scorePerFrame = []
        self.frame_input = None

    def rules_of_game(self):
        print("Pool Scoring Application\n"
              "When prompted for the next frame score,\n"
              "please enter it in the following format: \n\n"
              "[],[]\n\n"
              "or possibly (in the 10th & final frame)\n\n"
              "[],[],[]\n\n"
              "Examples of valid scores:\n"
              "X\n"
              "7,/\n"
              "7,2\n"
              "7,/,3\n"
              "To quit game before you are finished, please enter:\n"
              "quit\n")

    def add_frame(self):
        self.scorePerFrame[self.frame] = self.frame_input
        self.frame += 1

    def print_score(self):
        return

    def calculate_score(self):
        return

    def is_game_over(self):
        if self.frame < 10:
            return False
        return True

    def parse_user_input(self, frame_score):
        if frame_score.lower() == "quit":
            return -1
        valid_expression = "^X|[0-9],([0-9]|\/)$"
        self.frame_input = frame_score.replace(" ", "")

        if re.search(valid_expression, self.frame_input):
            self.frame_input = self.frame_input.split(",")
            return 1

        return 0

    def game_play(self):
        self.rules_of_game()

        while (not self.is_game_over()):

            valid_answer = False
            userFrameScore = None

            while (not valid_answer):

                userFrameScore = input("Please enter the score for frame {}: ".format(self.frame + 1))

                parsed_input = self.parse_user_input(userFrameScore)
                if (parsed_input == -1):
                    return
                elif (parsed_input == 1):
                    valid_answer = True

            self.add_frame()
            self.calculate_score()

            self.print_score()




def start_game():

    game = Game("abbie")
    game.game_play()


#
# def start_server():
#     sel = selectors.DefaultSelector()
#     # ...
#     lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     lsock.bind((HOST, PORT))
#     lsock.listen()
#     print('listening on', (HOST, PORT))
#     lsock.setblocking(False)
#     sel.register(lsock, selectors.EVENT_READ, data=None)
#
#     poll(sel)
#
# def poll(buffer):
#     while True:
#         events = buffer.select(timeout=False)
#
# def main():
#     start_server()
#     poll()

def main():
    if (input("New game?")).lower() == "y":
        start_game()
    else:
        exit()

main()
