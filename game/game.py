import random
from sys import exit

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

answer = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess == answer:
            print("Just right!")
            #originally used a break statement but check50 just NEEDED the exit :) ... fun
            exit()
        elif guess > answer:
            print("Too large!")
        else:
            print("Too small!")
    except ValueError:
        pass