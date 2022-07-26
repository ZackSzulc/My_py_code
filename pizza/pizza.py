from sys import (exit, argv)
from tabulate import tabulate
import csv

##########################################
#Copied from lines.py. Would've imported but check50 didn't like it.
def find_code(code):
    try:
        open(f"{code}")
    except FileNotFoundError:
        exit("File not found.")

def find_extension(file):
    if file.rfind(".") == -1:
        exit("That's not a file.")
    extension = file[file.rfind("."):]
    return extension
##########################################

#check length
length = len(argv)
if length < 2:
    exit("Too few arguements.")
if length > 2:
    exit("Too many arguements.")

#check code existence and extension
code = argv[1]
if find_code(code) == -1:
    exit("File not found")
if find_extension(code) != '.csv':
    exit("That's not a CSV file")

#create iterable for tabulate
list = []
with open(code) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        list.append(row)

#separate header from rest of file
header = list[0]
list = list[1: ]

print(tabulate(list, header, tablefmt='grid'))