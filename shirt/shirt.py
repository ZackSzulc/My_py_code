from sys import (argv,exit)
from PIL import (Image,ImageOps)

def main():
    length = len(argv)
    if length != 3:
        exit("Incorrect number of cli arguements.")

    input = argv[1] #path to image
    output = argv[2] #path to image
    #now, to  validate the paths
    find_code(input)
    if find_extension(input) and find_extension(output) not in [".jpg", ".png", ".jpeg"]:
        exit("Wrong file type(s). JPG/JPEG and PNG only.")
    if find_extension(input) != find_extension(output):
        exit("The two files must have the same extension.")

    #these next 6 lines are the main objective of the code:
    #Crop the image to the size of the shirt and paste the shirt. Very simple
    shirt = Image.open("shirt.png")
    size=shirt.size
    with Image.open(input) as image:
        image = ImageOps.fit(image,size)
        image.paste(shirt,shirt)
        image.save(output)

def find_extension(file):
    if file.rfind(".") == -1:
        exit(f"{file} is not a file.")
    extension = file[file.rfind("."):]
    return extension

def find_code(code):
    try:
        open(f"{code}")
    except FileNotFoundError:
        exit("File not found.")


if __name__ == "__main__":
    main()