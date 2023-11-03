# rotate array by k shifts
def rotateK(arr,k):
    n=len(arr)

    n=k%n
    return arr[n:]+arr[:k]

print(rotateK([1,2,3,4,5],2))
    