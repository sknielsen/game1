import random

class dice(object):
    def __init__(self, number, sides = 6):
        self.number = number
        self.sides = sides
    def roll(self):
        die_value = random.randint(1, self.sides)
        print('''
                  ________            
                 /\       \           
                /  \   %i   \          
         %i.    /    \_______\         
               \    /       /         
                \  /       /          
                 \/_______/           ''') % (die_value, self.number)

def player_turn(num_of_players):
    players = 1
    while players <= num_of_players:
        print("It is player number %s's turn!") % (players)
        die1 = dice(1)
        die1.roll()
        die2 = dice(2)
        die2.roll()
        die3 = dice(3)
        die3.roll()
        die4 = dice(4)
        die4.roll()
        die5 = dice(5)
        die5.roll()
        die6 = dice(6)
        die6.roll()
        players += 1

def main():
    num_of_players = int(raw_input('Hello and welcome to Farkle! How many players are there? '))
    player_turn(num_of_players)

if __name__ == "__main__":
    main()

