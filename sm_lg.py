
#### finding max,min and average

def max(list):
    for i in list:
        max=True
        # for j in range(list[j],list[len(list)-1]):
        for j in list:
            if list.index(i) == list.index(j):
                continue
            elif i<j:
                max=False
                break
        if max == True:
            print(i)     
            break
             
def min(list):
    for i in list:
        min=True
        # for j in range(list[j],list[len(list)-1]):
        for j in list:
            if list.index(i) == list.index(j):
                continue
            elif i>j:
                min=False
                break
        if min == True:
            print(i)
            break
            
def avg(list):
    avg=0
    for i in list:
        avg+=i
    
    print(avg/len(list))
        
nums = [7,6,99,3,2,5,2,7,7,8,9,5,3]
min(nums)
max(nums)
avg(nums)