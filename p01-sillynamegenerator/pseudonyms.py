"""Genetare funny names by randomly combining separate lists"""
from enum import Enum
import random
import sys

class Bcolrs(Enum):
    """Enum to define terminal output text color"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    """Choose names at random from 2 tuples of names and print to screen"""
    print("\nWelcome to the Psych Sidekick Name Picker. \n")
    first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
             "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite'",
             'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
             'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread',
             'Crab Meat', 'Crapps', 'Dark Skies', 'Dennis Clawhammer',
             'Dicman', 'Elphonso', 'Fancypants', 'Figgs', 'Foncy', 'Gootsy',
             'Greasy Jim', 'Huckleberry', 'Huggy', 'Ignatious', 'Jimbo',
             "Joe 'Pottin Soil'", 'Johnny', 'Lemongrass', 'Lil Debil',
             'Longbranch', '"Lunch Money"', 'Mergatroid', '"Mr Peabody"',
             'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine', 'Pennywhistle',
             'Pitchfork Ben', 'Potato Bug', 'Pushmeet', 'Rock Candy',
             'Schlomo', 'Scratchensniff', 'Scut', "Sid 'The Squirts'",
             'Skidmark', 'Slaps', 'Snakes', 'Snoobs', 'Snorki', 'Soupcan Sam',
             'Spitzitout', 'Squids', 'Stinky', 'Storyboard', 'Sweet Tea',
             'TeeTee', 'Wheezy Joe', "Winston 'Jazz Hands'", 'Worms')

    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
             'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
             'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple',
             'Goodensmith', 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag',
             'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins',
             'Jingley-Schmidt', 'Johnson', 'Kingfish', 'Listenbee', "M'Bembo",
             'McFadden', 'Moonshine', 'Nettles', 'Noseworthy', 'Olivetti',
             'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler', 'Pealike',
             'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton', 'Porkins',
             'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal', 'Rubbins',
             'Sackrider', 'Snuggleshine', 'Splern', 'Stevens', 'Stroganoff',
             'Sugar-Gold', 'Swackhamer', 'Tippins', 'Turnipseed',
             'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax', 'Weiners',
             'Whipkey','Wigglesworth', 'Wimplesnatch', 'Winterkorn',
             'Woolysocks')
    print(first, last)

    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)

        # Use class enum to set colors in the output terminal
        print(
        f"\n{Bcolrs.WARNING.value}{first_name} {last_name}{Bcolrs.ENDC.value}\n",
        file=sys.stderr)

        response = input("\nWanna play More y/n?\n")

        if response.lower() == "n":
            break

if __name__ == "__main__":
    main()
