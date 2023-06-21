import csv
f = open('csv.csv')
csv_f = csv.reader(f)

####### 1st method
for row in csv_f: 
    Name, Age, Gender, Email, phone_number = row   # all list assign to variables in a line seprated by commas
    print("Name: {}, Age:{},Gender:{}, Email: {}, phone_number:{}".format(row[0], row[1], row[2], row[3], row[4]))

####### 2nd method
csv_f = csv.reader(f)
for row in csv_f: # 'row'--> list of all values in one line sep.. by comma
   print("Name: {}, Age:{},Gender:{}, Email: {}, phone_number:{}".format(row[0], row[1], row[2], row[3], row[4]))

f.close()