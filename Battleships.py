
import time
from datetime import datetime
from random import randint

# importing necessary functions
now = datetime.now()
print "Date: %02d/%02d/%02d" % (now.day, now.month, now.year)
print "Time: %02d:%02d" % (now.hour, now.minute)
# displaying time
print "---Once typing anything make sure you hit enter to continue---"
player_name = "a"
player_name = raw_input("Player Name: ")
player_name = player_name.upper()
# asking for the player's name

alliance = raw_input("Pirates or Ninjas? ")
if alliance != 'Pirates' and alliance != 'pirates':
    time.sleep(0.5)
    alliance = raw_input("Let's try that again, Pirates or Ninjas? ")
    if alliance != 'Pirates' and alliance != 'pirates':
        time.sleep(0.5)
        alliance = raw_input("I think you misunderstand, ninjas do not sail boats. Again, Pirates or Ninjas? ")
        if alliance != 'Pirates' and alliance != 'pirates':
            time.sleep(0.5)
            alliance = raw_input(
                "If you think you can be a ninja on a pirate ship you can go play another game, but I know you want to play this game so I'll ask again. Pirates or Ninjas? ")
            if alliance != 'Pirates' and alliance != 'pirates':
                time.sleep(0.5)
                alliance = raw_input(
                    "You are just doing this to annoy me. Please stop and just be a pirate so you can play this game. For the LAST TIME, Pirates or Ninjas!? ")
                if alliance != 'Pirates' and alliance != 'pirates':
                    time.sleep(0.5)
                    alliance = raw_input(
                        "Please, I just want to take a computer science degree and finish my EPQ so stop messing about. Just pick Pirates. Pirates or Ninjas? ")
                    if alliance != 'Pirates' and alliance != 'pirates':
                        time.sleep(0.5)
                        alliance = raw_input("Pirates or Pirates? ")
                        if alliance != 'Pirates' and alliance != 'pirates':
                            print "Ok, you had your chance, I'm sinking your ship. "
                            time.sleep(1)
                            print """
                                       ___________
                                     _|  %s
                                    | |___________
                                 ___[_]___ 
                                 \  | |   )                                     
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^)^|^|^^^^)^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^           
                                 /__| |___)           
            <><     ___[_]___    ___| |___    ___[_]___            ><>
                    \  | |   )   \  | |   )   \  | |   )
     <><             ) | |    )   ) | |    )   ) | |    )     <><
                    /__| |___)   /__| |___)   /__| |___)
                       | |    <><   | |          | |            ><>
               ________+_+__[o]_[o]_+_+_____[o]__+_+__[o]__
               \     ____    ____    ____    ____    ____  |
                \    :[]::[]::[]::[]::[]::[]::[]::[]::[]:  |\\          ><>
       <><       \                                         | \\
                  \________________________________________|__\\
""" % player_name
                            print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
# printing main visual

# asking player to choose the correct alliance
while alliance != 'Pirates' and alliance != 'pirates':
    time.sleep(1)


instructions = raw_input("Do you need instructions on how to play Battleships? Yes or No? ")
if instructions == "Yes" or instructions == "yes" or instructions == "y" or instructions == "Y":
    print "Welcome to Battleships, as captain of the ship your goal is to correctly guess the placement of the opponent's battleships."
    cont1 = raw_input("Press Enter to continue")
    if cont1 == "":
        print "Firstly you will need to position your own ship on the board, try not to think too hard about where to place it."
        cont2 = raw_input("Press Enter to continue")
        if cont2 == "":
            print "In this game you will be playing against a computer trying to guess the placement of your own battleship. The grid is 10 horisontal spaces by 8 vertical spaces, so only guess in this given range."
            cont3 = raw_input("Press Enter to continue")
            if cont3 == "":
                print "You will win by correctly choosing the coordinates of the opponent's ships before they correctly guess the placement of yours."
                cont4 = raw_input("Press Enter to continue")
                if cont4 == "":
                    print "Good it looks like you are ready, have fun."

board = []
pboard = []
# creates blank canvases for the boards
for x in range(8):
    pboard.append(["O"] * 10)
for x in range(8):
    board.append(["O"] * 10)


# stores 0000000000 on 8 seperate rows of each board
def print_board(board):
    for row in board:
        print " ".join(row)


# makes the board look nicer by adding spacing gaps between each 0
# print_board(board)
# print " 																																														"
# enemy board printing phase however was removed because it was unnecessary
def place_row(raw_input):
    raw_input = int(raw_input)
    if raw_input > 0 or raw_input < 9:
        return raw_input
    else:
        print "That placement is not even in the ocean. Try that again."


def place_col(raw_input):
    raw_input = int(raw_input)
    if raw_input > 0 or raw_input < 11:
        return raw_input
    else:
        print "That placement is not even in the ocean. Try that again."


