names = []
string = ""
while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        break
for name in names:
    if name != names[len(names)-1]:
        string += ' ' + name + ','
    else:
        string += " and " + name
if len(names) == 1:
    print("Adieu, adieu, to " + names[0])
elif len(names) == 2:
    print("Adieu, adieu, to " + names[0] + " and " + names[1])
else:
    print("Adieu, adieu, to" + string)