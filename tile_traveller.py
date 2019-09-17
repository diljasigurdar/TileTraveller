# 1. A game where a player starts in tile (1,1)
# 2. Each move the player selects the program should print the players travel options
# 3. Before the enters a direction he can see what directions he can choose
# 4. Directions North (up), South (down), West (left), East (right)
# 6. Player can only go where he wants if the wall is open
# 7. If the wall is closed then it should print out: "not a valid direction!" and the player can try again
# 8. When the player gets to tile (3,1) then the program should print out victory!

START_X = 1
START_Y = 1

tile = (START_X, START_Y)

valid_directions = ""

def directions(N, S, E ,W):
    if 

def tiles(x, y): 
    X_current = 1
    Y_current = 1
    if tile == (1, 1):
        valid direction = (N)
    elif tile == (1, 2):
        valid_directions = (N, E, S)
    elif tile == (2, 2):
        valid_directions = (S, W)
    elif tile == (2, 1):
        valid_directions = (N)
    elif tile == (1, 3):
        valid_directions = (S, E)
    elif tile == (2, 3):
        valid_directions = (W, E)
    elif tile == (3, 3):
        valid_directions = (W, S)
    elif tile == (3, 2):
        valid_directions = (N, S)
    else:
        print("Victory!")
        break


def invalid():

def print_directions(START_X, START_Y):
    print("You can travel: ", valid_directions)



direction = 
print("You can travel: ", direction)
N_S_W_E = input("Direction: ")


