import random

fruits = ["APPLE", "BANANA", "ORANGE", "GRAPES", "KIWI", "MELON", "CHERRY", "PEACH", "MANGO", "STRAWBERRY"]
things = ["PHONE", "BOOK", "CHAIR", "TABLE", "CAR", "HOUSE", "DOOR", "KEY", "LAMP", "CLOCK"]
colours = ["RED", "GREEN", "BLUE", "YELLOW", "ORANGE", "PURPLE", "PINK", "BLACK", "WHITE", "BROWN"]
profession = ["DOCTOR", "TEACHER", "NURSE", "ENGINEER", "LAWYER", "WRITER", "POLICE", "CHEF", "SINGER", "ARTIST"]

lives = 6
wrg_ans = 0

print("Welcome to Hangman!\nCan you guess the word before it's too late?")
print("\t\tNow you can choose the CATEGORY for the game\n\t\t\t\t1. Fruits\n\t\t\t\t2. Things\n\t\t\t\t3. Colours\n\t\t\t\t4. Profession")
lw = int(input("Enter the number of the category:"))

if lw == 1:
    lw = fruits
elif lw == 2:
    lw = things
elif lw == 3:
    lw = colours
elif lw == 4:
    lw = profession
else:
    print("The input is not valid.")

print("you have 6 chances to guess the word...")

# Choosing random words from lw
word = random.choice(lw)
answer = ["_ "] * len(word)


while True:
    print(" ".join(answer))
    guess = input("Guess a letter: ").upper()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                answer[i] = guess
    else:
        lives -= 1
        print(f"Oh no.. Incorrect Guess. You still have {lives} lives left")

    if "_ " not in answer or word == answer:
        print(" ".join(answer))
        print("YESSSS!!!! You got it right.\nCONGRATULATIONS!")
        break

    if lives == 0:
        print(f"Looks like you're all hung up on this word! Better luck next time.\nThe correct answer was {word}")
        break
