counter = 0
while True:
    try:
        x = float(input("What is x? "))
        y = float(input("What is y? "))
        break
    except ValueError:
        pass

while counter == 0:
    operator = input("Would you like to add, subtract, multiply or divide? ").lower().strip()
    if operator == 'add':
        z = x+y
        print(x, "plus", y, "is equal to", z)
        counter = 1
    elif operator == 'subtract':
        z = x-y
        print(x, "minus", y, "is equal to", z)
        counter = 1
    elif operator == 'multiply':
        z = x*y
        print(x, "times", y, "is equal to", z)
        counter = 1
    elif operator == 'divide':
        z = x/y
        print(x, "divded by", y, "is equal to", z)
        counter = 1
    else:
        print("That's not an option, try again.")
print("Thanks for using my new calculator. Easy, Simple, Boring. You're welcome, boring person.")
