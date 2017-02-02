import random

class Die(object):

    def __init__(self, number, sides=6):
        self.number = number
        self.sides = sides

    def roll(self):
        self.die_value = random.randint(1, self.sides)

    def __str__(self):
        return("""
                  ________            
                 /\       \           
                /  \   %i   \          
         %i.    /    \_______\         
               \    /       /         
                \  /       /          
                 \/_______/           """) % (self.die_value, self.number)


die1 = Die(1)
die2 = Die(2)
die3 = Die(3)
die4 = Die(4)
die5 = Die(5)
die6 = Die(6)

def begin_turn():
    die1.roll()
    print(die1)
    die2.roll()
    print(die2)
    die3.roll()
    print(die3)
    die4.roll()
    print(die4)
    die5.roll()
    print(die5)
    die6.roll()
    print(die6)

def player_turn(num_of_players):
    players = 1
    while players <= num_of_players:
        print("It is player number %s's turn!") % (players)
        begin_turn()
        kept_dice = raw_input("Which number dice would you like to keep? (ie '1 3 4' or 'none') ")
        if kept_dice.lower() == 'none':
            print('FARKLE!')
        else:
            kept_dice = map(int, kept_dice.split())
        players += 1

def main():
    num_of_players = int(raw_input('Hello and welcome to Farkle! How many players are there? '))
    player_turn(num_of_players)

if __name__ == '__main__':
    main()

