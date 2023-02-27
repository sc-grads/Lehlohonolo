import csv

with open('airtravel.csv', 'r') as f:
    reader = csv.reader(f)
    #next(reader)
    #Use this if you wanna skip header
    for row in reader:
        print(row)
        #print(row[1])
#if you want to print specific row,you use index

