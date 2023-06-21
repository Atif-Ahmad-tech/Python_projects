## program to prints a new list containing only the common elements between the two lists.


l1 = [1,2,3,4,87,998]
l2 = [9,7,3,1,2,87]
l3 = []
for i in l1:
    for j in l2:
        if i==j:
            l3.append(i)
print(f"The common element in {l1} and {l2} are: ",l3)
