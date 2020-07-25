#This is a small guessing game. You have to guess a number between 1 and 100. If you can't guess it, you will be given hints about the number.

from random import randint

number = randint(1, 100)
print("=========================\nI thought of a number between 1 and 100. Can you guess this number?\n=========================")

counter = 1
hint = 0
won = False
even = False
div3 = False
div5 = False
if (number % 2 == 0):
    even = True

if (number % 3 == 0):
    div3 = True

if (number % 5 == 0):
    div5 = True

def check_prime(number):
	is_prime = True
	if number == 1:
		is_prime = False
		return is_prime
	for i in range(2, number):
		if number % i == 0:
			is_prime = False
			return is_prime
	return is_prime
        
prime = check_prime(number)

def hints(hint):
    if hint == 1:
        return "I'll give you more hints next time."
    if hint == 2:
        if prime:
            return "Also, it is a prime number."
        else:
            return "Also, it is not a prime number."        
    if hint == 3:
        if even:
            return "Also, it is a even number."
        else:
            return "Also, it is an odd number."
    if hint == 4:
        if div3:
            return "Also, it is dividable by 3."
        else:
            return "Also, it is not dividable by 3."
    if hint == 5:
        if div5:
            return "Also, it is dividable by 5."
        else:
            return "Also, it is not dividable by 5."
    else:
        return "No more hints I'm afraid."

def check_guess(guess):
    global counter, won, hint
    if guess == number:
        won = True
        return print(f"===========================\nCongratulations, you guessed it right! You tried {counter} times.\n===========================")
    if guess < number:
        counter += 1
        hint += 1
        return print(f"===========================\nNope. My number is bigger than that. {hints(hint)}\n===========================")
    if guess > number:
        counter += 1
        hint += 1
        return print(f"===========================\nNope. My number is smaller than that. {hints(hint)}\n===========================")

while not won:
    try:
        guess = input("My guess is: ")
        if guess == "":
            print("=====================\nSee you later.")
            break
        else:
            guess = int(guess)
        check_guess(guess)
    except ValueError:
        print("That is not a number.")


