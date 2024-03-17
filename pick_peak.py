def pick_peaks(arr):
    pickPeak={'pos':[], 'peaks': []}
    n=len(arr)
    if n==0:
        return pickPeak
    
    for i in range(n-1):
        if i > 0 and i < n - 1 and arr[i-1]==arr[i] and arr[i+1]<=arr[i] :
            continue
        elif arr[i-1]<= arr[i] and arr[i+1]<= arr[i]:
            
            pickPeak['pos'].append(i)
            pickPeak['peaks'].append(arr[i])
    return pickPeak

print(pick_peaks([3,2,3,6,4,1,2,3,2,1,3,4,3,5,3,2,5,4,2,2,1]))
