#Abbie Jones
#Game class to control individual bowling game

import re

class Game:

    def __init__(self, player):
        self.player = player
        self.frame = 0 #current frame
        self.runningScore = 0
        self.trackFrames = [] #list of frame scores
        self.frame_input = None #per frame input from user


    def rules_of_game(self):
        return "Pool Scoring Application\n" \
               "When prompted for the next frame score,\n"\
              "please enter it in the following format: \n\n" \
               "[]\n" \
               "or\n"\
              "[],[]\n\n"\
              "or possibly (in the 10th & final frame)\n\n"\
              "[],[],[]\n\n"\
              "Examples of valid scores:\n"\
              "X\n"\
              "7,/\n"\
              "7,2\n"\
              "7,/,3\n\n"\
               "Please enter the score for Frame 1: \n"


    #append new frame score to list
    def add_frame(self):
        self.trackFrames.append(self.frame_input)
        self.update_score()
        self.frame += 1


    def print_score(self):
        if self.frame < 10:
            return "-----------------\n" \
                   "Current score  for Player {}\n" \
                  "at Frame {}:\n" \
                  "{}\n" \
                   "-----------------\n".format(self.player[1], self.frame, self.runningScore)
        else:
            return "-----------------\n" \
                   "Final score for Player {}:\n" \
                  "{}\n" \
                   "-----------------\n".format(self.player[1], self.runningScore)


    #helper function for calculating score after frame score list is flattened
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

        #flatten list so scores aren't divided into frames
        flattened_frames = [subframe for frame in self.trackFrames for subframe in frame]

        for x in range(len(flattened_frames)):
            if flattened_frames[x] == 'X':

                if x + 2 < len(flattened_frames): #only update score if you can lookahead two rolls
                    runningScore += 10 + self.frame_score(flattened_frames[x+1], flattened_frames[x+2])

            elif flattened_frames[x] == '/':

                if x + 1 < len(flattened_frames): #only update score if you can lookahead one roll
                    runningScore += 10 + self.frame_score(flattened_frames[x+1])

                runningScore -= self.frame_score(flattened_frames[x-1]) #remove weight from first roll in spare

                if self.frame == 9 and ((x + 2) == len(flattened_frames)): #don't doubly add scores from final frame
                    break

            else:
                runningScore += self.frame_score(flattened_frames[x])


        self.runningScore = runningScore #update field


    def is_game_over(self):
        if self.frame < 10:
            return False

        return True


    def parse_user_input(self, frame_score):

        valid_expression = "X|[0-9],([0-9]|\/)"

        self.frame_input = frame_score.replace(" ", "")

        if self.frame < 9:

            if re.match(valid_expression, self.frame_input) and (len(self.frame_input) == 1 or len(self.frame_input) == 3):
            #if input matches regex, and its length is either 1 or 3
                self.frame_input = self.frame_input.split(",") #split it up

                if len(self.frame_input) == 3 or (len(self.frame_input) == 2 and self.frame_input[1] != '/' and self.frame_score(self.frame_input[0], self.frame_input[1]) >= 10): #make sure list isn't of length 3 and that it doesn't equal 10 or more
                    return 0

                return 1 #valid

        valid_tenth_expression = "^(X,([0-9]|X),([0-9]|X|\/))|([0-9],\/,([0-9]|X))|([0-9],[0-9])$"

        if self.frame == 9:
            if re.match(valid_tenth_expression, self.frame_input) and (len(self.frame_input) == 3 or len(self.frame_input) == 5):
                #if input matches regex and its length is either 3 or 5
                self.frame_input = self.frame_input.split(",")

                if len(self.frame_input) == 2 and self.frame_input[1] != '/' and self.frame_score(self.frame_input[0], self.frame_input[1]) >= 10:  #make sure scores don't add up to 10 or greater
                    return 0

                if len(self.frame_input) == 3 and self.frame_input[1] != '/' and self.frame_input[1] != 'X' and \
                        self.frame_score(self.frame_input[1], self.frame_input[2]) >= 10: #alt. make sure scores don't add up to 10 or greater
                    return 0

                return 1
        return 0

    #for testing

    # def game_play(self):
    #     self.rules_of_game()
    #
    #     if (input("Ready to start? (y/n) ").lower() == "y"):
    #
    #         while (not self.is_game_over()):
    #
    #             valid_answer = False
    #             userFrameScore = None
    #
    #             userFrameScore = input("Please enter the score for frame {}: ".format(self.frame + 1))
    #
    #             while (not valid_answer):
    #                 parsed_input = self.parse_user_input(userFrameScore)
    #
    #                 if (parsed_input == 1):  # player's input is valid
    #                     valid_answer = True
    #                     break
    #
    #                 userFrameScore = input("Please try again: ".format(self.frame + 1))
    #
    #
    #             self.add_frame()
    #             self.print_score()
