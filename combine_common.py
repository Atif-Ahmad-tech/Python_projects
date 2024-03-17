## program to prints a new list containing only the common elements between the two lists.

l_1 = [1,2,3,4,5]
l_2 = [7,6,5,4,3]
l_3 = []
for i in l_2:
    if i in l_1:
        l_3.append(i)
    
print(f"The common element in {l_1} and {l_2} are: ",l_3)
