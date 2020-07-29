#This is a small text adventure game, where the player can move through different rooms.
#In every room, there is a descripton about the room. You can also move to another room if there is a door.
#To move in directions: W - Move Forward, S - Move Backwards, A - Move Left, D - Move Right, E - Exit Game

#set up rooms
rooms = []
for x in range(6):
    rooms.append([])
    for y in range(6):
        rooms[x].append(None)

rooms[2][0] = ("Room20", "u")
rooms[0][1] = ("Room01", "r")
rooms[1][1] = ("Room11", "rlu")
rooms[2][1] = ("Room21", "ld")
rooms[1][2] = ("Room12", "ud")
rooms[0][3] = ("Room03", "r")
rooms[1][3] = ("Room13", "dl")
rooms[2][3] = ("Room23", "ur")
rooms[4][3] = ("Room43", "u")
rooms[2][4] = ("Room24", "dr")
rooms[3][4] = ("Room34", "url")
rooms[4][4] = ("Room44", "lrd")
rooms[5][4] = ("Room54", "l")
rooms[3][5] = ("Room35", "d")

#set up player class as the character
class Player():
    def __init__(self, x, y):
        self.x = x  #the position of the player in the rooms
        self.y = y  #the position of the player in the rooms

    def get_direction(self):
        direction = input("=========================\nWhere do you want to move? (w - UP, s - DOWN, a - LEFT, d - RIGHT\n=========================")
        if direction in rooms[self.x][self.y][1]:
            return direction
        else:
            print("You can't move in that direction.")


    def move(self, direction):
        if direction == "w":
            self.y += 1
        elif direction == "s":
            self.y -= 1
        elif direction == "a":
            self.x -= 1
        elif direction == "d":
            self.x += 1
        


you = Player(2, 0)







