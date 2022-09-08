import csv

infile = open('steps.csv', 'r')
outfile= open('avg.steps.csv','w')

csvfile = csv.reader(infile, delimiter= ',')

next(csvfile) #this skips the first line
Months=['Months', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
count=0
total=0
prev=1
month=0
average=0
while Months<13:
    for line in csvfile:
        while line[0]== prev:
            count+=1
            average=count/total
            



infile.close()
outfile.close()
