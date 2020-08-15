from random import choice #hogy tudjunk véletlenszerűen egy szót választani

#a txt fájlból beolvassuk a szavakat egy listbe, majd abból fogunk választani kitalálandó szót
with (open("szavak.txt", "r")) as file:
    word_list = []
    for line in file:
        word_list.append(line.replace("\n", ""))

#a kitalálandó szó, véletlenszerűen választva a listából
word = choice(word_list)

#a kitalálandó szó betünként eltárolva, mellette False hogy még nem találtuk ki a betűt
word_data = [[i, False] for i in word]

#a szavak megjelenítése, kicsillagozva a még ki nem talált betűket
def show_letters(word_data):
    text = ""
    for i in word_data:
        if i[1] == True:
            text += i[0]
        else:
            text += "*"
    return text

#ennyiszer lehet majd hibázni a találgatás során
tries = 10

while True:
    print(f"======================\nWord: {show_letters(word_data)}\n(You have {tries} tries left. - Press '0' to Exit Game)\n======================")
    guess = input("Guess a letter: ")
    if guess == "0": #0-val ki tudunk lépni a játékból
        break
    if len(guess) != 1: #ha nem pont egy betűt adunk meg, akkor az nem érvényes
        print("Only guess one letter!")
        continue
    if guess not in word:
        tries -= 1
        print("======================\nWrong guess.")
        if tries == 0:
            print("Game over.")
            break
        continue
    else:
        won = True
        for i in word_data:
            if i[0] == guess:
                i[1] = True
            if i[1] == False:
                won = False
        if won:
            print("======================\nCongratulations! You won the game!")
            break
