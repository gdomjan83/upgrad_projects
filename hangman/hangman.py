from random import choice #hogy tudjunk véletlenszerűen egy szót választani

#a txt fájlból beolvassuk a szavakat egy listbe, majd abból fogunk választani kitalálandó szót
with (open("szavak.txt", "r")) as file:
    word_list = []
    for line in file:
        word_list.append(line.replace("\n", ""))

#a kitalálandó szó, véletlenszerűen választva a listából
word = choice(word_list)

#ennyiszer lehet majd hibázni a találgatás során
tries = len(word)



