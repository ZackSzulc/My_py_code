#simplified a bit; still could be much better
def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    int_list = "0123456789"
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~+=|` '''

    for punc in s:
        if punc in punctuations:
            return False

    if 2 <= len(s) <= 6 and s[0] not in int_list and s[1] not in int_list:
        for c in s:
            if c == "0":
                return False
            if c in int_list:
                for i in s[s.index(c): ]:
                    if i not in int_list:
                        return False
                return True
        return True

if __name__ == "__main__":
    main()