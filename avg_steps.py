import csv

infile = open('steps.csv', 'r')
outfile= open('avg.steps.csv','w')

csvfile = csv.reader(infile, delimiter= ',')
csvwriter=csv.writer(outfile)

next(csvfile) #this skips the first line

January = 0
February = 0
March = 0
April = 0
May = 0
June = 0
July = 0
August = 0 
September = 0
October = 0
November = 0
December = 0

for record in csvfile:
    if int(record[0]) ==1:
        jan_steps = int(record[1])
        January += jan_steps
        averagesteps_january= January/31
    elif int(record[0]) ==2:
        feb_steps = int(record[1])
        February += feb_steps
        averagesteps_february= February/28
    elif int(record[0]) ==3:
        march_steps = int(record[1])
        March += march_steps
        averagesteps_march = March/31
    elif int(record[0]) ==4:
        april_steps =int(record[1])
        April += april_steps
        averagesteps_april= April/30
    elif int(record[0]) == 5:
        may_steps = int(record[1])
        May += may_steps
        averagesteps_may = May/31
    elif int(record[0]) ==6:
        june_steps=int(record[1])
        June += june_steps
        averagesteps_june= June/30
    elif int(record[0]) ==7:
        july_steps=int(record[1])
        July += july_steps
        averagesteps_july = July/31
    elif int(record[0]) == 8:
        august_steps=int(record[1])
        August += august_steps
        averagesteps_august = August/31
    elif int(record[0]) ==9:
        september_steps=int(record[1])
        September += september_steps
        averagesteps_september = September/30
    elif int(record[0]) ==10:
        october_steps=int(record[1])
        October += october_steps
        averagesteps_october= October/31
    elif int(record[0]) == 11:
        november_steps = int(record[1])
        November += november_steps
        averagesteps_november = November/30
    elif int(record[0]) ==12:
        december_steps= int(record[1])
        December += december_steps
        averagesteps_december= December/31

csvwriter.writerow(['January', averagesteps_january])
csvwriter.writerow(['February', averagesteps_february])
csvwriter.writerow(['March', averagesteps_march])
csvwriter.writerow(['April', averagesteps_april])
csvwriter.writerow(['May', averagesteps_may])
csvwriter.writerow(['June', averagesteps_june])
csvwriter.writerow(['July', averagesteps_july])
csvwriter.writerow(['August', averagesteps_august])
csvwriter.writerow(['September', averagesteps_september])
csvwriter.writerow(['October', averagesteps_october])
csvwriter.writerow(['November', averagesteps_november])
csvwriter.writerow(['December', averagesteps_december])


infile.close()
outfile.close()
