import csv
from multiprocessing.resource_sharer import stop

infile = open('customers.csv', 'r')

outfile=open('customer_country.csv','w')

csvfile = csv.reader(infile, delimiter= ',')
outfile.write('Full Name, Country\n') 
next(csvfile) #this skips the first line
count=0
for record in csvfile:
    name= record[1]+' '+record[2]
    outfile.write(name)
    outfile.write(', ')
    outfile.write(record[4])
    outfile.write('\n')
    count+=1
outfile.write("Total number of customers: ")
outfile.write(str(count))

outfile.close
infile.close


