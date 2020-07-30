#This is a small text adventure game, where the player can move through different rooms.
#In every room, there is a descripton about the room. You can also move to another room if there is a door.
#To move in directions: W - Move Forward, S - Move Backwards, A - Move Left, D - Move Right, E - Exit Game

#set up rooms
rooms = []
for x in range(6):
    rooms.append([])
    for y in range(6):
        rooms[x].append(None)

rooms[2][0] = ("Room20", "w")
rooms[0][1] = ("Room01", "d")
rooms[1][1] = ("Room11", "daw")
rooms[2][1] = ("Room21", "as")
rooms[1][2] = ("Room12", "ws")
rooms[0][3] = ("Room03", "d")
rooms[1][3] = ("Room13", "sd")
rooms[2][3] = ("Room23", "wa")
rooms[4][3] = ("Room43", "w")
rooms[2][4] = ("Room24", "sd")
rooms[3][4] = ("Room34", "wda")
rooms[4][4] = ("Room44", "das")
rooms[5][4] = ("Room54", "a")
rooms[3][5] = ("Room35", "s")

print(rooms[2][0][0])
#set up player class as the character
class Player():
    def __init__(self, x, y):
        self.x = x  #the position of the player in the rooms
        self.y = y  #the position of the player in the rooms

    def get_direction(self):
        direction = input("=========================\nWhere do you want to move? (w - UP, s - DOWN, a - LEFT, d - RIGHT, x - EXIT GAME) Enter direction: ")
        print("=========================")
        return direction

    def move(self, direction):
        if direction in rooms[self.x][self.y][1]:
            if direction == "w":
                self.y += 1
            elif direction == "s":
                self.y -= 1
            elif direction == "a":
                self.x -= 1
            elif direction == "d":
                self.x += 1
            print("You step through the door to the next room.")
            print(rooms[self.x][self.y][0])
            return (self.x, self.y)
        else:
            if direction == "x":
                return False
            print(f"You can't move in that direction.\n{rooms[self.x][self.y][0]}")      

player = Player(2, 0) #set player starting position

while True:
    if (player.move(player.get_direction()) == False):
        break
    elif (player.move(player.get_direction()) == (3, 5)):
        print("Congratulations, you reached the end of the game.")
        break