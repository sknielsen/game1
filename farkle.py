import random, os, scoring_tools

class Die:
    # Creates die class with roll, freeze and unfreeze methods

    def __init__(self, number, sides=6):
        self.number = number
        self.sides = sides
        self._frozen = False
        self._value_to_str = { 1: """
            ________            
           /\       \           
          /  \   ()  \          
    {0}.   /    \_______\         
         \    /       /         
          \  /       /          
           \/_______/           """, 2: """
            ________            
           /\ ()    \           
          /  \     ()\          
    {0}.   /    \_______\         
         \    /       /         
          \  /       /          
           \/_______/           """, 3: """
            ________            
           /\ ()    \           
          /  \   ()  \          
    {0}.   /    \_____()\         
         \    /       /         
          \  /       /          
           \/_______/           """, 4: """
            ________            
           /\ () () \           
          /  \       \          
    {0}.   /    \_()_()_\         
         \    /       /         
          \  /       /          
           \/_______/           """, 5: """
            ________            
           /\ () () \           
          /  \   ()  \          
    {0}.   /    \_()_()_\         
         \    /       /         
          \  /       /          
           \/_______/           """, 6: """
            ________            
           /\ () () \           
          /  \ () () \          
    {0}.   /    \_()_()_\         
         \    /       /         
          \  /       /          
           \/_______/           """}

    def roll(self):
        # Assigns die random number from 1 to 6
        self.value = random.randint(1, self.sides)

    def freeze(self):
        # Adds a freeze attribute to the die so it is not rolled
        self._frozen = True

    def unfreeze(self):
        # Turns off the freeze attribute so the die will be rolled
        self._frozen = False

    def __str__(self):
        if self._frozen:
            return 'Kept ' + self._value_to_str[self.value].format(self.number)
        else:
            return self._value_to_str[self.value].format(self.number)

# Initialize six dice
die1 = Die(1)
die2 = Die(2)
die3 = Die(3)
die4 = Die(4)
die5 = Die(5)
die6 = Die(6)
game_dice = [die1, die2, die3, die4, die5, die6]

def clear_screen():
    os.system('clear')

def begin_game():
    # Prints welcome message and prompts for number of users
    clear_screen()
    players = int(raw_input("""
        Hello and welcome to Farkle! 
        The goal of this game is to reach 10,000 points. 

        Players take turns rolling all six dice. After each roll you take out any dice 
        worth points that you would like to keep, and set those aside. At least one die must 
        be kept from each roll. You then continue to roll the remaining dice. If all six dice
        have be set aside, then you can pick up all six again and continue rolling, adding
        to your score. A turn is over when a player either decides to stop rolling or if 
        they do not get any dice worth points in a roll. This is called FARKLE, and you 
        lose all the points for that turn. Play then continues to the next player, 
        and on until someone reaches 10,000 points.
        The scoring for the dice is as follows:

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

         Now let's play! How many players are there? """))

    players = range(1, (players + 1))
    return players

def dice_roll(saved_dice_numbers):
    # Rolls and prints unfrozen dice or just prints frozen dice
    for die in game_dice:
        if die.number in saved_dice_numbers:
            print(die)
        else:
            die.roll()
            print(die)

def unfreeze_dice():
    # unfreezes all dice
    for die in game_dice:
        die.unfreeze()

def keep_dice():
    # Prompts for which dice to keep and returns answer
    kept_dice = raw_input("Which number dice would you like to keep? (ie '1 3 4', 'all' or 'none') ")
    if kept_dice.lower() == 'none':
        return False
    elif kept_dice.lower() == 'all':
        return [1, 2, 3, 4, 5, 6]
    else:
        return map(int, kept_dice.split())

def rolling():
    # Continues rolling dice as long as player wants to keep rolling
    saved_dice_numbers = []
    while True:
        clear_screen()
        dice_roll(saved_dice_numbers)
        kept_dice = keep_dice()
        if not kept_dice:
            print('FARKLE!')
            return
        else:
            saved_dice_numbers.extend(kept_dice)
            if sorted(list(set(saved_dice_numbers))) == [1, 2, 3, 4, 5, 6]:
                unfreeze_dice()
                saved_dice_numbers = []
            else:
                for die_number in saved_dice_numbers:
                    game_dice[die_number - 1].freeze()
            roll_again_answer = raw_input('would you like to continue rolling? [y/n] ')
            if roll_again_answer.lower() == 'n':
                return

def game_play(players):
    # Cycles through each player
    still_playing = True
    player_scores = {}
    # Initialize scores to 0 for each player
    for player in players:
        player_scores[player] = 0
    while still_playing:
        for player in players:
            unfreeze_dice()
            try:
                input = raw_input("It is player number {0}'s turn! Press Enter to roll! ".format(player))
            except:
                pass
            rolling()
            #turn_score = int(raw_input('What was your score for this turn? '))
            # Adds players score from that round to running total
            #player_scores[player] += turn_score
            # Game ends if a player reachs 10000 points
            if player_scores[player] >= 10000:
                still_playing = False
                print 'Player number %i wins!!!' % (player)

def main():
    game_play(begin_game())

if __name__ == '__main__':
    main()

