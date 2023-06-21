def inversion(list):
    k=0
    # print(list[-2])
    for i in range(list[-2]):
        for j in range(i+1,list[-1]):
            if list[i]>list[j]:
                k+=1
        # if i==list[-2]:
        #     break
    print(k)
list = [2,4,3,5,6,9,7]
# print(list.index(1+2))
inversion(list)
