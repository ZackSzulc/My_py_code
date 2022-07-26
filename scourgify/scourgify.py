from sys import (argv,exit)
import csv
def main():
    length = len(argv)
    if length != 3:
        exit("Incorrect number of arguements.")

    student_list = argv[1] #csv file containing students
    name = argv[2] #this will be the new file name
    find_code(student_list)
    if find_extension(name) != '.csv' or find_extension(student_list) != '.csv':
        exit("Csv files only.")

#sort students from before.csv into a list of dictionaries
    students=[]
    with open (student_list) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last,first = row['name'].split(',')
            student = {"first":first.strip(),"last":last,"house":row["house"]}
            students.append(student)

#make a new file using the student list
    make_file(name,students)


def make_file(name, students):
    details = ['first','last','house']
    with open(f"{name}", "w") as file:
        writer = csv.DictWriter(file, fieldnames=details)
        writer.writeheader()
        for student in students:
            writer.writerow({"first":student['first'], "last":student['last'], "house":student['house']})

def find_extension(file):
    if file.rfind(".") == -1:
        exit(f"{file} is not a file.")
    extension = file[file.rfind("."):]
    return extension

def find_code(code):
    try:
        open(f"{code}")
    except FileNotFoundError:
        exit("File not found.")


if __name__ =="__main__":
    main()