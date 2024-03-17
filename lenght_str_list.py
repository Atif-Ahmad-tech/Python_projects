# find lenght of each string in a list

list = ['university','github','programming','mail']

for i in list:
    lent=0
    for j in i:
        lent+=1
    print(f"length of '{i}' is: ", lent)