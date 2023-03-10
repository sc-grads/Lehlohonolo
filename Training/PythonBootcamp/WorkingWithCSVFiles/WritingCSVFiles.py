## Importing the module
import csv

# Opening people.csv in append-mode
with open('people.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)  # getting a csv.writer object
    csvdata = (5, 'Anne', 'Amsterdam')
    writer.writerow(csvdata)  # appending a line to the end file. csvdata is a tuple

# Opening numbers.csv in write-mode
# If you want to add multiple rows
with open('numbers.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['x', 'x**2', 'x**3', 'x**4'])
    for x in range(1, 101):
        writer.writerow([x, x ** 2, x ** 3, x ** 4])
