#REVISED after test assignment. Looks cleaner and is more concise
def main():
    string = input("Input: ")
    print(shorten(string))

def shorten(word):
    vowels = 'aeiouAEIOU'
    for c in word:
        if c in vowels:
            word = word.replace(c,'')
    return word


if __name__ == "__main__":
    main()