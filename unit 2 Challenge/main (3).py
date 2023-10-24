'''Implement a class called player that represent a cricket player.The player class should have a 
method called play() which prints "the player is playing" cricket.
derive two class to print "batsman is batting" and "bowler is bowlin", respectively. write a program to create objects of both the
batsman and bowler classes and call the play() method for each objects.'''

# Define the base class player 
class Player:
    def play(self):
        print("The player is playing cricket.")

# Define the derived class batsman
class Batsman(Player):
    def play(self):
     print("The batsman is batting.")

# Define the derived class bowler
class Bowler(Player):
    def play(self):
     print("The bowler is bowling.")

# Create objects of batsman and bowler classes

batsman = Batsman()
bowler = Bowler()

# Call the play() method for each objects

batsman.play()
bowler.play()
