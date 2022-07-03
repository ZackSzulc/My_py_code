#still could be much better
def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    int_list = "0123456789"
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~+=|` '''
    flag = False

    for punc in s:
        if punc in punctuations:
            return False

    if 2 <= len(s) <= 6 and s[0:2] not in int_list:
        flag = True
        for c in s:
            if c == "0":
                return False
            if c in int_list:
                for i in s[s.index(c):len(s)]:
                    if i not in int_list:
                        return False
                break
    return flag
if __name__ == "__main__":
    main()