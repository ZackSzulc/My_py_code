def main():
    while True:
        inp = input("Fraction: ")
        try:
            perc = convert(inp)
            assert type(perc) == int
            break
        except (ValueError, ZeroDivisionError, AssertionError):
            pass
    print(gauge(perc))


def convert(fraction):
    x,y= fraction.split("/")
    x,y = int(x), int(y)
    if(x <= y and x >= 0 and y > 0):
        return int(round((x/y)*100, 0))
    elif y == 0:
        raise ZeroDivisionError
    else:
        raise ValueError

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()