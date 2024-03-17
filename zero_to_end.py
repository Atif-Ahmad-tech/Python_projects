# def move_zeros(arr):
#     non_zero_count = 0
#     n = len(arr)

#     # Traverse the array
#     for i in range(n):
#         if arr[i] != 0:
#             # If the element is non-zero, move it to the front
#             arr[non_zero_count] = arr[i]
#             non_zero_count += 1

#     # Fill the remaining positions with zeros
#     while non_zero_count < n:
#         arr[non_zero_count] = 0
#         non_zero_count += 1

#     return arr
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))

print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))