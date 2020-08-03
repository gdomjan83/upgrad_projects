#milyen típusú kockát szeretnél dobni
#hány darab kockát dobsz
#dobás
#dobás kinyomtatása
#kérdés, hogy szeretnél-e újra dobni, vagy másik kockát használni
from random import randint

def roll_dice(sides, dices):
    total = 0
    i = 0
    while i < dices:
        roll = randint(1, sides)
        total += roll
        print(f"A dobásod eredménye: {roll}.")
        i += 1
    return total

while True:
    try:
        print("=================")
        sides = int(input("Hány oldalú kockával szeretnél dobni? (6, 8, 10, 20, 100) "))
        if sides not in [6, 8, 10 , 20, 100]:
            print("Csak 6, 8, 10, 20 és 100 oldalú kockák közül választhatsz.")
            continue
        dices = int(input("Hány kockával szeretnél dobni? "))
        print("=================\nEredmény:")
        print(f"Összesen: {roll_dice(sides, dices)}")
        retry = input("Szeretnél újra dobni? (i/n) ")
        if (retry == "i"):
            continue
        else:
            break
    except ValueError:
        print("Ez nem egy szám.")