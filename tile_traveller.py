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

X_current = 1
Y_current = 1

N = "n"
S = "s"
E = "e"
W = "w"

def tiles(x, y): 
    if tile == (1, 1):
        valid_directions = "n"
    elif tile == (1, 2):
        valid_directions = "nes"
    elif tile == (2, 2):
        valid_directions = "sw"
    elif tile == (2, 1):
        valid_directions = "n"
    elif tile == (1, 3):
        valid_directions = "se"
    elif tile == (2, 3):
        valid_directions = "we"
    elif tile == (3, 3):
        valid_directions = "ws"
    elif tile == (3, 2):
        valid_directions = "ns"
    else:
        print("Victory!")
    return valid_directions

valid_directions = tiles(X_current, Y_current)


def directions(x,y):
    while 1 <= x <= 3 and 1 <= y <= 3:
        if input_direction == "n" or input_direction == "N":
            y += 1
        elif input_direction == "s" or input_direction == "S":
            y -= 1
        elif input_direction == "w" or input_direction == "W":
            x -= 1
        elif input_direction == "e" or input_direction == "E":
            x += 1
    return(x,y)



for ch in valid_directions:
    if ch == N:
        print("You can travel: ", valid_directions)
    elif ch == S:
        print("You can travel: ", valid_directions)
    elif ch == W:
        print("You can travel: ", valid_directions)
    elif ch == E:
        print("You can travel: ", valid_directions)

print_direction = directions(input_direction)  
input_direction = input("Direction: ")






