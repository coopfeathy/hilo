'''
HiLo
Author: Cooper Featherstone
'''

import random

class Deal:
    def __init__(self):
        self.cards = []
        self.score = 300
        self.i = 0

    def new_card(self):
        self.cards.append(random.randint(1,13)) #cards go from 1-13, adds a new card to list
        self.i += 1 #increases i value for tracking next card

    def compare(self, guess): 
        result = False

        if self.cards[self.i - 2] > self.cards[self.i - 1]: #checks the two card variables and compares
            firstIsHigher = True
        else:
            firstIsHigher = False

        if firstIsHigher == True: #returns true or false based on user input
            if guess == 'l':
                result = True
            elif guess == 'h':
                result = False

        if firstIsHigher == False:
            if guess == 'l':
                result = False
            elif guess == 'h':
                result = True

        return result


class Hilo:
    def __init__(self):
        pass

    def start_game(self):
        deal = Deal()
        deal.new_card()
        playing = True
        guess = ''
        while playing:
            print("\nThe card is: ", deal.cards[deal.i - 1]) #deal.i - 1 points to the current card. When comparing, current card becomes deal.i - 2 and new card is deal.i - 1
            
            validResponse = False

            # Validates if the user enter an h or an l
            while validResponse == False:
                guess = input("Higher or lower? [h/l] ") #get user input here, should put check to make sure they type h or l
                if (guess.lower() == 'h' or guess.lower() == 'l'):
                    validResponse = True
                else:
                    print("\nPlease enter 'h' or 'l'")

            deal.new_card()

            # Here the new card is compared to the guess
            result = deal.compare(guess.lower())

            if result == True:   #Announces the winner and gives points
                print("\nYou won! +100 points\n") 
                deal.score = deal.score + 100
            elif result == False:
                print("\nBetter luck next time! -75 points\n")
                deal.score = deal.score - 75

            print("The new card was: ", deal.cards[deal.i -1], "\n") #declare the new card

            print("Your score is: ", deal.score) #print calculated score
            if deal.score > 0:      #test if game end and prompt user to play again
                playing = input("Keep playing? [y/n] ") in ['y']
            else:
                print("Sorry! Game over!")
                playing = False


if __name__ == "__main__":
    hilo = Hilo()
    hilo.start_game()