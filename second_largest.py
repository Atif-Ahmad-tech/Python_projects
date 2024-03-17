a=[2,3,6,7,8]
def larg(a):
    for i in a:
        for j in a:
            gr = 0
            if i>=j:
                continue
            else:
                gr = 1
                break 
        if gr ==0:
            return i
            break

def second(a):
    greatest = larg(a)
    for i in a:
        if  i ==greatest:
            continue
        for j in a:
            gr = 0
            if  j ==greatest:
                continue
            elif i>=j:
                continue
            else:
                gr = 1
                break 
        if gr ==0:
           return i
            break
second(a)