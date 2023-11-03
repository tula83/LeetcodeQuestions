# finding leaders in array 

def find_leaders(arr):
    n=len(arr)
    max=arr[n-1]
    leaders=[]
    leaders.insert(0,arr[n-1])

    for i in range(n-2,-1,-1):
        if arr[i]>max:
            max=arr[i]
            leaders.insert(0,max)
    return leaders


print(f'leaders in array are {find_leaders([6,7,9,4])}')
