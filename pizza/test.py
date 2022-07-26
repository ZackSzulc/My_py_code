import csv
from tabulate import tabulate
sicilian = []
with open("sicilian.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        sicilian.append (row)