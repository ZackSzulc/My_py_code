def main():
    x, y, z = input("Expression: ").split(" ")
    x = int(x)
    z = int(z)
    if y == "+":
        answer = float(x + z)
    if y == "-":
        answer = float(x - z)
    if y == "*":
        answer = float(x * z)
    if y == "/":
        answer = float(x / z)
    print(round(answer, 1))
main()