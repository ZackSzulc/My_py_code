#define variables and catch errors
while True:
    try:
        x,y= input("Fraction: ").split("/")
        x,y = int(x), int(y)
        if(x <= y):
            percentage = int(round((x/y)*100, 0))
            break
    except (ValueError, ZeroDivisionError):
        pass


if(percentage <= 1):
    print("E")
elif(percentage >= 99):
    print("F")
else:
    print(percentage,"%", sep="")