def main():

    #ask question
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").title().strip()
    if answer == "Forty Two" or answer == "Forty-Two" or answer == "42":
        print("Yes")
    else:
        print("No")
main()
