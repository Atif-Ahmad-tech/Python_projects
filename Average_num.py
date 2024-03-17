# finding average

x=int(input("How many number u want me to find the average?"))
z=[]
for i in range(1,x+1):
    print(f"Enter {i} number:")
    y=int(input())
    z.append(y)
    
print("the average of above numers is",sum(z)/len(z))