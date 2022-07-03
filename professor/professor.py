from random import randint


def main():
    level = get_level()
    correct = 0
    for problem in range(10):
        x,y = generate_integer(level),generate_integer(level)
        answer = x + y
        guess_counter = 0
        while guess_counter < 3:
            try:
                print(f"{x} + {y} = ", end="")
                guess = int(input())
                guess_counter += 1
                if guess == answer:
                    correct += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
                guess_counter += 1
                pass
        if guess_counter == 3:
             print(f"{x} + {y} =", answer)

    print("Score:", correct)




def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        integer = randint(0, 9)
    elif level == 2:
        integer = randint(10, 99)
    else:
        integer = randint(100, 999)
    return integer


if __name__ == "__main__":
    main()