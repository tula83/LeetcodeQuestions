def secondLargest(arr):
    n=len(arr)
    max=arr[0]
    secondmax=-9999

    for i in range(1,n):
        if arr[i]>max:
            secondmax=max
            max=arr[i]
        elif arr[i]>secondmax and secondmax!=max:
            secondmax=arr[i]
    if secondmax==-9999:
        return "not second largest"
    return secondmax
print(secondLargest([1,2,3,45,3]))