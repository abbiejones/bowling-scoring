import re

class Game:

    def __init__(self, player):
        self.player = player
        self.frame = 0
        self.runningScore = 0
        self.trackFrames = []
        self.frame_input = None


    def rules_of_game(self):
        return "Pool Scoring Application\n" \
               "When prompted for the next frame score,\n"\
              "please enter it in the following format: \n\n"\
              "[],[]\n\n"\
              "or possibly (in the 10th & final frame)\n\n"\
              "[],[],[]\n\n"\
              "Examples of valid scores:\n"\
              "X\n"\
              "7,/\n"\
              "7,2\n"\
              "7,/,3\n"\
              "To quit game before you are finished, please enter:\n"\
              "quit\n\n" \
               "Please enter the score for Frame 1: \n"


    def add_frame(self):
        self.trackFrames.append(self.frame_input)
        self.update_score()
        self.frame += 1


    def print_score(self):
        return "-----------------\n" \
               "Current score  for Player {}\n" \
              "at Frame {}:\n" \
              "{}\n" \
               "-----------------\n".format(self.player[1], self.frame, self.runningScore)

    def frame_score(self, frame1,frame2=0):
        score = 0
        if frame1 == 'X':
            score += 10
        else:
            score += int(frame1)

        if frame2 == 'X':
            score += 10
        elif frame2 == '/':
            score += 10 - int(frame1)
        else:
            score += int(frame2)

        return score


    def update_score(self):

        runningScore = 0
        flattened_frames = [subframe for frame in self.trackFrames for subframe in frame]

        for x in range(len(flattened_frames)):
            if flattened_frames[x] == 'X':

                if x + 2 < len(flattened_frames):
                    runningScore += 10 + self.frame_score(flattened_frames[x+1], flattened_frames[x+2])

            elif flattened_frames[x] == '/':

                if x + 1 < len(flattened_frames):
                    runningScore += 10 + self.frame_score(flattened_frames[x+1])

                runningScore -= self.frame_score(flattened_frames[x-1])

                if self.frame == 9 and ((x + 2) == len(flattened_frames)):
                    break

            else:
                runningScore += self.frame_score(flattened_frames[x])


        self.runningScore = runningScore


    def is_game_over(self):
        if self.frame < 10:
            return False

        return True


    def parse_user_input(self, frame_score):
        if frame_score.lower() == "quit":
            return -1

        valid_expression = "X|[0-9],([0-9]|\/)"

        self.frame_input = frame_score.replace(" ", "")

        if self.frame < 9:

            if re.match(valid_expression, self.frame_input) and (len(self.frame_input) == 1 or len(self.frame_input) == 3):

                self.frame_input = self.frame_input.split(",")

                if len(self.frame_input) == 3 or (len(self.frame_input) == 2 and self.frame_input[1] != '/' and self.frame_score(self.frame_input[0], self.frame_input[1]) >= 10):
                    return 0

                return 1

        valid_tenth_expression = "^(X,([0-9]|X),([0-9]|X|\/))|([0-9],\/,([0-9]|X))|([0-9],[0-9])$"

        if self.frame == 9:
            if re.match(valid_tenth_expression, self.frame_input) and (len(self.frame_input) == 3 or len(self.frame_input) == 5):

                self.frame_input = self.frame_input.split(",")

                if len(self.frame_input) == 2 and self.frame_input[1] != '/' and self.frame_score(self.frame_input[0], self.frame_input[1]) >= 10:
                    return 0

                if len(self.frame_input) == 3 and self.frame_input[1] != '/' and self.frame_input[1] != 'X' and \
                        self.frame_score(self.frame_input[1], self.frame_input[2]) >= 10:
                    return 0

                return 1
        return 0

    def game_play(self):
        self.rules_of_game()

        if (input("Ready to start? (y/n) ").lower() == "y"):

            while (not self.is_game_over()):

                valid_answer = False
                userFrameScore = None

                userFrameScore = input("Please enter the score for frame {}: ".format(self.frame + 1))

                while (not valid_answer):
                    parsed_input = self.parse_user_input(userFrameScore)

                    if (parsed_input == -1):  # player wants to exit game
                        return

                    elif (parsed_input == 1):  # player's input is valid
                        valid_answer = True
                        break

                    userFrameScore = input("Please try again: ".format(self.frame + 1))


                self.add_frame()
                self.print_score()
