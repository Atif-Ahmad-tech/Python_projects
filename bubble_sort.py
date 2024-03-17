
# bubble sort algorithms

def BubbleSort(array):
  for i in range(len(array)):
    for j in range(0, len(array) - i - 1):
      if array[j] > array[j + 1]:
        # swapping elements 
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


data=[-2,4,6,78,98,-4]
BubbleSort(data)
print('Sorted Array in Ascending Order:')
print(data)
