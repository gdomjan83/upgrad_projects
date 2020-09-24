from os import path
import print_db, add_data, create_db

print("""
--------CONTACT BOOK--------\n

1) Add new contact.\n
2) Show contacts.\n
3) Exit program.
""")

if not path.exists("contacts.db"):
    create_db.main()

while True:
    userInput = input("Choose option (1, 2, 3): \n")

    if (userInput not in ["1", "2", "3"]):
        print("Please enter a valid option! (1, 2, 3)\n")
    else:
        break

if userInput == "1":
    while True:
        add_data.main()
        while True:
            userInput2 = input("\nDo you want to add another contact? (y/n)")
            if (userInput2 not in ["y", "n"]):
                print("Please enter y or n!\n")
            if (userInput2 == "y"):
                break
            if (userInput2 == "n"):
                exit()
elif userInput == "2":
    print_db.main()
elif userInput == "3":
    print("\nClosing program.\n")