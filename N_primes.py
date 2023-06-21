b=[1]
i=2
while b.index(b[-1])!=100: ## the 100 is DANGROUS is its a LARGE NUMBER
    prime = True
    for j in range(2,i):
        if i%j==0:
            prime = False
            break
    if prime is True:
        b.append(i)
       
        
    i+=1
print(b) ## output all the primes
print(b.index(b[-1])) # rotal primes number ina list