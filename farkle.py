import random
import os

class Die(object):
    # Creates die class with roll, freeze and unfreeze methods

    def __init__(self, number, sides=6):
        self.number = number
        self.sides = sides
        self._frozen = False
        self._value_to_str = { 1: """
            ________            
           /\       \           
          /  \   ()  \          
     %s.  /    \_______\         
         \    /       /         
          \  /       /          
           \/_______/           """, 2: """
            ________            
           /\ ()    \           
          /  \     ()\          
     %s.  /    \_______\         
         \    /       /         
          \  /       /          
           \/_______/           """, 3: """
            ________            
           /\ ()    \           
          /  \   ()  \          
     %s.  /    \_____()\         
         \    /       /         
          \  /       /          
           \/_______/           """, 4: """
            ________            
           /\ () () \           
          /  \       \          
     %s.  /    \_()_()_\         
         \    /       /         
          \  /       /          
           \/_______/           """, 5: """
            ________            
           /\ () () \           
          /  \   ()  \          
     %s.  /    \_()_()_\         
         \    /       /         
          \  /       /          
           \/_______/           """, 6: """
            ________            
           /\ () () \           
          /  \ () () \          
     %s.  /    \_()_()_\         
         \    /       /         
          \  /       /          
           \/_______/           """}

    def roll(self):
        # Assignes die random number from 1 to 6
        self.value = random.randint(1, self.sides)

    def freeze(self):
        # Freezes die so it won't roll
        self._frozen = True

    def unfreeze(self):
        self._frozen = False

    def __str__(self):
        if self._frozen:
            return "Kept " + self._value_to_str[self.value] % self.number
        else:
            return self._value_to_str[self.value] % self.number

# Initialize six dice
die1 = Die(1)
die2 = Die(2)
die3 = Die(3)
die4 = Die(4)
die5 = Die(5)
die6 = Die(6)
# List of the dice
rolling_dice = [die1, die2, die3, die4, die5, die6]

def begin_game():
    # Clears the screen and prints welcome message and prompts for number of users
    os.system('clear')
    players = int(raw_input("""
        Hello and welcome to Farkle! 
        The goal of this game is to reach 10,000 points. The scoring is as follows:

                 5's = 50 point
                 1's = 100 points
                 1,1,1 = 300 points
                 2,2,2 = 200 points
                 3,3,3 = 300 points
                 4,4,4 = 400 points
                 5,5,5 = 500 points
                 6,6,6 = 600 points
                 Four of a Kind = 1,000 points
                 Five of a Kind = 2,000 points
                 Six of a Kind = 3,000 points
                 A Straight of 1-6 = 1,500 points
                 Three Pairs = 1,500 points
                 Four of a Kind + a Pair = 1,500
                 Two sets of Three of a Kind = 2,500

         Players take turns rolling all six dice. Take out any dice worth points
         after each roll. This forms your running score for the round. Roll the
         remaining dice, removing any dice worth points and adding them to your
         running total. If you are ever able to set aside all six dice, you may
         re-roll all of your dice and keep building your running total. If ever you
         are unable to set aside any dice (no dice are worth points), you have
         Farkled. You lose your running point total and your turn is over.You continue
         rolling until you either Pass or Farkle. Then the next player rolls the six dice.
         Play continues until it is your turn again.

         Now let's play! How many players are there? """))
    # Sets list with name players with numbers 1 to players
    players = range(1, (players + 1))
    return players

def dice_roll(saved_dice_numbers):
    print saved_dice_numbers
    # Rolls and prints dice or just prints dice of they are frozen
    for die in rolling_dice:
        if die.number in saved_dice_numbers:
            print(die)
        else:
            die.roll()
            print(die)

def unfreeze_dice():
    # unfreezes all dice
    for die in rolling_dice:
        die.unfreeze()

def rolling():
    # Continues rolling dice as long as player wants to keep rolling and asks which dice to freeze
    saved_dice_numbers = []
    while True:
        os.system('clear')
        dice_roll(saved_dice_numbers)
        kept_dice = raw_input("Which number dice would you like to keep? (ie '1 3 4', 'all' or 'none') ")
        if kept_dice.lower() == 'none':
            print('FARKLE!')
            return
        elif kept_dice.lower() == 'all':
            unfreeze_dice()
            saved_dice_numbers = []
            roll_again_answer = raw_input("would you like to continue rolling? [y/n] ")
            if roll_again_answer.lower() == 'n':
                return
        else:
            # Adds the numbers of the dice the player chose to keep to the list saved_dice_numbers
            saved_dice_numbers.extend(map(int, kept_dice.split()))
            # If all the dice are saved then they all unfreeze
            if sorted(saved_dice_numbers) == [1, 2, 3, 4, 5, 6]:
                unfreeze_dice()
                saved_dice_numbers = []
            else:
                for die_number in saved_dice_numbers:
                    rolling_dice[die_number - 1].freeze()
            roll_again_answer = raw_input("would you like to continue rolling? [y/n] ")
            if roll_again_answer.lower() == 'n':
                return

def player_turn(players):
    # Cycles through each player and prompts them for their score at the end of each turn
    still_playing = True
    # Initiate empty dictionary called scores to keep players scores in
    scores = {}
    # Initialize scores to 0 for each player
    for player in players:
        scores[player] = 0
    while still_playing:
        for player in players:
            os.system('clear')
            unfreeze_dice()
            try:
                input = raw_input("It is player number %i's turn! Hit any key to roll! " % (player))
            except:
                pass
            rolling()
            turn_score = int(raw_input('What was your score for this turn? '))
            # Adds players score from that round to running total
            scores[player] += turn_score
            # Game ends if a player reachs 10000 points
            if scores[player] >= 10000:
                still_playing = False
                print 'Player number %i wins!!!' % (player)

def main():
    player_turn(begin_game())

if __name__ == '__main__':
    main()

