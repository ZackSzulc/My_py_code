import sys
from random import choice
from pyfiglet import Figlet
figlet = Figlet()
args = len(sys.argv)

try:
    #expect 2 arguements
    if args == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font') and (sys.argv[2] in figlet.getFonts()):
        inp = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(inp))
        #Next line not necessary, just to output exit code 0
        sys.exit()


    #not enough arguements? expect zero
    elif args == 1:
        inp = input("Input: ")
        fontChoice = choice(figlet.getFonts())
        figlet.setFont(font=fontChoice)
        print(figlet.renderText(inp))
        #Next line not necessary, just to output exit code 0
        sys.exit()


    #any other arguement combination raise an error
    else:
        raise IndexError


except IndexError:
    sys.exit("Invalid usage")