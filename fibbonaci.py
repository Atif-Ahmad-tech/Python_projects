x=[0,1]
n=31
for i in range(2, n+1):
    x.append(x[i-1] + x[i-2])
print(x[31]) 