# defining the placement functions of the player's ship
print """
                                       ___________
                                     _|  %s
                                    | |___________
                                 ___[_]___ 
                                 \  | |   )                                     
                                  ) | |    )           
                                 /__| |___)           
                    ___[_]___    ___| |___    ___[_]___
                    \  | |   )   \  | |   )   \  | |   )
                     ) | |    )   ) | |    )   ) | |    )
                    /__| |___)   /__| |___)   /__| |___)
                       | |          | |          | |
               ________+_+__[o]_[o]_+_+_____[o]__+_+__[o]__
               \     ____    ____    ____    ____    ____  |
                \    :[]::[]::[]::[]::[]::[]::[]::[]::[]:  |\\
^^^^^^^^^^^^^^^^^\^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|^\^^^^^^^^^^^^   
                  \________________________________________|__\\
""" % player_name
# printing main visual
time.sleep(2)
# waiting 3 seconds
print "                                                                                                    "
place_col = place_col(raw_input("Place ship column (range 1-10): "))
if place_col <= 10 and place_col >= 1:
    pass
else:
    print "We can't possibly sail to that longitude"
    place_col = (int(raw_input(str("Place ship column (range 1-10): "))))
place_row = place_row(raw_input("Place ship row (range 1-8): "))
if place_row <= 8 and place_row >= 1:
    pass
else:
    print "We can't possibly sail to that latitude"
    place_row = (int(raw_input(str("Place ship row (range 1-8): "))))
pboard[8 - place_row][place_col - 1] = "#"
print " 																																														"
print_board(pboard)

player_name = player_name.lower()
# places one ship on the player's board
time.sleep(1)
# waiting 3 seconds
def random_row(board):
    return randint(0, 8)


def random_col(board):
    return randint(0, 10)


ship_row = random_row(board)
ship_col = random_col(board)
# chooses a random ship placement for the enemy's board
print "Enemy ship placement: (%s,%s)" % (ship_row, ship_col)
print " 																																														"


# prints this location for debugging purposes
def random_attack_row(board):
    return randint(1, 8)

def random_attack_col(board):
    return randint(1, 10)

def ra_speech(num):
    if num == 1:
        print "We missed! Load up another cannon!"
    elif num == 2:
        print "They out manoeuvred us! Rotate the ship so we can get another shot!"
    elif num == 3:
        print "That wasn't even close! They swept right past us!"
    elif num == 4:
        print "We hit their ship but only caused minimal damage captain"


def en_speech(num):
    if num == 1:
        print "Prepare for impact!"
    elif num == 2:
        print "Looks like they're lining up a shot!"
    elif num == 3:
        print "This ship is too close! Light the grenados!"
    elif num == 4:
        print "Enemy ship closing in quick at %s 'O clock!" % str(randint(1, 12))


def ms_speech(num):
    if num == 1:
        print "That was close!"
    elif num == 2:
        print "Quickly now let's line up another shot!"
    elif num == 3:
        print "Powder the cannons!"
    elif num == 4:
        print "Now's our chance! Attack!"


win = 0
enemywin = 0
turn = 1
loopx = False
# setting variables
if enemywin < 1 and win < 1:
    if turn == 1:
        loopx = False
    else:
        loopx = True

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
    	time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
    	time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
    	time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
    	time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
    	time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
    	time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
    	time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
    	time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
    	time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
    	time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
    	time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
    	time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
    	time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
    	time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

if loopx == False:
    print "                                                                                                    "
    print "Turn %s" % turn
    print "                                                                                                    "
    guess_col = int(raw_input("Guess Enemy Col (range 1-10): "))
    guess_row = int(raw_input("Guess Enemy Row (range 1-8): "))
    print "                                                                                                    "
    time.sleep(0.5)
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the enemy's battleship!"
        print "                                                                                                    "
        print  """|---+---+---+---+---+---+---|
 												| G | A | M | E | W | I | N |
 												|---+---+---+---+---+---+---|"""
        time.sleep(100)
        win = 1
    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 10):
            print "It's not possible to fire our cannons that far!"
            print "                                                                                                    "
            loopx = False
        elif (board[8 - guess_row][guess_col - 1] == "X"):
            print "There's no point firing in the same place captain %s." % player_name
            print "                                                                                                    "
            loopx = False
        else:
            ra_speech(randint(1, 4))
            print "                                                                                                    "
            board[8 - guess_row][guess_col - 1] = "X"
            print_board(board)
            turn += 1
            loopx = True
            print "                                                                                                    "
            time.sleep(1)
            en_speech(randint(1, 4))
            time.sleep(1)
            print "                                                                                                    "
# player turn over
time.sleep(0.5)
# computer turn commences
if loopx == True:
    rarow = random_attack_row(pboard)
    racol = random_attack_col(pboard)
    time.sleep(0.5)
    if rarow == place_row and racol == place_col:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(0.5)
        print "We're going down! It was nice knowing you, I salute you captiain s%" % player_name
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "@"
        print_board(pboard)
        enemywin += 1
        print "                                                                                                    "
        print """ 		|---+---+---+---+---+---+---+---|
 		| G | A | M | E | O | V | E | R |
 		|---+---+---+---+---+---+---+---|"""
        time.sleep(100)
    elif (pboard[8 - rarow][racol - 1] == "X"):
        loopx = True
    else:
        print "Enemy attacks at: (%s,%s)" % (int(racol), int(rarow))
        print "                                                                                                    "
        time.sleep(1)
        print "                                                                                                    "
        pboard[8 - rarow][racol - 1] = "X"
        time.sleep(1)
        print_board(pboard)
        print "                                                                                                    "
        ms_speech(randint(1, 4))
        time.sleep(1)
        loopx = False

#84 itterations
