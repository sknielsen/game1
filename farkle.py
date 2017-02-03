import random

class Die(object):

    def __init__(self, number, sides=6):
        self.number = number
        self.sides = sides
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

    def __str__(self):
        return self._value_to_str[self.value] % self.number

die1 = Die(1)
die2 = Die(2)
die3 = Die(3)
die4 = Die(4)
die5 = Die(5)
die6 = Die(6)

def begin_game():
    players = int(raw_input('Hello and welcome to Farkle! How many players are there? '))
    players = range(1, (players + 1))
    return players

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

def player_turn(players):
    still_playing = True
    while still_playing == True:
        for player in players:
            print("It is player number %i's turn!") % (player)
            begin_turn()
            kept_dice = raw_input("Which number dice would you like to keep? (ie '1 3 4' or 'none') ")
            if kept_dice.lower() == 'none':
                print('FARKLE!')
            else:
                kept_dice = map(int, kept_dice.split())




def main():
    player_turn(begin_game())

if __name__ == '__main__':
    main()

