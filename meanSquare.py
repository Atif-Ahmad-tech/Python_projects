# given two arrays, find abasloute diference b/w two arrays corresponding elements diference, square it and then find average of these
def solution(array_a, array_b):
    new=[]
    for i,j in zip(array_a,array_b):
        new.append((abs(i-j)**2))
    
    return sum(new)/len(array_a)

print(solution(array_a=[1,2,3],array_b=[4,5,6]))
