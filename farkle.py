import random
import os

class Die(object):

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
        self.value = random.randint(1, self.sides)

    def freeze(self):
        self._frozen = True

    def unfreeze(self):
        self._frozen = False

    def __str__(self):
        if self._frozen:
            return "Kept " + self._value_to_str[self.value] % self.number
        else:
            return self._value_to_str[self.value] % self.number

die1 = Die(1)
die2 = Die(2)
die3 = Die(3)
die4 = Die(4)
die5 = Die(5)
die6 = Die(6)
rolling_dice = [die1, die2, die3, die4, die5, die6]

def begin_game():
    os.system('clear')
    players = int(raw_input("""
                          Hello and welcome to Farkle! How many players are there? """))
    players = range(1, (players + 1))
    return players

def dice_roll(saved_dice_numbers):
    for die in rolling_dice:
        if die.number in saved_dice_numbers:
            print(die)
        else:
            die.roll()
            print(die)

def unfreeze_dice():
    for die in rolling_dice:
        die.unfreeze()

def rolling():
    saved_dice_numbers = []
    while True:
        dice_roll(saved_dice_numbers)
        kept_dice = raw_input("Which number dice would you like to keep? (ie '1 3 4' or 'none') ")
        if kept_dice.lower() == 'none':
            print('FARKLE!')
            return
        else:
            saved_dice_numbers.extend(map(int, kept_dice.split()))
            if saved_dice_numbers == [1, 2, 3, 4, 5, 6]:
                unfreeze_dice()
                saved_dice_number = []
            else:
                for die_number in saved_dice_numbers:
                    rolling_dice[die_number - 1].freeze()
            roll_again_answer = raw_input("would you like to continue rolling? [y/n] ")
            if roll_again_answer.lower() == 'n':
                return

def player_turn(players):
    still_playing = True
    scores = {}
    for player in players:
        scores[player] = 0
    while still_playing:
        for player in players:
            os.system('clear')
            unfreeze_dice()
            print("It is player number %i's turn!") % (player)
            rolling()
            turn_score = int(raw_input('What was your score for this turn? '))
            scores[player] += turn_score
            if scores[player] >= 10000:
                still_playing = False
                print 'Player number %i wins!!!' % (player)

def main():
    player_turn(begin_game())

if __name__ == '__main__':
    main()

