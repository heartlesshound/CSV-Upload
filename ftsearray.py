import csv

with open('ftse100.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

print(data)
