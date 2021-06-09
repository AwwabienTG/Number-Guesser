import random
number = random.randint(1,100)
print(number)
print("Hello to Awwabs number guesser!\nGuess the number (1-100): ")
i = int(input())
not_guessed = True
diffrence = number - i

while not_guessed == True:
    if abs(diffrence) <= 10 and i != number:
        print("\nClose, but wrong guess. Try again: ")
        i = int(input())
        diffrence = number - i
    elif i == number:
        print("\nCorrect guess! The number was: ", number)
        not_guessed = False
    else:
        print("\nWrong guess! Try again: ")
        i = int(input())
        diffrence = number - i
