strn = "This is my sentence"
done = []
for i in strn.lower():
    if i in done:
        continue
    elif i==' ':
        continue
    num=0
    for j in strn.lower():
        if i==j:
            num+=1
    done.append(i)
    print(i,"occur" ,num," Times")