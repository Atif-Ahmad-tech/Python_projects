# comment out one method. first method to explicitly close files
file = open('csv.txt')
print(file.read())

file.close()

###### another method automatically close the files 
with open('csv.txt') as file:
    print(file.readline())     #readline for one-line
