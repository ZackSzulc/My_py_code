from sys import (argv,exit)
def main():
    length = len(argv)
    if length < 2:
        exit("Too few arguements.")
    if length > 2:
        exit("Too many arguements.")

    file = argv[1]
    if find_extension(file) != ".py":
        exit("That's not a python file.")
    find_code(file)
    print(f"There is {count_lines(file)} lines of code")



def find_code(code):
    try:
        open(f"{code}")
    except FileNotFoundError:
        exit("File not found.")

def find_extension(file):
    if file.rfind(".") == -1:
        exit("That's not a file.")
    extension = file[file.rfind("."):]
    return extension

def count_lines(code):
    counter = 0
    with open(code) as file:
        for line in file:
#not including multiline comments that use """ or '''
            if line.strip() != "" and line.strip()[0] != "#":
                counter+=1
    return counter


if __name__ == "__main__":
    main()
