def main():
    get_string = input("camelCase: ")
    print("snake_case: ", end="")

    #become new string
    for c in get_string:
        if c.isupper():
            #replace uppercase letter with an _ and make it lowercase
            print("_",c.lower(),sep="",end="")
        else:
            print(c, end="")
    #make terminal look pretty
    print()

main()