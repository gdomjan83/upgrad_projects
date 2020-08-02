#This is a small text adventure game, where the player can move through different rooms.
#In every room, there is a descripton about the room. You can also move to another room if there is a door.
#To move in directions: W - Move Forward, S - Move Backwards, A - Move Left, D - Move Right, E - Exit Game
print("\nEgy különös hívást kaptál, amelyben egy régi barátod - akiről azt hitted, hogy már régóta halott - egy öreg házhoz invitált.")
#set up rooms
rooms = []
for x in range(6):
    rooms.append([])
    for y in range(6):
        rooms[x].append(None)

rooms[2][0] = ("A ház bejáratánál állsz. Előtted egy hosszú folyosó terül el.", "w")
rooms[0][1] = ("Nincs mit szépíteni rajta, ez a mellékhelyiség. A WC-t már jó ideje nem használták. Elég undorító képet fest.", "d")
rooms[1][1] = ("Ez a szoba a vendégek fogadására szolgált, mielőtt a lakók elköltöztek. Néhány ruhafogas látható a falon, mellettük egy kalaptartó áll a sarokban.", "daw")
rooms[2][1] = ("A folyosón állsz, melytől balra több szoba is található.", "as")
rooms[1][2] = ("A folyosón állsz, ami összeköti az előszobát a többi helyiséggel.", "ws")
rooms[0][3] = ("Egy apró tároló helyiségbe léptél. Az ajtón belülről kaparások nyomai láthatóak. Mintha valaki a kezével próbált volna kiszabadulni a helyiségből.", "d")
rooms[1][3] = ("A nappali, ahol a társasági élet folyt. Néhány kanapé és fotel található a szobában, itt-ott néhány kis asztallal.", "sd")
rooms[2][3] = ("A belső nappali, melyet egy ősrégi kandalló \"ural\". Jó ideje nem gyújthatták már be.", "wa")
rooms[4][3] = ("Ez a szoba szönyű állapotban van. Mindenfelé széttörött bútorok és vakolat darabok hevernek.", "w")
rooms[2][4] = ("Megérkeztél ahhoz a lépcsőhöz, ami az emeletre visz. A lépcsőfokok nyikorognak, jobb ha óvatosan lépkedsz.", "sd")
rooms[3][4] = ("Egy újabb folyosón, mely szemmel láthatóan a hálószobák felé vezet.", "wda")
rooms[4][4] = ("Folyosó végén állsz. Még két szoba nyílik innen. Mindkettő ajtaján furcsa vésetek találhatóak.", "das")
rooms[5][4] = ("A szobában korom sötét van, nem látsz tovább az orrodnál. Fura szagot érzel, és mintha valamiféle éneket hallanál a távolban. Úgy döntesz, hogy követed a hangot.", "a")
rooms[3][5] = ("Benyitsz a szobába, melynek szemközti falán egy vérrel felfestett mosolygó arcot látsz. A festményt látva rossz érzés fog el.", "s")

print(rooms[2][0][0])
#set up player class as the character
class Player():
    def __init__(self, x, y):
        self.x = x  #the position of the player in the rooms
        self.y = y  #the position of the player in the rooms

    def get_direction(self):
        direction = input("=========================\nMerre szeretnél mozogni? (w - ELŐRE, s - HÁTRA, a - BALRA, d - JOBBRA, x - KILÉPÉS) ")
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
            print("Átlépsz a következő helyiségbe.")
            print(rooms[self.x][self.y][0])
            return (self.x, self.y)
        else:
            if direction == "x":
                print("Köszönöm a játékot.")
                return False
            if direction in "wasd":
                print(f"Arra nem tudsz haladni.")
                return True
            else:
                print("Ez nem egy irány.")
                return True
               

player = Player(2, 0) #set player starting position

while True:
    if (player.move(player.get_direction()) == False):
        break
    if (player.x, player.y) == (5, 4):
        print("Folyamatosan a hang irányába haladsz, de mintha sosem kerülnél közelebb hozzá. Egy idő után már nem is vagy tudatában a körülötted lévő dolgoknak,\ncsak haladsz előre, miközben üveges tekintettel bámulsz magad elé. Sosem látnak viszont téged.")
        break