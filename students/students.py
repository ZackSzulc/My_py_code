import csv
def main():

    students = []

    with open("students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)

    for student in sorted(students, key=lambda student: student['name']):
        print(f"{student['name']} is in {student['home']}")


if __name__ == "__main__":
    main()



















"""
    number = float(input("Gimme number: "))
    if is_even(number):
        print("yeup. even.")
    else:
        print("nope")
def is_even(num):
    return num %2 ==   0
"""

"""
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
"""