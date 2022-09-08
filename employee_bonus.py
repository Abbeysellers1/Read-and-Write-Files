import csv
from multiprocessing.resource_sharer import stop

infile = open('EmployeePay.csv', 'r')

csvfile = csv.reader(infile, delimiter= ',')

next(csvfile) #this skips the first line

for record in csvfile:
    print("Employee ID:", record[0])
    print("First Name:", record[1])
    print("Last Name: ", record[2])
    print('Salary:', record[3])
    print('Bonus:', record[4])
    print()
