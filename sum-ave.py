def f(name):
    sum = 0
    for i in name:
        sum += i
    average = sum / len(name)
    minimum = min(name)
    maximum = max(name)
    return sum, average, minimum, maximum


sum, average, minimum, maximum = f([10, 20, 30, 40, 50, 60])
print(sum)
print(average)
print(minimum)
print(maximum)
