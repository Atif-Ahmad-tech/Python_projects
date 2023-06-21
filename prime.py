a = [i for i in range(2,100)]
b = []

for i in a:
    prime = True
    for j in range(2,i):
        if i%j==0:
            prime = False
            break
    if prime is True:
        b.append(i)
        
print(b) # output all the numbers as a lists
print(b.index(b[-1])) ## output the total size of list

